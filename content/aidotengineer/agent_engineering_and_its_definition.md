---
title: Agent Engineering and its Definition
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

## The Evolution of AI Engineering

The field of [[State of AI Engineering | AI engineering]] has been undergoing significant maturation and expansion across various disciplines <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. Previous conferences have landmarked its progress:
*   **"The Rise of the AI Engineer"**: Focused on the emergence of the AI engineer <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
*   **"The Three Types of AI Engineer"**: Explored different archetypes within the field <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **"AI Engineer World's Fair"**: Highlighted the discipline's maturity and spread <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

While many initially viewed [[State of AI Engineering | AI engineering]] as either an extension of machine learning (ML) with some [[Importance of prompt engineering | prompt engineering]] <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, or primarily [[Impact of AI coding agents on software engineering | software engineering]] with calls to large language model (LLM) APIs <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>, it is emerging as its own distinct discipline <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. It is currently often described as "90% [[Impact of AI coding agents on software engineering | software engineering]], 10% AI," but this AI component is expected to grow significantly over time <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

## Defining Agent Engineering

The AI Engineer Summit has pivoted to become an [[Agent frameworks and orchestration layers in AI engineering | Agent Engineering]] conference <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This shift signifies a focused approach, opting to exclude topics like RAG, open models, and GPUs in favor of concentrating solely on agents <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This decision was influenced by YouTube's top-performing talks, which indicated a strong audience interest in "agentic things" <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. A new rule was implemented to prioritize talks from those *using* agent frameworks in production rather than just vendors creating them, making content curation more challenging but valuable <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

A common phrase, "2025 is the year of Agents," is a prediction pushed by prominent figures like Satya Nadella, Roman, Greg Brockman, and Sam Altman <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>. While there was initial skepticism among conference organizers, including a past recommendation to remove "agents" from branding <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>, that advice has now reversed <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

### What is an Agent?

Defining an agent is a "monumental task" <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. Different perspectives exist:
*   **Machine Learning (ML) perspective**: Focuses on reinforcement learning environments, actions, and achieving goals <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Software Engineering (SE) perspective**: Tends to be more reductive, often simplifying it to a "for loop" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

Simon Willison, considered a "patron saint" in the [[Evolution of AI engineering and tools | AI engineering]] community, has crowdsourced over 300 definitions for what constitutes an agent <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Common themes among these definitions include:
*   Goals <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Tools <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Long-running processes <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Small, multi-step task completion <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>

OpenAI also recently released a new definition for agents, which they are building upon <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

## Why Agents are Working Now

The current success of agents, compared to a year or two ago, can be attributed to several factors:
*   **Increased Capabilities**: Agent capabilities are rapidly growing and are beginning to hit human baselines <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   **Improved Reasoning and Tool Use**: Models now possess better reasoning and tool-use abilities <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   **Model Diversity**: The market share for models like OpenAI has diversified, with OpenAI's share dropping from 95% to 50% in two years, and new Frontier Model Labs emerging as potential challengers <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
*   **Lower Cost of Intelligence**: The cost of GPT-4 level intelligence has decreased by 1,000 times in the last 18 months <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **RL Fine-tuning Options**: New options for reinforcement learning (RL) fine-tuning are becoming available <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Charging for Outcomes**: The shift towards charging for outcomes rather than just costs <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
*   **Multi-agents and Faster Inference**: Advances in multi-agent systems and faster inference due to improved hardware <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

## Agent Use Cases

Several agent use cases have demonstrated product-market fit (PMF) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>:
*   **[[Impact of AI coding agents on software engineering | Coding agents]]** <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>
*   **Support agents** <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>
*   **Deep research agents** <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>

However, certain "anti-use cases" are discouraged from being demonstrated, such as agents that book flights or Instacart orders, as users often prefer to retain control over these tasks <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

## Impact on AI Product Growth

The growth of AI products, particularly platforms like ChatGPT, is tightly linked to reasoning capabilities and the deployment of agentic models <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>. OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. ChatGPT experienced a period of stagnant growth until it began shipping agentic models <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. The introduction of 01 models doubled ChatGPT's usage <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>, projecting it to reach one billion users by the end of the current year, a fivefold increase from September of last year <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. This growth indicates a significant opportunity for the wider AI industry <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.

## The Future of AI Engineering

The role of the [[The future of AI engineering | AI engineer]] is evolving to focus on building agents, similar to how ML engineers build models and [[Impact of AI coding agents on software engineering | software engineers]] build software <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. This shift underscores the increasing importance of agent engineering as a core discipline within the broader AI landscape.