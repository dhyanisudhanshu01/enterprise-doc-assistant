from pathlib import Path
from app.core.config import settings

MAX_FILE_SIZE_MB = settings.max_file_size_mb

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".csv",
    ".xlsx",
    ".json",
}


def validate_file(
    file_name: str,
    file_size: int,
) -> bool:

    extension = (
        Path(file_name)
        .suffix
        .lower()
    )

    if (
        extension
        not in ALLOWED_EXTENSIONS
    ):
        return False

    size_mb = (
        file_size /
        (1024 * 1024)
    )

    return (
        size_mb <= MAX_FILE_SIZE_MB
    )