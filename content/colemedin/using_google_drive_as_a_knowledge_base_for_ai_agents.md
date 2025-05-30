---
title: Using Google Drive as a knowledge base for AI agents
videoId: Xifzdn7zW3A
---

From: [[colemedin]] <br/> 

Building advanced AI agents with Retrieval Augmented Generation (RAG) is not limited to complex, custom-coded applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This can be achieved without writing any code by [[using_n8n_to_build_an_ai_knowledge_base | using n8n]], a workflow automation tool, alongside LangChain for AI development <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This approach allows for a full-blown RAG AI agent that leverages [[integrating_google_drive_as_a_knowledge_base | Google Drive as its knowledge base]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The agent can answer questions by using documents uploaded to the Google Drive <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Why n8n for AI Agent Development?

n8n is a workflow automation tool similar to make.com or Zapier, but it offers self-hosting capabilities, eliminating the need for expensive monthly fees and allowing for infinite scalability <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Crucially, n8n integrates directly with LangChain, making it exceptionally easy to [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | build powerful AI agents]] with tool calling and RAG capabilities <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Most AI agent functionalities can be implemented without code using n8n <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

The n8n workflows for this RAG AI agent are available for download as JSON files from a GitHub repository, allowing users to import them into their own n8n instance in seconds <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Workflow Structure

Every workflow in n8n, similar to make.com and Zapier, consists of triggers and action nodes <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### Trigger: Chat Input

The workflow is initiated by a chat input trigger, specifically when a chat message is received <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This setup provides an immediate chat window within the n8n UI, simplifying the testing and iteration process for AI agents <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### AI Agent Node (LangChain)

Once a chat message is received, it flows into the RAG AI agent, which is a tools agent using LangChain under the hood <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The AI Agent node handles various components without requiring custom code:

*   **Chat Model**: Supports various models like OpenAI (GPT-4o Mini), Anthropic (Claude), Llama 3.1 (Grok), and Ollama <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. API key setup is straightforward <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **Chat Memory**: Offers multiple options, including local in-memory storage, PostgreSQL chat memory, or Redis <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. For production, using a Supabase PostgreSQL table for chat memory is recommended <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Tool Calling (RAG Integration)**: This is where the RAG functionality is integrated <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Tools for Knowledge Retrieval and Ingestion

The AI agent uses two primary tools:

1.  **Built-in Vector Store Tool**: This tool retrieves documents based on a user query <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   **Vector Store**: An in-memory vector store is used for demonstration, but production setups could use external options like Supabase or Pinecone <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Using a Supabase vector store allows for managing RAG and chat memories in one place <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
    *   **Embedding Models**: OpenAI's `text-embedding-3-large` model is used to convert document chunks into vectors for retrieval <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
    *   **Retrieval Model**: A large language model (e.g., GPT-4o Mini) processes the retrieved documents to extract relevant information <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

2.  **n8n Workflow as a Tool for Google Drive Integration**: This custom tool is crucial for [[integrating_google_drive_with_n8n_for_document_management | integrating Google Drive]] with the AI agent's knowledge base <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   The tool is described to the AI agent as "use this to search for a file in Google Drive" <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   It defines parameters (e.g., a query) that the AI agent provides to execute the workflow properly <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   This secondary workflow starts with a webhook to receive the query <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
    *   It then interacts with Google Drive to search for a file/folder based on the query <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
    *   The identified file is downloaded <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   Text is extracted from the downloaded file <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
    *   Finally, the extracted text is inserted into the vector database, using the same memory key as retrieval to ensure synchronization <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   A default data loader defines how text is chunked (e.g., 1,000 character chunks) and converted into vectors for the database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Workflow ID Nuance

A technical workaround is currently necessary where the tool's workflow ID cannot reference the main agent's workflow ID directly due to potential errors <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. This requires a separate, small workflow that hooks back into the main workflow for data insertion into the in-memory vector store <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. This is because the in-memory vector store's memory key is prefixed by the workflow ID <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. This issue is avoided when using a production-ready vector database like Supabase, as it allows for defining a dynamic memory key without workflow ID prefixing <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Demonstration

The agent can start with an empty knowledge base <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Users can instruct the AI chatbot to add specific files from Google Drive to its knowledge base for future reference <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

For example:
1.  Initially, asking "what are the action items from the meeting on 8:22" yields no answer as the information is not in the knowledge base <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
2.  Commanding the agent: "find the 822 meeting notes in the drive and add them to your knowledge base" <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The agent then searches, downloads, and processes the file, adding it to the vector database <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
3.  Re-asking the same question, "what are the action items from 8:22," now results in a precise answer based on the newly added document <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

This controlled approach to adding documents prevents the vector database from becoming bloated with unnecessary files, giving users control over the agent's knowledge <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. Alternatively, workflows can be scheduled to automatically pull files from specific folders and hydrate the vector database regularly <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

## Embedding the Chatbot

The created AI agent can be embedded directly into a website using a simple HTML snippet provided by n8n <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. This allows for quickly integrating the AI chatbot widget, visible on many websites, for user interaction <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

> [!NOTE] Further development may focus on deploying RAG agents to production environments, particularly utilizing Supabase <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.