---
title: Role of serverless platforms in AI
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

The evolution of AI applications has significantly impacted infrastructure requirements, particularly concerning the compute layer <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While traditional web services focused on millisecond response times, AI applications often require runtimes of several seconds or even minutes, leading to new [[challenges_in_building_ai_applications | infrastructure challenges]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Evolution of AI Applications and Infrastructure Needs

Initially, AI engineers develop prototypes with simple prompts and tool calls <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, these prototypes quickly evolve into complex workflows, requiring the transformation of non-deterministic code into deterministic processes <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This involves chaining specific prompts and carefully controlling context, extending workflow runtimes from 30 seconds to several minutes <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Ultimately, AI engineers often transition into data engineers, as the primary challenge becomes gathering and ingesting the correct context for prompts, which may involve crawling user inboxes, ingesting GitHub code, or processing numerous other artifacts requiring extensive LLM processing <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Traditional Web 2.0 infrastructure, designed for API requests and database interactions returning responses in tens of milliseconds, is not suitable for modern AI applications <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. AI applications, even with fast models or prompt caches, typically have a P1 latency of a couple of seconds <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The unreliability of current LLM applications, characterized by frequent outages and rate limits, further complicates deployment <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Burst traffic patterns, common during batch processing or new customer onboarding, exacerbate rate limit issues, making it costly to achieve high traffic tiers for experimentation <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Challenges with Traditional Serverless Platforms for AI

While long-running workflows and data engineering have existing tools like SQS, Airflow, or Temporal, these are often designed for different paradigms <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. For full-stack developers accustomed to serverless environments, existing serverless providers pose several limitations for long-running AI workflows:
*   **Timeouts**: Most time out after 5 minutes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **HTTP Request Limitations**: Some limit outgoing HTTP requests <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Lack of Native Streaming Support**: Streaming must be bolted on at the application layer, not natively supported by the infrastructure <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **No Resumability**: Users lose context if they refresh the page or navigate away during a multi-minute process <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This is critical for product experiences like data ingestion during onboarding or multi-step content generation, where waiting 10 minutes for completion can increase user fall-off <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

## Key Requirements for Serverless AI Infrastructure

For effective AI deployments, especially with agentic workflows, the infrastructure needs to support:
*   **Long-running processes**: Workflows can take minutes or even hours <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Resumability**: Users should not lose progress if they leave or refresh the page <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   **Streaming**: Both final content and intermediate status updates need to be streamed to keep users engaged <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Transparent Error Handling**: Errors should be handled gracefully without forcing users to restart long processes <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Architectural Solution for Agentic Workflows

A tailored serverless platform for long-running workflows and agentic UIs addresses these challenges by separating the API and compute layers <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

### Separate API and Compute Layers
*   **Independent Scaling**: The API layer can scale independently of the compute layer <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Pluggable Compute**: The compute layer can be pluggable, allowing users to bring their own compute on top of existing solutions like ECS <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Redis Stream Communication**: The API layer invokes the compute layer and passes a Redis stream ID <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. All subsequent status and output are communicated via this Redis stream <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   **Heartbeats**: The sandbox program emits heartbeats, allowing background processes to monitor workflow completion and trigger restarts or notifications if a workflow crashes <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### Resumability via Redis Streams
*   The API layer reads directly from the Redis stream, not the compute layer <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   This enables UIs that allow users to refresh the page, navigate away, and still retrieve the full history of status messages and output without losing work <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

### Component Model for AI Workflows
A framework designed for these needs often utilizes an "infra-aware" component model <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This model provides:
*   **Reusable Components**: Independent, idempotent, and testable steps <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. An example is a wrapped OpenAI SDK call for retries and tracing <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Workflows**: Collections of components that run together <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Automatic REST APIs**: Workflows can be automatically exposed as REST APIs supporting synchronous and asynchronous invocation, with APIs to retrieve intermediate and final output streams <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Retry and Error Boundaries**: Every component includes built-in retry mechanisms and error boundaries, along with comprehensive tracing for debugging <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

## Lessons for Building AI Infrastructure

When developing infrastructure for agentic workflows:
*   **Start Simple**: Don't over-engineer for hour-long workflows on day one <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
*   **Plan for Long-Running Processes**: Anticipate that agents will increasingly perform extended, independent work <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Separate Compute and API Planes**: This allows for independent scaling and flexibility <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Leverage Redis Streams for Resumability**: Make it easy for users to navigate away without losing progress <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Careful Deployment**: For long-running workflows, pay close attention to worker draining and blue/green deployment patterns <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

While building this infrastructure can be complex, open-source libraries like Genisx aim to simplify the process for developers <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.