---
title: evaluation and improvement of RAG solutions
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

This article provides insights into the evaluation and improvement of [[retrieval_augmented_generation_rag | RAG]] (Retrieval Augmented Generation) solutions, drawing from lessons learned over many iterations <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The focus is on practical components used in a [[components_of_rag_stack | RAG stack]] for both prototyping and production environments <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Components of a [[retrieval_augmented_generation_rag | RAG]] Solution

A typical [[components_of_rag_stack | RAG stack]] includes:
*   Orchestration <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
*   Embedding models <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   Vector database <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>
*   Monitoring and Tracing tools <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   Re-ranking solutions <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>
*   Evaluation frameworks <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>

Solutions often differ between prototyping and production. Prototyping is typically done in Google Colab for free hardware accelerators <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Production environments, especially for financial institutions, often require on-premise data processing, making Docker a common choice for deployment <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Orchestration
*   **Prototyping:** Llama Index or LangChain/LangGraph <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   **Production:** Llama Index <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>

### Embedding Models
*   **Prototyping:** Closed models (via APIs) or open models (e.g., Nvidia, BAAI) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The BAAI BGE small model is an example of an open embedding model <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Production:** Open models (e.g., BAAI, Nvidia) <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Vector Database
*   Qdrant is recommended due to its scalability from a few documents to hundreds of thousands <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Large Language Models (LLMs)
*   **Prototyping:** Closed models (via APIs for simplicity) or open models (e.g., Meta, Qwen 3) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Production:** Open models, served using Olama or Hugging Face Text Generation Inference within a Docker environment (e.g., Llama 3.2, Qwen 3.4 billion from Alibaba Cloud) <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Improving [[retrieval_augmented_generation_rag | RAG]] Solution Accuracy

A naive [[retrieval_augmented_generation_rag | RAG]] solution involves embedding a query, retrieving relevant documents from a vector database, and passing them to an LLM for response generation <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. To enhance accuracy, two key steps can be added:
1.  **Query Processing:** Removing or refining information in the initial query (e.g., personal identifiable information) before it enters the [[retrieval_augmented_generation_rag | RAG]] system <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
2.  **Post-Retrieval Processing (Re-ranking):** Improving the accuracy of documents retrieved from the vector database before they are sent to the LLM <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

### Cross-Encoders vs. Bi-Encoders

Understanding the difference between cross-encoders and bi-encoders is crucial for effective information retrieval and re-ranking:

*   **Cross-Encoder:**
    *   Semantically compares a query with a document by sending both to a BERT model (encoder from the original transformer model) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
    *   A classifier then provides a similarity score between 0 and 1 <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
    *   **Pros:** Excellent for additional accuracy <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
    *   **Cons:** Slow and not scalable, especially with large documents, as the query and document are processed together <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
    *   **Placement in [[retrieval_augmented_generation_rag | RAG]]:** Best used *post-retrieval* (as a re-ranker) because it works with a smaller number of documents retrieved from the vector database <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.

*   **Bi-Encoder:**
    *   Uses two separate encoders (e.g., BERT models) for the query and the document <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. Each encoder produces an embedding.
    *   Similarity is then compared using metrics like cosine similarity <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   **Pros:** Fast and scalable because query and document embeddings are generated independently, allowing for efficient comparison <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. Excellent for information retrieval <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
    *   **Placement in [[retrieval_augmented_generation_rag | RAG]]:** Ideal for the vector database search where the query is compared against many documents <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Re-ranking with Cross-Encoders
Re-rankers improve the accuracy of a [[retrieval_augmented_generation_rag | RAG]] solution <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Prototyping:** Closed models like Cohere's re-ranker <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   **Production:** Open solutions like Nvidia's re-ranker <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Evaluation of [[retrieval_augmented_generation_rag | RAG]] Solutions

Evaluating how well a [[retrieval_augmented_generation_rag | RAG]] solution performs is critical <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Monitoring and Tracing
Monitoring and tracing help troubleshoot issues and identify performance bottlenecks within the [[retrieval_augmented_generation_rag | RAG]] pipeline <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Prototyping:** LangChain Phoenix or Langsmith <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Production:** Arise Phoenix, which can be easily used in a Docker container <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### [[tools_and_interfaces_for_rag_evaluation | RAG Evaluation Frameworks]]
While a single query can be tested manually, a robust [[retrieval_augmented_generation_rag | RAG]] solution requires testing against a larger set of documents and queries <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.
*   **Ragas:** A recommended framework for [[tools_and_interfaces_for_rag_evaluation | RAG evaluation]], which allows checking the quality of solutions in different ways and works well with LLMs, making the task relatively painless <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

## Production Environment Setup
A production [[retrieval_augmented_generation_rag | RAG]] environment often uses a `docker-compose.yaml` file to manage various services as Docker containers <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>. Key images include:
*   Data ingestion <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>
*   Qdrant for the vector database <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>
*   Front-end application <a class="yt-timestamp" data-t="00:18:09">[01:18:09]</a>
*   Olama or Hugging Face Text Generation Inference for serving models <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>
*   Phoenix for tracing <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>
*   Ragas for evaluation <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>