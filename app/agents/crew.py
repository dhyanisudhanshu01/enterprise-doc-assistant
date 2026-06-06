from crewai import (
    Agent,
    Task,
    Crew,
    Process,
    LLM,
)

from app.core.config import settings
from app.services.retrieval_service import (
    retrieval_service
)


gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=settings.gemini_api_key,
)


class EnterpriseCrew:

    def run(
        self,
        question: str,
    ):

        retrieved_chunks = (
            retrieval_service.retrieve(
                question,
                top_k=settings.top_k_results,
            )
        )

        context = "\n\n".join(
            chunk["content"]
            for chunk in retrieved_chunks
        )

        # -------------------------
        # Planner Agent
        # -------------------------

        planner = Agent(
            role="Planner Agent",
            goal=(
                "Understand the user's question "
                "and determine what information "
                "is needed."
            ),
            backstory=(
                "Expert at analyzing enterprise "
                "questions and planning answers."
            ),
            llm=gemini_llm,
            verbose=False,
        )

        # -------------------------
        # Retriever Agent
        # -------------------------

        retriever = Agent(
            role="Retriever Agent",
            goal=(
                "Identify the most relevant "
                "information from retrieved "
                "documents."
            ),
            backstory=(
                "Expert in semantic search "
                "and knowledge retrieval."
            ),
            llm=gemini_llm,
            verbose=False,
        )

        # -------------------------
        # Reasoning Agent
        # -------------------------

        reasoner = Agent(
            role="Reasoning Agent",
            goal=(
                "Generate a grounded answer "
                "using retrieved context."
            ),
            backstory=(
                "Expert at reasoning over "
                "enterprise documents."
            ),
            llm=gemini_llm,
            verbose=False,
        )

        # -------------------------
        # Validator Agent
        # -------------------------

        validator = Agent(
            role="Validator Agent",
            goal=(
                "Verify that the answer is "
                "supported by retrieved context."
            ),
            backstory=(
                "Expert in hallucination "
                "detection."
            ),
            llm=gemini_llm,
            verbose=False,
        )

        # -------------------------
        # Response Agent
        # -------------------------

        responder = Agent(
            role="Response Agent",
            goal=(
                "Create the final user-friendly "
                "response."
            ),
            backstory=(
                "Expert at communicating "
                "clearly and concisely."
            ),
            llm=gemini_llm,
            verbose=False,
        )

        # -------------------------
        # Tasks
        # -------------------------

        planning_task = Task(
            description=(
                f"""
                Analyze the question:

                {question}
                """
            ),
            expected_output=(
                "A clear plan outlining what information is needed."
            ),
            agent=planner,
        )

        retrieval_task = Task(
            description=(
                f"""
                Review the retrieved context:

                {context}
                """
            ),
            expected_output=(
                "A summary of the most relevant information."
            ),
            agent=retriever,
        )

        reasoning_task = Task(
            description=(
                f"""
                Use the question:

                {question}

                And the context:

                {context}

                Generate a grounded answer.
                """
            ),
            expected_output=(
                "A concise answer to the user's question, "
                "fully supported by the provided context."
            ),
            agent=reasoner,
        )

        validation_task = Task(
            description=(
                """
                Verify that the answer is
                supported by the context.
                """
            ),
            expected_output=(
                "A validation report confirming whether the answer is supported by the context."
            ),
            agent=validator,
        )

        response_task = Task(
            description=(
                """
                Produce the final response.
                """
            ),
            expected_output=(
                "A user-friendly final response."
            ),
            agent=responder,
        )

        crew = Crew(
            agents=[
                planner,
                retriever,
                reasoner,
                validator,
                responder,
            ],
            tasks=[
                planning_task,
                retrieval_task,
                reasoning_task,
                validation_task,
                response_task,
            ],
            process=Process.sequential,
            verbose=False,
        )

        result = crew.kickoff()

        return (
            str(result),
            retrieved_chunks,
        )


enterprise_crew = EnterpriseCrew()