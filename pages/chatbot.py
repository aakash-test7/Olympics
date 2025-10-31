import streamlit as st
import google.generativeai as genai
import time

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding-bottom: 0rem;
    }
    
    /* Remove extra padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100vh;
    }
    
    /* Chat message styling */
    .stChatMessage {
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
    }
    
    /* User message background */
    [data-testid="stChatMessageContent"] {
        background-color: transparent;
    }
    
    /* Input box styling - remove fixed positioning */
    .stChatInputContainer {
        padding: 1rem 0;
        background-color: transparent;
    }
    
    /* Header styling */
    h1 {
        color: #1f77b4;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #1f77b4;
        margin-bottom: 1rem;
    }
    
    /* Caption styling */
    .stCaption {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 2rem;
    }
    
    /* Scrollable chat container */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        overflow-y: auto;
    }
    
    /* Warning/Error styling */
    .stAlert {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Make the chat area fill available space */
    section[data-testid="stChatFloatingInputContainer"] {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: linear-gradient(to top, white 80%, transparent);
        padding-top: 1rem;
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# Configure Gemini with your API key
gemini_key = st.secrets["gemini_api_key"]["GEMINI_API_KEY"]
genai.configure(api_key=gemini_key)

def handle_rate_limit():
    st.session_state.rate_limit_exceeded = True
    current_time = time.time()
    time_since_last_request = current_time - st.session_state.last_request_time
    
    # Progressive backoff
    wait_time = max(5, min(30, time_since_last_request * 2))  # Between 5-30 seconds
    
    with st.spinner(f"⏳ Rate limit exceeded. Waiting {int(wait_time)} seconds..."):
        time.sleep(wait_time)
    st.session_state.rate_limit_exceeded = False
    st.session_state.last_request_time = time.time()
    st.rerun()

def get_gemini_response(prompt):
    try:
        messages = []
        for m in st.session_state.messages:
            if m["role"] == "system":
                continue
            messages.append({"role": m["role"], "parts": [m["content"]]})

        model = genai.GenerativeModel(
            'gemini-2.5-pro',
            system_instruction="""You are an expert Olympic historian. Provide detailed information about:
            - Olympic history, athletes, and events
            - Medal statistics and records
            - Future Olympic plans
            Be accurate and concise. If unsure about something, say so."""
        )

        chat = model.start_chat(history=messages)
        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower() or "rate" in error_msg.lower():
            handle_rate_limit()
            return None
        else:
            st.error(f"Error: {error_msg}")
            return None

def chat_page():
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "model", "content": "🏆 Welcome to the Olympics Chatbot! Ask me anything about Olympic history, athletes, events, records, and future games!"}
        ]
    if "rate_limit_exceeded" not in st.session_state:
        st.session_state.rate_limit_exceeded = False
    if "last_request_time" not in st.session_state:
        st.session_state.last_request_time = 0

    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🏆 Olympics Chatbot")
        st.caption("💻 Built by Aakash Kharb | GoogleCloudProjects")
    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "model", "content": "🏆 Welcome to the Olympics Chatbot! Ask me anything about Olympic history, athletes, events, records, and future games!"}
            ]
            st.rerun()
    
    st.markdown("---")
    
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "model":
            with st.chat_message("model", avatar="🏅"):
                st.markdown(message["content"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Ask me about the Olympics... (e.g., 'Who won the most gold medals in 2024?')"):
        if st.session_state.rate_limit_exceeded:
            st.warning("⏳ Please wait a moment before sending another message.")
            st.stop()
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Display model response
        with st.chat_message("model", avatar="🏅"):
            with st.spinner("Thinking..."):
                # Record request time
                st.session_state.last_request_time = time.time()
                
                # Get Gemini response
                full_response = get_gemini_response(prompt)
                
                if full_response is None:
                    full_response = "⚠️ I'm experiencing some technical difficulties. Please try again in a moment."
                
                st.markdown(full_response)
        
        # Add model response to chat history
        st.session_state.messages.append({"role": "model", "content": full_response})
        st.rerun()

if __name__ == "__main__":
    chat_page()