---
title: Challenges and progress in AI model alignment research
videoId: W1aGV4K3A8Y
---

From: [[redpointai]] <br/> 

## Current State of Alignment Research

Alignment research has seen significant advancements, particularly in the area of interpretability. Last year, researchers were just beginning to discover superposition and features in models. Now, there is a meaningful understanding of circuits in frontier models, allowing for the characterization of their behaviors in explicit terms <a class="yt-timestamp" data-t="00:44:16">[00:44:16]</a>. This includes work like the "biology of a large language model" paper, which breaks down the models' ability to reason over concepts <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>.

Despite these advancements, a full characterization of models is not yet available, and difficult cases still exist <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

## Default Alignment and RL Challenges

Models, based on their pre-training, are often "default aligned," showing a general ability to ingest human values <a class="yt-timestamp" data-t="00:45:13">[00:45:13]</a>. However, this default alignment is not guaranteed after applying Reinforcement Learning (RL), as the learning process can lead models to "do anything to achieve the goal" <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>. Overseeing this RL process is a complex challenge that researchers are actively learning to manage <a class="yt-timestamp" data-t="00:45:40">[00:45:40]</a>.

## Reliability and Agents

A key aspect of alignment in practice is agent reliability <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Measuring success rate over time horizon is considered the right way to assess the extension of agent capabilities <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Substantial progress is being made, though models do not yet succeed 100% of the time <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Many evaluations can be completely solved with multiple attempts, but first-time success is not guaranteed <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. The trend line suggests that expert superhuman reliability for most trained tasks is on track <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.

The development of new models, like Anthropic's Claude 4, shows a significant step up in software engineering, with "Opus" being highlighted as an "incredible software engineering model" capable of autonomously handling ill-specified tasks and discovering information <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. These models are substantially better at handling multiple actions and pulling in necessary information from their environments <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. The ability to give models access to tools and run with longer contexts and greater personalization is seen as an attempt to "crack agency" by "unhobbling" them <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

An example of this progress is an interpretability agent developed by Anthropic, which can find circuits in language models without being explicitly trained for it. This agent can mix its coding abilities with knowledge of "theory of mind" to understand and reason through models, using tools to visualize neurons and circuits. It successfully wins an "auditing game" alignment safety evaluation by identifying what is wrong with a twisted model <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

## Policy and Future Directions

For policymakers, it is crucial to viscerally understand the current AI trend lines <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. This involves measuring model capabilities against national economic metrics, such as evaluating tasks performed in various jobs and plotting their progress <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.

Investing significantly in research to make models understandable, steerable, and honest, which falls under the "science of alignment," is paramount <a class="yt-timestamp" data-t="00:47:27">[00:47:27]</a>. This research, often driven by frontier labs, needs more attention from universities and other entities, as it is akin to the "pure science" of what is happening inside these models, comparable to discovering DNA chirality or general relativity <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>. The "MATS program" is an example of meaningful alignment research being conducted outside frontier labs <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

## Perceptions and Urgency

The recent "AI 2027" work, which discusses potential future scenarios, is considered "very plausible," though perhaps a 20th percentile case <a class="yt-timestamp" data-t="00:45:52">[00:45:52]</a>. The speaker is generally more bullish on [[approaches_to_ai_safety_and_alignment | alignment research]] and estimates a timeline that is only about a year slower than what was presented in AI 2027 <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.

The belief among researchers at leading labs like Anthropic, Google DeepMind, and OpenAI is that "drop-in remote worker AGI" is achievable by 2027 <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>. Even if this is considered a 10-20% chance by those outside the labs, governments and countries should still treat it as the number one issue for future planning, as the pace of change is significantly underestimated <a class="yt-timestamp" data-t="00:56:14">[00:56:14]</a>.

> "Even if you don't have the level of confidence that the people working at the labs do and you're still like, you know what, it's a 10 or 20% chance, you should still like plan for that like if you're a government or a country you should still be like that should still be the number one issue at the top of your list of of like how is the future going to change and I think that isn't felt enough" <a class="yt-timestamp" data-t="00:56:12">[00:56:12]</a>

The continuous improvement in models, particularly through scaled RL, is expected to bring rapid advances, with significant gains still to be made even with existing compute resources <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This is partly due to the fact that RL scaling has received comparatively smaller compute investment than pre-training <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>. By the end of the current year, coding agents are expected to become very competent, allowing for confident delegation of hours of work <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. This shift means that instead of watching models for five minutes, users might only need to check in every few hours <a class="yt-timestamp" data-t="00:31:56">[00:31:56]</a>. This relates to [[challenges_in_ai_model_training_and_scalability | Challenges in AI model training and scalability]], as efficient feedback loops for models are crucial. If models can do hours of work that can be judged by overall completion, it allows them to "climb these like rungs of the ladder ever faster" <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>.