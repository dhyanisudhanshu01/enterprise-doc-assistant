from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.models.document import Document
from app.core.config import settings


class ChunkingService:
    """
    Handles document chunking.
    """

    def __init__(
        self,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    ):
        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )
        )

    def create_chunks(
        self,
        document: Document,
    ) -> list[Document]:

        chunks = (
            self.text_splitter.split_text(
                document.content
            )
        )

        documents = []

        for index, chunk in enumerate(chunks):

            metadata = {
                **document.metadata,
                "chunk_id": index,
            }

            documents.append(
                Document(
                    content=chunk,
                    metadata=metadata,
                )
            )

        return documents


chunking_service = ChunkingService()