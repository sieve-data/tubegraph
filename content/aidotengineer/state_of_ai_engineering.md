---
title: State of AI Engineering
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

## Current Status and Evolution
AI engineering is an evolving discipline, with varying perspectives on its core identity <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. While some machine learning engineers view it as an extension of ML with a few prompts, software engineers often see it as mostly software engineering with calls to LLM APIs <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. Currently, it's described as approximately 90% software engineering and 10% AI, a proportion expected to grow over time <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. The discipline is maturing and spreading across different fields <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

Previous "state of the industry" talks have covered:
*   The rise of the AI engineer <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
*   The three types of AI engineers <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>
*   The maturation and spread of AI engineering <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>

The sentiment around AI engineering varies; an O'Reilly book suggests a positive outlook <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, while Gartner believes it has peaked and is now in decline <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

[[evolution_of_ai_engineering_and_tools | Evolution of AI Engineering and Tools]]

## The Pivot to Agent Engineering
The AI Engineer Summit has strategically pivoted to become an agent engineering conference <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This focus means saying "no" to other topics like RAG, open models, and GPUs, to concentrate solely on agents <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. This decision was driven by audience interest, as top-performing talks last year favored agent-related content <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. A new rule for speakers requires a focus on production deployment rather than just vendor pitches <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. The belief is that "everything plus agent works," such as agent plus RAG, agent plus search, or agent plus sentiment analysis <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

## Defining an Agent
Defining "agent" is a monumental task, with various interpretations <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
*   **Machine Learning (ML) perspective:** Focuses on reinforcement learning environments, actions, and achieving goals <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Software Engineering (SE) perspective:** Often simplifies it to a for loop <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

Simon Willison has crowdsourced over 300 definitions <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>, which generally revolve around:
*   Goals <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Tools <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Long-running processes <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Small, multi-step task completion <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>

OpenAI also recently released a new definition of agents that the community should pay attention to <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

## Why Agents are Working Now
The current success of agents, compared to previous years, is attributed to several factors <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>:
*   **Improved Capabilities:** AI capabilities, including reasoning and tool use, have significantly grown and are hitting human baselines around 2025 <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.
*   **Model Diversity:** OpenAI's market share has decreased from 95% to 50% in two years, leading to a much more diverse landscape of models <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. New Frontier Model Labs are emerging as potential challengers <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Reduced Cost of Intelligence:** The cost of GPT-4 level intelligence has decreased by 1,000 times in the last 18 months <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **RL Fine-tuning Options:** The availability of reinforcement learning fine-tuning options <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Focus on Outcomes:** Shifting focus from charging for costs to charging for outcomes <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.
*   **Multi-agents and Faster Inference:** Advancements in multi-agent systems and faster inference due to better hardware <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

Despite skepticism from some in the community who are "tired of hearing about agents" <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>, industry leaders like Satya Nadella, Roman, Greg Brockman, and Sam Altman predict that 2025 will be the year of agents <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. David Luan, former VP at OpenAI, initially advised against branding with agents but now suggests putting it back on <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

[[state_of_the_ai_frontier_in_2025 | State of the AI Frontier in 2025]]

## Agent Use Cases
Agents are seeing product-market fit (PMF) in areas such as [[impact_of_ai_coding_agents_on_software_engineering | coding agents]] and support agents <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Deep research agents also have PMF <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.

However, certain "anti-use cases" should be avoided:
*   Demoing agents that book flights <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>
*   Booking Instacart orders <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>

## Impact on AI Product Growth
The growth of AI products is tightly linked to reasoning capabilities and the number of agents that can be shipped to users <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. For example, OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>. ChatGPT usage doubled with the introduction of "01 models" (agentic models) <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. It is projected to reach one billion users by the end of 2024, quadrupling its user base from September 2023 <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>. This signifies that one-eighth of the world's population will be using ChatGPT by year-end <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

## The Future Role of AI Engineers
The job of an AI engineer is evolving towards building agents, similar to how ML engineers build models and software engineers build software <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.

[[the_future_of_ai_engineering | The future of AI engineering]]