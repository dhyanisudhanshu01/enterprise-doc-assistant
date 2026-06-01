from app.services.ingestion_service import (
    ingestion_service
)

from app.services.chunking_service import (
    chunking_service
)

doc = ingestion_service.ingest_document(
    "data/uploads/sample.txt"
)

chunks = chunking_service.create_chunks(
    doc
)

print(
    f"Total Chunks: {len(chunks)}"
)

for chunk in chunks:
    print(chunk.metadata)