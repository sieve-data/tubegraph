---
title: Enterprise and consumer AI trends
videoId: P6y0gr-W2-k
---

From: [[redpointai]] <br/> 

This article explores various trends and discussions surrounding enterprise and consumer AI, drawing insights from industry experts.

## Key Surprises in AI

The AI landscape has seen rapid changes, leading to several surprises for industry observers:

*   **Reasoning Models and Timing** The unexpected release of reasoning models directly after Ilia's "scaling is dead" talk was a positive surprise. This swift transition from pre-training to inference time as the new scaling law felt "suspiciously neat," almost as if strategically planned by major AI labs [00:01:14], [00:01:36], [00:02:07].
*   **Open Source Adoption in Enterprise** A negative surprise has been the low adoption of open-source models within enterprises. While hobbyist communities embrace open-source models, enterprise usage is estimated at 5% and declining. Enterprises are currently focused on [[enterprise_adoption_and_use_cases_for_ai | use case discovery]], prioritizing the most powerful models available, which often means closed-source options [00:02:30], [00:03:05], [00:03:14].
*   **Speed of Open Source Catch-Up** Conversely, the speed at which open-source models, particularly DeepSeek, caught up to reasoning models was a significant surprise. This rapid progress suggests that the competitive advantage of closed-source models might be shorter than anticipated [00:03:33], [00:04:04]. However, this "catch-up" is largely seen as replication or distillation, not fundamental innovation, with DeepSeek potentially ceasing open-sourcing its models [00:04:48], [00:04:13].
*   **Low-Code Builders Missing AI Market** It was surprising that traditional low-code builders like Zapier, AirTable, Retool, and Notion did not capture the AI builder market. Despite having the DNA, reach, and distribution, they integrated AI by improving existing features rather than creating entirely new software paradigms from scratch, which was achieved by new AI-native companies [00:07:51], [00:08:09], [00:09:09].
*   **Apple Intelligence's Missteps** Apple's approach to AI, particularly with Apple Intelligence, has been a letdown. Despite being in a prime position for personal assistance features, its AI products have struggled with accuracy and adoption [00:10:11], [00:10:16].

## Overhyped vs. Underhyped AI Concepts

### Overhyped

*   **Agents Frameworks** The current state of agent frameworks is considered overhyped. They are described as being in a "jQuery era" of single-file, big frameworks with many helpers, rather than the "React" era of stable, buildable platforms. The rapid flux of workloads makes it challenging for these frameworks to reconcile their offerings [00:11:42], [00:11:25]. Instead of frameworks, the focus should be on establishing stable protocols, like MCP, as the foundation for future development [00:11:55].
*   **New Model Training Companies** There's surprise at the continued emergence of new companies solely focused on training models. While some niche, specialized foundation models (e.g., for robotics, biology, material science) with unique datasets might have a case, the general LLM/agent space is tough to compete in, especially with the dominance of major players [00:16:16], [00:17:15], [00:18:02].

### Underhyped

*   **Apple's Private Cloud Compute (PCC)** Despite Apple Intelligence's struggles, Apple's Private Cloud Compute (PCC) is seen as an underhyped development. It aims to bring on-device security to the cloud, enabling single-tenant-like privacy guarantees in multi-tenant environments. This is crucial for large enterprises that cannot always secure enough GPUs for purely private VPCs [00:12:44], [00:13:55].
*   **Memory / Stateful AI** The concept of memory and stateful AI is significantly underhyped. While conversational memory exists, deeper "memory memory" – like storing knowledge graphs or enabling agents to learn on the job beyond context length – is largely ignored by major labs, despite its potential to make agents smarter [00:14:03], [00:14:54], [00:15:28]. The "memory server" in MCP is highlighted as a promising starting point [00:15:14].
*   **AI DevOps / AI SRE** While currently struggling to take off due to technological limitations, AI DevOps and AI SRE are considered interesting opportunities. As the technology matures, AI advancements could significantly improve mean time to recovery (MTR) and enable semantic understanding beyond mere anomaly detection [00:48:50], [00:49:10].
*   **Voice Real-time Infrastructure** This area is very hot and interesting, though its ultimate market size is still unclear [00:48:37].

## Product Market Fit in AI Applications

Genuine product market fit (PMF) in AI applications is measured by significant revenue, such as reaching $100 million in revenue [00:26:10].

*   **Existing PMF Categories**:
    *   **Co-pilot** [00:26:17]
    *   **Jasper** (formerly) and other writing assistance tools [00:26:20].
    *   **Cursor** (coding agent) [00:26:26].
    *   **Deep Research**: Models like Grok, Gemini, and Perplexity that offer long-term agentic reporting are showing strong PMF, driving significant revenue for companies like OpenAI [00:26:42], [00:27:12].
    *   **Customer Support**: Companies like Dekugan and Sierra are effectively leveraging AI for customer support, demonstrating significant market opportunity by addressing major cost centers for businesses [00:30:41], [00:31:55]. This first wave of AI apps focused on cost-cutting, often in areas previously outsourced, leading to immediate traction but potentially fierce price competition [00:32:02], [00:32:21], [00:32:44].

*   **Emerging PMF Categories**:
    *   **Screen Sharing Assistance**: AI that offers assistance while observing user workflows [00:35:56].
    *   **Outbound Sales**: Moving from support to proactive sales efforts with AI [00:36:06].
    *   **Hiring/Recruiting**: AI-powered solutions for the recruitment process [00:36:14].
    *   **Education**: Personalized teaching and learning experiences using AI [00:36:16].
    *   **Finance**: AI applications tailored for financial use cases [00:36:31].
    *   **Personal AI**: While harder to monetize, personal AI assistants are a growing area of interest [00:36:35].
    *   **Voice AI**: For tasks like scheduling and intake (e.g., for home services), even 75% accuracy is a significant improvement over current human-based systems, leading to substantial revenue increases for customers [00:33:17].

The next wave of AI apps is expected to focus more on revenue growth and topline increases, which could be more defensible than the initial cost-cutting wave [00:32:04], [00:33:05].

## Defensibility at the Application Layer

Defensibility in AI applications is primarily driven by:

*   **Network Effects**: Prioritizing multiplayer experiences over single-player ones helps build robust network effects, which are paramount for long-term survival. An example is Chai Research, a Character AI competitor, which despite not owning its models, thrives on its network of model submitters and marketplace-like interface [00:39:16], [00:40:19], [00:40:37].
*   **Brand and Product Surface Area**: Companies that quickly establish themselves as a strong brand synonymous with an entire category gain significant advantage, leading to higher average contract values (ACVs) as customers pay a premium for recognized solutions [00:41:17], [00:41:41].
*   **Velocity and User Experience**: The ability to rapidly build a broad product and continually adapt to new model releases (every 3-6 months) by integrating them first is crucial. This focus on user experience, design, and speed of execution, often involving "a thousand small things," creates defensibility, similar to traditional application SaaS companies [00:42:04], [00:42:12], [00:42:24]. The initial "head fake" of focusing on unique datasets or training custom models for defensibility has proven less useful [00:41:50].

## Infrastructure and Development Landscape

The infrastructure space around AI is evolving, with a shift from bare-metal infrastructure to "infra around the model" [00:43:26].

*   **LLM OS Concepts**: Areas like code execution (e.g., E2P), memory, and advanced search capabilities are becoming integral parts of the "LLM OS" [00:42:55].
*   **Cybersecurity**: AI is increasingly applied to cybersecurity, especially in areas where offense uses AI, necessitating AI on the defense side (e.g., email security, identity verification). The ability of models to understand "semantics" (e.g., in binary inspection) beyond mere syntax is a significant advancement for security [00:43:38], [00:44:07].
*   **Model Labs' Expansion**: Major research labs like OpenAI are increasingly expanding into the developer and infrastructure categories, offering tools like search APIs. This raises questions about whether they aim to be API companies or product companies, as selling search APIs can be less lucrative than building direct products like ChatGPT search [00:45:10], [00:46:18].
*   **Application Layer Focus**: The application layer is clearly more interesting and valuable than core infrastructure. Applications can charge for utility rather than just cost, allowing for higher margins compared to infrastructure which often reduces to "cost plus" pricing [00:47:10], [00:47:17], [00:47:21].
*   **Struggling Areas**:
    *   **Fine-tuning companies**: Standalone fine-tuning services struggle to form a large business unless integrated into broader [[role_of_custom_models_and_enterprise_ai_integration | enterprise AI]] or services offerings [00:47:56], [00:48:06].
    *   **AI DevOps/SRE**: The technology is not yet mature enough for widespread adoption of autonomous SRE [00:48:50].

## Unanswered Questions and Future Implications

*   **Scaling Reinforcement Learning (RL)**: The biggest unanswered question is whether RL can be successfully applied to non-verifiable domains, such as law (contracts), marketing, and sales (simulating conversations). If not, autonomous agents might be limited to verifiable domains, while non-verifiable ones would still require human "taste-makers" with co-pilots [00:50:15], [00:50:46].
*   **Hardware Scaling and Dominance**: The "rule of nines" at OpenAI suggests that achieving higher reliability (e.g., 90% to 99%) requires an order of magnitude increase in compute every 2-3 years. This raises concerns about how compute will scale, and whether Nvidia's dominance will continue, or if competitors like AMD, AWS (with Trainium chips), Microsoft, and Facebook will successfully challenge it. The stability of the transformer architecture suggests a case for dedicated silicon (ASICs) for transformers, but who will win that race is unknown [00:51:34], [00:51:48], [00:52:00], [00:52:50], [00:53:03].
*   **Agent Authentication**: A critical emergent question is how to authenticate agents accessing websites on behalf of users. A new "SSO effectively for agents" is needed to distinguish human users from their agents, potentially leading to new authentication methods like retina scans, as suggested by Sam Altman [00:54:41], [00:55:06], [00:55:21].