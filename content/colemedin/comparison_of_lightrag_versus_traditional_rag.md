---
title: Comparison of LightRAG versus traditional RAG
videoId: Fx3J8k--U3E
---

From: [[colemedin]] <br/> 

One of the most frequent questions in AI development is how to make [[building_ai_agents_with_lightrag | RAG AI agents]] more accurate <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. RAG (Retrieval-Augmented Generation) remains crucial for integrating external knowledge into [[building_ai_agents_with_lightrag | AI agents]], allowing them to become experts on specific documents and data <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. While Large Language Models (LLMs) can now handle millions of tokens, RAG is still highly relevant <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Limitations of Traditional RAG
Traditional RAG systems generally provide "pretty accurate" answers by searching documents and using fetched context to improve responses <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. However, benchmarks for basic RAG show accuracy ranging from 35-45% to 75% for pulling relevant information <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This level of accuracy is often insufficient for building robust AI solutions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Simple RAG agent setups in tools like N8N and Langchain are often inadequate for real-world applications <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, highlighting the [[limitations of traditional RAG systems | limitations of traditional RAG systems]].

## Introducing LightRAG: A Powerful Solution
A powerful solution to these accuracy challenges is enhancing RAG with knowledge graphs <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, specifically using the open-source [[introduction_to_lightrag_framework | LightRAG framework]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
[[introduction_to_lightrag_framework | LightRAG]] goes beyond traditional RAG by not only vectorizing documents but also building a knowledge graph <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This graph connects topics, ideas, and concepts from documents, significantly improving the contextual understanding of the [[building_ai_agents_with_lightrag | AI agent]] <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### LightRAG Workflow
The workflow for [[introduction_to_lightrag_framework | LightRAG]] can be understood in three distinct parts <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>:
1.  **Pipeline Setup**: An instance of the RAG pipeline is set up, defining the embedding model and the large language model to be used <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Data Insertion**: Data is inserted into both the knowledge graph and the vector database simultaneously using `rag.insert()`. [[introduction_to_lightrag_framework | LightRAG]] automatically handles chunking and optimal insertion <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
3.  **Query Execution**: Queries are run using `rag.query()`, specifying a question and a search mode <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. [[introduction_to_lightrag_framework | LightRAG]] offers various search modes:
    *   **Naive search**: Basic RAG <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   **Hybrid search** <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   **Mix search**: Utilizes both vector retrieval (basic RAG) and knowledge graph search, ensuring no loss of functionality compared to basic RAG <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

### Customization and Flexibility
[[introduction_to_lightrag_framework | LightRAG]] is highly customizable <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>:
*   **LLMs and Embedding Models**: Users can change the LLM and embedding model, supporting OpenAI-like APIs (Gemini, Open Router), Ollama for local LLMs, AWS Bedrock, and Azure OpenAI <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Database Options**: For storing the knowledge base, [[introduction_to_lightrag_framework | LightRAG]] supports Neo4j for the knowledge graph and PostgreSQL for both vector and graph databases (via Apache Age) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Performance Claims
[[introduction_to_lightrag_framework | LightRAG]] claims significant performance improvements over "naive RAG" (traditional RAG) across various datasets <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It is also shown to be simpler, faster, and more powerful than more complex implementations like Microsoft's Graph RAG <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

## Practical Implementation and Comparison

### Project Setup
A demonstration project was created to compare [[introduction_to_lightrag_framework | LightRAG]] and traditional RAG, featuring two [[building_ai_agents_with_lightrag | RAG AI agents]] <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>:
1.  **Traditional RAG Agent**: Uses Chroma DB as a fast, local vector database <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
2.  **LightRAG Agent**: Built with [[introduction_to_lightrag_framework | LightRAG]], setting up a local knowledge graph <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

Both agents were built using Pydantic AI as the Python agent framework <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a> and shared the same knowledge base: the entire Pydantic AI documentation, compiled into a single text file <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Both agents were run via Streamlit user interfaces for side-by-side comparison <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Limitations with Real-time Data
One of the main [[limitations of RAG and solutions | limitations of RAG]], including [[introduction_to_lightrag_framework | LightRAG]], is the difficulty in working with real-time data <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Updating the knowledge base requires re-inserting documents into the vector database and recomputing the knowledge graph, which is not a fast process <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Solution for Real-time Data: Graffiti
For constantly evolving data like user interactions and time-sensitive metrics, **Graffiti** is a powerful open-source platform for building real-time knowledge graphs <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Graffiti excels at maintaining constantly evolving relationships and historical context within a knowledge graph, allowing [[building_ai_agents_with_lightrag | AI agents]] to track changes over time <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. It powers the core of Zep's memory layer <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### Test Case: Building a Web Search Agent
Both agents were tasked with creating an [[building_ai_agents_with_lightrag | AI agent]] implementation that could search the web using Brave <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

*   **Traditional RAG (Chroma DB) Results**: The Chroma DB agent provided a faster response because it only searched the vector database <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. However, it exhibited a "classic hallucination," incorrectly using the DuckDuckGo search tool instead of Brave <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This is likely due to incorrect context being pulled from the documentation <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   **LightRAG Results**: The [[introduction_to_lightrag_framework | LightRAG]] agent produced code that correctly used Brave for the web search tool <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. While not perfect (it simulated the request and used a placeholder for the model), it demonstrated a much better contextual understanding of the request and how to tie it to the documentation <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

### Scalability and Performance Advantage
[[introduction_to_lightrag_framework | LightRAG]] generally outperforms traditional RAG, especially as the knowledge base grows exponentially to thousands or hundreds of thousands of documents <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Its use of a knowledge graph provides a deeper contextual understanding, allowing it to maintain performance where traditional RAG would falter <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

## Building a LightRAG Agent

### Data Ingestion Script
The script for building the [[introduction_to_lightrag_framework | LightRAG]] knowledge base:
*   Initializes the [[introduction_to_lightrag_framework | LightRAG]] pipeline, defining the working directory (where the local knowledge graph will be created), embedding model (OpenAI), and LLM (GPT-4 mini) <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
*   Fetches the Pydantic AI documentation from a single URL (`/lms.ext`) <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   Inserts the entire documentation as a single string into the knowledge base, with [[introduction_to_lightrag_framework | LightRAG]] handling all chunking and optimized insertions <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

This ingestion process takes about 20 minutes for the entire Pydantic AI documentation <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>, but only needs to be run once or when updating the knowledge base <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. This ingestion script for [[introduction_to_lightrag_framework | LightRAG]] is significantly more concise (53 lines of code) compared to a traditional RAG implementation (177 lines for Chroma DB) because [[introduction_to_lightrag_framework | LightRAG]] handles complex operations like chunking and optimization behind the scenes <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

### LightRAG Agent Setup
The [[building_ai_agents_with_lightrag | LightRAG agent]] setup involves:
*   Defining the same working directory to reference the created knowledge base <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   Initializing the [[introduction_to_lightrag_framework | LightRAG]] instance by defining the working directory, embedding model, and LLM (GPT-4 mini) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. Storage is initialized, but pipeline status is not needed since data is not being inserted <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.
*   Defining dependencies for the [[building_ai_agents_with_lightrag | agent]], injecting the [[introduction_to_lightrag_framework | LightRAG]] instance <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.
*   Setting up the [[building_ai_agents_with_lightrag | agent]] itself with the chosen LLM and a system prompt <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   Providing a single `retrieve` tool that calls the `rag.query()` function with the agent's search query and using the `mix` search mode (vector retrieval and knowledge graph search) <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

This setup allows for interaction via a Streamlit UI, providing a user-friendly interface for the [[building_ai_agents_with_lightrag | AI agent]] <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

## Conclusion

[[introduction_to_lightrag_framework | LightRAG]], with its integration of knowledge graphs, offers a significant leap in accuracy and contextual understanding for [[building_ai_agents_with_lightrag | RAG AI agents]] compared to traditional RAG <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. While traditional RAG might yield similar results for smaller knowledge bases, [[introduction_to_lightrag_framework | LightRAG]] truly excels with thousands or hundreds of thousands of documents <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>. Beyond knowledge graphs, other strategies for [[improving_rag_accuracy_with_additional_strategies | improving RAG accuracy with additional strategies]] include [[agentic_rag_strategy_and_implementation | agentic RAG]], query expansion, and reranking <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>.