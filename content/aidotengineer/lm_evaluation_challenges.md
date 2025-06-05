---
title: LM evaluation challenges
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

Evaluating Large Language Models (LLMs) is crucial for building AI systems that deliver real-world value beyond fancy demos <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Despite common beliefs that existing evaluation frameworks are robust, recurring patterns suggest that many evaluations might be meaningless <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This article discusses the fundamental components of evaluation, the rise of LM evaluators, and the significant [[challenges_in_ai_agent_evaluation | challenges]] they pose, along with practical solutions for overcoming them.

## Fundamentals of Evaluation

An evaluation in AI applications is analogous to unit and integration testing in traditional software development <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Just as changes aren't pushed to production without tests, AI applications shouldn't be updated without proper evaluations <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

A robust [[importance_of_evaluation_frameworks | evaluation framework]] requires three key components to test quality before deployment:

1.  **Agent** <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>
    This is the AI system or component being evaluated, which could be an end-to-end agent, a small function, or a retrieval pipeline <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. Examples include customer service chatbots, Q&A agents for legal contracts, or document Q&A systems <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. Each agent has unique requirements, such as accuracy, compliance with regulations, explainability, or nuance in specific domains (e.g., financial accounting standards) <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
2.  **Data Set** <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>
    This component serves as the benchmark against which the agent is evaluated <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. A common pitfall is relying on a few handwritten test cases that do not cover all use cases or edge cases <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. An effective [[data_set_and_evaluation_alignment | data set]] must include:
    *   Inputs: Queries and requests that mirror real-world production scenarios <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
    *   Ideal Outputs: Examples of what good and bad responses should look like <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
    *   Edge Cases: Scenarios where the system might fail <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
    These examples should be written by domain experts who understand the business context and can define quality requirements <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
3.  **Evaluators** <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>
    Evaluators are methods used to measure quality <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
    *   **Human Evaluators**: Subject matter experts review outputs and provide scores and feedback <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>. While effective, this method is slow and expensive <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
    *   **Code-based Evaluators**: Suitable for objective metrics like response time or latency <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
    *   **LM Evaluators**: Promise a balance of nuanced reasoning (like humans) and the speed/scalability of automated systems <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

These three components are dynamic and must evolve as the agent improves, the data set expands with more challenging cases, and evaluation criteria become more sophisticated <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

## Rise of LM Evaluators

LM evaluators have gained significant popularity, with many teams switching their entire evaluation stack to rely on "LM as a judge" <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. Their compelling advantages include:

*   **Speed**: Evaluations that took 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. For example, processing a thousand test cases takes about a full day with Mechanical Turk but only 50-60 minutes with an LM evaluator (assuming sequential execution) <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   **Cost**: A traditional human evaluation via Mechanical Turk for a thousand ratings can cost several hundred dollars <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>. LM evaluators, depending on the model chosen, can cost anywhere from $3 to $120 for the same number of ratings, representing a 10x cost reduction <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.
*   **Consistency**: LM evaluators show over 80% consistency with human judgments <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>. This consistency is comparable to the agreement rates observed between different human evaluators, who also do not agree 100% of the time <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. Research papers like NLG Eval and Spade have demonstrated strong correlations between human judgments and LLM scores, and major model providers are increasingly using this approach for alignment <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.

## [[LM Evaluation Challenges]]

Despite their benefits, LM evaluators face two major [[challenges_in_ai_agent_evaluation | challenges]] that can render evaluations meaningless <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>:

> [!CAUTION] The Uncomfortable Truth <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>
> LM evaluators have two significant problems: Criteria Drift and Data Set Drift.

### Criteria Drift

Criteria drift occurs when an LM evaluator's definition of "good" no longer aligns with the user's perception of quality <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>. While popular frameworks (e.g., Ragas, Promptfoo, LangChain) provide built-in evaluation criteria, these are often designed for generalizability and may not measure what is crucial for a specific use case <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

For example, an AI startup built an LM-based recommendation system for e-commerce, and their evaluator checked standard metrics like context relevance and generation relevance <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>. While results looked good in testing, user complaints surfaced in production because the evaluator overemphasized keyword relevance without understanding the broader product description and user query context <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. This led to a complete miss of actual relevance issues <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>. Additionally, inconsistent grading can occur if the underlying LLM model used by the evaluator changes (e.g., an unstable OpenAI version) <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. Research like Shanker and team at Berkeley's "EvalGen" paper highlights that evaluation criteria need to evolve, balancing true positives and false positives to maximize F1 score against human judgments <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### Data Set Drift

[[data_set_and_evaluation_alignment | Data set drift]] refers to a lack of test coverage, where the evaluation data set no longer accurately represents real-world user queries <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. Teams might spend weeks creating perfect test cases with clear queries and obvious answers <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. However, once launched in beta, real users often provide context-dependent, messy inputs that the meticulously crafted test suite fails to account for <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>.

Common usage patterns that lead to data set drift include:
*   Users asking questions broader than anticipated test cases <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>.
*   Queries requiring real-world data like SERP API results <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>.
*   Users combining multiple questions in unforeseen ways <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

In such cases, metrics might still appear favorable because the evaluator is happily scoring on the outdated test cases, but these tests no longer reflect reality <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

## Solutions: Fixing Meaningless Evals

The core insight for effective evaluation is that evaluators and data sets must be iteratively aligned, similar to how an LLM application itself is aligned <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

A three-step approach for effective evaluations:

1.  **Align Your Evaluators with Domain Experts** <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>
    *   Have domain experts regularly grade outputs and critique the evaluator's results <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.
    *   Use their critiques and few-shot examples to refine the evaluator prompt, ensuring it aligns with a real-world understanding of quality <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>. This involves significant iteration and "massaging" of the prompt <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
2.  **Keep Your Data Sets Aligned with Real-World User Queries** <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>
    *   Log production underperforming queries and automatically or manually feed them back into the test suite <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>. Your test bank should be a living, breathing entity <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
3.  **Measure and Track Alignment Over Time** <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>
    *   Use concrete metrics like F1 score (for binary judgments) or correlation coefficients (for Likert scales) to track how well your evaluator matches human judgment with each iteration <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>. This provides critical information on whether the evaluator is improving or regressing <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.

### Practical Steps

Implementing these solutions requires sustained effort, but it's far less work than dealing with the consequences of a meaningless evaluation <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

1.  **Customize the LM Evaluator Prompt**: This is the most important step <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Avoid relying on generic, templated metrics <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>. Carefully tailor evaluation criteria, add few-shot critique examples from domain experts, and decide between binary or Likert scales (binary is highly recommended) <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. Ensure that what's being measured is truly meaningful to your specific use case and business context <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
2.  **Involve Domain Experts Early**: Get experts to evaluate the evaluator itself <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>. Starting with just 20 examples in a spreadsheet can provide a good sense of whether evaluator judgments align with domain experts, helping inform prompt improvements <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.
3.  **Start with Logging Production Underperformance**: Read your logs <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. Every time the system underperforms in production, it's an opportunity to improve the test bank <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>. These real-world failures are invaluable for identifying where the evaluation system falls short and for continuously adding ground truth labels to the test bank <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.
4.  **Iterate Your LM Evaluator Prompts**: Evaluator prompts are not static <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>. Continuously test new versions against your expanding test bank and make them more specific to your use case <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.
5.  **Invest in an Eval Console**: Build or use a tool that allows domain experts to directly iterate on evaluator prompts and assess agreement with critiques and judgments <a class="yt-timestamp" data-t="17:08:00">[17:10:00]</a>.
6.  **Continuous Measurement**: You cannot improve what you do not measure <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>. Set up a dashboard to track alignment scores (F1 score or correlation metrics) over time <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. This systematic tracking informs whether evaluator templates are improving, similar to how an LM application's prompt is tested <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>.

Ultimately, LM evaluations are only as good as their alignment with real-world usage <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>. Avoid static evaluation approaches; instead, build iterative feedback loops into the development process. This continuous improvement yields significant payoffs in effectively improving evaluations over time <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.