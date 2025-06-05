---
title: Proactive AI versus reactive AI
videoId: 2cEGQEllBGc
---

From: [[aidotengineer]] <br/> 

Many current [[challenges_with_current_ai_implementation | AI implementations]] today focus on adding chatbots to products, which often serves as an easy, albeit not always helpful, solution <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Arthur, a product designer at Evil Martians, advocates for challenging conventional thinking about [[implementing_ai_in_enterprises | AI in products]] and adopting [[guidelines_for_developing_proactive_ai_systems | practical principles]] for more effective integration <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Problem with Reactive AI

The prevailing approach involves creating AI assistants that wait for user input, primarily through chat interfaces <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This means users must initiate interaction and explain their needs, which can be time-consuming and disruptive to their workflow <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Such reactive models often lead to generic "how can I help?" questions that don't effectively move work forward <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Inspiration from the Past: Clippy

The concept of proactive assistance isn't new <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The much-maligned Clippy, though often hated for its terrible execution and timing, had the right idea: to anticipate user needs <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. With current technology, the execution can now be done effectively <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Introducing Proactive AI

Proactive AI, in contrast to reactive models, is designed to anticipate user needs without being explicitly asked <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It works by understanding the context of the user's activity and intervening at the precise moment with relevant, contextual questions or suggestions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This integration occurs seamlessly within the natural flow of work, eliminating the need for context switching or extra windows <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Examples of Proactive AI in Action (Tigon)

The [[developing_and_optimizing_ai_agents | AI issue tracker]] Tigon demonstrates proactive AI through different modes:

*   **Suggestion Mode**: This mode tracks what a user is writing in real-time, understands the context, and provides specific, non-generic questions exactly when needed, without a chat window <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, if a user reports a "legality share," the AI immediately asks relevant questions to clarify the issue <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

*   **Action Mode**: This mode allows the AI to identify complexity in a user's input and suggest better ways to organize work <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. For instance, if a user writes an issue that can be split into sub-issues, the AI identifies and suggests splitting it, leveraging previous data and understanding best organizational practices <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This is an example of [[importance_and_progress_of_ai_agents | AI that actually understands]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

*   **Question Plus Action Mode**: This combines the previous two, allowing the AI to not only organize work but also consider timelines and resources, acting like a proactive project manager <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. All interactions happen within the user's workflow, without requiring new interfaces <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Users maintain control, with the ability to easily revert any AI-suggested changes with a single click <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### Core Principles of Proactive AI

To foster proactive AI in products, three simple rules are followed:

1.  AI should supplement user agency, not replace it <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
2.  AI should offer recommendations, never force them <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
3.  AI should be part of the natural workflow, not disrupt it <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Applications Beyond Issue Tracking

The pattern of proactive AI can be powerful across various professional tools:

*   **Code Editors**: AI can proactively monitor for common pitfalls and suggest improvements, which is particularly valuable for developers learning new languages or frameworks <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Design Tools**: Imagine a tool that suggests accessible design improvements as you work, eliminating the need for post-design checks <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Communication Tools**: AI could prepare relevant context before meetings or locate documents mentioned during calls, acting as a personal advisor <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Implementing Proactive AI in Your Products

To start thinking about implementing proactive AI:

1.  **Look for friction points**: Identify areas where users have to stop their work to ask for help; these are opportunities for proactive assistance <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Identify user behavior patterns**: Determine where users commonly need help or what questions they frequently ask; these provide clues for automation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
3.  **Consider context**: Focus on where users get stuck; this is where AI can provide the most help <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

Instead of merely adding chat interfaces, which is a common pitfall in AI strategy, developers should be willing to experiment and challenge the status quo of UI solutions <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. AI interface design is still in its early stages, lacking a fully formed playbook of best practices <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.