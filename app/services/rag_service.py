from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from app.core.config import settings
from app.prompts.rag_prompt import (
    RAG_PROMPT
)
from app.services.retrieval_service import (
    retrieval_service
)


class RAGService:

    def __init__(self):

        self.llm = (
            ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=(
                    settings.gemini_api_key
                ),
                temperature=0,
            )
        )

    def answer_question(
        self,
        question: str,
        session_id: str,
    ) -> dict:

        retrieved_chunks = (
            retrieval_service.retrieve(
                query=question,
                session_id=session_id,
                top_k=settings.top_k_results,
            )
        )
        if not retrieved_chunks:
            return {
                "answer": "Sorry, I couldn't find relevant information in the documents.",
                "sources": [],
            }
        context = "\n\n".join(
            chunk["content"]
            for chunk in retrieved_chunks
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        response = (
            self.llm.invoke(prompt)
        )

        sources = []

        for chunk in retrieved_chunks:

            source = {
                "file_name": (
                    chunk["metadata"].get(
                        "file_name",
                        "Unknown"
                    )
                ),
                "chunk_id": (
                    chunk["metadata"].get(
                        "chunk_id",
                        "Unknown"
                    )
                ),
            }

            sources.append(source)

        return {
            "answer": response.content,
            "sources": sources,
        }


rag_service = RAGService()