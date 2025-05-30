---
title: Introduction to Retrieval Augmented Generation RAG
videoId: BrUW8_cCTew
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation | Retrieval Augmented Generation (RAG)]] is a powerful technique for enhancing AI agents by providing them with external knowledge <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It enables large language models (LLMs) to answer user questions using information beyond their initial training data <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. This article provides a concise overview of [[basics_of_retrieval_augmented_generation_rag | how RAG works]] and its practical applications.

## What is RAG?

[[retrieval_augmented_generation | RAG]] stands for [[retrieval_augmented_generation | Retrieval Augmented Generation]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Its core purpose is to inject external, up-to-date, or specific knowledge into a large language model's context <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This allows the LLM to provide more informed and accurate answers to user queries <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## How RAG Works

At its essence, [[retrieval_augmented_generation | RAG]] operates by directing a user's question to a knowledge database before it reaches the LLM <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This database employs vector mathematics to identify the most relevant knowledge pertaining to the user's question <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This retrieved knowledge then provides additional context to the LLM, enabling it to formulate a better answer than it could with only its pre-trained information <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Detailed Process

1.  **Document Ingestion and Chunking:**
    *   Documents intended for the knowledge database are split into smaller, manageable chunks <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This ensures that the entire document isn't returned as context, which could be too large for the LLM <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   Chunk sizes can vary (e.g., 100 or 1,000 characters) and can be optimized based on the use case <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
    *   LangChain offers various loaders, including a directory loader, to pull documents into the system <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

2.  **Vectorization and Storage:**
    *   Each document chunk is transformed into a numerical representation called a vector <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   These vectors are then stored as embeddings in a vector database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Chroma is a common choice for local vector databases <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   An embedding function, often from an open-source model like those on Hugging Face, is used for this conversion <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

3.  **Query Processing and [[Contextual retrieval in RAG | Retrieval]]:**
    *   When a user asks a question, the same embedding function is applied to create a vector for that question <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   This question vector is then used to query the vector database <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
    *   Mathematical functions like cosine similarity are used to determine how similar the user's question vector is to the stored document chunk vectors <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
    *   The "top K" (e.g., five) most similar document chunks are retrieved <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

4.  **Augmentation and Generation:**
    *   The retrieved chunks of knowledge are fed into the large language model as additional context within the prompt <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   The LLM then uses this augmented prompt, combining the original user question with the relevant external context, to formulate its answer <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Example Scenario
Consider a database filled with meeting summaries <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If a user asks, "What are the action items from the meeting on the 20th?" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, [[retrieval_augmented_generation | RAG]] would find the relevant meeting summary, extract the action items, and provide them to the LLM, which then generates a concise response <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Practical Implementation with Llama 3.1

[[retrieval_augmented_generation | RAG]] can be implemented to create powerful chatbots that interact with local documents, such as PDF and text files <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. A demonstrated example involves building such a chatbot using the Llama 3.1 405 billion parameter model <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

Key components used in the implementation:
*   **LangChain:** A framework for developing applications powered by language models <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Streamlit:** Used for creating the user interface of the chatbot <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Hugging Face:** Provides access to various models, including Llama 3.1 <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Chroma:** Employed as the local, in-memory vector database for storing document embeddings <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

The process involves:
1.  Loading environment variables for the model (defaulting to Llama 3.1) and the document directory <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
2.  Instantiating the Llama 3.1 model, potentially via a Hugging Face inference endpoint if local resources are insufficient <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
3.  Loading and chunking documents (e.g., PDFs and text files) from a specified directory using LangChain's directory loader <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
4.  Creating an embedding function and initializing a Chroma vector database with the chunked documents <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
5.  Defining a query function that performs a similarity search on the vector database to retrieve the most relevant document chunks based on a user's question <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
6.  Constructing the prompt for the LLM by combining the retrieved context with the user's question <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
7.  Setting up the Streamlit UI to display messages and handle user input, dynamically updating the chat based on LLM responses <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

This setup allows the chatbot to accurately answer questions by retrieving specific details (e.g., "wellness programs" or "team survey results") or summarizing information (e.g., "meeting discussions") from the local documents <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

## Conclusion and Future of RAG

This basic understanding of [[retrieval_augmented_generation | RAG]] provides a solid foundation <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. While this covers the fundamental mechanism, there are numerous ways to optimize and enhance [[retrieval_augmented_generation | RAG]] systems, such as implementing tool calling for AI agents to decide when to engage [[retrieval_augmented_generation | RAG]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. [[Retrieval augmented generation for AI | RAG]] is just the beginning of what can be achieved in [[retrieval_augmented_generation | AI agents]] <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.