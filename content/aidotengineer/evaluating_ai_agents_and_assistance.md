---
title: Evaluating AI agents and assistance
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

[[evaluating_ai_agents_methods_and_metrics | Evaluating AI agents]] and assistants is a crucial topic, especially when these agents are deployed into production environments. Understanding how they perform in the real world is paramount for their success and reliability <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This includes evaluating not only text-based agents but also more complex multimodal systems <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Evolution of AI Agents

Initially, many discussions revolved around text-based agents, such as chatbots that perform actions and figure out tasks <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. However, the field is rapidly advancing beyond this:

*   **Voice AI**: Voice AI is becoming a significant frontier, already transforming call centers that handle over a billion calls worldwide <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Real-time voice APIs are enabling agents to revolutionize customer service <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. An example is the Price Line Penny bot, a production travel agent that allows users to book entire vacations hands-free <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Multimodal Agents**: Beyond text and voice, agents are increasingly multimodal, requiring specific [[evaluating_ai_agents_methods_and_metrics | evaluation]] strategies due to their complexity <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Core Components of an AI Agent

Regardless of the framework used (e.g., Lan graph, Crei, Llama index workflow), AI agents typically consist of three common patterns <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>:

1.  **Router**: This component acts like a "boss," deciding the next step an agent will take <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. For e-commerce agents, a router directs user queries (e.g., "I want to make a return," "Are there any discounts?") to the appropriate skill <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
2.  **Skills**: These are the logical chains that perform the actual work <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. A skill might involve LLM calls or API calls depending on its implementation <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
3.  **Memory**: This component stores the context and history of the conversation. It's crucial for multi-turn interactions to prevent the agent from forgetting previous statements <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Agent Execution Example: Code-Based Agent Trace

An agent's inner workings can be observed through "traces," which show the sequence of actions taken <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. For instance, in a code-based agent that responds to a question like "What trends do you see in my trace latency?" <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>:

1.  **Router Call**: The agent first calls a router to decide how to tackle the question <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Multiple router calls can occur as the application grows <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
2.  **Tool/Skill Call**: The router makes a tool call to run a SQL query, collecting application traces <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
3.  **Second Router Call & Skill**: It then returns to the router, which calls a second skill—the data analyzer. This skill takes the collected traces and application data to analyze them <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
4.  **Memory**: Throughout this process, memory stores everything happening behind the scenes <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

This example illustrates the interplay of the router, skills, and memory components <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## [[evaluating_ai_system_performance | Evaluating AI System Performance]]

Every step within an agent's execution flow is an area where it can go wrong <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. Therefore, [[evaluating_ai_agents_methods_and_metrics | evaluation]] needs to be comprehensive and cover each component:

### Evaluating the Router

For routers, teams primarily care about whether the agent called the right skill <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. If a user asks for "leggings" but is sent to customer service, the router failed <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Key evaluation points include:

*   **Correct Skill Selection**: Did the router correctly identify and call the appropriate skill (e.g., product search vs. customer service)? <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>
*   **Correct Parameter Passing**: Did the router pass the correct parameters into the chosen skill (e.g., specific material, cost range for a product search)? <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>

### Evaluating a Skill

[[evaluating_ai_agents_methods and metrics | Evaluating a skill]] is complex due to its many internal components <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. For a Retrieval-Augmented Generation (RAG) type of skill, [[evaluating_ai_agents_methods_and_metrics | evaluation]] involves:

*   **Relevance of Chunks**: Assessing the relevance of information chunks pulled by the skill <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Correctness of Answer**: Verifying the correctness of the generated answer <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **LLM as a Judge Evals**: Using Large Language Models (LLMs) to evaluate the skill's output <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Code-Based Evals**: Running code-based evaluations to assess skill performance <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Evaluating Agent Path and Convergence

One of the most challenging aspects to evaluate is the agent's execution path and its "convergence" <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This refers to the consistency and efficiency of the steps an agent takes to complete a task <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

*   **Consistent Steps**: Ideally, an agent should consistently take a similar number of steps (e.g., five or six) to query, use correct parameters, and call the necessary skill components <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Reliability**: Different LLM models (e.g., OpenAI vs. Anthropic) can lead to vastly different numbers of steps for the same skill <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. The goal is to achieve succinctness and reliability in the number of steps an agent takes to consistently complete a task <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Evaluating Voice AI Applications

Voice applications are among the most complex to deploy and require additional evaluation pieces <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>:

*   **Audio Chunk Evaluation**: Beyond just the text transcript, the actual audio chunk needs to be evaluated <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **User Sentiment**: Assessing the user's sentiment from the audio <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Speech-to-Text Accuracy**: Verifying the accuracy of the speech-to-text transcription <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   **Tone Consistency**: Ensuring the tone remains consistent throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Audio-Specific Evals**: Defining evaluations specifically for audio chunks, focusing on intent, speech quality, and speech-to-text accuracy <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Comprehensive [[evaluating_ai_agents_methods_and_metrics | Evaluation Strategy]]

A key takeaway for [[building_effective_ai_agents | building effective AI agents]] is to implement [[evaluating_ai_agents_methods_and_metrics | evaluations]] throughout the entire application trace <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. This layered approach allows for precise debugging if something goes wrong, identifying whether the issue occurred at the router level, skill level, or elsewhere in the flow <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

For example, a company like Arise dogfoods its own tool to evaluate its co-pilot agent <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>:

*   **Overall Response Eval**: Evaluating the overall correctness of the response (e.g., for a search question) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   **Router Eval**: Assessing if the search router picked the correct route and passed the correct arguments <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Skill Completion Eval**: Checking if the task or skill was completed correctly during execution <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

By having [[evaluating_ai_agents_methods_and_metrics | evaluations]] at every step, teams can effectively identify and resolve issues, ensuring the reliability and performance of their AI agents <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.