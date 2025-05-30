---
title: Langfuse as a tool for AI agent observability
videoId: DpPVEw4dd0w
---

From: [[colemedin]] <br/> 

Developing [[ai_agents_and_large_language_models | AI agents]] often involves guesswork, and many struggle to build production-ready, useful [[ai_agents_and_large_language_models | AI agents]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Langfuse is presented as a "secret weapon" to address this, being a free and [[open_source_ai_agent_development | open-source]] tool <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It functions as an LLM engineering platform specifically for agent observability <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Understanding Agent Observability

Observability for [[ai_agents_and_large_language_models | AI agents]] means the ability to monitor every action an agent takes <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This includes tracking:
*   Cost of each request <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>
*   Response times <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   User conversations with the agent <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

This visibility is crucial for iterating and improving an agent over time <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While local testing might seem sufficient for tracking issues <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, deploying an agent without a platform like Langfuse is akin to "flying completely blind" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Without observability, issues like failure causes, spending, and iteration strategies become unknown <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Key Features of Langfuse

Langfuse is a feature-rich platform <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, trusted by companies like Twilio and Khan Academy <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Tracing Agent Executions
The main focus of Langfuse is tracing, which allows monitoring of agent executions and the decisions agents make in production <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This provides visibility into:
*   Total cost per request <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>
*   Request duration <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>
*   Input and output tokens <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>
*   User ID and session ID for grouping traces <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
*   Specific agent decisions, such as tool usage and inputs/outputs of those tools <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   System prompts, user messages, and assistant responses <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   Identifying tool misbehavior or bad parameters <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
*   Monitoring for errors during execution <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.

### Open-Source and Self-Hosting
Langfuse is 100% [[open_source_ai_agent_development | open-source]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, offering managed services or the option to self-host for data privacy and cost control <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Self-hosting ensures all user interactions remain within one's own infrastructure <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Self-hosting Langfuse can be simplified using a "local AI package" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. This is because Langfuse relies on various services for data storage, such as Redis, PostgreSQL, ClickHouse, and blob storage <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

### Integration with Frameworks
Langfuse integrates with a wide range of [[frameworks_and_tools_for_ai_agent_development | frameworks and tools for AI agent development]], making it easy to set up agent monitoring regardless of the chosen framework <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. These include:
*   Pydantic AI <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
*   LangChain <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
*   [[building_ai_agent_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
*   CrewAI <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   Semantic Kernel <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>

For a full list and setup guides, the Langfuse documentation provides comprehensive instructions <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Integrating Langfuse into AI Agents

### Simple OpenAI Client Integration
Langfuse offers a drop-in replacement for the OpenAI client. By importing `OpenAI` from the Langfuse package, users can continue using the OpenAI client in the exact same way, gaining instant tracing capabilities <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. The `@observe` decorator must be added to any function that calls the OpenAI client <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

To connect Langfuse, three environment variables are needed: `LF_PUBLIC_KEY`, `LF_SECRET_KEY`, and `LF_HOST` <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. These are obtained by creating a project and an API key within the Langfuse client <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

### Pydantic AI Integration
[[pydantic_ai_for_ai_agents | Pydantic AI]] utilizes Logfire, which supports an OpenTelemetry backend, allowing direct [[integration_of_langfuse_with_different_frameworks | integration of Langfuse with different frameworks]] <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. This means Langfuse can integrate directly with Logfire under the hood using OpenTelemetry <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

Key steps for [[integration_of_langfuse_with_different_frameworks | integrating Langfuse with Pydantic AI]]:
1.  Install `pydantic-ai` and `logfire` <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
2.  Incorporate Langfuse environment variables and configure Logfire <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
3.  Ensure the `instrument=True` parameter is included when setting up the Pydantic AI agent to enable Logfire and OpenTelemetry communication <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.

Custom metadata, such as user ID and session ID, can be set on agent executions to track traces for specific sessions and users <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. This is done by creating a "span" from the OpenTelemetry trace and setting custom attributes like `user_id` and `session_id`, as well as defining input and output values <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. This level of control allows for granular troubleshooting, like finding a user's conversation to diagnose specific issues <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>.

### Current Status of N8N Integration
As of the transcript, there is no native [[prototyping_ai_agents_using_flowise_and_n8n | N8N]] integration for Langfuse <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>. While community efforts exist to integrate them using custom tool nodes, it's not an ideal solution due to the need to hardcode authentication keys <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. Both [[prototyping_ai_agents_using_flowise_and_n8n | N8N]] users and Langfuse maintainers have expressed interest in a native integration <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

## Conclusion

[[developing_ai_agents_with_lang_chain_and_lang_graph | Developing AI agents]] for production without a platform like Langfuse is highly inadvisable <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. Langfuse is considered a leading observability platform due to its robust features and [[open_source_ai_agent_development | open-source]] nature <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>.