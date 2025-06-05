---
title: Challenges in building AI applications
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

Building AI applications, particularly those involving AI agents, presents a distinct set of [[challenges_in_ai_development | challenges]] for infrastructure and development compared to traditional web applications <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Evolution of AI Development Workflows

Initially, AI engineering often begins with a simple prompt and a few tool calls, which might be sufficient for early-stage development <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, this quickly evolves into building complex workflows to make non-deterministic code as deterministic as possible <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This involves chaining tailored prompts, careful context control, and extensive evaluation <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The runtime of these workflows can increase from seconds to several minutes <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

Ultimately, AI engineers often transition into data engineers because the most significant [[challenges_in_ai_agent_development | challenge]] lies in providing the right context to prompts <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This can involve crawling user inboxes, ingesting data from sources like GitHub, and processing numerous artifacts with Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Shifting Infrastructure Assumptions

Traditional Web 2.0 infrastructure, designed for rapid API requests and database interactions returning responses in tens of milliseconds, is not well-suited for modern AI applications <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. AI applications, especially those using LLMs, often have a response time of several seconds at best, even with fast models or prompt caches <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. A multi-second response time that would trigger an alert in previous infrastructure paradigms is now common <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Reliability and Availability Concerns

Building reliable AI applications today is difficult due to what is described as "shoddy foundations" <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Developers frequently encounter issues and outages from core dependencies like OpenAI and Gemini, sometimes simultaneously <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

Beyond outages, developers must contend with rate limits, especially given the bursty traffic patterns that arise from tasks like batch processing documents or onboarding new customers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Achieving higher rate limits often requires significant financial investment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## Challenges with Long-Running Workflows

As AI workflows extend from minutes to hours, full-stack AI engineers increasingly face [[technical_challenges_in_ai_agent_development | challenges]] typically associated with data engineering <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

Existing tools for long-running workflows, such as SQS, Airflow, or Temporal, are often complex and not ideal for full-stack developers <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Current serverless providers are also generally ill-suited for long-running workflows because they:
*   Time out after about 5 minutes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   May limit outgoing HTTP requests <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   Lack native streaming support, requiring it to be bolted on at the application layer <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Do not inherently support resumability, which is crucial if a user refreshes a page during a multi-minute process <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Common Product Experience Challenges

Building AI applications for product experiences like onboarding or content generation highlights key [[challenges_in_implementing_gen_ai_projects | implementation challenges]]:

### Onboarding
For user onboarding, where a significant amount of data might be ingested upfront using an LLM, the process can take multiple minutes and involve hundreds of LLM calls <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. To prevent user fall-off, this ingestion must run in the background, and the application needs to transparently show the status to the user as they immediately begin using the product <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Content Generation
In applications like content generation where an agent performs tasks over several minutes, it's essential to:
*   Inform the user about the expected duration <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   Display the step-by-step progress (e.g., research, outlining, writing sections) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   Ensure that if a user leaves or navigates away from the page, they don't lose context or progress, requiring resumability <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Stream both the final content and intermediate status to the user <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   Minimize user frustration by handling intermediate errors transparently, avoiding the need to restart a 5-minute process from the beginning <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

The friction involved in experimenting with longer workflows (e.g., beyond five minutes) often forces developers to make deep infrastructure changes due to serverless provider limitations, hindering rapid iteration <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Solutions and Architectural Considerations

To address these [[challenges_in_creating_effective_ai_agents | challenges]], an infrastructure-aware component model can be adopted <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This approach focuses on building blocks and takes inspiration from React's component model, applying it to the backend <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Key elements of such a solution include:
*   **Components**: Reusable, idempotent, and independently testable steps <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. An example is a simple function that wraps an OpenAI SDK call, providing tooling for retries and tracing <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   **Workflows**: Collections of components that run together <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Workflows offer retry boundaries, error boundaries, and traces at both the workflow and component levels for easy debugging <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Automatic REST APIs**: Workflows can be automatically exposed as REST APIs supporting synchronous and asynchronous invocation, with APIs to retrieve intermediate and final output streams <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Built-in Retries and Caching**: Components can be configured with fluent APIs for exponential retry policies and caching <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Architectural Blueprint
A tailored serverless platform for long-running workflows and agentic UIs can be built with a critical separation of API and compute layers <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. This separation allows for:
*   **Independent Scaling**: The API layer can scale independently of the compute layer <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Pluggable Compute**: The stateless compute layer can be pluggable, allowing users to bring their own compute <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Redis Streams for Resumability**: All API output flows through Redis streams for both synchronous and asynchronous workflows <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The API layer reads solely from the Redis stream, not directly from the compute layer <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This design enables UIs to offer:
    *   **Page Refresh Resilience**: Users can refresh the page or navigate away without losing progress <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
    *   **Transparent Error Handling**: Errors are handled without work loss <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   **Full History**: Access to the complete history of status messages and output <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   **Heartbeats**: The sandbox program emits heartbeats to monitor workflow execution and ensure completion, with automatic restart or user notification if a workflow crashes <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Lessons for Building AI Infrastructure

When building infrastructure for agentic workflows, it's advised to:
*   **Start Simple, Plan for Long-Running**: Don't over-engineer from day one, but anticipate future needs for workflows that run for extended periods, as this is the direction of AI agents <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
*   **Separate Compute and API**: Maintain a distinct compute and API plane <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Leverage Redis Streams**: Utilize Redis streams for resumability and to ensure progress is not lost when users navigate away or connections terminate <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Transparent Error Handling**: Design systems to handle errors gracefully and transparently for the user <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
*   **Careful Deployment**: Implement robust deployment strategies, such as blue/green deployments and careful worker draining, especially for workflows running for extended durations <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

While it is easy to get started with AI applications, getting the underlying infrastructure right for long-running, reliable agentic workflows is considerably more difficult <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. For those who prefer not to build all this infrastructure themselves, open-source libraries like Genisx implement many of these solutions <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.