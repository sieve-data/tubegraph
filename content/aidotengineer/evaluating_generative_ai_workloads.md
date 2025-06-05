---
title: Evaluating generative AI workloads
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 

Justin Mohler, a Principal Applied AI Architect at AWS, presented a talk on the "seven habits of highly effective generative AI evaluations" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. His small specialist team focuses on helping customers [[scaling_ai_solutions_in_production | scale GenAI workloads]] <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, having observed many successful and failed deployments across various industries and customer sizes <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Through this experience, they've gathered [[best_practices_for_ai_evaluation | best practices]] from successful workloads and identified common failure points <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## The Core Challenge in Scaling Generative AI

The single biggest challenge in [[challenges_in_scaling_generative_ai | scaling generative AI]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> is the lack of proper [[evaluating_and_optimizing_ai_agents_and_workflows | evaluations]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While concerns like cost, hallucinations, accuracy, and capacity often arise <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, evaluations are the "missing piece to scaling GenAI" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Implementing [[evaluating_ai_agent_performance_and_reliability | evaluations]] can unlock the ability to [[scaling_ai_solutions_in_production | scale]] solutions <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Customer Example: Document Processing Workload

In July 2024, Mohler was called to an escalated document processing workload that had been in development for 6-12 months with 6-8 engineers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The project's accuracy was only 22%, leading to thoughts of cancellation <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. After a couple of weeks of discovery, it was evident they had "zero evaluations" beyond a single end-to-end accuracy number <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Designing an [[evaluating_and_optimizing_ai_agents_and_workflows | evaluation framework]] made the problems clear, and fixing them became "trivial" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Within six months, the team built the framework, fixed issues, and achieved 92% accuracy by January <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This success allowed them to [[scaling_ai_solutions_in_production | launch to production at scale]] and become the single largest document processing workload on AWS in North America at the time <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Why Evaluations are Crucial for Project Success

Mohler views [[evaluating_and_optimizing_ai_agents_and_workflows | evaluations]] as the "number one filter that separates a science project from a successful project" <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Teams willing to invest time in creating a "gold standard set" for [[evaluating_ai_agent_performance_and_reliability | evaluations]] are more likely to have successful projects, whereas those who see it as "boring" often end up with unscalable "science projects" <a class="yt-timestamp" data-t="00:05:57">[00:06:14]</a>.

## Purpose of Evaluation Frameworks

While [[evaluating_ai_agent_performance_and_reliability | GenAI evaluations]] *do* produce a score, measuring quality is a secondary goal <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. The *main goal* of any [[evaluating_and_optimizing_ai_agents_and_workflows | evaluation framework]] should be to **discover problems** <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. A good framework tells you *where* the problems are and can even suggest solutions, especially if it incorporates [[generative_ai_project_challenges_and_strategies | generative AI]] reasoning <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

Thinking of evaluations as a tool to find errors leads to a different design mindset than simply measuring performance <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Addressing Generative AI Evaluation Challenges

[[Challenges in AI agent evaluation | Generative AI]] workloads, especially those producing free-text outputs, can seem daunting to evaluate if coming from a traditional AI/ML background focused on exact numeric scores <a class="yt-timestamp" data-t="00:06:57">[00:07:09]</a>. However, humans have been grading and evaluating free text for centuries (e.g., essay grading) <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

The key distinction with [[evaluating_and_optimizing_ai_agents_and_workflows | generative AI evaluations]] is to go deeper than just a score <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Like a good professor, the evaluation should point out what went wrong and where to improve <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Evaluating Reasoning

A unique [[challenges_in_ai_agent_evaluation | complexity]] in [[evaluating_ai_agent_performance_and_reliability | generative AI evaluation]] is that the *methodology* or *reasoning* behind the output matters, not just the output itself <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

For instance, a meteorology company summarized sensor data. If the model incorrectly states "today it's sunny and bright" when it's raining, the output score is zero <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. But if the model's reasoning is revealed as, "it's important to mental health to be happy, so I decided not to talk about the rain" <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>, this provides crucial insight into fixing the problem <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Conversely, a correct output ("sunny") could still be problematic if the underlying reasoning is flawed <a class="yt-timestamp" data-t="00:10:40">[00:11:09]</a>.

## Prompt Decomposition

[[Evaluating_and_optimizing_ai_agents_and_workflows | Prompt decomposition]] is a technique often used in the context of [[evaluating_ai_agent_performance_and_reliability | evaluations]] <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. It involves breaking a large, complex prompt into a "chaining series of prompts" <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. This allows for attaching an [[evaluating_ai_agent_performance_and_reliability | evaluation]] to each section of the prompt <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>, making it easier to identify where errors are occurring and focus efforts <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

This technique also helps determine if [[generative_ai_project_challenges_and_strategies | generative AI]] is even the right tool for a specific part of the prompt <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. For example, a weather company's prompt struggled with simple mathematical comparisons (e.g., "is seven less than five?") <a class="yt-timestamp" data-t="00:12:21">[00:12:48]</a>. By decomposing the prompt and replacing the mathematical comparison with a Python step, accuracy increased to 100% <a class="yt-timestamp" data-t="00:13:38">[00:13:45]</a>.

### Semantic Routing

Semantic routing is a common pattern where an input query is first categorized to determine the task type (easy vs. hard), and then routed to an appropriate model (small model for easy, large model for hard) <a class="yt-timestamp" data-t="00:14:02">[00:14:15]</a>. Attaching [[evaluating_ai_agent_performance_and_reliability | evaluations]] to each step in this process allows for proving which model is most appropriate for each step, often leading to significantly increased accuracy by removing "dead space" or unnecessary tokens/instructions <a class="yt-timestamp" data-t="00:14:34">[00:14:56]</a>.

## Seven Habits of Highly Effective Generative AI Evaluations

These are the seven most common trends observed across [[scaling_ai_solutions_in_production | successfully scaled]] [[generative_ai_project_challenges_and_strategies | generative AI workloads]] <a class="yt-timestamp" data-t="00:15:35">[00:15:37]</a>. Mohler states he has never seen a workload [[scaling_ai_solutions_in_production | scale]] without [[evaluating_and_optimizing_ai_agents_and_workflows | evaluations]], and most include these seven habits <a class="yt-timestamp" data-t="00:15:42">[00:15:46]</a>.

1.  **Fast**:
    *   [[Evaluating_ai_agent_performance_and_reliability | Evaluation]] results should be available quickly, ideally within seconds, not days <a class="yt-timestamp" data-t="00:15:50">[00:15:58]</a>.
    *   This rapid feedback allows teams to make hundreds of changes and tests daily, significantly accelerating the pace of innovation and accuracy improvements <a class="yt-timestamp" data-t="00:16:19">[00:16:30]</a>.
    *   A target rule of thumb is 30 seconds for an [[evaluating_ai_agent_performance_and_reliability | evaluation framework]] run, using [[generative_ai_project_challenges_and_strategies | generative AI]] as a judge or Python for numeric outputs <a class="yt-timestamp" data-t="00:16:51">[00:17:11]</a>. This 30 seconds can be broken down into:
        *   10 seconds for parallel generation across 100 test cases <a class="yt-timestamp" data-t="00:17:18">[00:17:25]</a>.
        *   10 seconds for parallel judging of those results against a gold standard <a class="yt-timestamp" data-t="00:17:28">[00:17:39]</a>.
        *   10 seconds for summarizing the judged output, often broken down by categories, highlighting right and wrong trends <a class="yt-timestamp" data-t="00:17:41">[00:18:15]</a>.

2.  **Quantifiable**:
    *   Effective frameworks always produce numbers <a class="yt-timestamp" data-t="00:18:21">[00:18:24]</a>.
    *   While scores might have some "jitter," this is managed by having enough test cases and averaging the results, similar to how multiple assignments contribute to a student's final grade <a class="yt-timestamp" data-t="00:18:49">[00:19:14]</a>.

3.  **Numerous / Diverse**:
    *   It is important to be **numerous** and **diverse** in test cases to cover all use cases and the full scope of the project <a class="yt-timestamp" data-t="00:19:17">[00:19:22]</a>.
    *   Building 100 test cases helps teams define the project's scope, identifying what queries should be answered and what should be redirected <a class="yt-timestamp" data-t="00:19:32">[00:20:06]</a>.
    *   For core use cases, many examples are needed, while edge cases might only require a few <a class="yt-timestamp" data-t="00:22:20">[00:22:27]</a>.

4.  **Explainable**:
    *   [[Evaluating_ai_agent_performance_and_reliability | Evaluations]] should provide insight into *how* the model reached its output, not just the output itself <a class="yt-timestamp" data-t="00:20:09">[00:20:13]</a>. This includes the reasoning for both the generation and the scoring by the judge <a class="yt-timestamp" data-t="00:20:17">[00:20:20]</a>.
    *   Just as prompt engineering is done for the user-facing prompt, the judge prompt also needs to be engineered <a class="yt-timestamp" data-t="00:20:27">[00:20:35]</a>. Asking the judge to explain its reasoning helps in this process <a class="yt-timestamp" data-t="00:21:16">[00:21:22]</a>.
    *   The judge should operate with a clear "rubric" of rules and instructions, similar to how a professor grades an essay <a class="yt-timestamp" data-t="00:20:49">[00:21:13]</a>.

5.  **Segmented**:
    *   Almost all [[scaling_ai_solutions_in_production | scaled workloads]] are multi-step processes, not single prompts <a class="yt-timestamp" data-t="00:21:26">[00:21:35]</a>.
    *   Each step should be evaluated individually <a class="yt-timestamp" data-t="00:21:36">[00:21:38]</a>. This allows for determining the most appropriate and smallest model for each specific step, optimizing for cost and efficiency <a class="yt-timestamp" data-t="00:21:47">[00:22:06]</a>.

6.  **Traditional**:
    *   It's important not to discard traditional tooling and evaluation techniques when working with [[generative_ai_project_challenges_and_strategies | GenAI]] <a class="yt-timestamp" data-t="00:22:30">[00:22:39]</a>.
    *   For numeric outputs, traditional numeric [[evaluating_ai_agent_performance_and_reliability | evaluations]] are appropriate <a class="yt-timestamp" data-t="00:22:52">[00:22:54]</a>.
    *   For RAG (Retrieval Augmented Generation) architectures, database accuracy [[evaluating_ai_agent_performance_and_reliability | evaluations]], retrieval precision, recall, and F1 scores are still relevant <a class="yt-timestamp" data-t="00:22:58">[00:23:08]</a>.
    *   Measuring cost and latency also relies on traditional tooling <a class="yt-timestamp" data-t="00:23:11">[00:23:13]</a>.

## Evaluation Framework Example

A visual representation of an [[evaluating_and_optimizing_ai_agents_and_workflows | evaluation framework]]:
1.  **Gold Standard Set**: The most crucial part to invest time in <a class="yt-timestamp" data-t="00:23:33">[00:23:36]</a>. Errors in this set will lead to a system that creates similar errors <a class="yt-timestamp" data-t="00:23:44">[00:23:48]</a>. It's generally not recommended to use [[generative_ai_project_challenges_and_strategies | GenAI]] to create the gold standard directly, as it can propagate the system's own biases or errors <a class="yt-timestamp" data-t="00:24:00">[00:24:13]</a>. A "silver standard set" can be generated by [[generative_ai_project_challenges_and_strategies | GenAI]] as a guess, but must be human-reviewed for accuracy <a class="yt-timestamp" data-t="00:24:16">[00:24:23]</a>.
2.  **Generation**: An input from the gold standard set is fed into a prompt template and an LLM to generate an output, which includes both the answer and the reasoning <a class="yt-timestamp" data-t="00:24:26">[00:24:36]</a>.
3.  **Judging**: The generated output and its reasoning are compared with the matching answer from the gold standard input, using a "judge prompt" to generate a score and the reasoning behind that score <a class="yt-timestamp" data-t="00:24:38">[00:24:48]</a>.
4.  **Categorization and Summary**: The gold standard set often includes categories <a class="yt-timestamp" data-t="00:24:54">[00:24:58]</a>. The final step involves breaking down the results by category and generating a summary for right and wrong answers within each category <a class="yt-timestamp" data-t="00:25:02">[00:25:16]</a>.