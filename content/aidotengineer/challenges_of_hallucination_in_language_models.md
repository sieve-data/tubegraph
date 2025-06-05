---
title: Challenges of hallucination in language models
videoId: pPvoLjYj_mY
---

From: [[aidotengineer]] <br/> 

Large Language Models (LLMs) can exhibit a phenomenon known as hallucination, where they generate answers that are not grounded in the provided context or factual information. This presents a significant challenge, especially in domain-specific applications where [[Accuracy and grounding in language models | accuracy and grounding]] are critical <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

## Defining Hallucination

Hallucination in the context of LLMs refers to instances where models provide an answer even when given incorrect context, wrong data, or a completely different grounding <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. While models might not refuse to answer questions, their failure to follow the provided (even incorrect) context leads to significantly higher rates of hallucination <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

## Evaluation and Observations

To understand the extent of this issue, a specialized evaluation called "FAIL" was developed to assess model performance in real-world scenarios <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This evaluation includes two main categories of failures:

1.  **Query Failure** <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
    *   **Misspelling queries**: Questions with spelling errors <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   **Incomplete queries**: Missing keywords or unclear information <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   **Out-of-domain queries**: Questions outside the model's expert domain, or general answers applied to specific contexts <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
    *   Models tend to perform "amazingly" on query failures, successfully providing answers even with misspellings, wrong grammar, or out-of-domain queries <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

2.  **Context Failure** <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>:
    *   **Missing context**: Asking questions about context that does not exist in the prompt <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   **OCR errors**: Errors introduced during the conversion of physical documents to text, such as character issues, spacing, or merged words <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
    *   **Irrelevant context**: Providing a completely wrong document for a specific question <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### The Grounding Problem

While general models can achieve high average accuracy, sometimes reaching 80-90% on general benchmarks, the situation changes dramatically when it comes to [[Accuracy and grounding in language models | grounding]] <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. In "FAIL" evaluations, particularly in financial services use cases, models showed very interesting results <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>:

*   Thinking models often do not refuse to answer, even when given wrong context or data <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   This failure to follow the provided context, especially when it's irrelevant or erroneous, leads to significantly higher hallucination <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   When it comes to "grounding" and "context grounding," performance drops sharply <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. For tasks like text generation or question answering, performance is "just not performing well" <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
*   Larger, "thinking" models show the "worst result" in grounding, with performance decreasing by 50-70% compared to their ability to provide an answer <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This means the model often fails to follow the attached context, with answers existing outside the context completely <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

> [!WARNING] The Coherence Trap in Large Language Models
> The data suggests that for domain-specific tasks, these models are "not thinking" at the stage of [[The Coherence Trap in Large Language Models | reasoning]], leading to very high hallucination rates <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

There is a substantial gap between a model's robustness and its ability to avoid hallucination while providing a correct answer <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Even the best models in the evaluation did not achieve more than 81% in robustness and context grounding <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>, implying that nearly 20% of requests could be "completely wrong" <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

## Implications and Future Needs

The persistent challenges with grounding and context following indicate that, despite improvements in general [[Accuracy and grounding in language models | accuracy and grounding]], domain-specific models are still necessary <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. To build reliable systems today, a "full stack" approach is required, incorporating:

*   Robust systems <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>
*   Effective grounding mechanisms <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
*   Guard rails around the system <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>

These components are essential to create a reliable and trustworthy system that can effectively manage the [[Challenges in instruction following by language models | challenges in instruction following by language models]] and mitigate hallucination <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.