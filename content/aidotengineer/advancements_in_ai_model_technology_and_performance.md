---
title: Advancements in AI model technology and performance
videoId: wJwTlvb_TSo
---

From: [[aidotengineer]] <br/> 

The landscape of AI models is rapidly expanding, with over 50,000 AI models uploaded to Hugging Face per month, a rate that is accelerating to more than one model per minute [00:00:08]. This explosive growth highlights significant [[ai_technological_advancements | technological advancements]] and increased accessibility within the field.

## Breakthrough Open-Source Models

The emergence of powerful open-source models has begun to challenge the dominance of larger, proprietary AI labs.

### DeepSeek-R1
DeepSeek-R1 is notable as the first open-source model to match and even surpass GPT-4 in performance [00:00:22]. This achievement demonstrates that significant progress can be made without requiring multi-billion dollar investments, instead leveraging "a little smart and prudence" [00:00:27]. DeepSeek-R1 has seen immense popularity, with over 4 million downloads of its 685 GB model on Hugging Face in a single month, accounting for over 2.74 exabytes of data transfer across the internet [00:00:32].

### Mistral Nemo Chat
Mistral Nemo Chat was one of the early truly open-source models, holding an A2 license, and it surpassed GPT-3.5+ [00:03:30]. Unlike models with Llama license restrictions that caused discomfort for enterprise lawyers [00:04:43], Mistral Nemo Chat became a default model across various cloud platforms, including AWS and GCP [00:04:51]. Its widespread adoption led to hundreds of [[finetuning_ai_models_for_better_performance | fine-tuning]] tutorials and heavy integration into existing user workflows, replacing GPT-3.5 [00:04:56]. Despite being over eight months old and effectively replaced by newer, larger, and better models, its "stain power" in production and tutorials is strong, with many enterprises reluctant to change systems that are working reliably [00:03:50].

## Trends in Model Adoption and Usage

User behavior and enterprise needs significantly influence which AI models are adopted and persist in use.

### Consistency Over Cutting-Edge
For business and production environments, consistency is paramount [00:03:19]. Developers prefer to change models only when they choose to, not when a provider decides to update [00:03:21]. This leads to a surprising stickiness of models in production, where systems that reliably perform at scale are rarely updated for quarters or even years, even if newer, better models exist [00:04:16]. For example, the Llama 2 model, despite having newer and better versions, still accounts for about 2% of workloads, particularly as a go-to for AI Safeguard tutorials [00:05:53].

### Fine-Tuning and Personalization
The concept of [[finetuning_ai_models_for_better_performance | fine-tuning]] has led to significant fragmentation, where larger models like Llama and Qwen are customized into individual models with distinct "personalities and individual use cases" [00:02:51]. This allows for models to be tailored to specific applications.

### Broad Applications of Open Models
Data from Featherless AI, which provides unlimited API requests to over 3,700 open AI models [00:00:57], reveals diverse usage patterns among individual and business users [00:07:07]:
*   **AI for Creativity or Companionship**: This is the largest segment for non-coding AI requests, representing 30-40% of all AI traffic [00:07:35]. It includes creative writing (e.g., NovelCrafter for outlining novels) [00:07:44] and AI role-playing/companionship (e.g., Spicy Chat, Soul Haven) [00:08:12]. Contrary to stereotypes, over 60% of users in the companionship segment are women, mirroring trends in romance novel sales [00:08:58]. Users often engage in long conversations for de-stressing or due to real-life emotional unavailability [00:09:31].
*   **Therapy and Journaling**: A fragmented category with many apps, but also users leveraging ChatGPT clones with "therapy character" prompts [00:09:57].
*   **AI for Code**: Accounts for 20-30% of traffic [00:13:05]. This includes code auto-completion (considered largely "solved" by small models) [00:13:47] and semi-autonomous "agentic" coding with human intervention, a trend termed "Vibe Coding" [00:14:10]. These agents are "token hungry," generating a thousand times more traffic than companion models [00:14:34].
*   **ComfyUI and Friends**: About 5% of traffic for personal agentic workflows, used by non-developers like musicians, lawyers, and influencers to chain complicated workflows for text generation [00:16:39]. This indicates a slow but gradual build-up of users [00:17:32].
*   **ChatGPT Clones**: Represents about 20% of requests, with platforms offering their own UIs (like Featherless's Phoenix) [00:17:53].
*   **AI for Agents and Work**: 10-20% of traffic, split into workflow automation (human-in-the-loop agents) and fully automated agents [00:18:44]. For workflow automation, the focus is on maximizing ROI by automating 80-90% of tasks (e.g., email drafting for insurance claims) with human "escape hatches" for review, leading to higher adoption and productivity [00:19:07]. Fully automated agents, while aspirational, are noted to often fail in production environments, leading to project abandonment [00:22:39].

## Future Directions and Architectural Innovations

The future of AI models is shifting beyond raw benchmarks to focus on reliability and new architectures.

### Quirky Model
A significant advancement is the Quirky model, a 72-billion parameter linear transformer and attention transformer hybrid [00:26:22]. This model boasts a "completely new architecture" that operates at less than half the GPU compute cost of other transformer models [00:26:27]. It cost only $100,000 to build, in stark contrast to DeepSeek's $10 million [00:26:53]. The development of such models is part of the [[advancements_in_ai_and_future_implications | advancements in AI and future implications]] focused on persisting memories, customization, and improving reliability for future AI agents [00:27:37].

### Evolving Benchmarks
As the average AI model surpasses the average office worker in MML (Multimodal Language understanding) [00:27:01], traditional benchmarks are losing their meaning [00:27:06]. The focus for [[advancements_in_ai_and_future_implications | future AI models]] is shifting towards reliability, consistency, and avoiding issues like hallucination [00:27:24]. The aim is to build systems that reliably handle 80-90% of scenarios with human oversight for the remainder, allowing for incremental [[continuous_improvement_in_ai_systems | improvements]] and long-term project survival [00:24:11].