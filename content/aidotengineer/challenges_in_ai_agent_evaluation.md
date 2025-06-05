---
title: Challenges in AI agent evaluation
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

Evaluating AI agents and assistants is a critically important topic for ensuring they work effectively in the real world once deployed into production <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It is crucial for both technical teams and leadership to understand how to verify the performance of what is being put out <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Types of AI Agents and Their Evaluation Needs

While many are familiar with text-based agents like chatbots <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>, the next frontier includes Voice AI, which is already revolutionizing call centers with billions of calls made worldwide using voice APIs <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. An example is Price Line Penny, a real production application allowing users to book an entire vacation hands-free using voice <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

These are not just text-based agents but multimodal agents <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The approach to [[Evaluating AI agents and assistants | evaluating these types of agents]] is different: voice agents require specific types of evaluations, and multimodal agents necessitate additional considerations <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a> <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Components of an AI Agent

Regardless of the framework used (e.g., LangGraph, CrewAI, LlamaIndex), agents typically share common architectural patterns <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Each of these components presents unique evaluation [[Design challenges for AI agents | challenges for AI agents]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>:

*   **Router:** This component acts like a "boss," deciding the agent's next step <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a> <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. For instance, in an e-commerce agent, it directs a user query (e.g., "I want to make a return," "Are there discounts?") to the appropriate skill <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. An agent can have multiple router calls as the application grows <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Skills (Logical Chains):** These are the actual logical chains that perform the work requested by the router <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. They can involve LLM calls, API calls, or a combination <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **Memory:** This component stores the context of the conversation, allowing for multi-turn interactions without the agent "forgetting" previous statements <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a> <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## [[Evaluating AI agent performance and reliability | Challenges in AI agent evaluation]] for Each Component

Every step within an agent's operation is an area where things can go wrong <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Router Evaluation

For routers, the primary concern is whether it called the **right skill** <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. If a user asks for leggings but is routed to customer service or discount information, the router has failed <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Beyond just calling the correct skill, it's essential to evaluate whether the router passed in the **right parameters** into that skill <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. For example, if a user asks for leggings of a specific material or cost range, the router must ensure these details are correctly passed to the product search skill <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Skill Evaluation

Evaluating a skill is complex due to its many internal components <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. For a Retrieval Augmented Generation (RAG) type skill, evaluation needs to cover:
*   **Relevance of pulled chunks** <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>
*   **Correctness of the generated answer** <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>

Skills can be evaluated using various methods, such as LLM-as-a-judge evaluations or code-based evaluations <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

### Path and Convergence Evaluation

One of the most [[Challenges in building reliable AI agents | challenging areas]] to evaluate is the **path the agent took** to complete a task <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a> <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Ideally, an agent should converge, consistently taking a similar, succinct number of steps (e.g., five or six) to query user requests, input parameters, and call necessary components to generate the right answer <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

However, the number of steps can vary wildly, even for the same skill implemented with different models like OpenAI or Anthropic <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. The goal is to ensure both succinctness and **reliability in the number of steps** an agent takes to consistently complete a task <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a> <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Voice and Multimodal Agent Evaluation

Voice applications represent some of the most complex applications ever built <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Their evaluation requires additional considerations beyond text <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. It's not just the text or transcript that needs to be evaluated, but also the **audio chunks** themselves <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a> <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a> <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

Key evaluation dimensions for voice agents include:
*   User sentiment <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>
*   Speech-to-text transcription accuracy <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>
*   Consistency of tone throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>

Specific evaluations must be defined for audio chunks, focusing on aspects like intent, speech quality, and speech-to-text accuracy <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a> <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

## [[Best practices for AI evaluation | Best Practices for AI Evaluation]]

A key takeaway for [[Improving AI evaluation methods | improving AI evaluation methods]] is to implement evaluations **throughout the entire application trace** <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a> <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This allows for effective debugging when something goes wrong, by pinpointing whether the issue occurred at the router level, skill level, or elsewhere in the flow <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. For example, evaluations can assess the overall response correctness, whether the correct router was picked, if correct arguments were passed, and if the task was completed correctly by the skill <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.