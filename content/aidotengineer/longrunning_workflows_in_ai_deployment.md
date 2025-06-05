---
title: Longrunning workflows in AI deployment
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

## Introduction
The rise of [[AI agents and agentic workflows | AI agents]] and complex AI applications has introduced significant challenges for traditional infrastructure, particularly at the compute layer <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Unlike Web 2.0 services designed for low-latency, stateless requests, modern AI applications often involve [[agent_continuations_for_ai_workflows | longrunning workflows]] that can extend from minutes to hours <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This shift necessitates a re-evaluation of infrastructure design to support these extended execution times and ensure reliability <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

## The Evolution of AI Workflows
The journey of an AI engineer often begins with simple prompts and tool calls, which can quickly evolve into complex workflows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Initially, the focus is on making non-deterministic AI code as deterministic as possible through chaining tailored prompts and controlling context <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This process can extend workflow runtimes from 30 seconds to several minutes <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Ultimately, many AI engineers find themselves tackling data engineering challenges, as the most difficult aspect becomes providing the correct context to prompts, often requiring extensive LM processing of diverse data sources like inboxes or GitHub code <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Infrastructure Challenges for AI Applications
Traditional Web 2.0 infrastructure, designed for API requests completed in tens of milliseconds, is ill-suited for current AI applications <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. AI application latency, even with fast models or prompt caches, typically ranges from a few seconds to minutes <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This means that an alert-triggering latency in the past is now a best-case scenario <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Key challenges include:
*   **Reliability**: Building reliable AI applications is difficult due to frequent outages and rate limits from underlying dependencies like OpenAI and Gemini <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Outages can coincide across providers, and bursty traffic patterns from batch processing or new customer onboarding often hit rate limits unless significant investment is made in higher tiers <a class="yt-timestamp" data-t="00:02:46">[00:03:13]</a>.
*   **Long Runtimes**: Workflows that run for minutes or hours strain infrastructure designed for short, synchronous interactions <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This often forces AI engineers to become data engineers to manage these processes effectively <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Existing Solutions and Their Limitations
For [[managing_longrunning_agents_in_production | managing longrunning agents in production]] and workflows, existing data engineering tools are often employed:
*   **Queues**: Tools like SQS are used to build complex, "Rube Goldberg" machines for process orchestration <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Batch Processing Tools**: Airflow is a common choice for batch processing <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Durable Execution Engines**: Temporal provides capabilities for durable execution <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

However, these tools are often not ideal for full-stack AI engineers, especially those preferring modern web technologies like TypeScript <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

**Serverless Providers** (e.g., AWS Lambda, Vercel Functions) also have limitations for [[agent_continuations_for_ai_workflows | longrunning workflows]] <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>:
*   **Timeouts**: Most time out after 5 minutes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **HTTP Request Limits**: Some limit outgoing HTTP requests <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Lack of Native Streaming Support**: Streaming usually needs to be bolted on at the application layer, not natively supported by the infrastructure <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **No Resumability**: If a user refreshes a page or leaves, the context and progress are lost, which is critical for multi-minute processes <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## Use Cases for Longrunning Workflows
Longrunning workflows are essential for various AI product experiences:

1.  **Onboarding/Data Ingestion**:
    *   Users provide a URL, initiating a single LLM call to extract initial information and identify pages for scraping <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   A background scraping job then runs for multiple minutes, making hundreds of LLM calls to extract and enrich content <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
    *   The goal is to allow users to use the product immediately while ingestion happens in the background, showing status updates to prevent fall-off in the funnel <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

2.  **Content Generation Agents**:
    *   An [[ai_agents_and_agentic_workflows | AI agent]] might generate a blog post, a process explicitly communicated to the user as taking several minutes <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
    *   The user is shown intermediate steps like research, outlining, and section writing <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
    *   Crucially, if the user leaves or navigates away, they should not lose context, and the process should be resumable <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
    *   Streaming of both final content and intermediate status is vital, along with transparent error handling so users don't lose progress and get frustrated <a class="yt-timestamp" data-t="00:06:52">[00:07:11]</a>.

## Architectural Solutions for Longrunning Workflows
A robust approach to [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]] involves an infrastructure-aware component model:

### Component Model
*   **Infrastructure Awareness**: The framework is aware of the infrastructure it runs on, and vice-versa, enabling features like resumable streams for status and output <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Building Blocks**: Adopting an "anti-framework" philosophy, it focuses on reusable, idempotent, and independently testable components <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Components**: These are simple functions, often wrapping SDKs (like OpenAI's) to provide tooling for retries and tracing, taking prompts/context and returning responses <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Workflows**: Collections of components that run together, with each component providing a retry boundary and error boundary <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

### Key Features
*   **Tracing**: Workflows provide detailed traces of nested components, including token usage and OpenAI call details, simplifying debugging <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Built-in Retries**: Components can be configured with fluent APIs for things like exponential retry policies and caching, addressing specific problematic components <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Automatic REST APIs**: Workflows can automatically be exposed as REST APIs supporting synchronous and asynchronous invocation, with APIs to retrieve intermediate and final output streams <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Infrastructure Architecture (Example: Genisys)
A tailored serverless platform for longrunning workflows can separate the API and compute layers <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>:

*   **API Layer**: Invokes the compute layer and passes a Redis stream ID <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Compute Layer**: Executes the sandbox program. Communication after initial invocation happens via Redis streams <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   **Redis Streams**: Used for transmitting status, output, and heartbeats from the executing sandbox program <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This allows background processes to monitor workflow completion and automatically restart or notify users if a workflow dies <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

This separation offers several benefits:
*   **Independent Scaling**: The API and compute layers can scale independently <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Pluggable Compute**: The compute layer can be stateless and pluggable, allowing users to bring their own compute <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Resumability**: Since the API layer only reads from the Redis stream (not directly from compute), UIs can be built to support refreshing the page, navigating away, and transparently handling errors while maintaining the full history of status messages and output <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This ensures no work is lost even if the user or browser connection is terminated <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

## Key Considerations for [[best_practices_for_building_resilient_ai_workflows | Building Resilient AI Workflows]]
When [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]] that involve longrunning processes, consider the following:
*   **Start Simple, Plan for Longrunning**: Begin with simple workflows but design the infrastructure with the future in mind, anticipating that agents will increasingly handle complex, extended tasks <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
*   **Separate Compute and API Planes**: Keep these layers distinct and leverage Redis streams for resumability <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **User Experience**: Make it easy for users to navigate away without losing progress and handle errors transparently <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Deployment Care**: When workflows can run for 60 minutes, meticulous attention must be paid to deployment patterns like draining workers and blue-green deployments to avoid disruptions <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. [[scaling_ai_agents_in_production | Scaling AI agents in production]] and managing these long-running processes requires careful consideration of these details.
*   **Complexity**: While easy to prototype, getting longrunning [[ai_in_workflow_automation | AI in workflow automation]] right in production is challenging <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

> [!NOTE] Cost and latency optimization in AI deployments
> While not the primary focus, the design choices for [[scaling_ai_agents_in_production | scaling AI agents in production]] and supporting longrunning workflows inherently contribute to [[cost_and_latency_optimization_in_ai_deployments | cost and latency optimization in AI deployments]] by ensuring efficient resource use, managing rate limits, and improving overall system reliability.

For those not wishing to build this infrastructure from scratch, open-source libraries like Genisys implement many of these architectural patterns <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.