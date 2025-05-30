---
title: Trends in alignment research and AI safety
videoId: W1aGV4K3A8Y
---

From: [[redpointai]] <br/> 

The field of AI alignment research focuses on ensuring AI systems act in ways that are beneficial and safe for humanity. Recent advancements in large language models (LLMs) have brought this area into sharper focus, with discussions on current progress, challenges, and future implications.

## Current State of Alignment Research

Alignment research has seen significant progress, particularly in the area of interpretability. Last year, the field was just beginning to discover superposition and features within models, representing a substantial leap in understanding. Now, researchers have meaningfully identified circuits in frontier models and can characterize their behaviors, as detailed in papers like "The Biology of a Large Language Model" <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.

While a full characterization of models is not yet available, and difficult cases persist, the models themselves are "quite good" <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a> at generally ingesting human values through pre-training, making them "default aligned" in many ways <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>. However, this default alignment is not guaranteed after Reinforcement Learning (RL), as RL processes can lead models to do "anything to achieve the goal" <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>, requiring careful oversight <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a>.

### Interpretability Agents and Auditing Games
Anthropic has been developing an interpretability agent designed to find circuits in language models <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This agent, although primarily a coding agent, can use its knowledge of theory of mind and access to visualization tools (for neurons and circuits) to reason through and understand other models <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

This capability has been demonstrated in the "auditing game," an [[concerns_and_considerations_for_ai_safety_and_regulation | alignment safety]] evaluation where a model is intentionally "twisted," and the agent must identify what is wrong with it <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. The agent can converse with the flawed model, generate hypotheses about the problem, and utilize its tools to diagnose issues <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. This showcases the generalizable competence of models equipped with tools and memory <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Reliability and Future Trajectory
A key metric for agent success is reliability, specifically the success rate over time horizon <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. While not 100% reliable yet, and a gap exists between one-shot performance and multiple attempts, the progress is significant <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. The current [[trends_in_ai_model_training_and_deployment | trend lines]] suggest that "expert superhuman reliability" will be achieved for most tasks that models are trained on <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

A potential concern would be if models were to "fall off trend line," particularly in coding, which serves as a leading indicator for AI capabilities <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. However, confidence remains high that current algorithms do not have inherent limitations that would prevent this progress <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

By the end of 2025, it is expected that general-purpose agents will be capable of handling various personal tasks, like filling out forms and navigating the internet, demonstrating a high degree of reliability <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. This is partly due to the ability to provide models with practice reps and verifiable feedback loops, similar to how humans learn <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

## AI Progress and Societal Impact
The current paradigm of pre-training plus RL is widely believed to be sufficient for achieving AGI, as [[challenges_and_advancements_in_ai_technology | trend lines]] continue upwards without bending <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.

The initial economic impact of AI is projected to resemble China's emergence, but at a dramatically faster pace <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. By 2027 or 2028, or certainly by the end of the decade, models are expected to be capable of automating any white-collar job <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This is because such tasks are highly susceptible to current algorithms, benefiting from extensive data and computational repeatability <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.

However, a potential mismatch exists: while white-collar work will be significantly impacted, progress in fields like robotics or biology will require more extensive data collection and infrastructure (e.g., automated laboratories, vast numbers of robots) <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. To fully realize meaningful changes to global GDP and pull forward material abundance (like advancements in medicine), these physical feedback loops need to be established <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

## Policy and Preparedness

### Call for Government Action
Governments are urged to:
*   **Viscerally understand AI trend lines:** Policymakers need to break down economic sectors and job types, measure AI capability improvements in these areas, and establish national benchmarks to plot [[the_evolving_landscape_of_ai_regulation_and_safety | trend lines]] that reveal future impacts, such as by 2027 or 2028 <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.
*   **Invest in alignment science:** Substantial investment is needed in research that makes models understandable, steerable, and honest <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>. This "science of alignment" has primarily been driven by frontier labs, but universities should also increase their focus on it, as it represents the fundamental science of LLMs <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>. The lack of inclusion of mechanistic interpretability workshops in major conferences like ICML is seen as a missed opportunity for raw scientific discovery <a class="yt-timestamp" data-t="00:48:36">[00:48:36]</a>.
*   **Address energy limitations:** The increasing compute demands of AI models will lead to significant energy consumption, potentially reaching 20% of US energy production by 2028 <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. Governments must invest more in energy infrastructure to avoid bottlenecks, contrasting the flat energy production in the US with China's rapid growth <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.

### The AI 2027 Work
The "AI 2027" work, which speculates on the future of AI, is considered "very plausible" <a class="yt-timestamp" data-t="00:45:54">[00:45:54]</a>. While there are branching possibilities and the projected scenario might represent a 20th percentile case, its mere possibility is significant <a class="yt-timestamp" data-t="00:46:03">[00:46:03]</a>. The timeline of "drop-in remote worker AGI" by 2027 is widely accepted among leading AI labs like Anthropic, Google DeepMind, and OpenAI <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>.

Even if individuals have lower confidence in this timeline (e.g., 10-20% chance), governments and countries should still prioritize planning for it as the number one issue for future change <a class="yt-timestamp" data-t="00:56:17">[00:56:17]</a>.

## Underhyped Areas and Optimistic Outlook
One underhyped area is "world models," which could enable AI models to generate virtual worlds with accurate physics understanding, potentially leveraging advancements in augmented and virtual reality <a class="yt-timestamp" data-t="00:51:33">[00:51:33]</a>. This physics understanding has already been demonstrated in video models that accurately reflect light and shadows in novel scenarios <a class="yt-timestamp" data-t="00:52:10">[00:52:10]</a>. This technology could also translate to applications like virtual cells <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>.

While software engineering has seen the most impact from AI, there is "a lot of headroom" <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a> in almost every other field for underexplored applications <a class="yt-timestamp" data-t="00:53:25">[00:53:25]</a>. The principles of async background software agents, like those found in Claude Code, Cursor, and WindinSurf, have yet to be fully translated to other domains <a class="yt-timestamp" data-t="00:53:32">[00:53:32]</a>.

The speaker believes that AI will empower individuals to be dramatically more creative, transforming societal consumption habits into active creation <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. People will gain the leverage of an entire company of talented models or individuals, leading to significantly better lives and addressing current societal challenges <a class="yt-timestamp" data-t="00:50:36">[00:50:36]</a>.