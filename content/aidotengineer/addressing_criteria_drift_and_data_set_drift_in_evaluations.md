---
title: Addressing criteria drift and data set drift in evaluations
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

Effective evaluation is crucial for building AI systems that deliver real-world value beyond mere demonstrations <a class="yt-timestamp" data-t="0:01:57">[00:01:57]</a>. While traditional software development relies on unit and integration testing, AI applications require robust evaluation frameworks to ensure quality before deployment <a class="yt-timestamp" data-t="0:02:11">[00:02:11]</a>. Many teams, despite having testing setups, often face uncertainty about what constitutes a good evaluation framework <a class="yt-timestamp" data-t="0:02:39">[00:02:39]</a>.

## Components of AI Evaluation

To test quality before production, three key components are needed:
1.  **Agent** <a class="yt-timestamp" data-t="0:02:55">[00:02:55]</a>: This is whatever is being evaluated, ranging from an end-to-end agent or a small function within it, to a retrieval pipeline <a class="yt-timestamp" data-t="0:02:59">[00:02:59]</a>. Agents, such as customer service chatbots or Q&A systems for legal contracts, have unique requirements like accuracy, compliance, explainability, and nuance <a class="yt-timestamp" data-t="0:03:10">[00:03:10]</a>.
2.  **Data Set** <a class="yt-timestamp" data-t="0:03:48">[00:03:48]</a>: This component is what the agent is evaluated against <a class="yt-timestamp" data-t="0:03:53">[00:03:53]</a>. It should include both inputs (production queries/requests) and ideal outputs, covering not just typical scenarios but also tricky edge cases where issues might arise <a class="yt-timestamp" data-t="0:04:12">[00:04:12]</a>. These examples should be written by domain experts who understand the business context and quality requirements <a class="yt-timestamp" data-t="0:04:34">[00:04:34]</a>.
3.  **Evaluators** <a class="yt-timestamp" data-t="0:04:50">[00:04:50]</a>: This defines how quality is measured <a class="yt-timestamp" data-t="0:04:55">[00:04:55]</a>.
    *   **Human Evaluators**: Subject matter experts review and score outputs, providing feedback, but this method is slow and expensive <a class="yt-timestamp" data-t="0:05:00">[00:05:00]</a>.
    *   **Code-Based Evaluators**: Effective for objective metrics like response time or latency <a class="yt-timestamp" data-t="0:05:09">[00:05:09]</a>.
    *   **LLM Evaluators**: These promise to combine the nuance of human reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="0:05:21">[00:05:21]</a>.

These three components are dynamic and must evolve over time as the agent improves, the data set grows, and evaluation criteria become more sophisticated <a class="yt-timestamp" data-t="0:05:57">[00:05:57]</a>.

## The Rise of LLM Evaluators

LLM evaluators have gained significant popularity, with teams switching their entire evaluation stack to rely on LLMs as judges <a class="yt-timestamp" data-t="0:06:19">[00:06:19]</a>. Their main promises are compelling:
*   **Speed**: Evaluations that previously took 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="0:06:43">[00:06:43]</a>. For a thousand test cases, human evaluations might take a full day, while an LLM evaluator could finish in 50-60 minutes <a class="yt-timestamp" data-t="0:06:54">[00:06:54]</a>.
*   **Cost**: A traditional human evaluation for a thousand ratings might cost several hundred dollars, whereas LLM evaluators range from $3 to $120, representing a 10x reduction in cost <a class="yt-timestamp" data-t="0:07:19">[00:07:19]</a>.
*   **Consistency**: LLM evaluators show over 80% consistency with human judgments <a class="yt-timestamp" data-t="0:07:45">[00:07:45]</a>. This level of consistency is comparable to the agreement between different human evaluators <a class="yt-timestamp" data-t="0:07:55">[00:07:55]</a>. Research papers like NLG Eval and SPADE show strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="0:08:12">[00:08:12]</a>. Major model providers like OpenAI and Anthropic are also increasingly using LLM evaluators for alignment <a class="yt-timestamp" data-t="0:08:20">[00:08:20]</a>.

## Challenges and Limitations of Traditional Evaluation Methods

Despite their advantages, LLM evaluators face two major problems that can render evaluations meaningless <a class="yt-timestamp" data-t="0:08:42">[00:08:42]</a>:

### Criteria Drift
Criteria drift occurs when an evaluator's notion of "good" no longer aligns with the user's perception of quality <a class="yt-timestamp" data-t="0:10:41">[00:10:41]</a>. This often happens because popular frameworks (e.g., Ragas, Prompts, LangChain) use built-in evaluation criteria designed for generalizability, not specific use cases <a class="yt-timestamp" data-t="0:09:10">[00:09:10]</a>.

For example, an AI startup building an LLM-based recommendation system for e-commerce found that while their evaluator checked standard boxes like context relevance and generation relevance, it missed crucial user requirements for relevance in production <a class="yt-timestamp" data-t="0:09:29">[00:09:29]</a>. The evaluator focused too heavily on keyword relevance, failing to consider the broader context of product descriptions in relation to user queries <a class="yt-timestamp" data-t="0:09:58">[00:09:58]</a>. Additionally, inconsistent grading can occur if the underlying LLM model for the evaluator changes or is not a stable version <a class="yt-timestamp" data-t="0:10:30">[00:10:30]</a>. Research, such as the EvalGen paper by Shanker and his team at Berkeley, highlights that evaluation criteria must evolve over time to balance true positives and false positives and maximize F1 score alignment with human judgments <a class="yt-timestamp" data-t="0:10:50">[00:10:50]</a>.

### Data Set Drift
[[challenges_in_current_ai_benchmarking_practices | Data set drift]] refers to when test data sets lack sufficient coverage and no longer represent real-world usage patterns <a class="yt-timestamp" data-t="0:11:19">[00:11:19]</a>. Developers might spend weeks crafting perfect test cases with clear queries and expected answers, but these curated tests often fail to hold up when real users introduce messy, context-dependent inputs <a class="yt-timestamp" data-t="0:11:27">[00:11:27]</a>.

Users commonly ask questions broader than anticipated, require real-world data like search API results, or combine multiple questions in unexpected ways <a class="yt-timestamp" data-t="0:11:55">[00:11:55]</a>. This means that while metrics might look good on existing test cases, they don't reflect actual performance. It's akin to training for a marathon on a treadmill without accounting for real-world factors like incline or surface traction <a class="yt-timestamp" data-t="0:12:26">[00:12:26]</a>.

## [[effective_evaluation_frameworks | Steps to Create Effective Evaluations for AI Applications]]

The key insight to address these challenges is that [[importance_of_evaluatoragentdata_set_alignment | evaluators and data sets need to be iteratively aligned]], similar to how an LLM application itself is aligned <a class="yt-timestamp" data-t="0:12:59">[00:12:59]</a>.

Here is a three-step approach for [[iterative_improvement_of_evaluation_processes | iterative improvement of evaluation processes]]:

1.  **Align Evaluators with Domain Experts**:
    *   Have domain experts regularly grade outputs, not just once, but continuously <a class="yt-timestamp" data-t="0:13:25">[00:13:25]</a>.
    *   Encourage experts to critique evaluator results, identifying what the evaluator misses or overemphasizes <a class="yt-timestamp" data-t="0:13:30">[00:13:30]</a>.
    *   Use these critiques and few-shot examples in the evaluator prompt to ground it in a real-world understanding of quality <a class="yt-timestamp" data-t="0:13:38">[00:13:38]</a>.
    *   Continuously iterate on the evaluator prompt itself, rather than solely relying on templated metrics <a class="yt-timestamp" data-t="0:13:47">[00:13:47]</a>.

2.  **Keep Data Sets Aligned with Real-World User Queries**:
    *   Log real-world usage and treat the test bank as a "living, breathing" entity <a class="yt-timestamp" data-t="0:14:13">[00:14:13]</a>.
    *   Automatically flow underperforming queries from production back into the test suite, either manually or via automation <a class="yt-timestamp" data-t="0:14:19">[00:14:19]</a>. These real-world failures are "golden" opportunities to improve the test bank and identify where the evaluation system falls short <a class="yt-timestamp" data-t="0:16:32">[00:16:32]</a>.
    *   Add ground truth labels to these new test cases to continuously improve the test bank <a class="yt-timestamp" data-t="0:16:47">[00:16:47]</a>.

3.  **Measure and Track Alignment Over Time**:
    *   Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="0:14:35">[00:14:35]</a>.
    *   Track how well the evaluator matches human judgment with every iteration <a class="yt-timestamp" data-t="0:14:44">[00:14:44]</a>. This systematic tracking informs whether the evaluator is truly improving or regressing <a class="yt-timestamp" data-t="0:14:50">[00:14:50]</a>.
    *   Set up a simple dashboard to monitor alignment scores <a class="yt-timestamp" data-t="0:17:30">[00:17:30]</a>.

### Practical Implementation Steps

*   **Customize LLM Evaluator Prompts**: Avoid relying solely on templated metrics <a class="yt-timestamp" data-t="0:15:16">[00:15:16]</a>. Carefully tune evaluation criteria, add few-shot examples of critiques from domain experts, and choose between binary or Likert scales (binary often recommended) <a class="yt-timestamp" data-t="0:15:22">[00:15:22]</a>. Ensure that what is being measured is meaningful to the specific use case, application, and business context <a class="yt-timestamp" data-t="0:15:38">[00:15:38]</a>.
*   **Involve Domain Experts Early**: Get domain experts to evaluate the evaluator itself <a class="yt-timestamp" data-t="0:15:53">[00:15:53]</a>. Even starting with 20 examples in a spreadsheet can provide a good sense of whether evaluator judgments align with expert opinions and inform necessary changes <a class="yt-timestamp" data-t="0:16:00">[00:16:00]</a>.
*   **Iterate LLM Evaluator Prompts**: Evaluator prompts are not static; they must evolve over time <a class="yt-timestamp" data-t="0:16:55">[00:16:55]</a>. Test new versions against the expanding test bank and make them more specific <a class="yt-timestamp" data-t="0:17:03">[00:17:03]</a>.
*   **Invest in an Eval Console**: Build or utilize a tool that allows domain experts to iterate on evaluator prompts and assess agreement with evaluator critiques and judgments <a class="yt-timestamp" data-t="0:17:08">[00:17:08]</a>.

The goal is not perfection, but continuous improvement <a class="yt-timestamp" data-t="0:18:00">[00:18:00]</a>. LLM evaluations are only as effective as their alignment with real-world usage <a class="yt-timestamp" data-t="0:18:07">[00:18:07]</a>. Teams should avoid static evaluation approaches and instead integrate [[evaluations_and_finetuning_in_ai_development | iterative feedback loops]] into their development processes to achieve significant payoffs in evaluation quality <a class="yt-timestamp" data-t="0:18:24">[00:18:24]</a>.

> [!NOTE]
> For tools to implement this workflow, consider platforms like HoneyHive.ai <a class="yt-timestamp" data-t="0:18:40">[00:18:40]</a>.