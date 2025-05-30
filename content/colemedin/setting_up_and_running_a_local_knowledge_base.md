---
title: Setting up and running a local knowledge base
videoId: uWDocIoiaXE
---

From: [[colemedin]] <br/> 

This article outlines how to set up and run a local knowledge base using ChromaDB, which is integrated with AI agents for enhanced information retrieval and reasoning. This setup focuses on a simple yet powerful agentic Retrieval-Augmented Generation (RAG) system, particularly useful for extracting in-depth insights.

## Core Components
The local knowledge base serves as a crucial tool for an AI agent, allowing it to look up knowledge and pull relevant context from a vector database to answer user questions <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

Key components include:
*   **Vector Database (ChromaDB)**: Used to store and retrieve document chunks. The setup demonstrated is designed for simplicity, clearing and reloading the database with PDFs from a local directory each time the script is run <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>.
*   **Embedding Model**: Essential for converting user queries into numerical vectors (embeddings) that can be matched against the relevant context stored in the vector database <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. The system uses a local embedding model from Hugging Face <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
*   **PDF Loader and Splitter (LangChain)**: Used to load PDF documents and split them into manageable chunks before they are embedded and stored <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

## Knowledge Base Setup Process

### 1. Ingesting PDFs into ChromaDB
To set up the local knowledge base, the process involves loading, splitting, and embedding PDF documents, then storing them in ChromaDB.

*   **Data Directory**: Place your PDF files in a `data` directory <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. Example fake data generated from Claude is provided in the GitHub repository <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   **Ingestion Script**: A Python script (`ingest_PDFs.py`) utilizes LangChain to load PDFs and split them into chunks <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.
*   **Clearing and Loading**: The script first clears the entire vector database to prevent duplicate data, then creates new embeddings for all chunks using the specified embedding model, and finally inserts them into the ChromaDB <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.
*   **Execution**: Run the ingestion script from your terminal: `python ingest_PDFs.py` <a class="yt-timestamp" data-t="15:33:00">[15:33:00]</a>. This process runs locally and quickly sets up the knowledge base <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

### 2. Configuring Local Language Models (LLMs) with Ollama

For the AI agent to leverage the knowledge base, appropriate language models need to be set up, ideally with extended context limits for better performance in RAG scenarios. [[incorporating_ai_models_and_databases_in_a_local_setup | Incorporating AI models and databases in a local setup]] is crucial for maintaining a local setup.

*   **Ollama Installation**: Install Ollama from `ollama.com` <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
*   **Model Selection**: Search for models like DeepSeek R1, which offers smaller "distill" versions (e.g., 7 billion parameter) that are feasible to run locally <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. These models are fine-tuned versions of competitors like Qwen and Llama, using data from DeepSeek R1 to become smaller reasoning LLMs <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Increasing Context Limit**: By default, Ollama models often have a limited context window (e.g., 2,048 tokens), which is insufficient for many use cases <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>.
    *   Navigate to the Ollama models folder.
    *   Create a simple model file (e.g., `deepseek-r1-7b-8k.modelfile`) with two lines:
        *   `FROM <model_ID>` (e.g., `deepseek-r1:7b`) <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>
        *   `PARAMETER num_ctx <desired_tokens>` (e.g., `PARAMETER num_ctx 8096`) <a class="yt-timestamp" data-t="16:57:00">[16:57:00]</a>. A context limit of 8,096 tokens is recommended for these models <a class="yt-timestamp" data-t="17:03:00">[17:03:00]</a>.
    *   Run `ollama create <new_model_name> -f <modelfile_name>` (e.g., `ollama create deepseek-r1-7b-8k -f deepseek-r1-7b-8k.modelfile`) <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
    *   Ollama will download the base model if not present and then apply the configuration without creating a duplicate copy on your hard drive <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>.
    *   These models can then be used as the reasoning model (e.g., DeepSeek R1) and the primary conversation driver (e.g., Qwen Instruct) <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.
*   **Hugging Face Integration**: Alternatively, models can be accessed directly from Hugging Face via their inference endpoints or by installing them locally <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. The setup supports both Hugging Face API models and Ollama local models <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

## Integrating the Knowledge Base with the AI Agent

The knowledge base is integrated into an agentic RAG system using the Small-Agents framework, which simplifies complex workflows <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

*   **Agent Configuration**:
    *   A primary LLM (e.g., Qwen or Llama, a non-reasoning LLM) serves as the "fast agent" driving the conversation <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
    *   A reasoning LLM (e.g., DeepSeek R1) is set up as a tool <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
    *   Small-Agents allows for step-by-step problem breakdown, where the primary LLM can decide when to call the knowledge lookup tool <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   **RAG Tool (`rag_with_reasoner`)**:
    *   This is a single tool for the primary LLM that accepts a user query <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
    *   It performs a similarity search in the vector database using the embedded user query, retrieving the top relevant chunks of information <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
    *   The retrieved context is then fed into the reasoning LLM (R1) to extract in-depth insights <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.
    *   The reasoning LLM can also suggest a better query back to the primary LLM if the initial retrieval was insufficient, enabling an iterative RAG loop <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>.
    *   The reasoning LLM is configured with a maximum of two reasoning steps to prevent hallucination <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.
    *   The conversation history is maintained for the reasoning LLM to consider previous prompts and retrieved information <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.

## User Interface (UI)

Small-Agents integrates directly with Gradio UI, allowing for a user interface to be built with a single line of code <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. This UI automatically handles conversation history and displays the steps, function calls, and execution logs of the agent, providing transparency into its thought process <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.

This [[integrating_knowledge_bases_with_ai | integrating knowledge bases with AI]] approach creates a powerful agentic RAG setup that combines the slow, powerful reasoning of models like DeepSeek R1 with faster, lighter models for nimble conversation flow <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.