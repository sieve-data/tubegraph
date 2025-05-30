---
title: Creating and utilizing a vector database for RAG
videoId: BrUW8_cCTew
---

From: [[colemedin]] <br/> 

Retrieval Augmented Generation (RAG) is a powerful component of [[agentic_rag_strategy_and_implementation | AI agents]] that allows Large Language Models (LLMs) to access and incorporate external knowledge beyond their initial training data [00:00:04]. This enables LLMs to answer user questions with more current and specific information [00:00:12].

## How RAG Works

At its core, RAG involves a user sending a question to an LLM, but before the LLM processes it directly, the question is first routed to a database of knowledge [00:00:38]. Within this database, complex vector mathematics are used to match the user's question with the most relevant information [00:00:48]. This retrieved knowledge then provides extra context to the LLM, allowing it to formulate a more informed response than it could using only its pre-trained data [00:00:56].

For example, if the knowledge database contains meeting summaries, a user could ask, "What are the action items from the meeting on the 20th?" [00:01:08]. The RAG system would provide the relevant meeting information to the LLM, enabling it to generate a concise answer to the user's query [00:01:17].

## Preparing Documents for a Vector Database

To integrate external knowledge into a RAG system, documents must be processed and stored in a vector database [00:01:28].

The process involves:
1.  **Chunking Documents**: Each document is split into smaller, manageable "chunks" [00:01:35]. This is done to ensure that when relevant knowledge is retrieved for an LLM, it's not the entire document but only concise, pertinent sections [00:01:42]. Chunk sizes can vary, such as 100 or 1,000 characters [00:01:50].
2.  **Creating Embeddings (Vectors)**: Each chunk is then transformed into a numerical representation called a vector [00:01:54]. These vectors are stored as embeddings in the vector database [00:01:56]. This mathematical representation allows for comparison and retrieval of similar text [00:02:02].

## Querying the Vector Database

When a user asks a question, the RAG system performs the following steps:
1.  **Vectorize User Question**: The user's question is also converted into a vector using the same embedding function used for the document chunks [00:02:20].
2.  **Similarity Search**: This question vector is then used to query the [[choosing_vector_databases_for_rag_applications | vector database]] [00:02:27]. Mathematical functions like cosine similarity are applied to find the most similar document chunks to the user's question [00:02:05].
3.  **Retrieve Top K Chunks**: The system retrieves the "top K" most similar chunks (e.g., the five most similar chunks) from the database [00:02:37].
4.  **Augment LLM Prompt**: These retrieved chunks are then added as context to the user's original question, forming an augmented prompt that is fed into the LLM [00:02:42].
5.  **Generate Response**: The LLM uses this augmented prompt to generate a comprehensive and contextually relevant answer to the user's question [00:02:46].

## Building a RAG Chatbot for Local Documents

A practical implementation of RAG can be seen in building a chatbot that interacts with local documents using models like Llama 3.1 [00:03:04].

### Implementation Steps

The following steps outline how to implement a RAG system to chat with PDF and text documents:

1.  **Import Packages**: Essential libraries include:
    *   LangChain: For document loading and processing [00:03:40].
    *   Streamlit: For creating the user interface [00:03:42].
    *   Hugging Face: For accessing LLMs like Llama 3.1 and embedding models [00:03:44].
2.  **Load Environment Variables**: Define variables such as the default LLM (e.g., Llama 3.1 405B) and the directory containing local documents [00:04:00].
3.  **Instantiate Local Model**: Access the LLM, either through a Hugging Face inference endpoint (for large models that cannot run locally) or by directly downloading the model if the computer has sufficient resources [00:04:21]. Streamlit caching can prevent re-instantiation of the model upon UI refresh [00:04:13].
4.  **Load and Chunk Documents**:
    *   Use LangChain's `DirectoryLoader` to ingest documents from a specified directory [00:04:58]. LangChain supports various loaders for different file types like PDFs, text documents, Word documents, HTML, or Markdown files [00:09:03].
    *   Split the loaded documents into chunks, for example, with a chunk size of 1,000 characters [00:05:14].
5.  **[[Setting up a Superbase vector store for RAG | Set Up Vector Database]]**:
    *   Chroma is a suitable choice for a local, in-memory vector database [00:05:31]. It can also be configured for persistent storage [00:05:35].
    *   Create an embedding function using an open-source Hugging Face embedding model [00:05:52]. This function generates vectors for document chunks and user questions [00:05:57].
    *   Instantiate the Chroma vector database using the loaded document chunks and the embedding function [00:06:03]. Caching this instance prevents repeated creation on UI refreshes [00:06:16].
6.  **Query Documents**:
    *   Implement a function to query the vector database, specifically using Chroma's `similarity_search` function [00:06:44].
    *   This function retrieves the top 5 most related document chunks based on the user's question [00:06:50].
7.  **Prompt the LLM**:
    *   Construct the LLM prompt by first querying the relevant document chunks based on the user's latest message [00:07:10].
    *   Format the prompt to include the retrieved context and then the user's actual question [00:07:16].
    *   Invoke the LLM (e.g., Hugging Face's `chat` object) with the augmented prompt to get a response [00:07:25].
8.  **Streamlit UI**:
    *   Set up a Streamlit UI to display chat messages and handle user input [00:08:01].
    *   User messages are added to the UI and session state, followed by the LLM's response [00:08:22].

### Demonstration and Results

Using example meeting notes (PDF and text files), the chatbot demonstrated its ability to accurately answer questions by retrieving relevant information from the local documents [00:08:41]:
*   When asked about "wellness programs Emily proposed," it correctly identified "yoga sessions and Mental Health Resources" [00:09:45].
*   For "results of the team survey," it accurately summarized that "overall morale is high but some team members Express concerns about workload and deadlines" [00:10:02].
*   When prompted to summarize "what was discussed in the meeting on the 22nd," it provided a concise summary of topics like "review of previous action items, Art and Design updates, server stress test preparation, marketing metas and adjustments, and focus group planning for cyber Warriors" [00:10:35].

These examples highlight the RAG system's effectiveness in [[Contextual retrieval in RAG | contextual retrieval]] and summarization using local data, demonstrating its ability to find the most relevant chunks and provide them to the LLM for concise answers [00:10:21].

## Advanced RAG Implementation

While this provides a basic understanding, [[advanced RAG implementation techniques | RAG can be optimized]] and integrated into more complex [[agentic_rag_strategy_and_implementation | AI agents]] that dynamically decide when to use RAG capabilities [00:02:56]. Further exploration into advanced techniques for [[Efficient document management with a vector database | efficient document management]] and retrieval is possible [00:11:17].