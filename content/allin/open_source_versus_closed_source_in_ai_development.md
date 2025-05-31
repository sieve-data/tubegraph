---
title: Open source versus closed source in AI development
videoId: 8RkgkOqWs0s
---

From: [[allin]] <br/> 

The debate between [[ai_open_source_versus_closed_source_models | open-source]] and closed-source approaches is a central theme in AI development, with implications for innovation, cost, and geopolitical competition <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>.

## Deepseek R1: A Case Study
The release of Deepseek's R1 language model, which is comparable to [[openai_and_ai_advancements | OpenAI's]] 01 model, brought this debate to the forefront <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. Deepseek claimed to have developed R1 for $6 million using 2,000 GPUs, a stark contrast to [[openais_approach_to_ai_development_and_accessibility | OpenAI's]] reported $800 million cost for GPT-4 training and a projected $1 billion for GPT-5 <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. Deepseek further intensified the debate by [[ai_open_source_versus_closed_source_models | open-sourcing]] R1 and offering API access at a fraction of the cost <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.

This development legitimately surprised many in the industry, accelerating perceptions of how close China is to the US in AI model development, from 6-12 months behind to potentially 3-6 months <a class="yt-timestamp" data-t="00:21:32">[00:21:32]</a>.

### Cost Claims and Compute Resources
The claim of developing R1 for $6 million has been largely debunked <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. This figure likely refers only to the final training run, not the total R&D and hardware costs <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. Experts estimate Deepseek, including its associated hedge fund, possesses a compute cluster of over 50,000 Hopper GPUs (10,000 H100s, 10,000 H800s, and 30,000 H20s), a setup costing over a billion dollars <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

### Innovation Driven by Constraint
Despite the disputed cost, Deepseek's technical innovations are notable <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. They developed a new reinforcement learning algorithm (GRPO) that uses less computer memory and is highly performant, differing from the conventional PPO algorithm <a class="yt-timestamp" data-t="00:27:15">[00:27:15]</a>. They also worked around Nvidia's proprietary CUDA language by using PTX, going directly to the bare metal <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. These innovations suggest that constraints, possibly related to GPU access or memory, can drive unique solutions that might not emerge in environments with abundant compute resources <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

### Distillation Accusations
A significant part of the controversy involves accusations that Deepseek's R1 model was "distilled" from [[openai_and_ai_advancements | OpenAI's]] models <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>. Distillation is a process where a smaller model learns from a larger, more powerful model by asking it questions and refining its own responses <a class="yt-timestamp" data-t="00:31:13">[00:31:13]</a>. Evidence, such as Deepseek's V3 model self-identifying as Chat GPT-4, suggested substantial training on [[openai_and_ai_advancements | OpenAI]] output <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>. This could occur either by crawling publicly available [[openai_and_ai_advancements | OpenAI]] output or by heavily using [[openai_and_ai_advancements | OpenAI's]] API <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>. [[microsofts_investment_in_openai_and_generative_ai_technologies | OpenAI]] has stated they found evidence that Deepseek used their proprietary models for training <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>.

The situation is further complicated by [[microsofts_investment_in_openai_and_generative_ai_technologies | Microsoft]], a key partner of [[openai_and_ai_advancements | OpenAI]], hosting Deepseek's R1 model on Azure <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. Critics argue this shows a lack of loyalty from [[microsofts_investment_in_openai_and_generative_ai_technologies | Microsoft]] to [[openai_and_ai_advancements | OpenAI]] by facilitating the use of a potentially "stolen" or distilled model that undercuts their partner <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

## Arguments for [[ai_open_source_versus_closed_source_models | Open Source]]
Proponents of [[ai_open_source_versus_closed_source_models | open source]] AI argue that it promotes innovation, reduces costs, and benefits humanity <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>. The idea is that if foundational models become commoditized and cheaper, the value shifts to the application layer, similar to how YouTube was built on storage or Uber on GPS <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. This would lead to a "thousand flowers blooming" effect with widespread innovation <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>.

Additionally, as the cost of AI decreases, demand and usage are expected to increase significantly (Jevons Paradox), leading to more applications becoming economically feasible <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>. [[metas_open_source_ai_strategy | Meta]] is seen as a crucial player in the [[ai_open_source_versus_closed_source_models | open-source]] space, expected to continue embracing and extending these developments to foster developer ecosystems and applications <a class="yt-timestamp" data-t="00:41:13">[00:41:13]</a>.

## Arguments for Closed Source / Concerns about [[ai_open_source_versus_closed_source_models | Open Source]]
Companies like [[openai_and_ai_advancements | OpenAI]], which initially aimed for [[ai_open_source_versus_closed_source_models | open source]] but shifted to a closed-source model, face scrutiny <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>. The argument for closed-source models often centers on the need to protect intellectual property and ensure a return on the substantial capital invested in developing frontier models <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>.

Concerns about [[ai_open_source_versus_closed_source_models | open source]] also include:
*   **IP Theft:** The risk of other entities using proprietary models and data without permission for their own development <a class="yt-timestamp" data-t="00:36:16">[00:36:16]</a>.
*   **Geopolitical Strategy:** From a US perspective, Chinese companies open-sourcing models could be seen as a strategic move to catch up and undercut leading American companies <a class="yt-timestamp" data-t="00:48:52">[00:48:52]</a>.
*   **Safety and Control:** The proliferation of powerful AI models through [[ai_open_source_versus_closed_source_models | open source]] raises questions about control and potential misuse, leading to calls for stricter regulation like KYC requirements for model users <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>.

## Industry Implications
The ongoing debate highlights several [[challenges_and_opportunities_in_ai_development_and_deployment | challenges and opportunities in AI development and deployment]]:
*   **Value Chain Shift:** If models become commoditized, the value in AI development will shift from building foundational models to creating specialized applications and services built on top of them <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>. This requires companies to build "shims" or abstraction layers to easily swap out underlying models <a class="yt-timestamp" data-t="00:42:43">[00:42:43]</a>.
*   **Hardware and Data Moats:** While model performance may depreciate quickly, competitive advantages could still arise from controlling unique datasets (e.g., Tesla's driving data, Google's YouTube content) or from innovations in hardware and manufacturing <a class="yt-timestamp" data-t="01:08:56">[01:08:56]</a>.
*   **Overcapitalization Risks:** Excessive capital in AI development might lead to a lack of innovation driven by constraint, making companies "too soft" or "too bureaucratic" <a class="yt-timestamp" data-t="01:04:48">[01:04:48]</a>.
*   **Electricity and Infrastructure:** The increasing demand for AI, especially in areas like autonomous vehicles, will place immense pressure on electricity grids and require massive investment in power generation and infrastructure to support these technologies <a class="yt-timestamp" data-t="01:28:15">[01:28:15]</a>.

The future of AI development will likely involve a dynamic interplay between [[ai_open_source_versus_closed_source_models | open-source]] collaboration and proprietary innovations, with market forces and geopolitical considerations shaping the landscape <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>.