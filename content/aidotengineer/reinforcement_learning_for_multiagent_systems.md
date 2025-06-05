---
title: Reinforcement Learning for Multiagent Systems
videoId: JIsgyk0Paic
---

From: [[aidotengineer]] <br/> 

Reinforcement Learning (RL) is a paradigm where a system is designed to learn how to improve at achieving a goal over time through repeated interaction with an environment <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This approach is seen as crucial for the future development of more autonomous and capable [[Developing and optimizing AI agents | AI agents]] <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Speaker's Background
Will Brown, a machine learning researcher at Morgan Stanley, previously conducted theoretical work on [[multiagent_systems_and_their_applications | multi-agent reinforcement learning]] at Columbia University <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. His current work at Morgan Stanley involves Large Language Model (LLM) related projects, some of which resemble [[Stateful AI Agents | agents]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## The Evolution of AI Agents
Current LLMs largely function as chatbots or reasoners, excelling at question answering and interactive problem solving <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. While models like GPT-4, Claude 3, and Gemini are adept at longer thinking processes <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, advancing to [[Building and Improving AI Agents | agent]] level systems (Level 3 in OpenAI's framework) means creating systems that can take actions, perform longer, harder, and more complex tasks <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Currently, [[Building and Improving AI Agents | agents]] are often built by chaining multiple calls to underlying LLMs, using techniques like prompt engineering, tool calling, and human-in-the-loop evaluations <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. While effective for tasks with tight feedback loops (e.g., IDEs like Cursor, Warp, Replit, or advanced search tools) <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, few [[Stateful AI Agents | agents]] currently operate autonomously for extended periods, beyond 10 minutes at a time <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Examples of more autonomous [[Stateful AI Agents | agents]] include Devin, Operator, and OpenAI's Deep Research <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

The challenge lies in how to increase the autonomy of these systems <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. While waiting for "better models" is a common approach <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, RL provides a path forward for teaching models to improve skills through trial and error <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## How Reinforcement Learning Works for Agents
The core idea of RL is to "explore and exploit": try various actions, observe what works, and then favor successful actions while reducing unsuccessful ones <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This feedback loop allows a model to learn from synthetic data rollouts and scores <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

A key algorithm demonstrating this is GRPO (Generalized Reinforcement Learning with Policy Optimization), used by DeepSeek for their R1 model <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. The GRPO algorithm involves:
1.  Sampling multiple completions (n) for a given prompt <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
2.  Scoring all completions <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
3.  Instructing the model to behave more like the higher-scoring completions <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

This process enables models to learn effective strategies for problem-solving, leading to emergent behaviors like long chains of thought, as seen in models like O1 and R1 <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

## RL's Role in Agentic Capabilities
RL has been a significant unlock for capabilities, particularly in [[reinforcement_learning_in_large_language_models | test-time scaling]] <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **DeepSeek R1**: This model demonstrated that RL could teach a model to perform complex reasoning, like solving math questions, by learning to self-correct and utilize longer chains of thought based on accuracy rewards <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **OpenAI's Deep Research**: This system uses end-to-end RL to take potentially hundreds of tool calls, browsing and querying the internet to synthesize large answers <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. While impressive, it still faces [[Challenges and solutions in scaling AI agents | limitations]] with out-of-distribution tasks or highly manual calculations <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

While RL significantly enhances autonomy and skill acquisition, it does not automatically grant [[Stateful AI Agents | agents]] the ability to solve all kinds of problems universally <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. It is a path for teaching models specific skills, especially when combined with environments, tools, and verification mechanisms <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Infrastructure and Future Directions
Current RL infrastructure for LLMs is largely RLHF (Reinforcement Learning from Human Feedback) style, focused on single-turn interactions with human-curated reward signals <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. The future envisions RL [[Stateful AI Agents | agents]] as part of more complex systems, potentially supported by API services from large labs allowing fine-tuning for specific tasks <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

[[Challenges and Techniques in Reinforcement Learning for Agents | Key challenges]] and opportunities for this ecosystem include:
*   **Cost and Model Size**: Determining the economic viability and minimum effective model size <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Generalization**: Ensuring models can generalize learned skills across different tasks <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Reward and Environment Design**: Developing effective reward signals and environments <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Rubric Engineering
A promising approach for designing rewards is "rubric engineering," where models are given points for specific aspects of their output, beyond just correctness <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Examples include rewarding adherence to XML structures or correct answer formats, even if the final numerical answer is wrong <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This allows models to receive continuous feedback and improve <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

Future advancements in rubric engineering could involve using LLMs to design or autotune rubrics, incorporating LLM judges into scoring, and diligently preventing "reward hacking" <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Multi-step Environments
New open-source efforts are focusing on frameworks for doing RL within [[multiagent_systems_and_their_applications | multi-step environments]] <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. The goal is to leverage existing agent frameworks for API models and allow models to plug into these environments, learning from interaction protocols without needing to manage weights or tokens directly <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. This represents a step towards truly autonomous [[Multiagent orchestration for AI copilot development | multiagent orchestration for AI copilot development]] or organizational systems powered by LLMs <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

AI engineering skills developed in recent years, such as building evaluations and prompts, directly translate to the [[Challenges and Techniques in Reinforcement Learning for Agents | challenge]] of building environments and rubrics for RL <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. Continued development of monitoring tools and a supportive ecosystem are essential for this advancement <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.