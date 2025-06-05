---
title: Use of SQL in structured RAG data processing
videoId: Ywl4LsvHKzU
---

From: [[aidotengineer]] <br/> 

Traditional Retrieval Augmented Generation (RAG) systems often struggle with complex, aggregative questions that require information from multiple sources or a structured understanding of data <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Conventional RAG pipelines, which typically grab the top-k chunks and attempt to compile an answer, perform poorly on such queries <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>, <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. This limitation leads to a disconnect between high scores on [[limitations_of_current_RAG_benchmarks | flawed benchmarks]] and actual performance with user data <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## Limitations of Traditional RAG for Complex Queries
Many real-world questions, especially in domains like financial data, are aggregative <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>, <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Examples include:
*   "Which company has reported the highest quarterly revenue the most times?" <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>
*   "In how many fiscal years did Apple exceed hundred billion in annual revenue?" <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>
*   "List all Fortune 500 companies." <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>

Traditional RAG systems find these challenging because they rely on retrieving a limited number of chunks, which might not contain all the necessary information for a complete aggregate answer <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>, <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. A small corpus of FIFA World Cup historical pages, for instance, showed common RAG pipelines answering only 5-11% of such questions correctly <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>, <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>, <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>, <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Structured RAG with SQL
A proposed solution to address these [[challenges_in_RAG_evaluation | challenges in RAG evaluation]] is to convert unstructured data into a structured format, like a database, and then process queries on top of this structured data <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>, <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>, <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. The nature of these aggregative questions (counting, max/min, calculations) is inherently SQL-like <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>, <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>, <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>.

This approach splits the process into two main phases:

### Ingestion Phase
This phase involves investing compute to structure the data <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>:
1.  **Document Clustering**: Documents are grouped into sub-corpuses (e.g., financial data, FIFA World Cup data) <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>, <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>, <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.
2.  **Schema Identification**: For each sub-corpus, a relevant schema is identified <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>, <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.
3.  **Schema Population**: An LLM-based pipeline populates the identified schema using data from each document <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>, <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>, <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. For the FIFA World Cup corpus, a schema might include attributes like year, winner, top three teams, and top scorer <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>, <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>, <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>, <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
4.  **Database Upload**: The populated schema and data are then uploaded into an SQL database <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>, <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

### Inference Phase
This phase focuses on quick query processing <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>:
1.  **Schema Identification for Query**: When a query is received, the relevant schema (e.g., financial or FIFA) is identified <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>, <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>, <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.
2.  **Text-to-SQL Conversion**: A standard text-to-SQL process is performed on the identified schema within the SQL database <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
3.  **Answer Retrieval**: The final answer is returned directly from the SQL query result <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>, <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. For example, "Which team has won the FIFA World Cup the most times?" becomes a simple SQL query <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>, <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>, <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

## Limitations of the Structured RAG Approach
While effective for certain use cases, this approach does not solve all RAG challenges <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>, <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>:
*   **Corpus Suitability**: Not every corpus or query is suitable for a relational database model <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>, <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. Not all data is homogeneous or necessarily contains an underlying schema <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>, <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>, <a class="yt-timestamp" data-t="08:19:00">[08:19:00]</a>.
*   [[normalization_issues_in_RAG_systems | Normalization Issues]]: Even with simple examples like the FIFA World Cup data, building the correct schema can be challenging <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>, <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>. Questions arise about how to normalize data points (e.g., "West Germany" vs. "Germany" for host country) or handle multi-valued attributes (e.g., "South Korea and Japan" co-hosting) <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>, <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>, <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>, <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>, <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>, <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>.
*   **Ambiguity**: LLMs may try to answer questions even if they don't directly fit the schema, leading to potentially incorrect or irrelevant responses <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>, <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>, <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.
*   **Trade-offs**: There are trade-offs between complexity, granularity, and computational investment during schema inference and clustering in the ingestion phase <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>, <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>, <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
*   **Text-to-SQL Complexity**: Text-to-SQL remains a complex issue, especially with intricate schemas <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>, <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Conclusion
RAG is not a one-size-fits-all solution, and different clients and data types require tailored approaches <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>, <a class="yt-timestamp" data-t="10:03:00">[10:03:00]</a>. For specific settings involving structured data or aggregative queries, going beyond the standard RAG pipeline (chunking, embedding, retrieving, reranking) to incorporate SQL databases can significantly improve performance and address [[challenges_in_RAG_evaluation | existing benchmark failures]] <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>, <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>, <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>, <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.