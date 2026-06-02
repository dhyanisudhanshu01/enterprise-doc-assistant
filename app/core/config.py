from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.chunk_size = int(os.getenv("CHUNK_SIZE", 5000))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 200))
        self.chroma_db_path = os.getenv("CHROMA_DB_PATH", "data/vector_db")

settings = Settings()