---
title: Components of AI agents
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

AI agents and assistants are becoming increasingly prevalent, moving beyond text-based interactions to include multimodal capabilities like voice AI <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. These advanced agents require careful evaluation once they are put into production to ensure they function correctly in the real world <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Understanding the fundamental components of an AI agent is crucial for effective evaluation and [[building_and_improving_ai_agents | building and improving AI agents]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Core Components of an Agent

Regardless of the specific framework used (e.g., LangGraph, CrewAI, LlamaIndex Workflow), AI agents typically exhibit three common patterns or components <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>:
*   **Router** <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>
*   **Skills** <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   **Memory** <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>

[[different_architectures_for_ai_agents | Different architectures for AI agents]] might implement these components in various ways, but their underlying functions remain consistent <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Router
The router acts as the "boss" of the agent, deciding the next step an agent will take <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Its primary goal is to determine which "skill" to call based on the user's query <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

For example, in an e-commerce agent, when a user types a question like "I want to make a return," "give me an idea of what to go buy," or "are there any discounts on this?", the user query funnels into a router. The router then decides whether to call a customer service skill, a discount suggestion skill, or a product suggestion skill <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

#### Evaluation of the Router
For routers, teams typically focus on whether the router called the *right skill* <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. It's also important to verify that the router not only calls the correct skill but also passes the *right parameters* into that skill <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Skills
Skills are the actual logical chains that perform the work an agent needs to do <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. These can involve LLM calls, API calls, or other computational steps <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. When a router directs a query to a specific skill, that skill executes a flow to fulfill the user's request, such as performing a product search <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

#### Evaluation of Skills
Evaluating a skill can be complex due to its many internal components <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. Key evaluation points for skills include:
*   **Relevance of pulled chunks:** For RAG-type skills, assessing the relevance of information chunks retrieved <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **Correctness of the generated answer:** Verifying that the skill produces the correct output <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **Convergence/Path taken:** Evaluating the path the agent takes to complete a task. Ideally, the agent should converge, meaning it consistently takes a similar, succinct number of steps to achieve its goal <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Different models (e.g., OpenAI vs. Anthropic) can lead to wildly different numbers of steps for the same skill <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This aspect is considered one of the hardest to evaluate <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Memory
Memory is the component responsible for storing the agent's context and past interactions <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This is critical for multi-turn conversations, as agents need to remember what was previously said to maintain a coherent dialogue <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. It ensures the agent keeps the conversation in some semblance of state <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Traces: Visualizing Agent Components

Understanding the "traces" of an agent provides insight into its inner workings <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Traces allow engineers to see what happened under the scenes when an agent processes a query <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.

For instance, in a code-based agent asked "what trends do you see in my Trace latency?", the trace reveals:
1.  **Router Call 1:** The router decides how to tackle the question <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
2.  **Skill Execution (Tool Call):** The router makes a tool call to run a SQL query and collect application traces <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
3.  **Router Call 2:** After the first skill, the process returns to the router to decide the next step <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
4.  **Skill Execution (Data Analyzer):** The router calls a second skill, the data analyzer, which takes the collected traces and application data to analyze them <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
Throughout this process, **memory** stores everything that is happening behind the scenes <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## Multimodal Agents and Additional Evaluation
The "next frontier" for AI agents includes voice AI, which is already revolutionizing call centers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Examples like the PriceLine Penny bot allow users to book entire vacations hands-free <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

These complex applications require additional evaluation considerations beyond just text-based interactions <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. For voice agents, evaluations must encompass:
*   **Audio chunks:** Not just the generated transcript, but the actual audio itself needs evaluation <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **User sentiment:** Assessing the user's emotional state <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Speech-to-text transcription accuracy:** Checking the quality of the transcription <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Tone consistency:** Ensuring the agent's tone remains consistent throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

### Comprehensive Evaluation Strategy
It is crucial to have evaluations defined throughout the entire application trace, not just at one layer <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This allows for effective debugging, pinpointing whether an issue occurred at the router level, skill level, or elsewhere in the flow <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. For example, a co-pilot might have evaluations at the top for overall response correctness, at the search router for picking the right router and passing correct arguments, and at the skill execution for task completion <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.