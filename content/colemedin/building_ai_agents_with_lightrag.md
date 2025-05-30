---
title: Building AI agents with LightRAG
videoId: Fx3J8k--U3E
---

From: [[colemedin]] <br/> 

[[improving_rag_ai_agent_accuracy | Improving RAG AI agent accuracy]] is a common challenge for developers looking to integrate external knowledge into their AI agents <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While Retrieval Augmented Generation (RAG) is crucial for making agents experts on specific documents and data <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, basic RAG can exhibit accuracy as low as 35-45% <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This level of accuracy is insufficient for [[building_fullscale_ai_agents | building real AI solutions]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

Traditional RAG solutions, even when built with tools like n8n and Langchain, often fall short of delivering the required performance <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. A powerful solution to this problem is [[enhancing_ai_agents_with_rag_technology | enhancing RAG with knowledge graphs]], specifically using the open-source framework [[introduction_to_lightrag_framework | LightRAG]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## What is LightRAG?

[[introduction_to_lightrag_framework | LightRAG]] is an open-source framework designed to significantly improve RAG accuracy <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Unlike traditional RAG, which primarily vectorizes documents, [[introduction_to_lightrag_framework | LightRAG]] also builds an "all-important graph" that connects topics, ideas, and concepts from your documents <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This approach takes the contextual understanding of an AI agent to the "next dimension" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Despite its advanced capabilities, it is "pretty easy to get up and running" <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Core Components and Usage

[[introduction_to_lightrag_framework | LightRAG]] operates in three distinct parts <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:

1.  **Setting up the RAG Pipeline:**
    *   This involves initializing an instance of the RAG pipeline <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Developers define the embedding model and large language model (LLM) to be used, with extensive customization options for OpenAI-like APIs (e.g., Gemini, Open Router), Olama for local LLMs, AWS Bedrock, and Azure OpenAI <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

2.  **Inserting Data:**
    *   Data is inserted into both the knowledge graph and vector database simultaneously using `rag.insert()` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
    *   [[introduction_to_lightrag_framework | LightRAG]] automatically handles chunking and optimal data insertion <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
    *   For persistent storage, options include Neo4j for the knowledge graph and PostgreSQL (with Apache AGE) for both vector and graph databases <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

3.  **Running Queries:**
    *   Queries are executed using `rag.query()` with a specified search mode <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Available search modes include:
        *   **Naive search:** Equivalent to basic RAG <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
        *   **Hybrid search** <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
        *   **Mix search:** Utilizes both vector retrieval (basic RAG) and knowledge graph search, offering the best of both worlds <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## [[improving_rag_ai_agent_accuracy | LightRAG]] vs. Traditional RAG

[[introduction_to_lightrag_framework | LightRAG]] consistently outperforms traditional RAG, especially as the knowledge base grows <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. While traditional RAG struggles with thousands or hundreds of thousands of documents, [[introduction_to_lightrag_framework | LightRAG]] maintains performance due to its enhanced contextual understanding provided by the knowledge graph <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Benchmarks show significant improvements in accuracy compared to "naive RAG" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. [[introduction_to_lightrag_framework | LightRAG]] is also simpler and faster than more complex implementations like Graph RAG from Microsoft <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Practical Comparison Example

When tested against a traditional RAG agent (using Chroma DB) with the same knowledge base (Pyantic AI documentation) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>:

*   **Traditional RAG (Chroma DB):** Produced a faster response due to only searching a vector database <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. However, it suffered from a "classic hallucination," pulling incorrect context and attempting to use a different search tool (DuckDuckGo) than requested (Brave) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **[[introduction_to_lightrag_framework | LightRAG]] Agent:** Provided a more accurate and relevant code implementation, correctly incorporating Brave for the web search tool <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. It demonstrated a "better context around what I'm trying to build and tying that specifically to the documentation" <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

### Code Simplicity

[[introduction_to_lightrag_framework | LightRAG]] significantly reduces the complexity of data ingestion. A script to ingest the Pyantic AI documentation into [[introduction_to_lightrag_framework | LightRAG]] is only 53 lines of code <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>, whereas the equivalent for basic RAG (Chroma DB), which requires manual chunking and inserting, is 177 lines <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This abstraction simplifies [[rag_ai_agent_development | RAG AI agent development]] <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.

## [[creating_rag_ai_agents_using_n8n | Building a LightRAG Agent]]

The process of [[building_ai_agents | building an AI agent]] with [[introduction_to_lightrag_framework | LightRAG]] can be broken down into these steps:

1.  **Create the Knowledge Base Script:**
    *   Initialize the [[introduction_to_lightrag_framework | LightRAG]] instance, defining the working directory, embedding model (e.g., OpenAI), and LLM (e.g., GPT-4 mini) <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
    *   Fetch documentation (e.g., Pyantic AI docs as a single string from a URL) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
    *   Insert the fetched documentation into the [[introduction_to_lightrag_framework | LightRAG]] knowledge base <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>.
    *   This initial ingestion can take time (e.g., 20 minutes for Pyantic AI docs) as it builds the vector database and knowledge graph <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

2.  **Set Up the Agent:**
    *   Import necessary libraries and define the same working directory to reference the created knowledge base <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
    *   Initialize the [[introduction_to_lightrag_framework | LightRAG]] instance without re-initializing the pipeline status (as data is already inserted) <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
    *   Define agent dependencies, injecting the [[introduction_to_lightrag_framework | LightRAG]] instance <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.
    *   Create the agent, specifying the LLM (e.g., GPT-4 mini) and a system prompt <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
    *   Provide a single `retrieve` tool that allows the agent to search the knowledge base using `rag.query()` with the `mix` search mode <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

3.  **User Interface (Optional):**
    *   A Streamlit application can be used to create a UI for interacting with the agent in a browser <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

## Limitations and Advanced Considerations

One primary limitation of RAG, including [[introduction_to_lightrag_framework | LightRAG]], is the difficulty in working with real-time data <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Updating the knowledge base requires re-inserting documents and re-computing the knowledge graph, which is not a fast process <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. For constantly evolving data, a platform like Graffiti, which specializes in real-time knowledge graphs, can be a solution <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Graffiti can maintain evolving relationships and historical context in a knowledge graph <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

Future enhancements for [[introduction_to_lightrag_framework | LightRAG]] agents could include integrating external storage solutions like Neo4j or PostgreSQL <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. Beyond [[introduction_to_lightrag_framework | LightRAG]] and knowledge graphs, other strategies for [[improving_rag_ai_agent_accuracy | RAG accuracy]] include [[agentic_rag_ai_agent_template | agentic RAG]], query expansion, and reranking <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.