class FileValidationError(Exception):
    """
    Raised when uploaded file
    fails validation.
    """
    pass


class DocumentProcessingError(Exception):
    """
    Raised when document
    processing fails.
    """
    pass


class RetrievalError(Exception):
    """
    Raised when retrieval
    operation fails.
    """
    pass