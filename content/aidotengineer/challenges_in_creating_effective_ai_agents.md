---
title: Challenges in creating effective AI agents
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

AI agents, particularly personal ones, hold significant potential for augmenting daily life, but their effective and trustworthy development faces several [[Challenges in AI agent development | challenges]]. The speaker, a co-founder of PyTorch, emphasizes the importance of local and private AI agents due to concerns about control, privacy, and decentralization <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Defining an AI Agent

An AI agent is characterized by its ability to act in the world and possess agency <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. If a system can only gather context or information but cannot take actions, it is not considered an agent <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## The Critical Role of Context

A primary [[Challenges in AI agent development | challenge]] in [[building effective AI agents | building effective AI agents]] is ensuring they have sufficient context. An intelligent agent without the right context is considered "useless" or "as good as a bag of rocks" <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Examples of Context Limitations
*   **Partial Information**: An agent might fail to accurately answer a personal query, like whether a prescription was renewed, if it lacks access to all relevant communication channels (e.g., iMessage vs. Gmail) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Incomplete Financial Data**: Similarly, an agent might misinform about finances if it only accesses one bank account but not other platforms like Venmo <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

Without comprehensive context, a personal agent becomes unreliable and "irritating to use," as users cannot predict when it will be useful or provide accurate information <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For an agent to be truly useful, it must achieve a high level of reliability and predictability <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Practical Considerations for Local Agents

Achieving comprehensive context for a personal agent ideally means it should "see everything you see and listen to everything you hear" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. However, this presents [[technical_challenges_in_ai_agent_development | technical challenges]]:

*   **Wearable Devices**: Current wearable technology lacks sufficient battery life to continuously provide context to an AI <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Smartphones**: Running agents persistently in the background on phones is limited by ecosystem restrictions, particularly on platforms like Apple <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Feasible Local Device**: A Mac Mini, connected to the internet and running asynchronously at home, is suggested as a feasible device for running personal AI agents due to no battery issues and access to various services and Android ecosystems <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>, <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Arguments for Local and Private Agents

The speaker strongly advocates for local and private personal agents over cloud-based services for several reasons, highlighting key [[challenges_and_benefits_of_ai_agents | challenges and benefits of AI agents]] in a cloud environment:

1.  **Trust and Predictability**: Unlike simple digital services like email, which have predictable behaviors ("email in, reply out"), AI agents possess a powerful and unpredictable action space <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   **Loss of Control**: Users become uncomfortable when an AI agent can take significant actions (e.g., auto-replying to a boss with inappropriate content) without explicit user control <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   **Monetization Incentives**: Cloud service providers might monetize by influencing agent actions (e.g., directing shopping queries to partners offering kickbacks), eroding user trust and control over personal decisions <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

2.  **Decentralization**: Relying on one ecosystem for a personal agent can lead to "walled gardens" and lack of interoperability, which is problematic for an agent that needs to interact with various aspects of a user's daily life <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

3.  **Privacy and "Thought Crimes"**: AI agents, especially those augmenting users intimately, may be exposed to highly personal thoughts or queries that users would not vocalize publicly <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
    *   **Logging and Safety Checks**: Cloud providers, even with enterprise-grade contracts, are legally mandated to perform logging and safety checks, potentially exposing sensitive or "thought crime" data <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
    *   **Risk of Persecution**: The speaker expresses a desire to avoid scenarios where personal thoughts or queries could lead to prosecution or persecution, making local agents a safer choice <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

## Technical and Research [[Challenges in AI Agent Development | Challenges]]

Even with the conviction for local agents, significant [[technical_challenges_in_ai_agent_development | technical challenges in AI agent development]] remain:

*   **Local Model Inference**:
    *   Running local models, even with projects like `ollama` and `sglang` (built on PyTorch), is currently "slow and limited" compared to cloud services <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   While smaller, distilled models run faster, the latest unquantized models remain very slow locally <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. This is expected to improve over time <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

*   **Multimodal Models**:
    *   Open multimodal models are "good but not great," especially for computer use, and even closed models frequently "break" <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
    *   They are not adept at understanding specific visual tastes in shopping, often relying on text matching rather than true visual identification <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>, <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

*   **Catastrophic Action Classifiers**: A major gap exists in developing robust classifiers to identify and prevent "catastrophic actions" <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
    *   Many agent actions are harmless and reversible, but some, like purchasing a Tesla instead of Tide Pods, are disastrous <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   More research is needed to enable agents to identify such actions before taking them and notify users instead <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>. Trust in agents, whether personal or cloud-based, hinges on improving this capability <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

*   **Voice Mode**: Open-source voice mode for local agents is "barely there," despite being a crucial feature for natural interaction <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>, <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

## Optimism for the Future

Despite these [[challenges_and_solutions_in_building_ai_agents | challenges]], the speaker remains optimistic, particularly about open models. Open models are seen as "compounding in intelligence faster than closed models" due to coordinated improvement across a broader community <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This phenomenon, observed with projects like Linux, suggests that once open source reaches a critical mass, it can achieve unprecedented success <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>.

The speaker highlights ongoing efforts, including PyTorch's work on enabling local agents by addressing [[technical_challenges_in_ai_agent_development | technical challenges]] <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>, and the release of open reasoning data to bridge the reasoning gap between open and closed models <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.