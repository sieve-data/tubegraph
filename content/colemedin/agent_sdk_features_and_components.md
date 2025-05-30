---
title: Agent SDK features and components
videoId: e7qvd2bOITc
---

From: [[colemedin]] <br/> 
The [[openai_agent_sdk_overview | OpenAI Agent SDK]] is a new, production-ready framework for building agentic [[ai_agents_and_their_development | AI agents]] and applications. It is built on top of [[swarm_foundation_in_agent_sdk | Swarm]], an open-source [[ai_development_tools | AI agent framework]] previously released by OpenAI, and remains completely free and open source <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The SDK aims to be very easy to use for creating full agentic [[incorporating_ai_agents_and_advanced_development_features | AI apps]] with minimal abstractions <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

### Core Concepts and Features

The [[openai_agent_sdk_overview | Agent SDK]] is designed around several core concepts that facilitate the creation of robust [[building_complex_agent_systems | complex agent systems]]:

#### Agents
At its most fundamental, an agent involves providing instructions and tools to a Large Language Model (LLM) <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. The SDK allows for the definition of agents with a name, instructions (system prompt), and a specified model <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. [[ai_agents_and_their_development | Agents]] operate more effectively when specialized, working together in a "mixture of experts" approach <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

#### Handoffs
Handoffs enable different specialized agents to collaborate on a problem <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This feature makes it straightforward to set up processes where a primary agent can delegate tasks to other specialized agents as needed <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. An agent can call upon another agent when the user's query aligns with that agent's specialization, facilitated by a `handoff_description` attribute <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

#### Guardrails
Guardrails are crucial safety checks that can be custom-created and use LLMs to validate input and output for LLMs <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. They can prevent responses if issues like hallucinations are detected <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Guardrails can be implemented as `input_guard_rails` (running before agent execution) or `output_guard_rails` (running before sending a response to the user) <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. This capability helps to ensure the realism and appropriateness of an agent's planned actions or responses <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

#### Tracing
Tracing provides a way to monitor the execution of LLMs and agents, allowing developers to inspect prompts, outputs, and identify where issues might occur <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This feature is vital for debugging and monitoring [[ai_agents_and_their_development | agents]] in production <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The SDK integrates with external tracing dashboards like OpenAI's own or third-party solutions such as Pydantic Logfire <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

#### Structured Outputs
This feature standardizes LLM responses by forcing them into a specific format, such as JSON <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. By defining an `output_type` for an agent, developers can ensure specific values are always returned, which is a powerful method to reduce LLM hallucinations and achieve consistent responses <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

#### Tools
Tools give [[ai_agents_and_their_development | AI agents]] the ability to interact with the external world, performing actions like searching for flights, reserving hotels, or retrieving weather information <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Tools are defined as Python functions decorated with `@function_tool`, and their docstrings serve as prompts to the LLM, instructing it on when and how to use the tool <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. The LLM determines the parameters for the tool call, and the tool's string return is then reasoned about by the LLM <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

#### User Context Management
The SDK allows for passing `user_context` (e.g., user ID, preferences) to tools without including it directly in the LLM's prompt <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This enables tools to alter their operations based on higher-level metadata, allowing for personalized interactions and functionality <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

### Example Application: Travel Planner Assistant

The SDK's capabilities are demonstrated through a travel planner assistant application, showcasing a multi-agent system:
*   A primary travel agent manages the overall conversation and planning <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   Specialized agents handle specific tasks, such as:
    *   A flight agent for flight recommendations using a `search_flights` tool <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
    *   A hotel agent for hotel reservations using a `search_hotels` tool <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
*   A general weather tool helps the primary agent by providing weather data relevant to trip planning <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   A budget analysis agent acts as an `input_guard_rail` to determine if a user's trip budget is realistic before the main planning begins <a class="yt-timestamp" data-t="00:20:02">[00:20:02]</a>.
*   User preferences, like preferred airlines or hotel amenities, are managed through `user_context` to personalize recommendations <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

This system demonstrates how agents, handoffs, tools, structured outputs, guardrails, and context management work together to build a non-trivial agentic application <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Installation and Usage

Getting started with the [[openai_agent_sdk_overview | Agent SDK]] is simplified with a single-line Pip installation command and comprehensive documentation <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Developers can set up their OpenAI API key and choose their desired LLM, including non-OpenAI models that are OpenAI-compatible (like OpenRouter or OLLama) via custom clients <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. The [[live_agent_studio_platform | Live Agent Studio platform]] can be used for UI <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Comparison with Other Frameworks

While the [[openai_agent_sdk_overview | Agent SDK]] offers ease of use and powerful capabilities, some developers note that it leans towards higher abstraction compared to frameworks like Pydantic AI and LangGraph <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. This can make it very easy to get started but might limit full control and customizability for complex production applications <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>. Specific [[ai_agent_development_challenges | challenges]] include detailed control over multi-agent handoffs, lack of built-in "human in the loop" approval mechanisms, and less comprehensive documentation for agent testing compared to some other frameworks <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>, <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

Despite these observations, given its "brand new" status, the [[openai_agent_sdk_overview | Agent SDK]] is expected to evolve with more features in the future <a class="yt-timestamp" data-t="00:29:58">[00:29:58]</a>.