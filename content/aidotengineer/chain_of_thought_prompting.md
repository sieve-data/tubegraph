---
title: Chain of Thought prompting
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

[[Chain of Thought reasoning in AI | Chain of Thought (CoT)]] prompting is a revolutionary technique in [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | prompt engineering]] that has proven particularly effective, especially for "test time compute" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It is considered one of the most effective and topical methods <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## What is Chain of Thought Prompting?

[[Chain of Thought reasoning in AI | Chain of Thought]] prompting involves instructing a language model (LLM) to explicitly reason or think about a problem or solution before providing its final answer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Key Characteristics and Benefits
*   **Problem Decomposition** It breaks down complex problems into smaller, manageable sub-problems <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Transparency** It provides insight into the model's thought process, which is beneficial for troubleshooting and understanding its reasoning <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Wide Applicability** [[Chain of Thought reasoning in AI | CoT]] can be used with virtually any model <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Ease of Implementation** It is relatively easy to implement <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Power and Integration** It is so powerful that it is now being built directly into [[Reasoning models and their prompting differences | reasoning models]], often making explicit prompting for reasoning unnecessary for these models <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

## Methods of Implementation

### Zero-Shot Chain of Thought
The simplest way to implement [[Chain of Thought reasoning in AI | CoT]] is to add a phrase to your prompt that encourages the model to think before generating the output <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Examples include:
*   "Think step by step" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
*   "Take a breath and take it through things" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>

### Few-Shot Chain of Thought
Another popular method involves providing [[Few shot prompting | few-shot examples]] that demonstrate the desired reasoning steps <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For instance, when solving math problems, you can include an example where the reasoning steps are explicitly shown <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Automated Chain of Thought Generation
LLMs can also be used to generate these reasoning chains <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Automatic Chain of Thought** is a framework that involves LLMs generating reasoning chains <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Auto Reason** is a single prompt that, when given a task or question, generates reasoning chains, often including [[Few shot prompting | few-shot examples]] of reasoning <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   DeepSeek's R1 model training template leveraged this by having the model generate its thinking process within "think tags," then using these generated reasoning chains to train the model to excel at [[Chain of Thought reasoning in AI | Chain of Thought]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Chain of Thought with Reasoning Models

[[Reasoning models and their prompting differences | Reasoning models]] differ in how they work and how they should be prompted <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Research, including Microsoft's MedPrompt framework and DeepSeek's R1, has shown that for these models:
*   **[[Few shot prompting | Few-shot prompting]] can degrade performance** by over-complicating things and confusing the model <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.
*   **More reasoning generally leads to better output** <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Studies indicate that as the length of the thought process increases, accuracy and performance also increase <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Minimal Prompting is Key** A clear task description is often sufficient. While encouraging more reasoning can help with performance, explicitly instructing the model *how* to reason can actually hurt performance because it's built into the model <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. If [[Few shot prompting | few-shot prompting]] is used, it should be limited to one or two diverse examples <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

> [!NOTE] [[Chain of Thought reasoning in AI | CoT]] prompting, along with [[Few shot prompting | Few-shot prompting]], are considered the most effective and topical methods in prompt engineering <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Many other [[Techniques and patterns in AI orchestration and prompt engineering | reasoning prompts]] exist, often falling under the broader umbrella of general [[Reasoning models and their prompting differences | reasoning models]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.