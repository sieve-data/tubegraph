---
title: Challenges and limitations of traditional evaluation methods
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

Traditional evaluation approaches, often rooted in unit and integration testing frameworks from conventional software development, frequently fall short when applied to artificial intelligence (AI) applications <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While many teams believe their existing testing frameworks are robust, a deeper examination often reveals uncertainty about what constitutes an [[effective_evaluation_frameworks | effective evaluation framework]] for AI <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Fundamentals of Evaluation

To assess quality before deployment, an evaluation requires three key components <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:

1.  **Agent**: Whatever is being evaluated, ranging from an end-to-end AI agent to a small function or retrieval pipeline <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Each agent, such as a customer service chatbot or a Q&A agent for legal contracts, has unique requirements that traditional evaluations may not capture <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
2.  **Dataset**: The benchmarks against which the agent is evaluated <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
3.  **Evaluators**: The methods used to measure quality <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Limitations of Traditional Approaches

### Inadequate Datasets and Test Coverage
A significant stumbling block for many teams is the dataset <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Traditional approaches often rely on:
*   **Handwritten Test Cases**: Developers manually create a few test cases, assuming they cover all use cases, which is often not true <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. These static test cases tend to focus only on "happy paths" and miss critical edge cases where issues might arise in production <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Lack of Domain Expertise**: Ideal test cases, including both inputs and desired outputs, should be created by domain experts who understand the business context and quality requirements <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Without this, the dataset may not accurately define what "good" responses look like.
*   [[challenges_in_current_ai_benchmarking_practices | **Data Set Drift**]]: Even if an initial dataset is well-crafted, it can quickly become unrepresentative of real-world usage patterns <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. Production users often provide context-dependent, messy inputs or combine multiple questions in unexpected ways <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This means that while internal metrics might still look good, they no longer reflect actual performance, similar to training for a marathon on a treadmill without accounting for real-world conditions <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Inefficient Evaluators
Historically, evaluators typically included:
*   **Human Evaluators**: Subject matter experts review outputs, score them, and provide feedback <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. While this method can work, it is notably **slow and expensive** <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. For example, evaluating 1,000 test cases with human evaluators could take a full day of work <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Rule-Based Evaluators**: These are effective for objective metrics like response time or latency <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. However, they struggle with subjective or nuanced aspects of AI outputs, such as relevance or adherence to specific standards like ROUGE-L, which may not always align with true quality <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Generalizability Over Specificity
Many established evaluation frameworks and libraries (e.g., Ragas, Promptfoo, LangChain) provide built-in evaluation criteria <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. While convenient, these are designed for **generalizability** and do not necessarily measure what is crucial for a unique use case <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. This can lead to [[evaluations_versus_traditional_metrics_in_ai | "criteria drift"]], where the evaluator's notion of quality diverges from the user's <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. For instance, an e-commerce recommendation system's evaluator might over-index on keyword relevance, missing the broader context of user intent, leading to user complaints despite positive internal test results <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Consequences of Static Evaluation
Treating evaluations as static tests, similar to traditional software testing, is a significant trap in AI <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. AI systems, particularly those using Large Language Models (LLMs), require dynamic and [[iterative_improvement_of_evaluation_processes | iterative evaluation processes]] <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. A static approach leads to:
*   **Meaningless Evaluations**: Tests may not accurately reflect real-world performance or user satisfaction <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Failure to Catch Bugs**: Critical issues only emerge in production, causing user complaints <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Hindered AI System Development**: Without proper evaluations, it's difficult to build AI systems that truly deliver value in the real world beyond being just "fancy demos" <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

The emergence of LM evaluators aims to address these limitations by offering faster, cheaper, and more consistent evaluation <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. However, they also introduce their own [[challenges_in_ai_agent_evaluation | challenges]] that must be addressed through continuous alignment with real-world usage and domain expert input <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.