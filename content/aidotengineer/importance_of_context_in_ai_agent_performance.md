---
title: Importance of context in AI agent performance
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

Effective AI agents, particularly personal ones, necessitate comprehensive "life context" to be truly valuable <a class="yt-timestamp" data-t="02:46">[02:46]</a>. Without the appropriate context, a highly intelligent agent is considered useless, akin to a "bag of rocks" <a class="yt-timestamp" data-t="03:21">[03:21]</a>.

## Defining an Agent and the Role of Context

An agent is characterized as something with "agency" that possesses the capability to "act in the world" <a class="yt-timestamp" data-t="03:05">[03:05]</a>. Any system that can only gather information without the ability to take action is not classified as an agent <a class="yt-timestamp" data-t="03:12">[03:12]</a>.

> "A highly intelligent agent without the right context is as good as a bag of rocks, it's like really useless." <a class="yt-timestamp" data-t="03:21">[03:21]</a>

### The Impact of Insufficient Context

When a personal agent operates with incomplete context, it risks providing inaccurate information, leading to user frustration and a breakdown of trust <a class="yt-timestamp" data-t="04:17">[04:17]</a>.

**Examples of Contextual Failure:**
*   **Prescription Renewal:** An agent might falsely report that a prescription has not been renewed because its access is limited to Gmail, WhatsApp, and calendar, while the actual confirmation was received via iMessage from CVS, a source it cannot access <a class="yt-timestamp" data-t="03:30">[03:30]</a>.
*   **Financial Information:** An agent reporting on a bank account balance could be incorrect if funds arrived via Venmo and the agent only has access to a traditional bank account <a class="yt-timestamp" data-t="04:08">[04:08]</a>.

These scenarios underscore that even an agent performing its best with limited information remains unhelpful if it cannot reliably provide accurate details due to missing context <a class="yt-timestamp" data-t="03:55">[03:55]</a>. An agent becomes genuinely useful only when it reaches a certain level of reliability and predictability <a class="yt-timestamp" data-t="04:33">[04:33]</a>.

## Strategies for Providing Context to AI Agents

To ensure an AI agent has the necessary context, one might ideally envision it seeing everything a user sees and hearing everything they hear <a class="yt-timestamp" data-t="05:14">[05:14]</a>. However, this is currently impractical due to limitations like battery life in wearable devices <a class="yt-timestamp" data-t="05:31">[05:31]</a>.

Running an agent on a phone to monitor screen activity and background processes seems plausible, as much of a user's life context resides on their phone <a class="yt-timestamp" data-t="05:43">[05:43]</a>. However, mobile ecosystems, such as Apple, impose significant restrictions on asynchronous background processes, limiting this approach <a class="yt-timestamp" data-t="06:01">[06:01]</a>.

A more feasible current solution involves utilizing a Mac Mini placed in the user's home <a class="yt-timestamp" data-t="06:23">[06:23]</a>. This device can run agents asynchronously without battery concerns, allow logging into all personal services, and access Android ecosystems, which are more open <a class="yt-timestamp" data-t="06:36">[06:36]</a>. This approach enables the comprehensive context gathering crucial for [[building_effective_ai_agents | effective AI agents]].

## Why Local and Private Agents are Preferred for Personal Context

For personal agents that deeply integrate into a user's life, keeping them local and private is crucial due to several factors:

*   **Trust and Predictability:** Unlike simple digital services like email, whose behavior is predictable (email in, reply out), AI agents have a much broader and more unpredictable action space <a class="yt-timestamp" data-t="08:01">[08:01]</a>. Users are uncomfortable with services that can take powerful actions on their behalf without full understanding or control <a class="yt-timestamp" data-t="08:51">[08:51]</a>.
*   **Monetization Concerns:** Cloud-based agents could potentially be monetized in ways that conflict with user interests, such as prioritizing purchases from partners who offer kickbacks <a class="yt-timestamp" data-t="09:09">[09:09]</a>. Local agents ensure the user maintains control over such decisions <a class="yt-timestamp" data-t="09:33">[09:33]</a>.
*   **Decentralization and Ecosystem Lock-in:** Relying on a single ecosystem for a personal agent could lead to "walled gardens" and interoperability issues, similar to existing digital services like maps and email <a class="yt-timestamp" data-t="09:53">[09:53]</a>. A decentralized approach through local agents avoids this lock-in for critical personal functions <a class="yt-timestamp" data-t="10:17">[10:17]</a>.
*   **Privacy and "Thought Crimes":** Users might ask personal agents questions or explore thoughts they would never voice aloud <a class="yt-timestamp" data-t="11:07">[11:07]</a>. Cloud providers, even with enterprise-grade contracts, are subject to legally mandated logging and safety checks, posing a risk of "persecution for thought crimes" <a class="yt-timestamp" data-t="11:36">[11:36]</a>. Local agents mitigate this risk by keeping sensitive interactions private <a class="yt-timestamp" data-t="11:47">[11:47]</a>.

## Current Challenges in Providing Context to AI Agents

While the technical and infrastructural [[technical_challenges_in_ai_agent_development | challenges in AI agent development]] for local agents are rapidly improving, specific issues persist:

*   **Local Model Inference Speed:** Running local models, a key component of agents, is currently slower and more limited compared to cloud services, even on powerful machines <a class="yt-timestamp" data-t="13:13">[13:13]</a>. Although this is changing with smaller, distilled models, the latest unquantized models remain very slow <a class="yt-timestamp" data-t="13:38">[13:38]</a>.
*   **Multimodal Model Quality:** Open multimodal models are not yet great, particularly for computer use, often breaking <a class="yt-timestamp" data-t="14:20">[14:20]</a>. They also struggle with understanding specific user tastes in shopping queries, relying more on text matching than visual identification <a class="yt-timestamp" data-t="14:58">[14:58]</a>.
*   **Catastrophic Action Classifiers:** A significant gap exists in the ability of agents to identify "catastrophic actions" before taking them <a class="yt-timestamp" data-t="15:37">[15:37]</a>. While many actions are reversible or harmless, some, like an unintended purchase, are not <a class="yt-timestamp" data-t="15:48">[15:48]</a>. More research is needed to improve agent reliability in notifying users before executing such critical actions <a class="yt-timestamp" data-t="16:25">[16:25]</a>. This directly impacts [[challenges_in_creating_effective_ai_agents | challenges in creating effective AI agents]].
*   **Voice Mode:** Open-source voice mode for local agents is still underdeveloped, yet crucial for intuitive interaction with personal agents <a class="yt-timestamp" data-t="16:52">[16:52]</a>.

Despite these [[challenges_in_ai_agent_development | challenges in AI agent development]], optimism remains high for [[improving_ai_agent_task_execution | improving AI agent task execution]]. Open models are rapidly compounding intelligence faster than closed models due to coordinated community effort <a class="yt-timestamp" data-t="17:11">[17:11]</a>. This parallels the success seen in other open-source projects like Linux <a class="yt-timestamp" data-t="18:17">[18:17]</a>. The PyTorch project, for instance, is actively working on enabling local agents, addressing many of the technical hurdles <a class="yt-timestamp" data-t="19:27">[19:27]</a>.