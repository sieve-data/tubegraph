---
title: Domainspecific LLMs in finance
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Wasim, co-founder and CTO of Writer, discusses the company's journey and addresses a crucial question regarding the continued relevance of [[comparison_between_general_and_specific_llms | domain-specific models]] in the age of highly accurate general Large Language Models (LLMs) <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

## Writer's Background and Model Philosophy

Writer was founded in 2020, focusing on building transformer models, specifically encoder-decoder models <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. The company currently offers a family of about 16 published models, with another 20 in development <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. These models fall into two main categories:
*   **General Models:** Such as p x p 3 4 (with b 5 coming soon) <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.
*   **[[comparison_between_general_and_specific_llms | Domain-Specific Models]]:** Including models tailored for creative, financial services, and medical sectors <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

By early 2024, a noticeable trend emerged where general LLMs achieved very high accuracy on general benchmarks, often reaching between 80% and 90% <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>. This led to internal discussions at Writer about the necessity of continuing to build and fine-tune [[comparison_between_general_and_specific_llms | domain-specific models]] if general models were already performing so well <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

## Evaluating LLMs in Real-World Scenarios

To answer the question about the ongoing need for [[comparison_between_general_and_specific_llms | domain-specific models]], Writer developed an [[evaluation_of_llms_using_realworld_scenarios | evaluation]] framework called "FAIL" <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. The objective of FAIL is to create real-world scenarios to assess how well models perform <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. While applicable to various domains like medical or customer support, the presentation focused specifically on the financial services benchmark <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

The evaluation categories included:
*   **Query Failure:**
    *   **Misspelling Queries:** Introducing spelling errors in user input <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
    *   **Incomplete Queries:** Missing keywords or unclear phrasing <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
    *   **Out-of-Domain Queries:** Questions from users not expert in the field or general answers applied to specific contexts <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
*   **Context Failure:**
    *   **Missing Context:** Asking questions about context not provided in the prompt <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
    *   **OCR Error:** Simulating errors from converting physical documents to text, such as character issues or merged words <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.
    *   **Irrelevant Context:** Providing a completely wrong document for a question <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

The evaluation metrics focused on two key aspects:
1.  Whether the model provides the **correct answer** <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
2.  The model's ability to **follow context grounding** <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>.

The data, evaluation set, and leaderboard are open-sourced and available on GitHub and Hugging Face <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

## Evaluation Results: General vs. Domain-Specific LLMs

A group of general chat and "thinking" models were selected for the [[evaluation_of_llms_using_realworld_scenarios | evaluation]] <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

### Key Findings:

*   **Answer Robustness:** General and "thinking" models show good behavior in not refusing to answer and can provide an answer even with misspelled, incomplete, or out-of-domain queries <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. Their scores for simply providing an answer are close to each other, with thinking models sometimes scoring slightly higher <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.
*   **Context Grounding Challenges:** This is where the significant difference appears. When given wrong context, wrong data, or completely different grounding, these models fail to follow the provided context <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. This leads to **significantly higher hallucination rates** <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   **Performance in Specific Tasks:** In tasks like text generation or question answering with poor context, general models do not perform well <a class="yt-timestamp" data-t="07:48:00">[07:48:00]</a>.
*   **"Thinking" Models and Hallucination:** The larger, more "thinking" models delivered worse results in grounding, with up to 50-70% worse performance <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. This indicates that these models often don't truly "think" in domain-specific tasks and lead to high hallucination when context is not followed <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.
*   **Smaller Models:** Surprisingly, smaller models sometimes performed better in context grounding than the larger, "overthinking" models <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.

## Conclusion: The Enduring Need for Domain-Specific LLMs

Even the best performing general models in the [[evaluation_of_llms_using_realworld_scenarios | evaluation]] achieved only about 81% in robustness and context grounding <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>. While seemingly good, this translates to roughly 20% of requests being "completely wrong" in a real-world scenario <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

```ad-note
**The answer to the question "Do we still need to build models?" is a definitive YES.** <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>
```

Despite the increasing accuracy of general models, their ability to correctly follow and ground context is still significantly behind what is needed for reliable applications <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. Therefore, there remains a critical need to build and continue developing [[comparison_between_general_and_specific_llms | domain-specific models]], especially for use cases like financial services where accuracy and grounding are paramount <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. Furthermore, a "full stack" approach is required, incorporating robust systems, grounding, and guard rails to ensure reliability <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.