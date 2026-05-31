import streamlit as st

from app.services.chat_service import chat_service
from app.utils.file_validator import validate_file
from app.core.logger import app_logger


st.set_page_config(
    page_title="Enterprise Document Assistant",
    page_icon="📄",
    layout="wide",
)

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []


# -------------------------
# Sidebar
# -------------------------

with st.sidebar:
    st.title("System Status")

    st.success("Application Running")

    st.divider()

    st.subheader("Uploaded Files")

    if st.session_state.uploaded_files:
        for file_name in st.session_state.uploaded_files:
            st.write(f"• {file_name}")
    else:
        st.info("No files uploaded")


# -------------------------
# Main Page
# -------------------------

st.title("Enterprise Document Assistant")

st.markdown(
    """
    Upload enterprise documents and
    ask questions using natural language.
    """
)

# -------------------------
# File Upload
# -------------------------

uploaded_files = st.file_uploader(
    "Upload Documents",
    accept_multiple_files=True,
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        if validate_file(uploaded_file.name):

            if (
                uploaded_file.name
                not in st.session_state.uploaded_files
            ):
                st.session_state.uploaded_files.append(
                    uploaded_file.name
                )

            st.success(
                f"{uploaded_file.name} uploaded successfully."
            )

            app_logger.info(
                f"Uploaded file: {uploaded_file.name}"
            )

        else:
            st.error(
                f"Unsupported file: {uploaded_file.name}"
            )

# -------------------------
# Chat History
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------

user_question = st.chat_input(
    "Ask a question..."
)

if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    response = chat_service.get_response(
        user_question
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)