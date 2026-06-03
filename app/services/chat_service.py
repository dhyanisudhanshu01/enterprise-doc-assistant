from app.services.rag_service import (
    rag_service
)


class ChatService:
    def get_response(
        self,
        question: str,
    ) -> dict:

        return (
            rag_service.answer_question(
                question
            )
        )


chat_service = ChatService()