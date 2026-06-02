import chromadb

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

from app.core.config import settings


class ChromaManager:

    def __init__(self):

        self.embedding_model = (
            GoogleGenerativeAIEmbeddings(
                model="models/gemini-embedding-001",
                google_api_key=settings.gemini_api_key,
            )
        )

        self.client = (
            chromadb.PersistentClient(
                path=settings.chroma_db_path
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="enterprise_documents"
            )
        )

    def add_documents(
        self,
        chunks,
    ):

        for chunk in chunks:

            embedding = (
                self.embedding_model.embed_query(
                    chunk.content
                )
            )

            self.collection.add(
                ids=[
                    f"{chunk.metadata['file_name']}"
                    f"_{chunk.metadata['chunk_id']}"
                ],
                embeddings=[embedding],
                documents=[
                    chunk.content
                ],
                metadatas=[
                    chunk.metadata
                ],
            )


chroma_manager = ChromaManager()