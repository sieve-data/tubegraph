---
title: Agent frameworks and orchestration layers in AI engineering
videoId: UcW_s4BmuD0
---

From: [[aidotengineer]] <br/> 

[[full_stack_ai_engineering_in_serverless_environments | Full stack AI engineering]] today involves deploying "zero ops resilient agent-powered user-ready apps" in serverless environments <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. The core challenge for [[the_future_of_ai_engineering | AI engineers]] is to get [[ai_agents_in_devops | agentic workflows]] into the hands of users <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This modern approach necessitates a specific infrastructure, which typically includes a client application, an [[components_of_ai_agents | agent framework]], an [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | orchestration layer]], all running serverlessly in the cloud <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Agent Frameworks

[[components_of_ai_agents | Agent frameworks]] are foundational for building AI applications. There are numerous options emerging constantly <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Examples of Agent Frameworks
*   Langchain <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   Vercel's AI SDK <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   Flowwise agents <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>
*   OpenAI's agents SDK <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>

### Preferred Agent Framework: OpenAI Agents SDK
The OpenAI agents SDK is highlighted for its capabilities <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>:
*   Native tool calling <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
*   One-shot [[multiagent_orchestration_for_ai_copilot_development | multi-agent calls]] <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
*   Built-in tracing and evaluation hooks for observability <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>
*   Strong backing from OpenAI, ensuring longevity <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>
*   Ability to interchange models, preventing vendor lock-in <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>

## Orchestration Layers

[[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | Orchestration layers]] are crucial for managing complex AI workflows, especially for long-running jobs that might exceed typical cloud function time limits <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### Examples of Orchestration Layers
*   Temporal <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>
*   AWS Step Functions <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   Langmith <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>
*   Ingest <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>

### Preferred Orchestration Layer: Ingest
Ingest is favored for its event-driven nature and ease of use <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>:
*   Uses events to trigger workflows, eliminating the need to manage JSON state machines <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
*   Operates entirely on demand, removing concerns about server warm-up <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
*   Features automatic retry mechanisms <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>
*   Provides step-level observability to monitor workflow progress and identify errors <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>
*   Offers a one-click integration with Vercel <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>

## Integrating Agent Frameworks and Orchestration
A recommended stack for [[state_of_ai_engineering | AI engineering]] combines Next.js for the client application, OpenAI's agents SDK for agentic capabilities, Ingest for orchestration, and Vercel for serverless deployment <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

### Architectural Overview
The typical architecture involves a Next.js client app connected to a database <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. When new work is needed, the client app triggers a workflow by sending an event to the Ingest service <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Ingest, acting as the orchestration layer, manages the connection to Python serverless functions where the [[components_of_ai_agents | AI agents]] (using the OpenAI agents SDK, which is currently Python-only) are running <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Vercel automatically hosts these Python functions <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. These functions handle AI inference and return results to the orchestration layer, which then updates the client app and caches data in the database <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Example Application Workflow
An example application that generates a newsletter demonstrates this integration <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The workflow highlights:
*   **Serverless Scalability**: The system supports long-running jobs without crashing or exceeding time limits for cloud functions, enabling cost efficiency by paying only for actual usage <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Local Developer Experience**: The setup allows for a seamless local development environment requiring three terminals for Python agents, Next.js, and the Ingest dev server <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Type Safety**: Full type safety is maintained across the stack using Pydantic in Python and TypeScript in Next.js <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Ingest Workflow Structure**: Workflows in Ingest define clear, individual steps. Each `step.run` invocation ensures reliable, sequential execution, passing results between steps <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. For instance, one agent performs research, another formats the newsletter, and a final step saves the output to storage <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.
*   **Vercel Deployment**: Vercel automatically detects and deploys Python functions within the API directory, simplifying [[building_ai_agents_without_frameworks | AI agent]] deployment without requiring complex configuration files like `vercel.json` <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

This combination of tools offers expected scalability, resilience, and the full [[ai_agents_in_devops | agentic power]] of OpenAI's SDK <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.