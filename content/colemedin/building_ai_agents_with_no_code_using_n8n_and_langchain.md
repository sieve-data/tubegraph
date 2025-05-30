---
title: Building AI agents with no code using n8n and LangChain
videoId: Xifzdn7zW3A
---

From: [[colemedin]] <br/> 

[[building_ai_agents_with_nocode_tools | Building advanced AI agents]] that incorporate Retrieval Augmented Generation (RAG) is not limited to complex, custom-coded applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's possible to create a full-blown RAG AI agent with a Google Drive knowledge base using n8n and [[setting_up_ai_agents_with_python_and_langchain | LangChain]], with literally zero lines of code <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Why n8n for AI Agents?

While coding AI agents can be beneficial, n8n allows for simple, no-code creation of agents <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. n8n is a workflow automation tool, similar to make.com or Zapier, but offers significant advantages:
*   **Self-hosting**: It can be self-hosted, eliminating hundreds of dollars in monthly fees common with other services <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Scalability**: n8n can be scaled infinitely <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Direct LangChain Integration**: n8n integrates directly with [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]], making it easy to [[building_ai_agents_with_n8n | build powerful AI agents]] with tool calling and RAG capabilities <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Core Components of an n8n AI Agent Workflow

n8n workflows, similar to make.com and Zapier, consist of triggers and action nodes <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The showcased RAG AI agent workflow is available as JSON files in a GitHub repository, allowing users to download and import them into their own n8n instance <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Triggers

The trigger for this RAG AI agent is a "Chat Input" node, which starts the workflow upon receiving a chat message <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This node allows for optional authentication and an initial message for the chat widget <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. A key feature of n8n is the built-in chat window in the UI, which facilitates quick testing and iteration of AI agents <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### AI Agent Node (LangChain Integration)

The core of the RAG agent is an "AI Agent" node, which leverages [[developing_ai_agents_with_lang_chain_and_lang_graph | LangChain]] under the hood <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This node handles tools, memory, and chat models without requiring any code <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For more custom functionalities that no-code might not support, a "LangChain Code" node can be used <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

#### Chat Model Options
The AI Agent node allows selection of various chat models <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
*   OpenAI (GPT-4o mini used in the example) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
*   Anthropic (Claude) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>
*   Grok (for Llama 3.1) <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>
*   Ollama <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>

#### Chat Memory Options
Multiple options are available for chat memory <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>:
*   In-memory (stored locally on the n8n instance) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>
*   PostgreSQL chat memory (SQL table for conversations) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>
*   Redis <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>
*   Supabase PostgreSQL table (recommended for production as it can manage both chat memory and vector store) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.

#### Tool Calling
Tool calling is a powerful aspect of the AI agent, enabling RAG integration <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Custom tools are provided, such as a calculator or a vector store <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. The most significant feature is the ability to call *any* n8n workflow as a tool <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This allows complex multi-step workflows (e.g., interacting with Google Drive) to be packaged as a single tool for the AI agent <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## RAG AI Agent Example: Google Drive Knowledge Base

The demonstrated RAG agent uses two main tools:
1.  **Vector Store Tool**: Retrieves documents to answer questions <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   **Vector Store**: In-memory vector store is used for demonstration, stored locally on the n8n instance <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Other options include Supabase or Pinecone vector stores <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   **Embedding Models**: OpenAI's `text-embedding-3-large` model is used for embeddings, converting document chunks into vectors for retrieval <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   **LLM for Retrieval**: GPT-4o mini is used to process retrieved documents and extract relevant information <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

2.  **n8n Workflow as a Tool (Google Drive Integration)**: This tool adds documents to the vector database knowledge base <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. The chatbot can be instructed to add files from Google Drive to its knowledge base for future reference <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

    The workflow for this tool involves several steps:
    *   **Webhook Trigger**: Receives the query (e.g., file name) from the AI agent <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   **Google Drive Search**: Searches for a file or folder based on the query <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
    *   **Download File**: Downloads the identified file <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   **Extract Text**: Extracts text content from the downloaded file <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   **Add to Vector Database**: Inserts the extracted text into the vector database <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
        *   It uses the same memory key as the retrieval tool to ensure synchronization <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
        *   A default data loader is used to split the text into chunks (e.g., 1,000 character chunks) before converting them into vectors <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Workflow ID Workaround
When using an in-memory vector store, a tool that references a workflow ID cannot reference the ID of the same workflow that contains the agent <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. This is because the in-memory vector store's memory key is prefixed by the workflow ID to avoid collisions <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Therefore, a separate workflow is needed to invoke the main workflow's webhook, ensuring that both data insertion and retrieval operate within the same workflow ID context <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This technicality is avoided when using a production vector database like Supabase, as the memory key can be defined more dynamically without workflow ID prefixing <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Demonstration and Testing

The n8n UI's integrated chat window allows for real-time testing of the AI agent <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Test Scenario
1.  **Initial Query (without knowledge)**: A question about meeting notes (e.g., "What are the action items from the meeting on 8/22?") is asked when the knowledge base is empty <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. The agent confirms it does not have access to that specific file <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>.
2.  **Adding Knowledge**: The user instructs the AI agent to "find the 8/22 meeting notes in the drive and add them to your knowledge base" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The agent successfully adds the meeting notes <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
3.  **Subsequent Query (with knowledge)**: The exact same question is asked again <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. This time, the agent retrieves the information from the newly added document and provides the correct action items <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

This method allows for controlled addition of knowledge to the agent, preventing the vector database from getting bloated with unnecessary files, unlike automatically feeding in every file from Google Drive <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

## Embedding the Chatbot

The created AI agent can be embedded into a website. By accessing "more info" in the n8n chat window, an HTML iframe code snippet can be copied and pasted into a website's HTML editor, creating a chat widget that functions directly on the site <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

## Future Developments

Future videos on [[creating_rag_ai_agents_using_n8n | RAG with n8n]] may focus on deploying agents in production environments, particularly utilizing Supabase for persistent memory and vector stores <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.