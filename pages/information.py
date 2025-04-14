import streamlit as st
from cloud import show_info_athlete,show_info_coach,show_info_technical_official

def info_page():
    # Initialize session state variables if they don't exist
    if 'show_athlete' not in st.session_state:
        st.session_state.show_athlete = False
    if 'show_coach' not in st.session_state:
        st.session_state.show_coach = False
    if 'show_technical' not in st.session_state:
        st.session_state.show_technical = False

    # Create buttons in columns for better layout
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Athlete",use_container_width=True):
            # Reset other states and set athlete state to True
            st.session_state.show_athlete = True
            st.session_state.show_coach = False
            st.session_state.show_technical = False

    with col2:
        if st.button("Coach",use_container_width=True):
            # Reset other states and set coach state to True
            st.session_state.show_athlete = False
            st.session_state.show_coach = True
            st.session_state.show_technical = False

    with col3:
        if st.button("Technical Official",use_container_width=True):
            # Reset other states and set technical state to True
            st.session_state.show_athlete = False
            st.session_state.show_coach = False
            st.session_state.show_technical = True

    # Call the appropriate function based on session state
    if st.session_state.show_athlete:
        show_info_athlete()
    elif st.session_state.show_coach:
        show_info_coach()
    elif st.session_state.show_technical:
        show_info_technical_official()
    return

if __name__=="__main__":
    info_page()