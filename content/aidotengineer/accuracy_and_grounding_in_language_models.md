---
title: Accuracy and grounding in language models
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

The rise of large language models (LLMs) achieving high accuracy on general benchmarks has prompted questions about the continued necessity of building [[general_versus_domain_specific_language_models | domain-specific models]] <a class="yt-timestamp" data-t="01:53:14">[01:53:14]</a>. To answer this, a specialized evaluation framework called `FAIL` was developed <a class="yt-timestamp" data-t="03:15:17">[03:15:17]</a>, designed to test real-world scenarios in domain-specific contexts, initially focusing on financial services <a class="yt-timestamp" data-t="02:29:43">[02:29:43]</a>.

## Evaluation Methodology: The `FAIL` Benchmark

The `FAIL` evaluation aims to assess how well models perform under challenging, real-world conditions, particularly in domain-specific tasks <a class="yt-timestamp" data-t="03:19:19">[03:19:19]</a>. The dataset and evaluation set are open-source and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="05:37:37">[05:37:37]</a>. The key evaluation matrix focuses on two aspects:
*   Can the model provide the correct answer? <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>
*   Can the model properly follow grounding or context grounding? <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>

The `FAIL` benchmark introduces two main categories of challenges:

### 1. Query Failure <a class="yt-timestamp" data-t="03:40:40">[03:40:40]</a>
This category evaluates a model's robustness to imperfections in the user's query:
*   **Misspelling Queries:** Queries with spelling errors <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.
*   **Incomplete Queries:** Queries missing keywords or unclear elements <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
*   **Out-of-Domain Queries:** Queries that are not specific to the model's trained domain <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

### 2. Context Failure <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>
This category tests a model's ability to handle problematic or irrelevant context provided to it:
*   **Missing Context:** Questions about context that does not exist in the prompt <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **OCR Error:** Context containing errors introduced during optical character recognition (OCR), such as character issues, incorrect spacing, or merged words <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.
*   **Irrelevant Context:** Providing a completely wrong document or context for the question asked <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## Key Findings: Accuracy vs. Grounding

While [[evaluating_language_model_performance | general language models]] can achieve an average accuracy of 80-90% on standard benchmarks <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>, the `FAIL` evaluation reveals a significant discrepancy between models' ability to provide an answer and their ability to ground that answer in the provided context <a class="yt-timestamp" data-t="07:20:00">[07:20:00]</a>.

### Performance on Query Failures
Models, including smaller ones, perform "amazingly" well when handling query failures such as misspelled, incomplete, or out-of-domain queries <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>. They can still provide an answer even with wrong grammar or misspellings <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>. "Reasoning" or "thinking" models tend to refuse to answer less often, which might seem positive <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

### Performance on Context Failures (Grounding)
When it comes to grounding, models — especially larger "thinking" models — show a significant drop in performance <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
*   Even when given wrong context, wrong data, or a completely different grounding, these models often fail to follow the context and still provide an answer <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.
*   This leads to significantly higher rates of [[challenges_of_hallucination_in_language_models | hallucination]] <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   In tasks like text generation or question answering, performance related to context grounding is not good <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
*   Surprisingly, smaller models often perform better in grounding tasks than larger, "overthinking" models, suggesting that current "thinking" capabilities might be more akin to "Chain of Thought" rather than true understanding in domain-specific tasks <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

### The Robustness-Hallucination Gap
There is a significant gap between a model's robustness (its ability to handle imperfect queries) and its tendency to hallucinate or provide an incorrect answer due to poor grounding <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. Even the best-performing models in this evaluation only achieved around 81% accuracy in combined robustness and context grounding <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. This means that for every 100 requests, approximately 20 could still be completely wrong <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

## Conclusion

Despite the growing accuracy of [[building_and_scaling_large_language_models | general LLMs]], the evaluation data strongly suggests that there is still a need to build and continue developing [[general_versus_domain_specific_language_models | domain-specific models]] <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. The primary reason is that while general accuracy improves, the ability to correctly follow and ground answers in provided context remains significantly behind <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. This highlights the importance of robust systems with strong grounding mechanisms and guardrails for reliable real-world utilization <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.