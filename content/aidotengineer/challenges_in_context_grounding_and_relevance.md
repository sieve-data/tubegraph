---
title: Challenges in context grounding and relevance
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

A significant [[challenges_in_ai_development | challenge in AI development]], particularly with large language models (LLMs), revolves around their ability to correctly understand and adhere to provided context, even when general accuracy metrics appear high <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. This concern led to an evaluation questioning whether continued development of domain-specific models is necessary if general models achieve high accuracy <a class="yt-timestamp" data-t="01:53:02">[01:53:02]</a>.

## The FAIL Benchmark for Evaluation
To address this, a real-world scenario evaluation set called "FAIL" was created to test model performance in diverse, challenging conditions <a class="yt-timestamp" data-t="03:12:35">[03:12:35]</a>. This benchmark includes two main categories of failures: Query Failure and Context Failure <a class="yt-timestamp" data-t="03:34:06">[03:34:06]</a>.

### Context Failure Categories
The "context failure" category specifically introduces issues related to the provided context, which is crucial for evaluating [[importance_of_context_in_ai_agent_performance | context grounding]] <a class="yt-timestamp" data-t="04:23:07">[04:23:07]</a>. This category includes three subcategories:
*   **Missing Context** The LLM is asked questions about context that does not exist in the prompt <a class="yt-timestamp" data-t="04:33:48">[04:33:48]</a>.
*   **OCR Errors** Introduction of character issues, incorrect spacing, or merged words, mimicking errors from converting physical documents to text <a class="yt-timestamp" data-t="04:44:27">[04:44:27]</a>.
*   **Irrelevant Context** A completely wrong document is uploaded, and the evaluation assesses if the LLM still attempts to answer or recognizes the irrelevance <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

The evaluation's key metrics focused on whether the model gave a correct answer and whether it followed the grounding or context correctly <a class="yt-timestamp" data-t="05:52:16">[05:52:16]</a>.

## Observed Challenges in Context Grounding
When evaluating general and [[reasoning_models_and_their_unique_prompting_requirements | thinking models]], interesting results emerged regarding [[challenges_in_ai_agent_development | context grounding]] <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>.
*   **Failure to Follow Context** Many "thinking models" were observed not to refuse to answer, even when given wrong or irrelevant context or data <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. This leads to a significantly higher rate of hallucination <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **High Hallucination Rates** While models generally provide an answer, particularly [[reasoning_models_and_their_unique_prompting_requirements | reasoning or thinking models]], their performance in [[importance_of_context_in_ai_agent_performance | context grounding]] for tasks like text generation or question answering is not good <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. This suggests that in domain-specific tasks, these models might not be "thinking" but rather producing high hallucination rates <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.
*   **Smaller Models Outperform Larger Ones in Grounding** Surprisingly, smaller models showed better performance in [[importance_of_context_in_ai_agent_performance | context grounding]] compared to larger, more "thinking" models, which gave worse results <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. The larger models often did not follow the attached context, with answers existing outside the provided information <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Robustness vs. Grounding Gap** There is a significant gap between a model's robustness (ability to handle misspelled queries or incomplete input) and its ability to correctly ground answers in the provided context <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. Even the best models achieved only around 81% in [[importance_of_context_in_ai_agent_performance | context grounding]] and robustness, meaning approximately 20% of requests could be completely wrong <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.

## Conclusion
The data suggests that despite increasing general accuracy of LLMs, [[challenges_with_instruction_following_in_ai | challenges with instruction following in AI]] remain, particularly concerning proper context grounding and relevance <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>. Therefore, the continued development and implementation of domain-specific models are still essential <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. To create reliable AI applications, a "full stack" approach is needed, incorporating robust systems, grounding mechanisms, and guardrails built around the entire system <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.