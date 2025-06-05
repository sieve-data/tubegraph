---
title: Data set and evaluation alignment
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

[[lm_evaluation_challenges | LM evaluations]] are a critical component of building effective AI systems, ensuring that applications deliver real-world value beyond being mere "fancy demos" <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. However, many existing [[importance_of_evaluation_frameworks | evaluation]] methods, even those with [[testing_and_evaluation_of_ai_models | robust testing frameworks]], can lead to meaningless evaluations <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. This article explores the challenges and offers solutions for [[improving_ai_evaluation_methods | improving AI evaluation methods]] by ensuring iterative alignment between data sets and evaluators <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

## The Problem with Current AI Evaluations

Despite the common belief that existing [[testing_and_evaluation_of_ai_models | testing frameworks]] are sufficient, working with hundreds of teams has revealed recurring patterns of issues with [[improving_ai_evaluation_methods | evaluation]] that standard frameworks cannot handle <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. Many teams express uncertainty about what constitutes a good [[importance_of_evaluation_frameworks | evaluation framework]] <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

### Fundamentals of Evaluation

An [[importance_of_evaluation_frameworks | evaluation]] fundamentally involves testing the quality of an AI system before it's deployed to production <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>, similar to unit and integration testing in traditional software <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. Three key components are necessary for effective evaluation:

1.  **Agent** <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>: This is the system being evaluated, which could be an end-to-end agent, a small function, or a retrieval pipeline <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. Agents vary widely (e.g., customer service chatbot, Q&A agent for legal contracts) and each has unique requirements. For instance, a document Q&A system may need to be accurate, compliant with regulations, explain its reasoning, and understand domain nuances <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Your [[ai_evaluation_and_risk_scoring | evaluation needs to account]] for all these aspects <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

2.  **Data Set** <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>: This is what the agent is evaluated against and is considered the most important component <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. Many teams struggle here, relying on limited, hand-written test cases that don't cover all use cases <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. A robust data set must include:
    *   Inputs: Queries and requests the system will receive in production <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
    *   Ideal Outputs: What good responses should look like <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
    *   Coverage: Not just "happy paths," but also tricky edge cases where things might go wrong <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.
    *   Domain Expert Input: Examples should be written by experts who understand the business context and can define quality requirements <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

3.  **Evaluators** <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>: This determines how quality is measured <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
    *   **Human Evaluators**: Subject matter experts review and score outputs, providing feedback. This is effective but slow and expensive <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
    *   **Code-based Evaluators**: Good for objective metrics like response time, latency, or even metrics like ROUGE/BLEU (though their effectiveness is debated) <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
    *   **[[lm_evaluation_challenges | LM Evaluators]]**: Promise to combine nuanced reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

These components are dynamic and must evolve over time as the agent improves, data sets need to include more challenging cases, and [[building_custom_evaluations_for_better_ai_performance | evaluation criteria]] become more sophisticated <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

## The Rise of [[lm_evaluation_challenges | LM Evaluators]]

[[lm_evaluation_challenges | LM evaluators]] have gained significant popularity, with teams switching their entire evaluation stack to rely on "LM as a judge" <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>. Their compelling promise includes:
*   **Speed**: Evaluations that previously took 8-10 hours with [[improving_ai_evaluation_methods | human evaluation]] can now be completed in under an hour <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. A thousand test cases could be evaluated in 50-60 minutes, a significant improvement over a full day of human work <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   **Cost**: A traditional human evaluation for 1,000 ratings could cost several hundred dollars via platforms like Mechanical Turk, whereas [[lm_evaluation_challenges | LM evaluators]] range from $3 to $120, representing a 10x cost reduction <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   **[[improving_benchmark_systems_for_accurate_evaluation | Consistency]]**: [[lm_evaluation_challenges | LM evaluators]] show over 80% consistency with human judgments, a level comparable to agreement between different human evaluators <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. Research papers like "nlg eval" and "Spade" demonstrate strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. Major model providers like OpenAI and Anthropic are increasingly using this approach for alignment <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## Major Problems with [[lm_evaluation_challenges | LM Evaluators]]

Despite their benefits, [[misuse_of_data_and_ai_evaluation_metrics | LM evaluators have two very major problems]]:

1.  **[[building_custom_evaluations_for_better_ai_performance | Criteria Drift]]** <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>: This occurs when an evaluator's notion of "good" no longer aligns with the user's <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. Popular frameworks often use generalized [[building_custom_evaluations_for_better_ai_performance | evaluation criteria]] not tailored to unique use cases <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>.
    *   *Example*: An LM-based e-commerce recommendation system performed well in testing using standard criteria like context and generation relevance. However, in production, [[misuse_of_data_and_ai_evaluation_metrics | user complaints]] arose because the evaluator over-indexed on keyword relevance and missed the broader context of product descriptions relevant to user queries, failing to catch real [[misuse_of_data_and_ai_evaluation_metrics | relevance issues]] <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
    *   *Root Cause*: Underlying LM models used for evaluation might change, leading to inconsistent grading <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
    *   *Research*: The "EvalGen" paper by Shanker and team at Berkeley highlighted that [[building_custom_evaluations_for_better_ai_performance | evaluation criteria]] must evolve, balancing true and false positives to maximize F1 score alignment with human judgments <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

2.  **[[misuse_of_data_and_ai_evaluation_metrics | Data Set Drift]]** <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>: This refers to test data sets lacking sufficient coverage of real-world scenarios <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>.
    *   *Problem*: Hand-crafted test cases, while seemingly perfect, often fail to represent the messy, context-dependent, and often complex inputs users provide in production <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. Users might ask broader topics, require real-world data, or combine multiple questions unexpectedly <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>.
    *   *Analogy*: It's like training for a marathon on a treadmill; metrics look good, but the real race includes inclines and varying surfaces that weren't accounted for <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. Your test cases no longer reflect reality <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

## Solutions: Iterative Alignment for Meaningful Evals

To [[improving_ai_evaluation_methods | fix these problems]] and [[building_custom_evaluations_for_better_ai_performance | make evals work for ourselves]], the core insight is that evaluators and data sets must be iteratively aligned, much like aligning an LLM application itself <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

Here's a three-step approach for [[best_practices_for_ai_evaluation | getting your evaluation right]]:

1.  **Align Evaluators with Domain Experts** <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>:
    *   Have domain experts regularly grade outputs and critique evaluator results <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.
    *   Use their critiques and few-shot examples in the evaluator prompt to ground the evaluator with a real-world notion of what's good and bad <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.
    *   Iterate on the underlying evaluator prompt, rather than relying on templated library metrics, until satisfactory agreement is reached <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.

2.  **Keep Data Sets Aligned with Real-World User Queries** <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>:
    *   Log all queries and treat your test bank as a "living, breathing thing" <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
    *   Automatically (or manually) flow underperforming queries from production back into the test suite, as these "real-world failures" are invaluable for improving the test bank <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
    *   Continuously add these test cases and their ground truth labels to the test bank <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.

3.  **Measure and Track Alignment Over Time** <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>:
    *   Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>.
    *   Track how well your evaluator matches human judgment with every iteration to understand if it's truly improving or regressing <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.

### Practical Implementation Steps:

*   **Customize the [[lm_evaluation_challenges | LM evaluator]] Prompt** <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>:
    *   Tailor your [[building_custom_evaluations_for_better_ai_performance | evaluation criteria]] carefully <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>.
    *   Add few-shot examples of critiques from domain experts <a class="yt-timestamp" data-t="15:25:00">[15:25:00]</a>.
    *   Choose between binary or Likert scales for ratings (binary is highly recommended) <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.
    *   Ensure you are measuring something genuinely meaningful to your use case and business context, not just generic out-of-the-box metrics <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.

*   **Involve Domain Experts Early** <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>:
    *   Get them to evaluate the evaluator itself <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
    *   Starting with even 20 examples in a spreadsheet can provide a good sense of alignment between evaluator judgments and expert opinions <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>.

*   **Log and Iterate** <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>:
    *   Continuously add real-world failures from production to your test bank <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>.
    *   Iterate on your [[lm_evaluation_challenges | LM evaluator]] prompts; they are not static <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>. Make them more specific to your use case <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>.
    *   Consider investing in an "eval console" tool (or building one internally) to allow domain experts to directly iterate on and assess evaluator critiques <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>.

*   **Continuous Measurement** <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>:
    *   Set up a simple dashboard to track alignment scores (F1, correlation metrics) over time <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. This systematic tracking informs whether evaluator templates are improving <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>.

## Conclusion

The goal is continuous improvement, not perfection <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>. [[lm_evaluation_challenges | LM evaluations]] are only as good as their alignment with real-world usage <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>. Avoid the trap of static evaluation; LLMs require iterative feedback loops in development processes to ensure meaningful improvement <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>.