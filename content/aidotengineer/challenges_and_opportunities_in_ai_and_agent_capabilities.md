---
title: Challenges and Opportunities in AI and Agent Capabilities
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

## Introduction to AI Engineering and Agents

AI engineering is an evolving discipline that aims to landmark the state of the art in the industry <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. Past discussions at AI Engineer Summits have covered the rise of the AI engineer, the three types of AI engineers, and the maturation and spread of the discipline across different fields <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

### Evolution of the Discipline
There's ongoing resistance regarding the identity of an AI engineer <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>:
*   **Machine Learning (ML) View:** An AI engineer is mostly an ML engineer with some prompting <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Software Engineering (SE) View:** An AI engineer is primarily a software engineer calling a few Large Language Model (LLM) APIs <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

However, it's expected that AI engineering will emerge as its own distinct discipline over time, growing beyond the current perception of being 90% software engineering and 10% AI <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Differences in language, such as ML engineers saying "test time compute" versus AI engineers saying "inference time compute," highlight this distinction <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

## Defining an AI Agent

Defining "agent" is a monumental task, with various perspectives:
*   **Machine Learning Perspective:** Agents are often discussed in the context of reinforcement learning environments, focusing on actions achieving goals <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Software Engineering Perspective:** Can be reductive, sometimes equating an agent to a simple "for loop" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.
*   **Crowdsourced Definitions:** Simon Willison crowdsourced over 300 definitions, highlighting common themes <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. Key characteristics include:
    *   Goal-oriented behavior <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
    *   Tool use <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
    *   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
    *   Long-running processes <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
    *   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
    *   Small multi-step task completion <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>
*   **OpenAI's Definition:** OpenAI introduced a new definition for agents, indicating ongoing work in this area <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

## Why Agents are Gaining Traction Now

The current momentum for agents, in contrast to previous years, is attributed to several factors:
*   **Increased Capabilities:** Agent capabilities are starting to reach human baselines <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. This includes:
    *   Better reasoning <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>
    *   Improved tool use <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>
    *   Better tools <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>
*   **Model Diversity:** The market share for models like OpenAI has diversified significantly, from 95% two years ago to 50% now <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. The emergence of new Frontier Model Labs poses challenges to established players like OpenAI <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Reduced Cost of Intelligence:** The cost of GPT-4 level intelligence has decreased by 1,000 times in the last 18 months <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>. Similar cost reductions are being observed for "01 level intelligence" <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   **RL Fine-Tuning Options:** The availability of reinforcement learning (RL) fine-tuning options is contributing to agent development <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Outcome-Based Charging:** A shift towards charging for outcomes rather than just costs is emerging <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
*   **Advancements in Multi-Agents and Hardware:** Progress in multi-agent systems and faster inference due to improved hardware are also key factors <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

## [[challenges_and_opportunities_in_ai_adoption | Challenges and Opportunities in AI Adoption]] and Development

### Current [[challenges_and_insights_in_developing_ai_coding_agents | Challenges and Insights in Developing AI Coding Agents]] and Agents in General
While there's a strong push for 2025 to be the "Year of Agents" by major figures like Satya Nadella, Sam Altman, and Greg Brockman <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>, skepticism exists. Some were initially told to remove "agents" from their branding, only to be told to put it back on later <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.

A significant [[challenges_in_developing_ai_agents | challenge in developing AI agents]] is that speakers often come from backgrounds where they primarily make agent frameworks for a living, rather than putting them into production <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. This has led to a new rule at conferences: "no more vendor pitches" <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, making curation more difficult as speakers have less incentive to share production-level insights <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

### Opportunities and Use Cases
*   **Product Market Fit:** Coding agents and support agents are showing product market fit <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>. Deep research also has product market fit <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   **Emerging Use Cases:** Several other use cases are up and coming <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.
*   **The "Everything + Agent" Formula:** It has been observed that "everything plus agent works," such as:
    *   Agent + RAG (Retrieval-Augmented Generation) <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>
    *   Agent + Sentiment <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>
    *   Agent + Search <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>
    This formula is seen as a "simple formula for making money in 2025" <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

However, there are "anti-use cases" that should be avoided, such as agents for booking flights or Instacart orders, as users often prefer to handle these tasks themselves <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

## [[future_prospects_in_ai_and_agentbased_technologies | Future Prospects in AI and Agent-based Technologies]]

The growth of AI products, particularly agents, is strongly tied to reasoning capabilities <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. The growth of ChatGPT, from zero to 400 million users in 2.5 years, shows a clear trend <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

ChatGPT's usage growth stalled for a year when it didn't ship any agentic models <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. However, the introduction of "01 models" has doubled ChatGPT usage, and it's projected to hit a billion users by the end of the year, quintupling its September last year user base <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. This means 1/8th of the world's population could be using ChatGPT by year-end <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.

The job of an AI engineer is evolving towards building agents, similar to how ML engineers build models and software engineers build software <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.