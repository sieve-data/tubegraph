---
title: Domain specific language models in finance
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Ater, detailed the company's journey and their focus on developing language models, particularly in the financial sector <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Ater, founded in 2020, began by building decoder-encoder models, eventually expanding to a family of approximately 16 published models with another 20 in development <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. These models fall into two categories: general models (e.g., PxP34, P5) and [[general_versus_domain_specific_language_models | domain-specific models]] tailored for areas such as Financial Services, medical, and legal <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The Challenge for Domain-Specific Models

By early 2024, Ater observed a trend of Large Language Models (LLMs) achieving very high accuracy in general benchmarks, often reaching 80-90% <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. This raised a crucial question internally: is it still necessary to build and maintain [[general_versus_domain_specific_language_models | domain-specific models]] if general models can achieve such high accuracy, perhaps with fine-tuning or a focus on reasoning capabilities <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>?

To answer this question, Ater decided to gather data and conduct evaluations applicable to various domain-specific models, including financial services, medical, and customer support <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The focus of the presented data was on the financial services domain <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## FinFAIL Evaluation Methodology

Ater developed an evaluation framework called "FinFAIL" to test models in real-world scenarios <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This framework introduces specific types of errors and complexities that users might encounter, aiming to see if new models truly deliver on promised accuracy in practical, challenging situations <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

FinFAIL categorized evaluation challenges into two main types:

### 1. Query Failure <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>
This category assesses how models handle imperfect or unusual queries:
*   **Misspelling Queries**: Introducing spelling errors in user questions <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Incomplete Queries**: Queries missing keywords or lacking clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Out-of-Domain Queries**: When a non-expert attempts to ask about a specific field, or a general answer is used for a highly specific topic <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Context Failure <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>
This category examines model performance when the provided context is problematic, highlighting [[challenges_in_data_processing_for_finance_professionals | challenges in data processing for finance professionals]]:
*   **Missing Context**: Asking a question about context that doesn't exist within the prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **OCR Errors**: Introducing errors common when converting physical documents to text, such as character issues, spacing, or merged words <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Irrelevant Context**: Uploading a completely wrong document when asking a question about a specific one, to see if the LLM still attempts to answer or recognizes the irrelevance <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

Ater ensures diversity in the financial services data used for evaluation, and the FinFAIL white paper, dataset, and leaderboard are open-source and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The key evaluation metrics are whether the model provides a correct answer and its adherence to the provided context (grounding) <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Evaluation Results: The Importance of Grounding

Selected chat and "thinking" models were evaluated <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Initial observations showed that thinking models often refuse to answer, which seems good in theory <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. However, when provided with incorrect context or grounding, these models frequently fail to adhere to it, leading to higher hallucination rates <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

While many general models and [[general_versus_domain_specific_language_models | domain-specific models]] could provide *an answer* even with query issues (misspelling, incomplete, out-of-domain), scoring high on answer correctness <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, the performance drastically declined when it came to context grounding <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

Notably, larger "thinking" models yielded worse results in grounding tasks, with accuracy dropping significantly (e.g., 50-70% worse) <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This indicates that these models often don't follow the attached context and provide answers existing outside of it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. For [[general_versus_domain_specific_language_models | domain-specific tasks]], smaller models actually performed better in context grounding than these overthinking models <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. This finding suggests that what appears to be "thinking" might simply be a "Chain of Thought" process that increases hallucination in domain-specific contexts <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

There remains a significant gap between model robustness and their ability to provide correct, well-grounded answers <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Even the best models achieved only about 81% in robustness and context grounding, meaning nearly 20% of requests could be completely wrong <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

## Conclusion: The Continued Need for Domain-Specific Models

Based on current data and technology, [[general_versus_domain_specific_language_models | domain-specific models]] are still essential <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. While general model accuracy continues to improve, their ability to follow and correctly utilize context (grounding) remains significantly behind <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. For reliable utilization today, a full-stack system is necessary, encompassing robust systems, grounding mechanisms, and guardrails <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.