
import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .stApp {
        background: #0e1117;
    }

    header {
        background: transparent !important;
    }

    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #9ca3af;
        font-size: 15px;
        margin-bottom: 30px;
    }

    .user-message {
        background: #263449;
        color: white;
        padding: 14px 18px;
        border-radius: 18px 18px 4px 18px;
        margin: 12px 0 12px auto;
        max-width: 75%;
        width: fit-content;
        font-size: 16px;
        line-height: 1.6;
    }

    .bot-message {
        background: #1c2330;
        color: #e5e7eb;
        padding: 14px 18px;
        border-radius: 18px 18px 18px 4px;
        margin: 12px auto 12px 0;
        max-width: 85%;
        width: fit-content;
        font-size: 16px;
        line-height: 1.7;
    }

    .stChatInput {
        border-radius: 15px;
    }

    [data-testid="stSidebar"] {
        background-color: #151b26;
    }

    .sidebar-title {
        font-size: 23px;
        font-weight: bold;
        color: white;
        padding-bottom: 15px;
    }

    .status {
        color: #22c55e;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- CONFIGURATION ----------------
API_URL = "http://127.0.0.1:8000/my-chatbot"


# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 My AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status">● AI Assistant Interface</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("➕  New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("🗑️  Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### About")
    st.caption(
        "Your personal AI chatbot powered by "
        "FastAPI and a Large Language Model."
    )

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")


# ---------------- MAIN HEADER ----------------
st.markdown(
    '<div class="main-title">🤖 AI Chat Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Your intelligent assistant. Ask anything and start a conversation!'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- WELCOME SCREEN ----------------
if not st.session_state.messages:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; padding:30px;">
            <div style="font-size:55px;">💬</div>
            <h2 style="color:white;">How can I help you today?</h2>
            <p style="color:#9ca3af;">
                Start a conversation by typing your message below.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- DISPLAY CHAT HISTORY ----------------
for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message("user", avatar="👤"):
            st.markdown(message["content"])

    else:

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message["content"])


# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Message your AI assistant...")


# ---------------- HANDLE USER MESSAGE ----------------
if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Get chatbot response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("AI is thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"message": user_input},
                    timeout=120
                )

                response.raise_for_status()

                bot_response = response.json()["response"]

            except requests.exceptions.ConnectionError:
                bot_response = (
                    "⚠️ Cannot connect to the FastAPI server. "
                    "Please make sure your backend is running."
                )

            except requests.exceptions.Timeout:
                bot_response = (
                    "⏳ The request timed out. Please try again."
                )

            except requests.exceptions.RequestException as e:
                bot_response = f"⚠️ API Error: {str(e)}"

            except (ValueError, KeyError):
                bot_response = (
                    "⚠️ Invalid response received from the backend."
                )

        st.markdown(bot_response)

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
