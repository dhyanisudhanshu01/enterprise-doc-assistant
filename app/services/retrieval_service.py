from app.vectorstore.chroma_manager import (
    chroma_manager
)
from app.core.config import settings


class RetrievalService:
    """
    Handles semantic retrieval.
    """

    def retrieve(
        self,
        query: str,
        top_k: int = settings.top_k_results,
    ):

        results = (
            chroma_manager.similarity_search(
                query=query,
                top_k=top_k,
            )
        )

        documents = (
            results.get(
                "documents",
                [[]]
            )[0]
        )

        metadatas = (
            results.get(
                "metadatas",
                [[]]
            )[0]
        )

        retrieved_chunks = []

        for doc, metadata in zip(
            documents,
            metadatas,
        ):
            retrieved_chunks.append(
                {
                    "content": doc,
                    "metadata": metadata,
                }
            )

        return retrieved_chunks


retrieval_service = RetrievalService()