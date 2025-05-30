---
title: Challenges and strategies in AI evaluation
videoId: E5EgUuzzH5I
---

From: [[everyinc]] <br/> 

The shift from deterministic to stochastic software, especially with the rise of AI, presents significant [[challenges_in_building_ai_tools | challenges in building AI tools]] and evaluating their performance at scale <a class="yt-timestamp" data-t="02:28:26">[02:28:26]</a>. Unlike traditional software where a QA document and tests can guarantee predictable outcomes, AI's probabilistic nature makes testing and evaluation complex <a class="yt-timestamp" data-t="02:28:51">[02:28:51]</a>.

## The Problem of Unknown Failure Cases

A core difficulty with AI evaluation is that the system can fail in various cases, and often, the developers might not even know all the scenarios where failure can occur <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. As prompts are refined, new and sometimes major classes of errors are discovered, even after extensive evaluation sets <a class="yt-timestamp" data-t="02:29:20">[02:29:20]</a>. This makes discovering the full distribution of possible errors exceptionally hard <a class="yt-timestamp" data-t="02:29:30">[02:29:30]</a>.

## Types of Evaluations

Two main categories of evaluations are employed:

### Deterministic Evaluations
If a deterministic evaluation is possible, it is highly preferred <a class="yt-timestamp" data-t="02:29:47">[02:29:47]</a>. This involves designing workflows with classifier elements that produce a clear, enumerable output (e.g., "yes," "no," or a specific value) <a class="yt-timestamp" data-t="02:29:51">[02:29:51]</a>. These are straightforward to evaluate by collecting input data and the correct output, then scoring the AI's performance <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>.

### Non-Deterministic Evaluations
Non-deterministic evaluations often involve using AI to assess another AI's output, for instance, checking if the "vibe" of an output is correct <a class="yt-timestamp" data-t="03:00:59">[03:00:59]</a>. The challenge with this approach is the "meta-problem" of having to evaluate the evaluator itself <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a><a class="yt-timestamp" data-t="03:00:24">[03:00:24]</a>.

> "If you have an AI evaluating, you need to evaluate eval now." <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

Model-graded evaluations require careful setup. They work best when the evaluation task is targeted and clearly described, ensuring the model used for evaluation is extremely good at that specific task <a class="yt-timestamp" data-t="03:00:50">[03:00:50]</a><a class="yt-timestamp" data-t="03:10:50">[03:10:50]</a>.

## Strategies for Effective Evaluation

### Focus on Targeted & Clear Tasks
To ensure reliability, AI models should be used for tasks they excel at, making the evaluation process more trustworthy <a class="yt-timestamp" data-t="03:10:50">[03:10:50]</a>. This often means providing narrow, very clear instructions <a class="yt-timestamp" data-t="03:11:16">[03:11:16]</a>.

### Implement Robust Logging and Data Collection Loops
A solid feedback loop is crucial for [[practical_approaches_to_ai | practical approaches to AI]] development <a class="yt-timestamp" data-t="03:22:23">[03:22:23]</a>. This involves:
1.  **Logging**: Recording outputs and user interactions.
2.  **Collecting Issues**: Identifying and gathering instances where the AI performs incorrectly.
3.  **Labeling**: Categorizing the identified issues.
4.  **Optimizing Prompts**: Improving prompts based on the collected data <a class="yt-timestamp" data-t="03:23:26">[03:23:26]</a>.
5.  **Flagging Regressions**: Ensuring that prompt changes do not negatively impact previously resolved issues <a class="yt-timestamp" data-t="03:23:34">[03:23:34]</a>.

This loop relies on good, appropriate evaluations and data sets that accurately capture the distribution of relevant errors <a class="yt-timestamp" data-t="03:31:53">[03:31:53]</a>.

### Phased Evaluation Approach

Early in a project, it's beneficial to avoid overly rigorous evaluations <a class="yt-timestamp" data-t="03:54:55">[03:54:55]</a>. Starting with a "vibe check" allows for flexibility in structuring the task flow, as significant improvements can come from changing the fundamental structure rather than fixing minor prompt issues <a class="yt-timestamp" data-t="03:03:01">[03:03:01]</a>. Intensive issue finding and data collection become critical when transitioning to a "productionize" mode <a class="yt-timestamp" data-t="03:24:40">[03:24:40]</a>. Dedicated data labelers are helpful in this phase to understand usage patterns and map data sets to real-world application <a class="yt-timestamp" data-t="03:33:31">[03:33:31]</a>.

## Considerations for Context and Input

When providing context to AI models, especially in retrieval-augmented generation (RAG) systems, it's generally best to limit the context and remove irrelevant information <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a><a class="yt-timestamp" data-t="03:44:41">[03:44:41]</a>. While models are gaining longer context windows, issues like latency costs, attention distribution (where relevant information in the middle of context might be overlooked), and overall quality still mean that more selective context packing yields better results <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. As models evolve with longer context and faster processing, the need to meticulously filter irrelevant data may decrease <a class="yt-timestamp" data-t="03:45:57">[03:45:57]</a>.

## Building for Personal Use

A principle in development is building something for personal use <a class="yt-timestamp" data-t="04:50:50">[04:50:50]</a>. This approach is beneficial when developing AI tools, as the relative newness of the field means "low-hanging fruit" hasn't been picked yet <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. It allows developers to explore the "frontier" and often find that creative technical ideas work <a class="yt-timestamp" data-t="04:50:50">[04:50:50]</a>. This feeling of successfully implementing a creative idea provides significant motivation <a class="yt-timestamp" data-t="04:50:50">[04:50:50]</a>.