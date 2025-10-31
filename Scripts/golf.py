import streamlit as st
import joblib
import pandas as pd
from cloud import load_all_pickles_for_sport
from google.oauth2 import service_account

def golf_model():
    secrets = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(secrets)
    bucket_name = "olympics-2025"
    golf_models = load_all_pickles_for_sport("Golf", bucket_name, credentials)

    # Try to load all required objects
    model_men = golf_models.get("golf_model", {}).get("men")
    model_women = golf_models.get("golf_model", {}).get("women")

    scaler_result_men = golf_models.get("scaler_result", {}).get("men")
    scaler_result_women = golf_models.get("scaler_result", {}).get("women")

    scaler_weight_men = golf_models.get("scaler_weight", {}).get("men")
    scaler_weight_women = golf_models.get("scaler_weight", {}).get("women")

    country_count_men = golf_models.get("country_count", {}).get("men", {})
    country_count_women = golf_models.get("country_count", {}).get("women", {})

    max_rank_men = golf_models.get("max_rank", {}).get("men")
    max_rank_women = golf_models.get("max_rank", {}).get("women")

    # Validate availability
    if not all([model_men, model_women, scaler_result_men, scaler_result_women,
                scaler_weight_men, scaler_weight_women]):
        st.error("🚫 Required model files could not be loaded. Please check GCS bucket structure.")
        return

    # Function to assign start weight
    def assign_start_weight(start_order):
        if start_order <= 10:
            return 0.80
        elif start_order <= 20:
            return 0.85
        elif start_order <= 30:
            return 0.90
        elif start_order <= 40:
            return 0.95
        else:
            return 1

    # Function to assign country weight
    def assign_country_weight(country_count):
        if country_count >= 20:
            return 0.85
        elif country_count >= 15:
            return 0.90
        elif country_count >= 10:
            return 0.95
        else:
            return 1

    # Streamlit app
    st.title("🏌️ Golf Tournament Finishing Position Predictor")

    st.markdown("""
    This app predicts a golfer's finishing position based on:
    - Gender
    - Country representation
    - Starting position
    - Tournament score
    """)

    # User inputs
    gender = st.radio("Player Gender", ('M', 'W'), horizontal=True)
    country = st.text_input("Country Code (e.g., USA, JPN)", "USA").upper()
    start_order = st.slider("Starting Position", 1, 100, 15)
    result = st.number_input("Player's Score (Result)", min_value=60.0, max_value=200.0, value=72.0, step=0.1)

    if st.button("Predict Finishing Position"):
        # Assign weights
        start_weight = assign_start_weight(start_order)
        
        if gender == 'M':
            country_count = country_count_men.get(country, 0)
            country_weight = assign_country_weight(country_count)
        else:
            country_count = country_count_women.get(country, 0)
            country_weight = assign_country_weight(country_count)
        
        total_weight = country_weight * start_weight
        
        # Scale inputs
        if gender == 'M':
            result_scaled = scaler_result_men.transform([[result]])[0][0]
            weight_scaled = scaler_weight_men.transform([[total_weight]])[0][0]
            model = model_men
        else:
            result_scaled = scaler_result_women.transform([[result]])[0][0]
            weight_scaled = scaler_weight_women.transform([[total_weight]])[0][0]
            model = model_women
        
        # Compute final score
        final_score = result_scaled * 0.9 + weight_scaled * 0.1
        
        # Predict
        user_data = pd.DataFrame([[final_score]], columns=['final_score'])
        with st.spinner("Model initiated",show_time=True):
            predicted_rank_inverted = model.predict(user_data)[0]
        predicted_rank = -predicted_rank_inverted
        
        # Display results
        st.subheader("Prediction Results")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Predicted Finishing Position", f"{round(predicted_rank)}")
        with col2:
            st.metric("Performance Score", f"{final_score:.4f}")
        
        st.subheader("Weight Breakdown")
        st.write(f"- **Country Representation Weight**: {country_weight:.2f} (from {country_count} players)")
        st.write(f"- **Starting Position Weight**: {start_weight:.2f}")
        st.write(f"- **Total Weight Factor**: {total_weight:.2f}")
        
        st.info("ℹ️ Lower finishing positions indicate better performance (1st place is best)")

if __name__=="__main__":
    golf_model()
