---
title: Best practices for AI evaluation
videoId: wHhlvcQgi9M
---

From: [[aidotengineer]] <br/> 
The greatest challenge in scaling generative AI workloads is often the lack of effective [[Testing and evaluation of AI models | evaluations]] <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. According to Justin Mohler, a Principal Applied AI Architect at AWS, [[Testing and evaluation of AI models | evaluations]] are the "missing piece" that unlocks the ability to scale GenAI systems <a class="yt-timestamp" data-t="01:47:04">[01:47:04]</a>.

### The Purpose of AI Evaluation

The primary goal of any AI evaluation framework should be to [[Evaluation and feedback in AI systems | discover problems]] <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. While measuring quality is important, an effective framework tells you *where* the problems are and can even suggest solutions by including generative AI reasoning <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

A customer example highlights this: a document processing workload stuck at 22% accuracy for six months. Once an [[Testing and evaluation of AI models | evaluation framework]] was designed and implemented, fixing the underlying issues became trivial, leading to 92% accuracy and large-scale deployment within six months <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

[[Testing and evaluation of AI models | Evaluations]] also serve as a crucial filter, separating "science projects" (exploratory efforts) from successful, scalable initiatives. Teams willing to invest time in [[Building custom evaluations for better AI performance | building an evaluation framework]] are more likely to achieve significant returns <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>.

### Understanding Generative AI Evaluation

Unlike traditional machine learning models that often produce quantifiable metrics (e.g., F1 score, precision, recall), generative AI outputs free text, which can be challenging to evaluate <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. However, humans have been grading free text for centuries (e.g., essays) <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>. The key is to provide feedback that explains what went wrong and how to improve, rather than just a score <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.

#### Evaluating Reasoning, Not Just Output

A critical aspect of [[Improving AI evaluation methods | evaluating generative AI]] is to assess the *reasoning* behind the output, not just the final result <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. For instance, a model might produce the correct answer for the wrong reason (e.g., a weather summary that correctly says "sunny" but reveals the model decided to ignore rain data for "mental health" reasons) <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. Understanding the model's reasoning provides invaluable insight into how to fix underlying problems <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.

#### Prompt Decomposition

For complex generative AI prompts, a technique called **prompt decomposition** can be highly effective for [[Testing and evaluation of AI models | evaluation]] <a class="yt-timestamp" data-t="11:23:00">[11:23:00]</a>. This involves breaking a large, complicated prompt into a series of smaller, chained prompts <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. This allows [[Testing and evaluation of AI models | evaluations]] to be attached to each step, pinpointing where errors occur <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>.

Additionally, prompt decomposition helps determine if generative AI is even the right tool for a specific step. For example, a simple mathematical comparison (like "is 7 larger than 5?") is better handled by traditional Python code than a large language model (LLM), improving accuracy and reducing cost <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>.

**Semantic routing** is a common pattern that benefits from decomposition, where an input query is routed to a specific model (e.g., small for easy tasks, large for hard tasks). By evaluating each routing step, accuracy can increase by removing "dead tokens" (unnecessary instructions) that confuse the model and add cost <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

### Seven Habits of Highly Effective Generative AI Evaluations

Based on observations from successfully scaled generative AI workloads, Mohler identifies seven key habits:

1.  **Fast:** Evaluations should be run quickly, ideally within 30 seconds, to enable rapid iteration. This allows teams to make hundreds of changes and tests daily, accelerating innovation <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>. This speed is achieved by using generative AI as a judge in parallel for scoring and by summarizing results by category <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.
2.  **Quantifiable:** Effective frameworks produce numbers (scores). While there might be some jitter in scores for free-text outputs, running numerous test cases and averaging the scores can mitigate this <a class="yt-timestamp" data-t="18:17:00">[18:17:00]</a>.
3.  **Numerous:** Having a large number of test cases (e.g., 100) helps cover diverse use cases and averages out score jitter <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>. The process of building these test cases can also help clarify project scope and product design <a class="yt-timestamp" data-t="19:32:00">[19:32:00]</a>.
4.  **Explainable:** The evaluation should provide insight into *how* the model reached its output (its reasoning) and *how* the judge scored it. This means engineering the judge's prompt with a clear rubric and asking it to explain its reasoning, similar to a professor grading an essay <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>.
5.  **Segmented:** Most scaled workloads involve multiple steps or chained prompts. Each step should be evaluated individually to identify precise error locations and determine the most appropriate (often smallest) model for each task <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>.
6.  **Diverse:** Evaluations should cover all in-scope use cases, with more examples for core functions and fewer for edge cases <a class="yt-timestamp" data-t="22:09:00">[22:09:00]</a>.
7.  **Traditional:** Don't abandon traditional [[Testing and evaluation of AI models | evaluation techniques]]. If an output is numeric, use numeric evaluation. For Retrieval Augmented Generation (RAG) architectures, traditional database accuracy [[Testing and evaluation of AI models | evaluations]], retrieval precision, and F1 scores are still relevant. Cost and latency measurements also rely on traditional tooling <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.

### Building an Evaluation Framework

A common visual workflow for building an evaluation framework involves:

1.  **Gold Standard Set:** Start with a carefully crafted "gold standard set" of inputs and expected outputs (including reasoning) <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>. This set should *not* be generated by AI, as it might perpetuate existing errors. While AI can create a "silver standard" (a guess), it requires human review for accuracy <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.
2.  **Generate Output:** Take an input from the gold standard set, feed it into the prompt template and LLM to generate an output (including its answer and reasoning) <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.
3.  **Judge Output:** Compare the generated output against the matching gold standard answer using a "judge prompt." The judge should generate a score and explain its reasoning for that score <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
4.  **Categorize & Summarize:** Pull the category associated with the input (often included in the gold standard set) to break down results by category. This allows for a summary of right and wrong answers per category, aiding in problem identification <a class="yt-timestamp" data-t="24:54:00">[24:54:00]</a>.