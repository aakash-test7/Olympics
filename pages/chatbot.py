import streamlit as st
import google.generativeai as genai
import time

# Configure Gemini with your API key
gemini_key = st.secrets["gemini_api_key"]["GEMINI_API_KEY"]
genai.configure(api_key=gemini_key)

def handle_rate_limit():
    st.session_state.rate_limit_exceeded = True
    current_time = time.time()
    time_since_last_request = current_time - st.session_state.last_request_time
    
    # Progressive backoff
    wait_time = max(5, min(30, time_since_last_request * 2))  # Between 5-30 seconds
    
    with st.spinner(f"⏳ Rate limit exceeded. Waiting {wait_time} seconds..."):
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
            'gemini-1.5-pro-latest',  # Updated model name
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
        st.error(f"Error: {str(e)}")
        handle_rate_limit()
        return None

def chat_page():
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "TechWill x Olympics !!! Ask anything about Olympics "}
        ]
    if "rate_limit_exceeded" not in st.session_state:
        st.session_state.rate_limit_exceeded = False
    if "last_request_time" not in st.session_state:
        st.session_state.last_request_time = 0

    st.title("🏆 Olympics Chatbot 🤖")
    st.caption("Aakash Kharb - GoogleCloudProjects")
    
    for message in st.session_state.messages:
        avatar = "🏅" if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Ask me about the Olympics..."):
        if st.session_state.rate_limit_exceeded:
            st.warning("Please wait a moment before sending another message.")
            st.stop()
            
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant", avatar="⚙️"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Record request time
            st.session_state.last_request_time = time.time()
            
            # Get Gemini response
            full_response = get_gemini_response(prompt)
            
            if full_response is None:
                message_placeholder.markdown("⚠️ Unable to get response. Please try again later.")
            else:
                message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history if successful
        if full_response:
            st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    chat_page()
