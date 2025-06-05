---
title: Evaluations versus traditional metrics in AI
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 
The largest challenge in scaling generative AI applications is evaluations, which are frequently the missing piece in a project's ability to scale <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. While concerns like cost, hallucinations, accuracy, and capacity are often raised, a lack of robust evaluations is the primary impediment <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. For example, one document processing workload, initially achieving 22% accuracy, was able to reach 92% accuracy and become the largest of its kind on AWS in North America after an evaluation framework was implemented <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

### Beyond Traditional Metrics: The Goal of Generative AI Evaluations
In traditional AI/ML, evaluations often focus on measuring quality using metrics like F1 score, precision, and recall <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. While generative AI evaluations also produce scores, their primary objective is to [[Strategies for AI evaluation and troubleshooting | discover problems]] and suggest solutions <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. The mindset when designing a generative AI evaluation framework should be to find errors, which leads to a different design approach than simply measuring performance <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

### Unique Complexities in Generative AI Evaluation
[[Challenges in AI Agent Evaluation | Evaluating AI Agent Evaluation]] for generative AI presents unique challenges compared to traditional machine learning:

*   **Free Text Output**: Unlike traditional models that might output specific numbers or classifications, generative AI produces free-form text <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. While humans have been grading free text for centuries, it makes mathematically exact calculations difficult <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.
*   **Evaluating Reasoning, Not Just Output**: The *methodology* or *reasoning* behind a generative AI's output is as important as the output itself <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. A correct answer achieved through flawed reasoning indicates a systemic problem that needs to be addressed for future reliability <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
    *   **Example**: A weather summary model correctly states it's sunny, but its internal reasoning reveals it ignored rain data because "it's important to mental health to be happy" <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>. While the output is correct in one scenario, the underlying logic is flawed and needs fixing. Asking the model to explain its reasoning provides crucial insight <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.

### [[Steps to create effective evaluations for AI applications | Prompt Decomposition]] and Segmentation
Large, complex prompts are challenging to evaluate effectively with a single end-to-end metric, much like trying to find an electrical fault in a complex circuit with a single multimeter reading <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. [[Evaluating AI systems at scale | Prompt decomposition]] involves breaking down a large prompt into a series of chained, smaller prompts <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.

*   **Benefits for Evaluations**:
    *   **Localized Error Identification**: Allows attaching an evaluation to each section of the prompt, pinpointing where errors occur <a class="yt-timestamp" data-t="13:09:00">[13:09:00]</a>.
    *   **Optimized Tool Selection**: Helps determine if generative AI is the right tool for a specific sub-task <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>. For instance, a mathematical comparison (e.g., "is 7 larger than 5?") is better handled by Python than by a large language model <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.
    *   **Increased Accuracy and Efficiency**: By breaking down tasks and using the most appropriate tool (including traditional programming) for each step, accuracy significantly increases, and costs decrease by removing "dead space" or unnecessary tokens from prompts <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.
*   **Semantic Routing**: A common pattern where an initial step classifies an input and routes it to an appropriate model (e.g., small model for easy tasks, large model for hard tasks) <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. Evaluating each routing step independently is crucial, often using traditional numeric evaluations for the routing decision itself <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

### Habits of Effective Generative AI Evaluations

Successfully scaled generative AI workloads typically incorporate the following evaluation habits:

1.  **Fast**: Evaluations should run quickly (e.g., target 30 seconds for a full framework run) to enable rapid iteration and hundreds of changes daily <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>. This contrasts with slow, manual testing that limits development pace <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.
2.  **Quantifiable**: Even with free-text outputs, evaluations should produce numbers <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. To account for potential "jitter" in scores (due to the probabilistic nature of LLMs), use numerous test cases and average results <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.
3.  **Explainable**: Evaluations should provide insight into *why* the model produced a particular output and *how* the judge reasoned its score <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>. This is akin to a professor providing a rubric and feedback, not just a grade <a class="yt-timestamp" data-t="20:50:00">[20:50:00]</a>.
4.  **Segmented**: For multi-step workloads, evaluate each step individually <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>. This allows for choosing the most appropriate (and often smallest, cheapest) model for each specific task, improving efficiency and accuracy <a class="yt-timestamp" data-t="21:47:00">[21:47:00]</a>.
5.  **Diverse**: Cover all relevant use cases with a broad set of test cases, including edge cases and scenarios where the model should *not* respond <a class="yt-timestamp" data-t="22:10:00">[22:10:00]</a>.
6.  **Traditional**: Do not abandon traditional AI/ML techniques. Numeric evaluations, database accuracy metrics (like F1 score for retrieval), cost, and latency measurements are still vital components of a comprehensive evaluation framework for generative AI <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. It's not a replacement, but an integration.

### Evaluation Framework Setup
An effective evaluation framework typically starts with a **gold standard set** of inputs and desired outputs <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>. This set is crucial; errors in the gold standard will propagate throughout the evaluation process <a class="yt-timestamp" data-t="23:42:00">[23:42:00]</a>. Generative AI should not be used to create the gold standard set, as it might introduce the same errors the system aims to fix <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.

The process involves:
1.  Taking an input from the gold standard set <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.
2.  Feeding it into the prompt template and LLM to generate an output, which includes both the answer and its reasoning <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.
3.  Comparing the generated output with the matching gold standard answer using a "judge prompt" <a class="yt-timestamp" data-t="24:38:00">[24:38:00]</a>.
4.  The judge generates a score and the reasoning behind that score <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a>.
5.  Categorizing results (e.g., based on input categories in the gold standard) to summarize right and wrong answers, providing actionable insights for improvement <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.