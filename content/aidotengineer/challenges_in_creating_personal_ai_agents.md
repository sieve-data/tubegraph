---
title: Challenges in creating personal AI agents
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

Developing personal AI agents presents multifaceted [[challenges_in_developing_ai_agents | challenges]], ranging from ensuring their reliable operation and access to comprehensive personal context, to navigating privacy concerns and technical limitations for local deployment <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Defining an AI Agent
An AI agent is characterized by its ability to act in the world and possess "agency" <a class="yt-timestamp" data-t="03:05:01">[03:05:01]</a>. Unlike an aggregator, which only gathers and processes context, an agent can take actions on a user's behalf <a class="yt-timestamp" data-t="03:01:01">[03:01:01]</a>. For example, "swix is AI news," an AI news aggregator, is not considered an agent because it cannot act in the world <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Robotics, on the other hand, embodies agents that act in the world <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## The Critical Role of Context
A highly intelligent agent without the right context is largely useless <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
*   **Misinformation due to limited access**: An agent tasked with checking prescription renewal might lie if it only has access to Gmail, WhatsApp, and calendar, missing a text message from a pharmacy on iMessage <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Similarly, an agent with access to only one bank account might misreport finances if money arrived via Venmo, which it cannot see <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **User Frustration**: A personal agent lacking sufficient context becomes irritating to use, making its utility unreliable. Users will question its accuracy and feel compelled to verify its outputs <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   **Reliability**: For an agent to be truly useful, it must achieve a certain level of [[challenges_in_building_reliable_ai_agents | reliability]] and predictability where the user trusts its correctness <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.

The ideal scenario for providing context would be for the AI to "see everything you see and listen to everything you hear" <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

## Why Personal Agents Should Be Local and Private
There are several compelling reasons to keep personal AI agents local rather than relying on cloud services <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>:

### 1. Control and Predictability
Unlike simple digital services like cloud email, where the mental model is straightforward (email in, reply out), AI agents can take powerful and unpredictable actions <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.
*   **Unforeseen Actions**: If an email service were to auto-reply on your behalf, you would be uncomfortable due to the potential for catastrophic actions, such as sending a nasty reply to your boss <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
*   **Monetization Conflicts**: Cloud services must monetize, raising concerns that an agent might prioritize purchases from partners offering kickbacks rather than acting purely in the user's best interest <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
*   **Intimacy**: Personal agents are so intimate to a user's life that control over their behavior is paramount <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

### 2. Decentralization
Current digital ecosystems are often "walled gardens" that resist interoperability <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. Relying on one ecosystem for a personal agent that performs diverse actions across your daily life is risky and undesirable <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Decentralized, local agents could become the norm <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.

### 3. Protection from "Thought Crimes"
An intimate personal agent might be asked questions that users would never voice publicly <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. There's a risk that private thoughts or queries, even if deemed harmless, could be logged or used against an individual by cloud providers, especially given legally mandated logging and safety checks in enterprise-grade contracts <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. The speaker expresses a desire to avoid being prosecuted or persecuted for "thought crimes" <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

## Practical Approaches for Local Personal Agents
*   **Wearable Devices**: While ideal for constant context, current wearable devices lack sufficient battery life <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Smartphones**: Running agents on phones in the background is hindered by ecosystem restrictions (e.g., Apple's limitations on asynchronous processes) <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
*   **Mac Mini**: A feasible solution is using a Mac Mini at home. It can run agents asynchronously, has no battery life issues, and can log into various services, including those from open Android ecosystems <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

## Technical [[challenges_in_developing_ai_agents | Challenges in Developing AI Agents]]
Even if the decision is made to go local, technical hurdles remain:

### 1. Local Model Inference
*   **Speed and Limitations**: As of today, local model inference is slow and limited compared to cloud services, even on powerful machines <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. While smaller models (e.g., 20 billion parameters or distilled models) run faster, the latest, unquantized models are very slow locally <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.
*   **Infrastructure**: Projects like VLLM and SGLang, built on [[pytorch | PyTorch]], are helping to run local models <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. This challenge is expected to resolve itself over time <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.

### 2. Research and Product Gaps
*   **Multimodal Models**: Open multimodal models are currently good but not great <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
    *   **Computer Use**: Even advanced closed models struggle with computer use and frequently break <a class="yt-timestamp" data-t="14:28:00">[14:28:00]</a>.
    *   **Visual Understanding and Taste**: Models often provide generic shopping recommendations <a class="yt-timestamp" data-t="14:42:00">[14:42:00]</a>. They struggle to match specific, fine-grained tastes and often rely on text matching rather than accurate visual identification (e.g., confusing a red velvet sofa with oak legs for a green velvet sofa without oak legs) <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>.
*   **Catastrophic Action Classifiers**: There's a significant lack of robust catastrophic action classifiers <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
    *   **Definition**: Catastrophic actions are irreversible or highly damaging actions (e.g., buying a Tesla car instead of Tide Pods) <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.
    *   **Need for Research**: More research is needed to enable agents to identify catastrophic actions *before* taking them, potentially notifying the user instead <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. This is crucial for user trust, whether for personal or cloud agents <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>.
*   **Voice Mode**: [[challenges_in_building_ai_voice_agents | Open source voice mode]] for agents is "barely there" <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>. Voice interaction is desired for personal agents for convenience <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.

## Optimism for Open Models
Despite the [[challenges_with_current_ai_implementation | challenges with current AI implementation]], the speaker remains bullish about the future of personal AI agents due to the rapid advancement of open models <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>. Open models are seen as compounding intelligence faster than closed models because of coordinated, widespread community contributions (e.g., Llama, Mistral, Guac, DeepSeek) <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>. Similar to Linux and other projects, once open-source initiatives achieve a critical mass of coordination, they tend to win in unprecedented ways <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.

[[pytorch | PyTorch]], co-founded by the speaker and funded by Meta, is actively working on enabling local agents by addressing these technical challenges <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a> <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>.