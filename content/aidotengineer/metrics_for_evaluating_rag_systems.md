---
title: Metrics for evaluating RAG systems
videoId: 1cQlnfwmIdU
---

From: [[aidotengineer]] <br/> 

Evaluating Retrieval Augmented Generation (RAG) systems is crucial for optimizing their performance. A significant [[challenges_of_rag_evaluation_without_golden_answers | challenge in RAG evaluation]] has traditionally been the requirement for [[challenges_of_rag_evaluation_without_golden_answers | golden answers]] or [[challenges_of_rag_evaluation_without_golden_answers | golden chunks]], which is often non-scalable <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. The [[openrag_eval_project_overview | OpenRAG Eval]] project aims to address this by providing a quick and scalable solution for [[challenges_in_rag_evaluation | RAG evaluation]] that does not rely on these prerequisites <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## OpenRAG Eval Architecture

The [[openrag_eval_project_overview | OpenRAG Eval]] architecture begins with a set of user queries (e.g., 10, 100, or 1000) deemed important for a RAG system <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. A RAG connector, available for platforms like Vectara, LangChain, and LlamaIndex, collects information such as actual chunks and answers generated by the RAG pipeline <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. This output is then fed into the evaluation process, which runs various metrics grouped into "evaluators" <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. These evaluators generate RAG evaluation files containing all necessary information for pipeline assessment <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Key Metrics for Evaluation

[[openrag_eval_project_overview | OpenRAG Eval]] introduces several metrics designed to function effectively without the need for [[challenges_of_rag_evaluation_without_golden_answers | golden answers]]:

### Umbrella (Retrieval Metric)
Umbrella is a retrieval metric that assigns a score between zero and three to each chunk <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:
*   **Zero:** The chunk has no relevance to the query <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Three:** The chunk is dedicated to the query and contains the exact answer <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

Research by the University of Waterloo's Jimmy Lynn lab indicates that this approach correlates well with human judgment, allowing for reliable retrieval evaluation without [[challenges_of_rag_evaluation_without_golden_answers | golden chunks]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### AutoNuggetizer (Generation Metric)
AutoNuggetizer evaluates generation without requiring [[challenges_of_rag_evaluation_without_golden_answers | golden answers]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. It follows three steps:
1.  **Nugget Creation:** Atomic units, called "nuggets," are created from the response <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  **Vital/Okay Rating:** Each nugget is assigned a vital or okay rating, and the top 20 are selected <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  **LLM Judge Analysis:** An LLM judge analyzes the RAG response to determine if each selected nugget is fully or partially supported by the answer <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Citation Faithfulness
This metric assesses whether citations within the RAG response are accurate <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. It measures if the citation or passage is high fidelity, fully supported, partially supported, or has no support in the response <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Hallucination Detection
Utilizing Victara's Hallucination Detection Model (HHM), this metric checks if the entire RAG response aligns with the retrieved content, aiming to identify instances of hallucination <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## User Interface for Analysis
Once evaluation files are generated, they can be uploaded to `open evaluation.ai` <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. This provides a user-friendly interface to visualize and compare retrieval and generation scores across different queries <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Benefits of OpenRAG Eval
[[openrag_eval_project_overview | OpenRAG Eval]] is an open-source package designed to help optimize and tune RAG pipelines <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Its open-source nature promotes transparency in how metrics function and includes connectors for various RAG pipelines like Vectara, LangChain, and LlamaIndex, with provisions for community contributions of additional connectors <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.