from app.agents.agent_service import (
    agent_service
)
from app.utils.safety import (
    detect_prompt_injection
)
from app.core.logger import (
    app_logger
)

class ChatService:
    def get_response(
        self,
        question: str,
        session_id: str,
    ) -> dict:
        app_logger.info(
            f"Question: {question}"
        )
        if detect_prompt_injection(question):
            return {
                "answer": (
                    "Potential prompt injection "
                    "attempt detected."
                ),
                "sources": [],
            }
        response = agent_service.answer_question(question, session_id=session_id)
        app_logger.info("Response generated successfully.")
        return response


chat_service = ChatService()