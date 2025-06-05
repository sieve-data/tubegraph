---
title: Cross encoders and bioencoders in RAG solutions
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

Retrieval Augmented Generation (RAG) is a technique used to improve the output of Large Language Models (LLMs) by giving them access to external knowledge bases <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. This approach aims to provide more accurate and contextually relevant responses <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

A typical RAG process involves:
1.  **Retrieval**: A user query, such as "Where can I get help in London?", is used to perform a semantic search through a vector database to retrieve relevant documents <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
2.  **Augmentation**: The retrieved information is combined with the original query to provide context to the LLM <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
3.  **Generation**: The LLM uses this context and the original query to generate a response <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

## Naive RAG Solution Limitations
A basic RAG solution involves embedding the query, comparing it to documents in a vector database, retrieving relevant documents, and passing them to an LLM for response generation <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. However, such a "naive" solution may not always provide satisfactory results <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. To improve accuracy, additional steps like query processing and post-retrieval processing are needed <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.

## Understanding Cross-Encoders
A cross-encoder is a model designed to semantically compare a query with a document <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

### Mechanism
The process involves:
*   Sending both the query and the document to a BERT model (an encoder from the original transformer model) <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
*   Passing the output to a classifier <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>.
*   Receiving a score between 0 and 1, indicating the semantic similarity between the query and the document <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.

### Advantages and Disadvantages
*   **Advantage**: Excellent for achieving additional accuracy <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
*   **Disadvantage**: As document size increases, the solution becomes less scalable <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. It is slow and not scalable for many documents due to the need to pass both the query and full document through a single model <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.

### Placement in RAG Pipeline
Given its high accuracy but low scalability, a cross-encoder is best used **post-retrieval** <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>. It functions effectively as a "reranker" to refine the top few documents retrieved by an initial, more scalable method <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. For example, Cohere's closed model can be used for reranking, or an open solution from Nvidia in production environments <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>, <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>.

## Understanding Bi-Encoders
Bi-encoders address the scalability issues of cross-encoders by splitting the encoding process <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.

### Mechanism
*   Instead of one model, two separate encoders are used <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   One encoder (BERT layer, pooling, embedding layer) processes the query <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.
*   Another separate encoder (BERT layer, pooling, embedding layer) processes the document <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
*   The similarity between the query and document embeddings is then compared using metrics like cosine similarity <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.

### Advantages
*   **Fast and Scalable**: By separating the models, this approach allows for faster and more scalable information retrieval <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>. This is because document embeddings can be pre-computed and stored, enabling quick similarity searches.

### Placement in RAG Pipeline
A bi-encoder is ideal for the **initial retrieval** step, particularly where the vector data is stored <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. It efficiently compares the query against multiple documents to retrieve a set of relevant candidates <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. An example of an open bi-encoder solution is the BGE small model from B AI <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.

## Integrating Encoders into RAG
A robust RAG solution typically combines both bi-encoders and cross-encoders:
1.  **Bi-encoder for Initial Retrieval**: The bi-encoder, often part of the vector database (e.g., Qdrant), quickly retrieves a larger set of potentially relevant documents based on semantic similarity <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>, <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. This is a fast and scalable step.
2.  **Cross-encoder for Re-ranking**: The smaller set of retrieved documents is then passed through a cross-encoder (reranker) for a more fine-grained similarity assessment <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>. This improves the accuracy of the final selection of documents provided to the LLM <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.

## Practical Implementation Notes
*   **Prototyping**: Google Collab is useful for prototyping RAG solutions due to free hardware accelerators <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>.
*   **Orchestration**: LlamaIndex and LangGraph are options for the orchestration layer <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. LlamaIndex can quickly set up a basic RAG solution <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **Embedding Models**: Both closed (e.g., OpenAI's text embedding ADA/three large) and open (e.g., Nvidia, B AI) embedding models can be used <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>, <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
*   **Vector Database**: Qdrant is highlighted for its excellent scalability from a few documents to hundreds of thousands <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>, <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.
*   **Language Models**: Closed models like OpenAI's GPT-3.5 Turbo or GPT-4 offer simplicity via APIs <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>, <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>. Open models include those from Meta or Qwen <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. For production with Docker, Olama or Hugging Face's text generation inference can serve models like Llama 3.2 or Qwen 3.4 billion <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

### [[monitoring_tracing_and_evaluation_in_rag_systems|Monitoring, Tracing, and Evaluation]]
*   **Monitoring and Tracing**: Tools like Langsmith or Phoenix Arise are crucial for troubleshooting and understanding component performance in a RAG solution <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>, <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.
*   **[[metrics_for_evaluating_rag_systems|Evaluation]]**: Frameworks like Ragas are essential for testing the quality of RAG solutions across a larger set of questions, working with LLMs to make the evaluation process smoother <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>, <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>, <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.

For production, Docker Compose can be used to set up images for data ingestion, vector databases (Qdrant), front-end apps, LLM serving (Olama/Hugging Face TGI), tracing (Phoenix), and [[metrics_for_evaluating_rag_systems|evaluation]] (Ragas) <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.