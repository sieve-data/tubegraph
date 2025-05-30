---
title: Improving RAG AI agent accuracy
videoId: Fx3J8k--U3E
---

From: [[colemedin]] <br/> 

One of the most frequently asked questions in AI agent development is how to enhance the accuracy of [[retrieval_augmented_generation_rag_in_ai_agents|RAG AI agents]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. While Large Language Models (LLMs) are now capable of handling millions of tokens in a single prompt, [[retrieval_augmented_generation_rag_in_ai|RAG]] remains crucial for integrating external knowledge and making agents experts on specific documents and data <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Challenges with Basic RAG Accuracy

While [[retrieval_augmented_generation_rag_in_ai|RAG]] generally improves answers by providing extra context from documents, its accuracy can vary significantly <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Benchmarks for basic [[retrieval_augmented_generation_rag_in_ai|RAG]] cite accuracy for pulling relevant information between 35% and 75% <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Such rates are insufficient for building reliable AI solutions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Building a simple [[rag_ai_agent_development|RAG AI agent]] using tools like [[creating_rag_ai_agents_using_n8n|N8N]] and LangChain is not enough; more advanced strategies are required <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## [[enhancing_ai_agents_with_rag_technology|Enhancing RAG Accuracy]] with Knowledge Graphs and LightRAG

A powerful solution for [[improving_rag_accuracy_with_additional_strategies|RAG accuracy]] involves [[enhancing_ai_agents_with_rag_technology|enhancing RAG]] with knowledge graphs <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Specifically, an open-source framework called [[building_ai_agents_with_lightrag|LightRAG]] stands out <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

[[building_ai_agents_with_lightrag|LightRAG]] not only vectorizes documents like traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] but also constructs a knowledge graph that connects topics, ideas, and concepts within your documents <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This significantly deepens the contextual understanding of the AI agent <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Core Components and Functionality of [[building_ai_agents_with_lightrag|LightRAG]]

[[building_ai_agents_with_lightrag|LightRAG]] can be understood in three distinct parts:
1.  **Pipeline Setup**: Users define the embedding model and large language model to be used <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. These can be customized to use any OpenAI-like API (e.g., Gemini, Open Router), Olama for local LLMs, AWS Bedrock, or Azure OpenAI <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
2.  **Data Insertion**: Data is inserted into both the knowledge graph and vector database simultaneously using `rag.insert()` <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. [[building_ai_agents_with_lightrag|LightRAG]] automatically handles chunking and optimal insertion <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
3.  **Query Execution**: Queries are run using `rag.query()`, specifying a question and a search mode <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Naive search**: Basic [[retrieval_augmented_generation_rag_in_ai|RAG]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   **Hybrid search**: Combines vector retrieval with graph search <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   **Mix search**: Utilizes both vector retrieval and knowledge graph search, ensuring no loss of basic [[retrieval_augmented_generation_rag_in_ai|RAG]] capabilities <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Database Customization
[[building_ai_agents_with_lightrag|LightRAG]] offers options for customizing the database used for knowledge storage:
*   **Neo4j**: Can be used for the knowledge graph <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **PostgreSQL**: Can be used for both the vector database and the graph DB with Apache Age <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
    *   It's also possible to combine Neo4j for the knowledge graph and PostgreSQL for the vector database to leverage their individual strengths <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Performance Comparison
The [[building_ai_agents_with_lightrag|LightRAG]] GitHub repository provides benchmarks showing its superior performance compared to "naive [[retrieval_augmented_generation_rag_in_ai|RAG]]" (traditional [[retrieval_augmented_generation_rag_in_ai|RAG]]) across various datasets <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. [[building_ai_agents_with_lightrag|LightRAG]] also compares favorably against more complex implementations like GraphRAG from Microsoft, being simpler, faster, and more powerful <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Practical Implementation: [[building_a_nocode_rag_ai_agent|Building a LightRAG AI Agent]]

A practical example demonstrates [[building_ai_agents_with_lightrag|LightRAG]]'s power by comparing it against a traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] setup <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This solution includes a downloadable resource on GitHub <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

The project features two [[rag_ai_agent_development|RAG AI agents]]:
*   A traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] agent using Chroma DB for a fast, local vector database <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   A second [[rag_ai_agent_development|AI agent]] built with [[building_ai_agents_with_lightrag|LightRAG]] <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

Both agents utilize the same knowledge base, which consists of the entire Pydantic AI documentation, ingested as a single text file <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The documentation is ingested into Chroma DB for the traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] agent and a local knowledge graph for the [[building_ai_agents_with_lightrag|LightRAG]] agent <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

Both agents are accessible via Streamlit user interfaces, allowing for side-by-side comparison of their responses to the same questions <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Building the [[building_ai_agents_with_lightrag|LightRAG]] Knowledge Base
The process for building the [[building_ai_agents_with_lightrag|LightRAG]] knowledge base involves:
1.  **Initialization**: Defining a working directory, selecting the embedding model (e.g., OpenAI) and LLM (e.g., GPT-4 mini), and initializing storage and the pipeline <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
2.  **Data Insertion**: Using an asynchronous insert function to add information to the knowledge base <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. [[building_ai_agents_with_lightrag|LightRAG]] handles chunking and optimized insertions automatically <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
    *   This initial process of building the knowledge base can take time (e.g., 20 minutes for the entire Pydantic AI documentation) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, but it only needs to be run once unless updates are required <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. Subsequent agent runs are much faster <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

### Setting Up the [[building_ai_agents_with_lightrag|LightRAG]] Agent
The [[building_ai_agents_with_lightrag|LightRAG]] agent is set up by:
*   Defining the same working directory to reference the created knowledge base <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   Initializing the [[building_ai_agents_with_lightrag|LightRAG]] instance with the chosen LLM (e.g., GPT-4 mini) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
*   Defining a `retrieve` tool for the agent, which uses the [[building_ai_agents_with_lightrag|LightRAG]] instance's asynchronous query function with `mix` search mode <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. This ensures searches utilize both vector retrieval and the knowledge graph <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

## Addressing Real-time Data Limitations with Graffiti

A limitation of [[building_ai_agents_with_lightrag|LightRAG]] and [[retrieval_augmented_generation_rag_in_ai|RAG]] in general is the difficulty in working with real-time data <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Updating the knowledge base requires re-inserting documents and re-computing the knowledge graph, which is not a fast process <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

**Graffiti** is a powerful open-source platform designed for [[rag_ai_agent_development|building real-time knowledge graphs]] <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. It's an ideal solution for situations requiring constantly changing data, such as user interactions or time-sensitive metrics <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Graffiti excels at maintaining constantly evolving relationships in a knowledge graph and preserving historical context <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Comparative Test Results: LightRAG vs. Chroma DB

A test was conducted where both the [[building_ai_agents_with_lightrag|LightRAG]] agent and the Chroma DB agent were asked to create an AI agent implementation that could search the web using Brave <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

*   **Chroma DB Agent (Traditional RAG)**: The Chroma DB agent provided a faster response due to only searching the vector database <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. However, it exhibited a "hallucination," opting to use the DuckDuckGo search tool instead of Brave <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This common hallucination with traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] often occurs when the wrong context is pulled from the documentation <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

*   **[[building_ai_agents_with_lightrag|LightRAG]] Agent**: The [[building_ai_agents_with_lightrag|LightRAG]] agent produced code that correctly utilized Brave for the web search tool <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>. While the code wasn't immediately runnable without further implementation (as it only had Pydantic AI docs, not Brave docs), it demonstrated a much better contextual understanding of the request, correctly tying it to the relevant documentation <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

[[building_ai_agents_with_lightrag|LightRAG]] generally outperforms traditional [[retrieval_augmented_generation_rag_in_ai|RAG]], especially as the knowledge base grows to thousands or hundreds of thousands of documents <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Its use of a knowledge graph provides a deeper contextual understanding <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### Code Complexity Comparison
When comparing the Python scripts for ingesting documentation:
*   The script for traditional [[retrieval_augmented_generation_rag_in_ai|RAG]] with Chroma DB was 177 lines of code, as it required manual chunking and insertion <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
*   The script for [[building_ai_agents_with_lightrag|LightRAG]] was only 53 lines of code, due to [[building_ai_agents_with_lightrag|LightRAG]] handling chunking and optimized insertions automatically <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>.
    *   While manual chunking can offer more control, [[building_ai_agents_with_lightrag|LightRAG]]'s optimization and higher level of abstraction are beneficial <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

## Conclusion

[[building_ai_agents_with_lightrag|LightRAG]] and knowledge graphs are game-changers for [[improving_rag_accuracy_with_additional_strategies|RAG accuracy]] <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. While [[building_ai_agents_with_lightrag|LightRAG]] may show similar results to basic [[retrieval_augmented_generation_rag_in_ai|RAG]] with smaller knowledge bases, its advantages become pronounced with thousands or hundreds of thousands of documents <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

Other strategies to consider for [[improving_rag_accuracy_with_additional_strategies|RAG accuracy]] include:
*   [[agentic_rag_ai_agent_template|Agentic RAG]] <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>
*   Query expansion <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>
*   Reranking <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>