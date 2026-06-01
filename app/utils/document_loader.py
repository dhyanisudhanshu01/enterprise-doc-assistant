import json
from pathlib import Path

import pandas as pd
from pypdf import PdfReader


class DocumentLoader:

    @staticmethod
    def load(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return DocumentLoader._load_pdf(file_path)

        if extension == ".txt":
            return DocumentLoader._load_txt(file_path)

        if extension == ".csv":
            return DocumentLoader._load_csv(file_path)

        if extension == ".xlsx":
            return DocumentLoader._load_excel(file_path)

        if extension == ".json":
            return DocumentLoader._load_json(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    @staticmethod
    def _load_pdf(file_path: str) -> str:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    @staticmethod
    def _load_txt(file_path: str) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()

    @staticmethod
    def _load_csv(file_path: str) -> str:

        dataframe = pd.read_csv(file_path)

        return dataframe.to_string(index=False)

    @staticmethod
    def _load_excel(file_path: str) -> str:

        dataframe = pd.read_excel(file_path)

        return dataframe.to_string(index=False)

    @staticmethod
    def _load_json(file_path: str) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return json.dumps(
            data,
            indent=2
        )