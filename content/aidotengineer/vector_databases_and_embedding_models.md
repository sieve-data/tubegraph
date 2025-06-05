---
title: Vector databases and embedding models
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

This article explores the roles of vector databases and embedding models within [[ai_models_and_training_methods | AI]] systems, particularly focusing on Retrieval Augmented Generation (RAG) solutions.

## Understanding RAG and Component Breakdown

Retrieval Augmented Generation (RAG) is a process that involves an initial user query, followed by a retrieval step where a [[semantic_and_graphbased_data_in_ai_systems | semantic search]] is performed through a [[benefits_of_graph_databases_in_ai_applications | vector database]] to retrieve relevant documents based on the query <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. The original query is then combined with the retrieved information to provide context to the [[using_language_models_to_generate_text | language model]] for the generation piece <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

Components of a RAG stack typically include:
*   Orchestration <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>
*   Embedding models <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>
*   Vector database <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>
*   [[building_and_deploying_large_language_models | Large language model]] <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>

For prototyping, Google Collab is often used due to free hardware accelerators <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. For production environments, especially with financial institutions requiring on-premise data processing, Docker is a common solution <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Embedding Models

[[ai_models_and_training_methods | Embedding models]] are crucial for converting queries and documents into a format that allows for [[semantic_and_graphbased_data_in_ai_systems | semantic comparison]] <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

### Types of Embedding Models
*   **Closed Models:** These are typically accessed via APIs, making them simple to use <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. Examples include OpenAI's `text-embedding-ada-002` (default in Quadrant) <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a> and `text-embedding-3-large` <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   **Open Models:** These can be downloaded and run locally, providing more control <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. Examples include models from Nvidia and B AI <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, specifically the BGE small model from B AI available on Hugging Face <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.

### Cross-Encoder vs. Bi-Encoder
The choice of encoder impacts accuracy and scalability within a RAG pipeline.

*   **Cross-Encoder:**
    *   Semantically compares a query with a document by sending both to a BERT model and then to a classifier <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
    *   Produces a result between 0 and 1 indicating semantic similarity <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.
    *   Excellent for additional accuracy <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>, but is slow and not scalable, especially with larger documents <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
    *   Best used post-retrieval as a "reranker" due to its accuracy and inability to scale with many documents <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
    *   An example of a closed model for reranking is Cohere's solution <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a> <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. Nvidia offers an open solution for reranking <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

*   **Bi-Encoder:**
    *   Uses two separate encoders (BERT models), one for the query and one for the document, each with pooling and embedding layers <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
    *   Compares the query and document embeddings using metrics like cosine similarity <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>.
    *   This separation makes it a fast and scalable solution <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>.
    *   Excellent for information retrieval, making it suitable for the [[semantic_and_graphbased_data_in_ai_systems | vector database]] component where multiple documents are compared <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.

## Vector Databases

A [[benefits_of_graph_databases_in_ai_applications | vector database]] stores vector embeddings of documents, allowing for [[semantic_and_graphbased_data_in_ai_systems | semantic search]] and retrieval of relevant documents based on a query's embedding <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.

### Quadrant
Quadrant is highlighted as an excellent [[benefits_of_graph_databases_in_ai_applications | vector database]] solution because it scales very well, handling a range from a couple of documents to hundreds of thousands <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. It is a preferred choice for both prototyping and production environments <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.

## Integration in RAG Pipeline

In a naive RAG solution, a query is embedded, compared to documents in a [[benefits_of_graph_databases_in_ai_applications | vector database]], relevant documents are retrieved, and then passed along with the query to a [[using_language_models_to_generate_text | language model]] for response generation <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

For a more sophisticated RAG solution, a query processing step can be added (e.g., to remove personally identifiable information) <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>. A post-retrieval step can also be used to improve the accuracy of retrieved documents <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.

### Component Workflow in RAG
*   **Orchestration:** Tools like LlamaIndex or LangChain (LangGraph) are used for orchestrating the RAG pipeline. LlamaIndex is suggested for both prototyping and production <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.
*   **Embedding Models:** An open solution, such as the BGE small model from B AI, can be downloaded and used as the default embedding model in tools like LlamaIndex <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   **Vector Database:** Quadrant is integrated to store and retrieve document embeddings <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **Reranking (Cross-Encoder):** After initial retrieval from the vector database, a reranker (cross-encoder) like Cohere's model or Nvidia's open solution can be applied to improve accuracy by re-ranking the top results <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a> <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>.

### Monitoring and Evaluation
Monitoring and tracing solutions, such as Langsmith or Phoenix/Arise, are crucial for troubleshooting and understanding performance (e.g., where most time is spent) <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a> <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. RAG evaluation frameworks like Ragas are used to test the quality of RAG solutions across many documents <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a> <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.

### Production Environment
A production environment often uses Docker Compose with separate Docker images for:
*   Data ingestion <a class="yt-timestamp" data-t="17:57:00">[17:57:00]</a>
*   Quadrant as the [[benefits_of_graph_databases_in_ai_applications | vector database]] <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>
*   Front-end application <a class="yt-timestamp" data-t="18:09:00">[18:09:00]</a>
*   Model serving (e.g., Olama or Hugging Face Text Generation Inference) <a class="yt-timestamp" data-t="18:12:00">[18:12:00]</a>
*   Tracing (Phoenix) <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>
*   Evaluation (Ragas) <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>

[[ai_models_and_training_methods | Embedding models]] and reranking models are specified within this Docker setup <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>.