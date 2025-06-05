---
title: Best practices for building resilient AI workflows
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

Building artificial intelligence (AI) applications, particularly those involving [[developing_ai_agents_and_agentic_workflows | AI agents]] and long-running processes, presents significant infrastructure challenges. Traditional web infrastructure is often ill-suited for the unique demands of AI workloads, necessitating [[strategies_for_effective_ai_implementation | new strategies]] for resilience and efficiency <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## The Evolution of AI Engineering Challenges

The journey of an AI engineer often starts with a simple prompt and a few tool calls, which might be sufficient for initial prototypes <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. However, as applications mature, the focus shifts to building [[ai_in_workflow_automation | AI workflows]] <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. This involves making non-deterministic code as deterministic as possible by chaining tailored prompts and carefully controlling context <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. Workflows can quickly increase runtime from 30 seconds to several minutes <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.

Ultimately, many AI engineers find themselves becoming data engineers because the most challenging aspect is providing the correct context to prompts <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. This often requires complex data ingestion from various sources, such as user inboxes or GitHub, which demands extensive LLM processing <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

## Infrastructure Limitations for AI Applications

Assumptions about infrastructure have significantly changed for AI applications compared to Web 2.0 <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.
Traditional web services expect API requests to return data in tens of milliseconds <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. In contrast, AI applications often have P1 latencies of several seconds, even with fast models or prompt caches <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. This means infrastructure designed for the past decade of the web is not suitable for modern AI applications <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

Key issues impacting resilience include:
*   **Reliability**: LLM applications are built on "shoddy foundations," making it difficult to build reliable apps <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. Dependencies frequently experience outages, sometimes for extended periods <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Uptime**: Even major AI providers like OpenAI and Gemini can experience concurrent outages <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   **Rate Limits**: Burst traffic patterns, common when batch processing documents or onboarding new customers, quickly hit rate limits <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. High-tier rate limits often require significant financial investment <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

## The Need for [[longrunning_workflows_in_ai_deployment | Longrunning Workflows in AI Deployment]]

As workflows extend to minutes or hours, full-stack AI engineers inadvertently become data engineers <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

### Existing Solutions and Their Limitations
Existing tools for [[longrunning_workflows_in_ai_deployment | longrunning workflows]] and data engineering include message queues like SQS, batch processing tools like Airflow, and durable execution engines like Temporal <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. However, these are often designed with a different paradigm (e.g., Java engineering) and are not ideal for modern TypeScript/full-stack developers <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

Serverless providers, while appealing, are not well-suited for these types of workflows <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>:
*   **Timeouts**: Most time out after 5 minutes <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **HTTP Request Limits**: Some limit outgoing HTTP requests <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
*   **Lack of Native Streaming**: Streaming support must be bolted on at the application layer, not natively provided by the infrastructure <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.
*   **No Resumability**: Without native resumability, if a user refreshes the page or navigates away, the context of a multi-minute process is lost <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

### Common Product Experiences Requiring Resilience
AI applications often require workflows that run in the background while keeping users engaged:

*   **Onboarding Data Ingestion**: When a user inputs a URL for data ingestion, an initial LLM call might identify pages to scrape <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. The subsequent scraping job can take minutes and involve hundreds of LLM calls <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. To prevent user fall-off, ingestion must run in the background, with real-time status updates shown to the user <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   **Content Generation Agents**: For tasks like writing a blog post, an agent might run for multiple minutes, performing research, outlining, and writing sections step-by-step <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. It's crucial that if the user leaves the page or navigates away, they don't lose context, and can resume the process with the full history of status messages and output <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. Experiencing intermediate errors after a long wait is far more frustrating without resumability <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.

## Architectural [[best_practices_for_building_ai_agents | Best Practices for Building AI Agents]] and Workflows

To address these challenges, specialized infrastructure and frameworks are needed.

### Genisys Component Model and Workflows
Genisys developed an open-source library that provides an infrastructure-aware component model <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. This framework is unopinionated and focuses on reusable building blocks, taking inspiration from React's component model but applied to the backend <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. The goal is to allow sharing, composition, and reuse of code without excessive abstraction <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.

*   **Components**: Reusable, idempotent, independently testable steps <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. For example, a simple component might wrap the OpenAI SDK for LLM calls, providing tooling for retries and tracing while exposing the same API surface <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>.
*   **Workflows**: Collections of components that run together <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>. Each step in a workflow gains a retry boundary and an error boundary <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. Traces are provided at both the workflow and component levels, aiding debugging <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **REST APIs**: Workflows can be automatically turned into REST APIs supporting synchronous and asynchronous invocation, with APIs to retrieve intermediate streams and final output <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>.
*   **Built-in Retries and Caching**: Components have a fluent API to configure policies like exponential retries and caching <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>.

### Tailored Serverless Platform Architecture
Genisys built a serverless platform specifically designed for [[longrunning_workflows_in_ai_deployment | longrunning workflows]] and [[developing_ai_agents_and_agentic_workflows | agentic UIs]] <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.

Key architectural points include:
*   **Separation of API and Compute Layers**: The API layer and compute layer are completely separate <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. The API layer invokes the compute layer and passes a Redis stream ID <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. All subsequent communication (status, output) happens via the Redis stream <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>.
    *   **Benefits**: Allows independent scaling of API and compute layers <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>, and enables users to "bring their own compute layer" as the compute is stateless <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>.
*   **Redis Streams for Resumability**: The API layer only reads from the Redis stream, not directly from the compute layer <a class="yt-timestamp" data-t="11:22:00">[11:22:00]</a>.
    *   **Benefits**: UIs can be built that allow users to refresh the page, navigate away, and still receive the full history of status messages and output, without losing progress <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. Heartbeats from the executing sandbox program ensure background processes monitor workflow completion, allowing for automatic restarts or user notifications if a workflow crashes <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.

## Lessons for Resilient AI Workflow Infrastructure

When [[best_practices_for_building_ai_agents | building AI agents]] and their infrastructure:
*   **Start Simple, Plan for Long-Running**: Don't over-engineer on day one for an hour-long workflow, but plan for a future where workflows run for extended periods, as this is the direction of AI agents <a class="yt-timestamp" data-t="12:13:00">[12:13:00]</a>.
*   **Separate Compute and API**: Keep your compute and API planes separate for independent scaling and flexibility <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.
*   **Leverage Redis Streams for Resumability**: Use Redis streams to enable users to navigate away from the page, not lose progress, and handle errors transparently <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>.
*   **Careful Deployment**: When workflows run for extended periods, be meticulous about draining workers and implementing blue/green deployment patterns <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.

While it's easy to get started with [[building_effective_ai_agents | AI agents]], achieving the necessary resilience for [[longrunning_workflows_in_ai_deployment | longrunning workflows]] is complex and requires attention to detail <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.