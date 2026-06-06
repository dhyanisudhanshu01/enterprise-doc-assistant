import chromadb

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

from app.core.config import settings


class ChromaManager:
    def get_collection(
            self,
            session_id: str,
        ):

            collection_name = (
                f"session_{session_id}"
            )

            return (
                self.client.get_or_create_collection(
                    name=collection_name
                )
            )

    def delete_collection(
        self,
        session_id: str,):

        collection_name = (
            f"session_{session_id}"
        )

        try:

            self.client.delete_collection(
                collection_name
            )

        except Exception:
            pass

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

        
    
    def add_documents(
        self,
        chunks,
        session_id: str,
    ):

        for chunk in chunks:

            embedding = (
                self.embedding_model.embed_query(
                    chunk.content
                )
            )
            collection = (self.get_collection(
                session_id
            ))
            collection.add(
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

    def similarity_search(
    self,
        query: str,
        top_k: int = 5,
        session_id: str = None,
    ):
        """
        Retrieve the most relevant chunks.
        """

        query_embedding = (
            self.embedding_model.embed_query(
                query
            )
        )
        collection = (
            self.get_collection(
                session_id
            )
        )
        results = (
            collection.query(
                query_embeddings=[
                    query_embedding
                ],
                n_results=top_k,
            )
        )

        return results


chroma_manager = ChromaManager()