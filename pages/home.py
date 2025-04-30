import streamlit as st

def home_page():    
        
    st.markdown("""
    <style>
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
    
    # University Header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <h2>UNIVERSITY INSTITUTE OF ENGINEERING & TECHNOLOGY</h2>
        <h3>MAHARSHI DAYANAND UNIVERSITY, ROHTAK</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Title Section
    st.markdown('<h2 style="text-align: center;">LC-CSE-350G Project</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <p style="font-size: 1.2rem; color: #666;">Semester - 6th</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Information
    with st.container():
        cols = st.columns([1,1])
        with cols[0]:
            st.markdown("### Submitted To:")
            st.markdown("""
            <div style="padding: 1rem; background: #f0f2f6; border-radius: 10px;">
                <p><b>Dr. Yogesh</b></p>
                <p><b>⠀</b></p>
                <p><b>⠀</b></p>
            </div>
            """, unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown("### Submitted By:")
            st.markdown("""
            <div style="padding: 1rem; background: #f0f2f6; border-radius: 10px;">
                <p><b>Aakash</b></p>
                <p><b>Roll No:</b> 2080033</p>
                <p><b>Program:</b> B.Tech. AIML</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Project Features
    st.markdown("---")
    st.markdown("## 🚀 Project Features")
    
    with st.expander("📚 Project Overview", expanded=True):
        st.markdown("""
        This academic project demonstrates the application of:
        - Cloud computing concepts using Google Cloud Platform
        - Data analysis and visualization techniques
        - Machine learning for predictive modeling
        - Streamlit for interactive web applications
        """)
    
    feature_cols = st.columns(2)
    
    with feature_cols[0]:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Data Analysis</h3>
            <p>Comprehensive analysis of Olympic datasets with interactive visualizations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>☁️ Cloud Integration</h3>
            <p>Google Cloud Storage for dataset hosting and retrieval</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_cols[1]:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI Chatbot</h3>
            <p>Gemini-powered assistant for Olympic information retrieval</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Predictive Models</h3>
            <p>Medal prediction using machine learning algorithms</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown("---")
    st.markdown("## 🛠️ Technology Stack")
    tech_cols = st.columns(4)
    tech_cols[0].markdown("**Python**")
    tech_cols[1].markdown("**Streamlit**")
    tech_cols[2].markdown("**Google Cloud**")
    tech_cols[3].markdown("**Gemini AI**")
    
    # Academic Purpose Notice
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 10px;">
        <p><i>This project has been developed purely for academic purposes as part of the 6th semester curriculum at UIET, MDU Rohtak.</i></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()
