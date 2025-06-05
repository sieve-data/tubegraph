---
title: Role of reasoning models in application development
videoId: y6L5RkEqQ8g
---

From: [[aidotengineer]] <br/> 

Reasoning models play a crucial role in modern AI application development, particularly for handling complex requests and providing detailed, well-thought-out responses. These models allow applications to go beyond simple, direct answers, offering deeper insights and planning capabilities <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Addressing Complexity with Reasoning Models

Traditional AI applications, like early versions of ChatGPT, can sometimes feel disjointed, as if different functionalities were developed by separate teams without integrated user experience <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This often results in a "science fair full of potential options" rather than a cohesive product <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. To overcome this, a key improvement involves smartly choosing the right model based on the user's request <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

For complex tasks, a system can hand off to a [[reasoning_models_and_their_unique_prompting_requirements | reasoning model]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This allows the AI to:
*   **Plan intricate operations**: For example, when asked to "refactor this entire codebase to use Flutter instead," a reasoning model detects the complexity and writes a detailed plan to ensure the code functions correctly <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This demonstrates an implicit form of [[chain_of_thought_reasoning_in_ai | Chain of Thought reasoning]].
*   **Provide in-depth information**: If a user requests "details and pros and cons" on a topic, the system can utilize a reasoning model to generate a more comprehensive and detailed response <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Implementation and Triggers

The integration of reasoning models can be achieved using "off-the-shelf APIs" and "tool calls" <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Heuristics can be employed to determine when to engage a reasoning model <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

Key triggers for using a reasoning model include:
*   **Complex requests**: When an [[AI Model Considerations | AI model]] detects a query requiring significant planning or multi-step execution <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Deep dives**: If a user expresses a desire to "go deeper on a topic" <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>, such as asking for the history of a location like Yosemite National Park <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Requests for analysis**: Queries asking for detailed breakdowns, advantages, or disadvantages of a subject <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

By leveraging tool calls, developers can send details to the reasoning model and then integrate its sophisticated response back into the application or directly to the client <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This approach highlights the ongoing [[evolution_of_ai_models_and_their_application | evolution of AI models and their application]] in creating more intelligent and user-friendly systems, reinforcing the [[importance_of_domainspecific_models_despite_advancements | importance of domain-specific models]] or specialized models for particular tasks, and underscoring the [[role_of_domain_experts_in_ai_system_development | role of domain experts in AI system development]] for defining these specialized tasks.

The underlying framework of such applications relies on sophisticated [[tool_usage_and_development_in_ai_frameworks | tool usage and development in AI frameworks]], contributing to robust [[ai_application_frameworks_and_architecture | AI application frameworks and architecture]].