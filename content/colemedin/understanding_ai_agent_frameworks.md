---
title: Understanding AI agent frameworks
videoId: XIIIXd5VqO0
---

From: [[colemedin]] <br/> 

While prompt engineering has often been overemphasized, certain techniques are crucial for developing [[building_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>, <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>, <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Although prompt engineering saw a decline in obsessive focus in 2023, it remains a point of excessive attention for many <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The key is to focus on foundational knowledge and practical application, rather than trying to master every minor technique <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Essential Prompt Engineering for AI Agents

A recommended resource for learning prompt engineering is the "Prompt Engineering Guide," which is designed to cut through the unnecessary "fluff" <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. When learning about prompt engineering, dedicating three to five hours is sufficient to grasp the basics, after which the focus should shift to actually building applications <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

The most important techniques for [[building_ai_agents | AI agents]] include:

*   **Basic Prompting Techniques**
    *   Zero-shot prompting <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
    *   Few-shot prompting <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
    *   Chain-of-Thought prompting <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
    *   Self-consistency <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
    *   General knowledge prompting <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
    *   Prompt chaining <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

*   **Advanced Techniques for Agents**
    *   **ReAct Prompting (Reason + Act Framework)**: This is a core [[frameworks_and_tools_for_ai_agent_development | framework]] used by agents to reason with themselves and interact with tools <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. It enables an agent to decide when to invoke a tool, process its response, and communicate with the user <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   **Reflection (Self-reflection)**: This technique allows an [[understanding_ai_agents | AI agent]] to improve its own responses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

The "Prompt Engineering Guide" also covers topics like a Prompt Hub, different LLM models, LLM research findings, and a section specifically on LLM agents <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>, <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>, <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. By focusing on these fundamental and agent-specific techniques, users can achieve 95-99% of desired AI functionalities, especially when [[building_fullscale_ai_agents | building fullscale AI agents]] <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Simple Prompt Template for Complex Agents

A straightforward [[creating_custom_ai_agent_frameworks_with_mcp | framework]] for creating complex and concise prompts, particularly for [[building_ai_agents | AI agents]], involves four main categories <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>, <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>:

1.  **System Prompt**: Defines who the agent is and describes its characteristics (e.g., "intuitive," "friendly," "skilled") <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>, <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
2.  **Goal**: States the agent's primary objective (e.g., "help the user manage their tasks") <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
3.  **Things to Do**: Lists specific actions or behaviors the agent should exhibit <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
4.  **Things Not to Do**: Outlines behaviors or outcomes the agent should avoid, such as preventing specific hallucinations <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>, <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

This simple structure effectively defines a clear goal for an agent without requiring overly complex prompt engineering <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.