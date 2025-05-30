---
title: introduction to Graffiti as a dynamic knowledge graph tool
videoId: PxcOIINgiaA
---

From: [[colemedin]] <br/> 

Graffiti is an open-source platform designed for building [[advantages_of_temporal_aware_knowledge_graphs | temporal aware knowledge graphs]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. It functions as a layer on top of [[introduction_to_retrieval_augmented_generation_rag | Retrieval Augmented Generation (RAG)]], specifically engineered for continuously ingesting ever-changing data and maintaining a historical record of how that data has evolved <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This capability ensures that [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] are aware of changes in their knowledge base over time <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Limitations of Traditional RAG

[[introduction_to_retrieval_augmented_generation_rag | Retrieval Augmented Generation]] is a foundational component in most [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] for providing them with a knowledge base from documents and data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, traditional [[introduction_to_retrieval_augmented_generation_rag | RAG]] by itself has significant limitations:
*   **Static Nature** <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>: It is the user's responsibility to constantly synchronize the agent's knowledge base with the data store, a process that is often inefficient and unreliable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Difficulty with Dynamic Data** <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>: When working with constantly changing data, such as user preferences, internal metrics, or market conditions, traditional [[introduction_to_retrieval_augmented_generation_rag | RAG]] struggles to keep up <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Graffiti addresses these issues by providing a dynamic solution for knowledge management in evolving environments <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Core Features and Advantages

### Temporal Awareness
Graffiti's core strength lies in its temporal awareness. Instead of merely replacing outdated facts, it adds new information while maintaining historical context <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. For example, if a user's preference changes from Adidas to Puma, Graffiti records both preferences along with the timeframes of their validity <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. This historical record is crucial for [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agents]] to provide personalized and context-rich responses, understanding past preferences alongside current ones <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Knowledge Graph Structure
Graffiti utilizes Neo4j as the engine behind its knowledge graphs <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, an open-source knowledge graph engine <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Information is stored as interconnected pieces (nodes) with relationships, helping to understand how all data relates to each other and how it has changed over time <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. This structure allows [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agents]] to reason about knowledge relationships, which is a key advantage over traditional [[introduction_to_retrieval_augmented_generation_rag | RAG]] methods <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Lightweight and Scalable Performance
Graffiti is designed to be lightweight and highly scalable <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Compared to other knowledge graph solutions like Light RAG, Graffiti offers significantly faster performance for both building the knowledge graph and querying it, typically achieving subsecond latency <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This efficiency makes it suitable for production environments to build robust [[introduction_to_retrieval_augmented_generation_rag | RAG]] solutions for [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Flexible Data Ingestion (Episodes)
Information added to Graffiti's knowledge graph is referred to as "episodes" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. A key feature is that these episodes do not need to follow a specific format; they can be simple strings or structured JSON objects with key-value pairs <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The underlying LLM dynamically processes these episodes, understands the data, and builds appropriate relationships within the knowledge graph <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Each episode includes metadata such as name, source, and a crucial "reference time" for temporal tracking <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### Powerful Search Capabilities
Graffiti simplifies searching the knowledge graph with a single function call <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. Search results provide not only the fact itself but also its unique identifier, the `valid_at` timestamp (when it was inserted), and the `invalidated_at` timestamp (if it became invalid) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This temporal context allows [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] to reason about the relevance of information when answering questions <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

Additionally, Graffiti supports "center node searches" <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. This allows for more refined searches by specifying a particular piece of information (a node) and exploring its immediate context, preventing the retrieval of irrelevant facts <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Comparison to Other Knowledge Graphs
While other knowledge graph implementations like Graph RAG and Light RAG exist, they are often more suited for static document summarization, such as unchanging documentation <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Graffiti, conversely, excels in scenarios involving dynamic, continuously updating data, which is common in most business and platform use cases <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Integrating Knowledge Graphs with RAG Agents

It is highly recommended to integrate knowledge graphs like Graffiti alongside more traditional [[introduction_to_retrieval_augmented_generation_rag | RAG]] approaches that use [[integrating_knowledge_graphs_with_vector_databases_for_ai_solutions | vector databases]] <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. This is an example of [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agentic RAG]], where an agent is given the ability to explore knowledge through different tools <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. An [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agent]] can be equipped with a tool to search the knowledge graph and another to search a [[integrating_knowledge_graphs_with_vector_databases_for_ai_solutions | vector database]] <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. This hybrid approach is powerful because sometimes information is better represented in one format over the other, allowing the agent to choose the optimal retrieval method for better overall answers <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>. Graffiti, with its temporal awareness, adds rich context to [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agents]], making it a top contender for knowledge graph tools in an ideal [[introduction_to_retrieval_augmented_generation_rag | RAG]] solution <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.