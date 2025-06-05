---
title: Normalization issues in RAG systems
videoId: Ywl4LsvHKzU
---

From: [[aidotengineer]] <br/> 

Current RAG (Retrieval Augmented Generation) evaluation systems often struggle with real-world data, which is inherently messier and less generalized than data used in most benchmarks <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This leads to a vicious cycle where RAG systems are optimized for flawed benchmarks, perform well on those benchmarks, but then struggle with actual user or customer data <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. One significant aspect of this challenge lies in normalization issues when attempting to structure unstructured data for RAG systems.

## Limitations of Current Benchmarks and Standard RAG
Most existing RAG benchmarks are limited, often focusing on retrieval-only or generation-only tasks <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. They frequently assume that answers lie within specific chunks of data <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>, and often use "multiple hope questions" that are not realistic <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. They fail to test the entire system holistically, overlooking aspects like chunking, parsing, and cases where answers aren't in a direct, local segment <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

Standard RAG pipelines, which typically involve chunking, embedding, retrieving, and reranking, are often insufficient for many complex questions, especially those requiring aggregation or analysis across multiple data points <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>. For example, questions like "which company has reported the highest quarterly revenue the most times" <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a> or "how many fiscal years did Apple exceed hundred billion in annual revenue?" <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a> cause current RAG systems to struggle because they are limited to grabbing top K chunks and compiling answers from those <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

An experiment with FIFA World Cup historical data showed that common RAG pipelines achieved only 5% to 11% accuracy on such questions <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

## Structuring Unstructured Data for Better RAG
To address these limitations, one approach is to convert unstructured corpuses into structured data, then pose questions on top of this structured data <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>. This is particularly effective for questions that are essentially SQL-like queries, involving counting, max/min calculations, or other aggregations <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.

This process involves:
1.  **Ingestion Phase:**
    *   Clustering documents into sub-corpuses (e.g., financial data, FIFA World Cup data) <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
    *   Identifying a schema that represents each sub-corpus <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.
    *   Populating the schema using an LLM pipeline for every document <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
    *   Uploading the results into an SQL database <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.
2.  **Inference Flow:**
    *   Identifying the relevant schema for a given query (e.g., financial or FIFA World Cup) <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
    *   Performing a text-to-SQL conversion over the structured data to return the final answer <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.

For instance, with the FIFA World Cup corpus, a schema could include attributes like year, winner, top three teams, and top scorer <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. A question like "which team has won the FIFA World Cup the most times?" <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a> would translate into a simple SQL query <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.

## Normalization Challenges and Other Limitations
Despite the benefits of this structured approach, it does not solve all problems in RAG evaluation and system design <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. Significant challenges arise, particularly concerning normalization:

### Schema Inconsistencies and Homogeneity
Not every corpus or query is suitable for a relational database model <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. Furthermore, not every corpus is homogeneous in terms of its attributes, and an underlying schema may not always be easily discernible <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.

### Normalization Difficulties
Even with seemingly straightforward examples like the FIFA World Cup data, building the correct schema can be a struggle due to normalization issues <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>:
*   **Geographical/Historical Variations:** For a "host country" attribute, "West Germany" might appear, but a user could ask about "Germany" <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>. Determining whether "West Germany" should count as "Germany" for aggregation is a normalization challenge.
*   **Singular vs. List Attributes:** The "host country" might sometimes be a singular entity, but other times it could be a list (e.g., "South Korea and Japan" hosted together) <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. This requires careful consideration during schema design and data population.

These normalization issues impact both the ingestion and inference phases of the system <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Ambiguity and LLM Behavior
Ambiguity in user queries can also pose problems <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. If a user asks a question not directly related to the current schema (e.g., "did Real Madrid win the 2006 final?" in a World Cup context), LLMs tend to try and "please the users" by attempting to answer even if the data isn't directly relevant or complete <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.

### Complexity and Compute Trade-offs
There is a trade-off between the complexity and granularity of clustering and schema inference during the ingestion phase and the amount of compute power required <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. Additionally, transforming text to SQL queries becomes increasingly complex as the schemas themselves become more intricate <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

## Conclusion
[[monitoring_tracing_and_evaluation_in_rag_systems | RAG evaluation]] highlights that RAG is not a one-size-fits-all solution; each client and dataset needs separate consideration <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Standard RAG pipelines and [[limitations_of_current_rag_benchmarks | existing benchmarks fail to capture]] the nuances of complex use cases, particularly those involving aggregation and requiring structured understanding of data <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>. To overcome these [[challenges_in_rag_evaluation | challenges]], especially normalization issues, it's often necessary to go beyond standard RAG approaches for specific settings <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.