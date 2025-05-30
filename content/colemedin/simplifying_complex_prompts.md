---
title: Simplifying complex prompts
videoId: XIIIXd5VqO0
---

From: [[colemedin]] <br/> 

There is a prevalent over-obsession with [[critique_of_excessive_focus_on_prompt_engineering | prompt engineering]], with many believing it to be the most crucial aspect of AI and a lucrative career path <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. However, [[importance_of_prompt_engineering | prompt engineering]] is fundamentally simple and not worth an extensive deep dive <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Although it was a fad in 2023, many still focus on it excessively <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The goal is to cut through the fluff and demonstrate that it's not the most important element in AI development <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Recommended Resource & Time Investment

The "Prompt Engineering Guide" is a highly recommended and potentially sole resource needed for learning [[importance_of_prompt_engineering | prompt engineering]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. While some techniques are beneficial, much of what is discussed in the field is unnecessary fluff <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

It's advisable to spend only about 3 to 5 hours studying [[importance_of_prompt_engineering | prompt engineering]] before moving on to building projects <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Avoid spending 20, 40, or even 100 hours attempting to master every technique or craft the perfect prompt for every LLM interaction or [[building_complex_agent_systems | AI agent]] build <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Key Prompt Engineering Techniques

Not all techniques need to be learned; focusing on a few basic, crucial ones is sufficient <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Essential [[recommended_techniques_for_prompt_engineering | techniques for prompt engineering]] include the first six basic ones:
*   Zero-shot prompting <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Few-shot prompting <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Chain of Thought prompting <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Self-consistency <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   General knowledge prompting <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Prompt chaining <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

Additionally, "React prompting" (Reason + Act framework) is highly recommended <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This framework is used by [[building_complex_agent_systems | agents]] when they reason with themselves and interact with tools on your behalf <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. It forms the core of [[building_complex_agent_systems | AI agents]]' ability to reason about invoking tools and relaying responses to users <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

Self-reflection, where an AI can improve its own response, is also a critical technique <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. These two (React and Reflection) along with the initial six basic ones are the primary focus areas <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## A Simple Template for Complex Prompts

A practical four-category framework for creating concise and clear prompts that define a goal for an agent includes <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>:

1.  **System Prompt**: Defines who the agent is and describes it with adjectives (e.g., "intuitive," "friendly," "skilled") <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This is analogous to [[dynamic_system_prompts_and_dependencies_in_pantic_ai | dynamic system prompts]].
2.  **Goal**: States the agent's objective (e.g., "Your goal is to help the user manage their tasks") <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Things to Do**: A list of actions the agent should perform <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
4.  **Things Not to Do**: A list of actions or behaviors the agent should avoid, useful for preventing specific hallucinations or niche issues <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

This straightforward structure simplifies the creation of complex prompts, eliminating the need for overly intricate prompt engineering <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Mastering these basics enables 95% to 99% of desired AI functionalities, particularly for [[building_complex_agent_systems | AI agents]], without relying on complex hacks or jailbreaks <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.