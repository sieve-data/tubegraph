---
title: integrating knowledge graphs with vector databases for AI solutions
videoId: PxcOIINgiaA
---

From: [[colemedin]] <br/> 

[[integrating_knowledge_bases_with_ai | Retrieval augmented generation (RAG)]] is a fundamental component of most [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]], serving as the method to establish a [[managing_embeddings_and_vectors_in_a_knowledge_base | knowledge base]] from documents and data <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, RAG inherently possesses significant limitations, particularly its static nature <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. It is the user's responsibility to continually synchronize the agent's knowledge base with the underlying data store, a process that is both inefficient and unreliable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This limitation becomes critical when dealing with constantly evolving data, such as user preferences, internal metrics, or market conditions, where traditional RAG struggles to keep pace <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Graffiti: Temporal Aware Knowledge Graphs

To address the limitations of static RAG, a platform called Graffiti focuses on building [[advantages_of_temporal_aware_knowledge_graphs | temporal aware knowledge graphs]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This technology acts as a layer on top of RAG, designed for:
*   Continuously ingesting ever-changing data <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Maintaining a historical record of how data has evolved <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Enabling [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] to be aware of how the [[managing_embeddings_and_vectors_in_a_knowledge_base | knowledge base]] changes over time <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

A key benefit of temporal aware [[using_knowledge_graphs_with_rag_agents | knowledge graphs]] is their ability to retain past preferences or states, providing crucial context for personalized experiences <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. For example, a customer support agent can understand a user's past preferences in addition to their current ones <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Underlying Technology and Comparison to Other Knowledge Graphs

Graffiti's [[using_knowledge_graphs_with_rag_agents | knowledge graph]] functionality is powered by Neo4j, an open-source [[using_knowledge_graphs_with_rag_agents | knowledge graph]] engine <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a> <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. This allows information to be linked together with relationships that show how data relates and changes over time <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

While [[using_knowledge_graphs_with_rag_agents | knowledge graphs]] like those built with Graffiti are generally more powerful than traditional RAG due to their ability to represent relationships and metadata, they serve different purposes <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. Other [[using_knowledge_graphs_with_rag_agents | knowledge graph]] implementations, such as graph RAG or light RAG, are often better suited for static document summarization, like documentation that changes infrequently <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. In contrast, Graffiti is specifically designed for dynamic data and continuous incremental updates, making it highly suitable for evolving business or platform environments <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Graffiti is also noted for being more lightweight and scalable, offering typically sub-second latency for both knowledge graph building and querying, making it suitable for production environments <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Integrating Knowledge Graphs and Vector Databases

A powerful strategy for [[integrating_knowledge_bases_with_ai | AI solutions]] is to combine the strengths of [[using_knowledge_graphs_with_rag_agents | knowledge graphs]] with traditional RAG using [[reasoning_with_local_models_and_vector_databases | vector databases]] <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.
*   **Complementary Tools**: An [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agent]] can be equipped with one tool to search a [[using_knowledge_graphs_with_rag_agents | knowledge graph]] and another tool to perform a traditional lookup in a [[reasoning_with_local_models_and_vector_databases | vector database]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a> <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>.
*   **Agentic RAG**: This approach, known as agentic RAG, allows the agent to explore knowledge in diverse ways <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. The agent can reason about which knowledge source is more appropriate for a given query <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.
*   **Enhanced Accuracy**: By combining both methods, agents can achieve better answers, as some information might be better represented in a [[using_knowledge_graphs_with_rag_agents | knowledge graph]] (e.g., relationships, temporal context) while others in a [[reasoning_with_local_models_and_vector_databases | vector database]] (e.g., semantic similarity of raw text) <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>.

This hybrid approach forms an ideal RAG solution for most [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]], particularly when dealing with dynamic data <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>. Using a tool like Graffiti for the [[using_knowledge_graphs_with_rag_agents | knowledge graph]] component adds rich, [[advantages_of_temporal_aware_knowledge_graphs | temporal aware]] context to agents <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.