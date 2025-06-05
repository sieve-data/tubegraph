---
title: Impact of AI and agents on infrastructure
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

Evan Bole, founder and CEO of Genisx, presented on how [[role_of_ai_agents_and_agentic_frameworks | agents]] have significantly impacted infrastructure, with a particular focus on the compute layer <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Evolution of AI Engineering and Infrastructure Demands

The journey for AI engineers often begins with simple prompts and tool calls, which can be sufficient for initial funding rounds <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, as projects mature, the focus shifts to building complex workflows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This involves making non-deterministic code as deterministic as possible by chaining tailored prompts and carefully controlling context, extending workflow runtimes from seconds to minutes <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Eventually, AI engineers often transition into data engineers because the most significant challenge becomes providing the correct context to prompts <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This necessitates crawling user inboxes, ingesting data from platforms like GitHub, and processing numerous artifacts, all requiring extensive LLM processing <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Shifting Infrastructure Assumptions

Traditional Web 2.0 infrastructure, designed for simple web services with API requests, database interactions, and responses within tens of milliseconds, is ill-suited for modern [[impact_of_ai_on_organizational_operations_and_efficiency | AI applications]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. In [[impact_of_ai_on_organizational_operations_and_efficiency | AI applications]], a P1 (primary latency metric) of a couple of seconds is considered good, and only if a fast model or prompt cache is used <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Reliability and Availability Challenges

Current LLM applications are built on "shoddy foundations," making reliable app development difficult <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Outages from dependencies like OpenAI and Gemini can occur simultaneously, impacting service availability <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Even without full outages, rate limits pose a significant challenge, especially for bursty traffic patterns seen during batch processing or new customer onboarding <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Achieving higher rate limits often requires substantial financial investment <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The shift from simple prototypes to complex, long-running workflows turns full-stack AI engineers into data engineers <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Existing Solutions and Their Limitations

Long-running workflows, a niche historically, have existing data engineering tools <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
These include:
*   Queues like SQS <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>
*   Batch processing tools like Airflow <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>
*   Durable execution engines like Temporal <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>

However, these tools, often designed by Java engineers, are not preferred by full-stack TypeScript developers <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

Existing serverless providers are also not well-suited for long-running workflows due to:
*   Timeouts, typically after 5 minutes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>
*   Limitations on outgoing HTTP requests <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>
*   Lack of native streaming support, requiring it to be bolted on at the application layer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>
*   No inherent resumability, which is crucial for applications that run for multiple minutes and where users might refresh the page <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

## Product Experience Requirements for AI Agents

For [[role_of_ai_agents_and_agentic_frameworks | agentic workflows]], certain product experiences necessitate specific infrastructure capabilities:

*   **Onboarding**: Users submit a URL, an LLM extracts information, and a scraping job is kicked off in the background, making hundreds of LLM calls to enrich content <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Users need to start using the product immediately while ingestion occurs, and the system must show real-time status updates <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Waiting 10 minutes for ingestion increases user fall-off <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Content Generation**: For tasks like writing a blog post with an [[role_of_ai_agents_and_agentic_frameworks | agent]], the process can take several minutes, involving research, outlining, and section writing <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It's critical that if a user leaves or navigates away, they do not lose context or progress <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Running workflows longer than five minutes often requires deep infrastructure changes due to serverless provider limitations <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Streaming and Resumability**: Both final content and intermediate status need to be streamed <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. If a user refreshes the page, they should resume from where they left off, seeing the same status and output <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Intermediate errors are less frustrating if users don't lose significant progress <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## Genisx's Approach to Agentic Infrastructure

Genisx developed an open-source library to address these challenges, creating a simple, infrastructure-aware component model <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This framework provides resumable streams for intermediate status and final output <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

Key principles include:
*   **Anti-framework**: Unopinionated and focused on building blocks, taking inspiration from React's component model applied to the backend <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Composition over Abstraction**: Emphasizes sharing, composing, and reusing code rather than abstracting it <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

The solution consists of:
*   **Components**: Reusable, idempotent, independently testable steps <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. An example is a wrapped OpenAI SDK call that includes tooling for retries and tracing, while maintaining the same OpenAI surface area <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Workflows**: Collections of components that run together <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Each step in a workflow gets a retry boundary and an error boundary, along with traces at both the workflow and component levels for easy debugging <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Automatic REST APIs**: Workflows can be turned into REST APIs that support synchronous and asynchronous invocation, with APIs to retrieve intermediate and final output streams <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Built-in Features**: Components can be configured with a fluent API for features like exponential retry policies and caching <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Architectural Highlights

The platform is a serverless solution tailored for long-running workflows and [[role_of_ai_agents_and_agentic_frameworks | agentic UIs]] <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
Key architectural points include:
*   **Separation of API and Compute Layers**: These layers are completely separate, allowing independent scaling <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The API layer invokes the compute layer once, passing a Redis stream ID, and subsequent communication happens via the Redis stream <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Pluggable Compute Layer**: The compute layer is stateless and interacts only with the API layer and Redis streams, allowing users to bring their own compute <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Redis Streams for Resumability**: All API output goes to the Redis stream for both synchronous and asynchronous workflows <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This means the API layer reads from the Redis stream, not directly from the compute layer, enabling UIs that support page refreshes, navigation away, transparent error handling, and a full history of status messages and output <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. None of the work is lost if the user navigates away or the browser connection terminates <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
*   **Heartbeats**: The sandbox program emits heartbeats, allowing background processes to monitor workflow completion and automatically restart or notify users if a workflow crashes <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Lessons and Considerations for Building Agentic Infrastructure

When building infrastructure for [[role_of_ai_agents_and_agentic_frameworks | agentic workflows]], it's essential to:
*   **Start Simple**: Don't build for an hour-long workflow on day one, but plan for a future with long-running processes <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. The future of [[the_impact_and_future_potential_of_ai_and_agents | agents]] involves giving instructions and letting them work independently <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Separate Compute and API Planes**: This allows for independent scaling and flexibility <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Leverage Redis Streams for Resumability**: Make it easy for users to navigate away, not lose progress, and handle errors transparently <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Careful Deployment**: For workflows running for extended periods (e.g., 60 minutes), be cautious with draining workers and implement blue/green deployment patterns <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Attention to Detail**: While it's easy to get started, getting long-running [[role_of_ai_agents_and_agentic_frameworks | agentic workflows]] right is challenging due to the intricate details involved <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

For those not wanting to build this infrastructure themselves, Genisx provides an open-source library that implements many of these solutions <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.