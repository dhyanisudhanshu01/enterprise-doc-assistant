class ChatService:
    """
    Temporary chat service.

    In Phase 7 this will be replaced
    by the complete RAG pipeline.
    """

    def get_response(self, question: str) -> str:
        return (
            f"Received your question: '{question}'. "
            f"RAG pipeline will be integrated in Phase 7."
        )


chat_service = ChatService()