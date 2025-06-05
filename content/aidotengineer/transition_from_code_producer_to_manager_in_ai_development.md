---
title: Transition from code producer to manager in AI development
videoId: 9u6xvcNJaxc
---

From: [[aidotengineer]] <br/> 

The emergence of Generative AI (GenAI) has significantly impacted the software development workflow, leading to a shift in how developers interact with code creation <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. As technology advances from simple Large Language Models (LLMs) to sophisticated AI agents and even teams of agents, the concept of "AI native" development is gaining prominence <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This new paradigm introduces a different set of practices, redefining developers' tasks <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## The AI Native Shift

AI's integration into development means that existing tasks are either replaced or enhanced, and entirely new tasks emerge <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This transformation can be distilled into four key patterns, with the developer at the center moving into different roles <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. One of the most significant shifts is the transition from being a code producer to becoming a manager of AI agents <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

## Pattern 1: From Producer to Manager

Historically, developers have been the primary producers of code <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. With AI agents now capable of producing code, the developer's role evolves to managing these agents <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This shift is already evident, as developers spend less time coding and more time reviewing <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. This increased review time often comes with a higher cognitive load because the "thinking work" now occurs during the review phase <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Reducing Cognitive Load in Review

To mitigate the increased cognitive load, new approaches to code review are emerging:
*   **Summarized Review Views** Instead of clunky diff views or verbose chat views, new tools can strip down the review to a summary, allowing developers to quickly approve or reject changes <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Step-by-Step Reviews** For multi-file changes, breaking down the review into a guided, step-by-step flow helps manage complexity <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Visual Reviews** Reviewing diagrams of changes can be significantly easier and faster than reviewing text, aiding in spotting errors and understanding impact <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Moldable Development Environments** Integrated Development Environments (IDEs) are expected to adapt to specific code review needs or domain specifics, moving beyond an endless stream of text <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This adaptation further helps to reduce cognitive load <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

### Managing AI Agent Behavior

The management role also extends to guiding and controlling the AI agents themselves:
*   **Auto-Committing with Review Options** Some systems propose auto-committing code, allowing developers to review and revert if necessary, rather than requiring a manual "yes to commit" step <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This relies on heuristics to assess risk or impact <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Checkpoints for Longer-Running Agents** For agents that operate over extended periods, checkpoints allow developers to jump in at specific points to regenerate or modify the agent's thought process without re-running the entire generation <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This prevents repeated reviews of the same iterations <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Setting Constraints and Permissions** Developers, much like managers, can set rules for AI agents, such as locking files or defining permissions, to establish "guardrails" for what the AI can and cannot do <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This aligns with [[best_practices_for_building_ai_systems | best practices for building AI systems]].
*   **Cost Monitoring** As agents run for longer periods, developers must monitor the cost associated with their operations, as tasks are no longer just about a single prompt <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. This relates to [[scaling_ai_agents_in_production | scaling AI agents in production]] and [[implementing_ai_in_enterprises | implementing AI in enterprises]].

Ultimately, this first pattern highlights that developers are transitioning from performing the direct work to managing a team of AI agents <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This aligns with broader themes in [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] and [[building_and_improving_ai_agents | building and improving AI agents]].

This shift in role also opens the door for other patterns in AI native development, such as moving from implementation to specifying intent, from delivery to discovery, and from data to knowledge <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a> <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This broader understanding demonstrates that AI's impact extends far beyond merely accelerating typing <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.