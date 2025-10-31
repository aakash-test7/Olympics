import streamlit as st
import pandas as pd
import joblib
import numpy as np
from google.cloud import storage
from google.oauth2 import service_account
import io
from cloud import read_excel_from_gcs
from cloud import wrestling_df

# Function to load the model from Google Cloud Storage (GCS)
def load_pickles_from_gcs(bucket_name, blob_name, credentials):
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_bytes()
    return joblib.load(io.BytesIO(data))

# Load the simulated ranking model from GCS
def load_simulation_model_from_gcs(bucket_name, gcs_path, credentials):
    return load_pickles_from_gcs(bucket_name, gcs_path, credentials)

# Function to simulate ranking
def simulate_event(event_df):
    results = {}
    for _, row in event_df.iterrows():
        winner = row['participant_code'] if row['result_WLT'] == 'W' else None
        loser = row['participant_code'] if row['result_WLT'] == 'L' else None

        for code in [winner, loser]:
            if code and code not in results:
                results[code] = {'wins': 0, 'losses': 0}

        if winner:
            results[winner]['wins'] += 1
        if loser:
            results[loser]['losses'] += 1

    active = {k: v for k, v in results.items() if v['losses'] == 0}
    ranking = sorted(active.items(), key=lambda x: x[1]['wins'], reverse=True)
    return ranking

# Compute rank for user
def compute_user_rank(user_code, user_results, event_df, ranking_model):
    user_df = pd.DataFrame(user_results, columns=['round', 'result_WLT'])

    wins = (user_df['result_WLT'] == 'W').sum()
    losses = (user_df['result_WLT'] == 'L').sum()

    if losses > 0:
        return "Eliminated", wins, losses

    simulated_df = event_df.copy()

    # Create DataFrame for user rounds to concat
    user_rounds_df = pd.DataFrame([{
        'participant_code': user_code,
        'result_WLT': row['result_WLT']
    } for _, row in user_df.iterrows()])

    # Concatenate instead of append
    simulated_df = pd.concat([simulated_df, user_rounds_df], ignore_index=True)

    # Use the loaded ranking model
    ranking = ranking_model
    rank = next((i + 1 for i, (code, _) in enumerate(ranking) if code == user_code), "Not Found")
    
    return rank, wins, losses

# Streamlit app
def wrestling_model():
    secrets = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(secrets)
    bucket_name = "olympics-2025"
    gcs_path = 'Model/Wrestling/simulated_ranking_model.pkl'

    # Load the model from GCS
    ranking_model = load_simulation_model_from_gcs(bucket_name, gcs_path, credentials)

    st.title("🏅 Olympic Wrestling Rank Predictor 🥇")
    st.markdown("Estimate a wrestler or team's final rank based on performance and metadata.")

    # Event selection
    st.markdown("### Available Events:")
    event_choices = list(wrestling_df['event_code'].unique())
    event_choice = st.selectbox("Select an Event", event_choices)

    user_code = st.text_input("Enter Participant Code (e.g., '1543088')")
    num_rounds = st.number_input("Enter number of rounds you participated in", min_value=1, max_value=10, step=1)

    user_results = []
    for i in range(num_rounds):
        result = st.radio(f"Result for Round {i+1} (W/L)", ['W', 'L'], key=f'round_{i+1}')
        user_results.append((f"Round {i+1}", result))

    if st.button("Predict Rank"):
        rank, wins, losses = compute_user_rank(user_code, user_results, wrestling_df[wrestling_df['event_code'] == event_choice], ranking_model)

        # Display results
        st.subheader("📊 Prediction Results")

        if isinstance(rank, (int, float)):
            st.metric("Predicted Rank", f"{int(round(rank))}")
        elif rank == "Eliminated":
            st.metric("Predicted Rank", "Eliminated")
        else:
            st.metric("Predicted Rank", str(rank))  # Fallback for any other case

        st.metric("Wins", wins)
        st.metric("Losses", losses)

        # Medal determination
        if rank == "Eliminated":
            st.markdown("**Status**: Eliminated")
        elif isinstance(rank, (int, float)):  # Only compare if rank is numeric
            if rank <= 1:
                st.markdown("**Medal**: 🥇 Gold Medal")
            elif rank <= 2:
                st.markdown("**Medal**: 🥈 Silver Medal")
            elif rank <= 4:
                st.markdown("**Medal**: 🥉 Bronze Medal")
            else:
                st.markdown("**Medal**: 🎯 No Medal")
        else:
            st.markdown("**Medal**: 🎯 No Medal")  # Fallback for unexpected rank types

if __name__ == "__main__":
    wrestling_model()
