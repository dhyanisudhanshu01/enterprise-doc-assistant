# Enterprise Document Assistant

## Overview

Enterprise-grade RAG application built using:

- Streamlit
- Gemini
- ChromaDB
- CrewAI
- LangChain

## Features

- Multi-document ingestion
- Semantic search
- Agentic AI workflow
- Grounded responses
- Enterprise safety controls

## Project Structure

enterprise-doc-assistant/
│
├── app/
│   │
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── retriever_agent.py
│   │   ├── reasoning_agent.py
│   │   ├── validator_agent.py
│   │   └── response_agent.py
│   │
│   ├── services/
│   │   ├── ingestion_service.py
│   │   ├── retrieval_service.py
│   │   ├── rag_service.py
│   │   └── chat_service.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── security.py
│   │
│   ├── prompts/
│   │   ├── rag_prompt.py
│   │   └── safety_prompt.py
│   │
│   ├── utils/
│   │   ├── file_utils.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   ├── models/
│   │   ├── document.py
│   │   └── response.py
│   │
│   └── vectorstore/
│       └── chroma_manager.py
│
├── data/
│   ├── uploads/
│   ├── processed/
│   └── vector_db/
│
├── docs/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py

## Setup

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run main.py
```