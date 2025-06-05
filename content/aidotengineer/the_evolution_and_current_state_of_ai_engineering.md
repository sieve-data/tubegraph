---
title: The evolution and current state of AI engineering
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

## Introduction

[[AI Engineering Trends | AI engineering]] is an emerging discipline that is still very early in its development <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. The discipline is anticipated to grow, moving beyond its current state of being "90% software engineering 10% AI" <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. This field involves an "anthropological" approach, observing how people describe themselves, form groups, and establish identities and industries <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

## Evolution of AI Engineering

Over time, the [[Evolution and history of AI technology | discipline of AI engineering]] has been maturing and spreading across different fields <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

Key milestones in the discussion of [[Evolution of AI models and their application | AI engineering]] include:
*   **"The Rise of the AI Engineer"** (during "Latent Space" conference) <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
*   **"The Three Types of AI Engineer"** (at the first AI Engineer Summit) <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>
*   **"AI Engineer Worlds Fair"** (last year), which focused on the discipline's maturation and spread <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>

## Challenges and Resistance

Despite its growth, [[Challenges in AI Development | AI engineering]] faces [[Challenges in building AI applications | resistance]] from two perspectives within the AI engineer spectrum <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>:
*   **Machine Learning (ML) viewpoint:** Views the AI engineer as "mostly an MLE plus a few prompts" <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. ML engineers use terms like "test time compute" because inference is primarily for testing <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
*   **Software Engineering viewpoint:** Considers AI engineering to be "mostly software engineering and calling a few LLM APIs" <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

However, it is expected that [[AI Engineering Trends | AI engineering]] will eventually emerge as its own distinct discipline <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. AI engineers, for instance, care about "inference time compute" as they are concerned with actual inference <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

## Pivot to Agent Engineering

The AI Engineer Summit has pivoted to become the "agent engineering conference" <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, making a conscious decision to focus solely on this area <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This pivot was driven by audience interest, as demonstrated by last year's top-performing YouTube talks which heavily featured "agentic things" <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

A key rule for the conference is "no more vendor pitches," aiming to focus on practical applications and shared experiences from those putting agents into production <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

### Defining an Agent

A fundamental step in discussing agents is defining the term <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Drawing on Simon Willison's crowdsourced definitions, an agent can be understood in terms of:
*   Goals <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Tools <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>
*   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Long-running processes <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>
*   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Small multi-step task completion <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>

OpenAI also recently released a new definition of agents <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

### Why Agents Are Working Now

Agents are gaining traction now for several reasons, which include enhanced capabilities and changes in the AI landscape:
*   **Improved Capabilities:** Better reasoning, better tool use, and improved tools <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. AI capabilities, particularly between 2023 and 2025, have grown to "hit human baselines" <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Model Diversity:** OpenAI's market share has decreased from 95% to 50% in two years, indicating a more diverse landscape <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. New frontier model labs are emerging as potential challengers <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.
*   **Reduced Cost of Intelligence:** The cost of GPT-4 level intelligence has decreased by 1,000 times in the last 18 months <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **RL Fine-tuning Options:** The availability of RL fine-tuning options <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Multi-agents and Faster Inference:** Development in multi-agent systems and faster inference due to better hardware <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
*   **Outcome-based Charging:** Charging for outcomes rather than costs <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.

### Agent Use Cases and Impact

Coding agents and support agents currently have "product market fit" (PMF), and deep research agents are also reaching PMF <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.

The speaker highlights "anti-use cases" that should be avoided, such as demonstrating agents that book flights or Instacart orders, as users prefer to handle these tasks themselves <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.

The growth of agentic models has a significant impact on user adoption:
*   OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>.
*   ChatGPT's user base grew from zero to 400 million in two to two-and-a-half years <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.
*   Initial stagnation in ChatGPT usage was attributed to a lack of shipping "agentic models" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   "01 models" have doubled ChatGPT usage <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   ChatGPT is projected to reach one billion users by the end of the year, quintupling its September last year user base <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.

This growth indicates a strong correlation between the success of AI products and their reasoning capabilities and the number of agents they can ship <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.

## The Future Role of AI Engineering

The [[Role of engineering teams in AI agent production | job of an AI engineer]] is evolving towards building agents, similar to how ML engineers build models and software engineers build software <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. This shift underscores the growing importance of [[Future directions for software architecture using AI | agentic capabilities]] in the broader [[Role of AI Engineering in Reliability | AI engineering]] landscape.