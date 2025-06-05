---
title: Evaluating language model performance
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Writer, shared insights into the company's journey and an evaluation of language model performance <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Writer, founded in 2020, views its history as the story of the Transformer, having built numerous decoder-encoder models <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The company currently has a family of about 16 published models, with another 20 in development <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

These models fall into two categories:
*   **General Models**: Such as PX and P3/P4, with P5 coming soon <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Domain-Specific Models**: Including Creative, Financial Services, and Medical models <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## The Shifting Landscape of LLM Accuracy
By early 2024, a significant trend emerged: [[Accuracy and grounding in language models | large language models]] (LLMs) began achieving very high accuracy across general benchmarks <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The average accuracy for good general models rose to between 80% and nearly 90% <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This raised a crucial question within Writer: is it still worthwhile to continue [[Building and scaling large language models | building and scaling large language models]] that are domain-specific if general models can achieve around 90% accuracy <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>? The alternative considered was to fine-tune general models and focus on reasoning or thinking models <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Evaluation Methodology: FAIL
To answer this question, Writer developed an evaluation framework called "FAIL" (Financial LLM Assessment and Insights Leaderboard), designed to create real-world scenarios for [[Testing and evaluation of AI models | evaluating language models]] <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. While the specific data presented was for the financial services domain, similar results were observed for medical models <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

The FAIL evaluation introduced two primary categories of failures:

### 1. Query Failure
This category focuses on issues within the user's query <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. It includes three subcategories:
*   **Misspelling Queries**: User queries containing spelling errors <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Incomplete Queries**: Queries missing keywords or lacking clarity <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Out-of-Domain Queries**: Users attempting to answer specific questions with general knowledge or copy-pasted general answers <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### 2. Context Failure
This category focuses on issues related to the provided context for the LLM <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. It includes three subcategories:
*   **Missing Context**: Asking the LLM questions about context that does not exist in the prompt <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **OCR Errors**: Introducing errors common in Optical Character Recognition (OCR), such as character issues, spacing, or merged words, when converting physical documents to text <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Irrelevant Context**: Providing a completely wrong or irrelevant document when asking a question about a specific document <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

The evaluation data, including the dataset, evaluation set, and leaderboard, is open-sourced and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Evaluation Metrics
The evaluation focused on two key metrics <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>:
1.  Can the model give the **correct answer** <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>?
2.  Can the model give good **follow-up to grounding or context grounding** <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>?

## Results and Findings

The evaluation included a group of models, specifically "chat models" and "thinking models" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### General Model Performance in Query Handling
When models were presented with misspelled, incomplete, or out-of-domain queries, they showed "amazing" performance in providing an answer <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Most general models, including reasoning or thinking models, did not refuse to answer <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. They generally gave an answer, and their scores were close to each other, with reasoning/thinking models even achieving slightly higher scores <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### The Crucial Challenge: Grounding and Context Following
However, the results became "very interesting" when evaluating grounding and context following <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Poor Grounding**: When given wrong context, wrong data, or a completely different grounding, these models, especially the larger "thinking" models, failed to follow the context and still provided an answer <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This leads to significantly higher [[Accuracy and grounding in language models | hallucination]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Performance Gap**: In tasks like text generation or question answering, general models did not perform well regarding grounding <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Smaller Models Outperform**: Counter-intuitively, smaller models often performed *better* in grounding compared to the larger, "overthinking" models <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The larger, more "thinking" models showed the worst results in grounding, with performance being 50-70% worse <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This indicates that these models are "not thinking at that stage," resulting in high [[Accuracy and grounding in language models | hallucination]], particularly in financial use cases <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Persistent Gap**: There remains a significant gap between the model's robustness and its ability to avoid hallucination while getting the answer correct <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Even the best models in the evaluation did not achieve more than 81% in robustness and context grounding <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, implying that nearly 20% of requests could be completely wrong <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## Conclusion: The Continued Need for Domain-Specific Models
Based on the data, the answer to the initial question — whether to continue building domain-specific models — is **yes** <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Despite the growing accuracy of general models, their ability to follow context and provide proper grounding is "way, way, way behind" <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. For reliable utilization today, a "full stack" system is needed, including guard rails and robust grounding mechanisms built around the LLM <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.