---
title: Local AI versus cloud AI benefits
videoId: T2QWhXpnT5I
---

From: [[colemedin]] <br/> 

The choice between local and cloud-based AI solutions often depends on specific needs for control, security, and performance. While cloud AI offers powerful models, local AI provides distinct advantages, particularly for those prioritizing data privacy and offline functionality <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Why Choose Local AI?

There is a growing belief that [[local_vs_managed_ai_solutions | local AI]], where users maintain control over their data and large language models (LLMs), is the necessary direction for generative AI <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
Key benefits of local AI include:
*   **Data Control**: Users maintain complete control over their data and LLMs <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Security & Offline Capability**: A local setup ensures 100% security and the ability to operate offline <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, which is a significant advantage <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Customization**: [[extending_local_ai_infrastructure | Extending local AI infrastructure]] allows for tailored solutions like modifying model context lengths <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.

### Challenges with Local LLMs

Local LLMs, while beneficial for privacy, can present certain quirks. A common issue is the default context length of models like Ollama, which is often limited to 2,000 tokens <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. This can cause problems as prompts lengthen with more information from RAG lookups, potentially overriding system prompts and tool instructions <a class="yt-timestamp" data-t="00:28:43">[00:28:43]</a>.

### Overcoming Local LLM Limitations

To address the context length issue, users can create custom model versions with extended context parameters (e.g., 8,000 tokens) using a model file <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. This process involves inheriting from a base model and simply changing the context length parameter <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.

## Agentic RAG: Enhancing Knowledge Base Access

Retrieval Augmented Generation (RAG) is a widely adopted method for giving AI agents access to a knowledge base, making them domain experts <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, RAG alone is often not powerful enough <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Naive RAG vs. Agentic RAG

*   **Naive/Traditional RAG**: This approach involves taking documents, splitting them into chunks, embedding them into vectors, and storing them in a vector database <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. User questions are also vectorized to match relevant document chunks, which are then combined into a single prompt for the LLM <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The main limitation is that it's a "one-shot" process; the LLM doesn't have the ability to reason or explore the knowledge base in different ways <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

*   **Agentic RAG**: This method levels up RAG by placing an AI agent first, which then has tools to perform RAG and explore the knowledge base in various ways <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. The agent can search multiple vector databases, decide when to use each, and employ other tools like web search or different ways of looking at the knowledge base beyond basic vector mathematics <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This introduces more reasoning into the retrieval process <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Implementing Local Agentic RAG with n8n

A local AI version of the n8n agentic RAG template allows for a 100% offline, secure, and powerful RAG agent <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Key Components and Setup

1.  **Database Setup**:
    *   The database stores conversation history and the knowledge base <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   Credentials for Postgres (or self-hosted Superbase) need to be configured <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>.
    *   Tables for document metadata (high-level info for the LLM to list documents) <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a> and document rows (for storing tabular data from CSV/Excel files) are created <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
    *   The `documents` table, where embeddings for RAG are stored, is automatically created by the Postgres PG Vector store node <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

2.  **Knowledge Base Pipeline**:
    *   This pipeline adds local files into the Postgres/Superbase knowledge base <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
    *   It uses a local file trigger to watch for added or changed files in a specified folder <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   Upon file changes, old document records are deleted to ensure the knowledge base contains only updated information <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
    *   Document metadata (ID, title, file type) is inserted <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
    *   File content extraction varies by file type (PDF, CSV, text) using different n8n nodes <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.
    *   The extracted text is split into chunks and stored as embeddings using the PG Vector store node with an [[comparison_of_local_and_cloudbased_ai_models | Ollama embedding model]] (e.g., `namic embed text`) <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>.
    *   For CSV and Excel files, rows are inserted into the `document_rows` table, and a text representation of the entire table is also added for RAG <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. The schema of tabular data is also stored in the document metadata table, allowing the LLM to write SQL queries against it <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

3.  **AI Agent Setup**:
    *   Triggers include a chat trigger for UI interaction and a webhook for API endpoint usage <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
    *   A basic system prompt instructs the agent on its role and tool usage <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.
    *   Postgres chat memory is used for conversation history <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
    *   The chat model uses Ollama, configured through an Open AI credential node by changing the base URL to point to the local Ollama container due to an n8n glitch with direct Ollama chat model nodes <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>.
    *   Agent tools include:
        *   **RAG Lookup**: Utilizes the Postgres PG Vector store node for basic document retrieval <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. Metadata (like title and file ID) is included for source citation <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
        *   **List Documents**: Queries the `documents_metadata` table to list available documents <a class="yt-timestamp" data-t="00:27:04">[00:27:04]</a>.
        *   **Get File Contents**: Combines chunks from the `documents_PG` table to retrieve the full text of a specific document <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.
        *   **Query Tabular Data**: Allows the LLM to generate SQL queries against the `document_rows` table to analyze data, such as computing averages from customer feedback or sales pipelines <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This tool is particularly useful as traditional RAG often struggles with tabular data <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## [[comparison_between_local_and_large_ai_models | Comparison of Local and Large AI Models]]

While large cloud-based LLMs like Claude 3.7 Sonnet or GPT-4o offer super powerful capabilities, the demonstrated power with local AI models like Quan 2.51 14b, despite being relatively small, highlights the impressive potential of local AI setups <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Results can be inconsistent depending on the specific local LLM used <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

## Voice AI Innovation

Cartesia is a notable player in the voice AI space, revolutionizing voice content and products across various applications like online education, customer service, audiobooks, and video games <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. They address common issues of slowness, unpredictability, and robotic voices in current voice AI solutions <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Their upcoming Sonic 2.0 model, based on a revolutionary state-space model architecture, promises unbelievably realistic voices, low latency (as low as 40 milliseconds), and unprecedented control over emotions, accents, and speed <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Their playground allows voice cloning with as little as 3 seconds of audio <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.