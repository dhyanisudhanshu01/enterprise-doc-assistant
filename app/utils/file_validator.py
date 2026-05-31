from pathlib import Path


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".csv",
    ".xlsx",
    ".json",
}


def validate_file(file_name: str) -> bool:
    """
    Validate uploaded file extension.
    """

    extension = Path(file_name).suffix.lower()

    return extension in ALLOWED_EXTENSIONS