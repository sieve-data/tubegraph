---
title: Implementing RAG with local text and PDF documents
videoId: BrUW8_cCTew
---

From: [[colemedin]] <br/> 

[[Retrieval Augmented Generation RAG and its challenges | Retrieval Augmented Generation (RAG)]] is a powerful technique for integrating external knowledge into large language models (LLMs), allowing them to answer user questions with more information than their training data provides <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article details how to implement RAG to enable a chatbot to interact with local text and PDF documents, using the Llama 3.1 405B parameter model <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## What is RAG?

In its essence, [[Retrieval Augmented Generation RAG and its challenges | RAG]] functions by directing a user's question to a knowledge database before it reaches the LLM <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This database employs vector mathematics to identify and retrieve the most pertinent knowledge related to the user's query <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This retrieved knowledge then provides extra context to the LLM, enabling it to formulate a more informed and accurate response than it could with only its pre-trained data <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. For example, if the database contains meeting summaries, an LLM can answer specific questions like "What are the action items from the meeting on the 20th?" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## How RAG Works

The process of RAG involves several key steps:

1.  **Document Chunking**: For every document intended for the knowledge database, the content is split into smaller, concise chunks <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This is done to ensure that only relevant portions of a document are returned as context to the LLM, rather than the entire document <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Chunk sizes can vary, such as 100 or 1,000 characters <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  **Vectorization**: Each document chunk is converted into a numerical vector (embedding) using an embedding function <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. These vectors are then stored in a vector database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
3.  **Similarity Search**: When a user asks a question, the question itself is also converted into a vector using the same embedding function <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This query vector is then used to perform a similarity search within the vector database <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Mathematical functions like cosine similarity are used to determine how similar the user's question is to the stored document chunks <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
4.  **Context Retrieval**: The system returns the top 'K' most similar chunks (e.g., the five most similar chunks) from the database <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
5.  **Augmented Prompt**: These retrieved chunks are then fed into the large language model as additional context within the prompt <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
6.  **Response Generation**: The LLM uses this augmented prompt to formulate an answer to the user's question <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Building a Chatbot for Local Documents

To build a chatbot that can chat with local text and PDF documents using [[Retrieval Augmented Generation RAG and its challenges | RAG]], a Python implementation can be followed using libraries like LangChain, Streamlit (for the UI), and Hugging Face (for model access) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Implementation Steps

1.  **Import Packages and Load Environment Variables**:
    *   Required packages include LangChain, Streamlit, and Hugging Face <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
    *   Environment variables, such as the default Llama 3.1 405B model and the directory containing local documents, are loaded <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

2.  **Get the Local Model**:
    *   A function `get_local_model` is created to instantiate the LLM <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   This function is cached with Streamlit to prevent re-instantiation upon UI reloads <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   While Llama 3.1 405B is massive and often run via Hugging Face inference endpoints, local execution is possible for capable machines <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

3.  **Load and Chunk Documents**:
    *   The `load_documents` function uses LangChain's `DirectoryLoader` to read all documents from a specified directory (e.g., `rag_directory`) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   Documents are then split into chunks, typically around 1,000 characters, though chunking strategies can be experimented with <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. LangChain offers various loaders for different file types like Word, HTML, or Markdown <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

4.  **Initialize Vector Database**:
    *   Chroma is recommended for a local vector database, running in memory or saved to disk for persistence <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   An open-source Hugging Face embedding model is used to create the embedding function for converting both document chunks and user questions into vectors <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    *   The Chroma vector database instance is created using these documents and the embedding function <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This instance is also cached <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

5.  **Query Documents**:
    *   The `query_documents` function uses Chroma's `similarity_search` to find the most relevant knowledge given a question <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   It retrieves the five most related document chunks (top K similar chunks) <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

6.  **Prompt the Large Language Model**:
    *   The `prompt_llm` function takes the last user message and uses it to query the documents <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   The retrieved context is then formatted into a prompt, alongside the user's actual question <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   A `ChatHuggingFace` object is defined with the selected LLM <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   The LLM is invoked with the full message list, but the last message is replaced with the user's query augmented by the retrieved context <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

7.  **Define Streamlit UI**:
    *   The `main` function sets up the Streamlit user interface <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
    *   It includes a title, initializes the state, displays messages, and handles user input <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   User messages are added to the UI and session state, the LLM is prompted, and the response is displayed <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Demonstration

A chatbot can be run using the command `streamlit run [script_name.py]`, allowing interaction with local PDF and text documents <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. For example, querying "What's included in the wellness programs Emily proposed?" successfully retrieves "yoga sessions and Mental Health Resources" <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Another example, "What are the results of the team survey?" accurately yields "overall morale is high but some team members Express concerns about workload and deadlines" <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The system can also summarize information, such as "What was discussed in the meeting on the 22nd?", providing a concise summary of topics like "review of previous action items, Art and Design updates, server stress test preparation, marketing metas and adjustments and focus group planning for cyber Warriors" <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.

This implementation provides a solid foundation for [[Retrieval Augmented Generation RAG and its challenges | RAG]] systems, with many avenues for further optimization and [[advanced_rag_implementation_techniques | advanced RAG implementation techniques]] <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Future developments might include [[Agentic RAG strategy and implementation | agentic RAG strategies]] where an agent decides when to employ RAG, rather than always performing it <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.