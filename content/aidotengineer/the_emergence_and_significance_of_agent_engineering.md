---
title: The emergence and significance of agent engineering
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

The field of [[ai_engineering_trends | AI engineering]] is undergoing a significant transformation, with a notable pivot towards [[role_of_ai_agents_and_agentic_frameworks | agent engineering]]. This shift marks a new phase in the discipline's maturity, driven by evolving capabilities and increasing demand for sophisticated AI applications <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

## Current State of AI Engineering

AI engineering has seen considerable growth, marked by publications like an O'Reilly book on the topic <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. Historically, past summits have aimed to landmark the state of the industry, covering topics such as the rise of the AI engineer, the three types of AI engineers, and the discipline's maturation and spread <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>.

Despite this progress, there's a perceived "peak" by some, including Gartner, suggesting a potential decline <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. However, the discipline continues to evolve, facing resistance from those who view it as either an extension of ML engineering with "a few prompts" <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a> or primarily software engineering "calling a few LLM APIs" <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. The speaker anticipates [[ai_engineering_trends | AI engineering]] will emerge as its own distinct discipline, growing beyond its current 90% software engineering and 10% AI composition <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## The Pivot to Agent Engineering

The AI Engineer Summit has deliberately pivoted to become the [[role_of_ai_agents_and_agentic_frameworks | agent engineering]] conference, a decision not made lightly <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This focus means saying "no" to other areas like RAG (Retrieval-Augmented Generation), open models, and GPUs, in favor of concentrating solely on agents <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This strategic narrowing has opened new doors, attracting speakers who work on [[role_of_ai_agents_and_agentic_frameworks | agent frameworks]] <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. A new rule has been implemented to exclude vendor pitches, prioritizing insights from those actively putting agents into production <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.

It has been observed that "everything plus agent works," with combinations like "agent plus RAG," "agent plus sent," and "agent plus search" proving effective <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

### Defining an Agent

A crucial step in any agent conference is defining what an agent is <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Perspectives vary:
*   **Machine Learning**: Views agents in the context of reinforcement learning environments, focusing on actions achieving goals <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Software Engineers**: Tend to be more reductive, sometimes simply equating it to a for-loop <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

Simon Willison, considered a "patron saint" in the [[ai_engineering_trends | AI engineering]] community, has crowdsourced over 300 definitions <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Common themes in these definitions include:
*   Goals <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Tools <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>
*   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Long-running processes <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>
*   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Small multi-step task completion <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>

OpenAI also recently released a new definition of agents that warrants attention, as they are building upon it <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>. This evolving definition of [[the_role_and_definition_of_agents_in_ai | agents]] highlights the dynamic nature of the field.

## Why Agents are Working Now

The current effectiveness of agents, compared to a year or two ago, is attributed to several key factors:
*   **Increased Capabilities**: AI capabilities have significantly grown, reaching human baselines around 2023-2025 <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>. This includes better reasoning, improved tool use, and more advanced tools <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   **Model Diversity**: OpenAI's market share has decreased from 95% two years ago to about 50% now, indicating a much more diverse model landscape <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. The emergence of two new Frontier Model Labs in the past week also adds to this diversity <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.
*   **Lower Cost of Intelligence**: The cost of GPT-4 level intelligence has decreased by 1,000 times in the last 18 months, with similar trends for other intelligence levels <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **RL Fine-tuning Options**: The availability of RL fine-tuning options further enhances agent development <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Focus on Outcomes**: Conversations with leaders like Brett Taylor highlight the shift towards charging for outcomes rather than just costs <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
*   **Multi-agents and Faster Inference**: Advancements in multi-agent systems and faster inference due to better hardware contribute significantly <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

These factors collectively contribute to [[the_impact_and_future_potential_of_ai_and_agents | the impact and future potential of AI and agents]], making agents more viable and effective now than ever before.

## Agent Use Cases and Anti-Use Cases

Certain agent use cases are showing clear product-market fit (PMF):
*   **Coding Agents**: These agents assist in generating, debugging, and optimizing code <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
*   **Support Agents**: These agents provide automated customer service and support <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
*   **Deep Research Agents**: These agents excel at conducting thorough research <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

There are also "anti-use cases" that should be avoided:
*   **Flight Booking Agents**: The speaker suggests allowing users to book their own flights <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.
*   **Instacart Order Agents**: Similarly, users prefer to manage their own grocery orders <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>.
*   **Astroturfing Agents**: Agents used for deceptive online campaigns are to be avoided <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.

These examples offer insight into [[building_effective_agents | building effective agents]] by focusing on areas where automation truly adds value without removing user agency or being deployed for harmful purposes.

## The Future of AI and Agents

The growth of AI products, particularly in agentic models, is significant. OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>. ChatGPT usage dramatically increased after the introduction of [[ai_agents_and_agentic_workflows | agentic models]], doubling its usage <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. It is projected that ChatGPT could reach a billion users by the end of the year, quintupling its user base from September of last year <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

This massive growth underscores that the growth of any AI product is "very, very tight to reasoning capabilities and the amount of agents that you can ship for your users" <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. The role of the AI engineer is now evolving towards [[role_of_engineering_teams_in_ai_agent_production | building agents]], much like ML engineers build models and software engineers build software <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a>.