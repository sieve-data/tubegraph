---
title: Challenges in RAG evaluation
videoId: Ywl4LsvHKzU
---

From: [[aidotengineer]] <br/> 

Despite the perception that Retrieval Augmented Generation (RAG) is a solved problem, its evaluation presents significant challenges <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The core issue is that [[limitations_of_current_rag_benchmarks | RAG evaluation is broken]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Issues with Current RAG Benchmarks
The primary reasons for the broken state of RAG evaluation stem from how easily benchmarks are constructed <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>:

*   **Local Questions and Answers** Most benchmarks consist of "local questions that have local answers," assuming the answer resides within a specific data chunk <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Unrealistic Scenarios** Benchmarks are often manufactured and do not represent real-world data <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. For instance, "multiple hope questions" famously framed by Google, are not realistic <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Lack of Holistic Testing** Existing benchmarks typically test only a part of the RAG system:
    *   **Retrieval-only benchmarks** focus on retrieving the best segments or chunks, assuming the answer is within them <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   **Generation-only benchmarks** (grounding benchmarks) assess if a question can be answered based on context already provided in the prompt <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   They neglect crucial pipeline stages like chunking, parsing, or cases where answers are not directly localized in the data <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Disconnection from Real-World Data** Benchmarks often do not correlate with real-world data, which is typically messier and more diverse <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

This leads to a vicious cycle where RAG systems are developed for flawed benchmarks, achieve high scores, but then struggle when applied to user or customer data <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Performance Limitations of Standard RAG Pipelines
Standard RAG pipelines, which simply retrieve `top k` chunks, struggle with complex query types <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>:

*   **Aggregative Questions** They fail to answer questions requiring aggregation or calculations, such as "which company has reported the highest quarterly revenue the most times?" or "how many fiscal years did Apple exceed hundred billion in annual revenue?" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **"All of Something" Questions** Queries like "all Fortune 500 companies" are problematic because limiting retrieval to `top k` chunks might miss relevant information beyond that threshold <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

An experiment using a small corpus of FIFA World Cup historical data demonstrated these limitations. A common RAG pipeline (e.g., using LangChain or LlamaIndex) and OpenAI responses answered only 5% to 11% of questions correctly, even for answers found in local segments <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## [[solutions_to_improve_rag_systems | Solutions to Improve RAG Systems]]: Beyond Standard RAG
To address these challenges, a proposed approach involves converting unstructured data into a structured format and then querying that structure <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This is because many complex questions are inherently SQL-like (counting, max/min, calculation) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The process is split into two phases, similar to standard RAG, optimizing compute in ingestion for faster inference:

### Ingestion Phase
1.  **Cluster Documents** Documents are first grouped into subcorpuses (e.g., financial corpus, FIFA World Cup corpus) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
2.  **Identify Schema** A schema is identified for each subcorpus <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  **Populate Schema** An LLM pipeline populates this schema with data from each document <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. For example, a FIFA corpus schema might include year, winner, top three teams, and top scorer <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
4.  **Upload to SQL DB** The results are then uploaded to an SQL database <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Inference Flow
1.  **Identify Relevant Schema** When a query is received, the system identifies the schema relevant to that query (e.g., financial or FIFA World Cup) <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
2.  **Text-to-SQL** A text-to-SQL process is performed over the structured data to generate the final answer <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. For instance, "which team has won the FIFA World Cup the most times?" becomes a simple SQL query <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Limitations of Structured RAG Solutions
While promising, this structured approach has its own challenges:

*   **Applicability** Not every corpus or query is suitable for a relational database model <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Not all corpuses are homogeneous or necessarily contain an underlying schema <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **[[normalization_issues_in_rag_systems | Normalization Issues]]** Even in simple examples like the FIFA World Cup data, building a correct schema can be challenging. Questions arise regarding entities like "West Germany" vs. "Germany" or whether an attribute like "host country" should be singular or a list (e.g., South Korea and Japan hosting together) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Ambiguity/Abstinence** LLMs tend to try to please users, which can lead to attempts to answer irrelevant questions (e.g., "did Real Madrid win the 2006 final?" in a World Cup context) <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Ingestion Trade-offs** There's a trade-off between the complexity and granularity of clustering and schema inference during ingestion versus the computational investment <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Text-to-SQL Complexity** Generating SQL from natural language becomes increasingly complex as schemas become more intricate <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

## Key Takeaways
*   RAG is not a one-size-fits-all system; different clients and use cases require tailored approaches <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   The standard RAG pipeline (chunking, embedding, retrieving, reranking) is insufficient for many types of questions <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   Existing benchmarks fail to capture these complex use cases, being too limited <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   To solve problems, it may be necessary to go beyond standard RAG for specific settings <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.