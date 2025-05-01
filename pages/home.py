import streamlit as st

def home_page():
    # Basic CSS for styling
    st.markdown("""
    <style>
    .feature-card {
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        background: #F5F9FF;
        border: 1px solid #ddd;
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        background: #fff;
    }
    .center-title {
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
        font-size: 2.2rem;
    }
    .footer {
        background-color: #000;
        color: #fff;
        text-align: center;
        padding: 1rem 0;
        margin-top: 3rem;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Centered title
    st.markdown('<h1 class="center-title" style="font-size: 8rem;">TECHWILL x OLYMPICS</h1>', unsafe_allow_html=True)

    # Project Overview
    con=st.container(border=True, key="con12hp")
    st.markdown("""<style>.stVerticalBlock.st-key-con12hp {background-color: rgba(61, 204, 219,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con12hp:hover {background-color: rgba(61, 204, 219,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con.markdown("## 📘 Project Overview")
    con.markdown("""
A feature-rich, cloud-integrated web application offering real-time data exploration, medal prediction, and a Gemini-powered chatbot for the Paris 2024 Olympics.

- 📊 **Explore Olympic Data**: Access structured data for athletes, events, and medals.
- 🥇 **Medal Predictions**: Simulate outcomes using past trends and AI logic.
- 🤖 **AI Chatbot**: Retrieve insights about schedules, venues, and sports rules.
- ☁️ **Cloud-Powered**: Hosted on Google Cloud for high scalability and reliability.
    """)

    # Key Features
    con=st.container(border=True, key="con13hp")
    st.markdown("""<style>.stVerticalBlock.st-key-con13hp {background-color: rgba(61, 204, 219,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con13hp:hover {background-color: rgba(61, 204, 219,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con.markdown("## 🚀 Key Features")
    col1, col2 = con.columns(2)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Data Visualization</h4>
            <p>Dynamic visuals for medals, athletes, and event stats.</p>
        </div>
        <div class="feature-card">
            <h4>☁️ Cloud Integration</h4>
            <p>GCP-hosted datasets accessed via `cloud.py` module.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 Gemini Chatbot</h4>
            <p>Context-aware answers on Olympic events and participants.</p>
        </div>
        <div class="feature-card">
            <h4>📈 Medal Predictions</h4>
            <p>Simulate outcomes with athlete/event-level insights.</p>
        </div>
        """, unsafe_allow_html=True)

    # Tech Stack
    con=st.container(border=True, key="con14hp")
    st.markdown("""<style>.stVerticalBlock.st-key-con14hp {background-color: rgba(61, 204, 219,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con14hp:hover {background-color: rgba(61, 204, 219,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    with con:
        st.markdown("## 🧰 Tech Stack")
        tech_stack = st.columns(4)
        tech_stack[0].markdown("🔹 **Python**")
        tech_stack[1].markdown("🔹 **Streamlit**")
        tech_stack[2].markdown("🔹 **Google Cloud**")
        tech_stack[3].markdown("🔹 **Gemini AI**")

        # Repo structure
        st.markdown("## 🗂️ Repository Structure")
        st.code("""
    Olympics/
    ├── app.py                # Main entry point
    ├── cloud.py              # GCS integration
    ├── pages/
    │   ├── home.py
    │   ├── dataset_page.py
    │   ├── prediction.py
    │   ├── chatbot.py
    │   ├── information.py
    |   └── tutorial.py          
    └── scripts/
        ├── archery.py
        ├── golf.py
        └── wrestling.py
        """)

    # Footer
    st.markdown("""
    <div class="footer">
        © Aakash Kharb
    </div>
    """, unsafe_allow_html=True)

# Run the page
if __name__ == "__main__":
    home_page()
