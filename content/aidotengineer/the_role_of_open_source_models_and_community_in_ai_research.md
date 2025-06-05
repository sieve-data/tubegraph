---
title: The Role of Open Source Models and Community in AI Research
videoId: JIsgyk0Paic
---

From: [[aidotengineer]] <br/> 

Will Brown, a machine learning researcher at Morgan Stanley, presented insights into the future of AI engineering, particularly focusing on the role of reinforcement learning (RL) in the development of AI agents and the significant contribution of the [[open_sourcing_and_applications_in_realworld_tasks | open source]] community <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. His talk synthesized trends within the broader research community and included recent [[open_sourcing_and_applications_in_realworld_tasks | open source]] work <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The objective was to help prepare for a potential future where reinforcement learning is integrated into the agent engineering loop <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Current Landscape of LLMs and Agents

Most Large Language Models (LLMs) today function primarily as chatbots or reasoners, excelling at question answering and interactive problem solving <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Models like O1, O3, R1, Gro3, and Gemini are adept at longer-form thinking <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. The current challenge lies in evolving these into "agents" (Level 3 in OpenAI's framework), which are systems capable of taking actions and performing longer, more complex tasks <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This is typically achieved by chaining multiple calls to underlying chatbot or reasoner LLMs, employing techniques like prompt engineering, tool calling, and human-in-the-loop evaluations <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

A distinction is made between "agents" and "pipelines" (or workflows):
*   **Pipelines** (or workflows) are systems with low degrees of autonomy, requiring significant engineering to define decision trees and refine prompts <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **Agents**, in the traditional reinforcement learning sense, are entities that interact with an environment with a goal, designed to learn and improve over time through repeated interaction <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

Current agents, such as those integrated into IDEs like Cursor, Warp, Surf, and Replit, or advanced search tools, often operate with very tight feedback loops and typically don't perform tasks for more than 10 minutes at a time <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. More autonomous examples include Devin, Operator, and OpenAI's Deep Research <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

## Model Trends and the Resurgence of RL

Traditional wisdom suggests waiting for better models to achieve more autonomous agents <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. However, pre-training shows diminishing returns on capital <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Reinforcement Learning from Human Feedback (RLHF), while good for friendly chatbots, doesn't seem to continuously push the frontier of smarter models <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Synthetic data helps distill larger models into smaller, performant ones but isn't a standalone unlock for massive capabilities without verification or rejection sampling <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

Reinforcement Learning (RL) has emerged as a key "trick," notably unlocking test-time scaling for O1 models in R1 <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. RL is not bottlenecked by manually curated human data and has proven effective <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

The release of DeepSeek's R1 model and paper was significant, as it was the first detailed explanation of how to build something akin to O1 <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The core mechanism was reinforcement learning: giving a model questions, measuring correctness, and iteratively feeding back information to encourage successful behaviors <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The long chain of thought seen in models like O1 and R1 emerged as a byproduct of this RL process, not from manual programming <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. RL's strength lies in identifying effective strategies for problem-solving <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### The Rise of [[open_source_models_vs_closed_models | Open Source Models]]

A notable trend is the resurgence of [[open_source_models_vs_closed_models | open source models]] <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. There is considerable excitement within the [[open_sourcing_and_applications_in_realworld_tasks | open source]] community, with efforts focused on:
*   **Replication:** Replicating projects like O1 <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Distillation:** Distilling data from larger models like O1 into smaller models <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

## Open Source Community's Impact: A Case Study

The speaker recounted an experience after the R1 paper's release, where he created a single Python file implementing the GRPO algorithm from a HuggingFace trainer with a small Llama 1B model to solve math questions <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. This experiment involved manually curating reward functions <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

Upon sharing this work on X (formerly Twitter), it demonstrated the model's self-correction, improved accuracy, and emergent longer chains of thought <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. While not a "true" replication, its simplicity resonated widely, taking on a life of its own in the [[open_sourcing_and_applications_in_realworld_tasks | open source]] community <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. People forked it, modified it for Jupyter notebooks, and wrote blog posts about it, drawn to its single-file, user-friendly nature that invited modification <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

This phenomenon highlighted "rubric engineering" – the process of designing rewards for RL beyond simple right/wrong answers <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Rewards could be given for adhering to formats (e.g., XML structure) or even partially correct answers (e.g., providing an integer answer in the correct format, even if the value is wrong) <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This allows the model to receive granular feedback and improve <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

Challenges in rubric engineering include:
*   Preventing "reward hacking," where the model finds loopholes to maximize reward without achieving the actual task <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   Opportunities lie in using LLMs to design or autotune rubrics and incorporating LM judges into scoring <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

Following this experience, the speaker has focused on creating more robust, usable [[open_sourcing_and_applications_in_realworld_tasks | open-source]] research code for RL in multi-step environments <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This framework allows users to create "environment" objects that models can plug into, enabling RL without needing to worry about model weights or tokens, only the interaction protocol <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## The Future of AI Engineering in the RL Era

The [[open_sourcing_and_applications_in_realworld_tasks | open source]] community has a significant role to play in building and growing the infrastructure, determining best practices, and creating necessary tools for this ecosystem <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

It is uncertain whether off-the-shelf API models will suffice for all tasks <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. Skills are difficult to include in prompts and are often acquired through trial and error, a process at which models also excel <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. This trial-and-error learning, facilitated by RL, has been the most promising unlock for higher autonomy agents like Deep Research <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

Fine-tuning, once dismissed, is regaining importance as the gap between [[open_source_models_vs_closed_models | open and closed source]] models narrows <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. Many platforms now use [[open_sourcing_and_applications_in_realworld_tasks | open source]] hosted models <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. True RL, as demonstrated by DeepSeek's R1 and OpenAI's Deep Research, requires explicit reinforcement learning <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

While many research questions remain unanswered, existing AI engineering skills are highly transferable <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. Building environments and rubrics for RL is conceptually similar to building evaluations and prompts <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. The ecosystem will continue to need robust monitoring tools and a broad range of supporting companies and platforms <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. The future of AI engineering may increasingly involve reinforcement learning to achieve truly autonomous agents, innovators, or language model-powered organizations <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.