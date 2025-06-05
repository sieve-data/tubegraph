---
title: Personal private AI agents
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

The speaker, a co-founder of PyTorch and an employee at Meta, focuses on the topic of personal local AI agents <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a> <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Their interest stems from observing the personal productivity benefits of AI tools, such as Swyx's AI news aggregator <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. Additionally, their work in robotics, where robots act as agents, contributes to their understanding of AI agents <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. The core premise is that personal agents, due to their significant agency in taking actions and extensive access to personal context, are best kept local and private <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

## Defining an AI Agent
An AI agent is characterized by its ability to act in the world; it possesses "agency" <a class="yt-timestamp" data-t="03:05:05">[03:05:05]</a>. An aggregator, such as Swyx's AI news, is not considered an agent because it gathers context but cannot take actions <a class="yt-timestamp" data-t="03:01:01">[03:01:01]</a>.

### The Critical Role of Context
A highly intelligent agent without the correct context is essentially useless <a class="yt-timestamp" data-t="03:23:05">[03:23:05]</a>. For example, a personal agent might inaccurately report on prescription renewals if it lacks access to text messages, or provide incorrect financial information if it doesn't have access to all bank accounts <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a> <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. Without sufficient context, a personal agent becomes irritating and unreliable, making its utility questionable <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

## Why Personal Agents Should Be Local and Private
The speaker argues against running personal AI agents in the cloud through large tech companies, highlighting several critical reasons for keeping them local and private <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>:

> [!important] Reasons for Local and Private Agents
> *   **Control and Trust**: Unlike simple digital services like email, which have predictable mental models (e.g., "email in, reply out") <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>, AI agents possess a powerful and potentially unpredictable action space. If an agent can auto-reply on your behalf, you might lose trust if you don't understand its behavior or worry about worst-case actions (e.g., replying inappropriately to your boss) <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a> <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.
> *   **Monetization Risks**: Cloud services might monetize personal data or actions. For instance, an agent handling shopping queries could be influenced to only recommend products from companies offering kickbacks, compromising user control and interests <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
> *   **Decentralization**: Current digital ecosystems often create "walled gardens" that limit interoperability <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. Relying on one ecosystem for a personal agent that performs diverse actions could lead to dependence and restricted functionality <a class="yt-timestamp" data-t="10:01:00">[10:10:00]</a>.
> *   **Privacy and "Thought Crimes"**: A personal agent intimately augmenting your life might be privy to thoughts or queries you would never voice publicly <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. Using a cloud provider carries the risk of mandated logging and safety checks, potentially exposing private "thought crimes" and leading to unintended consequences <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a> <a class="yt-timestamp" data-t="11:42:00">[11:42:00]</a>.

## Practical Considerations for Running Personal Private Agents
To provide an agent with all the necessary personal context (e.g., seeing everything you see, hearing everything you hear), current wearable technologies lack sufficient battery life <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a> <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. Running an agent on a phone in the background is also limited by ecosystem restrictions, particularly with Apple <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a> <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

A feasible solution currently is to use a device like a Mac Mini at home <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>. It has no battery life issues, can remain connected to the internet, allows logging into all services, and can access Android ecosystems because Android is open <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a> <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>.

## [[challenges_in_creating_personal_ai_agents | Challenges in Creating Personal AI Agents]]
While local and private agents are ideal, there are significant [[developing_and_optimizing_ai_agents | challenges in their development]].

### Technical Challenges
*   **Local Model Inference**: Running local models, which are key [[components_of_ai_agents | components of AI agents]], is currently slow and limited compared to cloud services <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a> <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>. Although this is rapidly changing, the latest, unquantized models remain very slow <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>. Open-source projects like `ollama` and `llm` (possibly meant to be `llama.cpp` or a similar project from `sg_lang` context) are making progress in this area <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Open Multimodal Models**: While improving, open multimodal models are not yet great, particularly in:
    *   **Computer Use**: Even advanced closed models struggle with computer vision tasks and frequently break <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.
    *   **Specificity and Taste**: Models often provide generic recommendations and struggle to understand specific, nuanced user preferences for things like shopping, relying more on text matching than visual identification <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a> <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.

### Research and Product Challenges
*   **Catastrophic Action Classifiers**: A major gap exists in developing robust systems to identify and prevent "catastrophic actions"—irreversible or highly damaging actions an agent might take (e.g., buying a car instead of laundry detergent) <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a> <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a> <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. More research is needed to enable agents to identify such actions and notify users before proceeding <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>. This directly impacts [[evaluating_ai_agents_and_assistants | evaluating AI agents]].
*   **Open-Source Voice Mode**: Robust open-source voice mode capabilities are still in early stages, which is crucial for a seamless personal agent experience <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## Optimism for Open Models
Despite the [[challenges_in_creating_personal_ai_agents | challenges in creating personal AI agents]], the speaker is bullish on their future because:
*   **Compounding Intelligence**: Open models are advancing in intelligence faster than closed models because of distributed resources and coordinated efforts across the community <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a> <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.
*   **Open Source Advantage**: Similar to Linux and other major open-source projects, once a critical mass of coordination is achieved, open source tends to achieve unprecedented success and outpace proprietary solutions <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>. This suggests that open models will eventually become superior to closed models in terms of investment efficiency <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

## Related Initiatives
*   **Open Reasoning Data**: Ross Taylor's work on Galactica, an open science model, led to the release of open reasoning data, which aims to bridge the reasoning gap between open and closed models <a class="yt-timestamp" data-t="19:14:00">[19:14:00]</a> <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>.
*   **PyTorch**: PyTorch is actively working on enabling local agents and addressing the technical challenges involved <a class="yt-timestamp" data-t="19:27:00">[19:27:00]</a>. They are also hiring for AI and systems engineers <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.
*   **LlamaCon**: An event, LlamaCon, is scheduled for April 29th, promising new developments related to Llama <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>.