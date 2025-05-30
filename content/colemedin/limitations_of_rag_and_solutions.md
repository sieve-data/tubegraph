---
title: limitations of RAG and solutions
videoId: mQt1hOjBH9o
---

From: [[colemedin]] <br/> 

[[Retrieval Augmented Generation | Retrieval Augmented Generation]] (RAG) is a widely adopted tool that provides [[Enhancing AI agents with RAG technology | AI agents]] access to a knowledge base, making them domain experts for specific documents <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, traditional RAG implementations often present significant [[limitations of traditional RAG systems | challenges]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Key [[limitations of traditional RAG systems | Limitations of Traditional RAG]]

Traditional RAG systems frequently struggle with several key issues:
*   **Missing Context and Information** Traditional RAG relies on a lookup process that can often miss crucial context and related information <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. For example, it might only pull a fraction of the necessary chunks when analyzing trends in a large spreadsheet <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, or retrieve meeting notes from an incorrect date despite the date being in the document title <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.
*   **Lack of Broader Context** RAG often struggles to connect different documents together, failing to provide the necessary broader context <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Inability to Zoom Out** RAG cannot easily "zoom out" to analyze entire documents or sets of documents unless the context is very small <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **No Concept of Data Analysis** Traditional RAG lacks the inherent capability for proper data analysis <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   **Poor Tabular Data Handling** It does not work well with tabular data, such as CSVs and Excel files, because it cannot typically pull an entire large file for analysis, leading to incomplete or incorrect answers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
*   **Limited Exploration Capabilities** If a RAG lookup fails, the agent has no other way to explore the knowledge base and is "stuck," unable to find an answer even if the information exists in the documents in another accessible format <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Reliability Issues** Overall, traditional RAG isn't always reliable <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## [[Agentic RAG strategy and implementation | Agentic RAG]] as a Solution

To overcome these [[limitations of traditional RAG systems | limitations]], one highly effective method is [[Agentic RAG strategy and implementation | Agentic RAG]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Defining [[Agentic RAG strategy and implementation | Agentic RAG]]

[[Agentic RAG strategy and implementation | Agentic RAG]] empowers [[RAG AI agent development | AI agents]] with the ability to reason about how they explore the knowledge base, rather than relying on a single tool <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This includes capabilities such as:
*   Improving RAG lookup queries <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   Choosing different tools to answer various user questions <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Tools and Capabilities in [[Agentic RAG advantages and future applications | Agentic RAG]]

An [[Agentic RAG setup | Agentic RAG setup]] in n8n (an example platform) can include several tools beyond just a basic RAG lookup <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:
*   **Improved RAG Lookup** An enhanced RAG lookup tool that can cite its sources <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Postgres Tools for Knowledge Exploration** These tools allow the agent to:
    *   **List all available documents** in the knowledge base <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   **Get file contents** of specific documents <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This means if a RAG lookup fails, the agent can list documents, reason about which one to inspect (e.g., by matching a date in the title), pull the entire content, and then answer the question <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This addresses the "zooming out" limitation <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   **Query Excel and CSV files as SQL tables** This is a powerful feature that enables the agent to perform data analysis tasks like calculating sums or maximums over tabular data, which is typically not possible with traditional RAG <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a> <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Practical Implementation

The process of implementing [[Agentic RAG setup | Agentic RAG]] involves:
1.  **Setting up the Database**: Creating tables for documents (for RAG embeddings and content), document metadata (for high-level info like URLs and titles, and schema for tabular data), and document rows (for storing tabular data in a queryable format) <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
2.  **Developing a RAG Pipeline**: This pipeline ingests documents from sources like Google Drive, processes different file types (PDFs, text, CSVs, Excel), clears old data for updated files to ensure data integrity, and inserts content into the knowledge base <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   Special handling for CSV/Excel files involves turning them into text documents for RAG while also storing individual rows and their schema for SQL-like querying <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.
3.  **Configuring the [[RAG AI agent development | AI Agent]]**:
    *   **System Prompt**: A carefully crafted system prompt guides the agent on how to use its tools, prioritizing RAG first and then leveraging other tools if RAG is insufficient <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. The prompt can also instruct the agent to be honest if it cannot find an answer, reducing hallucinations <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
    *   **Tools**: The agent is provided with the improved RAG tool, document listing and retrieval tools (e.g., via Postgres queries), and a tool for SQL-like querying of tabular data <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

By combining these elements, [[Agentic RAG strategy and implementation | Agentic RAG]] significantly improves an [[Enhancing AI agents with RAG technology | AI agent's]] ability to explore, understand, and respond to queries from a knowledge base, addressing many of the core [[limitations of traditional RAG systems | limitations of traditional RAG]] <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.