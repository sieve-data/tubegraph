---
title: General versus domain specific language models
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Riter, a company founded in 2020, views its history as intertwined with the development of the Transformer model <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. In its early days, Riter focused on building decoder-encoder models <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, and today possesses a family of approximately 16 published models, with another 20 in development <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. These models fall into two primary categories: general models (e.g., PXP3, PXP4, with PXP5 coming soon) and [[domain_specific_language_models_in_finance | domain-specific models]] tailored for areas such as Creative Financial Services, Palo, and Medical <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## The Question of Continued Domain-Specific Development

By early 2024, a significant trend emerged where large language models (LLMs) achieved very high general accuracy, with average performance for good general models reaching 80-90% on benchmarks <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. This development prompted Riter to question the necessity of continuing to build and maintain [[domain_specific_language_models_in_finance | domain-specific models]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The alternative considered was whether to focus on refining general models through fine-tuning, or by developing "reasoning" or "thinking" models <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Evaluating Language Model Performance: The FAIL Framework

To answer this question, Riter developed an evaluation framework called "FAIL," designed to assess models in real-world scenarios <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. The framework focuses specifically on financial services, though similar evaluations are underway for medical applications with similar results <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The evaluation metrics include whether the model provides the correct answer and its adherence to grounding or context <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

The FAIL framework categorizes challenges into two main types:

### 1. Query Failure <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
This category introduces errors in the user's query:
*   **Misspelling Queries**: Queries with spelling errors <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Incomplete Queries**: Queries missing keywords or lacking clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Out-of-Domain Queries**: Queries posed by non-experts or attempts to answer specific questions with general responses <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Context Failure <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
This category introduces issues with the provided context for the query:
*   **Missing Context**: Questions where the necessary context does not exist in the prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **OCR Error**: Context derived from OCR (Optical Character Recognition) with character issues, spacing problems, or merged words <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Irrelevant Context**: Uploading a completely wrong or irrelevant document to answer a question <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The evaluation data, including the evaluation set, leaderboard, and white paper, is open source and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Key Findings

The evaluation involved a selection of general chat and "thinking" models <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

*   **Query Handling**: General models, particularly "thinking" models, showed good behavior in handling query failures such as misspelled, incomplete, or out-of-domain queries, still providing answers <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Context Grounding**: The challenge arose significantly with context failures. When given wrong context, wrong data, or a completely different grounding, general models tended to fail to follow the context and still provided an answer, leading to significantly higher [[accuracy_and_grounding_in_language_models | hallucination]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   In tasks like text generation or question answering, general models did not perform well in grounding <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   Notably, larger, "thinking" models exhibited worse results in context grounding, showing almost 50-70% poorer performance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   This indicates that general models may not truly be "thinking" in [[domain_specific_language_models_in_finance | domain-specific tasks]], but rather exhibiting [[accuracy_and_grounding_in_language_models | Chain of Thought]] leading to high [[accuracy_and_grounding_in_language_models | hallucination]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
    *   In some cases, smaller models performed better in grounding compared to larger, "overthinking" models <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Robustness vs. Grounding**: There remains a substantial gap between a model's robustness (ability to answer a query despite errors) and its ability to correctly ground its answers in the provided context <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Even the best models in the evaluation did not achieve more than 81% in robustness and context grounding combined <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>, implying that nearly 20% of requests could be completely wrong <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Conclusion

Based on the evaluation data, Riter concludes that, with current technology and model implementations, there is still a clear need to build and continue developing [[domain_specific_language_models_in_finance | domain-specific models]] <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. While the general accuracy of LLMs continues to grow, their ability to correctly follow and ground answers within specific contexts remains significantly behind <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

For reliable utilization of LLMs today, a full-stack system is required, encompassing strong grounding, robust guardrails, and overall system reliability <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.