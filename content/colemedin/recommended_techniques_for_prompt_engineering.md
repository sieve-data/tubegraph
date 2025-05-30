---
title: Recommended techniques for prompt engineering
videoId: XIIIXd5VqO0
---

From: [[colemedin]] <br/> 

While [[critique_of_excessive_focus_on_prompt_engineering | prompt engineering]] has seen an excessive focus, leading to a misconception that it is the most important part of AI development, it is actually simpler than often portrayed and not worth diving into extensively <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite being considered a "fad" in 2023, many still overemphasize it <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Although [[importance_of_prompt_engineering | prompt engineering]] is important for certain techniques, much of what is taught is considered "fluff" <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Core Resource and Time Commitment

For learning [[importance_of_prompt_engineering | prompt engineering]], a primary resource is the "Prompt Engineering Guide" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This guide is recommended as the sole resource for learning, as it covers essential techniques without unnecessary complexity <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

It is suggested to study [[importance_of_prompt_engineering | prompt engineering]] for only 3 to 5 hours, then focus on building applications <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Spending 20, 40, or 100 hours trying to master all techniques or craft perfect prompts for every LLM interaction or [[building_applications_with_ai_assistance | AI agent]] is unnecessary <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The key is to keep it simple <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Essential Prompt Engineering Techniques

From the "Prompt Engineering Guide," focusing on a few basic but important techniques is sufficient <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Basic Techniques
The first six techniques are highly recommended for learning <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>:
*   Zero-shot prompting <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Few-shot prompting <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Chain of Thought prompting <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Self-consistency <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   General knowledge prompting <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
*   Prompt chaining <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

### Advanced Techniques
Two particularly important frameworks are crucial, especially for [[building_applications_with_ai_assistance | AI agents]]:
*   **React Prompting (Reason + Act)**: This framework is fundamental for how [[building_applications_with_ai_assistance | AI agents]] reason and interact with tools <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It's the core mechanism for an [[building_applications_with_ai_assistance | AI agent]] to determine when to invoke a tool, process its response, and communicate with the user <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Reflection (Self-reflection)**: This enables an AI to improve its own responses <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

Mastering these basic and advanced techniques will allow you to accomplish 95-99% of tasks with AI, particularly when [[building_applications_with_ai_assistance | building things like AI agents]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. There's no need for "crazy little hacks and jailbreaks" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Template for Complex Prompts

For [[simplifying_complex_prompts | creating more complex prompts]] that are concise and clearly define a goal for an [[building_applications_with_ai_assistance | AI agent]], a simple four-category framework is effective <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>:

1.  **System Prompt**: Defines "who you are" by describing the agent with adjectives (e.g., intuitive, friendly, skilled) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. For example, in a [[planning_and_task_management_in_ai_development | task management AI agent]], this section identifies the agent and its attributes <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
2.  **Goal**: States the agent's objective (e.g., "Your goal is to help the user manage their tasks") <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Things To Do**: Lists all desired actions or instructions <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
4.  **Things Not To Do**: Specifies actions or responses to avoid, such as hallucinations or niche behaviors <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

This straightforward structure proves very effective and avoids over-complicating [[simplifying_complex_prompts | prompt engineering]] <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The overall message is to focus on [[simplifying_complex_prompts | simplicity]] and practical application rather than excessive detail in [[importance_of_prompt_engineering | prompt engineering]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.