---
title: Limitations of large language models (LLMs) in solving novel tasks
videoId: UakqL6Pj9xo
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Large Language Models (LLMs) have demonstrated remarkable capabilities in various tasks, but they exhibit significant limitations when faced with truly novel problems that require adaptation and reasoning beyond their training data. François Chollet, AI researcher at Google and creator of Keras, highlights these limitations, particularly in the context of the [[arc_as_a_benchmark_for_machine_intelligence_and_its_resistance_to_memorization | Abstraction and Reasoning Corpus (ARC) benchmark]].

## The Challenge of True Novelty

A core limitation of LLMs is their difficulty in adapting to tasks and situations that are genuinely novel from the perspective of their training data [[ai_alignment_and_safety | [00:03:49]]]. While LLMs can appear to perform complex reasoning, this is often a result of retrieving and reapplying learned patterns rather than synthesizing new solutions on the fly.

### Memorization vs. Generalization

LLMs are described as "big interpolative memory" systems [[role_of_memory_in_learning_and_understanding | [00:01:24]]], [[ai_scalability_and_breakthroughs | [00:18:59]]]. Their performance on many benchmarks can be attributed to their ability to memorize a vast number of patterns and even specific solutions [[ai_alignment_and_safety | [00:17:53]]]. If a problem, or a similar variant, has been seen during training, LLMs can often "fetch" an appropriate pre-existing solution program [[the_role_of_memory_in_learning_and_understanding | [00:18:33]]].

Chollet distinguishes between:
*   **Skill:** The ability to perform tasks based on learned knowledge and patterns. Scaling up LLMs and their training data increases their skill and usefulness on tasks they have been exposed to [[ai_alignment_and_safety | [00:19:25]]].
*   **Intelligence:** The ability to adapt efficiently to new, previously unseen situations and acquire new skills with little data [[the_role_of_deep_learning_and_discrete_program_search_in_ai_development | [00:04:08]]], [[impact_of_ai_on_software_development_and_productivity | [00:19:30]]]. Scaling alone does not inherently increase this form of intelligence [[ai_alignment_and_safety | [00:00:00]]], [[impact_of_ai_on_software_development_and_productivity | [00:19:19]]].

An example illustrating this is the Caesar cipher: LLMs might solve it for common transposition lengths (e.g., 3 or 5) seen frequently online, but fail with an arbitrary, less common number (e.g., 9), suggesting they've memorized specific cases rather than the general algorithm [[ai_alignment_and_safety | [00:26:40]]].

### The Constantly Changing World

The real world is dynamic and constantly presents new situations [[impact_of_ai_on_future_technology_and_society | [00:05:15]]]. Human intelligence evolved to cope with this unpredictability, allowing us to adapt to circumstances not explicitly prepared for by our experiences or evolutionary history [[impact_of_ai_on_future_technology_and_society | [00:05:34]]], [[the_role_of_deep_learning_and_discrete_program_search_in_ai_development | [00:58:55]]]. LLMs, trained on static datasets, fundamentally struggle with this aspect. For instance, a self-driving car (often using transformer models similar to LLMs [[ai_alignment_and_safety | [00:30:38]]]) trained extensively in one city like the Bay Area would likely fail if deployed in a significantly different environment like London, with different driving rules and layouts, without specific retraining for that new environment [[ai_alignment_and_safety | [00:30:09]]].

## The ARC Benchmark: A Litmus Test for Novelty

The Abstraction and Reasoning Corpus (ARC) was designed as an "IQ test for machine intelligence" specifically to be resistant to memorization [[the_role_of_memory_in_learning_and_understanding | [00:01:12]]], [[ai_alignment_and_safety | [00:26:04]]].
*   **Novel Puzzles:** Each ARC puzzle is intended to be unique and not found elsewhere, even if an AI has memorized the entire internet [[ai_alignment_and_safety | [00:02:02]]], [[the_role_of_memory_in_learning_and_understanding | [00:08:24]]].
*   **Core Knowledge:** Solving ARC requires only "core knowledge" – basic concepts about objectness, counting, elementary physics, geometry, and symmetries that a young child possesses [[ai_alignment_and_safety | [00:01:38]]], [[the_role_of_memory_in_learning_and_understanding | [00:08:02]]]. LLMs are considered to possess this knowledge [[ai_alignment_and_safety | [00:08:10]]].
*   **LLM Performance:** Despite possessing the requisite core knowledge, LLMs have historically performed poorly on ARC [[ai_alignment_and_safety | [00:02:08]]], [[the_role_of_memory_in_learning_and_understanding | [00:25:42]]]. The primary reason cited is the "unfamiliarity aspect": each task is different, requiring the synthesis of a new solution program on the fly, which LLMs struggle with [[reasoning_in_ai_models | [00:10:57]]]. Approaches that do better on ARC tend towards discrete program search and synthesis [[the_role_of_memory_in_learning_and_understanding | [00:02:17]]].

Even when multimodal models are considered, which might seem better suited for ARC's spatial reasoning, the fundamental challenge of novelty and on-the-fly program synthesis remains the key bottleneck for LLMs [[ai_alignment_and_safety | [00:09:50]]], [[the_role_of_memory_in_learning_and_understanding | [00:11:13]]].

## Program Synthesis vs. Program Fetching

A crucial distinction in how systems solve problems lies in whether they are *synthesizing* a new solution or *fetching* a pre-existing one.
*   **Program Fetching:** LLMs excel at this. When presented with a problem, they can identify a similar problem structure from their training and apply a memorized solution template [[the_role_of_memory_in_learning_and_understanding | [00:18:33]]], [[ai_alignment_and_safety | [00:21:10]]]. This can resemble reasoning but is fundamentally retrieval and application.
*   **Program Synthesis:** This involves creating a *new* program or solution strategy on the fly, often from basic building blocks, when faced with a problem for which no template exists in memory [[ai_alignment_and_safety | [00:21:41]]]. This is dramatically harder and is a key area where LLMs are limited [[ai_alignment_and_safety | [00:28:27]]].

The ability to perform on-the-fly program synthesis is seen as essential for true general intelligence, allowing adaptation to arbitrary tasks [[ai_alignment_and_safety | [00:21:48]]], [[ai_alignment_and_safety | [00:24:28]]].

## Limitations of Current LLM Paradigms

The current dominant paradigm for improving LLMs largely revolves around scaling data, model size, and compute. However, this approach has inherent limitations concerning the development of true generalization and adaptability.

### Scaling and Memorization-Based Benchmarks

Increasing the scale of LLMs and training them on more data primarily enhances their capacity for memorization and pattern recognition within the distribution of that data [[ai_scalability_and_breakthroughs | [00:19:05]]]. Many standard LLM benchmarks can be solved through sophisticated memorization of knowledge and reasoning patterns, which appear as static programs the LLM can retrieve [[the_role_of_memory_in_learning_and_understanding | [00:17:53]]], [[ai_scalability_and_breakthroughs | [00:18:09]]]. This improves "skill" but not necessarily "intelligence" in the sense of adapting to the unknown [[impact_of_ai_on_future_technology_and_society | [00:19:19]]].

### Active Inference and Test-Time Adaptation

Standard LLMs operate via static inference: the model is frozen post-training and does not learn or adapt its internal state during use [[impact_of_ai_on_future_technology_and_society | [00:15:13]]]. Some recent approaches, like that of Jack Cole on ARC, involve "test-time fine-tuning," where the model is adapted on-the-fly for each specific test problem [[ai_alignment_and_safety | [00:15:08]]], [[ai_alignment_and_safety | [01:14:15]]]. This is seen as a step towards "active inference" and is critical for achieving better performance on tasks like ARC [[ai_alignment_and_safety | [00:15:38]]]. However, even these successes often depend on pre-training the LLM on millions of generated ARC-like tasks, effectively attempting to bring the novel tasks into the distribution through sheer volume [[ai_alignment_and_safety | [00:14:29]]], [[challenges_and_methodologies_in_ai_training_and_data_usage | [01:15:47]]]. This strategy could be seen as trying to "cheat" the novelty aspect of a benchmark by brute-forcing the task space [[ai_alignment_and_safety | [00:40:37]]].

### The "Oxygen Out of the Room" Effect

The intense focus and hype surrounding LLMs have, according to Chollet, "sucked the oxygen out of the room" for other AI research directions [[ai_alignment_and_safety | [00:00:34]]], [[impact_of_technological_change_on_politics | [01:07:37]]]. This, combined with a trend towards closed-off frontier research publishing (partially attributed to OpenAI's influence [[open_source_ai_models_and_their_implications | [00:28:00]]], [[open_source_ai_models_and_their_implications | [01:06:14]]], [[metas_advancements_in_ai_technology_and_infrastructure | [01:07:14]]]), may slow down progress towards overcoming these fundamental limitations and achieving more general AI.

## The Path Beyond Current Limitations

Chollet suggests that overcoming these limitations requires moving beyond merely scaling current LLM architectures. A critical path forward involves:
*   **Developing systems capable of efficient adaptation to novelty:** The ability to learn new skills efficiently from little data when faced with unseen tasks is paramount [[ai_alignment_and_safety | [00:03:55]]].
*   **Integrating System 1 and System 2 capabilities:** This involves merging the pattern-recognition strengths of deep learning (akin to human System 1, intuitive thinking) with the systematic reasoning and planning capabilities of approaches like discrete program search and synthesis (akin to human System 2, deliberate thinking) [[the_role_of_memory_in_learning_and_understanding | [00:51:37]]], [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:51:51]]], [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:52:28]]].
*   **Program synthesis guided by learned intuition:** The envisioned architecture would have an outer loop of discrete program search, but this search would be guided and made more efficient by deep learning models providing intuition about promising search directions and evaluating partial solutions [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:52:37]]], [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:53:44]]]. Such a system would assemble solutions from a bank of learned patterns and modules (which could be differentiable or algorithmic) in response to new situations [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:54:29]]].

The development of such hybrid systems, capable of robust on-the-fly program synthesis, is posited as a more promising direction for achieving AI that can genuinely generalize and adapt to the complexities and novelties of the real world [[impact_of_ai_research_trends_and_the_challenges_of_advancing_towards_agi | [00:54:51]]].