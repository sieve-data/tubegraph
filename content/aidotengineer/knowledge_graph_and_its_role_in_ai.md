---
title: Knowledge graph and its role in AI
videoId: RR5le0K4Wtw
---

From: [[aidotengineer]] <br/> 

Knowledge graphs are an increasingly vital component in modern artificial intelligence systems, particularly within the realm of Retrieval Augmented Generation (RAG). They offer a structured way to represent information and its complex relationships, addressing limitations of traditional semantic search methods <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## What is a Knowledge Graph?

A knowledge graph is fundamentally a network that represents relationships between different entities <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. These entities can be anything from people, places, concepts, to events <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The crucial aspect is the "edge of relationship" between two entities, which only [[graph_data_structures_in_ai_and_its_benefits | graph-based networks]] or knowledge graphs can effectively exploit <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

[[graph_data_structures_in_ai_and_its_benefits | Knowledge graphs]] are essential for preserving wisdom by connecting information and creating a network of interconnected relationships <a class="yt-timestamp" data-t="02:41:40">[02:41:40]</a>. They represent the thought process and a comprehensive taxonomy of a specific domain of expertise, enabling AI systems to offer advice rather than just retrieve data <a class="yt-timestamp" data-t="02:49:50">[02:49:50]</a>. The universe itself can be thought of as a temporal network database with a graph structure, preserving causal links through relationships <a class="yt-timestamp" data-t="01:36:54">[01:36:54]</a>. This ability to maintain causal links is key to solving hallucinations in AI and optimizing hypothesis generation and testing <a class="yt-timestamp" data-t="01:38:44">[01:38:44]</a>.

## Knowledge Graphs vs. Traditional RAG

While RAG (Retrieval Augmented Generation) is not considered "dead," its traditional vector database-based approach has limitations. If a basic RAG system can solve the problem in production, a more complex agent system may not be necessary <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. However, traditional RAG systems based on vector databases primarily rely on semantic similarity, which may not be the same as relevance <a class="yt-timestamp" data-t="02:26:50">[02:26:50]</a>.

**Advantages of Knowledge Graphs in RAG:**
*   **Detailed Information Capture**: Knowledge graphs capture information between entities in much greater detail, providing a comprehensive view of knowledge <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Contextual Understanding**: Unlike semantic vector databases, knowledge graphs excel at exploiting relationships between entities, which is crucial for deep contextual understanding <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
*   **Data Organization**: They have the ability to organize data from multiple sources effectively <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Temporal and Relational Reasoning**: Traditional RAG lacks native temporal and relational reasoning <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>. Knowledge graphs, especially those with temporal awareness like Graffiti, can model "why" things change over time and enable richer reasoning <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>.
*   **Explainability**: [[graph_data_structures_in_ai_and_its_benefits | Graph RAG]] offers better explainability by visualizing and analyzing the structured nodes and semantics, unlike statistical probabilities from vector databases <a class="yt-timestamp" data-t="02:29:28">[02:29:28]</a>.
*   **Reduced Hallucination**: Knowledge graphs can help reduce the hallucination rate in LLMs <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
*   **Efficiency**: Using knowledge graphs in conjunction with techniques like fusion and decoder can improve efficiency and lower costs <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>. Early studies show a three times improvement in accuracy with [[graph_data_structures_in_ai_and_its_benefits | Graph RAG]] compared to SQL-based RAG <a class="yt-timestamp" data-t="02:31:20">[02:31:20]</a>.

### Knowledge Augmented Generation (KAG)
KAG is an enhanced language model approach that integrates structured knowledge graphs for more accurate and insightful responses <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Unlike simple RAG, KAG understands and advises, rather than just retrieves <a class="yt-timestamp" data-t="02:57:07">[02:57:07]</a>. Experts often have common ways of thinking and decision-making, which knowledge graphs can perfectly fit to store and leverage <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>.

## Building a Graph RAG System

Building a graph RAG or hybrid system involves four key components: data, data processing, graph creation (or semantic embedding vector database creation), and inferencing <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### 1. Data Processing and Graph Creation
The quality of data processing directly impacts the quality of the knowledge graph and subsequent retrieval <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

*   **Triplet Creation**: The goal is to create triplets (Subject-Predicate-Object) that define the relationship between entities, which is a strength of graph-based systems <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **LLM-powered Extraction**: Large Language Models (LLMs) are crucial for extracting structured information and triplets from unstructured documents <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Ontology and Prompt Engineering**: Defining a clear ontology based on the use case and using precise prompt engineering are critical <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This stage is where developers might spend about 80% of their time to ensure a high-quality ontology and accurate triplets <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Noisy triplets lead to noisy retrieval <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Data Cleaning**: Small tweaks like removing apostrophes or other irrelevant characters can significantly improve results in triplet generation <a class="yt-timestamp" data-t="01:53:08">[01:53:08]</a>, leading to better accuracy <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>.

### 2. Semantic Vector Database Creation
This is a more straightforward and well-studied process <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Documents are broken into chunks with appropriate overlap (to maintain context), converted into vector embeddings using an embedding model, and stored in a vector database <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### 3. Graph Enrichment
Once the base knowledge graph is constructed, it can be further enriched:
*   **Graph Algorithms**: Running [[graph_data_structures_in_ai_and_its_benefits | graph algorithms]] like PageRank, community detection, or link prediction can enrich data and identify cross-document topics or communities <a class="yt-timestamp" data-t="02:36:39">[02:36:39]</a>.
*   **LLM-Generated Summaries**: LLMs can generate summaries for identified communities or clusters in the entity graph <a class="yt-timestamp" data-t="02:36:49">[02:36:49]</a>.

## Retrieval in Graph RAG

Retrieval is the process of querying the knowledge graph to answer user questions <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

*   **Multi-Hop Search**: A crucial advantage of knowledge graphs is the ability to exploit relationships through multiple nodes (hops) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. While deeper hops provide richer context, they also increase retrieval latency <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Finding a "sweet spot" between depth and latency is important for production environments <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Accelerated Search**: Libraries like `cuGraph` (integrated with `NetworkX`) can accelerate graph searches, allowing for deeper traversal while reducing latency and improving performance <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   **Hybrid Retrieval**: A graph RAG retriever can perform an initial index search (e.g., vector, full-text) to find entry points in the graph, then follow relationships to retrieve additional context based on relevance and external user context <a class="yt-timestamp" data-t="02:37:27">[02:37:27]</a>. Modern LLMs are increasingly trained to process graph structures, allowing them to handle node-relationship-node patterns as additional context <a class="yt-timestamp" data-t="02:38:33">[02:38:33]</a>.

## Evaluating Performance

Evaluating a graph RAG system involves multiple factors and specialized tools:

*   **Metrics**: Key metrics include faithfulness, answer relevancy, precision, recall, helpfulness, collectiveness, coherence, complexity, and verbosity <a class="yt-timestamp" data-t="01:28:20">[01:28:20]</a>.
*   **Ragas Library**: `Ragas` is a Python library specifically designed to evaluate RAG workflows end-to-end, assessing the response, retrieval, and query interpretation <a class="yt-timestamp" data-t="01:42:36">[01:42:36]</a>. It uses an LLM (defaulting to GPT but allowing custom models) for evaluation across several parameters <a class="yt-timestamp" data-t="01:32:57">[01:32:57]</a>.
*   **Reward Models**: Specialized reward models, like Nvidia's Lanimotron 340B, can judge the responses of other LLMs based on specific parameters <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>.

## Optimization Strategies

Improving the performance of a graph RAG system, especially the last 20% of the job, can take 80% of the time due to iterative fine-tuning <a class="yt-timestamp" data-t="01:50:02">[01:50:02]</a>.

*   **Knowledge Graph Quality**: The better the knowledge graph, the better the results <a class="yt-timestamp" data-t="01:51:21">[01:51:21]</a>.
*   **LLM Fine-tuning**: Fine-tuning LLMs can significantly improve the quality of generated triplets and overall accuracy. For example, fine-tuning a Llama 3.1 model improved accuracy from 71% to 87% in one experiment <a class="yt-timestamp" data-t="01:57:07">[01:57:07]</a>.
*   **Data Pre-processing**: Simple data cleaning steps, like removing apostrophes or unnecessary characters, can lead to better triplet generation <a class="yt-timestamp" data-t="01:58:34">[01:58:34]</a>.

## Applications and Use Cases

The choice between a semantic RAG system, a graph-based RAG system, or a hybrid approach depends on the data and the specific use case <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

### Data Characteristics
*   **Structured Data**: Data from retail, FSI (Financial Services Industry), or employee databases often have good predefined structures, making them excellent use cases for [[adoption_of_knowledge_graphs_in_enterprise_ai | graph-based systems]] <a class="yt-timestamp" data-t="01:51:40">[01:51:40]</a>.
*   **Unstructured Data**: If a good knowledge graph can be created from unstructured data, experimenting with a [[graph_data_structures_in_ai_and_its_benefits | graph path]] is worthwhile <a class="yt-timestamp" data-t="02:06:58">[02:06:58]</a>.

### Specific Use Cases
*   **Complex Relationship Understanding**: If a use case requires understanding complex relationships to extract information for responses, graph-based systems are beneficial <a class="yt-timestamp" data-t="02:12:41">[02:12:41]</a>.
*   **Agent Memory**: Knowledge graphs are excellent for building real-time, dynamic, temporal memory for [[applications_and_future_of_ai_technology | AI agents]] <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>. They enable agents to reason about temporal changes and causal relationships, which traditional vector database RAG cannot <a class="yt-timestamp" data-t="00:40:52">[00:40:52]</a>. Zep's Graffiti framework, for instance, uses temporal graphs for agent memory <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>.
*   **Domain-Aware Memory**: Allowing developers to model their business domain on the graph enables highly relevant memory retrieval specific to an application (e.g., financial goals for a finance coach vs. media preferences for a music assistant) <a class="yt-timestamp" data-t="01:57:51">[01:57:51]</a>.
*   **Competitive Analysis**: Knowledge graphs can power expert AI systems for tasks like competitive analysis, turning data into strategy by mapping insights, experience, and situations <a class="yt-timestamp" data-t="03:00:10">[03:00:10]</a>.
*   **Network Operations**: In complex network environments, knowledge graphs can represent network components, their relationships, and configuration data, serving as a digital twin for multi-agent systems to perform tasks like impact assessment and test plan generation <a class="yt-timestamp" data-t="02:48:49">[02:48:49]</a>.
*   **Legal Industry**: Knowledge graphs are crucial for legal applications where accuracy and explainability are paramount <a class="yt-timestamp" data-t="03:10:22">[03:10:22]</a>. They facilitate:
    *   **Legal Discovery**: Structuring vast amounts of unstructured data (e.g., emails) into a graph format allows immediate identification of relevant information, augmenting it for visual decision-making by experts <a class="yt-timestamp" data-t="03:15:31">[03:15:31]</a>.
    *   **Case Research**: Scraping web data, filtering it down to specific signals based on lawyer-defined schemas, and generating personalized reports is possible <a class="yt-timestamp" data-t="03:19:21">[03:19:21]</a>. This enables early identification of potential lawsuits (e.g., product complaints) <a class="yt-timestamp" data-t="03:21:03">[03:21:03]</a>.

## The Future of AI Memory

The future of [[applications_and_future_of_ai_technology | AI]] memory lies in [[layered_chain_of_thought_for_robust_ai | agentic systems]] that follow the network database principle, requiring [[graph_data_structures_in_ai_and_its_benefits | graph databases]] to recover causality from fuzzy data <a class="yt-timestamp" data-t="01:41:14">[01:41:14]</a>. Tools like GraphRack Chat Arena are being developed for simulating and evaluating evolving [[applications_and_future_of_ai_technology | agentic graph memory]] <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. The [[adoption_of_knowledge_graphs_in_enterprise_ai | adoption of knowledge graphs in enterprise AI]] is trending upwards, as shown by Gartner's hype cycle, indicating their increasing importance in breathing life into the [[applications_and_future_of_ai_technology | AI ecosystem]] <a class="yt-timestamp" data-t="02:30:12">[02:30:12]</a>. Leading organizations are already deploying production applications leveraging knowledge graphs <a class="yt-timestamp" data-t="02:30:41">[02:30:41]</a>.