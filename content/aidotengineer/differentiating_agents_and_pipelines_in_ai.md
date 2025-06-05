---
title: Differentiating Agents and Pipelines in AI
videoId: JIsgyk0Paic
---

From: [[aidotengineer]] <br/> 

Will Brown, a machine learning researcher at Morgan Stanley, discusses the distinction between AI [[components_of_ai_agents | agents]] and pipelines, highlighting the potential role of reinforcement learning (RL) in advancing [[developing_and_optimizing_ai_agents | agent]] capabilities. His talk aims to synthesize current research trends and speculate on the future of [[building_and_improving_ai_agents | AI engineering]], particularly concerning the [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent]] engineering loop <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>, <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>, <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## Current Landscape of LLMs <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>

Most Large Language Models (LLMs) currently operate as chatbots or reasoners, excelling at question answering and interactive problem solving <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Examples include models like GPT-4, Claude 3, and Gemini <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. To create [[components_of_ai_agents | agents]] (OpenAI's Level 3), which are systems that take actions and perform longer, more complex tasks, the common approach involves chaining multiple calls to these underlying chatbot or reasoner LLMs <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>, <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. This process often relies on prompt engineering, tool calling, evaluation (eval), and human-in-the-loop interventions <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>, <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. While these methods yield "pretty good" results, they do not yet achieve the high degree of autonomy often imagined for Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>, <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

## Agents vs. Pipelines <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>

Brown distinguishes between [[components_of_ai_agents | agents]] and pipelines:

*   **Pipelines** (also referred to as workflows) <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>:
    *   Characterized by fairly low degrees of autonomy <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.
    *   Require a non-trivial amount of engineering to define decision trees and prompt refinements <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
    *   Often feature tight feedback loops where a user interacts with an interface, receives quick responses, and guides the system <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
    *   Examples include Integrated Development Environments (IDEs) like Cursor, Wind, Surf, and Replit, as well as search tools for complex question answering with web integration <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>, <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. These systems typically perform tasks for less than 10 minutes at a time <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

*   **[[components_of_ai_agents | Agents]]**:
    *   Imply higher levels of autonomy, performing tasks for extended durations <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
    *   Few examples currently exist that truly embody this, with Devon, Operator, and OpenAI's Deep Research being notable exceptions <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>, <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

Traditionally, an [[components_of_ai_agents | agent]] in reinforcement learning (RL) is defined as a system that interacts with an environment with a specific goal, learning to improve its performance over time through repeated interactions <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>, <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. Brown notes that achieving higher performance (e.g., from 70% to 90% success) often requires models to learn from interaction rather than just relying on prompt tuning or static data <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>, <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.

## Reinforcement Learning as an Unlock <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>

Brown suggests that while traditional methods like pre-training and RLFH (Reinforcement Learning from Human Feedback) have their benefits, they face diminishing returns or limitations in pushing the frontier of capabilities <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>, <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Synthetic data is good for distilling models but not for massive capability unlocks on its own <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

Reinforcement learning (RL) appears to be the key trick for achieving "test-time scaling" <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>. DeepSeek's R1 model and paper, which explained the architecture of models like GPT-4, demonstrated that RL is used to enable long chains of thought and complex reasoning <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>, <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. RL identifies good strategies for solving problems by giving models questions, measuring correctness, and providing feedback to encourage successful behaviors <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>, <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.

RL operates on the principle of "explore and exploit": trying different approaches, identifying what works, and then doing more of what worked <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. An example is a model writing code to pass test cases, receiving numerical rewards for formatting, language use, and ultimately passing tests <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. This feedback loop allows models to learn from synthetic data rollouts and refine their strategies <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. The GRPO algorithm, used by DeepSeek, simplifies this process: sample completions, score them, and tell the model to be more like the higher-scoring ones <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

### RL for Autonomous Agents <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>
OpenAI's Deep Research, an example of a more autonomous system, was built with end-to-end reinforcement learning, enabling it to make potentially hundreds of tool calls for browsing and querying to synthesize answers <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>, <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>. While impressive, such [[different_architectures_for_ai_agents | agents]] still struggle with out-of-distribution tasks or highly manual calculations, indicating that RL is a big unlock for new skills and autonomy, but not a universal solution for all problems <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>, <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. It is particularly effective for teaching skills and improving performance in conjunction with environments, tools, and verification <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>, <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

## Challenges and Opportunities <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>

The [[scaling_ai_agents_in_production | integration of AI agents into existing infrastructure]] via RL is still in its early stages. Key questions remain:
*   Cost of RL training <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   Minimum model size for effectiveness <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>.
*   Generalization across tasks <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>.
*   Designing effective rewards and environments <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.

This presents significant opportunities for:
*   **Open-source infrastructure**: Building and defining best practices <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
*   **Tooling companies**: Supporting the RL ecosystem <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.
*   **Services**: Dedicated to supporting agentic RL <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.

Brown also mentions that even at the prompt level, automation can mimic RL's flavor, such as with DSPI, which uses a signal to improve a system based on downstream scores <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>, <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>.

### Rubric Engineering <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>
Inspired by the public's engagement with a simple Python file demonstrating RL, Brown introduces "rubric engineering." This concept is analogous to prompt engineering but for defining rewards in RL <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>, <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>. Instead of just a binary right/wrong score, models can be given points for following specific formats (e.g., XML structure) or demonstrating progress even if the final answer is incorrect <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>, <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.

Rubric engineering allows for creative design of rules that not only help developers evaluate performance but also provide direct feedback to the model for further training <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>, <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>. Future work in this area could involve using LLMs to design or auto-tune rubrics and prompts, incorporating LLM judges into scoring, and guarding against "reward hacking" (where models find loopholes to achieve high rewards without performing the actual task) <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>, <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

Brown is developing an open-source framework to facilitate RL in multi-step environments, allowing users to leverage existing API model [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks]] to run RL experiments <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>, <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>. The goal is to enable users to define interaction protocols and environments, then let a model learn and improve over time with rewards <a class="yt-timestamp" data-t="15:18:00">[15:18:00]</a>, <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.

## The RL Era in AI Engineering <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>

The speaker posits that off-the-shelf API models might not always suffice because skills are hard to embed in prompts; they are often learned through trial and error <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>, <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. This trial-and-error process, facilitated by RL, has proven to be the most promising path for creating higher-autonomy [[components_of_ai_agents | agents]] like Deep Research <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>, <a class="yt-timestamp" data-t="16:21:00">[16:21:00]</a>.

Fine-tuning, once dismissed, is gaining renewed importance as the gap between open and closed-source models narrows <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>. True RL (as used by DeepSeek and OpenAI) necessitates fine-tuning based on reinforcement learning feedback <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.

While challenges remain, existing [[building_and_improving_ai_agents | AI engineering]] skills—such as building evaluations (evals) and crafting prompts—directly translate to the new challenges of building environments and designing rubrics <a class="yt-timestamp" data-t="17:08:00">[17:08:00]</a>, <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>. Continued development of monitoring tools and a supportive ecosystem of companies and platforms will be crucial for the types of [[components_of_ai_agents | agents]] engineers aim to build <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>, <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>. The future of AI engineering may increasingly involve reinforcement learning to unlock truly autonomous [[components_of_ai_agents | agents]] and AI-powered organizations <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>, <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.