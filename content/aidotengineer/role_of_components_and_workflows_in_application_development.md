---
title: Role of components and workflows in application development
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

## The Evolution of AI Application Development

The journey of an AI engineer often begins with simple prompts and tool calls, which can be sufficient for initial prototypes. However, as applications mature, the focus shifts to building robust workflows to manage the inherent non-determinism of AI models and make as much of the code deterministic as possible <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This often involves chaining specific prompts and carefully controlling context, increasing workflow runtimes from seconds to minutes <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

Ultimately, [[impact_of_ai_on_development_workflow | AI engineers often transition into data engineers]] due to the complexity of getting the correct context into prompts, which may require crawling user data, ingesting code from GitHub, or processing many artifacts using Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Challenges with Traditional Infrastructure for AI Applications

Traditional web 2.0 infrastructure, designed for rapid API requests and database interactions (tens of milliseconds), is ill-suited for modern [[agentic_workflows_and_their_levels_of_autonomy | AI applications]]. These applications often have P1 latencies of several seconds, even with fast models or prompt caches <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This creates significant reliability issues, as a multi-second request in the previous era would trigger an on-call page <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Key Infrastructure Pain Points:
*   **Reliability:** LLM applications are built on "shoddy foundations," making it hard to create reliable apps <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Frequent outages and issues from dependencies are common <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Availability:** Major AI service providers like OpenAI may experience downtime, and even simultaneous outages across different providers (e.g., OpenAI and Gemini) can occur <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Rate Limits:** Bursty traffic patterns from batch processing or new customer onboarding often hit rate limits, requiring significant investment to unlock higher tiers <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Long-Running Workflows:** Existing serverless providers typically time out after 5 minutes and lack native streaming support or resumability, which are crucial for workflows that run for minutes or hours <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Solutions: Components and Workflows

To address these challenges, a structured approach using components and workflows, especially designed with infrastructure awareness, is crucial for building robust [[multiagent_systems_in_technical_workflows | multiagent systems in technical workflows]].

### What are Components?
Components are reusable, idempotent, and independently testable steps within a larger application <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. They can be simple functions, like a wrapped OpenAI SDK call, that take prompts, ingest context, and return a response <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

#### Benefits of Components:
*   **Reusability:** Promotes code sharing and composition <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Idempotence:** Ensures that executing a component multiple times has the same effect as executing it once.
*   **Testability:** Each component can be run or tested independently <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Retry and Error Boundaries:** Each component can have its own retry policy and error boundary, making it easier to manage transient failures <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Caching:** Components can be configured with a cache for improved performance <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### What are Workflows?
Workflows are collections of components that run together to achieve a larger task <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. For example, a workflow might fetch data, analyze posts, generate reports, and then write and edit content <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

#### Benefits of Workflows:
*   **Orchestration:** Connects individual components into a coherent process.
*   **Tracing and Debugging:** Provides top-level traces and detailed traces for all nested components, including token usage and model details, simplifying debugging <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Automatic REST APIs:** Workflows can be automatically exposed as REST APIs supporting synchronous and asynchronous invocation, with APIs for retrieving intermediate and final output streams <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Resumability:** Critical for long-running processes, allowing users to navigate away or refresh the page without losing context or progress <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. This is achieved by persistent storage of status and output streams, often via Redis streams <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
*   **User Engagement:** Allows for streaming intermediate status to keep users engaged during multi-minute operations, showing progress like data enrichment or content generation steps <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

## Infrastructure Design for Long-Running Agentic Workflows

A key architectural pattern for [[agentic_workflows_and_their_levels_of_autonomy | agentic workflows]] is the separation of the API layer and the compute layer <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

*   **API Layer:** Invokes the compute layer and receives a Redis stream ID. It then reads status and output directly from the Redis stream, not the compute layer <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Compute Layer:** Executes the sandbox program and emits heartbeats to monitor workflow completion. If a workflow crashes, it can be automatically restarted <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. This layer can be stateless and pluggable (e.g., running on ECS or user-provided compute) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

This separation allows for independent scaling of API and compute layers and enables critical features like resumability and transparent error handling <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. All API data flows to the Redis stream for both synchronous and asynchronous workflows, ensuring that the full history of status messages and output is preserved even if the user refreshes the page or disconnects <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

## Considerations for Deployment

When deploying long-running workflows, extreme care must be taken with draining workers and implementing blue/green deployment patterns to avoid disrupting ongoing processes <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. While it's easy to start building, getting these complex systems right requires attention to detail <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

Projects like Genisx (GenSx) offer open-source implementations of these concepts, providing an infrastructure-aware component model for building [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agent frameworks and orchestration layers in AI engineering]] designed for long-running, resilient workflows <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.