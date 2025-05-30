---
title: Integrating large language models like GPT with custom tools
videoId: Xifzdn7zW3A
---

From: [[colemedin]] <br/> 

Building advanced AI agents, particularly with Retrieval Augmented Generation (RAG), is no longer limited to complex, custom-coded applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's possible to create full-blown RAG AI agents using no-code workflow automation tools like n8n and AI development libraries like LangChain <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This approach allows users to build powerful agents that can answer questions using documents from a knowledge base, such as Google Drive, without writing a single line of code <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## What is n8n?

n8n is a powerful workflow automation tool similar to Make.com or Zapier <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. A key advantage of n8n is its ability to be self-hosted, eliminating recurring monthly fees and allowing for infinite scalability <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Crucially, n8n integrates directly with LangChain, making it straightforward to build robust AI agents with capabilities like [[function_calling_in_large_language_models | tool calling]] and RAG <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

n8n workflows are composed of triggers, which initiate the workflow, and action nodes, which perform tasks like interacting with AI models, Google Drive, or vector databases <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. n8n also provides a built-in chat window within its UI, making it very easy to test and iterate on AI agents <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Building a RAG AI Agent in n8n

The process involves setting up a workflow that responds to chat inputs, incorporates a LangChain AI agent, and integrates custom tools for RAG.

### Workflow Trigger
The agent's workflow is triggered by a chat input, meaning it activates when a chat message is received <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Users can configure authentication and an initial message for the chat widget <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### The Core AI Agent
The central component is the LangChain AI Agent node, which provides all necessary functionalities for an AI agent without requiring custom code <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
It manages:
*   **Chat Model**: Users can select from various [[utilizing_gpt_models_for_task_automation | large language models]] like OpenAI (GPT-4o mini used in the example), Anthropic (Claude), Grok (Llama 3.1), or Ollama <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Credentials typically only require an API key <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Custom code can be used for other models like Fireworks <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Chat Memory**: Several options are available for managing conversational memory, including local in-memory storage, PostgreSQL tables, or Redis <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. For production, using a Superbase PostgreSQL table for chat memory is recommended <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Tool Calling**: This is crucial for RAG integration. n8n offers various pre-built tools (e.g., calculator, vector store) and the ability to call any n8n workflow as a custom tool <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Tools for RAG Integration

Two primary tools are used for the RAG agent:

1.  **Built-in Vector Store Tool**: This tool is responsible for retrieving documents based on a user query <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   **Vector Store**: For demonstration, an in-memory vector store is used, storing files locally on the n8n instance <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Production-ready options include Superbase or Pinecone vector stores <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Superbase is highly recommended as it can manage both chat memory and vector store in one place <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Embedding Models**: OpenAI's `text-embedding-3-large` model is used to convert document chunks into vectors for retrieval <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
    *   **Processing LLM**: A [[reasoning_large_language_models_and_their_impact | large language model]] like GPT-4o mini processes the retrieved documents to extract relevant information and answer questions <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

2.  **Custom n8n Workflow as a Tool (Google Drive Integration)**: This tool enables the AI agent to add documents to its knowledge base on demand <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   **Functionality**: The bot can search Google Drive for a specified file, download it, extract its text, and then add it to the vector database <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
    *   **Workflow Steps**:
        *   A webhook receives the query (e.g., file name) from the AI agent <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
        *   A Google Drive node searches for the file/folder <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
        *   Another Google Drive node downloads the identified file <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
        *   A text extraction node pulls the content from the file <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
        *   Finally, a Vector Store node inserts the extracted text into the knowledge base, ensuring it uses the same memory key as the retrieval tool <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   **Data Loading**: The process involves splitting the text into chunks (e.g., 1000 chunk size) before converting them into vectors <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This configuration offers the same power and customization as a coded RAG agent, but with no code <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

> [!tip] In-Memory Vector Store Workaround
> When using an in-memory vector store, the memory key is prefixed by the workflow ID to avoid collisions <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This necessitates a workaround where the tool that inserts data into the vector database must be in the exact same workflow as the retrieval tool. If separate workflows are used, the data won't be accessible to the agent <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This issue is avoided when using production vector databases like Superbase, as they allow for more dynamic memory key definitions without workflow ID prefixing <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Demonstration of the AI Agent

The agent can initially fail to answer questions that require external knowledge not yet in its database <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. However, once prompted to add a specific file (e.g., "822 meeting notes") from Google Drive to its knowledge base, it can then successfully retrieve and answer questions based on that newly ingested document <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This on-demand knowledge injection prevents the vector database from getting bloated with unnecessary files <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## Deployment and Future Enhancements

The created chat widget can be easily embedded into a website by copying a provided HTML snippet <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Future developments could focus on [[benefits_of_hosting_your_own_large_language_models | deploying these AI agents in production]] environments, particularly leveraging Superbase for robust and scalable solutions <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.