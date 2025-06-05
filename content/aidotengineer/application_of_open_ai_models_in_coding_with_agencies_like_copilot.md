---
title: Application of open AI models in coding with agencies like copilot
videoId: wJwTlvb_TSo
---

From: [[aidotengineer]] <br/> 

The landscape of artificial intelligence (AI) models is rapidly expanding, with over 50,000 AI models uploaded to Hugging Face per month, a rate exceeding one model per minute <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Open-source models like DeepSeek-R1 have demonstrated their capability by catching up to and even surpassing closed-source models such as GPT-4, proving that significant budgets are not a prerequisite for competitive AI development <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Fedus AI: Democratizing Access to Open Models
Fedus AI offers a platform providing unlimited API requests to over 3,700 truly open AI models, including DeepSeek-R1, for a flat monthly fee of $25 for individuals <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The company's objective is to provide accessibility to all truly open AI models, with plans to continuously expand their catalog to cover all Hugging Face models <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This approach allows users to choose models based on preference and perceived quality rather than token-based pricing <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

A key insight from Fedus AI's data is the "staying power" of models once they enter production, particularly for commercial users <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Developers prioritize consistency and prefer to update models on their own terms, not when a provider decides to update <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Smaller models, like the Mistral Nemo models (eight months old), continue to dominate commercial usage due to their cost-effectiveness at scale and established presence in production environments and tutorials <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

> For many commercial and enterprise scales, once they get something working reliably at scale, especially once they have the metrics in place to observe changes and their reliability and they have prompted it to 99% plus accuracy, they really do not want to change their system and have it break overnight <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Similarly, Lama 2 remains a go-to model for [[commercial_and_enterprise_application_of_open_ai_models | AI Safeguard]] tutorials online, despite newer versions, because of its stability and active use in production <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## AI Usage Trends
Based on data from Fedus AI and collaborations with platforms like OpenRouter, the primary uses of open AI models are:
1.  **AI for Creativity or Companionship:** Representing 30-40% of all AI traffic, this includes applications for creative writing (e.g., NovelCrafter) and AI role-play/companionship (e.g., Spicy Chat, Soul Haven) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This segment also includes therapy and journaling apps <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.
2.  **AI for Code (Copilot & Agents):** This category accounts for 20-30% of all traffic <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.
3.  **ComfyUI and Friends:** About 5% of traffic for personal agentic workflows, used by non-developers for complex generation tasks <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
4.  **Write and Check (ChatGPT Clones):** Roughly 20% of requests, offering similar UI and features to popular chat models <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
5.  **AI for Agents and Work:** 10-20% of traffic, focusing on workflow automation <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>.

## AI for Coding: Copilots and Agents
The "coding co-pilot and coding agents" segment is a significant and rapidly growing area for open AI models <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Autocompletion Tools
Auto-completion tools for code, similar to GitHub Copilot, or chat-based editing within Integrated Development Environments (IDEs), are widely available through plugins and native integrations <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. These features are now considered essential for modern IDEs <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. Many smaller AI models (3 billion to 12 billion parameters) are considered "good enough" for this task, suggesting that auto-completion for code is largely a solved problem <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

### Evolution to Agentic Code
The focus of [[future_of_AI_in_coding | AI in code]] has shifted towards more [[ai_coding_agents_and_selfcoding_technology | agentic code]], specifically "nearly autonomous agents with lots of clarifying questions but involve interventions with humans in the loop" <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This phenomenon is termed "Vibe Coding," where developers primarily interact with the agent through chat and prompts, rather than directly editing code <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

These agents can be "token hungry," generating a thousand times more input and output tokens than a single person chatting with a companion model <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. Despite a smaller user base (tens of thousands of coders), the traffic volume generated by coding agents is growing rapidly <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>. While closed-source models like Claude Sonnet currently dominate this traffic by a 10-to-1 ratio, the growth of open models in this space, especially since the DeepSeek-R1 wave, has been significant <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

Notable open-source projects for [[impact_of_ai_coding_agents_on_software_engineering | AI in coding]] include:
*   **Client:** Focuses on the chat agentic workflow <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.
*   **Continue:** Provides auto-completion [[integration_of_ai_coding_agents_with_thirdparty_tools | integration]] <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
    Combined, these projects offer an experience comparable to commercial models with IDE platforms like Cursor <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

## AI for Agents and Workflow Automation
This category, representing 10-20% of traffic, focuses on workflow automation within enterprises <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. The priority for enterprises is to maximize ROI by getting agents into production while minimizing negative impact <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### Workflow Automation with Human Oversight
A common strategy is to build automation systems with "human escape hatches" from day one <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>. For example, AI agents can draft responses for inbound emails, check inventories, and apply rules, with a human platform for editing and finalizing the response before sending <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>. At launch, such systems can successfully draft 80-90% of responses, with humans handling the remainder <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>. Over time, as confidence builds, specific reliable use cases can be fully automated <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>.

> For companies in production who is trying to incrementally improve with each step to 99% plus reliability, it's nearly impossible to do so if you change the model every week <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.

### Challenges of Fully Automated Agents
Attempting 100% full automation without human oversight often leads to negative consequences, such as angry customers due to bad automated responses, potentially killing the entire AI project <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>. The mythical "fully truly 100% reliable agentic agents" does not currently exist in production environments <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>.

The recommended approach for [[challenges_and_insights_in_developing_ai_coding_agents | building AI for production]] is to aim for solving 80% of problems with escape hatches <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. This pragmatic approach, similar to reliability engineering, involves building a streamlined, reliable system for 80-90% of scenarios, then iterating for the remaining failure scenarios to achieve high reliability incrementally <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>. This strategy, though less "sexy," ensures project survival, significant ROI, and continuous improvement <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>.

## Quirky: A New Open Model for Reliability
Quirky is introduced as a 72-billion parameter linear transformer and attention transformer hybrid that runs at less than half the GPU compute cost of other transformer models <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>. Built for approximately $100,000, significantly less than models like DeepSeek ($10 million), Quirky represents a move towards more efficient and reliable AI model architectures <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

The focus for [[testing_and_optimization_of_ai_coding_agents | future AI models]] should be on persisting memories, customization, and improving reliability to create truly useful AI agents, rather than solely chasing benchmark scores like MML (which are losing meaning as models become highly capable) <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.