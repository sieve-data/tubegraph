---
title: Prompt engineering importance
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

Prompt engineering remains crucial for effectively working with Large Language Models (LLMs) and developing AI-based features <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Why Prompt Engineering is Still Important
While some memes suggest simply telling a model what to do, anyone who has actually shipped an AI-based feature understands that it is much more nuanced <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Understanding what you want the model to do can itself be a significant challenge <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Prompt engineering serves as an excellent starting point for individuals <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, offering the easiest and most accessible method to obtain better outputs from LLMs <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

It is part of a larger system <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. While everyone may have access to the same models, the prompts and architecture surrounding them can provide a competitive advantage in a product <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Simplicity and Efficiency
Prioritizing the simplest solution is key <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. It's easy to get carried away when working with LLMs <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Spending an hour experimenting with a prompt before concluding that a complex Retrieval Augmented Generation (RAG) system is necessary is not advisable <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. If a solution can be achieved through prompt engineering, it is often much simpler to manage <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Key Prompt Engineering Methods
The speaker highlights two main and highly effective methods:
*   **Chain of Thought Prompting** <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   **Few-shot Prompting** <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>

Other methods often fall under the umbrella of general reasoning prompts <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Chain of Thought Prompting
This method involves instructing the model to reason or "think about the problem" before providing an answer <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. It helps break down problems into sub-problems <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, offering insight into the model's thinking process, which aids troubleshooting <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It is widely applicable, easy to implement <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, and so powerful that it's now often built into reasoning models <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

A classic zero-shot approach is to add phrases like "think step by step" or "take a breath and take it through" to encourage reasoning before output <a class="yt-timestamp" data-t="00:02:58">[00:03:12]</a>. Few-shot examples of reasoning steps can also be provided <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. LLMs can also be used to generate these reasoning chains, for instance, through frameworks like Automatic Chain of Thought or AutoReason <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Few-shot Prompting
This involves including examples within the prompt for the model to mimic, effectively "showing rather than telling" <a class="yt-timestamp" data-t="00:04:38">[00:04:47]</a>. Most performance gains are achieved with just one or two examples <a class="yt-timestamp" data-t="00:05:17">[00:05:19]</a>, as adding too many examples can sometimes degrade performance <a class="yt-timestamp" data-t="00:05:28">[00:05:29]</a>. Builders typically need only one or two diverse examples to cover different inputs <a class="yt-timestamp" data-t="00:05:32">[00:05:37]</a>.

### Meta Prompting
This involves using an LLM itself to create, refine, or improve a prompt <a class="yt-timestamp" data-t="00:05:50">[00:05:55]</a>. Various frameworks and free tools exist for this purpose, such as those provided by Anthropic, OpenAI's playground, and PromptHub <a class="yt-timestamp" data-t="00:05:57">[00:06:11]</a>. PromptHub's tool tailors the meta-prompt based on the selected model provider, as prompts optimized for one model might not be effective for another <a class="yt-timestamp" data-t="00:06:14">[00:06:22]</a>.

## Prompting with Reasoning Models
Reasoning models behave very differently in terms of their internal workings and how they are prompted <a class="yt-timestamp" data-t="00:06:51">[00:06:56]</a>.

[!WARNING|Caveats with Reasoning Models]
*   **Fewer Examples are Better:** Research, such as Microsoft's MedPrompt framework with O1 and findings from DeepSeek with R1, indicates that adding examples can lead to worse performance <a class="yt-timestamp" data-t="00:07:06">[00:07:16]</a>. OpenAI also noted that providing excessive context can overcomplicate things and confuse the model <a class="yt-timestamp" data-t="00:07:20">[00:07:27]</a>.
*   **Encourage More Reasoning:** The more reasoning a model performs, the better the output can be <a class="yt-timestamp" data-t="00:07:34">[00:07:40]</a>. Extended reasoning has been shown to yield better results <a class="yt-timestamp" data-t="00:07:51">[00:07:52]</a>, increasing accuracy and performance <a class="yt-timestamp" data-t="00:08:03">[00:08:05]</a>.
*   **Avoid Instructing Reasoning:** For reasoning models, there's no need to explicitly instruct them on how to reason, as it's often built-in <a class="yt-timestamp" data-t="00:08:32">[00:08:34]</a>. Doing so can actually hurt performance <a class="yt-timestamp" data-t="00:08:36">[00:08:39]</a>.

[!NOTE|General Recommendations for Reasoning Models]
*   Use minimal prompting <a class="yt-timestamp" data-t="00:08:09">[00:08:12]</a>.
*   Provide a clear task description <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   Encourage more reasoning if facing performance issues <a class="yt-timestamp" data-t="00:08:17">[00:08:22]</a>.
*   Avoid few-shot prompting, or start with only one or two examples if necessary <a class="yt-timestamp" data-t="00:08:23">[00:08:30]</a>.