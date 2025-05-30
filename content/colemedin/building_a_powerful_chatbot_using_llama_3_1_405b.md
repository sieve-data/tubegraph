---
title: Building a powerful chatbot using Llama 3 1 405B
videoId: BrUW8_cCTew
---

From: [[colemedin]] <br/> 

This article outlines how to build a powerful chatbot that can interact with local documents, leveraging the [[metas_llama_32_language_models | Llama 3.1 405 billion parameter model]] through Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This approach allows the chatbot to answer user questions using external knowledge beyond its initial training data <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Understanding Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a crucial technique for AI agents, enabling them to incorporate external knowledge into a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This means the LLM can answer user questions with more information than it was originally trained on <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### How RAG Works <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

1.  **User Query and Database Interaction**: When a user sends a question to the LLM, it is first directed to a knowledge database <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
2.  **Vector Mathematics**: Within this database, complex vector mathematics is used to match the user's question with the most relevant information <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
3.  **Context Provision**: This retrieved knowledge is then sent to the LLM, providing it with additional context to formulate a more informed answer <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
    *   For example, if the database contains meeting summaries, a user could ask "What are the action items from the meeting on the 20th?" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The relevant summary would be retrieved, allowing the LLM to provide a concise response <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Incorporating Documents into the Knowledge Database <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>

To prepare documents for the knowledge database:
1.  **Document Chunking**: Documents are split into smaller, concise chunks (e.g., 100 to 1,000 characters) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This is done to avoid sending entire documents as context to the LLM <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
2.  **Vectorization**: Each chunk is converted into a vector (a mathematical representation) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
3.  **Storage in Vector Database**: These vectors are then stored as embeddings in a vector database <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Querying the Vector Database <a class="yt-timestamp" data-t="02:17:47">[02:17:47]</a>

1.  **User Question Vectorization**: When a user asks a question, the same embedding function used for document chunks creates a vector for the user's question <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
2.  **Similarity Matching**: This question vector is matched within the vector database to find the most relevant knowledge by determining similarity (e.g., using cosine similarity) <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
3.  **Top K Chunks Retrieval**: The system returns the "top K" most similar document chunks (e.g., five most similar chunks) <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
4.  **LLM Prompting**: These retrieved chunks are then fed into the prompt for the LLM as context <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>, enabling it to answer the user's question accurately <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

## Building the Chatbot with Llama 3.1 405B

This section details the practical steps to build a chatbot that can interact with local text and PDF documents using [[metas_llama_32_language_models | Llama 3.1 405B]] <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. The code is available on a GitHub repository <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

### Implementation Steps

1.  **Import Packages**: Essential packages include LangChain for document loading and processing, Streamlit for the user interface, and Hugging Face for access to the [[metas_llama_32_language_models | Llama 3.1 405B]] model <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
2.  **Load Environment Variables**: This involves defining the default model (Llama 3.1 405B) and the directory containing local documents to be chatted with <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
3.  **Get Local Model Instance**: A function `get_local_model` is created and cached with Streamlit to prevent re-instantiating the model every time the UI reloads <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
    *   Due to the size of the [[metas_llama_32_language_models | Llama 3.1]] model, a Hugging Face inference endpoint is used instead of pulling the model locally for most computers <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. However, code is provided to run Llama locally if the computer is powerful enough <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
4.  **Load Documents Function (`load_documents`)**: This function uses the LangChain directory loader to ingest all documents from a specified directory <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. It supports various document types including text and PDFs <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
5.  **Chunk Documents**: The loaded documents are then split into chunks, typically around 1,000 characters, using a text splitter <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
6.  **Initialize Vector Database (`get_vector_database`)**:
    *   Chroma is utilized as a local, in-memory vector database for efficient storage and retrieval <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. Chroma can also be saved to disk for persistent storage <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.
    *   An embedding function is created using an open-source Hugging Face embedding model <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. This function generates vectors for both document chunks and user questions <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
    *   The `chroma` vector database instance is created using the documents and the embedding function <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. This function is also cached by Streamlit <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.
7.  **Query Documents Function (`query_documents`)**: Given a user question, this function uses Chroma's similarity search to find the five most related document chunks from the vector database <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
8.  **Prompt LLM Function (`prompt_llm`)**:
    *   This function retrieves the last user message and queries the documents based on it <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.
    *   It formats the prompt by providing the retrieved context (from the vector database) followed by the user's actual question <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.
    *   The `ChatHuggingFace` object is invoked with a modified list of messages where the last user message is augmented with the extra context <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. The response from the LLM is then returned <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

### Streamlit User Interface (UI) <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>

The Streamlit UI in the `main` function orchestrates the chatbot's interaction:
*   Sets a title "Chat with local documents" <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   Initializes and displays chat messages on the UI <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
*   Handles user input, adds the user message to the UI and session state <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   Calls `prompt_llm` to get a response from the LLM <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
*   Adds the LLM's response to the UI and session state <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.

## Testing the Chatbot

To test the chatbot, place your local PDF and text documents in the designated directory <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. The chatbot is run using the command `streamlit run [your_python_script_name]` <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

### Example Queries and Responses:

*   **Question**: "What's included in the wellness programs Emily proposed?" <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>
    *   **Response**: "yoga sessions and Mental Health Resources" <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>
*   **Question**: "What are the results of the team survey?" <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>
    *   **Response**: "overall morale is high but some team members Express concerns about workload and deadlines" <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>
*   **Question**: "What was discussed in the meeting on the 22nd?" <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>
    *   **Response**: "review of previous action items Art and Design updates server stress test preparation marketing metas and adjustments and focus group planning for cyber Warriors" <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>

The chatbot successfully retrieves relevant information and concisely answers questions by leveraging the [[metas_llama_32_language_models | Llama 3.1 405B]] model with the RAG system <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.