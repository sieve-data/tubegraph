---
title: components of RAG stack
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 
The information in this article is based on the experiences of an independent AI engineer working to build and ship production-ready generative AI solutions <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. The insights shared are derived from 37 failed attempts to build a [[retrieval_augmented_generation_RAG | RAG]] stack <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## What is [[retrieval_augmented_generation_RAG | RAG]]?

[[retrieval_augmented_generation_RAG | Retrieval Augmented Generation]] (RAG) is a technique that combines retrieval of relevant information with the generation capabilities of large language models (LLMs) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

The process involves three main steps:
1.  **Retrieval** <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>: A user query (e.g., "Where can I get help in London?") is used to perform a semantic search through a vector database to retrieve relevant documents <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
2.  **Augmentation** <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>: The original query is combined with the information retrieved from the vector database. This combined information is then provided as context to the large language model <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
3.  **Generation** <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>: With the necessary context and the original query, the large language model can now generate an informed response <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Naive [[retrieval_augmented_generation_RAG | RAG]] Solution

A basic [[retrieval_augmented_generation_RAG | RAG]] solution follows a straightforward pipeline:
1.  **Query** <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>: The user's query is received.
2.  **Embedding** <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>: The query is embedded (converted into a numerical vector).
3.  **Comparison and Retrieval** <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>: The embedded query is compared to documents in a vector database, and relevant documents are retrieved <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
4.  **Context to LLM** <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>: The retrieved documents, along with the original query, are passed to the large language model as context <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
5.  **Response Generation** <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>: The LLM generates a response based on the provided context <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

While simple, a naive solution may not provide satisfactory responses, as demonstrated by a query about "help in London" yielding information about "wheelchair friendly taxis" from the knowledge base <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Enhancing [[retrieval_augmented_generation_RAG | RAG]] Solutions

To achieve a more sophisticated [[retrieval_augmented_generation_RAG | RAG]] solution, additional components can be added:
*   **Query Processing Step**: This can involve removing personally identifiable information (PII) from the query before it is passed to the [[retrieval_augmented_generation_RAG | RAG]] system <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Post-Retrieval Step**: This step aims to improve the accuracy of documents retrieved from the vector database <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Cross-encoders vs. Bi-encoders

Understanding cross-encoders and bi-encoders is crucial for improving [[retrieval_augmented_generation_RAG | RAG]] accuracy and scalability:

*   **Cross-encoder**:
    *   **Purpose**: Semantically compare a query with a document <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   **Mechanism**: Sends both the query and the document to a BERT model (encoder from the original transformer model) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, then through a classifier to get a similarity score between 0 and 1 <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   **Characteristics**: Excellent for additional accuracy but slow and not scalable, especially with larger documents, as both query and document are processed by a single model <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   **Placement in [[retrieval_augmented_generation_RAG | RAG]]**: Best used post-retrieval (as a re-ranker) because it works with a few documents and needs high accuracy <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

*   **Bi-encoder**:
    *   **Purpose**: Enable fast and scalable information retrieval <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   **Mechanism**: Uses two separate encoder models—one for the query and one for the document. Each passes through its own BERT layer, pooling, and embedding layer <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. The similarity between the query and document embeddings is then compared (e.g., using cosine similarity) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   **Characteristics**: Fast and scalable because the two models are separated <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Excellent for initial information retrieval <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
    *   **Placement in [[retrieval_augmented_generation_RAG | RAG]]**: Ideal where the vector data is stored, as it needs to compare the query with multiple documents quickly <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

## Components of the [[retrieval_augmented_generation_RAG | RAG]] Stack

The [[retrieval_augmented_generation_RAG | RAG]] stack typically includes several key components, with different choices recommended for prototyping versus production environments.

### Development Environments
*   **Prototyping**: Google Collab is preferred due to free access to hardware accelerators <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Production**: Docker is often used for on-premise or cloud deployments, particularly for financial institutions requiring data and processing to remain on-premise <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Orchestration
This layer manages the flow and interaction between different components of the [[retrieval_augmented_generation_RAG | RAG]] system.
*   **Prototyping**: Llama Index or Lang Graph <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Production**: Llama Index <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Embedding Models
These models convert text into numerical vectors (embeddings) for semantic search.
*   **Options**: Closed models (using APIs) or open models (like those from Nvidia or BAI) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Prototyping**: Closed models like OpenAI's `text-embedding-ada-002` (default in Llama Index) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a> or `text-embedding-3-large` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Open models such as BAI's BGE small model can also be downloaded and used <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Production**: Open models (BAI, Nvidia) <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.

### Vector Database
Stores the document embeddings and enables efficient semantic search.
*   **Recommendation**: Qdrant is an excellent choice for its scalability, handling anything from a few documents to hundreds of thousands <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Large Language Model (LLM)
Generates the final response based on the retrieved context and query.
*   **Prototyping**: Closed models are often preferred for their simplicity via APIs <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, such as OpenAI's GPT-3.5 Turbo (default) <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a> or GPT-4 <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. Open models like Meta's models or Qwen 3 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a> can also be used.
*   **Production**: Open models like Llama 3.2 or Qwen 3.4 billion models from Alibaba Cloud, served using Olama or Hugging Face Text Generation Inference <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Monitoring and Tracing
Essential for troubleshooting and understanding performance bottlenecks within the [[retrieval_augmented_generation_RAG | RAG]] solution <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Prototyping**: Langsmith or Phoenix (specifically LlamaIndex Phoenix) <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.
*   **Production**: Arise Phoenix (can be easily used in a Docker container) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a> <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.

### Re-rankers (Post-Retrieval)
Used to improve the accuracy of the retrieved documents by re-ranking them based on semantic similarity to the query. This uses a cross-encoder approach <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **Prototyping**: Closed models like Cohere's re-ranker <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **Production**: Open solutions from Nvidia <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a> <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

### [[evaluation_and_improvement_of_RAG_solutions | RAG Evaluation]]
Crucial for assessing the quality and performance of the [[retrieval_augmented_generation_RAG | RAG]] solution across various metrics.
*   **Framework**: Ragas is recommended for evaluating the quality of [[retrieval_augmented_generation_RAG | RAG]] solutions <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a> <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a> <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. It works with LLMs, making the task "painless" <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>.

## Production Environment Setup (Docker Compose)

For production, a `docker-compose.yaml` file integrates various Docker images to run the [[retrieval_augmented_generation_RAG | RAG]] solution as containers <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>:
*   **Ingestion Image**: Connects to the knowledge base to pull in data (e.g., HTML files) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.
*   **Qdrant Image**: For the vector database, pulled directly from Docker Hub <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
*   **Front-end App Image**: For the user interface of the solution <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **LLM Serving Image**: Uses Olama or Hugging Face's Text Generation Inference engine to serve the large language models <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **Phoenix Image**: For tracing and monitoring <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Ragas Image**: For [[evaluation_and_improvement_of_RAG_solutions | RAG evaluation]] <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

This setup allows for running each component as a separate container within Docker Compose, ensuring a robust and manageable production environment <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.