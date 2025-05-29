---
title: Large Language Models and Intelligence
videoId: yqKJ9pUQ6Q8
---

From: [[causalpython]] <br/> 

Large Language Models (LLMs) have sparked significant debate regarding their capabilities in understanding the world and performing [[language models and reasoning | reasoning]]. Some argue that LLMs can learn "world models," while others maintain this is impossible due to the principles of causal hierarchy <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

## How LLMs Acquire Causal Knowledge

Andrew Lineman from Google DeepMind proposes that LLMs can learn "active causal strategies from passive data" <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This passive data includes observational data, interventional data (describing experiments), and interactions between people (e.g., discussion forums) <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. In simple cases, a transformer-based LLM has been shown to generalize [[causality_and_large_language_models | causal reasoning]] <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

Professor Judea Pearl notes that [[Large Language Models and Causal Reasoning | Large language models]] access a unique type of data: text produced by humans who already possess a causal model of the world <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. This means LLMs can "copy" these models directly from human-authored content, bypassing the constraints of the "ladder of causation" that applies to learning solely from raw data <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. LLMs, in effect, create a "salad of associations" or "salad of rumors" by composing different causal models found in the text they process <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

## Limitations and Benchmarking

While some studies indicate that LLMs perform well on certain [[Large language models and causality | causal benchmarks]], they may perform poorly on others <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Pearl emphasizes the importance of using smaller, well-understood "toy problems" like the "firing squad problem" for benchmarking, as these allow for clear ground truth and controlled experimentation <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Experiments with LLMs on this problem show that while they may initially struggle or even moralize (e.g., "it's illegal to shoot in California"), with careful prompting and repeated clarification of assumptions, they can eventually arrive at the correct [[causality_in_large_language_models | causal conclusion]] <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. This highlights that working with LLMs often becomes an exercise in effective prompting <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

A benchmark proposed by Jiing Jing and Bernal Shilov generates stories with ground truth across different ranks of the ladder of causation <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Interestingly, [[Large Language Models and Causal Reasoning | large language models]] perform significantly worse when problems are presented with abstract variables instead of concrete objects, suggesting they are more proficient with "baby world" (object-based) understanding <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

## Human vs. Artificial Intelligence and Biases

Drawing on Daniel Kahneman's work on biases and errors in human [[language models and reasoning | reasoning]], it is noted that humans are constrained by resources, leading to shortcuts and inherent errors <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. The question arises whether a General Artificial Intelligence (AGI) should always reason correctly in a formal sense. Unlike humans, large machines may not face the same resource limitations, potentially allowing them to search deeper and avoid human-like biases <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. However, they might still be limited by the specific samples accessible in their training data <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. The speculative nature of predicting how future AI will behave is acknowledged due to differing computational limitations <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## The Future of LLMs and AI

Despite current limitations, LLMs are recognized as powerful tools for improving text, finding metaphors, and serving as functional approximators in [[The role of large language models in causal analysis | causal inference]] <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. A "hybrid of [[causality_and_large_language_models | causal inference]] and [[Large language models and causality | large language models]]" is seen as a viable approach <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>.

Future research directions for AI include:
*   **Automatic scientists**: AI systems capable of deciding the best experiments to conduct next <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>. These systems would need to move beyond brute-force experimentation and intelligently select interventions <a class="yt-timestamp" data-t="00:28:16">[00:28:16]</a>, perhaps by proposing local perturbations on existing models and testing intervening variables <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.
*   **Free will**: Understanding the computational advantage and survival value of the "illusion of free will" to program machines that can act as if they possess it <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>. This would lead to more trustable systems that understand human concepts of free will <a class="yt-timestamp" data-t="00:27:58">[00:27:58]</a>.
*   **Metaphors and analogies**: Incorporating the power of metaphors and analogical reasoning into AI, as these are crucial for human understanding and problem-solving, particularly when generating hypotheses for interventions <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>.
*   **Learning user knowledge**: Developing methods to automatically and efficiently learn a user's knowledge structure, treating the user as another "black box" or "environment" to be modeled <a class="yt-timestamp" data-t="00:49:10">[00:49:10]</a>.

There is a hope that the prominence of [[Large Language Models and Causal Reasoning | large language models]] will not "bury" the foundational results in [[causality_and_large_language_models | causal inference]] but rather "expose and amplify" them <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>. As people become more aware of LLM limitations, they inevitably turn to [[causality_and_large_language_models | causal questions]] for improvement, using the causal framework to understand the kind of questions machines can answer and the tools available <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.