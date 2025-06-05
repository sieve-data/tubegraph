---
title: Strategies for AI evaluation and troubleshooting
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 

Evaluating AI applications, particularly those leveraging generative AI, is crucial for successful deployment and scaling. It is often considered the most significant challenge in scaling generative AI workloads and is frequently the missing piece for achieving production-ready solutions <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

## Importance of Evaluations
[[importance_of_evaluations_in_ai_projects | Evaluations]] are not merely about measuring quality; their primary goal should be to discover problems within the AI system <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. By identifying where problems lie and potentially suggesting solutions through generative AI reasoning, evaluation frameworks enable significant improvements to workloads <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

A real-world example demonstrates this: a document processing workload struggled with 22% accuracy. After implementing a comprehensive [[evaluating_ai_system_performance | evaluation]] framework that pinpointed issues, the project achieved 92% accuracy, leading to a successful launch as the largest document processing workload on AWS in North America at the time <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This highlights that knowing *where* the problems are is often more challenging than fixing them <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

Investing in [[evaluating_ai_systems_at_scale | evaluations]] acts as a critical filter, distinguishing successful projects from "science projects" that do not scale <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. Teams willing to dedicate time to building robust evaluation frameworks are more likely to achieve significant returns on investment <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

## Nature of Generative AI Evaluations
Unlike traditional machine learning models with precise F1 scores, generative AI outputs often involve free text, which can seem daunting to quantify <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>. However, humans have evaluated free text for centuries (e.g., grading essays) <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>. The key is to design evaluations that not only provide a score but also explain *what went wrong* and *how to improve* <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

## Troubleshooting through Reasoning Evaluation
A crucial aspect of [[evaluating_ai_agents_methods_and_metrics | evaluating AI systems]] is to look beyond the output and examine the model's *reasoning* or *methodology* <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.

Consider a meteorology company's AI that summarizes local weather based on sensor data. If the sensor data indicates rain, but the summary states "today it's sunny and bright," the output is clearly incorrect <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. However, if the model's internal reasoning is revealed as, "it's important to mental health to be happy, so I decided not to talk about the rain," this insight immediately points to the root cause of the problem and how to fix it <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.

Even if an output is correct, understanding the underlying reasoning is vital for long-term scalability. A correct answer derived from flawed reasoning (e.g., guessing correctly) indicates a fragile system that may fail under different conditions <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

## Prompt Decomposition
[[steps_to_create_effective_evaluations_for_ai_applications | Prompt decomposition]] is a technique often used in conjunction with evaluations to troubleshoot complex generative AI prompts <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. Large, multifaceted prompts make it difficult to pinpoint errors because evaluations only provide an end-to-end score <a class="yt-timestamp" data-t="11:56:00">[11:56:00]</a>.

The strategy involves breaking down a large prompt into a series of smaller, chained prompts <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. This allows for:
*   **Segmented Evaluation:** Attaching an evaluation to each step of the prompt chain, identifying which specific section is causing errors <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.
*   **Tool Selection:** Determining if generative AI is even the most appropriate tool for a particular section of the prompt <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>. For example, a simple mathematical comparison (e.g., "is seven larger than five?") is best handled by Python for perfect accuracy, rather than relying on a generative AI model <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Semantic Routing:** A common pattern where an input query is first categorized to determine the appropriate model or path (e.g., easy task to small model, hard task to large model). [[evaluating_ai_systems_at_scale | Evaluating]] each routing step ensures the right model is chosen for the job, improving overall accuracy and efficiency by reducing "dead tokens" (unnecessary instructions for a given task) <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

## Seven Habits of Highly Effective Generative AI Evaluations
Successful generative AI workloads that scale typically incorporate these seven habits <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>:

1.  **Fast:** Evaluations should produce results quickly, ideally within 30 seconds for a typical test run <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>. This speed allows for many iterations (hundreds of changes and tests daily), significantly accelerating the pace of innovation and accuracy improvements <a class="yt-timestamp" data-t="16:19:00">[16:19:00]</a>. Achieved by parallelizing generation, judging (using generative AI as a judge), and summarizing results <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.
2.  **Quantifiable:** Effective frameworks produce numbers, even if there's some jitter in scores <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. This jitter is mitigated by having a sufficient number of test cases and averaging across them <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.
3.  **Numerous:** Evaluations must cover a diverse range of test cases to ensure broad coverage of all intended use cases and to identify out-of-scope queries <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>. A rule of thumb is at least 100 test cases, with more for core use cases and fewer for edge cases <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>.
4.  **Explainable:** Focus on understanding *how* the model reached its output, not just the output itself <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>. This includes examining the reasoning for both the generation and the scoring by the judge <a class="yt-timestamp" data-t="20:19:00">[20:19:00]</a>. Just like a professor uses a rubric to explain grades, the judge prompt should have clear instructions and be engineered to provide detailed reasoning <a class="yt-timestamp" data-t="20:49:00">[20:49:00]</a>.
5.  **Segmented:** Almost all scaled workloads involve multiple steps or prompts <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>. Each step should be evaluated individually to identify precise error sources and determine the most appropriate (and often smallest) model for each specific sub-task <a class="yt-timestamp" data-t="21:36:00">[21:36:00]</a>.
6.  **Diverse:** As mentioned in "Numerous," evaluations need to cover all in-scope use cases and include examples of out-of-scope queries to measure correct redirection <a class="yt-timestamp" data-t="22:10:00">[22:10:00]</a>.
7.  **Traditional:** Do not abandon traditional [[strategies_for_effective_ai_implementation | AI/ML evaluation techniques]] for generative AI <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. For numeric outputs, direct numeric evaluations are best <a class="yt-timestamp" data-t="22:52:00">[22:52:00]</a>. For RAG architectures, database accuracy, retrieval precision, and F1 scores are still relevant <a class="yt-timestamp" data-t="22:58:00">[22:58:00]</a>. Measuring cost and latency also relies on traditional tooling <a class="yt-timestamp" data-t="23:11:00">[23:11:00]</a>.

## Evaluation Framework Design
[[evaluations_and_finetuning_in_ai_development | Designing]] an [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] framework begins with a **gold standard set** <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>. This set is paramount, as the entire system is designed around it. Errors in the gold standard set will lead to a system that generates the same errors <a class="yt-timestamp" data-t="23:44:00">[23:44:00]</a>. Generative AI can assist in creating a "silver standard set" (a guess at the gold standard), but human review is always necessary to confirm accuracy <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.

The process typically involves:
1.  Taking an input from the gold standard set <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.
2.  Feeding it into a prompt template and an LLM to generate an output, including both the answer and its reasoning <a class="yt-timestamp" data-t="24:28:00">[24:28:00]</a>.
3.  Comparing the generated output with the matching answer from the gold standard input using a "judge prompt" <a class="yt-timestamp" data-t="24:38:00">[24:38:00]</a>.
4.  The judge generates a numerical score and, critically, the reasoning behind that score <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a>.
5.  Including categories in the gold standard set allows for a final summary that breaks down right and wrong answers by category, providing actionable insights for troubleshooting and improvement <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.