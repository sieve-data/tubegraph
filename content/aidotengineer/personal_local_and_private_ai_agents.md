---
title: Personal local and private AI agents
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

## Introduction
The discussion on [[ai_agents_beyond_chatbots | AI agents]] begins with an exploration of why personal, local, and private agents are crucial for enhancing individual productivity and control <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The speaker, a co-founder of PyTorch and an individual working at Meta, emphasizes the benefits of such agents, drawing from his personal experience and work in robotics <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.

The initial inspiration for exploring [[developing_ai_agents_for_productivity | AI agents]] came from the speaker's use of "Swix's AI news," which saved him significant time by aggregating AI news, demonstrating the potential for AI to augment daily life <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>. His work in robotics, where robots are inherently agents acting in the world, further solidified his interest in understanding [[building_effective_ai_agents | AI agents]] more deeply <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Defining an AI Agent
An agent is defined as something that possesses "agency," meaning it can actively take actions in the world <a class="yt-timestamp" data-t="03:05:07">[03:05:07]</a>. If a system can only gather context and process information but cannot act, it is not considered an agent <a class="yt-timestamp" data-t="03:16:03">[03:16:03]</a>.

### The Importance of Context
A highly intelligent agent without the right context is largely useless <a class="yt-timestamp" data-t="03:21:09">[03:21:09]</a>. For a personal agent to be effective, it needs access to a broad range of personal information <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

**Examples of Context Failure:**
*   An agent unable to confirm a prescription renewal because it lacked access to iMessage, only having Gmail, WhatsApp, and calendar access <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   An agent giving incorrect financial information because it only had access to one bank account, missing a Venmo deposit <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

When a personal agent lacks full context, it becomes irritating and unreliable, making it effectively useless because users cannot trust its information or actions <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

## Why Personal, Local, and Private Agents?
The key takeaway is that personal agents, due to their deep access to a user's life context, are best kept local and private <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Challenges in Providing Comprehensive Context
*   **Wearables:** While ideal for providing "see everything you see and listen to everything you hear" context, current wearable technology lacks sufficient battery life <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.
*   **Phones:** Running agents in the background on phones is restricted by ecosystem limitations, such as Apple's asynchronous execution policies <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.
*   **Proposed Solution:** A Mac Mini placed at home, connected to the internet, can run agents asynchronously without battery life concerns. It can log into all services and access open ecosystems like Android <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

### Arguments Against Cloud-Based Agents
1.  **Control and Predictability:**
    *   Trust in digital services (like cloud email) stems from a simple, predictable mental model (e.g., email in, reply out) <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>.
    *   As an agent's "action space" becomes more powerful and unpredictable (e.g., auto-replying to your boss, making purchases based on kickbacks), users become uncomfortable trusting services they don't fully control <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
    *   Personal life is intimate, and users desire control over how an agent acts on their behalf <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

2.  **Decentralization:**
    *   Current digital ecosystems are often "walled gardens" that resist interoperability <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
    *   Relying on one ecosystem for a personal agent that performs diverse actions across daily life could lead to undesirable lock-in <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Local agents promote decentralization and interoperability.

3.  **[[confidential_ai_and_its_impact | Confidential AI and its impact]] (Thought Crimes):**
    *   Users might ask a personal agent things they would never say out loud <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
    *   Cloud providers, even with enterprise-grade contracts, are often legally mandated to perform logging and safety checks <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
    *   This poses a risk of being "prosecuted or persecuted for thought crimes," making local agents preferable for the most personal [[implementing_ai_agents_in_daily_operations | augmentation]] <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

## Challenges in [[building_effective_ai_agents | Building Effective AI Agents]]
### Technical Challenges
*   **Local Model Inference Speed:** While projects like VM and SG Lang (built on PyTorch) enable running local models, inference is currently slow and limited compared to cloud services <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>. However, this is rapidly improving; distilled models can run fast, but the latest, unquantized models remain slow <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. This is expected to self-resolve <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.

### Research and Product Challenges
*   **Open Multimodal Models:** Current open multimodal models are "good but not great," particularly for computer use, often breaking <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.
*   **Visual Understanding for Shopping:** Models struggle with specific visual identification in shopping queries, often relying on text matching rather than precise visual recognition <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   **Catastrophic Action Classifiers:** A significant gap exists in the ability of agents to identify "catastrophic actions" – irreversible or highly damaging actions <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>. While many actions are harmless or reversible, critical actions like purchasing a Tesla instead of Tide Pods require robust identification and user notification to build trust <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. More research is needed in this area for [[evaluating_ai_agents_and_assistance | evaluating AI agents and assistance]] reliably.
*   **Voice Mode:** Open-source voice mode is barely present, but essential for natural interaction with personal local agents <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## Optimism for Open Models
Despite the challenges, there is strong bullishness on the future of open models for personal agents <a class="yt-timestamp" data-t="17:06:00">[17:06:00]</a>.
*   **Compounding Intelligence:** Open models are compounding intelligence faster than closed models because many independent entities contribute to their improvement in a coordinated manner <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>. This has been demonstrated by the rapid advancements seen with models like LLaMA, Mistral, Guac, and DeepSea <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>.
*   **Open Source Advantage:** Similar to Linux and other projects, open source, once it achieves a critical coordinated mass, tends to win in unprecedented ways <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>. This suggests open models will become superior to closed models in terms of performance per dollar of investment <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

## Future Outlook
PyTorch is actively working on enabling local agents and addressing their technical challenges <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. Additionally, efforts are underway to plug the reasoning gap between open and closed models through open reasoning data <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a>. The community is also looking forward to events like LLaMA Con on April 29th, where new developments in LLaMA will be shared <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>.