---
title: Technical challenges in AI agent development
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

AI agents, particularly personal ones, hold significant potential for augmenting daily life by taking actions on a user's behalf and leveraging extensive life context [00:02:40]. However, there are notable [[challenges_in_ai_agent_development | challenges]] in their development, especially when aiming for local and private operation.

## What is an AI Agent?
An AI agent is defined as something that can take action in the world [00:03:05]. Unlike an aggregator, which only gathers context and processes information, an agent possesses "agency" and can perform actions [00:03:05]. For instance, a news aggregator like Swix's AI news is not an agent because it cannot act [00:03:01].

A highly intelligent agent becomes largely useless without the appropriate context [00:03:21]. If an agent lacks access to relevant information sources (e.g., iMessage for prescription renewals [00:03:32], Venmo for financial transactions [00:04:08]), its responses can be unreliable and irritating, making it difficult for users to trust its utility [00:04:17].

## Why Local and Private Agents?
There are several compelling reasons to advocate for local and private personal AI agents over cloud-based services:

*   **Control and Trust:** Traditional digital services like cloud email operate on simple, predictable mental models (e.g., "email in, reply out") [00:08:01], fostering trust. However, AI agents have a powerful and often unpredictable action space [00:08:55]. Users may become uncomfortable if an agent can take actions on their behalf without full control, such as auto-replying to a boss inappropriately [00:08:31]. Furthermore, online services may prioritize monetization, potentially leading agents to make biased decisions (e.g., recommending products that offer kickbacks) [00:09:09]. Given the intimate nature of personal data, maintaining control is crucial [00:09:28].
*   **Decentralization:** Centralized ecosystems often create "walled gardens" that limit interoperability [00:09:55]. Relying on one ecosystem for a personal agent that performs diverse actions in daily life could lead to undesirable dependencies and restrictions [00:10:04].
*   **Privacy ("Thought Crimes"):** A personal agent intimately augments a user, potentially handling queries or thoughts that would never be vocalized publicly [00:11:02]. Cloud providers, even with enterprise-grade contracts, might be legally mandated to perform logging and safety checks [00:11:36]. To avoid any risk of being "punished for thought crimes," keeping personal agents local is a powerful argument [00:11:50].

## Technical Challenges in AI Agent Development

Despite the strong arguments for local agents, [[challenges_in_building_ai_applications | building effective AI agents]] presents several technical hurdles:

*   **Local Model Inference Speed and Limitations:** While open-source projects like LM Studio and MLC LLM (built on [[pytorch | PyTorch]]) are available for running local models [00:12:35], local model inference is currently slow and limited compared to cloud services [00:13:13]. Although 20-billion parameter or distilled models can run quickly [00:13:33], the latest, full, unquantized models remain very slow [00:13:41]. This area is expected to improve rapidly, but users may not always be able to run the absolute latest and greatest models locally [00:13:49].
*   **Multimodal Model Capabilities:**
    *   **Computer Use:** Open multimodal models are not yet great for computer use, and even closed models (APIs) frequently break [00:14:20].
    *   **Taste Identification:** Models struggle with specific and fine-grained user tastes, especially in areas like shopping [00:15:00]. They often provide generic recommendations and are not effective at visually identifying specific requests, relying more on text matching [00:15:26].
*   **Catastrophic Action Classifiers:** A significant challenge is the lack of robust catastrophic action classifiers [00:15:37]. While many agent actions are reversible or harmless (e.g., navigating to the wrong Wikipedia link) [00:15:51], some can be catastrophic (e.g., purchasing a Tesla instead of Tide Pods) [00:16:10]. More research is needed to enable agents to reliably identify and notify users before taking such irreversible actions [00:16:28].
*   **Open-Source Voice Mode:** The state of open-source voice mode for local agents is currently rudimentary [00:16:52]. For a truly personal agent, voice interaction is essential, but the technology is not yet mature enough [00:16:56].

## Optimism for the Future
Despite these [[challenges_in_creating_effective_ai_agents | challenges]], there is optimism regarding the future of personal local agents, primarily due to the rapid advancement of open models [00:17:07]. Open models are demonstrating faster intelligence compounding compared to closed models because development efforts are coordinated across a broader community [00:17:11]. This collaborative approach, seen in projects like Linux, PyTorch, and models such as Llama, Mistral, and Grok, often leads to unprecedented wins once a critical mass of coordination is achieved [00:18:09]. It is anticipated that open models will eventually surpass closed models in performance per dollar of investment [00:18:22].

Projects like Galactica and [[pytorch | PyTorch]] are actively working on plugging the reasoning gap between open and closed models [00:19:14] and enabling local agents by addressing the technical challenges [00:19:30].