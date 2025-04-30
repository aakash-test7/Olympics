import streamlit as st

def home_page():    
        
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    
    .main-title {
        font-size: 8rem; /* Increased for greater emphasis */
        font-weight: 900;
        background: linear-gradient(90deg, #8B8000, #555555, #6A3805); /* Darker gold/silver/bronze tones */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        letter-spacing: 0.05em;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .feature-card {
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        background: rgba(255,255,255,0.2);
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section with animated title
    st.markdown('<h1 class="main-title pulse">TECHWILL X OLYMPICS</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <p style="font-size: 1.2rem; color: #666;">Future Games Begin Here</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Feature Showcase
    with st.container():
        st.markdown("## 🚀 Interactive Features")
        cols = st.columns(3)
        
        with cols[0]:
            with st.expander("🏅 **Medal Prediction Engine**", expanded=True):
                st.markdown("""
                - Forecast medal counts by country
                - Athlete performance predictions
                - Real-time probability scoring
                """)
                #st.image("https://via.placeholder.com/300x150?text=Prediction+Dashboard", use_column_width=True)
        
        with cols[1]:
            with st.expander("🤖 **Olympic AI Assistant**", expanded=True):
                st.markdown("""
                - Gemini-powered natural queries
                - Historical facts on demand
                - Comparative analysis
                """)
                #st.image("https://via.placeholder.com/300x150?text=AI+Chat+Interface", use_column_width=True)
        
        with cols[2]:
            with st.expander("📊 **Data Explorer**", expanded=True):
                st.markdown("""
                - Interactive timeline (1896-2024)
                - Country comparison tools
                - Athlete career visualization
                """)
                #st.image("https://via.placeholder.com/300x150?text=Data+Viz+Tools", use_column_width=True)
    
    # Innovation Highlights
    st.markdown("---")
    st.markdown("## ✨ What Makes Us Different")
    
    innovation_cols = st.columns(2)
    
    with innovation_cols[0]:
        st.markdown("""
        <div class="feature-card">
            <h3>🏟️ Virtual Olympic Museum</h3>
            <p>Explore historical moments through immersive storytelling and AI-reconstructed footage</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 Predictive Neural Engine</h3>
            <p>Our custom ML models analyze 200+ factors to forecast future Olympic trends</p>
        </div>
        """, unsafe_allow_html=True)
    
    with innovation_cols[1]:
        st.markdown("""
        <div class="feature-card">
            <h3>🌐 Global Impact Analysis</h3>
            <p>Measure how host cities transform economically and socially post-Olympics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>⏱️ Real-Time Medal Alerts</h3>
            <p>Get live updates during games with historical context for each result</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("---")
    cta_cols = st.columns([1,2,1])
    with cta_cols[1]:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px;">
            <h2>Ready to Explore Olympic Information</h2>
            <p>Aakash Kharb</p>
            <button style="background: linear-gradient(90deg, #FFD700, #C0C0C0); border: none; padding: 0.75rem 2rem; border-radius: 30px; font-weight: bold; margin-top: 1rem;">Launch Dashboard</button>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()
