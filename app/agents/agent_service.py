from app.agents.crew import (
    enterprise_crew
)


class AgentService:

    def answer_question(
        self,
        question: str,
        session_id: str,
    ):

        answer, chunks = (
            enterprise_crew.run(
                question,
                session_id=session_id,
            )
        )

        sources = []

        for chunk in chunks:

            sources.append(
                {
                    "file_name": (
                        chunk["metadata"].get(
                            "file_name"
                        )
                    ),
                    "chunk_id": (
                        chunk["metadata"].get(
                            "chunk_id"
                        )
                    ),
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }


agent_service = AgentService()