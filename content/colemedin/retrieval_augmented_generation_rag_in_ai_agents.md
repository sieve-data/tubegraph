---
title: retrieval augmented generation RAG in AI agents
videoId: PxcOIINgiaA
---

From: [[colemedin]] <br/> 

[[retrieval_augmented_generation | Retrieval augmented generation (RAG)]] is a fundamental technique used in most AI agents to provide them with documents and data, building a knowledge base for their operations <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This process enables agents to access and utilize external information beyond their initial training data <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Limitations of Traditional RAG

While [[retrieval_augmented_generation | RAG]] is widely adopted, it has significant limitations when used without additional strategies <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. A primary limitation is its static nature <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Maintaining synchronization between an agent's knowledge base and the underlying data store is the user's responsibility, a process that is both inefficient and unreliable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

Traditional [[retrieval_augmented_generation | RAG]] struggles to keep pace with dynamic environments where businesses or platforms constantly evolve, handling frequently changing data such as user preferences, internal metrics, or market conditions <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Introducing Graffiti: Temporal-Aware Knowledge Graphs

Graffiti is an open-source platform designed to address the static limitations of traditional [[retrieval_augmented_generation | RAG]] by building temporal-aware knowledge graphs <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It functions as a layer atop [[retrieval_augmented_generation | RAG]], specifically engineered for:
*   Constantly ingesting ever-changing data <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Maintaining a historical record of data changes <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This allows the AI agent to be aware of how the knowledge base evolves over time <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

This capability is particularly powerful for dynamic environments where AI agents are deployed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### How Graffiti Works

Graffiti represents information and its changes over time within a knowledge graph <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. For example, if a user's preference changes from Adidas shoes to Puma shoes, Graffiti records both facts along with historical context, indicating when the previous preference was valid and when the new one took effect <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This historical context is crucial for personalized interactions, such as those by customer support agents <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

The temporal-aware knowledge is stored in a knowledge graph powered by Neo4j, an open-source knowledge graph engine <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Information pieces are linked together by relationships that show how data relates to each other and how it has changed over time <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This includes metadata, like identifying GPT-3.5 as a previous version of GPT-4 <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

Knowledge graphs are generally more powerful than traditional [[retrieval_augmented_generation | RAG]] because they represent relational information <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Comparison to Other Knowledge Graphs

Other implementations of knowledge graphs for [[retrieval_augmented_generation | RAG]] include Graph RAG and Light RAG <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. However, Graffiti serves different use cases and offers advantages over these more static knowledge graphs <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

*   **Static vs. Dynamic Data:** Solutions like Graph RAG and Light RAG are better suited for static document summarization, such as documentation that rarely changes <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Graffiti, conversely, is designed for dynamic data scenarios, which are prevalent in most real-world applications for platforms or businesses <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Continuous Updates & Scalability:** Graffiti excels at handling continuous incremental updates to information and building historical context <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. It is also more lightweight and scalable, offering fast performance (typically sub-second latency) for both knowledge graph building and querying, making it suitable for production environments <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Technical Implementation

#### Prerequisites
To use Graffiti, the following prerequisites are typically needed <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>:
*   **Python** <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>
*   **Neo4j:** Serves as the knowledge graph engine, which can be run locally via Neo4j Desktop or Docker <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **LLMs and Embedding Models:** OpenAI models are commonly used, but other providers like Gemini or Anthropic are also supported, including local options like Olama <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

#### Adding and Querying Episodes
In Graffiti, pieces of information stored in the knowledge graph are called "episodes" <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Episodes can have flexible formats, such as simple strings or JSON objects with key-value pairs <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The LLM dynamically creates relationships between episodes based on its understanding of the data provided <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

Each episode includes metadata like its name, source, and crucially, a "reference time" to track when the information was inserted and, if applicable, when it became invalid <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

Graffiti provides straightforward methods for searching the knowledge graph <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>:
*   **Basic Search:** A single function call `graffiti.search()` allows querying the knowledge graph with a question <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. Results include a unique node identifier, the fact itself, and timestamps for validity (`valid_at` and `invalidated_at`) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This timestamped information helps the AI agent reason about the relevance of facts <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Center Node Search:** This allows for more refined searches by specifying a particular "center node" around which to search <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. For example, if a question relates to "Claude 4," searching around that specific node prevents accidentally pulling information for other LLMs like GPT <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Search Recipes:** Graffiti also offers different search recipes or strategies to explore the knowledge graph, optimizing searches for specific use cases <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

### Graffiti in Action: Evolving Knowledge Bases

A key benefit of Graffiti is its ability to manage continuously evolving knowledge bases, allowing AI agents to provide context-rich answers that reflect changes over time <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>.

For instance, an agent's knowledge base can be updated in phases:
1.  **Phase 1:** Information on current "best LLMs" like Gemini 2.5 Pro, Claude 3.7 Sonnet, and GPT 4.1 is added <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. An agent asked "What is the best LLM?" would respond with Gemini 2.5 Pro <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
2.  **Phase 2:** The introduction of "Claude 4" as the new "best LLM" is added <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>. Graffiti updates the knowledge graph by invalidating the previous "best LLM" fact and adding the new one <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. When asked the same question, the agent now correctly identifies Claude 4, but also notes that Gemini 2.5 Pro was previously considered the best, showcasing its historical awareness <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>.
3.  **Phase 3 (Hypothetical):** The introduction of "Massive Language Models (MLMs)" renders LLMs obsolete <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. The agent, leveraging Graffiti's temporal awareness, can state that while Claude 4 is currently the best LLM, MLMs have emerged and are making LLMs less relevant <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.

This demonstrates how a temporal-aware knowledge graph provides robust context, allowing agents to offer nuanced answers with historical caveats <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

## Combining Knowledge Graphs with Traditional RAG

It is not necessary to choose between knowledge graphs and traditional [[retrieval_augmented_generation | RAG]] using vector databases; they can be combined for enhanced performance <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. This concept, sometimes referred to as "agentic RAG," involves giving an agent the ability to explore knowledge in multiple ways <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

An AI agent can have tools for both:
*   Searching a knowledge graph <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.
*   Performing a lookup in a vector database <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.

This hybrid approach is powerful because information might be better represented in one format over the other depending on the query <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. An agent capable of reasoning which tool to use, or if one search failed, which other tool to try, can provide more accurate and comprehensive answers <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

The ideal [[retrieval_augmented_generation | RAG]] solution for most AI agents often includes a knowledge graph as one of its core search capabilities <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. Graffiti, with its temporal awareness, stands out as a top contender for knowledge graph tools, adding rich context to AI agents <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.