---
title: Limitations of current RAG benchmarks
videoId: Ywl4LsvHKzU
---

From: [[aidotengineer]] <br/> 

## Why RAG Evaluation is Broken <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>

RAG (Retrieval Augmented Generation) evaluation faces significant [[challenges_in_rag_evaluation | challenges]] primarily due to the ease with which benchmarks are constructed, often reflecting how humans typically think <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### Characteristics of Flawed Benchmarks
*   **Local Questions and Answers** Most benchmarks consist of local questions that have local answers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. There is an inherent assumption that the answer resides within a specific chunk of data <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Manufactured and Unrealistic Scenarios** The natural way to build such benchmarks involves reading a long document, finding a question whose answer is contained within, and labeling it as the "golden answer" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. While some benchmarks attempt to overcome this with "multiple hope" questions, famously framed by Google, these questions are often unrealistic and do not represent real-world scenarios <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Lack of Holistic System Testing** Most existing benchmarks are either:
    *   **Retrieval-only:** Focusing solely on retrieving the best segments or chunks, assuming the answer is contained within one or several of them <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
    *   **Generation-only (Grounding benchmarks):** Primarily checking if a system can answer a question based on context already provided in the prompt <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    This narrow focus neglects crucial aspects like chunking, parsing, and specific cases where answers are not directly derivable from a single, directed data point <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

### Disconnect from Real-World Data
Current benchmarks do not correlate well with real-world data, which is inherently messier and more diverse <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Each dataset is unique, and benchmarks often fail to generalize effectively <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

<div class="callout callout-caution">
<h4>The Vicious Cycle of Flawed Benchmarking</h4>
When developing RAG systems, a vicious cycle emerges:
1.  Developers build RAG systems optimized for flawed benchmarks <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  High scores are achieved and celebrated <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
3.  Upon real-world deployment or testing with customer data, the systems struggle and underperform <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
4.  New benchmarks are created, re-optimized for, and the cycle continues, often replicating the same underlying problems <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
</div>

## Performance on Complex Questions <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

RAG systems currently struggle with aggregative or comprehensive questions that require more than just retrieving top-k chunks <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Examples of Challenging Questions
*   "Which company has reported the highest quarterly revenue the most times?" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   "In how many fiscal years did Apple exceed 100 billion in annual revenue?" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>
*   Questions requiring an exhaustive list, such as "all Fortune 500 companies," where retrieving a limited number of chunks (e.g., 10) may miss additional relevant entities <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Empirical Evidence of Struggles
A small corpus of 22 documents from FIFA World Cup historical Wikipedia pages was used to test common RAG pipelines <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Questions asked included "Which team has won the FIFA World Cup the most times?" and "In how many FIFA World Cups did Brazil participate?" <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   A common RAG pipeline (e.g., LangChain or LlamaIndex) achieved only 5% correct answers <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   Open responses achieved 11% correct answers <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
These results demonstrate significant failures even for questions with local answers <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Conclusion

Existing benchmarks fail to capture the complexity and nuance required for many real-world RAG use cases <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. RAG is not a one-size-fits-all solution, and optimization must account for individual client needs <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. The standard pipeline of chunking, embedding, retrieving, and reranking is insufficient for many types of questions <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. To address these [[solutions_to_improve_rag_systems | problems]], it may be necessary to go beyond standard RAG approaches for specific settings <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.