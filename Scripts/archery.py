import streamlit as st
import joblib
import numpy as np
import pandas as pd
from cloud import load_all_pickles_for_sport
from google.oauth2 import service_account

def assign_start_weight(start_order):
    if start_order <= 10: return 1.0
    elif start_order <= 20: return 0.95
    elif start_order <= 30: return 0.90
    elif start_order <= 40: return 0.85
    else: return 0.80

def archery_model():
    secrets = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(secrets)
    bucket_name = "olympics-2025"
    archery_models = load_all_pickles_for_sport("Archery", bucket_name, credentials)

    # Extract models and scalers
    model_men = archery_models.get("model", {}).get("men")
    model_women = archery_models.get("model", {}).get("women")
    model_mixed = archery_models.get("model", {}).get("mixed")

    scaler_men = archery_models.get("scaler", {}).get("men")
    scaler_women = archery_models.get("scaler", {}).get("women")
    scaler_mixed = archery_models.get("scaler", {}).get("mixed")
    
    st.title("🏹 Archery Final Rank Predictor")
    st.markdown("Estimate an archer or team's final rank based on performance and metadata.")
    # Country weights (sample values)
    country_weights = {
        'M': {'KOR': 1.2, 'USA': 1.1, 'NED': 1.1, 'TPE': 1.1},
        'W': {'KOR': 1.3, 'CHN': 1.2, 'USA': 1.1},
        'X': {'KOR': 1.3, 'USA': 1.1, 'NED': 1.1}
    }

    # Inputs
    gender = st.radio("Select Gender", ['M', 'W', 'X'], format_func=lambda x: {'M': 'Men', 'W': 'Women', 'X': 'Mixed'}[x])
    country = st.text_input("Enter Country Code (e.g., USA, KOR)", value="USA").upper()
    start_order = st.slider("Start Order", 1, 64, 10)
    qualification_score = st.number_input("Qualification Score", min_value=0.0, step=0.1)

    st.markdown("#### Elimination Rounds (1 = Win, 0 = Lose)")
    win_32 = st.radio("1/32 Elimination", [1, 0], horizontal=True)
    win_16 = st.radio("1/16 Elimination", [1, 0], horizontal=True)
    win_8 = st.radio("1/8 Elimination", [1, 0], horizontal=True)
    win_qf = st.radio("Quarterfinal", [1, 0], horizontal=True)
    win_sf = st.radio("Semifinal", [1, 0], horizontal=True)
    win_final = st.radio("Final", [1, 0], horizontal=True)

    if st.button("Predict Final Rank"):
        # Stage weights
        stage_weights = {
            '1/32 Elimination Round': 1.2,
            '1/16 Elimination Round': 1.5,
            '1/8 Elimination Round': 2.0,
            'Quarterfinal': 3.0,
            'Semifinal': 4.0,
            'Final': 6.0
        }

        # Elimination score
        elim_score = (
            win_32 * stage_weights['1/32 Elimination Round'] +
            win_16 * stage_weights['1/16 Elimination Round'] +
            win_8 * stage_weights['1/8 Elimination Round'] +
            win_qf * stage_weights['Quarterfinal'] +
            win_sf * stage_weights['Semifinal'] +
            win_final * stage_weights['Final']
        )

        start_weight = assign_start_weight(start_order)
        country_weight = country_weights.get(gender, {}).get(country, 1.0)

        composite_score = qualification_score + elim_score + (start_weight * country_weight)
        X_input = np.array([[composite_score]])

        # Choose the right model/scaler
        if gender == 'M':
            model = model_men
            scaler = scaler_men
        elif gender == 'W':
            model = model_women
            scaler = scaler_women
        else:
            model = model_mixed
            scaler = scaler_mixed

        X_scaled = scaler.transform(X_input)
        with st.spinner("Model initiated",show_time=True):
            predicted_rank = model.predict(X_scaled)[0]

        # Determine medal
        if predicted_rank <= 1:
            medal = "🥇 Gold Medal"
        elif predicted_rank <= 2:
            medal = "🥈 Silver Medal"
        elif predicted_rank <= 4:
            medal = "🥉 Bronze Medal"
        else:
            medal = "🎯 No Medal"

        # Results
        st.subheader("📊 Prediction Summary")
        st.metric("Predicted Rank", f"{int(round(predicted_rank))}")
        st.metric("Medal Status", medal)
        st.metric("Composite Score", f"{composite_score:.2f}")
        st.caption("Note: Lower rank = better position (1 is the best).")

if __name__ == "__main__":
    archery_model()
