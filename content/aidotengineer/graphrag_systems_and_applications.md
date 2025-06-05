---
title: GraphRAG systems and applications
videoId: RR5le0K4Wtw
---

From: [[aidotengineer]] <br/> 

## Introduction to [[retrieval_augmented_generation_RAG | RAG]] and [[graph_databases_and_technical_implementations | GraphRAG]]

[[retrieval_augmented_generation_RAG | Retrieval Augmented Generation (RAG)]] is a technique that enhances large language models (LLMs) by providing them with access to external knowledge bases, helping to ground their responses and reduce hallucinations. A common question in the field is whether [[retrieval_augmented_generation_RAG | RAG]] is still relevant or if agent-based systems are taking over <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, for problems solvable by [[retrieval_augmented_generation_RAG | RAG]] in production, agents may not be necessary <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. There are many use cases where [[retrieval_augmented_generation_RAG | RAG]] has found successful application <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

[[graph_databases_and_technical_implementations | Graph RAG]] (or Graph-based Retrieval Augmented Generation) is an advanced form of [[retrieval_augmented_generation_RAG | RAG]] that leverages the structured nature of knowledge graphs to improve information retrieval and generation <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. This approach aims to make LLMs "smarter" by integrating structured knowledge <a class="yt-timestamp" data-t="02:24:52">[02:24:52]</a>.

## What is a [[graph_databases_and_technical_implementations | Knowledge Graph]]?

A [[graph_databases_and_technical_implementations | knowledge graph]] is a network that represents relationships between different entities <a class="yt-timestamp" data-t="02:27:50">[02:27:50]</a>. These entities can be people, places, concepts, or events <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. The "edge" or relationship between two entities is crucial, as it defines connections that only [[graph_databases_and_technical_implementations | graph-based networks]] or [[graph_databases_and_technical_implementations | knowledge graphs]] can effectively exploit <a class="yt-timestamp" data-t="02:58:02">[02:58:02]</a>. This representation is vital for understanding complex relationships and organizing data from multiple sources <a class="yt-timestamp" data-t="03:50:09">[03:50:09]</a>.

## Advantages of [[graph_databases_and_technical_implementations | Graph-Based Systems]] in [[retrieval_augmented_generation_RAG | RAG]]

[[graph_databases_and_technical_implementations | Knowledge graphs]] enhance [[retrieval_augmented_generation_RAG | RAG]] systems in several ways:
*   **Detailed Information Capture**: They capture information between entities in much greater detail than traditional semantic [[retrieval_augmented_generation_RAG | RAG]] systems, providing a comprehensive view of knowledge <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Relationship Exploitation**: The ability to exploit the relationships between entities is a unique advantage <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>. Semantic vector databases do not exploit these relationships as well <a class="yt-timestamp" data-t="09:40:02">[09:40:02]</a>.
*   **Causality and Reasoning**: [[graph_databases_and_technical_implementations | Knowledge graphs]] can model the "why" and "when" behind changes, enabling temporal and relational reasoning that traditional [[retrieval_augmented_generation_RAG | RAG]] approaches lack <a class="yt-timestamp" data-t="04:09:56">[04:09:56]</a>. This capability helps solve hallucinations and optimize hypothesis generation <a class="yt-timestamp" data-t="01:38:44">[01:38:44]</a>.
*   **Explainability**: [[graph_databases_and_technical_implementations | GraphRAG]] allows for explaining answers by exposing the thought process, relationships, and additional context, which is crucial for applications requiring transparency <a class="yt-timestamp" data-t="03:43:03">[03:43:03]</a>.
*   **Handling Complex Data**: [[graph_databases_and_technical_implementations | GraphRAG]] can handle complex data formats where answers might be split across multiple pages or involve similar but non-matching terms, leveraging the graph structure and relationships <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

## Building a [[graph_databases_and_technical_implementations | Graph RAG]] / Hybrid System

Building a [[graph_databases_and_technical_implementations | Graph RAG]] or hybrid system involves several [[components of RAG stack | key components]] <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>:

1.  **Data Processing**: The quality of processed data directly impacts the quality of the [[graph_databases_and_technical_implementations | knowledge graph]] and subsequent retrieval <a class="yt-timestamp" data-t="04:32:04">[04:32:04]</a>. This is a one-time, offline process <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
2.  **Graph Creation**: This involves extracting entities and relationships (triplets) from unstructured documents <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. LLMs are crucial for structuring this information, guided by prompt engineering and defining an ontology specific to the use case <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. This step often requires significant iterative refinement to ensure accurate triplets, as noisy triplets lead to noisy retrieval <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
3.  **Semantic Vector Database Creation**: For hybrid systems, documents are broken into chunks, embedded into vector representations, and stored in a vector database <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. Overlap between chunks helps maintain context <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.
4.  **Inferencing (Querying)**: This is the online phase where users ask questions, and the system retrieves information and generates responses <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Retrieval Strategies and Performance

In [[graph_databases_and_technical_implementations | GraphRAG]], retrieval is not limited to simple lookups. It involves traversing relationships between nodes <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.
*   **Multi-Hop Retrieval**: Exploiting relationships through multiple nodes (multi-hop) is very important for comprehensive context <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
*   **Depth vs. Latency**: There's a trade-off between going deeper into the graph for better context and increasing latency <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. Finding the sweet spot is crucial for production environments <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **Acceleration**: Libraries like `cool graph` (integrated with NetworkX) can accelerate searches in large graphs, allowing for deeper traversal while reducing latency <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.

## [[evaluation_and_improvement_of_RAG_solutions | Evaluation and Improvement]] of [[graph_databases_and_technical_implementations | GraphRAG]] Solutions

[[evaluation_and_improvement_of_RAG_solutions | Evaluating the performance]] of [[graph_databases_and_technical_implementations | GraphRAG]] systems involves assessing multiple [[Metrics for RAG evaluation | factors]]: faithfulness, answer relevancy, precision, recall, helpfulness, correctness, coherence, and complexity <a class="yt-timestamp" data-t="12:24:00">[12:24:00]</a>.
*   **Ragas Library**: `Ragas` is a Python library specifically designed to [[tools_and_interfaces_for_rag_evaluation | evaluate RAG workflows]] end-to-end, assessing the response, retrieval, and query interpretation <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>. It uses an LLM (defaulting to GPT, but configurable) for evaluation <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
*   **Reward Models**: Models like Lanimotron 340B are trained to evaluate the responses of other LLMs based on various parameters <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>.
*   **Improvement Strategies**:
    *   **Data Cleaning**: Removing irrelevant characters (e.g., apostrophes) can improve triplet generation and overall results <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.
    *   **Fine-tuning LLMs**: Fine-tuning an LLM model can significantly improve the quality of generated triplets <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. For example, fine-tuning LLaMA 3.1 with LoRA improved accuracy from 71% to 87% in one experiment <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.
    *   **Optimizing Retrieval**: Small tweaks, such as adjusting multi-hop depth or leveraging acceleration libraries, can drastically reduce latency and improve performance <a class="yt-timestamp" data-t="18:44:00">[18:44:00]</a>.

## Deciding Between Semantic, [[graph_databases_and_technical_implementations | Graph]], or Hybrid RAG

The choice between a semantic, [[graph_databases_and_technical_implementations | graph-based]], or hybrid [[retrieval_augmented_generation_RAG | RAG]] system depends on two main factors <a class="yt-timestamp" data-t="19:16:00">[19:16:00]</a>:
1.  **Data Structure**: If the data is traditionally structured (e.g., retail, FSI, employee databases), [[graph_databases_and_technical_implementations | graph-based systems]] are often a good fit <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>. Even with unstructured data, if a high-quality [[graph_databases_and_technical_implementations | knowledge graph]] can be created, it's worth experimenting with the [[graph_databases_and_technical_implementations | graph path]] <a class="yt-timestamp" data-t="19:57:00">[19:57:00]</a>.
2.  **Application and Use Case**: If the use case requires understanding complex relationships to extract information for responses, then a [[graph_databases_and_technical_implementations | graph system]] makes sense <a class="yt-timestamp" data-t="20:10:00">[20:10:10]</a>. However, it's important to consider that [[graph_databases_and_technical_implementations | graph-based systems]] can be compute-heavy <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>.

## Philosophical and Practical Applications / Insights

### Knowledge Augment Generations (KAG)

[[graph_databases_and_technical_implementations | Knowledge Augment Generations (KAG)]] is differentiated from [[retrieval_augmented_generation_RAG | RAG]] by its emphasis on integrating structured [[graph_databases_and_technical_implementations | knowledge graphs]] for more accurate and insightful responses <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. KAG aims not just to retrieve but to understand, synthesize, and advise <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. This "wisdom" is actively guided by decision-making and fed by knowledge, experience, and insight <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

### Multi-Agent Systems and [[graph_databases_and_technical_implementations | Knowledge Graphs]]

[[graph_databases_and_technical_implementations | Knowledge graphs]] are particularly well-suited for building expert AI systems and multi-agent systems <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. They provide a systematic method for preserving wisdom by connecting concepts and creating a network of interconnected relationships <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.

One practical application is in competitive analysis, where a "wisdom engine" (orchestration agent) leverages different types of data (market data, past campaign experience, industrial insight, competitor weaknesses) to generate strategies and advise clients <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Tools like Node-RED, with its AI agent nodes, can facilitate the prototyping of such complex state diagrams <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

### Benchmarking and Performance

Leveraging [[graph_databases_and_technical_implementations | knowledge graphs]] with techniques like fusion-in-decoder can improve efficiency and reduce hallucination rates in [[retrieval_augmented_generation_RAG | RAG]] systems <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. Benchmarking on datasets like Amazon's Robust QA has shown that [[graph_databases_and_technical_implementations | graph-enhanced retrieval systems]] can achieve superior accuracy and faster response times compared to vector-only search systems <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

## Agent Memory and [[graph_databases_and_technical_implementations | Knowledge Graphs]]

Traditional vector database-based [[retrieval_augmented_generation_RAG | RAG]] approaches fall short for agent memory because they treat each fact as isolated and immutable, lacking native temporal and relational reasoning <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This can lead to generic or hallucinatory responses when agents forget important dynamic context about users <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Graffiti: A Temporal [[graph_databases_and_technical_implementations | Graph Framework]]

Graffiti is an open-source framework for building real-time, dynamic, temporal graphs designed to address these memory problems <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.
*   **Temporal Awareness**: Graffiti extracts and tracks multiple temporal dimensions for each fact, identifying when a fact is valid and becomes invalid <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This enables temporal reasoning, allowing agents to understand how preferences or traits change over time without deleting historical facts, instead marking them as invalid <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Relational Structure**: It allows for explicit relationships between facts, modeling causality <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.
*   **Hybrid Search**: Graffiti uses semantic search and BM25 full-text retrieval to identify subgraphs, which can then be traversed for a richer understanding of memory <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Domain-Aware Memory**: Developers can model their business domain on the graph by building custom entities and edges, enabling specific retrieval of relevant information and preventing irrelevant facts from polluting memory <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.

## Current Industry Trends and Applications

The industry is seeing a rise in [[graph_databases_and_technical_implementations | GraphRAG]] adoption due to its ability to provide context-rich, grounded, and explainable answers <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Gartner's 2024 hype cycle shows [[graph_databases_and_technical_implementations | GraphRAG]] trending upwards, providing more life to the AI ecosystem <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

### Enterprise Applications
*   **LinkedIn Customer Support**: Using [[graph_databases_and_technical_implementations | knowledge graphs]] for customer support scenarios has shown improved results, including a 28.6% reduction in median per-issue resolution time <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Data.world Study**: A comparison of [[retrieval_augmented_generation_RAG | RAG]] on SQL vs. [[graph_databases_and_technical_implementations | graph databases]] demonstrated a three-times improvement in LLM response accuracy with graphs <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Network Analysis**: Cisco's Outshift group is developing a multi-agent framework for network analysis. This system uses a network [[graph_databases_and_technical_implementations | knowledge graph]] (digital twin) to represent complex network environments, enabling agents to perform impact assessments, create test plans, and run tests in a predictive manner <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Fine-tuning query agents reduced token consumption and response time for interacting with the [[graph_databases_and_technical_implementations | knowledge graph]] <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Legal Industry**: Companies like YHAR.AI use [[graph_databases_and_technical_implementations | GraphRAG]] and multi-agent systems to find class action/mass cases, support legal discovery, and conduct case research from web-scraped data <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. The ability to structure and query information about individuals, products, harms, and jurisdictions within a [[graph_databases_and_technical_implementations | knowledge graph]] allows for precise filtering and reporting, even with natural language queries <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. This approach addresses the legal industry's need for high accuracy and explainability <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.

## Building and Querying [[graph_databases_and_technical_implementations | Knowledge Graphs]] for [[retrieval_augmented_generation_RAG | RAG]]

The construction of [[graph_databases_and_technical_implementations | knowledge graphs]] for [[retrieval_augmented_generation_RAG | RAG]] typically involves three phases <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>:
1.  **Lexical Graph Construction**: Substructuring unstructured information into a lexical graph representing documents, chunks, and their basic relationships (e.g., predecessor/successor, parent) <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
2.  **Entity Extraction**: Using LLMs with a defined [[graph_databases_and_technical_implementations | graph schema]] to extract entities and relationships from the lexical graph <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. This can involve extracting new entities or recognizing and connecting to existing ground truth data in an existing [[graph_databases_and_technical_implementations | knowledge graph]] <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
3.  **Graph Enrichment**: Running [[evaluation and performance metrics of graphbased systems | graph algorithms]] (e.g., PageRank, community detection) to enrich the graph, identifying cross-document topics or clusters <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

For retrieval, a [[graph_databases_and_technical_implementations | GraphRAG]] retriever performs an initial index search (vector, full-text, etc.) to find entry points in the graph <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. It then follows relationships to a certain depth or relevancy, fetching additional context, which can also incorporate external user context <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This richer, more complete subset of the contextual graph is then passed to the LLM for answer generation <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Modern LLMs are increasingly trained to process these structured patterns, such as node-relationship-node patterns <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

Libraries and tools supporting these processes include Neo4j, ArangoDB, Cognify, Zep's Graffiti, and the `graph-rag` Python package, offering functionalities from [[graph_databases_and_technical_implementations | knowledge graph]] construction to various retrieval strategies <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.