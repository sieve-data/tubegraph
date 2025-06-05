---
title: Importance of infrastructure design for AI applications
videoId: _-oIuRH4oGA
---

From: [[aidotengineer]] <br/> 

Traditional infrastructure paradigms, largely shaped by Web 2.0 principles, are proving insufficient for the unique demands of modern AI applications, particularly those leveraging AI agents and large language models (LLMs) <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The shift in application characteristics necessitates a fundamental rethink of how computing resources are architected and managed.

## The Evolution of AI Engineering Needs

The journey of an AI engineer often begins with simple prompts and tool calls, enough to prototype a concept <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, as AI applications mature, engineers inevitably transition to building complex workflows <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This involves making non-deterministic AI code as deterministic as possible, often through chaining specific prompts, careful evaluation, and precise context control <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The most significant challenge quickly becomes "getting the right context into the prompts" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This requires extensive data ingestion and LLM processing, forcing AI engineers to effectively become [[data_engineering | data engineers]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Workflows that initially run for seconds can extend to minutes or even hours <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Limitations of Traditional Infrastructure for AI

The core assumptions underpinning Web 2.0 infrastructure are challenged by AI applications:
*   **Latency Expectations** In Web 2.0, a typical web service responds in tens of milliseconds <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. In contrast, AI applications often have a P1 (worst-case latency) of "a couple of seconds at best," even with fast models or prompt caches <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. A two-second response time would trigger an alert in a traditional setup <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Reliability and Outages** Building reliable AI applications is difficult due to the "shoddy foundations" of current LLM providers <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Major providers like OpenAI and Gemini experience frequent outages, sometimes simultaneously, making failover strategies ineffective <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Rate Limits and Bursty Traffic** AI applications, especially during batch processing or new customer onboarding, exhibit extremely bursty traffic patterns <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Contending with rate limits and obtaining higher service tiers often requires significant financial investment <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Serverless Provider Limitations** Existing serverless providers are not well-suited for long-running workflows, often timing out after 5 minutes, limiting outgoing HTTP requests, and lacking native streaming support <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Addressing the Challenges: Key Design Principles

To overcome these infrastructure limitations, a tailored approach is essential. This often involves building custom platforms or leveraging specialized tools designed for the unique demands of AI.

### Architectural Considerations for Long-Running AI Workflows
Key architectural points for [[ai_network_infrastructure | AI network infrastructure]] and long-running AI workflows include:
*   **Separation of API and Compute Layers** Decoupling the API layer from the compute layer allows for independent scaling and flexibility, enabling users to "bring their own compute layer" <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **Resumability with Redis Streams** All API output, for both synchronous and asynchronous workflows, is directed to a Redis stream <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. The API layer reads solely from this stream, not directly from the compute layer <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. This design ensures:
    *   **Resumability**: Users can refresh pages or navigate away without losing progress <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The system provides the full history of status messages and output upon reconnection <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   **Robustness**: Intermediate errors are handled transparently, preventing users from having to restart lengthy processes from scratch <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
*   **Infrastructure-Aware Component Model** A framework that is deeply aware of the underlying infrastructure can provide features like resumable streams for intermediate status and final output <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This "anti-framework" approach, inspired by React, focuses on reusable, idempotent, and independently testable "components" and "workflows" <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **Built-in Reliability Features** Components can be configured with built-in retries (e.g., exponential retry policies) and caching <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Each component also provides a retry and error boundary <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Enhanced Debugging** Automated tracing across workflows and nested components provides detailed information on token usage, OpenAI calls, and messages, simplifying debugging <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Product Experience Examples

Thoughtful infrastructure design enables superior user experiences for AI applications:

### Onboarding Experience
For applications requiring extensive data ingestion via LLMs upfront, a user can input a URL and immediately kick off a scraping job in the background <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. The application can then provide real-time status updates on the ingestion process, allowing users to start using the product immediately rather than waiting minutes, which can increase fall-off <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Content Generation
In a content generation app, where an agent might take multiple minutes to write a blog post, users can be told upfront that the process will take time <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The UI can display a step-by-step progression (e.g., research, outline, writing sections) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Crucially, if the user leaves and returns, they should see the same progress and context, preventing frustration from lost work <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## Lessons Learned and Future Considerations

When designing infrastructure for [[challenges_and_innovations_in_ai_engineering | agentic workflows]]:
*   **Start Simple, Plan for Long-Running** While initial workflows may be short, plan for a future where agents perform tasks for hours <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. [[the_future_of_ai_engineering | AI engineering]] is trending towards agents that operate independently and communicate on demand <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Separate Compute and API Planes** This separation, coupled with leaning on Redis streams for resumability, is critical for scaling and user experience <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Enable Seamless User Experience** Design for users to easily navigate away, not lose progress, and have errors handled transparently <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **[[best_practices_for_ai_deployment_and_optimization | Deployment and Optimization]] Care** For workflows running for extended periods, careful consideration must be given to deploying systems, including worker draining and blue/green deployment patterns <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. The [[cost_and_efficiency_in_deploying_ai_systems | devil is in the details]] when aiming for reliable, long-running systems <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

While building this infrastructure from scratch can be "fun," open-source solutions like GenSx aim to provide these capabilities for developers <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.