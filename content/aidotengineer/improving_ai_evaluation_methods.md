---
title: Improving AI evaluation methods
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

Effective [[testing_and_evaluation_of_ai_models | evaluation]] of AI models is crucial for building systems that deliver real-world value, not just fancy demos <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Many AI evaluations can be meaningless if not designed and maintained correctly <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

## Fundamentals of AI Evaluation

Just as traditional software requires unit and integration tests before pushing changes to production, AI applications need robust [[testing_and_evaluation_of_ai_models | evaluations]] before deployment <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. A robust [[evaluation_and_feedback_in_ai_systems | evaluation]] framework requires three key components <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>:

1.  **Agent**: This is whatever is being evaluated, which could be an end-to-end agent, a small function, or a retrieval pipeline <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Different agents (e.g., customer service chatbot, legal Q&A system) have unique requirements that evaluations must account for, such as accuracy, compliance, explainability, or nuance <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
2.  **Data Set**: This is the benchmark against which the agent is evaluated <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. A comprehensive data set must include both inputs (queries the system will receive in production) and ideal outputs (what good responses should look like) <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>. Critically, it must cover not only "happy paths" but also tricky edge cases where things might go wrong <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. These examples should ideally be written by domain experts who understand the business context and quality requirements <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.
3.  **Evaluators**: This refers to how quality is measured <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
    *   **Human Evaluators**: Traditionally, subject matter experts review outputs, score them, and provide feedback. While effective, this method is slow and expensive <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
    *   **Code-based Evaluators**: These are good for objective metrics like response time or latency <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
    *   **LLM Evaluators**: These promise to combine the nuance of human reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

These three components are dynamic and must evolve as the AI agent improves, evaluation criteria become more sophisticated, and new challenges arise <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

## The Rise and Challenges of LLM Evaluators

LLM evaluators have become popular due to their compelling advantages <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>:

*   **Speed**: Evaluations that once took 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
*   **Cost**: Costs can be reduced by as much as 10x compared to traditional human evaluations <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   **Consistency**: LLM evaluators can achieve over 80% consistency with human judgments, comparable to inter-human agreement <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. Research papers and major model providers are increasingly backing this approach <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.

However, [[challenges_in_ai_agent_evaluation | LLM evaluators face significant problems]] <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>:

### [[criteria_drift_in_ai_evaluation | Criteria Drift]]

[[criteria_drift_in_ai_evaluation | Criteria drift]] occurs when an evaluator's notion of "good" no longer aligns with the user's <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>. Standard evaluation frameworks often use generalizable criteria, which might not capture the unique requirements of a specific use case <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>. For example, an e-commerce recommendation system's evaluator might over-index on keyword relevance, missing the broader context of user intent, leading to user complaints despite seemingly good test results <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. [[criteria_drift_in_ai_evaluation | Evaluation criteria need to evolve over time]] to balance true positives and false positives, maximizing alignment with human judgments <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### [[data_set_drift_in_ai_evaluation | Data Set Drift]]

[[data_set_drift_in_ai_evaluation | Data set drift]] refers to a lack of test coverage, where carefully crafted test cases fail to represent real-world user inputs <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. Real users often provide context-dependent, messy, or complex queries that static, hand-written test suites cannot anticipate <a class="yt-timestamp" data-t="11:38:00">[11:38:00]</a>. This means metrics might look good on paper, but the system underperforms in production because the test cases don't reflect reality <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.

## Improving AI Evaluation Methods: Iterative Alignment

The fundamental insight for effective evaluation is that evaluators and data sets must be iteratively aligned, similar to how an LLM application itself is aligned <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>. This constitutes [[continuous_improvement_in_ai_systems | continuous improvement]] for AI systems.

Here's a three-step approach for [[best_practices_for_ai_evaluation | best practices for AI evaluation]]:

1.  **Align Your Evaluators with Domain Experts**:
    *   Have domain experts regularly grade outputs, not just at setup, but continuously <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>.
    *   Encourage experts to critique evaluator results themselves, identifying what the evaluator is missing or overemphasizing <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.
    *   Use these critiques and few-shot examples in your evaluator prompt to ground it with a real-world notion of what is good and bad <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.
    *   Iterate on the evaluator prompt, customizing it beyond templated metrics to measure what is truly meaningful to your application and business context <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
    *   Start with a small set of examples (e.g., 20) in spreadsheets to quickly gauge alignment between evaluator judgments and domain expert expectations <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.

2.  **Keep Your Data Sets Aligned with Real-World User Queries**:
    *   Treat your test bank as a living, breathing entity <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>.
    *   Log instances where the system underperforms in production and automatically (or manually) flow these real-world failures back into your test suite <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.
    *   Continuously add these test cases and their corresponding ground truth labels to improve your test bank over time <a class="yt-timestamp" data-t="16:43:00">[16:43:00]</a>.

3.  **Measure and Track Alignment Over Time**:
    *   Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.
    *   Track how well your evaluator matches human judgment with every iteration <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>. This provides critical feedback on whether your evaluator is improving or regressing <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.
    *   Set up a simple dashboard to systematically track these alignment scores <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.

Ultimately, [[building_custom_evaluations_for_better_ai_performance | AI evaluations are only as good as their alignment with real-world usage]] <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>. It's essential to avoid static evaluation and instead build iterative feedback loops into the development process <a class="yt-timestamp" data-t="18:13:00">[18:13:00]</a>. The [[importance_of_evaluation_and_metrics_in_ai_systems | goal is continuous improvement]], not perfection <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>.