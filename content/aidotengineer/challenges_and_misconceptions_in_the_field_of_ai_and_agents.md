---
title: Challenges and misconceptions in the field of AI and agents
videoId: 5N33E9tC400
---

From: [[aidotengineer]] <br/> 

## The Evolving Landscape of AI Engineering
AI engineering is a maturing discipline, moving beyond its initial phases described in previous summits, which covered the "rise of the AI engineer" <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, the "three types of AI engineer" <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>, and its "maturing and spreading across different disciplines" <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. While an O'Reilly book on AI engineering exists <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>, Gartner suggests the field may have peaked <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

### Resistance and Disciplinary Emergence
Currently, there is [[technical_challenges_in_ai_agent_development | resistance from two sides]] of the AI engineer spectrum <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>:
*   **Machine Learning (ML) viewpoint:** Sees AI engineering as primarily ML with some prompts <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Software Engineering viewpoint:** Views it as mostly software engineering calling LLM APIs <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

However, AI engineering is expected to emerge as its own distinct discipline <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. Historically, AI engineering was considered 90% software engineering and 10% AI, a ratio expected to grow over time <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. Differences in terminology, such as "test time compute" (ML) versus "inference time compute" (AI engineering), highlight this emerging distinction <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## The Pivot to Agent Engineering
The AI Engineer Summit has deliberately pivoted to become the "Agent Engineering Conference" <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. This decision involved saying "no" to other areas like RAG (Retrieval-Augmented Generation), open models, and GPUs, to focus specifically on agents <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

### Speaker and Content Curation
A key challenge in this pivot was ensuring quality content. Last year's top-performing YouTube talks indicated a strong audience interest in "agentic things" <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. However, this resulted in speakers predominantly from agent framework companies <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. To address the question of "who's putting this in production?" <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, a new rule was introduced: no more vendor pitches <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, making content curation significantly harder <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

### The "Everything + Agent Works" Formula
A simple observation highlights the potential: "everything plus agent works" <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This includes:
*   Agent + RAG <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>
*   Agent + Sentiment <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>
*   Agent + Search <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>

This "simple formula" is considered a way to "make money in 2025" <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.

## Debunking the "Year of Agents" Claim
The phrase "2025 is the year of Agents" is a common prediction <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>, often pushed by industry leaders like Satya Nadella, Roman, Greg Brockman, and Sam Altman <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. However, the speaker and co-host were initially skeptical <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>, reflecting a broader audience sentiment that "agents" is a buzzword people are tired of hearing <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

OpenAI's stance on branding has also shifted; in March 2024, they advised against using "agents" in branding, but now suggest putting it back on <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.

### The Fundamental [[challenges_in_creating_effective_ai_agents | Challenge]] of Defining "Agent"
A significant hurdle in the field is defining what an "agent" is <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Different perspectives exist:
*   **Machine Learning:** Focuses on reinforcement learning environments, actions, and achieving goals <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.
*   **Software Engineers:** Have a reductive view, often seeing it as a simple "for loop" <a class="yt-timestamp" data-t="05:49:00">[05:49:00]</a>.

Simon Willison crowdsourced over 300 definitions, highlighting common elements <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>:
*   Goals <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>
*   Tools <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>
*   Control flow <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>
*   Long-running processes <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>
*   Delegated authority <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>
*   Small multi-step task completion <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>

OpenAI also recently released a new definition for agents <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.

## Why Agents are Gaining Traction Now
Despite past skepticism, agents are working now for several reasons <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>:
*   **Increased Capabilities:** AI models' capabilities are rapidly growing and starting to "hit human baselines" <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>. This includes better reasoning, improved tool use, and more effective tools <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
*   **Model Diversity:** OpenAI's market share has decreased from 95% to 50% in two years, leading to a much more diverse landscape <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>, with new frontier model labs emerging as potential challengers <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Lower Cost of Intelligence:** The cost of GPT-4 level intelligence has dropped 1,000 times in the last 18 months <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **RL Fine-Tuning Options:** The availability of RL fine-tuning options <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
*   **Business Model Shifts:** Charging for outcomes instead of costs <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
*   **Technological Advancements:** Work on multi-agents and faster inference due to better hardware <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

## Agent Use Cases and Anti-Patterns
Certain agent use cases have achieved "product market fit" (PMF) <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>:
*   Coding agents <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>
*   Support agents <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>
*   Deep research agents <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>

However, there are also "anti-use cases" that should be avoided as primary demonstrations <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>:
*   Agents that book flights <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>
*   Agents that book Instacart orders <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>
*   "Astroturfing" agents <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>

## The Impact of Agentic Models on AI Product Growth
The growth of AI products is strongly tied to reasoning capabilities and the deployment of agents <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>. OpenAI reported 400 million users, a 33% growth in three months <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>. ChatGPT, for example, experienced a year of stagnation when it didn't ship agentic models <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. The introduction of 01 models doubled ChatGPT usage <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>, and it is projected to reach one billion users by the end of the year <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>, quintupling its user base from September of last year <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. This massive growth signifies that the job of an AI engineer is evolving towards building agents <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, similar to how ML engineers build models and software engineers build software <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.