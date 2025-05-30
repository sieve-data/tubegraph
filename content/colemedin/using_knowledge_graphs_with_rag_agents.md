---
title: Using knowledge graphs with RAG agents
videoId: Fx3J8k--U3E
---

From: [[colemedin]] <br/> 

A common question in AI development is how to make [[retrieval_augmented_generation_rag_in_ai_agents | RAG AI agents]] more accurate <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] remains crucial for integrating external knowledge into agents, making them experts on specific documents and data <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. While Large Language Models (LLMs) can now handle millions of tokens, [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] is still highly relevant <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## The Challenge of [[improving_rag_ai_agent_accuracy | Improving RAG AI Agent Accuracy]]

Basic [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] is generally "pretty accurate," typically providing better answers by searching documents for extra context <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. However, benchmarks for basic [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] show varying accuracy, from 75% for pulling relevant information to as low as 35-45% <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Such levels of accuracy are insufficient for building robust AI solutions <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Simply creating a basic [[retrieval_augmented_generation_rag_in_ai_agents | RAG AI agent]] in tools like [[creating_rag_ai_agents_using_n8n | N8N]] or Langchain is not enough for real-world applications <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Introducing [[building_ai_agents_with_lightrag | LightRAG]]: A Powerful Solution

A powerful solution for [[improving_rag_ai_agent_accuracy | RAG accuracy]] involves [[integrating_knowledge_graphs_with_vector_databases_for_ai_solutions | enhancing RAG with knowledge graphs]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. One effective open-source framework for this is [[building_ai_agents_with_lightrag | LightRAG]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

[[building_ai_agents_with_lightrag | LightRAG]] not only vectorizes documents like traditional [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] but also constructs an important graph that connects topics, ideas, and concepts from documents <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This significantly deepens the contextual understanding of the [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agent]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### LightRAG's Core Workflow

[[building_ai_agents_with_lightrag | LightRAG]] functions in three main parts <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:
1.  **Pipeline Setup**: Users define the embedding model and LLM for the [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] pipeline <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
2.  **Data Insertion**: Data is inserted into both the knowledge graph and vector database simultaneously using `rag.insert()`. [[building_ai_agents_with_lightrag | LightRAG]] automatically handles chunking and optimal insertion <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
3.  **Query Execution**: Queries are run using `rag.query()` with a specified search mode <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Search Modes

[[building_ai_agents_with_lightrag | LightRAG]] offers various search modes for its knowledge base <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>:
*   **Naive search**: Basic [[retrieval_augmented_generation_rag_in_ai_agents | RAG]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Hybrid search**: Combines different retrieval methods <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Mix search**: Utilizes both vector retrieval (basic [[retrieval_augmented_generation_rag_in_ai_agents | RAG]]) and the knowledge graph <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This mode combines the benefits of both approaches <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Customization and Backend Options

[[building_ai_agents_with_lightrag | LightRAG]] allows extensive customization, including changing the LLM and embedding models <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It supports OpenAI-like APIs (Gemini, Open Router), direct Olama support for local LLMs, AWS Bedrock, and Azure OpenAI <a class="yt-timestamp" data-t="00:03:58">[00:04:05]</a>.

For database storage, [[building_ai_agents_with_lightrag | LightRAG]] provides options:
*   **Neo4j**: For the knowledge graph <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Postgres with Apache Age**: Can be used for both the vector database and graph database <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

### Performance Comparison

[[building_ai_agents_with_lightrag | LightRAG]] significantly outperforms "naive [[retrieval_augmented_generation_rag_in_ai_agents | RAG]]" (traditional [[retrieval_augmented_generation_rag_in_agents | RAG]]) across various datasets <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It is also simpler, faster, and more powerful than more complex implementations like Graph [[retrieval_augmented_generation_rag_in_agents | RAG]] from Microsoft <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Building and Comparing [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | RAG AI Agents]]

To demonstrate its power, a solution was created comparing a traditional [[retrieval_augmented_generation_rag_in_agents | RAG]] agent using Chroma DB (for a fast, local vector database) against an [[building_ai_agents_with_lightrag | LightRAG]] agent <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Both are Pydantic [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] and use the same knowledge base: the entire Pydantic AI documentation <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, specifically retrieved from the `llms.ext` endpoint <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

Both agents run with Streamlit user interfaces, allowing for side-by-side comparison <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Comparison Results

When asked to implement an AI agent that searches the web with Brave, the traditional [[retrieval_augmented_generation_rag_in_agents | RAG]] agent (Chroma DB) provided a faster response but exhibited a classic "hallucination" <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. It incorrectly suggested using the DuckDuckGo search tool instead of Brave, likely due to incorrect context retrieval <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

In contrast, the [[building_ai_agents_with_lightrag | LightRAG]] agent produced clean Pydantic AI code that correctly utilized Brave for the web search tool <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. While not perfectly runnable due to missing Brave documentation, it demonstrated a significantly better contextual understanding of the request <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

[[building_ai_agents_with_lightrag | LightRAG]] generally outperforms traditional [[retrieval_augmented_generation_rag_in_agents | RAG]], especially as the knowledge base scales to thousands or hundreds of thousands of documents <a class="yt-timestamp" data-t="00:12:59">[00:13:06]</a>. The knowledge graph in [[building_ai_agents_with_lightrag | LightRAG]] provides a deeper contextual understanding <a class="yt-timestamp" data-t="00:13:17">[00:13:21]</a>.

## Constructing a [[building_ai_agents_with_lightrag | LightRAG]] Agent

Setting up a [[building_ai_agents_with_lightrag | LightRAG]] agent involves a few key steps:

### 1. Building the Knowledge Base

A Python script is used to pull the Pydantic AI documentation and build the [[building_ai_agents_with_lightrag | LightRAG]] knowledge base, stored locally as JSON files representing the vector database and knowledge graph <a class="yt-timestamp" data-t="00:14:07">[00:14:24]</a>.

The script involves two main functions:
*   **Initialize the [[retrieval_augmented_generation_rag_in_agents | RAG]] Pipeline**: Defines the working directory, embedding model (e.g., OpenAI), and LLM (e.g., GPT-4 Mini), and initializes storages and pipeline status <a class="yt-timestamp" data-t="00:15:01">[00:15:32]</a>.
*   **Fetch and Insert Documentation**: Retrieves the entire Pydantic AI documentation as a single string from a URL and inserts it into the knowledge base <a class="yt-timestamp" data-t="00:16:01">[00:16:40]</a>. [[building_ai_agents_with_lightrag | LightRAG]] handles chunking and optimized insertions automatically <a class="yt-timestamp" data-t="00:16:36">[00:16:38]</a>.

While initial knowledge base creation can take around 20 minutes for large documentation sets, subsequent agent runs are very fast <a class="yt-timestamp" data-t="00:16:51">[00:17:18]</a>. The script for [[building_ai_agents_with_lightrag | LightRAG]] is significantly shorter (53 lines) compared to a basic [[retrieval_augmented_generation_rag_in_agents | RAG]] implementation (177 lines) which requires manual chunking and insertion <a class="yt-timestamp" data-t="00:20:16">[00:20:35]</a>.

### 2. Integrating with the Agent

The [[building_ai_agents_with_lightrag | LightRAG]] instance is injected into the agent using Pydantic AI dependencies <a class="yt-timestamp" data-t="00:18:07">[00:18:14]</a>. The agent is configured with an LLM (e.g., GPT-4 Mini) and a system prompt <a class="yt-timestamp" data-t="00:18:22">[00:18:28]</a>.

A single `retrieve` tool is provided to the agent <a class="yt-timestamp" data-t="00:18:30">[00:18:37]</a>. This tool calls the `lightrag.query()` function with the agent's search query, using the `mix` search mode to leverage both vector retrieval and the knowledge graph <a class="yt-timestamp" data-t="00:18:52">[00:19:09]</a>.

A Streamlit application provides a user interface to interact with the agent <a class="yt-timestamp" data-t="00:19:21">[00:19:25]</a>.

## Real-time Data Challenges and Graffiti

A limitation of [[retrieval_augmented_generation_rag_in_agents | RAG]] and [[building_ai_agents_with_lightrag | LightRAG]] is the difficulty of working with real-time data <a class="yt-timestamp" data-t="00:09:28">[00:09:34]</a>. Updating the knowledge base requires re-inserting documents and re-computing the knowledge graph, which is not a fast process <a class="yt-timestamp" data-t="00:09:36">[00:09:42]</a>.

For [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] that integrate with complex and constantly evolving data (e.g., user interactions, time-sensitive metrics), a powerful open-source platform called Graffiti is a solution <a class="yt-timestamp" data-t="00:09:54">[00:10:00]</a>. Graffiti excels at maintaining constantly evolving relationships in a knowledge graph and preserving historical context, which is unique <a class="yt-timestamp" data-t="00:10:28">[00:10:41]</a>. It powers the core of Zep's memory layer <a class="yt-timestamp" data-t="00:10:14">[00:10:17]</a>.

## Further Exploration

Experimenting with different [[retrieval_augmented_generation_rag_in_agents | RAG]] solutions, especially with larger knowledge bases, can reveal significant differences in results between basic [[retrieval_augmented_generation_rag_in_agents | RAG]] and [[building_ai_agents_with_lightrag | LightRAG]] <a class="yt-timestamp" data-t="00:21:37">[00:22:12]</a>. Different search modes within [[building_ai_agents_with_lightrag | LightRAG]] also offer optimization possibilities <a class="yt-timestamp" data-t="00:22:20">[00:22:24]</a>.

While knowledge graphs are a game-changer for [[enhancing_ai_agents_with_rag_technology | enhancing AI agents with RAG technology]], other strategies for [[improving_rag_ai_agent_accuracy | improving RAG AI agent accuracy]] include agentic [[retrieval_augmented_generation_rag_in_agents | RAG]], query expansion, and reranking <a class="yt-timestamp" data-t="00:22:42">[00:22:48]</a>.