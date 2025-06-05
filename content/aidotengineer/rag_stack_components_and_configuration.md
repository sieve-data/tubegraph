---
title: RAG stack components and configuration
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

### Introduction to RAG Systems
Retrieval Augmented Generation (RAG) is a system designed to improve the responses of Large Language Models (LLMs) by providing them with relevant, external context <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. This guide presents a RAG stack based on learnings from 37 failed attempts, aiming to be a high-ROI (Return on Investment) guide per minute <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

The development process typically involves two phases:
*   **Prototyping** Usually conducted in Google Colab, leveraging its free hardware accelerators for ease of experimentation <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.
*   **Production Deployment** Often utilizes Docker for on-premise or cloud deployment, which is crucial for organizations like financial institutions requiring data and processing to remain on-premise <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

### The RAG Pipeline
A basic RAG solution involves a user query, which is then embedded and compared to documents within a vector database <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. Relevant documents are retrieved and passed along with the original query to an LLM, enabling it to generate a context-aware response <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

For a more sophisticated RAG solution, additional steps can be incorporated:
*   **Query Processing:** A step to potentially remove sensitive information (e.g., Personally Identifiable Information) before the query is sent to the RAG system <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
*   **Post-Retrieval Step:** This step improves the accuracy of the documents retrieved from the vector database, often by re-ranking <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Core RAG Stack Components
The RAG stack is broken down into several key components:

#### 1. Orchestration
The orchestration layer manages the flow and interaction between different RAG components.
*   **Prototyping:** [[graph_rag_workflows | LlamaIndex]] or [[graph_rag_workflows | LangChain]] <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.
*   **Production:** [[graph_rag_workflows | LlamaIndex]] <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

#### 2. Embedding Models
Embedding models convert text into numerical vectors for semantic search.
*   **Prototyping:**
    *   Closed models (APIs) for simplicity, e.g., OpenAI's `text-embedding-ada-002` or `text-embedding-3-large` <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
    *   Open models, e.g., from NVIDIA or BAI (specifically BGE Small model) <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Production:** Open models like those from BAI or NVIDIA, which can be downloaded and run locally <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.

#### 3. Vector Database
The vector database stores document embeddings for efficient retrieval.
*   **Choice:** Qdrant is recommended due to its excellent scalability, handling from a few to hundreds of thousands of documents <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

#### 4. Large Language Models (LLMs)
LLMs generate the final response based on the query and retrieved context.
*   **Prototyping:**
    *   Closed models (APIs) for simplicity, e.g., OpenAI's GPT-3.5 Turbo or GPT-4 <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
    *   Open models like Meta's Llama models or Alibaba Cloud's Qwen models <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
*   **Production:**
    *   Open models (e.g., Llama 3.2, Qwen 3.4 billion) served via Olama or Hugging Face Text Generation Inference within a Docker environment <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

#### 5. Monitoring and Tracing
[[monitoring_tracing_and_evaluation_in_rag_systems | Monitoring and tracing]] are critical for troubleshooting and understanding performance bottlenecks (e.g., where most time is spent) <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Prototyping:** Langsmith or Arize Phoenix <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Production:** Arize Phoenix, often used in a Docker container <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

#### 6. Re-ranking
Re-ranking improves the accuracy of the RAG solution by re-ordering retrieved documents based on their relevance to the query. This is typically done post-retrieval <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Prototyping:** Closed models (e.g., Cohere) <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
*   **Production:** Open solutions (e.g., from NVIDIA) <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

#### 7. Evaluation
[[metrics_for_evaluating_rag_systems | Evaluating RAG systems]] is essential to assess the quality of responses and retrieved documents.
*   **Framework:** RAGAS is a recommended framework for [[metrics_for_evaluating_rag_systems | RAG evaluation]], working with LLMs to make the task "painless" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. It allows checking quality across different metrics <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

### Encoder Types in RAG
*   **Cross-Encoder:**
    *   Semantically compares a query with a document by sending both to a BERT model and then a classifier, yielding a similarity score between 0 and 1 <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
    *   Offers additional accuracy but is slow and not scalable for large documents due to processing query and document together <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
    *   Best suited for post-retrieval re-ranking, as it works with a reduced set of documents <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.
*   **Bi-Encoder:**
    *   Uses two separate encoders (BERT models), one for the query and one for the document, each passing through pooling and embedding layers <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
    *   Compares the resulting embeddings using metrics like cosine similarity <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.
    *   A fast and scalable solution, excellent for initial information retrieval where the query is compared against multiple documents <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
    *   Typically used where the vector data is stored, as part of the initial retrieval process <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

### Production Environment Example (Docker Compose)
A production environment often uses a `docker-compose.yaml` file to manage multiple Docker images as containers <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>:
*   **Data Ingestion Image:** Connects to the knowledge base to pull in HTML files <a class="yt-timestamp" data-t="17:57:00">[17:57:00]</a>.
*   **Qdrant Image:** For the vector database, pulled from Docker Hub <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
*   **Front-end App Image:** For the user interface <a class="yt-timestamp" data-t="18:09:00">[18:09:00]</a>.
*   **LLM Serving Image:** Olama or Hugging Face Text Generation Inference engine to serve models <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>.
*   **Arize Phoenix Image:** For [[monitoring_tracing_and_evaluation_in_rag_systems | tracing]] <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>.
*   **RAGAS Image:** For [[metrics_for_evaluating_rag_systems | model evaluation]] <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

This setup allows for robust and scalable deployment of RAG solutions.