---
title: Evaluating AI agents and assistants
videoId: OC04sP_QgTI
---

From: [[aidotengineer]] <br/> 

Evaluating AI agents and assistants is a critical topic for ensuring their effectiveness in real-world applications <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While much attention is given to building agents and the tools available, it is equally important to [[evaluating_ai_agent_performance_and_reliability | evaluate them]] once they are in production <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This process helps confirm that agents function as intended and provide reliable performance <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Types of AI Agents and Evaluation Considerations

Initially, many discussions revolved around text-based agents, such as chatbots <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. However, the field is rapidly advancing to include voice AI <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> and multimodal agents <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Voice AI is already transforming call centers, handling billions of calls globally <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. An example is the Price Line Pennybot, a real production application allowing users to book an entire vacation hands-free using voice <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The method of [[evaluating_ai_agent_performance_and_reliability | evaluating these agents]] changes based on their modality:
*   Text-based agents require specific evaluation techniques <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Voice agents necessitate additional evaluations specific to voice <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   Multimodal agents require considering further types of evaluations <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## [[components_of_ai_agents | Components of AI Agents]]

Regardless of the framework used (e.g., Lan graph, Crei, Llama index workflow) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, common patterns define the [[components_of_ai_agents | components of an agent]] <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>:

1.  **Router**: This component acts as the "boss," deciding the next step an agent will take <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. For instance, in an e-commerce agent, a router funnels a user query (e.g., "I want to make a return," "Are there any discounts?") to the appropriate skill <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
2.  **Skills**: These are the logical chains that perform the actual work <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. A skill flow of execution might involve LLM calls or API calls to complete a user's request <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
3.  **Memory**: This component stores past interactions and context, enabling multi-turn conversations and ensuring the agent remembers previous statements <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Example: An Agent's Inner Workings (Traces)

To understand how these components interact, one can examine agent "traces," which show the inner workings of an agent's execution <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. For example, in a code-based agent asked about "trace latency trends" <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>:
*   The router first determines how to tackle the question <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   It might make a tool call (skill) to run a SQL query and collect application traces <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   The router might then call a second skill, like a data analyzer, to process the collected data <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   Throughout this process, memory stores everything that occurs <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

## How to [[evaluating_ai_agent_performance_and_reliability | Evaluate AI Agents]]

Every step within an agent's flow is a potential point of failure, necessitating distinct evaluation strategies <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### Evaluating the Router
For routers, the primary concern is whether it called the correct skill <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. If a user asks for "leggings" but is routed to "customer service" or "discounts," the router failed <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Evaluation should confirm the router correctly calls the right skill with the appropriate parameters, ensuring the agent passes the correct information (e.g., material type, cost range for a product search) <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Evaluating Skills
Skill evaluation is complex due to the varied components within a skill <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. For a Retrieval-Augmented Generation (RAG) skill, evaluations might include:
*   **Relevance of pulled chunks**: Assessing if the retrieved information is pertinent <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Correctness of the generated answer**: Verifying the accuracy of the agent's output <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.
*   **LLM-as-a-judge evaluations**: Using one LLM to evaluate the output of another <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Code-based evaluations**: Running specific code to assess skill performance <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Evaluating the Agent's Path (Convergence)
One of the most challenging aspects to [[challenges_in_ai_agent_evaluation | evaluate]] is the path an agent takes to complete a task <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Ideally, an agent should consistently converge, taking a reliable number of steps (e.g., five or six) to query, use parameters, and execute skills to generate the correct answer <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. Different LLM providers (e.g., OpenAI, Anthropic) can lead to vastly different numbers of steps for the same skill <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The goal is to ensure succinctness and reliability in the number of steps an agent takes to consistently complete a task <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Evaluating Voice AI Applications
Voice applications are among the most complex applications ever deployed <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. [[evaluating_ai_agent_performance_and_reliability | Evaluating them]] requires additional considerations beyond text or transcript evaluation <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. The audio chunk itself needs to be evaluated <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This includes:
*   User sentiment <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   Speech-to-text transcription accuracy <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   Consistency of tone throughout the conversation <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   Specific evaluations for intent, speech quality, and speech-to-text accuracy of audio chunks <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Example: Evaluating a Co-pilot Agent

One approach to [[implementation_of_evaluation_platforms_for_ai_agents | implementing evaluation platforms for AI agents]] is to dogfood one's own tools. For instance, the speaker's company, Arise, uses its own platform to [[evaluating_ai_agent_performance_and_reliability | evaluate its co-pilot]] <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. This co-pilot assists users within the product by helping with debugging, summarizing, and natural language search <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

For this co-pilot, evaluations are run at every single step of its traces in the wild <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>:
*   An overall evaluation assesses the correctness of the generated response (e.g., for a search query) <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   Evaluations check if the search router picked the correct router and passed the right arguments <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   Finally, evaluations ensure the task or skill was completed correctly during execution <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

The key takeaway is that evaluations should not be limited to a single layer but should be present throughout the entire application flow <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This enables precise debugging to identify if issues originate at the router level, skill level, or elsewhere in the agent's process <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.