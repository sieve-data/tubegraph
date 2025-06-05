---
title: Continuous improvement in AI systems
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

Traditional software development relies on static tests, but [[Evaluation and feedback in AI systems | AI evaluations]] must be dynamic and continuously aligned with real-world usage to build effective [[Best Practices for Building AI Systems | AI systems]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. This requires [[Incremental development and verification in AI | iterative alignment]] of evaluators and datasets, much like aligning an LLM application itself <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Fundamentals of AI Evaluation

An evaluation in AI functions similarly to unit or integration testing in traditional software, preventing the deployment of changes without proper verification <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. To test quality before production, three key components are essential <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>:

1.  **Agent**
    The agent is the system or component being evaluated, which could be an end-to-end agent, a specific function, or a retrieval pipeline <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Different agents, such as customer service chatbots or Q&A systems for legal contracts, have unique requirements regarding accuracy, compliance, explainability, and nuance that evaluations must account for <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

2.  **Dataset**
    The dataset is crucial as it defines what the agent is evaluated against <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It must include both the types of queries and requests the system will receive in production (inputs) and the ideal responses (outputs) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Importantly, datasets need to cover not only typical "happy paths" but also tricky edge cases where things might go wrong <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. These examples should ideally be written by domain experts who understand the business context and quality requirements <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

3.  **Evaluators**
    Evaluators determine how quality is measured <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
    *   **Human Evaluators:** Traditionally, subject matter experts review outputs, score them, and provide feedback, though this is slow and expensive <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>, <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
    *   **Code-Based Evaluators:** Suitable for objective metrics like response time or latency <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
    *   **LLM Evaluators:** Promise to combine the nuance of human reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

These components are dynamic and must evolve as the AI system improves <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. An improving agent requires more challenging test cases, and increasingly sophisticated evaluation criteria may necessitate different types of evaluators <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

### The Rise of LLM Evaluators

LLM evaluators have become popular due to their compelling advantages <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>:
*   **Speed:** Evaluations that previously took 8-10 hours with human evaluators can now be completed in under an hour, or a full day's work with Mechanical Turk can be done in 50-60 minutes with an LLM evaluator <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This represents a huge, incremental improvement <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Cost:** A 10x cost reduction is observed; traditional human evaluations via Mechanical Turk cost several hundred dollars for a thousand ratings, while LLM evaluators range from $3 to $120 depending on the model <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>, <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Consistency:** LLM evaluators achieve over 80% consistency with human judgments, a level comparable to agreement rates between different human evaluators <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Research papers like NLG Eval and SPADE show strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### Challenges with LLM Evaluators

Despite their promise, LLM evaluators face two major problems that necessitate continuous improvement <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>:

1.  **Criteria Drift:**
    Relying on built-in evaluation criteria from popular frameworks (e.g., Ragas, Prompts, LangChain) can lead to issues <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. These generalizable criteria may not measure what's important for a unique use case <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. For example, an e-commerce recommendation system's evaluator might check for context relevance but miss deeper user requirements for relevance, leading to user complaints despite good testing results <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. Criteria drift occurs when the evaluator's definition of "good" no longer aligns with the user's <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

2.  **Dataset Drift:**
    This problem arises from a lack of test coverage in datasets <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. Handcrafted, "perfect" test cases may not hold up when real-world users introduce context-dependent, messy inputs <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. Users often ask questions broader than anticipated, require real-world data (e.g., from search APIs), or combine multiple questions in unexpected ways <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. When datasets don't represent reality, metrics can still appear good, creating a false sense of security <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## A Three-Step Approach to Continuous Improvement

To address these challenges and ensure [[Improving AI evaluation methods | evaluations work effectively]], an iterative alignment process is crucial <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>, <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>:

1.  **Align Evaluators with Domain Experts**
    Regularly have domain experts grade outputs and critique evaluator results to identify what the evaluator is missing or overemphasizing <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>, <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Use these critiques and few-shot examples in the evaluator prompt to better ground the evaluator's notion of good and bad <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>, <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>. This involves significant massaging and iteration on the evaluator prompt itself <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

2.  **Keep Data Sets Aligned with Real-World User Queries**
    Your test bank needs to be a living, breathing entity <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>, <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Automatically flow underperforming queries from production back into the test suite <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. These real-world failures are "golden" opportunities to improve the test bank and the application <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. Continuously add these test cases with ground truth data to refine the dataset <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>, <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

3.  **Measure and Track Alignment Over Time**
    Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales to track how well your evaluator matches human judgment <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>, <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. This systematic measurement informs whether the evaluator is truly improving or regressing with each iteration <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

### Practical Implementation Steps

*   **Customize the LLM Evaluator Prompt:** Don't rely solely on templated metrics, which can be meaningless <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>, <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Carefully tailor evaluation criteria, add few-shot examples of critiques from domain experts, and decide between binary or Likert scales for ratings (binary is highly recommended) <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>, <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. Ensure that what you're measuring is truly meaningful to your use case and business context <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Involve Domain Experts Early:** Get domain experts to evaluate the evaluator, even starting with 20 examples in spreadsheets, to gauge alignment between evaluator judgments and expert opinions <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>, <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. Their feedback will inform changes to the evaluator prompt <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Log and Iterate:** Log every time your system underperforms in production <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>. These real-world failures should be continuously added to your test bank with ground truth data <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. Iteratively improve LLM evaluator prompts by testing new versions against your expanding test bank and making them more specific to your use case <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.
*   **Invest in an Eval Console:** Build or use a tool that allows domain experts to iterate on evaluator prompts and assess agreement with evaluator critiques and judgments <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
*   **Systematic Measurement:** Set up a simple dashboard to track alignment scores (F1 score or correlation metrics) over time <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>, <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. This provides a systematic way to track the improvement of your evaluator template <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

The ultimate goal is not perfection but continuous improvement, by building [[User feedback and AI development | iterative feedback loops]] into the development process <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>, <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>, <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>. This approach helps overcome [[challenges with early AI models and improvements | challenges with early AI models]] and ensures [[Advancements in AI model technology and performance | advancements in AI model technology]] translate into real-world impact and [[efficiency and smart execution in AI systems | efficiency]].