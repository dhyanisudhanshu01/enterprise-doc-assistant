from pathlib import Path

from app.models.document import Document
from app.utils.document_loader import DocumentLoader


class IngestionService:

    def ingest_document(
        self,
        file_path: str
    ) -> Document:

        content = DocumentLoader.load(
            file_path
        )

        metadata = {
            "file_name": Path(file_path).name,
            "file_type": Path(file_path).suffix,
        }

        return Document(
            content=content,
            metadata=metadata,
        )


ingestion_service = IngestionService()