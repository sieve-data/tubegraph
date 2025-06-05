---
title: Components of AI agents router skills and memory
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

When [[building_effective_ai_agents | building effective AI agents]] and putting them into production, it is crucial to evaluate their performance to ensure they function effectively in real-world scenarios <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This evaluation is important even at a leadership level to understand if deployed agents are working as intended <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

While many discussions focus on text-based agents, the "next frontier" is voice AI, which is already revolutionizing call centers worldwide <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Examples like the Price Line Pennybot demonstrate real-world applications where users can book entire vacations hands-free using voice <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This shift to multimodal agents necessitates specific evaluation methods, as different modalities require additional considerations <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Components of an AI Agent

Regardless of the specific framework used (e.g., Lan graph, Crei, Llama index workflow), AI agents are typically built with common architectural patterns <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The three primary components are:

1.  **Router** <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>
2.  **Skills** <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
3.  **Memory** <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

These components have different evaluation requirements <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### The Router

The router acts like the "boss" of an AI agent, deciding the next step an agent will take <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Its primary goal is to determine which specific "skill" to call based on a user's query <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

**Example**: In an e-commerce agent, a user query like "I want to make a return" or "Are there any discounts?" is funneled to the router <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. The router then decides whether to call a skill related to customer service, discounts, or product suggestions <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

A router might not always make the correct decision, but accuracy is vital as it dictates the subsequent path within the agent <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Agents can have multiple router calls as an application grows, where the agent repeatedly decides its next action <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Skills

Skills are the actual logical chains that perform the work requested by the user <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Once the router calls a specific skill, the agent executes a flow of actions to fulfill the user's request <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. These actions can involve [[importance_of_tool_calling_for_ai_agents | tool calls]], API calls, or [[building_ai_agents_using_primitives | LLM calls]] <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

**Example**: If a user asks for "the best leggings to buy," the router might call a "product search" skill <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This skill then executes a flow that might involve running a SQL query to collect product data and passing it to a data analyzer skill <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Memory

[[Stateful Agents and AI Memory Management | Memory]] is a crucial component that stores the context of previous interactions <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Since most agent interactions are multi-turn conversations, memory prevents the agent from forgetting what was previously said <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. It maintains the agent's state throughout the conversation <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This is a vital aspect of [[memory_management_and_delegation_in_ai | memory management and delegation in AI]] for effective agents.

## Evaluating Agent Components

Every step within an AI agent's flow presents an opportunity for error, necessitating comprehensive evaluation <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Evaluating the Router

Teams should focus on whether the router calls the *correct skill* with the *right parameters* <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. For example, if a user asks for leggings but is routed to customer service, the router made an incorrect decision <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Ensuring the router correctly identifies the appropriate skill and passes necessary details (e.g., material type, cost range for product search) is key <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Evaluating Skills

Evaluating skills is complex due to their multi-component nature <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. For a Retrieval-Augmented Generation (RAG) type skill, evaluations include <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>:
*   Relevance of pulled chunks <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>
*   Correctness of the generated answer <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>

Skills can also utilize [[building_ai_agents_using_primitives | LLM as a judge]] evaluations or code-based evaluations <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Evaluating the Agent Path (Convergence)

One of the most challenging aspects to evaluate is the "path" the agent takes, also known as convergence <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Ideally, when the same skill is called multiple times, it should consistently take a similar, succinct number of steps to complete the task <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

However, different models (e.g., OpenAI vs. Anthropic) can lead to wildly different numbers of steps for the same task <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The goal is to ensure reliability and consistency in the number of steps an agent takes to complete a task <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Evaluating Voice AI Agents

Voice applications are among the most complex applications ever built and require additional evaluation pieces <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Beyond text transcription, the audio chunk itself needs to be evaluated <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This includes assessing:
*   User sentiment <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>
*   Speech-to-text transcription accuracy <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>
*   Tone consistency throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>

Evaluations should be defined for intent, speech quality, and speech-to-text accuracy of the audio chunks <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

## Comprehensive Evaluation Approach

To effectively debug and optimize AI agents, evaluations should be integrated throughout the application, not just at a single layer <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This means having evaluations at the router level, skill level, and throughout the entire flow <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This allows for pinpointing exactly where an issue occurred within the agent's execution trace <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.