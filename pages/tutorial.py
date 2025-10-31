import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from datetime import timedelta

def tutorial_page():
    st.title("Tutorials Page")
    st.write("**Learn how to use this interface**")
    
    secrets = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(secrets)
    client = storage.Client(credentials=credentials)

    @st.cache_data(ttl=1800)  # cache for 30 minutes (1800 seconds)
    def generate_signed_url(blob_name, expiration_minutes=30):
        """Generate a signed URL for temporary access to a GCS object"""
        try:
            bucket = client.bucket("olympics-2025")
            blob = bucket.blob(blob_name)
            
            if not blob.exists():
                return None
                
            url = blob.generate_signed_url(
                version="v4",
                expiration=timedelta(minutes=expiration_minutes),
                method="GET"
            )
            return url
        except Exception as e:
            st.error(f"Error generating signed URL: {str(e)}")
            return None

    # List of video files
    video_files = [
        "Videos/video1.mp4",
        "Videos/video2.mp4",
        "Videos/video3.mp4",
        "Videos/video4.mp4",
    ]

    for video in video_files:
        video_url = generate_signed_url(video)
        if video_url:
            st.video(video_url, start_time=0)
        else:
            st.warning(f"Could not generate streaming URL for {video}")

if __name__ == "__main__":
    tutorial_page()
