# Enterprise Document Intelligence System

Project Link - https://enterprise-doc-assistant-whgc.onrender.com/

## Introduction

Enterprise organizations manage large volumes of unstructured and semi-structured documents such as reports, policies, invoices, spreadsheets, and operational manuals. Extracting useful information from these documents manually is time-consuming and inefficient.

The Enterprise Document Intelligence System addresses this challenge by leveraging Generative AI, Retrieval-Augmented Generation (RAG), Vector Databases, and Agentic AI to enable natural language interaction with enterprise documents.

---

## Problem Statement

Traditional document search systems rely on keyword matching and often fail to understand semantic meaning.

Challenges include:

* Information scattered across multiple documents
* Difficulty locating relevant content
* Time-consuming manual review
* Lack of contextual understanding
* Inability to ask natural language questions

---

## Solution Overview

The solution enables users to:

1. Upload enterprise documents.
2. Automatically process and chunk content.
3. Generate vector embeddings using Google Gemini Embeddings.
4. Store embeddings in ChromaDB.
5. Retrieve relevant content through semantic search.
6. Generate grounded answers using Gemini LLM.
7. Validate and refine responses through CrewAI agents.

---

## Key Features

### Document Processing

* PDF Support
* TXT Support
* CSV Support
* Excel Support
* JSON Support

### Retrieval-Augmented Generation

* Semantic Search
* Context-Aware Retrieval
* Source Citation
* Grounded Responses

### Agentic AI

* Planner Agent
* Retriever Agent
* Reasoning Agent
* Validator Agent
* Response Agent

### Safety Controls

* File Validation
* File Size Limits
* Prompt Injection Detection
* Request Logging
* Response Logging
* Empty Retrieval Protection

---

## Technology Stack

### Frontend

* Streamlit

### LLM

* Gemini 2.5 Flash

### Embeddings

* Google Gemini Embeddings

### Frameworks

* LangChain
* CrewAI

### Vector Database

* ChromaDB

### Data Processing

* Pandas
* PyPDF

---

## Business Value

The system reduces the effort required to search enterprise documents while improving accessibility and decision-making through natural language interaction.
