import streamlit as st

from app.services.chat_service import chat_service
from app.utils.file_validator import validate_file
from app.core.logger import app_logger
from pathlib import Path
from app.services.ingestion_service import (
    ingestion_service
)

from app.services.chunking_service import (
    chunking_service
)

from app.vectorstore.chroma_manager import (
    chroma_manager
)

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

UPLOAD_FOLDER = Path("data/uploads")

UPLOAD_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

uploaded_files = st.file_uploader(
    "Upload Documents",
    accept_multiple_files=True,
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        # Validate file type
        if not validate_file(uploaded_file.name, uploaded_file.size):

            st.error(
                f"Unsupported file: {uploaded_file.name}"
            )

            continue

        # Prevent duplicate processing
        if (uploaded_file.name
            in st.session_state.uploaded_files):

            st.warning(
                f"{uploaded_file.name} has already been processed."
            )

            continue

        try:

            # -------------------------
            # Save File
            # -------------------------

            save_path = (
                UPLOAD_FOLDER /
                uploaded_file.name
            )

            with open(
                save_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            app_logger.info(
                f"File saved: {uploaded_file.name}"
            )

            # -------------------------
            # Ingest Document
            # -------------------------

            document = (
                ingestion_service.ingest_document(
                    str(save_path)
                )
            )

            app_logger.info(
                f"Document ingested: "
                f"{uploaded_file.name}"
            )

            # -------------------------
            # Create Chunks
            # -------------------------

            chunks = (
                chunking_service.create_chunks(
                    document
                )
            )

            app_logger.info(
                f"Chunks created: {len(chunks)}"
            )

            # -------------------------
            # Store in ChromaDB
            # -------------------------

            chroma_manager.add_documents(
                chunks
            )

            app_logger.info(
                f"Vectors stored for: "
                f"{uploaded_file.name}"
            )

            # -------------------------
            # Update Session State
            # -------------------------

            st.session_state.uploaded_files.append(
                uploaded_file.name
            )

            # -------------------------
            # Success Message
            # -------------------------

            st.success(
                f"{uploaded_file.name} processed successfully."
            )

        except Exception as error:

            app_logger.error(
                f"Processing failed for "
                f"{uploaded_file.name}: "
                f"{str(error)}"
            )
            st.error(
                f"Failed to process "
                f"{uploaded_file.name}"
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
    answer = response["answer"]
    sources = response["sources"]

    formatted_response = answer
    if sources:

        formatted_response += (
            "\n\n### Sources\n"
        )

        for source in sources:

            formatted_response += (
                f"- {source['file_name']} "
                f"(Chunk {source['chunk_id']})\n"
            )    
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": formatted_response,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(formatted_response)