---
title: Role of human and automated evaluators in AI assessment
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

The success of AI systems in the real world hinges on effective [[importance_of_evaluations_in_ai_projects | evaluations]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. While traditional testing frameworks exist, unique patterns emerge with AI that necessitate a different approach to [[evaluating_ai_system_performance | evaluation]] <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Getting [[evaluations_versus_traditional_metrics_in_ai | evaluations]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> right is not just about catching bugs or measuring accuracy; it's about building AI systems that truly deliver value <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## What is an AI Evaluation?

An [[evaluating_ai_system_performance | evaluation]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a> in AI, similar to unit and integration testing in traditional software, is crucial before pushing changes to an AI application into production <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Many teams express uncertainty about what constitutes a robust [[steps_to_create_effective_evaluations_for_ai_applications | evaluation framework]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

To test quality before production, three key components are needed:

1.  **Agent** <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>: This is whatever is being [[evaluating_ai_agents_and_assistance | evaluated]] <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>, ranging from an end-to-end agent to a small function or retrieval pipeline <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Agents can be customer service chatbots, Q&A agents for legal contracts, or other complex systems <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Each agent has unique requirements, such as accuracy, compliance with regulations, explainability, or nuance around specific standards <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. The [[evaluating_ai_system_performance | evaluation]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> must account for all these aspects <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
2.  **Dataset** <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>: Considered the most important component, this is what the agent is [[evaluating_ai_system_performance | evaluated]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> against <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. A robust dataset must include both inputs (queries/requests the system will receive in production) and ideal outputs (what good responses should look like) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It should cover not only the "happy path" but also tricky edge cases where things might go wrong <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. These examples should ideally be written by domain experts who understand the business context and can define quality requirements <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
3.  **Evaluators** <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>: This defines how quality is measured <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

These components are dynamic and must evolve as the agent improves, the dataset needs to include more challenges, and evaluation criteria become more sophisticated <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Types of Evaluators

### Traditional Human Evaluators
Traditionally, human evaluators, often subject matter experts, review outputs, score them, and provide feedback <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Pros**: Provides nuanced judgment and understanding of complex contexts <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Cons**: Very slow and expensive <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. For example, processing a thousand test cases with human evaluators like Mechanical Turk could take a full day of work and hundreds of dollars <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Goal-Based Evaluators
These are great for objective metrics like response time or latency <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### LLM Evaluators (Automated)
Large Language Model (LLM) evaluators have gained popularity due to their promise of combining nuanced reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. They act as "LM as a judge" <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

#### Benefits of LLM Evaluators
*   **Speed**: [[Evaluating AI systems at scale | Evaluations]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a> that used to take 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. A thousand test cases could be processed in 50-60 minutes <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Cost Reduction**: Costs can drop from several hundred dollars for human evaluation to $3-$120 for LLM evaluators, representing a 10x reduction <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Consistency**: LLM evaluators show over 80% consistency with human judgments <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This is comparable to the agreement levels seen between different human evaluators, who also don't agree 100% of the time <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Research papers like NLG Eval and SPADE show strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

#### Challenges with LLM Evaluators
Despite their benefits, LLM evaluators present two major problems:

1.  **Criteria Drift** <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>: This occurs when an evaluator's notion of what is "good" no longer aligns with the user's notion of "good" <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Popular frameworks like Ragas, Prompts, or LangChain often rely on built-in evaluation criteria designed for generalizability <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   **Example**: An AI startup building an LLM-based recommendation system for e-commerce websites found that while their evaluator checked standard boxes like context and generation relevance, it missed crucial user requirements for relevance in production <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. The evaluator indexed too heavily on keyword relevance without considering the broader context of product descriptions or user queries <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   **Underlying Model Changes**: Even if an LLM evaluator works fine on a single test case, its consistency can drop if the underlying LLM model changes (e.g., using an unstable version of OpenAI's models) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
    *   **Research**: The "EvalGen" paper by Shanker and team at Berkeley highlighted that evaluation criteria need to evolve over time, balancing true positives with false positives to maximize F1 score alignment against human judgments <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

2.  **Dataset Drift** <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>: This problem refers to a lack of test coverage in datasets <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Hand-written test cases, perfect in theory, often fail to represent the messy, context-dependent inputs from real-world users in production <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
    *   **Real-world Usage**: Users constantly ask broader topics, require real-world data (e.g., from search APIs), or combine multiple questions in unanticipated ways <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
    *   **False Confidence**: Metrics might still look good because the evaluator is scoring happily on the outdated test cases, but these tests no longer represent reality <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

## Fixing Evaluation Problems: Iterative Alignment

The key insight to fixing these problems is that evaluators and datasets need to be iteratively aligned, similar to how an LLM application itself is aligned <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

Here's a three-step approach for [[strategies_for_ai_evaluation_and_troubleshooting | effective evaluation]] <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>:

1.  **Align your Evaluators with Domain Experts** <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>:
    *   Have domain experts regularly grade outputs and critique the evaluator's results <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
    *   Use their critiques and few-shot examples in the evaluator prompt to ground it in a real-world notion of what is good or bad <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
    *   Continuously massage and iterate on the evaluator prompt, not just relying on templated library metrics <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

2.  **Keep your Data Sets Aligned with Real-World User Queries** <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>:
    *   Log your test bank, treating it as a living, breathing entity <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
    *   Automatically (or manually) flow underperforming queries from production back into the test suite <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

3.  **Measure and Track Alignment Over Time** <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>:
    *   Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
    *   Track how well your evaluator matches human judgment with every iteration to determine if it's improving or regressing <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

## Practical Steps for Effective Evaluation

*   **Customize the LLM Evaluator Prompt** <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>: Instead of relying on templated metrics, carefully tailor your [[evaluations_and_finetuning_in_ai_development | evaluation criteria]] <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. Add few-shot examples of critiques provided by domain experts <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. Decide between binary scales (highly recommended) or Likert scales for ratings <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>. Ensure you're measuring something meaningful to your specific use case and business context <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Involve Domain Experts Early** <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>: Get them to [[evaluating_ai_system_performance | evaluate the evaluator]] <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Starting with 20 examples in a spreadsheet can provide a good sense of whether evaluator judgments align with domain experts, guiding future changes to the evaluator prompt <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>.
*   **Start with Logging** <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>: Every time your system underperforms in production, it's an opportunity to improve your test bank <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. These real-world failures are "golden" because they highlight exactly where your [[evaluating_ai_system_performance | evaluation system]] <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a> is falling short <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Continuously add these test cases and ground truth labels to your test bank <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
*   **Iterate LLM Evaluator Prompts** <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>: Evaluator prompts are not static; they need to evolve <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>. Test new versions against your expanding test bank and make them more specific to your use case <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **Invest in an Eval Console** <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>: Whether built internally or using a tool, an eval console allows domain experts to iterate on the evaluator prompt and assess agreement with its critiques and judgments <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **Systematic Measurement** <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>: Track alignment scores (F1 or correlation metrics) over time using a simple dashboard <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>. This systematic tracking informs whether your evaluator template is improving or not <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

Ultimately, your LM [[evaluating_ai_system_performance | evaluations]] <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a> are only as good as their alignment with real-world usage <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. Avoid static [[evaluating_ai_system_performance | evaluation]] <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a> and build iterative feedback loops into your development process <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.