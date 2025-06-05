---
title: Solutions to improve RAG systems
videoId: Ywl4LsvHKzU
---

From: [[aidotengineer]] <br/> 

While Retrieval Augmented Generation (RAG) systems are prevalent, their evaluation and performance in real-world scenarios often fall short of expectations, leading to a "broken" evaluation process <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Existing benchmarks, often designed with "local questions that have local answers" <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, fail to represent the messier, more diverse nature of real-world data <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

Traditional RAG benchmarks frequently focus on either retrieval-only or generation-only aspects, neglecting crucial steps like chunking and parsing, and specific cases where answers are not confined to a single data point <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This creates a [[challenges_in_rag_evaluation | vicious cycle]] where systems are optimized for flawed benchmarks, perform well on them, but then struggle when applied to customer data <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Addressing Aggregative Questions with Structured Data
To overcome the [[limitations_of_current_rag_benchmarks | limitations of current RAG benchmarks]] and improve RAG performance for complex queries, particularly aggregative questions, a proposed solution involves converting unstructured corpora into structured data <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. Aggregative questions include those asking "which company has reported the highest quarterly revenue the most times" or "how many fiscal years did Apple exceed hundred billion in annual revenue?" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Common RAG pipelines often fail miserably on such questions, correctly answering only 5-11% in tests <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

The core idea is to handle these types of queries as [[use_of_sql_in_structured_rag_data_processing | SQL]] questions <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, which traditional RAG struggles with because it typically just grabs a limited number of "top k chunks" <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### The Two-Phase Approach
This structured data approach splits the process into two main phases, similar to a regular RAG flow, where compute is invested in ingestion for quicker inference <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>:

#### Ingestion Phase
1.  **Document Clustering**: Documents are first clustered into sub-corpora (e.g., financial corpus, FIFA World Cup corpus) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
2.  **Schema Identification**: For each sub-corpus, a relevant schema representing the data is identified <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  **Schema Population**: An LLM-based pipeline is used to populate this schema according to each document <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
4.  **Database Upload**: The results are then uploaded into a [[use_of_sql_in_structured_rag_data_processing | SQL]] database <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

#### Inference Phase
1.  **Schema Identification**: When a query is received, the relevant schema (e.g., financial or FIFA World Cup) is identified <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
2.  **Text-to-SQL Conversion**: A [[use_of_sql_in_structured_rag_data_processing | text-to-SQL]] conversion is performed over the structured data <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
3.  **Answer Return**: The final answer is returned based on the [[use_of_sql_in_structured_rag_data_processing | SQL]] query result <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

For example, to answer "Which team has won the FIFA World Cup the most times?" a simple [[use_of_sql_in_structured_rag_data_processing | SQL]] query would be executed against a populated database <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

## Limitations of the Structured Approach
While effective for certain types of queries, this approach does not solve all RAG problems <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Key [[challenges_in_rag_evaluation | challenges]] include:

*   **Corpus Heterogeneity**: Not every corpus or query is suitable for a relational database model, nor is every corpus homogeneous enough to easily derive an underlying schema <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **[[normalization_issues_in_rag_systems | Normalization Issues]]**: Even in simple examples like the FIFA World Cup corpus, issues arise (e.g., "West Germany" vs. "Germany" for host country, singular vs. list attributes for hosts like South Korea and Japan) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Ambiguity and Abstinence**: LLMs may try to answer queries even when the question is irrelevant to the schema (e.g., asking about Real Madrid's win in a World Cup schema) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Trade-offs in Ingestion**: There's a trade-off between the complexity and granularity of clustering and schema inference during ingestion versus the computational investment <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Complex Text-to-SQL**: As schemas become more complex, the [[use_of_sql_in_structured_rag_data_processing | text-to-SQL]] conversion itself becomes a significant challenge <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Key Takeaways for Improving RAG Systems
Ultimately, RAG is not a one-size-fits-all solution, and each client or use case may require a tailored approach <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The standard RAG pipeline of chunking, embedding, retrieving, and reranking is often insufficient for many types of questions <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. Existing benchmarks fail to capture the nuances of these real-world use cases <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. To address the limitations and improve RAG performance in specific settings, it is often necessary to go beyond standard RAG pipelines <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.