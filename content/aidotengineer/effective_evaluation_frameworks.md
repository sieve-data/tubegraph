---
title: Effective evaluation frameworks
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 

Effective [[importance_of_evaluations_in_ai_projects | evaluations]] are considered the single biggest challenge and the "missing piece" to scaling generative AI (GenAI) workloads <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Many concerns arise when attempting to scale GenAI, such as cost, hallucinations, accuracy, and capacity, but the most common missing element is a robust evaluation framework <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Implementing such frameworks can unlock the ability to scale these applications <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Why Evaluations are Crucial

A real-world example highlights the transformative power of [[importance_of_evaluations_in_ai_projects | evaluations]]. A document processing workload, worked on by six to eight engineers for six to twelve months, stalled at 22% accuracy <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. The core issue was a complete lack of [[importance_of_evaluations_in_ai_projects | evaluations]] beyond a single, end-to-end accuracy number <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. By designing an [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] framework that identified specific problems, the team was able to achieve 92% accuracy within six months, leading to the project's successful launch as the largest document processing workload on AWS in North America at the time <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

The primary goal of any [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] framework should be to **discover problems** and, ideally, suggest solutions <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While measuring quality is important, the ability to pinpoint and fix errors is paramount for improvement <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

> [!TIP] Evaluations as a Project Filter
> Within AWS, [[importance_of_evaluations_in_ai_projects | evaluations]] serve as the primary filter distinguishing "science projects" from successful ventures <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Teams willing to invest time in building a robust gold standard for [[steps_to_create_effective_evaluations_for_ai_applications | evaluations]] are the ones whose projects achieve significant return on investment and scale <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Unique Complexities of Generative AI Evaluation

Unlike traditional machine learning where outputs are often numerical and easily quantifiable (e.g., F1 score, precision, recall), GenAI outputs are typically free text <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### The Importance of Reasoning

A critical aspect of GenAI evaluation is assessing not just the output, but **how the model arrived at that output** <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. This means evaluating the model's *reasoning*. For instance, a weather summary GenAI application given sensor data indicating rain and wind might output "today it's sunny and bright outside." While the output is clearly wrong (a score of zero), understanding *why* it produced that output (e.g., "it's important to mental health to be happy, so I decided not to talk about the rain") provides crucial insight for correction <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Conversely, a correct output (e.g., input: sunny, output: sunny) might still be based on flawed reasoning, indicating a fragile system prone to future errors <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Prompt Decomposition

One technique to manage the complexity of GenAI [[importance_of_evaluations_in_ai_projects | evaluations]] is **prompt decomposition** <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This involves breaking down a large, complex prompt into a series of chained, smaller prompts <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

*   **Benefit 1: Granular Evaluation:** By attaching an [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] to each section of the prompt, developers can pinpoint exactly where errors are occurring <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
*   **Benefit 2: Right Tool for the Job:** Decomposition allows for determining whether GenAI is even the appropriate tool for a given segment of the prompt <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. For example, a mathematical comparison ("is seven larger than five?") is better handled by Python than GenAI for perfect accuracy, reducing cost and confusion <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Benefit 3: Cost and Accuracy Improvement:** By removing "dead space" or unnecessary instructions for a given task (e.g., complex instructions for an easy query), decomposition can significantly increase accuracy and reduce cost <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.

An example of prompt decomposition in practice is **semantic routing** <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Here, an initial step uses GenAI to classify an input query (e.g., easy vs. hard task) and then routes it to the appropriate model (small model for easy tasks, large model for hard tasks) <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. [[steps_to_create_effective_evaluations_for_ai_applications | Evaluations]] are attached to each step, ensuring the correct routing and model selection <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

## Seven Habits of Highly Effective Generative AI Evaluations

Successfully scaled GenAI workloads consistently exhibit the following seven habits in their [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] frameworks <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>:

1.  **Fast** <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>:
    *   [[iterative_improvement_of_evaluation_processes | Iterative improvement]] is key; evaluations should enable rapid iteration, ideally within seconds <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.
    *   A target of **30 seconds** for a full [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] run is recommended, achieved by parallelizing generation (100 test cases in 10 seconds), judging (100 judges in 10 seconds), and summarizing results <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
    *   GenAI is often used as a "judge" to evaluate outputs for speed <a class="yt-timestamp" data-t="00:16:58">[00:16:58]</a>.

2.  **Quantifiable** <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>:
    *   Effective frameworks produce numerical scores, even if there's slight "jitter" in results <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
    *   This jitter is mitigated by having a **numerous** set of test cases and averaging across them <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>.

3.  **Explainable** <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>:
    *   Beyond just the output, understand the *reasoning* behind the generation <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>.
    *   Also, ensure the *judge's* reasoning is clear, often by engineering a rubric and asking the judge model to explain its scoring <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This ensures the judge prompt is correctly engineered.

4.  **Segmented** <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>:
    *   Most scaled GenAI workloads involve multiple steps, not a single prompt <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.
    *   Each step should be evaluated individually <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>, allowing for selection of the most appropriate (and often smallest, most cost-effective) model for that specific step <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.

5.  **Diverse** <a class="yt-timestamp" data-t="00:22:09">[00:22:10]</a>:
    *   [[steps_to_create_effective_evaluations_for_ai_applications | Evaluation]] sets must cover all intended use cases, including core cases (many examples) and edge cases (fewer examples) <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
    *   Include questions that fall outside the desired scope to measure the model's ability to redirect such queries <a class="yt-timestamp" data-t="00:19:58">[00:19:58]</a>.

6.  **Traditional** <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>:
    *   Do not abandon [[challenges_and_limitations_of_traditional_evaluation_methods | traditional evaluation methods]] <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.
    *   For numerical outputs, use standard numerical [[evaluations_versus_traditional_metrics_in_ai | metrics in AI]] <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
    *   For Retrieval Augmented Generation (RAG) architectures, use [[metrics_for_evaluating_RAG_systems | metrics for evaluating RAG systems]] like retrieval precision and F1 scores <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.
    *   Traditional tooling is also crucial for measuring cost and latency <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>.

### The Gold Standard Set

The foundation of an effective [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] framework is the **gold standard set** <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. This set dictates the entire system's design and purpose, so investing time in building a high-quality, error-free gold standard is crucial <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>.

> [!CAUTION] Avoid GenAI for Gold Standard Creation
> Using GenAI to create the gold standard set is generally a poor practice, as it can embed the AI's own errors into the benchmark, leading to a system that perpetuates those same errors <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. While GenAI can generate a "silver standard" (a preliminary guess), it must always be reviewed and confirmed for accuracy by a human <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

## The Evaluation Process Visualized

An [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] process typically flows as follows <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>:
1.  **Input from Gold Standard Set:** A specific query or scenario is taken from the pre-defined, human-verified gold standard <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
2.  **Prompt Template & LLM:** This input is fed into the GenAI prompt template and processed by the Large Language Model (LLM) <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
3.  **Generated Output:** The LLM produces an output, which should ideally include both the answer and the reasoning behind it <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
4.  **Judge Prompt:** The generated output is compared against the correct answer from the gold standard, often by another GenAI model acting as a "judge" <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.
5.  **Judge Output:** The judge generates a numerical score and the reasoning behind that score <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>.
6.  **Categorization & Summary:** The evaluation results are categorized (often based on categories pre-defined in the gold standard) to provide a summary of correct and incorrect answers, highlighting trends and areas for improvement <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>.