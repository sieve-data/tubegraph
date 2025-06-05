---
title: Umbrella and Auto Nuggetizer metrics
videoId: 1cQlnfwmIdU
---

From: [[aidotengineer]] <br/> 

[[open_rag_eval | Open RAG Eval]] is an open-source project designed for quick and scalable evaluation of Retrieval Augmented Generation (RAG) systems, specifically addressing the challenge of not requiring "golden answers" or "golden chunks" for evaluation <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This project is backed by research conducted in collaboration with the University of Waterloo's Jimmy Lynn lab <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The evaluation process starts with a set of queries, which are processed by a RAG connector (e.g., for Vectara, LangChain, LlamaIndex) to collect generated chunks and answers <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. These outputs are then fed into the evaluators, which run various [[metrics_for_evaluating_rag_systems | metrics]] grouped into evaluators to produce RAG evaluation files <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Among these [[metrics_for_evaluating_rag_systems | metrics]], Umbrella and Auto Nuggetizer are key for evaluating RAG systems without golden data <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Umbrella Metric

Umbrella is a retrieval metric designed to evaluate the relevance of retrieved chunks without the need for golden chunks <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### How it Works
*   Umbrella assigns a score to each retrieved chunk, ranging from zero to three <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   A score of **zero** indicates that the chunk or passage has no relevance to the query <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   A score of **three** signifies that the chunk is dedicated to the query and contains the exact answer <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Key Benefit
*   Research from the University of Waterloo lab has demonstrated that this approach correlates well with human judgment, providing reliable results even without golden chunks <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

## Auto Nuggetizer Metric

Auto Nuggetizer is a generation metric used to evaluate the quality of generated answers without requiring golden answers <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### How it Works
The process involves three main steps:
1.  **Nugget Creation**: Atomic units of information, referred to as "nuggets," are created from the response <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
2.  **Nugget Rating and Sorting**: Each nugget is assigned a "vital" or "okay" rating. The top 20 nuggets are then sorted <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
3.  **LLM Judge Analysis**: An LLM judge analyzes the RAG system's response to determine if each selected nugget is either fully supported or partially supported by the answer <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

Further details on this metric are available in the associated research papers <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

These [[metrics_for_evaluating_rag_systems | metrics]], along with others like citation faithfulness and hallucination detection, contribute to [[open_rag_eval | Open RAG Eval]]'s ability to provide a comprehensive evaluation of RAG pipelines <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The project also offers a user interface for visualizing evaluation results at [open evaluation.ai](http://open%20evaluation.ai) <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.