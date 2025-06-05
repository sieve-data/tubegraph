---
title: Comparison between general and specific LLMs
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Rytr, discussed the company's journey and shared insights from their internal evaluations regarding the efficacy of general versus domain-specific Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Rytr's Model Development Journey

Rytr, founded in 2020, began by building decoder-encoder models, evolving into a "family of models" <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Currently, Rytr has about 16 published models with another 20 in development <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. These models fall into two main categories:
*   **General Models**: Such as PXP3, PXP4, and the upcoming PX5 <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Domain-Specific Models**: Including those tailored for creative, [[domainspecific_llms_in_finance | financial services]], and medical applications <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## The Core Question: Are Domain-Specific LLMs Still Necessary?

Around early 2024, a significant trend emerged where general LLMs started achieving very high accuracy on standard benchmarks, often reaching 80-90% <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This raised a crucial question within Rytr: Is it still worthwhile to continue building and investing in [[domainspecific_llms_in_finance | domain-specific models]] if general models are performing so well, or should the focus shift to fine-tuning general models for reasoning and thinking capabilities <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>?

## Evaluation Methodology: The FAIL Benchmark

To answer this question, Rytr developed an [[evaluation_of_llms_using_realworld_scenarios | evaluation of LLMs using real-world scenarios]] called "FAIL" (Financial AI Language Benchmark) <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. While applicable to various domain-specific models (medical, customer support, etc.), the discussion primarily focused on the [[domainspecific_llms_in_finance | financial services]] benchmark <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

The FAIL benchmark introduced two main categories of evaluation scenarios <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>:

1.  **Query Failure** <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
    *   **Misspelling Queries**: Queries with spelling or grammatical errors <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
    *   **Incomplete Queries**: Queries missing keywords or clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   **Out-of-Domain Queries**: Queries where the user is not an expert or pastes general answers to specific questions <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

2.  **Context Failure** <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>:
    *   **Missing Context**: Asking the LLM a question about context that doesn't exist in the prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   **OCR Error**: Introducing character issues, spacing problems, or merged words typical of Optical Character Recognition (OCR) conversion from physical documents to text <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   **Irrelevant Context**: Providing a completely wrong document for a specific question <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The dataset for this evaluation included diverse financial services-specific data, and the white paper, [[data_handling_and_preparing_training_datasets_for_llms | evaluation set]], and leaderboard are openly available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The key evaluation metrics were whether the model provided a correct answer and its adherence to "context grounding" <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## Evaluation Results

Rytr evaluated a group of general chat and "thinking" models against their [[domainspecific_llms_in_finance | domain-specific models]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### General LLMs' Performance

*   **Refusal to Answer**: Thinking models generally tend not to refuse to answer questions, which might sound good but can be problematic <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Query Robustness**: When presented with "query failures" (misspelled, incomplete, or out-of-domain queries), general models, including reasoning/thinking models, performed "amazingly" and could still provide an answer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Most general models achieved similar scores in generating an answer <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Context Grounding Issues**: The significant challenge for general models arose with "context failures" and [[augmented_llm_architectures | context grounding]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   When given incorrect, missing, or irrelevant context, these models failed to properly follow the grounding <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   This led to "way higher hallucination" rates <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   In tasks like text generation or question answering, general models showed poor performance in grounding <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   Surprisingly, "bigger, more thinking" models gave the worst results in grounding, with scores often 50-70% worse <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This implies they are not truly "thinking" in domain-specific tasks, leading to high hallucination <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Domain-Specific LLMs' Performance

*   **Superior Context Grounding**: The evaluation revealed that "smaller models" (domain-specific ones) performed better than larger, general "thinking" models when it came to grounding and adhering to provided context <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Conclusion: The Continued Need for Domain-Specific LLMs

Despite the increasing accuracy of general LLMs on standard benchmarks, the results from the FAIL benchmark strongly indicate that [[domainspecific_llms_in_finance | domain-specific models]] are still necessary <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

Even the best performing general models in the evaluation achieved only about 81% in robustness and context grounding <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. In real-world applications, this means approximately 20% of requests could be completely wrong <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

The key takeaway is that while general model accuracy is improving, their ability to correctly follow and ground answers within a given context is "way, way, way behind" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. Therefore, a full-stack system incorporating robust systems, grounding, and guard rails is crucial for reliable LLM utilization today <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.