---
title: Evaluation and performance metrics of graphbased systems
videoId: RR5le0K4Wtw
---

From: [[aidotengineer]] <br/> 

Evaluating the performance of AI systems, particularly those employing Retrieval Augmented Generation (RAG) and graph structures, is crucial for their effectiveness and reliability <a class="yt-timestamp" data-t="01:25:05">[01:25:05]</a>. This involves understanding various metrics and optimization strategies to ensure accurate and insightful responses <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Importance of Evaluation in AI Systems
[[importance_of_evaluation_and_metrics_in_ai_systems | Evaluation]] is a critical component in the development and deployment of AI systems, especially for RAG pipelines <a class="yt-timestamp" data-t="01:22:21">[01:22:21]</a>. It helps in assessing factors like faithfulness, answer relevancy, precision, and recall <a class="yt-timestamp" data-t="01:16:19">[01:16:19]</a>. Without robust [[evaluation_and_feedback_in_ai_systems | evaluation]] mechanisms, systems might respond generically or even hallucinate, leading to poor user experience <a class="yt-timestamp" data-t="00:39:29">[00:39:29]</a>.

## General RAG Evaluation Metrics
For RAG systems, several [[metrics_for_rag_evaluation | metrics]] are vital:
*   **Faithfulness**: How well the generated answer is supported by the retrieved context <a class="yt-timestamp" data-t="01:12:28">[01:12:28]</a>.
*   **Answer Relevancy**: The degree to which the answer addresses the user's query <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.
*   **Precision and Recall**: Traditional information retrieval metrics to assess the completeness and accuracy of retrieval <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>.
*   **Helpfulness, Correctness, Coherence, Complexity, Verbosity**: These factors are also considered when evaluating the LLM's output <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

## [[evaluating_ai_agent_performance_and_reliability | Evaluating AI Agent Performance and Reliability]]
[[evaluating_ai_agent_performance_and_reliability | Evaluating]] the performance and reliability of AI agents is paramount <a class="yt-timestamp" data-t="01:12:24">[01:12:24]</a>. Tools like Ragas are designed to evaluate the entire RAG workflow from end to end, assessing the query, retrieval, and response phases <a class="yt-timestamp" data-t="01:12:42">[01:12:42]</a>. Ragas can break down responses and provide an eventual score <a class="yt-timestamp" data-t="01:13:07">[01:13:07]</a>. While Ragas uses LLMs for evaluation, it also allows users to bring their own models <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>. Reward models, such as Lanimotron 340 billion, are specifically trained to judge the responses of other LLMs based on various parameters <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>.

## Performance Metrics in [[graphrag_systems_and_applications | GraphRAG Systems and Applications]]
[[graph_data_structures_in_ai_and_its_benefits | Graph data structures]] excel at capturing detailed relationships between entities, which is often missed by semantic vector databases <a class="yt-timestamp" data-t="03:49:56">[03:49:56]</a>. This ability to exploit relationships through multiple nodes makes graph-based systems highly valuable <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

### Knowledge Graph Quality
The quality of the knowledge graph directly impacts retrieval performance <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Creating accurate triplets (entity-relationship-entity) from unstructured data is crucial and often requires significant effort, sometimes taking 80% of the development time <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Noise in triplets leads to noisy retrieval <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Prompt engineering and defining ontology for LLM extraction are key steps in this process <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

### Retrieval Strategies and Latency
In [[graph_databases_and_technical_implementations | graph-based systems]], retrieval involves traversing nodes and relationships. Different strategies, such as single-hop or multi-hop searches, influence the depth of context retrieved <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. While deeper searches provide better context, they can increase latency, which is a critical factor in production environments <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. Finding a "sweet spot" between retrieval depth and acceptable latency is essential <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

Search acceleration, for instance, using libraries like CoolGraph, can help mitigate latency issues in large graphs with millions or billions of nodes <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This allows for deeper graph traversal without significant performance degradation <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

### Semantic and Behavioral Evaluation of Agents
[[semantic_and_behavioral_evaluation_of_agents | Semantic and behavioral evaluation]] is particularly relevant for agents interacting with dynamic data <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Traditional RAG systems based on vector databases struggle with temporal and relational reasoning, as facts are isolated and immutable <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. Graph structures, however, can explicitly define relationships and model causality, enabling agents to reason about how facts change over time <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>. This includes tracking temporal dimensions of facts (when a fact is valid or invalid) to support complex temporal reasoning <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>.

## Strategies for [[improving_benchmark_systems_for_accurate_evaluation | Improving Benchmark Systems for Accurate Evaluation]]
Optimizing [[graphrag_systems_and_applications | GraphRAG systems]] to improve performance and accuracy involves several iterative strategies <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>:
*   **Data Cleaning**: Removing irrelevant characters like apostrophes and brackets can lead to better triplet generation and improved results <a class="yt-timestamp" data-t="01:16:31">[01:16:31]</a>.
*   **LLM Fine-tuning**: Fine-tuning an LLM model, such as Llama 3.1, can significantly enhance the quality of generated triplets and boost accuracy (e.g., from 71% to 87%) <a class="yt-timestamp" data-t="01:15:38">[01:15:38]</a>.
*   **Reducing Output Length**: Strategies to reduce the length of LLM outputs while maintaining information can also lead to better results <a class="yt-timestamp" data-t="01:16:51">[01:16:51]</a>.
*   **Accelerated Search**: Utilizing libraries like CoolGraph, integrated with tools like NetworkX, can drastically reduce execution latency for graph algorithms, improving overall system performance <a class="yt-timestamp" data-t="01:17:37">[01:17:37]</a>.

## Challenges and Considerations
The choice between semantic RAG, graph-based RAG, or a hybrid approach depends on the data and the specific use case <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>. Graph-based systems are particularly well-suited for data with inherent structures, such as retail, financial services, or employee databases <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. They are beneficial when the use case requires understanding complex relationships and extracting information based on those connections <a class="yt-timestamp" data-t="01:20:10">[01:20:10]</a>. However, graph systems can be compute-heavy, necessitating careful consideration of latency and resource allocation <a class="yt-timestamp" data-t="01:20:26">[01:20:26]</a>.

One of the significant challenges is dealing with "bad memory" or outdated facts <a class="yt-timestamp" data-t="02:11:26">[02:11:26]</a>. Graph-based systems address this by not deleting historical facts but marking them as invalid, preserving a sequence of state changes <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>. This allows agents to reason with these changes over time <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. Managing the ontology and business domain modeling within the graph structure also allows for more relevant retrieval by filtering out irrelevant facts <a class="yt-timestamp" data-t="01:55:51">[01:55:51]</a>.

## Conclusion
Effective [[evaluation_and_feedback_in_ai_systems | evaluation]] and performance optimization of [[graphrag_systems_and_applications | graph-based systems]] are vital for building robust and reliable AI applications. By leveraging graph data structures to capture intricate relationships and implementing strategies for efficient retrieval and continuous improvement, these systems can provide more accurate, contextual, and explainable answers, overcoming the limitations of traditional vector-based RAG <a class="yt-timestamp" data-t="02:28:54">[02:28:54]</a>.