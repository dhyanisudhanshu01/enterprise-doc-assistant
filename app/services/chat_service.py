from app.agents.agent_service import (
    agent_service
)


class ChatService:
    def get_response(
        self,
        question: str,
    ) -> dict:

        return (
            agent_service.answer_question(
                question
            )
        )


chat_service = ChatService()