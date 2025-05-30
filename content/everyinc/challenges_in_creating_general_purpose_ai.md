---
title: Challenges in creating general purpose AI
videoId: exzPO4hAD9s
---

From: [[everyinc]] <br/> 

The development of truly general-purpose artificial intelligence (AGI) presents significant [[challenges_in_building_ai_tools | challenges]], particularly in defining problems, evaluating performance, and avoiding over-generalization <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Jared, co-founder and CEO of PromptLayer, holds a view that AGI is not as interesting as the practical application of AI, focusing more on how to build with the technology rather than its potential to take over the world <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## Defining the Problem for AI
A core challenge in creating general-purpose AI is defining the problem to be solved <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Even with the best tools, the exact scope of a problem needs to be defined, which is considered an "irreducible" part of the process <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### The "Irreducible" Part
The concept of "computational irreducibility" suggests that while many parts of a problem can be collapsed or sped up, there remains a part that cannot be simplified or factored <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. In the context of AI, this means that even with an amazing AI capable of solving any problem, the hardest part is determining what to instruct it to solve <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This is because certain operations require the system to "run out the reality" to find out what happens, rather than being predicted by a formula <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

For instance, an AI secretary booking flights faces "irreducible" differences based on user preferences like aisle vs. window seat, or non-stop vs. business class with a stop, meaning there's no single perfect solution <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. This highlights that there isn't "one prompt to rule them all" or "one data set to rule them all" even within a specific domain <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Limitations of General Purpose System Prompts
System prompts for general-purpose AI tools like ChatGPT or Anthropic are often criticized as "bad" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>. These prompts lack specific use cases for evaluation, leading to "prompt debt" where more and more instructions are tacked on (e.g., "do this if they say this, don't say this," or ensuring diversity in historical figures) <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>, <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>. This approach can lead to over-fitting and a lack of conciseness <a class="yt-timestamp" data-t="00:42:53">[00:42:53]</a>.

For general-purpose AI, a better approach might involve having different prompts for different types of tasks and routing requests accordingly, despite latency concerns <a class="yt-timestamp" data-t="00:43:39">[00:43:39]</a>. This is exemplified by Snapchat AI, which uses multiple models to route user queries based on context <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.

## Evaluating General Purpose AI
[[challenges_and_strategies_in_ai_evaluation | Challenges and strategies in AI evaluation]] are amplified for general-purpose systems. Defining "better" is highly contextual and depends on how that definition is made <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. This contextual dependency makes generalized research papers about prompting strategies less useful, as prompting often relies on a "scientific method" of trial and error with good data sets and frameworks for iteration <a class="yt-timestamp" data-t="00:22:52">[00:22:52]</a>.

AI labs often focus on problems with clear "ground truth" for evaluation, such as math problems <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>. However, this raises questions about evaluating things without ground truth, like summarizing calls or therapy responses, where human heuristics and specific characteristics must be identified and mimicked <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>. Generalized evaluation benchmarks are often not trusted due to this lack of generic applicability <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

## The Role of Language Models (LLMs)
LLMs are described as fundamentally solving the problem of going from human language to data and vice versa <a class="yt-timestamp" data-t="00:57:43">[00:57:43]</a>. While they excel at processing natural language, integrating real-world data and common sense remains a challenge <a class="yt-timestamp" data-t="00:58:12">[00:58:12]</a>. For example, an LLM might know who John May's mother is, but if asked "Who is Cynthia May?" (John May's mother), it might not connect the information without explicit prompting or a pre-defined knowledge store <a class="yt-timestamp" data-t="00:56:29">[00:56:29]</a>. This suggests that current LLMs, while capable in certain domains, are not yet true AGI due to these fundamental gaps in common knowledge and context <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>.

The challenge of creating a "good summary" for an AI illustrates this further. What constitutes "most important" is context-dependent and varies by person, making a generically best summary impossible <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>. Current language model summaries can be "very Adept at saying a lot without saying anything," highlighting a limitation in their understanding of human intent and context <a class="yt-timestamp" data-t="00:50:33">[00:50:33]</a>.

## Conclusion
While the "hacker energy is back" and it's easier to build specific AI tools now <a class="yt-timestamp" data-t="00:38:41">[00:38:41]</a>, the path to general-purpose AI is fraught with fundamental [[the_challenges_and_potential_benefits_of_ai_development_and_regulation | challenges and potential benefits of AI development and regulation]]. These include the inherent difficulty of defining problems in an open-ended way, the limitations of current evaluation metrics for broad applications, and the contextual sensitivity that still requires human domain expertise to guide and refine AI outputs <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.