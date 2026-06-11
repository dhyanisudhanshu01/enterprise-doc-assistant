# Deployment Guide

## Local Setup

### Clone Repository

```bash
git clone <repository-url>

cd enterprise-doc-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a .env file.

```env
GEMINI_API_KEY=YOUR_API_KEY

TOP_K_RESULTS=5

CHUNK_SIZE=1000

CHUNK_OVERLAP=200
```

---

## Run Application

```bash
streamlit run main.py
```

---

## Render Deployment

### Step 1

Push code to GitHub.

### Step 2

Create a new Render Web Service.

### Step 3

Connect GitHub repository.

### Step 4

Configure environment variables.

### Step 5

Deploy application.

---

## render.yaml

```yaml
services:
  - type: web
    name: enterprise-doc-assistant

    runtime: python

    buildCommand: |
      pip install -r requirements.txt

    startCommand: |
      streamlit run main.py --server.port $PORT --server.address 0.0.0.0
```

---

## Deployment Verification

Verify:

* Application loads successfully
* Document upload works
* Question answering works
* Source citations appear
* Session-specific collections work
