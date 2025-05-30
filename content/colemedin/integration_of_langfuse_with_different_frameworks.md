---
title: Integration of Langfuse with different frameworks
videoId: DpPVEw4dd0w
---

From: [[colemedin]] <br/> 

Langfuse is an [[langfuse_as_a_tool_for_ai_agent_observability | LLM engineering platform for agent observability]] <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. It is a free and [[opensource_libraries_for_agent_development | open-source]] tool <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a> that helps in monitoring every action an AI agent takes, including request costs, response times, and user conversations <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This visibility is crucial for iterating and improving agents over time, especially when they are running in production <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Key Integration Capabilities

Langfuse integrates with a variety of frameworks, making it easy to set up agent monitoring regardless of the chosen framework <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>, <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Supported Frameworks
Langfuse offers direct integration with:
*   Pydantic AI <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
*   LangChain <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
*   [[building_ai_agent_workflows_with_langgraph | LangGraph]] <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>
*   Crew AI <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>
*   Semantic Kernel <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>

### OpenAI Client Integration
Langfuse provides a drop-in replacement for the OpenAI client, allowing existing agents to easily integrate with Langfuse's tracing capabilities <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. By importing `OpenAI` from the Langfuse package and applying the `@observe` decorator to functions calling the OpenAI client, all tracing data becomes instantly available <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This allows for monitoring of latency, cost, and token usage, along with full request and response details <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Pydantic AI Integration
Pydantic AI, which uses Logfire internally, supports the OpenTelemetry backend, a standard for communicating log data <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Langfuse can directly integrate with Logfire using OpenTelemetry <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

To integrate:
1.  Install `pydantic-ai` and `logfire` <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
2.  Configure Logfire with Langfuse environment variables (Host, Public Key, Secret Key) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
3.  Ensure the agent is configured with `instrument=True` to enable Logfire and send communication through OpenTelemetry <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>, <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
4.  Custom metadata like user ID and session ID, along with input and output values, can be set on the agent execution trace using the OpenTelemetry library <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>, <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>, <a class="yt-timestamp" data-t="00:18:44">[00:18:44]</a>. This allows for granular control and filtering of logs by users and sessions <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>, <a class="yt-timestamp" data-t="00:24:10">[00:24:10]</a>.

This integration provides detailed insights into agent decisions, tool calls, parameters passed to tools, and responses, which is vital for troubleshooting and improving agent behavior in production <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>, <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>, <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. It also helps in identifying and diagnosing errors within tool calls <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>, <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.

## Self-Hosting and Local AI Stack

Langfuse is 100% [[opensource_libraries_for_agent_development | open-source]] <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, allowing users to self-host the platform for free and maintain utmost data privacy <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>, <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Self-hosting ensures all user interactions with the agent remain within one's own infrastructure <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

Setting up Langfuse for self-hosting involves managing services for data storage like Redis, Postgres, ClickHouse, and blob storage <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. A dedicated "local AI package" simplifies this process by curating open-source software for the database, large language model, user interface, and Langfuse for agent observability <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## N8N Integration (Current Status)

While there is strong demand from the community for a native [[integration_with_various_platforms | Langfuse node in N8N]] for workflow monitoring <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>, <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>, a direct native integration is not yet available <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>, <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>. Current workarounds involve custom setups using code nodes and custom tool nodes, which can be more complex and require hardcoding authentication keys, which is not ideal <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>, <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>. Langfuse maintainers have expressed willingness to contribute to such an effort <a class="yt-timestamp" data-t="00:25:58">[00:25:58]</a>, <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

## Conclusion

Integrating Langfuse provides essential observability for AI agents, allowing developers to monitor, troubleshoot, and improve agent performance, costs, and user interactions effectively <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>, <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. Its [[opensource_libraries_for_agent_development | open-source]] nature and comprehensive integration options make it a powerful tool for building production-ready AI agents <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.