from pydantic import BaseModel
from typing import Dict


class Document(BaseModel):
    """
    Standard document object used
    throughout the application.
    """

    content: str
    metadata: Dict