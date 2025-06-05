---
title: Evaluation of LLMs using realworld scenarios
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Writer, details the company's journey and their approach to evaluating Large Language Models (LLMs) in real-world scenarios <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Writer, founded in 2020, began by building decoder-encoder models, evolving into a family of approximately 16 published models, with 20 more in development <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. These models fall into two categories: general models (e.g., PxP3, PxP4, with PxP5 coming soon) and [[domainspecific_llms_in_finance | domain-specific models]] tailored for creative, financial services, and medical fields <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Question of Domain-Specific LLMs

By early 2024, a significant trend emerged: general LLMs were achieving very high accuracy, often between 80% and 90% on general benchmarks <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This raised a critical question for Writer: Is it still worthwhile to continue building [[domainspecific_llms_in_finance | domain-specific models]] if general models are already achieving such high accuracy, or should the focus shift to fine-tuning general models for reasoning or thinking tasks <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>?

To answer this, Writer decided to conduct evaluations using real-world data, specifically focusing on the financial services domain, with similar results observed in the medical field <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## The FAIL Evaluation Framework

Writer developed an evaluation framework called "FAIL" (Financial AI Language) to assess LLMs in realistic scenarios <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. The goal was to determine if newer models could deliver the promised accuracy in real-world contexts <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

The evaluation included two main categories of failure, each with subcategories:

### 1. Query Failure
This category introduces issues within the user's query <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
*   **Misspelling Queries:** Queries containing spelling errors <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **Incomplete Queries:** Queries missing keywords or lacking clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Out-of-Domain Queries:** Questions asked by non-experts or general answers applied to specific fields <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Context Failure
This category focuses on issues related to the provided context <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>:
*   **Missing Context:** Questions asked about context not present in the prompt <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **OCR Errors:** Errors introduced when converting physical documents to text, such as character issues or merged words <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Irrelevant Context:** Supplying a completely wrong document for a specific question <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The evaluation data, including the white paper, dataset, and leaderboard, is open-sourced and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. The key evaluation metrics were:
*   Whether the model gave the correct answer <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   The model's ability to follow the grounding or context <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

## Evaluation Results and Insights

A group of chat and thinking models were selected for evaluation <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The results revealed several interesting behaviors:

*   **Hallucination and Context Following:** Thinking models, while often refusing to answer, tend to fail in following grounding when given wrong context or data, leading to significantly higher hallucination rates <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Query Robustness:** For queries with misspellings, incomplete information, or out-of-domain questions, most models (both [[domainspecific_llms_in_finance | domain-specific]] and general) could provide an answer, with reasoning or thinking models even scoring higher <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **[[comparison_between_general_and_specific_llms | Grounding and Context Adherence]]:** The critical difference emerged in grounding and context adherence <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   Smaller models actually performed better in grounding than larger, "overthinking" models <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   Larger, more "thinking" models showed a 50% to 70% worse performance in grounding, meaning they often did not follow the provided context, even when questions and answers existed outside of it <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   In domain-specific tasks, these models were not truly "thinking" but rather exhibiting a "Chain of Thought" behavior, leading to high hallucination in financial use cases <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **The Robustness-Hallucination Gap:** There is a substantial gap between a model's robustness and its ability to get the correct answer without hallucinating <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Even the best models achieved a maximum of 81% in robustness and context grounding, implying that nearly 20% of requests could be completely wrong in a real-world setting <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## Conclusion

Based on the data from these benchmarks, the answer to the initial question is a clear "yes": **[[domainspecific_llms_in_finance | domain-specific models]] are still necessary** <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. While general model accuracy continues to grow, their ability to follow context and perform proper grounding is significantly behind <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

Therefore, to achieve reliable LLM utilization today, a full-stack approach is essential <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. This includes [[augmented_llm_architectures | Retrieval Augmented Generation (RAG) systems]], robust grounding mechanisms, and effective guardrails built around the entire system <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.