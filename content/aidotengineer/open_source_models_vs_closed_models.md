---
title: Open source models vs closed models
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

This article discusses the advantages and challenges of [[the_role_of_open_source_models_and_community_in_ai_research | open source]] and local AI models, particularly in the context of personal agents, as presented by a co-founder of PyTorch at Meta <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## The Case for Personal Local Agents

The speaker's interest in personal local agents stemmed from observing how AI news aggregators significantly improved personal productivity <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This led to a deeper exploration of [[usage_of_open_ai_models_in_creative_writing_and_companionship | AI agents]] <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### What is an Agent?
An agent is defined as something that can take action in the world, possessing "agency" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. An AI that can only receive context and process information, but cannot act, is not considered an agent <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### The Importance of Context for Agents
A highly intelligent agent without the right context is deemed "as good as a bag of rocks" or "useless" <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. For example, a personal agent might lie about a prescription renewal because it lacked access to all relevant communication channels (e.g., iMessage vs. Gmail) <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. An agent that doesn't have the full context of a user's life will largely be irritating and unreliable, leading to a lack of trust <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Ideally, a personal AI should see everything the user sees and hear everything the user hears to gain sufficient context <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Why Local and Private?
For personal agents, keeping them local and private is crucial due to the immense amount of personal life context they would access <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

*   **Control and Predictability**: Unlike simple digital services like cloud email, which have a predictable "in, reply, out" mental model <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>, an AI agent's action space is powerful and potentially unpredictable <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. Users lose comfort and control when a service can auto-reply or make purchasing decisions on their behalf <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. There's concern that [[commercial_and_enterprise_application_of_open_ai_models | commercial and enterprise application of open AI models]] could prioritize kickbacks over user interest when making shopping queries <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Decentralization**: Current ecosystems often create "walled gardens" that limit interoperability <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. Relying on one ecosystem for an agent that takes diverse actions across daily life might be problematic <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
*   **Privacy of "Thought Crimes"**: An intimate personal agent might be asked questions that a user would never say out loud <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. There's a risk of legal or social ramifications if such personal interactions are logged or exposed by a third-party provider, even with enterprise-grade contracts <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>.

### Feasible Local Device
While wearable AI devices and phone-based agents face battery limitations or ecosystem restrictions (like Apple's asynchronous process limitations) <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, a Mac Mini in the home is suggested as a feasible device for running asynchronous personal agents <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. It avoids battery issues, can log into all services, and can access Android ecosystems <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## Challenges for Open Source and Local Models

Despite the benefits, there are technical and research challenges for local, [[the_role_of_open_source_models_and_community_in_ai_research | open source]] models:

*   **Local Model Inference Speed**: As of today, local model inference is slower and more limited compared to cloud services, even on beefy machines <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. While models like a 20 billion or distilled model can run fast locally, the latest, full unquantized models are "super duper damn slow" <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. However, this is seen as a rapidly improving area that will likely "fix itself" <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. PyTorch is actively working on enabling local agents and addressing these technical challenges <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   **[[multimodal_models_and_omni_models_development | Multimodal models and omni models development]] Quality**: [[the_role_of_open_source_models_and_community_in_ai_research | Open multimodal models]] are good but not yet great, especially for computer use <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Even closed models struggle with tasks like visually identifying specific items based on detailed user tastes, often relying on text matching <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Lack of Catastrophic Action Classifiers**: A significant gap is the inability of agents to reliably identify "catastrophic actions" before taking them <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. While many actions are harmless or reversible (e.g., visiting the wrong Wikipedia link), some, like an agent purchasing a car instead of Tide Pods, are disastrous <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. More research is needed in [[ai_safety_and_model_interpretability | AI safety and model interpretability]], specifically on how agents can better identify and notify users about such high-impact actions <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.
*   **Voice Mode**: [[the_role_of_open_source_models_and_community_in_ai_research | Open source]] voice models are described as "barely there," limiting the desired interaction method for personal agents <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

## Bullish on Open Models

Despite the challenges, the speaker is very optimistic about [[the_role_of_open_source_models_and_community_in_ai_research | open source]] models:

*   **Faster Intelligence Compounding**: [[the_role_of_open_source_models_and_community_in_ai_research | Open models]] are seen to be compounding intelligence faster than closed models <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. While companies like OpenAI and Anthropic improve their own models, [[the_role_of_open_source_models_and_community_in_ai_research | open models]] benefit from coordinated improvement across a broader community <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Power of Open Source Coordination**: Historically, [[the_role_of_open_source_models_and_community_in_ai_research | open source]] projects, once they achieve a critical mass for coordination, begin to win in unprecedented ways (e.g., Linux) <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>. Examples like Llama, Mistral, and Grok (by Deep Sea) are cited as evidence that [[the_role_of_open_source_models_and_community_in_ai_research | open models]] are increasingly competing with and potentially surpassing closed models <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
*   **Cost-Effectiveness**: [[the_role_of_open_source_models_and_community_in_ai_research | Open models]] are expected to become better than closed models "per dollar of investment" <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

### Relevant Projects
*   **Galactica**: An [[the_role_of_open_source_models_and_community_in_ai_research | open science model]] that faced early criticism but contributed to making [[general_versus_domain_specific_language_models | science with LLMs]] common <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. Its creator, Ross Taylor, is now working on plugging the reasoning gap between [[the_role_of_open_source_models_and_community_in_ai_research | open and closed models]] by releasing [[the_role_of_open_source_models_and_community_in_ai_research | open reasoning data]] <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **PyTorch**: Actively engaged in enabling local agents and addressing [[scaling_ai_models_and_their_impact_on_development_tools | technical challenges]] <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   **LlamaCon**: An upcoming event on April 29th, suggesting significant developments in the Llama ecosystem <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.