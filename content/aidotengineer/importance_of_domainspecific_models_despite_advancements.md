---
title: Importance of domainspecific models despite advancements
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Writer, details the company's journey and shares insights into the continued necessity of domain-specific models in the rapidly evolving landscape of AI <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## A History of Model Development at Writer
Writer, founded in 2020, views its story as intertwined with the evolution of the Transformer model <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Initially building encoder-decoder models, the company has since developed a family of approximately 16 published models, with another 20 in development <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. These models fall into two categories:
*   **General Models**: Such as PX and P3/P4 (with P5 coming soon) <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Domain-Specific Models**: Covering areas like Creative, Financial Services, and Medical <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## The Shifting Landscape of LLM Accuracy
By early 2024, a significant trend emerged: Large Language Models (LLMs) were achieving very high accuracy on general benchmarks, often reaching 80-90% <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This rise in performance sparked an internal question at Writer <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>: Is it still worthwhile to continue building [[finetuning_ai_models_for_specific_use_cases | domain-specific models]] if general models are nearing 90% accuracy <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>? The company considered whether to instead focus on [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] general models or developing [[role_of_reasoning_models_in_application_development | reasoning or thinking models]] <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## The Need for Data: Introducing the FAIL Benchmark
To answer this critical question, Writer developed a benchmark called "FAIL" <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The objective was to create real-world scenarios to evaluate models and assess their promised accuracy in domain-specific contexts <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The benchmark, which is open-source and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>, introduced two main categories of evaluation failures:

### 1. Query Failure
This category assesses how models handle imperfect user queries <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
*   **Misspelling Queries**: User inputs with spelling errors <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Incomplete Queries**: Queries missing keywords or clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Out-of-Domain Queries**: Attempts to answer specific domain questions using general knowledge <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Context Failure
This category focuses on the model's ability to handle issues with the provided context <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>:
*   **Missing Context**: Asking questions about information not present in the prompt <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **OCR Errors**: Introducing character issues, spacing problems, or merged words common in optical character recognition conversions <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Irrelevant Context**: Providing a completely wrong document for a specific question <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The evaluation metrics primarily focused on two aspects: whether the model gave the correct answer and its adherence to "context grounding" <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Evaluation Results: The Grounding Challenge
The evaluation, specifically focusing on financial services, revealed "very interesting results" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Hallucination and General Model Behavior
*   **Refusal to Answer**: [[role_of_reasoning_models_in_application_development | Thinking models]] generally did not refuse to answer, which might sound good but proved problematic <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Failure in Grounding**: When given incorrect or irrelevant context, these models often "fail to follow this part" and still provide an answer, leading to "way higher [[ai_model_considerations | hallucination]]" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Answer Accuracy vs. Grounding**: While most domain-specific and general models produced answers that were "close to each other" in terms of simple answer correctness, and [[role_of_reasoning_models_in_application_development | reasoning models]] even scored slightly higher <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, the "grounding and context grounding" performance showed a stark difference <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### The Problem of Context Grounding
*   **Poor Performance in Grounding**: In tasks like text generation or question answering, general models did "not performing well" in context grounding <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   **Significant Drop**: While models performed "amazingly" when handling misspelled, incomplete, or out-of-domain queries, their performance plummeted in grounding <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Worse Results for Bigger Models**: [[role_of_reasoning_models_in_application_development | Bigger, more thinking models]] yielded "the worst result" in grounding, with a 50-70% worse performance <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This means the model "is just not following" attached context or answers from completely irrelevant context <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Smaller Models Outperform**: Surprisingly, "smaller model actually performing better than all this model overthinking at that side" <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

These findings suggest that in domain-specific tasks, current models are "not thinking at that stage," leading to "really high" [[ai_model_considerations | hallucination]] <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Even the best models achieved only about 81% accuracy when combining robustness and context grounding, meaning nearly 20% of requests could be "completely wrong" <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Conclusion: The Enduring Need for Domain-Specific Models
Based on the data from the FAIL benchmark, the answer to the initial question is a definitive "yes" <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Writer concludes that it is still necessary to build and continue developing [[finetuning_ai_models_for_specific_use_cases | domain-specific models]] <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. While general model accuracy is improving, their ability to correctly handle "grounding" and "context following" remains "way, way, way behind" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

For reliable deployment today, a full-stack approach is required, incorporating "robust system," "grounding," and "guard rails" around the AI system <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.