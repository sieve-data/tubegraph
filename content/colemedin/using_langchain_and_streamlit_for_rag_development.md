---
title: Using LangChain and Streamlit for RAG development
videoId: BrUW8_cCTew
---

From: [[colemedin]] <br/> 

Retrieval Augmented Generation (RAG) is a powerful component of [[setting_up_ai_agents_with_langchain_and_streamlit | AI agents]] that allows Large Language Models (LLMs) to incorporate external knowledge and provide more informative answers to user questions than what they were initially trained on <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This article outlines the fundamental concepts of RAG and demonstrates how to implement a RAG-powered chatbot using [[setting_up_ai_agents_with_langchain_and_streamlit | LangChain]] and [[using_streamlit_and_python_for_web_development | Streamlit]].

## Understanding Retrieval Augmented Generation (RAG)

In essence, RAG operates by directing a user's question to a knowledge database before it reaches the LLM <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Complicated vector mathematics are employed to match the user's question with the most relevant information within the database <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This retrieved knowledge then provides extra context to the LLM, enabling it to answer the question more comprehensively <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>, <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. An example use case is querying a database of meeting summaries to find action items from a specific date <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### RAG Workflow

The process of integrating documents into a RAG system involves several key steps:

1.  **Document Chunking**: Documents are split into smaller, concise chunks (e.g., 100 or 1,000 characters) to optimize the amount of context returned to the LLM <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  **Vectorization (Embeddings)**: Each document chunk is transformed into a numerical vector (embedding) using an embedding function <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
3.  **Vector Database Storage**: These vectors are then stored in a [[creating_and_utilizing_a_vector_database_for_rag | vector database]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
4.  **Querying**: When a user asks a question, the question itself is converted into a vector using the same embedding function <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>, <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
5.  **Similarity Search**: The user's question vector is then matched against the document chunk vectors in the [[creating_and_utilizing_a_vector_database_for_rag | vector database]] using similarity measures like cosine similarity <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
6.  **Context Provision**: The top-K most similar document chunks are retrieved and sent to the LLM as additional context for generating a precise answer <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>, <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Building a RAG Chatbot with LangChain and Streamlit

A practical application of RAG is building a chatbot capable of interacting with local documents, such as text files and PDFs <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The following steps outline how to create such a chatbot using [[setting_up_ai_agents_with_langchain_and_streamlit | LangChain]] for backend logic and [[using_streamlit_and_python_for_web_development | Streamlit]] for the user interface.

### Prerequisites and Setup

The core packages required for this implementation include:
*   [[setting_up_ai_agents_with_langchain_and_streamlit | LangChain]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
*   [[using_streamlit_and_python_for_web_development | Streamlit]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   Hugging Face (for Llama 3.1 model access and embedding models) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>

Environment variables are used to load the LLM (defaulting to Llama 3.1 405B) and the directory containing local documents <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Core Components

1.  **Local Model Instantiation**:
    *   A function is used to get the local LLM. This function is cached with [[using_streamlit_and_python_for_web_development | Streamlit]] to prevent re-instantiation upon UI reloads <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   For Llama 3.1, a Hugging Face inference endpoint is typically used due to the model's large size, which makes local execution challenging for most computers <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. However, code for local execution is available if a powerful enough machine is used <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

2.  **Document Loading and Chunking**:
    *   The [[setting_up_ai_agents_with_langchain_and_streamlit | LangChain]] `DirectoryLoader` is used to load all documents (e.g., PDFs and text files) from a specified directory <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>, <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   Loaded documents are then split into chunks, often with a `chunk_size` of 1,000 characters <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. [[setting_up_ai_agents_with_langchain_and_streamlit | LangChain]] supports various loaders for different file types like Word, HTML, or Markdown <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

3.  **Vector Database Initialization**:
    *   Chroma is used as a local, in-memory [[creating_and_utilizing_a_vector_database_for_rag | vector database]] <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. It can also be configured for persistent storage <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
    *   An open-source Hugging Face embedding model generates the vectors for both document chunks and user questions <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   The `chroma` [[creating_and_utilizing_a_vector_database_for_rag | vector database]] instance is created using the loaded documents and the embedding function <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This database instance is also cached by [[using_streamlit_and_python_for_web_development | Streamlit]] <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

4.  **Document Querying**:
    *   A function queries the [[creating_and_utilizing_a_vector_database_for_rag | vector database]] for the most relevant knowledge based on a user's question <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
    *   It uses `chroma.similarity_search` to retrieve the top five most related document chunks <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>, <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

5.  **Prompting the LLM**:
    *   The last user message is used to query the documents and retrieve relevant context <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   The prompt for the LLM is formatted to include the retrieved context followed by the user's actual question <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   The LLM generates a response by invoking a `ChatHuggingFace` object with the full message history, where the last message is augmented with the RAG context <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### Streamlit UI Implementation

The [[using_streamlit_and_python_for_web_development | Streamlit]] user interface handles the display of messages and user input:
*   A title, "Chat with Local Documents", is displayed <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   The initial state for [[using_streamlit_and_python_for_web_development | Streamlit]] messages is initialized <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   All messages are displayed on the UI <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   User input is captured, added to the UI, and stored in the session state <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   The LLM is prompted with the user's message, and the generated response is added to the UI and session state <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Running the Chatbot

The chatbot can be run using the command `streamlit run your_script_name.py` <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
The system effectively retrieves information from various local documents, including PDFs and text files, and provides concise, accurate answers by feeding the relevant chunks to the LLM <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>, <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

> [!INFO] RAG Optimization
> While this provides a basic understanding of RAG, there are numerous ways to optimize it. Future developments may include using [[setting_up_ai_agents_with_langchain_and_streamlit | AI agents]] that decide when RAG is necessary, rather than applying it to all queries <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.