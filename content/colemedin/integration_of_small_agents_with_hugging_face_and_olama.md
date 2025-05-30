---
title: Integration of small agents with hugging face and olama
videoId: uWDocIoiaXE
---

From: [[colemedin]] <br/> 

This article explores the integration of small agents with both Hugging Face and Olama to create powerful, local, and efficient AI agentic workflows. The focus is on leveraging the DeepSeek R1 reasoning LLM within an agentic Retrieval Augmented Generation (RAG) setup <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach highlights the potential for advanced [[ai_agents_and_their_development | AI agents and their development]] even with smaller, locally run models <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Agentic RAG Setup Overview

The core idea is to combine powerful, but slow, reasoning models like DeepSeek R1 with faster, more lightweight models that direct the overall conversation or [[ai_agents_and_their_development | agentic flow]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. In this setup, DeepSeek R1 acts as a tool for the primary, faster Large Language Model (LLM), providing access to deeper reasoning when needed, albeit at the expense of a slower response time <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The architecture involves a primary LLM (referred to as a "fast agent," e.g., Llama or Qwen) that breaks down problems into steps <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. When it requires knowledge lookup, it calls a dedicated tool. This tool, an R1-driven RAG tool, is responsible for extracting in-depth insights from a knowledge base <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Workflow Steps
1.  **User Query:** The user's question is passed to the primary LLM <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
2.  **Tool Call:** The primary LLM, when needed, calls the RAG tool <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  **Retrieval:** The RAG tool performs a retrieval from a vector database to find relevant context for the user's question <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
4.  **Reasoning with R1:** The retrieved context is fed into DeepSeek R1, which then extracts the necessary insights <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
5.  **Response to Primary LLM:** R1's insights are returned to the primary agent to continue the conversation <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This setup enables a nimble conversation while leveraging the reasoning power of R1 for complex inquiries <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Even smaller distill R1 models have shown incredible results <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Components and Their Integration

### Small Agents Framework
Small Agents by Hugging Face is used as the framework for building this agentic workflow due to its simplicity <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It provides:
*   **Simple Documentation:** Easy to understand core concepts <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Code Agent:** The base agent type in Small Agents executes actions through code <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Tool Calling Agent:** Allows agents to use tools for specific tasks <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Custom Tool Creation:** Simple process to define and set up custom tools <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Problem Breakdown:** Small Agents can break down problems into steps and operate in a feedback loop <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a> <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Max steps can be limited to prevent hallucination <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Gradio UI Integration:** Allows for a simple, single-line code setup for the user interface <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### DeepSeek R1 Distill Models
DeepSeek R1 is an open-source reasoning LLM <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. DeepSeek developed distill versions of their model by fine-tuning models like Qwen and Llama based on data produced from the full DeepSeek R1, turning them into smaller, easily runnable reasoning LLMs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The 7 billion parameter version is a practical choice for local deployment <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### [[use_of_hugging_face_and_local_models_like_llama_3 | Use of Hugging Face and local models like Llama 3]]
Models can be accessed either through Hugging Face's inference API or run entirely locally using Olama <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a> <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

#### Hugging Face Integration
*   Models can be installed directly from Hugging Face or used via their inference endpoints <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   The `HF_API_MODEL` class in Small Agents allows for interaction with the Hugging Face API <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   A Hugging Face API token is optional but provides better rate limits for some restricted models <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

#### [[local_ai_agents_with_olama | Local AI agents with Olama]]
Olama is used to run models like DeepSeek R1 locally <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Installation:** Download Olama from `olama.com` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Model Management:** Search for and download various versions of models like DeepSeek R1 (e.g., 7B parameter version) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **OpenAI API Compatibility:** Olama instances are compatible with the OpenAI API, allowing `OpenAIServerModel` to be used by pointing its base URL to the local Olama instance <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. A dummy API key can be used as it's not needed locally <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Context Limit Expansion:** By default, Olama models have a limited context window (e.g., 2048 tokens) <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. This can be increased (e.g., to 8192 or 32000 tokens) by creating a custom model file for Olama that defines the desired context length <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a> <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. This does not create duplicate model copies, only adds configuration <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

### Local Knowledge Base (Chroma DB)
A local knowledge base is set up using Chroma DB <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.
*   **Data Ingestion:** PDFs from a local data directory are loaded using LangChain, split into chunks, and then embedded <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.
*   **Embeddings:** The same embedding model used in the agent is used to create embeddings for the chunks <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
*   **Vector Database:** Chunks and their embeddings are stored in Chroma DB <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. The script can be run multiple times to clear and reload the database, preventing duplicate data <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

## Developing the Agentic RAG System

The process of building the agent involves:
1.  **Importing Libraries:** Primarily relying on Small Agents classes for agents, tools, and UI <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
2.  **Loading Environment Variables:** Retrieving IDs for the reasoning model (e.g., R1) and the tool model (primary LLM, e.g., Qwen or Llama), along with an optional Hugging Face API token <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
3.  **Model Selection Function:** A function determines whether to use Hugging Face API or local Olama based on environment variables to instantiate the models <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
4.  **Reasoning Agent Setup:** An instance of a `CodeAgent` is created for the DeepSeek R1 model. This agent typically doesn't require extra tools as its role is pure reasoning on provided context <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Max steps are limited to prevent runaway loops <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
5.  **RAG Tool Definition:**
    *   An embedding model is initialized for vector database queries <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
    *   A custom tool, `rag_with_reasoner`, is defined using the `@tool` decorator <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   The tool takes a user query, performs a similarity search in the vector database, formats the retrieved context, and then feeds it into the reasoning model (R1) with a specific prompt <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
    *   The prompt can instruct R1 to suggest a better query if insufficient information is found, enabling a feedback loop for better retrieval <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
    *   R1 processes the context using `model.run()` with `reset=False` to maintain conversation history <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
6.  **Primary Agent Setup:** A `ToolCallingAgent` is created for the primary LLM (e.g., Qwen Instruct). This agent is configured with the `rag_with_reasoner` as its tool <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
7.  **User Interface:** A Gradio UI is created with a single line of code, automatically providing conversation history <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

This setup showcases a powerful form of [[ai_agent_orchestration_with_swarm | agentic orchestration]] where two distinct LLMs collaborate to handle complex tasks like RAG, with the reasoning model providing advanced insights and the primary LLM managing the conversational flow <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. While Small Agents has some quirks (e.g., parsing thinking tokens), its simplicity allows for rapid prototyping of such advanced workflows <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Future implementations could explore more robust frameworks like Pydantic AI and LangGraph <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.