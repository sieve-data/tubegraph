---
title: Issues with nondeterministic and deterministic workflows
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

AI application development often begins with simple, **nondeterministic** interactions like a prompt and a few tool calls. However, as these applications mature, developers quickly move towards building **deterministic workflows** to ensure reliability and control [00:00:31]. This transition reveals significant challenges with existing infrastructure, particularly at the compute layer [00:00:06].

Evan Bole, founder and CEO of Genisx, highlights how agents have "broke infrastructure" [00:00:02].

## The Evolution of AI Workflows

Initially, AI engineers prototype with simple prompts and tool calls [00:00:31]. While this approach can suffice for early-stage development, real-world deployment necessitates a shift towards structured workflows [00:00:39].

> "We take that fully non-deterministic code and make as much of it deterministic as possible." <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

This often involves chaining specific prompts and carefully controlling the context to reduce runtime from minutes to seconds [00:00:50]. The most challenging aspect becomes managing data, as getting the right context into prompts requires ingesting and processing large volumes of data from various sources [00:01:08]. This turns AI engineers into data engineers [00:01:05].

## Infrastructure Assumptions vs. AI Demands

Traditional web 2.0 infrastructure was designed for API requests completed in tens of milliseconds [00:01:26]. In contrast, AI applications often have P1 latencies of several seconds, even with fast models or prompt caches [00:01:39]. This fundamental shift means that infrastructure designed for rapid, short-lived requests is ill-suited for the longer, more complex operations of modern AI applications [00:01:56].

### Reliability Challenges
Building reliable AI applications on current foundations is difficult [00:02:09]. Developers frequently face issues with dependencies:

*   **Outages:** Major AI service providers like OpenAI and Gemini can experience simultaneous outages, leading to significant downtime [00:02:14].
*   **Rate Limits:** Even without outages, developers must contend with rate limits, especially with bursty traffic patterns during batch processing or new customer onboarding [00:02:53]. Achieving higher rate limits often requires substantial financial investment [00:03:03].

## [[Limitations of current serverless providers for longrunning workflows | Limitations of Existing Tools for Long-Running Workflows]]

The need for [[agentic_workflows_and_their_levels_of_autonomy | agentic workflows]] and long-running processes exposes weaknesses in conventional tools:

*   **Traditional Data Engineering Tools**: While tools like SQS, Airflow, and Temporal exist for batch processing and durable execution, they are often considered niche or cumbersome for full-stack developers, particularly those working with TypeScript [00:03:38].
*   **[[Limitations of current serverless providers for longrunning workflows | Existing Serverless Providers]]**:
    *   **Timeouts**: Most serverless functions time out after around 5 minutes [00:04:08].
    *   **HTTP Request Limits**: Some limit outgoing HTTP requests [00:04:11].
    *   **Lack of Native Streaming**: Streaming support for intermediate status or final output often needs to be "bolted on" at the application layer, rather than being a native infrastructure feature [00:04:16].
    *   **No Resumability**: If a user refreshes a page or navigates away during a long-running process, progress is typically lost, leading to frustration [00:04:31].

## Examples of Long-Running AI Workflows

These limitations directly impact user experience in common AI product scenarios:

### Onboarding Experience
Ingesting user data with LLMs can involve scraping many pages and making hundreds of LLM calls, taking multiple minutes [00:05:08]. To avoid increased user fall-off, this ingestion must run in the background, with users being able to see the status as more data is enriched [00:05:28].

### Content Generation
An [[agent_continuations_for_ai_workflows | agent]] generating a blog post might involve research, outlining, and writing sections, taking several minutes [00:05:43]. Critical requirements for such experiences include:
*   **Context Preservation**: Users must not lose context if they leave the page or navigate away [00:06:10].
*   **Resumability**: If the user refreshes, they should see the current status and output [00:06:56].
*   **Streaming**: Both final content and intermediate status need to be streamed [00:06:52].
*   **Transparent Error Handling**: Intermediate errors should not force users to restart a 5-minute process from scratch [00:07:04].

Previous experiences show significant friction when [[evaluating_and_optimizing_ai_agents_and_workflows | experimenting with longer workflows]], often forcing deep infrastructure changes to accommodate processes exceeding five minutes [00:06:23].

## A Proposed Infrastructure Solution

Genisx developed an open-source library that addresses these issues with an infrastructure-aware component model [00:07:26].

*   **Component Model**: Inspired by React, this model applies to the backend, focusing on reusable, idempotent, and independently testable steps called "components" [00:07:56].
*   **[[Role of components and workflows in application development | Workflows]]**: [[Role of components and workflows in application development | Workflows]] are collections of components that run together [00:08:11]. Each step in a workflow provides retry and error boundaries, along with detailed tracing for debugging [00:08:57].
*   **Serverless Platform**: The solution deploys to a serverless platform designed for [[agentic_workflows_and_their_levels_of_autonomy | agentic UIs]] and long-running background processes [00:10:04].
    *   **Separation of API and Compute Layers**: These layers are completely separate, allowing independent scaling and pluggable compute options [00:10:14].
    *   **Redis Stream Communication**: The API layer invokes the compute layer once and passes a Redis stream ID. All subsequent communication, status updates, and output occur via this Redis stream [00:10:23].
    *   **Heartbeats**: The sandbox program emits heartbeats to monitor workflow execution, allowing for automatic restarts or user notifications if a workflow dies or crashes [00:10:41].
    *   **Resumability**: Because the API layer only reads from the Redis stream, not directly from the compute layer, UIs can be built to allow users to refresh pages, navigate away, and transparently handle errors while still retrieving the full history of status messages and output [00:11:27]. This ensures no work is lost if the user disconnects [00:11:59].

## Lessons for Building Infrastructure for [[Agent continuations for AI workflows | Agent Workflows]]

When designing infrastructure for [[agentic_workflows_and_their_levels_of_autonomy | agentic workflows]]:

*   **Start Simple, Plan for Long-Running**: Begin with straightforward workflows but anticipate that agents will evolve to run for extended periods, potentially hours [00:12:13]. The future of agents involves giving instructions and letting them work independently [00:12:31].
*   **Separate Compute and API Planes**: This architectural separation is crucial for scalability and flexibility [00:12:39].
*   **Lean on Redis Streams for Resumability**: Utilize durable messaging or streaming mechanisms to ensure progress is not lost and users can resume from where they left off [00:12:41].
*   **Handle Deployment Carefully**: For long-running workflows, meticulous attention to worker draining and blue-green deployment patterns is necessary [00:12:54].

While it's easy to get started with AI workflows, building robust and reliable infrastructure for them is complex, with the "devil in the details" [00:13:06].