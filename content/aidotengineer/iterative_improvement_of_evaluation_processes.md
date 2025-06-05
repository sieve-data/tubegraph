---
title: Iterative improvement of evaluation processes
videoId: 3jwClx0Ft2E
---

From: [[aidotengineer]] <br/> 

[[importance_of_evaluations_in_AI_projects | Evaluations]] are fundamental to building AI systems that deliver real-world value, moving beyond mere "fancy demos" <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Just as traditional software relies on unit and integration testing before deployment, AI applications require robust [[evaluations_and_finetuning_in_ai_development | evaluations]] to ensure quality before pushing changes to production <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Components of an [[effective_evaluation_frameworks | Effective Evaluation Framework]]

To test the quality of an AI application before production, three key components are needed <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>:

1.  **Agent**: This is the system or function being evaluated, which could be an end-to-end agent, a small function within an agent, or a retrieval pipeline <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. Different agents, such as a customer service chatbot or a Q&A agent for legal contracts, have unique requirements and challenges <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. For example, a document Q&A system might need to be accurate, compliant with regulations, explain its reasoning, and understand nuanced financial accounting standards, all of which the [[evaluations_and_finetuning_in_ai_development | evaluation]] must account for <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
2.  **Data Set**: The dataset is what the agent is evaluated against <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. It must include both inputs (types of queries/requests the system will receive in production) and ideal outputs (what good responses should look like) <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. These datasets should cover not only "happy paths" but also tricky edge cases where things might go wrong, and ideally, be written by domain experts who understand the business context <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
3.  **Evaluators**: This component determines how quality is measured <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
    *   **Human Evaluators**: Traditionally, subject matter experts review and score outputs, providing feedback, but this is slow and expensive <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
    *   **Code-based Evaluators**: Effective for objective metrics like response time or latency <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
    *   **LLM Evaluators**: These promise to combine the nuance of human reasoning with the speed and scalability of automated systems <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

## The Rise of LLM Evaluators

LLM evaluators have gained significant popularity, with many teams switching their entire [[evaluations_versus_traditional_metrics_in_ai | evaluation]] stack to rely on LLMs as judges <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>. Their main promises are compelling:

*   **Speed**: Evaluations that took 8-10 hours with human evaluators can now be completed in under an hour <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>. For example, 1,000 test cases that might take a full day with Mechanical Turk could be evaluated in 50-60 minutes with an LLM evaluator <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   **Cost**: A traditional human [[evaluations_versus_traditional_metrics_in_ai | evaluation]] through Mechanical Turk for 1,000 ratings could cost several hundred dollars, whereas LLM evaluators range from $3 to $120, representing a 10x cost reduction <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   **Consistency**: LLM evaluators show over 80% consistency with human judgments <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. Research papers like NLG Eval and SPADE show strong correlations between human judgments and LLM scores <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>, with major model providers increasingly using this direction for alignment <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

## [[challenges_and_limitations_of_traditional_evaluation_methods | Challenges and Limitations]] of LLM Evaluators

Despite their advantages, LLM evaluators face two major problems <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>:

### [[addressing_criteria_drift_and_data_set_drift_in_evaluations | Criteria Drift]]
This occurs when an evaluator's notion of what constitutes "good" no longer aligns with the user's perception of quality <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. Popular frameworks often use generalized evaluation criteria that may not measure what is crucial for a unique use case <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>. For instance, an e-commerce recommendation system might pass initial [[evaluations_and_finetuning_in_ai_development | evaluations]] based on context or generation relevance, but fail in production because the evaluator over-indexed on keyword relevance instead of the broader product description and user query context, leading to user complaints <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>. [[addressing_criteria_drift_and_data_set_drift_in_evaluations | Criteria drift]] can also happen if the underlying LLM model used for [[evaluations_and_finetuning_in_ai_development | evaluation]] changes, leading to inconsistent grading <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. Research suggests that evaluation criteria must evolve over time to balance true positives with false positives and maximize alignment with human judgments <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### [[addressing_criteria_drift_and_data_set_drift_in_evaluations | Data Set Drift]]
This problem arises when datasets lack sufficient test coverage, meaning they don't accurately represent real-world usage <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. Hand-written test cases, even if initially "golden," often don't hold up in beta or production when real users provide messy, context-dependent inputs or ask broader, more complex, or combined questions <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. The system's metrics might still look good on the existing test cases, but it fails in reality because the test cases no longer reflect actual conditions <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.

## [[strategies_for_ai_evaluation_and_troubleshooting | Strategies for AI Evaluation and Troubleshooting]]: Iterative Alignment

The solution lies in ensuring that evaluators and datasets are iteratively aligned, similar to how an LLM application itself is aligned <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.

### [[steps_to_create_effective_evaluations_for_ai_applications | Three-Step Approach]] for Iterative Improvement:

1.  **Align Evaluators with Domain Experts**: Have domain experts regularly grade outputs and critique evaluator results <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>. Incorporate their feedback and "few-shot examples" into the evaluator prompt to ground it in a real-world understanding of good and bad <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. Continuously iterate on the evaluator prompt, moving beyond templated metrics, until a satisfactory level of agreement is reached <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.
2.  **Keep Data Sets Aligned with Real-World User Queries**: Treat the test bank as a "living, breathing thing" <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>. Log underperforming queries from production and automatically or manually flow them back into the test suite <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.
3.  **Measure and Track Alignment Over Time**: Use concrete metrics like F1 score for binary judgments or correlation coefficients for Likert scales <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. Tracking how well the evaluator matches human judgment with every iteration helps determine if the evaluator is truly improving or regressing <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a>.

### Practical Implementation Steps:

*   **Customize the LLM Evaluator Prompt**: This is considered the most important step <a class="yt-timestamp" data-t="15:11:00">[15:11:00]</a>. Tailor evaluation criteria, add few-shot examples of critiques from domain experts, and decide between binary or Likert scales (binary is highly recommended) <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>. Ensure that the prompt measures what is truly meaningful to the specific use case, application, and business context, rather than relying on out-of-the-box metrics <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Involve Domain Experts Early**: Have domain experts evaluate the evaluator itself, even starting with 20 examples in a spreadsheet, to gauge alignment with their judgments and inform future prompt changes <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.
*   **Log and Update Test Bank**: Continuously log underperforming queries from production and add them, along with ground truth labels, to the test bank <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. These real-world failures are invaluable for identifying where the [[evaluations_and_finetuning_in_ai_development | evaluation]] system falls short <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.
*   **Iterate LLM Evaluator Prompts**: Evaluator prompts are not static; they must evolve <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>. Test new versions against the expanding test bank, making them more specific to the use case <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>. Investing in or building an "eval console" can help domain experts iterate on prompts and assess agreement with evaluator judgments <a class="yt-timestamp" data-t="17:08:00">[17:10:00]</a>.
*   **Systematic Measurement**: It's crucial to track alignment scores (F1, correlation metrics) over time using a dashboard to systematically monitor evaluator improvement <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>. This process mirrors how the original LLM application's prompt is tested <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>.

## Conclusion

The ultimate goal is continuous improvement, not perfection <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>. LLM [[evaluations_and_finetuning_in_ai_development | evaluations]] are only as effective as their alignment with real-world usage <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>. Avoid static [[evaluations_and_finetuning_in_ai_development | evaluation]]—LLMs don't work with a "set it and forget it" approach <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>. Instead, [[ai_product_development_iteration | build iterative feedback loops]] into the development process for significant payoff <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.