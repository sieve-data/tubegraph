---
title: Finetuning and production stability of open AI models
videoId: wJwTlvb_TSo
---

From: [[aidotengineer]] <br/> 

The past 12 months have seen a dramatic increase in AI models, with over 50,000 models uploaded to Hugging Face per month, an acceleration equating to more than one AI model a minute <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This rapid growth highlights the increasing availability and adoption of open models in various applications <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The Rise of Open Models

Open-source models are proving capable of competing with large, proprietary models. DeepSeek-R1, for example, was the first open-source model to catch up with and surpass GPT-4, demonstrating that significant investment isn't always necessary to compete with major labs <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. DeepSeek-R1 recorded over 4 million downloads of its 685 GB model on Hugging Face in one month <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Companies like Featherless AI provide unlimited API requests to over 3,700 open AI models, including DeepSeek-R1, making them accessible to thousands of users <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Finetuning and Model Fragmentation

The proliferation of open models leads to significant [[finetuning_ai_models_for_better_performance|finetuning]] and fragmentation, where larger models like Llama and Qwen become specialized into individual models with distinct "personalities" and use cases <a class="yt-timestamp" data-t="02:51:30">[02:51:30]</a>. This allows for tailored solutions for specific tasks <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

## Production Stability and User Preference

A key insight into open model usage is the "staying power" of a model once it enters production <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>. Developers prioritize consistency and prefer to change their models only when they choose to, not when a provider decides to update <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

### Factors Contributing to Model Stickiness in Production:
*   **Cost-effectiveness**: Smaller models are generally cheaper at scale <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   **Established Tutorials and Integrations**: Models that gain early adoption and accumulate "hundreds of [[finetuning_ai_models_for_better_performance|fine-tuning]] tutorials" become default choices for cloud platforms (e.g., AWS, GCP), leading to widespread use in production environments <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   **Reliability and Accuracy**: Once a model reliably performs at scale, especially after being prompted to 99%+ accuracy and with metrics in place for observing changes, enterprises are reluctant to change it <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. The adage "if it ain't broke, don't fix it" applies <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **Licensing**: The A2 licensing of early truly open-source models like Mistral Nemo helped their adoption by enterprises, as it avoided the license restrictions of models like Llama that made legal teams uncomfortable <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

Models like Mistral Nemo, even when 8 months old and replaced by larger, better models, still show significant dominance in commercial use due to their established position <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. Similarly, Llama 2 remains a go-to for AI Safeguard tutorials and is actively used in production by new teams, despite newer versions being available <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

### User Behavior: Vibes over Benchmarks
For individual users, particularly in creative and companionship AI, model choice is often based on "Vibes" and preference rather than performance benchmarks (MML or price) <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. In these communities, models with different "flavors" emerge frequently, and users may return to "old favorites" for their specific charms <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.

## Key Use Cases and Their Impact on Stability

Based on platform usage data, AI models are commonly used for:
*   **Creativity and Companionship (30-40% of traffic)**: Includes creative writing (e.g., Novel Crafter), role-playing, companionship (e.g., Spicy Chat, Soul Haven), and to a lesser extent, therapy and journaling <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. This segment is characterized by rapid model changes driven by "Vibes" rather than strict performance metrics <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.
*   **Coding Co-pilot and Agents (20-30% of traffic)**: Covers auto-completion tools (like GitHub Co-pilot) and agentic coding workflows <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>. While auto-completion is largely solved, the focus is shifting to "nearly autonomous agents with lots of clarifying questions" and human intervention <a class="yt-timestamp" data-t="14:07:00">[14:07:00]</a>. This "Vibe coding" generates significantly more token traffic than companionship models <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>. Projects like Continue and Klon help achieve similar experiences to commercial models using open-source alternatives <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.
*   **ComfyUI and Friends (Approx. 5% of traffic)**: Used for complex AI generation workflows, particularly in image diffusion <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. These graph-style UIs are used by non-developers like musicians and lawyers <a class="yt-timestamp" data-t="16:57:00">[16:57:00]</a>.
*   **Write/Check (ChatGPT clones) (Approx. 20% of traffic)**: General-purpose AI usage for writing and checking tasks <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>.
*   **Agents and Workflow Automation (10-20% of traffic)**: This category is split into workflow automation with human oversight ("human escape hatches") and fully automated agents <a class="yt-timestamp" data-t="18:57:00">[18:57:00]</a>.

## [[Scaling AI agents in production|Scaling AI Agents in Production]] with Reliability

When [[scaling_ai_solutions_in_production|scaling AI solutions in production]], especially for enterprise use, maximizing ROI and minimizing negative impact are top priorities <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>. A common strategy involves building automation systems with built-in human escape hatches, allowing humans to take control when needed <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>. For example, an AI agent might draft 80-90% of email responses, with a human reviewing and finalizing before sending <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>. This approach builds confidence, allows for incremental automation of reliable use cases, and prevents catastrophic failures that could postpone AI adoption <a class="yt-timestamp" data-t="21:07:00">[21:07:00]</a>.

Fully automated, 100% reliable agentic agents for production environments are considered a mythical category that "does not exist" <a class="yt-timestamp" data-t="22:47:00">[22:47:00]</a>. The recommended mindset for building AI into production is to solve for the 80% with escape hatches, iteratively improving reliability from there <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>. This incremental approach, similar to software reliability engineering, can achieve high reliability (e.g., 99.998%) without the risks of an all-or-nothing launch <a class="yt-timestamp" data-t="24:11:00">[24:11:00]</a>.

### [[Testing and evaluation of AI models|Challenges with early AI models and improvements]]
The speaker notes that many current AI models are not 100% reliable and can hallucinate or fail <a class="yt-timestamp" data-t="27:24:00">[27:24:00]</a>. This highlights the ongoing need for [[robustness_and_coverage_in_ai_models|robustness and coverage in AI models]], especially for critical tasks.

## The Future of AI and Benchmarks

As the average AI model surpasses the MML (Multi-task Language Understanding) capabilities of an average office worker, traditional benchmarks are losing their meaning <a class="yt-timestamp" data-t="27:01:00">[27:01:00]</a>. The focus is shifting towards exploring linear transformer models as a means of "persisting memories, customization, and improving reliability for future AI models to make useful AI agents" <a class="yt-timestamp" data-t="27:33:00">[27:33:00]</a>.

Quirky, a 72-billion parameter linear Transformer and attention Transformer hybrid, is presented as an example of a new architecture that runs at less than half the GPU compute cost of other Transformer models, aiming to provide alternatives with lower inference costs <a class="yt-timestamp" data-t="26:22:00">[26:22:00]</a>. It cost only $100,000 to build, compared to DeepSeek's $10 million <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>.