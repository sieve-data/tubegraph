---
title: Introduction to LightRAG framework
videoId: Fx3J8k--U3E
---

From: [[colemedin]] <br/> 

A common challenge in developing RAG AI agents is achieving high accuracy <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. While RAG (Retrieval Augmented Generation) remains essential for integrating external knowledge and making AI agents experts on specific documents and data <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, basic RAG accuracy can vary significantly, ranging from 35-45% to 75% in benchmarks <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. To overcome these limitations and build robust AI solutions, simply setting up a [[rag_ai_agent_development | simple RAG AI agent]] in tools like N8N and LangChain is insufficient <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

A powerful solution for improving RAG accuracy involves enhancing RAG with knowledge graphs, particularly through the open-source framework called LightRag <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## What is LightRag?

LightRag is an open-source framework that goes beyond traditional RAG by not only vectorizing documents but also building an "all-important graph" <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This graph connects topics, ideas, and concepts from documents, significantly enhancing the contextual understanding of an AI agent <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. It is designed to be relatively easy to set up and run <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

LightRag is a legitimate framework backed by a research paper, offering in-depth technical details in its GitHub repository <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Core Components and Workflow

Working with LightRag is simplified into three main parts <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>:

1.  **Pipeline Setup**: An instance of the RAG pipeline is set up, where users define the embedding model and large language model (LLM) to be used <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
2.  **Data Insertion**: Data is inserted into both the knowledge graph and the vector database simultaneously using `rag.insert()` <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. LightRag automatically handles document chunking and optimizes insertions <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  **Query Execution**: Queries are run using `rag.query()` with a specified question and search mode <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Search Modes <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
LightRag offers various search modes for its knowledge base:
*   **Naive Search**: Equivalent to basic RAG <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Hybrid Search**: Combines different retrieval methods <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Mix Search**: Utilizes both vector retrieval (basic RAG) and knowledge graph search, ensuring no loss of functionality from traditional RAG while adding the benefits of graph understanding <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Customization Options <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>
Users can customize:
*   **LLMs and Embedding Models**: Any OpenAI-like API, including Gemini, OpenRouter, and local LLMs via Olama, AWS Bedrock, or Azure OpenAI <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Database**: Options include Neo4j for the knowledge graph, and Postgres for both the vector database and graph DB with Apache Age <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## [[comparison_of_lightrag_versus_traditional_rag | Comparison of LightRAG versus traditional RAG]]

LightRag demonstrates significant performance improvements over basic or traditional RAG, which is referred to as "naive RAG" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. Benchmarks indicate clear differences in accuracy across various datasets <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. It even outperforms more complex implementations like Microsoft's Graph RAG, being simpler, faster, and more powerful <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### Practical Demonstration
A comparison involved two RAG agents, one using traditional RAG with Chroma DB and another built with LightRag, both utilizing the entire Pydantic AI documentation as their knowledge base <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. These agents were integrated with Streamlit user interfaces for side-by-side testing <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

In a test asking agents to create an AI agent to search the web with Brave:
*   **Traditional RAG (Chroma DB)**: Produced a faster response but exhibited a hallucination, using DuckDuckGo instead of Brave, indicating incorrect context retrieval <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **LightRag**: Provided a cleaner, more accurate implementation that correctly utilized Brave for the web search tool, demonstrating a better contextual understanding <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

LightRag generally outperforms traditional RAG, especially as the knowledge base scales to thousands or hundreds of thousands of documents, due to its enhanced contextual understanding provided by the knowledge graph <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

### Code Simplicity for Ingestion
Another notable advantage of LightRag is the simplicity of its data ingestion process compared to traditional RAG <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. For example, ingesting the Pydantic AI documentation into LightRag requires only 53 lines of code, whereas a traditional RAG setup (e.g., with Chroma DB) that handles its own chunking and insertion may require 177 lines <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. LightRag automates chunking and optimizes insertions, simplifying development <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.

## [[building_ai_agents_with_lightrag | Building AI Agents with LightRAG]]

A step-by-step example for [[enhancing_ai_agents_with_rag_technology | enhancing AI agents with RAG technology]] using LightRag:

1.  **Initialize Rag Instance**: Define a working directory for the local knowledge graph and select the embedding and large language models (e.g., OpenAI's GPT-4 Mini) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Initialize storage and the pipeline for data insertion <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
2.  **Insert Data**: Use the asynchronous `rag.insert()` function to add information to the knowledge base <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This can include text from local files or cloud sources, which LightRag automatically chunks and optimizes <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
3.  **Run Queries**: Execute queries using `rag.query()` with a question and a chosen search mode (e.g., `mix` mode for combined vector database and knowledge graph search) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

The process of building the knowledge base can take time (e.g., 20 minutes for the entire Pydantic AI documentation) initially, but subsequent agent runs are very fast <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. The agent setup involves defining dependencies for the LightRag instance and a single retrieve tool that calls the `rag.query()` function with the `mix` search mode <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. [[using_langchain_and_streamlit_for_rag_development | Streamlit is used to create a UI for interaction]] <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

## Limitations and Solutions for Real-time Data

A limitation of LightRag, and RAG in general, is the difficulty in working with real-time data <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Updating the knowledge base requires re-inserting documents and re-computing the knowledge graph, which is not a fast process <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

For constantly evolving data like user interactions or time-sensitive metrics, Graffiti, a powerful open-source platform for building real-time knowledge graphs, offers a solution <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Graffiti excels at maintaining constantly evolving relationships in a knowledge graph and preserving historical context <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. (Note: Graffiti sponsored a segment in the video <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.)

## Further Enhancements

While LightRag and knowledge graphs are significant for improving RAG accuracy, other strategies exist to make RAG even more accurate, including:
*   [[agentic_rag_strategy_and_implementation | Agentic RAG strategy and implementation]] <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>
*   Query expansion <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>
*   Reranking <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>

These [[advanced_rag_implementation_techniques | advanced RAG implementation techniques]] can further refine RAG performance.