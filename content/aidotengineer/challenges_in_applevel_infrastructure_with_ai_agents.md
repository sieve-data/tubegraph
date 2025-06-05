---
title: Challenges in applevel infrastructure with AI agents
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

Developing applications with AI agents introduces significant infrastructure challenges, particularly at the compute layer, fundamentally changing assumptions from previous eras of web development <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Evolution of AI Engineering Workflows

The journey of an AI engineer often begins with a simple prompt and a few tool calls, which might be sufficient for initial funding <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this quickly evolves into building complex workflows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
Initially, engineers aim to make non-deterministic AI code as deterministic as possible by chaining tailored prompts, using `eval`s, and carefully controlling context, extending workflow runtimes from 30 seconds to several minutes <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Eventually, AI engineers become data engineers because the most challenging aspect is providing the correct context to prompts <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This involves tasks like crawling user inboxes, ingesting code from GitHub, or processing other artifacts that require extensive LLM processing <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Shifting Infrastructure Assumptions

Traditional Web 2.0 infrastructure was designed for web services that made API requests, interacted with databases, and returned responses in milliseconds <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. In such an environment, a request taking a couple of seconds would trigger an alert <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

However, in AI applications, a P1 (high-priority issue) might involve a response time of a few seconds, even with fast models or prompt caching <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The infrastructure developed over the last decade is not suitable for today's AI applications <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Challenges with Current AI Infrastructure

Building reliable AI applications on current foundations is difficult <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Reliability and Availability
AI applications often suffer from reliability issues with their underlying dependencies <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Services like OpenAI or Gemini can experience outages simultaneously <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### Rate Limits
Even without outages, developers must contend with rate limits, especially given the bursty traffic patterns that arise from batch processing documents or onboarding new customers <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Achieving higher rate limits often requires significant financial investment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Limitations of Existing Tools for Long-Running Workflows
While tools for long-running workflows and data engineering exist, such as SQS queues, batch processing tools like Airflow, or durable execution engines like Temporal, they are often not ideal for full-stack AI engineers <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Current serverless providers are also poorly suited for long-running AI workflows because most time out after five minutes, some limit outgoing HTTP requests, and none have native streaming support <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Streaming and resumability are crucial for applications that might run for multiple minutes, allowing users to refresh the page without losing context <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Product Experience Challenges

Long-running [[challenges_in_developing_ai_agents | AI agent]] workflows present specific challenges for user experience:

*   **Onboarding and Data Ingestion**: When ingesting data from a user's URL using an LLM, the initial scrape might take minutes and involve hundreds of LLM calls to extract and enrich content <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Users should be able to use the product immediately, requiring this ingestion to run in the background with visible status updates to prevent fall-off <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Content Generation and Agentic Workflows**: For processes like generating a blog post, which can take several minutes, the application needs to keep the user engaged by showing progress steps (e.g., research, outline, section writing) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Crucially, if a user leaves and returns to the page, they should not lose context or progress <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
    *   Previously, workflows taking 3-4 minutes already created friction, deterring experimentation with longer workflows (5+ minutes) due to the need for deep infrastructure changes <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
    *   Streaming both final content and intermediate status is vital, along with the ability to resume where left off if a user refreshes the page <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
    *   Intermediate errors are much more frustrating if it takes minutes to return to the previous state <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Solutions for Robust AI Agent Infrastructure

A robust solution involves building an infrastructure-aware component model designed for agentic workflows <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Infra-Aware Component Model
This framework is deeply aware of the underlying infrastructure it runs on, and vice-versa, allowing for features like resumable streams for intermediate status and final output <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. It's unopinionated and focuses on reusable building blocks <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

*   **Components**: These are reusable, idempotent, independently testable steps <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. An example is a wrapped OpenAI SDK call that provides tooling for retries and tracing while exposing the full OpenAI surface area <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Workflows**: Collections of components that run together, offering retry and error boundaries at each step, along with comprehensive traces for the workflow and its components <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Workflows can be automatically exposed as REST APIs supporting synchronous, asynchronous, and stream retrieval <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Debugging and Retries**: Built-in tracing provides detailed information on nested components, tokens, and OpenAI call details <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. Components also offer a fluent API for configuring retry policies (e.g., exponential retry) and caching <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

### Tailor-Made Serverless Platform
A serverless platform designed for long-running workflows and agentic UIs is crucial <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

*   **Separation of API and Compute Layers**: This allows for independent scaling of the API and compute layers <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The compute layer can be pluggable (e.g., defaulting to ECS but allowing user-provided compute) as it is stateless <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Redis Streams for Communication**: The API layer invokes the compute layer with a Redis stream ID, and subsequent communication for status and output happens via this stream <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Resumability and Monitoring**: All API interactions go through the Redis stream for both synchronous and asynchronous workflows, enabling resumability <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. The API layer reads solely from the Redis stream, not directly from the compute layer, allowing UIs to refresh, navigate away, and transparently handle errors while retaining full status history and output <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. The sandbox program emits heartbeats for background processes to monitor workflow completion, enabling automatic restarts or user notifications in case of failures <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Lessons for Building Agentic Workflow Infrastructure

*   **Start Simple, Plan for Long-Running**: Begin with basic workflows, but anticipate and design for a future where [[challenges_in_developing_ai_agents | agents]] will run for extended periods (e.g., an hour or more), taking instructions and performing work autonomously <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
*   **Separate Compute and API**: Keep your compute and API planes distinct to allow independent scaling and flexibility <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Leverage Redis Streams for Resumability**: Rely on Redis streams to manage state and output, making it easy for users to navigate away from a page without losing progress and enabling transparent error handling <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Careful Deployment**: When workflows run for extended durations (e.g., 60 minutes), implement robust deployment strategies like careful worker draining and blue/green deployments <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

While it's easy to start building AI agent applications, getting the infrastructure right is challenging and requires attention to detail <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

<div class="callout callout-info">
<div class="callout-title">Disclaimer: AI-Generated Diagrams</div>
<p>In the spirit of embracing AI for this talk, all diagrams presented were AI-generated. Be aware that the AI may still have spelling issues. <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a></p>
</div>