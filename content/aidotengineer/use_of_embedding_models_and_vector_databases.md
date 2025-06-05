---
title: use of embedding models and vector databases
videoId: 2CXn-CByNoo
---

From: [[aidotengineer]] <br/> 

Embedding models and vector databases are crucial components in a Retrieval Augmented Generation (RAG) stack <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. They enable the system to perform semantic searches and retrieve relevant information effectively.

## Embedding Models

Embedding models transform text (or other data) into numerical vectors (embeddings) that capture their semantic meaning. This allows for efficient comparison and retrieval of semantically similar items.

### Types of Embedding Models
*   **Closed Models**: These models are often used via APIs, simplifying their integration and use <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. An example mentioned is OpenAI's `text-embedding-ada-002` or `text-embedding-3-large` <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **[[open_source_models_vs_closed_models | Open Models]]**: These models can be downloaded and run locally, providing more control and often being preferred for production environments <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Examples include models from Nvidia or BAAI <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. The BGE small model from Hugging Face is specifically mentioned as an [[open_source_models_vs_closed_models | open solution]] <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

### How Embedding Models Work

Two main types of encoders are discussed in the context of semantic comparison:

*   **Cross-Encoder**:
    *   Objective: To semantically compare a query with a document <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   Process: Both the query and the document are sent to a BERT model (the encoder from the original transformer model), then passed to a classifier <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   Output: A result between 0 and 1, indicating semantic similarity <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   Characteristics: Excellent for additional accuracy but can be slow and not [[scaling_ai_models_and_their_impact_on_development_tools | scalable]], especially with larger documents <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. It's best used post-retrieval (as a re-ranker) because it only works with a few documents <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Bi-Encoder**:
    *   Objective: To provide a fast and [[scaling_ai_models_and_their_impact_on_development_tools | scalable]] solution for information retrieval <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   Process: Uses two separate encoders (BERT layers) for the query and the document, each followed by pooling and embedding layers <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. The similarity between the query and document embeddings is then compared using metrics like cosine similarity <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   Characteristics: Fast and [[scaling_ai_models_and_their_impact_on_development_tools | scalable]], making it excellent for information retrieval <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. It's ideally placed where the vector data is, comparing the query with multiple documents <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Vector Databases

Vector databases store embeddings and allow for efficient similarity search, which is a core part of the RAG retrieval step <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### Role in RAG
The first and most important step in RAG is the retrieval step, where a semantic search is performed through a vector database to retrieve relevant documents based on the user's query <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The retrieved information is then combined with the original query as context for the language model <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Specific Vector Database Solutions
*   **Qdrant**: An excellent solution for vector databases because it [[scaling_ai_models_and_their_impact_on_development_tools | scales]] very well, handling anything from a few documents to hundreds of thousands <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. It can be used as an in-memory solution for prototyping <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. In a production environment, Qdrant can be deployed via Docker <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.
*   **In-memory vector database**: Used for simple prototyping setups in environments like Google Colab <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Querying a Vector Database
In a naive RAG solution, a user's query is embedded and then compared to documents available in the vector database <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Relevant documents are retrieved and passed along with the query to the large language model as context for generating a response <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. LlamaIndex can be used to read HTML files into documents and store them in an in-memory vector database for basic RAG functionality <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Example of improved RAG with components:
1.  Read HTML files from a directory using LlamaIndex's simple directory reader <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
2.  Use Qdrant as the vector database <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
3.  Set the default embedding model (e.g., an [[open_source_models_vs_closed_models | open model]] like BGE small) <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
4.  Optionally, configure the Large Language Model (LLM) (e.g., GPT-4) <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
5.  Introduce a re-ranker (cross-encoder) in the post-retrieval step to improve accuracy by re-ranking the top results <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. Cohere's model is mentioned as a closed model for prototyping, while Nvidia's solution is preferred for production <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.