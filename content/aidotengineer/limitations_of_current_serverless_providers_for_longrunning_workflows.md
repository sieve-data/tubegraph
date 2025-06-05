---
title: Limitations of current serverless providers for longrunning workflows
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

AI applications, particularly those involving agents and complex workflows, introduce new demands on infrastructure that traditional web 2.0 paradigms and existing serverless providers struggle to meet <a class="yt-timestamp" data-t="02:01:06">[02:01:06]</a>. The shift from short, milliseconds-long requests to processes that can run for minutes or even hours highlights significant limitations in current serverless offerings <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

## The Evolution of AI Workflows and Infrastructure Demands

Traditionally, web 2.0 services involved simple API requests, database interactions, and quick returns within tens of milliseconds <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>. However, [[benefits_and_challenges_of_using_ai_in_workflow | AI applications]] operate differently:
*   **Extended Runtimes**: AI applications often have P1 (critical path) runtimes of several seconds at best, and this is only with fast models or prompt caches <a class="yt-timestamp" data-t="01:39:10">[01:39:10]</a>. Workflows can extend from 30 seconds to several minutes <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>.
*   **Data Engineering Shift**: As AI engineers build workflows from non-deterministic code, they increasingly become data engineers, focusing on getting the right context into prompts <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. This involves extensive LM processing to ingest data from sources like user inboxes or GitHub <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Reliability Challenges**: [[benefits_and_challenges_of_using_ai_in_workflow | LLM applications]] are built on "shoddy foundations," making it difficult to build reliable apps due to frequent outages and rate limits from dependencies like OpenAI <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. Traffic patterns can be extremely bursty, exacerbating rate limit issues <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Key Limitations of Existing Serverless Platforms

Existing serverless providers, while easy for quick prototypes (like a [[serverless_deployment_with_versel_and_nextjs | Next.js chatbot template]]), are not well-suited for [[longrunning_agents_and_failure_resilience | long-running workflows]] <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>:
*   **Timeout Limits**: Most serverless functions time out after approximately 5 minutes <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **HTTP Request Restrictions**: Some providers limit outgoing HTTP requests <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
*   **Lack of Native Streaming Support**: Streaming is typically bolted on at the application layer rather than being a native part of the infrastructure <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This is crucial for applications that run for multiple minutes <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Absence of Resumability**: Current serverless platforms generally do not offer native resumability <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. This means if a user refreshes the page or navigates away, the workflow context is lost <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>.

## Impact on User Experience and Development

These limitations create significant friction for developers and a poor experience for users:
*   **Development Friction**: [[full_stack_ai_engineering_in_serverless_environments | Full stack AI engineers]] are deterred from experimenting with workflows longer than five minutes because it necessitates deep infrastructure changes due to serverless provider limitations <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   **User Engagement**: For [[agent_continuations_for_ai_workflows | long-running agentic processes]], like content generation, users need constant engagement through intermediate status updates and the ability to resume without losing context <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
*   **Onboarding Challenges**: For processes like data ingestion, waiting 10 minutes for completion increases user fall-off in the funnel <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Background processing with real-time status updates is necessary <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.
*   **Error Handling**: If an intermediate error occurs, users become frustrated if they have to wait 5 minutes to get back to the same point <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

## Addressing the Challenges

While traditional [[longrunning_agents_and_failure_resilience | long-running workflows]] and data engineering tools like SQS, Airflow, or Temporal exist, they are often designed for Java engineers and are not ideal for TypeScript or [[full_stack_ai_engineering_in_serverless_environments | full stack engineers]] <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. A robust solution for [[longrunning_agents_and_failure_resilience | agentic workflows]] requires addressing these limitations by planning for a future that is inherently long-running <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>. This includes keeping compute and API layers separate and leveraging technologies like Redis streams for resumability <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.

```ad-note
It's easy to get started with basic prototypes, but building reliable and resilient [[longrunning_agents_and_failure_resilience | long-running AI workflows]] correctly in a serverless environment, especially when considering continuous deployment and worker draining, is very challenging <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
```