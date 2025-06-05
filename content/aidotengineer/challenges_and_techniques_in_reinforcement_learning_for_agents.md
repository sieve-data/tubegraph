---
title: Challenges and Techniques in Reinforcement Learning for Agents
videoId: JIsgyk0Paic
---

From: [[aidotengineer]] <br/> 

Will Brown, a machine learning researcher at Morgan Stanley, discusses the meaning of reinforcement learning (RL) for agents and potential future directions in AI engineering <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. His background includes working on theory for [[reinforcement_learning_for_multiagent_systems | multi-agent reinforcement learning]] at Columbia <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The talk focuses on where the field might be headed, offering speculation and insights from recent open-source work <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The goal is to help prepare for a future where reinforcement learning is part of the agent engineering loop <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Current State of LLMs and Agents

Most Large Language Models (LLMs) today function as chatbots <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Using OpenAI's five-levels framework, significant progress has been made with chatbots and reasoners, which are effective for question-answering and interactive problem-solving <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The next step is to elevate these to "agent level three" systems that can take actions and perform longer, more complex tasks <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Currently, agents are often built by chaining multiple calls to underlying chatbot or reasoner LLMs <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This involves techniques such as:
*   Prompt engineering <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   Tool calling <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   Eval (evaluation) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>
*   Integrating humans in the loop <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>

While these methods yield good results for many tasks, the field has not yet reached a point where AI agents operate with the high degree of autonomy imagined for Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Agents vs. Pipelines

It is helpful to distinguish between "agents" and "pipelines" (or workflows) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Pipelines are systems with lower degrees of autonomy, requiring significant engineering to define decision trees and refine prompts <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Many successful applications in the agent space utilize very tight feedback loops, where users interact with an interface, tasks are performed quickly, and results are returned promptly <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Examples include integrated development environments (IDEs) like Cursor, Warp, Surf, and Replit, and search tools that integrate web search or research <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Currently, few agents can perform tasks for more than 10 minutes at a time <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Exceptions that demonstrate a more autonomous direction include Devin, Operator, and OpenAI's Deep Research <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Limitations of Current Approaches

The traditional wisdom suggests that better models will automatically enable more capable agents <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. However, the traditional definition of reinforcement learning defines an agent as something that interacts with an environment with a goal, designed to learn and improve over time through repeated interaction <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Many current approaches lack the tools to automatically improve performance from 70% to 90% when prompt tuning or existing models struggle <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Model Trends and New Tricks

*   **Pre-training**: Showing diminishing returns on capital, suggesting a need for new techniques <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Reinforcement Learning from Human Feedback (RLHF)**: Excellent for creating friendly chatbots, but not consistently pushing the frontier of smarter models <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Synthetic Data**: Useful for distilling larger models into smaller, performant ones, but not a standalone unlock for massive capability improvements without verification or rejection sampling <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Reinforcement Learning (RL)**: Appears to be the key trick for test-time scaling, as seen in models like O1 and R1 <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. It is not bottlenecked by manual human data curation and has proven effective <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Reinforcement Learning for Reasoning and Agents

DeepSeek's R1 model and paper were significant because they explained how to build a model like O1, revealing that it was essentially reinforcement learning <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The process involves:
1.  Giving the model questions <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  Measuring if the answer is correct <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
3.  Iteratively providing feedback to encourage more successful behaviors and less unsuccessful ones <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

This process can lead to the emergence of long chains of thought, as observed in O1 and R1 models, without explicit manual programming <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. RL is fundamentally about identifying good strategies for problem-solving <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

Open-source models are also seeing a resurgence, with community efforts to replicate O1 and distill its data into smaller models <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## How Reinforcement Learning Works

The core idea of RL is "explore and exploit": trying different approaches, observing what works, and then doing more of what succeeded and less of what failed <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

For example, in a coding task, rewards can be given for formatting, using the correct language, and ultimately, passing test cases <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This numerical feedback allows the model to generate synthetic data rollouts, receive scores, and feed them back into the model for improvement <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### GRPO Algorithm

The GRPO algorithm, used by DeepSeek, is conceptually simple for RL:
1.  For a given prompt, sample N completions <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
2.  Score all completions <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
3.  Instruct the model to generate responses that are more similar to those with higher scores <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
This still often operates within a single-turn reasoner model <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Challenges in Developing AI Agents with RL

While RL can unlock new skills and greater autonomy, as demonstrated by OpenAI's Deep Research (an end-to-end RL system taking up to 100 tool calls for web browsing and querying) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, it doesn't solve all problems <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Deep Research struggles with out-of-distribution tasks or very manual calculations, indicating that RL alone does not grant agents the ability to do everything <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. However, it is a path for teaching models specific skills and improving them through interaction with environments and tools <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Infrastructure and Ecosystem [[challenges_in_developing_ai_agents | Challenges in Developing AI Agents]]

Existing infrastructure for RL is often RLHF-style, relying on reward signals from human-curated data <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. For RL agents to become integral to our systems, we would need:
*   Robust API services from large labs for building and fine-tuning these models <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   Multi-step tool calling capabilities <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Key unknown [[design_challenges for AI agents | questions]] and [[challenges_in_developing_ai_agents | challenges]] in this ecosystem include:
*   The cost of training these models <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   How small the models can be <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   Generalization across tasks <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   How to [[design_challenges_for_ai_agents | design good rewards]] and environments <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

This presents significant opportunities for open-source infrastructure development, defining best practices, and building tools and services to support agentic RL <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Beyond literal RL training, automation at the prompt level, like DSPI, can also provide signals for system improvement <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Rubric Engineering

A specific technique emerging with RL for LLMs is "rubric engineering" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>. Similar to prompt engineering, this involves designing the reward system for the model <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. Rewards don't just have to be binary (right/wrong answer); they can include points for:
*   Following specific formatting (e.g., XML structure) <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   Adhering to answer types (e.g., an integer answer, even if incorrect) <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

This allows for creative rule design that provides actionable feedback to the model for further training <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. Areas for further exploration include using LLMs to design or auto-tune rubrics and prompts, and incorporating LM judges into scoring systems <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### Reward Hacking

A significant [[challenges_in_building_reliable_ai_agents | challenge]] to be cautious of is "reward hacking" <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This occurs when the reward model does not accurately capture the true goal, allowing the agent to find "back doors" to achieve a high reward without actually performing the intended task <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

## Open-Source Efforts and Frameworks

An open-source effort aims to provide a more robust framework for RL within multi-step environments <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The goal is to leverage existing agent frameworks and API models by allowing users to create an "environment" that the model plugs into <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This abstracts away concerns about model weights or tokens, enabling users to define an interaction protocol that feeds into a trainer, allowing the model to improve over time with rewards <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

## The Future of AI Engineering in the RL Era

It is uncertain whether off-the-shelf API models will suffice for all tasks <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. A key reason is that while knowledge can be included in a prompt, skills are hard to convey <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. Like humans, models often require trial and error to truly master a skill <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. This trial-and-error approach, central to RL, has been the most promising unlock for higher autonomy agents like Deep Research <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.

### Importance of Fine-Tuning [[building_and_improving_ai_agents | Building and Improving AI Agents]]

Fine-tuning, previously somewhat disregarded, is regaining importance <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. The gap between open and closed-source models is narrowing, making open-source hosted models viable for platforms <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. Additionally, the "true" versions of RL, as seen in DeepSeek's R1 and OpenAI's Deep Research, necessitate reinforcement learning <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

Many [[challenges_in_developing_ai_agents | research questions]] remain unanswered regarding RL in AI engineering <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. However, existing AI engineering skills directly translate to this new paradigm:
*   The [[design_challenges_for_ai_agents | challenge of building environments]] and rubrics is akin to building evals and prompts <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   Good monitoring tools are still essential <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
*   A large ecosystem of companies, platforms, and products is needed to support the desired types of agents <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.

These existing skills will be crucial if the field moves towards a future requiring more reinforcement learning to unlock truly autonomous agents, innovators, or language model-powered organizations <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.