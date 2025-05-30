---
title: Prompting Techniques for o1 Model
videoId: MhlNfCIDToo
---

From: [[everyinc]] <br/> 

OpenAI has released a new model called o1, available in ChatGPT through the model selector <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This model introduces a new paradigm for AI performance, influencing how users should approach [[prompt_engineering_techniques | prompting]] it <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Overview of the o1 Models
The o1 model comes in two variants:
*   **o1 Preview** <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
    *   Smarter and slower <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   Possesses more knowledge of the world, making it suitable for questions requiring general knowledge <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **o1 Mini** <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>
    *   Faster but has less world knowledge <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>.
    *   Excels in math and coding problems, having scored an 800 on SAT Math <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
    *   Recommended for reasoning-specific problems <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

For a more detailed comparison, see [[Differences Between o1 Preview and o1 Mini | Differences Between o1 Preview and o1 Mini]].

## The Core Difference: Chain of Thought Reasoning
The key to o1's improved performance lies in its native "Chain of Thought" reasoning <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Process Visualization**: When given a complex question, o1 displays a "thinking" message and shows a summary of its thought process, such as "presenting a proof" or "revisiting ancient beliefs" <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. This allows users to see the steps it takes to arrive at an answer, similar to how one might perform long division on paper rather than in their head <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Improved Accuracy**: Chain of Thought reasoning, when explicitly requested from older GPT models, was found to improve accuracy and reduce hallucinations <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. o1 is trained to perform this process natively through reinforcement learning <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.
*   **Scalable Performance**: OpenAI discovered that scaling the amount of time the model uses to think (e.g., 7 seconds for a specific query) also scales its performance <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. This means future models might spend hours or days on difficult problems before responding <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

## Prompting o1: A New Skill in the Allocation Economy
The unique nature of o1, particularly its potential for long computation times and associated costs, suggests that [[the_concept_of_prompt_programming_and_its_potential | prompting]] it effectively will become a critical skill <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **Strategic Allocation**: Users will need to know when to utilize an "expensive, long-running model" like o1 and how to maximize its output <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
*   **Cost-Benefit Analysis**: Running o1 can be a "big bet," potentially taking minutes, hours, or even days to complete, incurring time and monetary costs <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. Therefore, knowing which "bets to take" and how to formulate successful prompts is essential <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Specific Prompting Techniques for o1
[[Prompt engineering techniques | Prompting]] o1 differs significantly from prompting other models like GPT-4o <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Conciseness is Key**: o1 performs better with shorter prompts that get straight to the point <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
*   **Avoid Extraneous Detail**: Unlike GPT-4o, where adding extensive context did not significantly degrade performance <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>, o1 requires users to be "more choosy" about the specific information provided <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>. This specificity helps its Chain of Thought reasoning remain on track <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## Use Cases and Benefits
The o1 model is particularly useful for tasks requiring a high level of reasoning <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **Complex Reasoning**: Approximately 10-20% of daily prompts may benefit from o1's advanced reasoning capabilities <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.
*   **Business Applications**: Businesses are expected to be major beneficiaries, as they are more likely to have complex queries that require significant, long-running reasoning processes <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. One internal incubation saw a 20% improvement from simple use of o1 <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.