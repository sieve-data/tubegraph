---
title: AI infrastructure and developer tools
videoId: P6y0gr-W2-k
---

From: [[redpointai]] <br/> 

This article draws insights from a crossover discussion between Unsupervised Learning and Latace, a technical newsletter and podcast focused on [[trends_and_challenges_in_ai_infrastructure | AI infrastructure]], tooling, and product for [[building_a_successful_ai_product_for_developers | AI engineers]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The conversation delves into key developments, trends, and challenges in the rapidly evolving AI landscape <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Key Surprises in the AI Landscape

The past year has brought several surprises in AI:
*   **Model Advancements:** The rapid progress of models, particularly the release of reasoning models (like DeepSeek), was unexpected. This occurred shortly after a significant discussion by Ilya Sutskever suggesting "scaling is dead," creating a perception of "so over" followed by "so back" in a short period <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The timing, particularly with DeepSeek's progress, felt "suspiciously neat" as pre-training seemed to tap out and inference time became the new scaling law <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Open Source Adoption:** There was a surprising lack of enterprise adoption for open-source models, despite their capabilities <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. Estimates placed open-source model usage in enterprises at about 5% and decreasing, as companies prioritize powerful models for use case discovery <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Open Source Catch-Up:** Conversely, the speed at which open source (specifically DeepSeek) caught up with closed-source reasoning models was unexpected. The value proposition of model companies, offering exclusive access to models for product building, now seems to have a much shorter exclusivity period <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. It's noted that "open source" in this context often refers to specific companies like DeepSeek choosing to release their models, rather than a broad "team open source" effort <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Low-Code Builders and AI:** It was surprising that low-code builders (e.g., Zapier, Airtable, Retool, Notion) did not capture the AI builder market despite having the DNA and distribution <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. This is attributed to a potential mindset difference: existing companies focused on improving their baseline, while new AI builders started from "whole cloth" without prior preconceptions <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Overhyped vs. Underhyped in AI

### Overhyped
*   **[[openai_agent_development_tools | Agent frameworks]]:** These are seen as overhyped due to the rapid flux in workloads, making it hard to build stable frameworks <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. The current state is compared to the "jQuery era," suggesting a need for a more stable, "React"-like approach <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Some argue it might even be too early for frameworks, with focus needed on protocols rather than frameworks <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **New Model Training Companies:** Despite initial thoughts that the era of new model training companies was passing, many continue to emerge <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. While not impossible, it's questioned what unique value they bring beyond pursuing AGI, which cannot be achieved by all <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. The trend points towards general-purpose models, with specialized models likely requiring unique datasets (e.g., in robotics, biology, material science) <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. The focus seems to be on whether these models will deliver on the promise of increased top-line revenue rather than just cost-cutting <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

### Underhyped
*   **Memory (Stateful AI):** The lack of true "memory memory" (beyond conversational memory) in agents from major labs like OpenAI and Cohere is surprising <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. The ability to store knowledge graphs about users, exceeding context length, is a significant opportunity for smarter agents that can learn on the job <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. Stateful AI is seen as potentially interesting to VCs due to its resemblance to databases <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Private Cloud Compute (PCC) on the device/local:** Apple's architectural work in bringing on-device security to the cloud (PCC) is considered underhyped <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. This addresses the challenge of running large LLMs in multi-tenant cloud environments while needing single-tenant guarantees, especially as obtaining enough GPUs for private VPCs is difficult <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.

## Product Market Fit in AI Applications

Current areas showing genuine product market fit:
*   **Coding Agents:** Companies like GitHub Copilot and Cursor are examples <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
*   **Support Agents (Customer Support):** Companies like Sierra and Dekugan are leading this space, addressing a significant cost center for businesses <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>.
*   **Deep Research:** Services that provide long-term agentic reporting, exemplified by Perplexity and OpenAI's deep research features, are gaining traction <a class="yt-timestamp" data-t="00:26:42">[00:26:42]</a>.
*   **Voice AI:** Applications that don't require 100% precision and recall (e.g., scheduling intake for home services) can provide significant value by improving efficiency even with partial effectiveness, as businesses often miss a high percentage of calls <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.

Emerging areas with potential for product market fit:
*   **Screen Sharing Assistance:** AI watching user work and offering assistance <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>.
*   **Outbound Sales:** AI assisting with proactive sales efforts <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
*   **Hiring/Recruiting:** AI applications for the recruiting side <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.
*   **Personalized Education/Teaching:** AI-powered personalized learning experiences <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   **Finance:** Various finance-specific use cases <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a>.
*   **Personal AI:** Though harder to monetize, personal AI assistants are an area of interest <a class="yt-timestamp" data-t="00:36:35">[00:36:35]</a>.

## Defensibility at the Application Layer

Defensibility at the application layer is crucial for [[building_a_successful_ai_product_for_developers | AI product]] success <a class="yt-timestamp" data-t="00:39:07">[00:39:07]</a>. Key factors include:
*   **Network Effects:** Prioritizing and building out multiplayer experiences can create strong network effects, as demonstrated by Chai Research (a character AI competitor) <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>. Chai Research, despite not owning its models, built a network of users submitting models, creating a robust marketplace <a class="yt-timestamp" data-t="00:40:18">[00:40:18]</a>.
*   **Brand:** Becoming a recognized brand synonymous with a category quickly (within 6-9 months) grants significant market access and allows for premium pricing, even if competitors offer similar technical capabilities <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>.
*   **Velocity and User Experience:** The true defensibility lies in a company's ability to execute "a thousand small things" that create a delightful user experience and design <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>. High product velocity is essential, as new models present an existential event every 3-6 months; companies must be first to figure out how to leverage them <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>. This approach is similar to traditional application SaaS companies. <a class="yt-timestamp" data-t="00:42:30">[00:42:30]</a>

## The [[ai_infrastructure_and_data_center_challenges | AI Infrastructure]] Space

The most interesting areas in [[ai_infrastructure_and_data_center_challenges | AI infrastructure]] are generally not the "bare metal" infrastructure (like GPU serving) but rather the "infra around models" <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>. This includes:
*   **LLM OS:** A conceptual framework for the operating system layer around LLMs <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.
*   **Code Execution:** As seen with companies like E2P <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
*   **Memory:** As discussed earlier, building stateful AI solutions <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.
*   **Search:** Companies focused on enhancing search capabilities with AI <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.
*   **Cybersecurity:** Applying AI on the defense side for areas like email security, identity, and rethinking practices like red teaming using AI <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **Semantics vs. Syntax:** AI models' ability to infer semantics from code or other data (understanding "what this code is trying to do") goes beyond simple syntax rules, offering a new dimension for security and other applications <a class="yt-timestamp" data-t="00:44:07">[00:44:07]</a>.

While GPU serving and [[ai_infrastructure_and_data_center_challenges | data centers]] are critical, they are capital-intensive and often reduce to a "cost plus" business model, which is less attractive compared to applications that charge for utility <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>.

### The Role of Major Labs in Infrastructure
OpenAI and other large research labs are increasingly encompassing parts of the developer and infrastructure categories by offering these as APIs. For example, OpenAI's search capability is now available as an API, competing with startups <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>. The question remains whether these labs will prioritize being API companies or product companies, and whether their bundled offerings will outweigh best-of-breed independent solutions <a class="yt-timestamp" data-t="00:46:18">[00:46:18]</a>.

### Challenges in AI Infrastructure
Certain areas face challenges for investment or widespread adoption:
*   **Finetuning Companies:** Standalone finetuning companies struggle to scale as a big business unless wrapped into a broader enterprise AI service offering <a class="yt-timestamp" data-t="00:47:56">[00:47:56]</a>.
*   **AI DevOps/AIOps:** While there's a theoretical opportunity for AI to self-heal and manage codebases, it hasn't fully materialized yet <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>. However, some believe it's an interesting opportunity for the short term as the technology improves to increase the efficacy of things like Mean Time to Resolution (MTR) <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.
*   **Voice Real-time Infrastructure:** While hot and interesting, its ultimate market size is still unclear <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>.

## Unanswered Questions with Broad Implications

*   **RL on Non-Verifiable Domains:** Can Reinforcement Learning (RL) be successfully applied to non-verifiable domains like law (contracts, documents) or marketing/sales (simulating outbound conversations)? <a class="yt-timestamp" data-t="00:50:22">[00:50:22]</a> If not, AI agents might be limited to verifiable domains, while co-pilots would be needed for non-verifiable ones, requiring human oversight <a class="yt-timestamp" data-t="00:50:46">[00:50:46]</a>.
*   **Hardware Scaling and GPU Dominance:** How will the AI ecosystem scale with the "rule of nines" (each order of magnitude increase in reliability requires an order of magnitude increase in compute)? <a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a> Will [[ai_infrastructure_and_data_center_challenges | Nvidia]] continue its dominance, or will competitors like AWS (with their Trainium/Inferentia chips), AMD, Microsoft, and Facebook successfully challenge it to increase GPU availability? <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>
*   **Agent Authentication:** A critical emerging question is how agents will authenticate themselves when accessing websites on behalf of users, indicating that it's an agent and not the user directly <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>. This points to a need for a "new SSO" for agents <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>.