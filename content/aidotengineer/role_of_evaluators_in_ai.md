---
title: Role of evaluators in AI
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

[[Evaluation and feedback in AI systems | Evaluation]] in AI applications is crucial for ensuring systems deliver value in the real world rather than remaining mere demonstrations <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Just as traditional software requires unit and integration tests before deployment, AI applications need robust evaluations to assess quality before changes are pushed to production <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

While many teams claim to have automated tests or internal testing processes, there is often uncertainty regarding what constitutes a good [[best_practices_for_ai_evaluation | evaluation framework]] <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Key Components of AI Evaluation

To test the quality of an AI system before production, three key components are necessary <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>:

1.  **Agent**: This is the system being evaluated <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. It could be an end-to-end agent, a small function within an agent, or even a retrieval pipeline <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Agents vary widely, from customer service chatbots to Q&A agents processing legal contracts, each with unique requirements and challenges <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. For example, a financial Q&A system needs to be accurate, compliant with regulations, explain its reasoning, and understand financial accounting standards <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The [[testing_and_evaluation_of_ai_models | evaluation]] must account for these specific aspects <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

2.  **Dataset**: This is the data against which the agent is evaluated <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. An effective dataset must include both the expected inputs (queries and requests the system will receive in production) and the ideal outputs (what good responses should look like) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. It should cover not only common scenarios but also tricky edge cases where problems might arise <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. These examples should ideally be created by domain experts who understand the business context and can define quality requirements <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

3.  **Evaluators**: This component determines how quality is measured <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Types of Evaluators

Historically, different approaches have been used for [[evaluating_ai_agents_and_assistants | evaluating AI agents]]:

*   **Human Evaluators**: Traditionally, subject matter experts review outputs, score them, and provide feedback <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. While effective, this method is often slow and expensive <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Code-based Evaluators**: These are suitable for objective metrics like response time or latency <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. However, metrics like ROUGE-L often fall short for nuanced linguistic evaluation <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Large Language Model (LLM) Evaluators**: These promise to combine the nuance of human reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. They have gained popularity due to their compelling benefits <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>:
    *   **Speed**: Evaluations that previously took 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. For example, 1,000 test cases that might take a full day with human evaluators can be done in 50-60 minutes using an LLM evaluator (assuming sequential execution) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
    *   **Cost Reduction**: Human evaluations via platforms like Mechanical Turk can cost several hundred dollars for 1,000 ratings <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. LLM evaluators can achieve similar results for $3-$120, representing a 10x cost reduction <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   **Consistency**: LLM evaluators show over 80% consistency with human judgments <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. This consistency is comparable to the agreement observed between different human evaluators, as humans do not always agree 100% of the time <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Research papers like NLG-Eval and SPADE have shown strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>, and major model providers are increasingly using LLM evaluators for alignment <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## [[Challenges in AI agent evaluation | Challenges with LLM Evaluators]]

Despite their benefits, LLM evaluators face two major problems <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>:

*   **Criteria Drift**: This occurs when an evaluator's definition of "good" no longer aligns with the user's perception of quality <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. Standard evaluation criteria in popular frameworks (e.g., Fraugash, Promptfoo, Langchain) are designed for generalizability and may not measure what is important for a unique use case <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. For instance, an e-commerce recommendation system's evaluator might focus too much on keyword relevance, missing broader product context, leading to user complaints in production despite good test scores <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Criteria can also drift if the underlying LLM model used for evaluation changes unexpectedly <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Research by Shanker and his team at Berkeley highlights that evaluation criteria must evolve over time to balance true positives and false positives effectively <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Dataset Drift**: This refers to a lack of test coverage in datasets, where carefully crafted test cases fail to represent real-world user queries <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. When real users interact with a system, their inputs are often context-dependent, messy, or combine multiple questions in unexpected ways <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. If the test dataset doesn't reflect these varied usage patterns, evaluation metrics might look good, but the system will underperform in production <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

## [[Improving AI evaluation methods | Improving AI Evaluation Methods]]

To overcome these challenges, evaluations and datasets must be iteratively aligned, similar to how LLM applications themselves are aligned <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. A three-step approach for effective [[importance_of_evaluation_and_metrics_in_ai_systems | evaluation]] involves:

1.  **Align Evaluators with Domain Experts**:
    *   Have domain experts regularly grade outputs and critique the evaluator's results <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.
    *   Use these critiques and few-shot examples in the evaluator's prompt to ground its understanding of quality <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   Continuously massage and iterate on the evaluator prompt itself, rather than relying solely on templated metrics <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
    *   Involve domain experts early in the process to validate evaluator judgments, even by starting with 20 examples in a spreadsheet <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

2.  **Keep Datasets Aligned with Real-World User Queries**:
    *   Log all queries, especially underperforming ones from production, and automatically flow them back into the test suite <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. These real-world failures are invaluable for identifying where the evaluation system falls short <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.
    *   Continuously add these test cases with ground truth labels to the test bank <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.

3.  **Measure and Track Alignment Over Time**:
    *   Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
    *   Track how well the evaluator matches human judgment with every iteration <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This informs whether the evaluator is truly improving or regressing <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
    *   Set up a simple dashboard to track alignment scores (F1 or correlation metrics) to systematically monitor improvements in the evaluator template <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

### Practical Steps for [[building_custom_evaluations_for_better_ai_performance | Customizing Evaluations]]

*   **Customize LLM Evaluator Prompts**: Avoid relying on templated metrics <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. Carefully tailor evaluation criteria, add few-shot examples of critiques from domain experts, and choose appropriate rating scales (binary is highly recommended over Likert) <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>. Ensure the metrics chosen are meaningful to the specific use case, application, and business context <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Iterate LLM Evaluator Prompts**: Prompts are not static; they need to evolve <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Test new versions against an expanding test bank and make them more specific <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. Consider investing in an evaluation console tool, or building one internally, to allow domain experts to iterate on prompts and confirm agreement with evaluator judgments <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **Implement an [[implementation_of_evaluation_platforms_for_ai_agents | Iterative Feedback Loop]]**: AI systems, unlike traditional software, require continuous feedback loops <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>. The goal is not perfection, but continuous improvement based on real-world usage and alignment <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

Ultimately, LLM evaluations are only as good as their alignment with real-world usage <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>. Avoiding static evaluation and building iterative feedback loops into the development process yields significant payoffs in improving evaluation over time <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.