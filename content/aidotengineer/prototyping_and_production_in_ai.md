---
title: prototyping and production in AI
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

Jonathan Fernandez, an independent AI engineer, specializes in helping companies build and ship production-ready generative AI solutions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. His approach to developing AI systems, particularly Retrieval Augmented Generation (RAG) stacks, involves a distinct separation between prototyping and production environments <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Development Workflow

The typical [[product_development_process_in_ai | product development process]] involves two main phases:
*   **Prototyping**: Often conducted in Google Colab due to access to free hardware accelerators, making it easy to prototype <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Production**: Frequently uses Docker for deployment, allowing solutions to run either on-premise (common for financial institutions with data residency requirements) or in the cloud <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## RAG Stack Components and Tooling

Based on learnings from 37 prior attempts, a robust RAG stack utilizes specific tools tailored for each phase <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

| Component                 | Prototyping Tools                  | Production Tools                                                                                                                                                                                                       | Notes                                                                                                                                                                                                                                                                 |
| :------------------------ | :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Orchestration Layer**   | LlamaIndex, LangChain / LangGraph  | LlamaIndex                                                                                                                                                                                                             | LlamaIndex is noted for its ability to create a basic RAG solution in a few lines of code <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.                                                                                                            |
| **Embedding Models**      | Closed (APIs e.g., OpenAI)         | Open (e.g., NVIDIA, BAAI)                                                                                                                                                                                              | Closed models simplify usage via APIs <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Open models like BGE small model from Hugging Face can be downloaded and used <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.                                    |
| **Vector Database**       | Qdrant (in-memory for prototype)   | Qdrant                                                                                                                                                                                                                 | Qdrant is an excellent choice for its scalability, handling anything from a few to hundreds of thousands of documents <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.                                                                             |
| **Large Language Model**  | Closed (APIs e.g., OpenAI)         | Open (e.g., Meta Llama, Alibaba Cloud Qwen) served by Olama or Hugging Face Text Generation Inference | Closed models offer simplicity via APIs <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. In production, open models are served using tools like Olama or Hugging Face's text generation inference engine, often within Docker <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. |
| **Monitoring and Tracing**| LangSmith, Arise Phoenix            | Arise Phoenix (Docker container)                                                                                                                                                                                       | Essential for troubleshooting, understanding time consumption of components, and tracking the RAG pipeline <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Arise Phoenix has a good Docker solution <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. |
| **Re-ranking / Accuracy** | Closed (e.g., Cohere)              | Open (e.g., NVIDIA)                                                                                                                                                                                                    | Re-ranking improves the accuracy of the RAG solution <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Cross-encoders, also known as rerankers, are placed post-retrieval for additional accuracy, though they are slower and less scalable than bi-encoders <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. |
| **Evaluation Framework**  | Ragas                              | Ragas                                                                                                                                                                                                                  | Crucial for evaluating the quality of the RAG solution across various metrics and works well with Large Language Models, making the task relatively painless <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. |

## Understanding RAG: Retrieval Augmented Generation

RAG is a process to enhance the generation capabilities of Large Language Models (LLMs) by providing them with relevant context from an external knowledge base <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

The process involves:
1.  **Retrieval**: A user query (e.g., "Where can I get help in London?") is used to perform a semantic search through a vector database to retrieve relevant documents <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
2.  **Augmentation**: The original query is combined with the retrieved information from the vector database, providing crucial context to the LLM <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Generation**: With the additional context, the LLM can produce a more accurate and relevant response to the original question <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

A naive RAG solution embeds the query, compares it to documents in a vector database, retrieves relevant documents, and passes them with the query to the LLM for response generation <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### Improving RAG Accuracy

To enhance a RAG solution, additional steps can be incorporated:
*   **Query Processing**: Steps to refine the query, such as removing Personally Identifiable Information (PII) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Post-Retrieval Processing**: Improving the accuracy of retrieved documents before passing them to the LLM <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This often involves re-rankers.

#### Cross-Encoders vs. Bi-Encoders
*   **Cross-Encoder**: Semantically compares a query with a document by sending both to a BERT model and then a classifier, yielding a similarity score (0-1) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. While excellent for additional accuracy, it is slow and not scalable for large documents <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. It is best used as a re-ranker *post-retrieval* with a limited number of documents <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Bi-Encoder**: Uses two separate encoder models (e.g., two BERT layers) for the query and the document independently, and then compares their embeddings using cosine similarity <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This solution is fast and scalable, making it excellent for information retrieval in the vector database step <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Production Environment Setup with Docker

A typical production setup for an AI solution, particularly a RAG pipeline, uses `docker-compose.yaml` to orchestrate multiple Docker images as containers <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.

Key Docker images for a RAG solution include:
*   **Data Ingestion**: An image for ingesting data from the knowledge base (e.g., HTML files) <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.
*   **Vector Database**: An image for Qdrant, pulled from Docker Hub <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **Front-end Application**: For user interaction <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   **LLM Serving**: Olama or Hugging Face's Text Generation Inference engine to serve large language models <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.
*   **Tracing/Monitoring**: Phoenix (Arise Phoenix) for tracking and troubleshooting <a class="yt-timestamp" data-t="00:18:19">[00:18:19]</a>.
*   **Evaluation**: Ragas for continuously evaluating model quality <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

This structured approach allows for robust [[scaling_ai_solutions_in_production | scaling AI solutions in production]] and effective [[effective_design_of_ai_in_products | design of AI in products]].