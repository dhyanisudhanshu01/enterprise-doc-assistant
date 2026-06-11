# Challenges and Learnings

## Challenge 1: Dependency Resolution Issues

### Problem

Several package versions were incompatible with the Python version used during deployment.

### Impact

Deployment failures and build interruptions.

### Resolution

* Cleaned requirements.txt
* Verified package compatibility
* Updated deployment configuration
* Standardized Python version

### Learning

Dependency management should be validated early in the development lifecycle.

---

## Challenge 2: Session Isolation

### Problem

Using a shared ChromaDB collection risked exposing documents between users.

### Resolution

Implemented session-specific collections.

### Learning

Data isolation is critical even in prototype applications.

---

## Challenge 3: Retrieval Quality

### Problem

Relevant information was sometimes missed when chunk sizes were not optimized.

### Resolution

Implemented recursive chunking and configurable retrieval settings.

### Learning

Chunking strategy significantly affects retrieval quality.

---

## Challenge 4: Hallucination Control

### Problem

The LLM could answer from prior knowledge when retrieval quality was poor.

### Resolution

* Context injection
* Source citation
* Validator Agent
* Empty retrieval checks

### Learning

Grounding mechanisms are essential for enterprise AI systems.

---

## Key Takeaways

* RAG systems depend heavily on retrieval quality.
* Agent orchestration improves response quality.
* Deployment challenges often arise from dependency conflicts.
* Security and validation should be built from the beginning.
