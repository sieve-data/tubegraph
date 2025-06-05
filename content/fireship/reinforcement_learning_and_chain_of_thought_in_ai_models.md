---
title: Reinforcement learning and chain of thought in AI models
videoId: 6xlPJiNpCVw
---

From: [[fireship]] <br/> 

Recent advancements in Artificial Intelligence (AI) have introduced new paradigms for deep thinking and [[artificial_intelligence_and_reasoning_models | reasoning models]], exemplified by OpenAI's O1 model. These models represent a significant leap beyond basic GPT architectures, demonstrating improved performance across various benchmarks, particularly in mathematics, coding, and science <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

## O1 Model Overview

The O1 model is characterized as a "new paradigm of deep thinking or [[artificial_intelligence_and_reasoning_models | reasoning models]]" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. OpenAI has released three versions: O1 mini, O1 preview (accessible to the public), and O1 regular (currently restricted, with hints of a $2,000 Premium Plus plan for access) <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. It's important to note that O1 is not considered ASI, AGI, or even a successor to GPT-5 <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

### Benchmarks and Performance

O1 shows substantial gains in accuracy compared to GPT-4, particularly in:
*   PhD-level physics <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>
*   Massive Multitask Language Understanding (MMLU) benchmarks for Math and formal logic <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>
*   Coding ability:
    *   At the International Olympiad in Informatics, it reached the 49th percentile with 50 submissions per problem and achieved a gold medal submission when allowed 10,000 submissions <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.
    *   Its CodeForce ELO improved from the 11th percentile (GPT-4) to the 93rd percentile <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
    *   In collaboration with Cognition Labs, O1 solved 75% of problems, a significant increase from GPT-4's 25% <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.

### Core Mechanisms

The distinctiveness of O1 models lies in their reliance on [[reinforcement_learning_in_ai_models | reinforcement learning]] to execute complex reasoning tasks <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

#### Reinforcement Learning

This approach enables models to produce a [[applications_of_chain_of_thought_models | chain of thought]] before presenting a final answer to the user, effectively "thinking" through the problem <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This method, while novel in its general availability, has been employed by Google for years in platforms like AlphaProof and AlphaCoder for math and coding competitions, using [[reinforcement_learning_in_ai_models | reinforcement learning]] to generate synthetic data <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

#### Chain of Thought and Reasoning Tokens

When presented with a problem, the O1 model goes through a series of internal thoughts to reach a conclusion, generating what are called "reasoning tokens" <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. These tokens act as internal outputs, allowing the model to refine its steps and backtrack when necessary. This process leads to more complex solutions with fewer hallucinations compared to prior models <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

However, this increased depth of thought comes with trade-offs:
*   Slower response times <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>
*   Higher computing power requirements <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>
*   Increased monetary cost, as users pay for these reasoning tokens at a price of $60 per 1 million tokens <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

The actual [[deep_seek_r1_chain_of_thought_model_features | Chain of Thought]] process is typically hidden from the end user, although examples have been provided. For instance, in a coding task to transpose a matrix in bash, the model's internal [[deep_seek_r1_chain_of_thought_models | Chain of Thought]] involved:
1.  Analyzing input and output shapes <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>
2.  Considering programming language constraints <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>
3.  Executing multiple other steps before generating the final response <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

## Practical Implications

In practical tests, O1 has demonstrated significant improvements in coding tasks, such as creating a playable snake game or a nonogram puzzle from a single prompt <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>. When tasked with recreating the game "Drug Wars," O1's output compiled immediately and adhered to game requirements much better than GPT-4 <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Despite some initial bugs and UI issues in the O1-generated game, the model's ability to create a more comprehensive and accurate initial result by leveraging its [[deep_seek_r1_chain_of_thought_model_features | Chain of Thought]] process was evident <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

While O1 is not truly intelligent and can still produce hallucinations and bugs with follow-up prompts, the [[deep_seek_r1_chain_of_thought_model_features | Chain of Thought]] approach holds "huge amount of potential" <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>, <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. O1 can be seen as an advanced version of GPT-4, with the added capability to recursively prompt itself, suggesting an evolution rather than a fundamental game-changer in the current AI landscape <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.