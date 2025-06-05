---
title: SDKs and instrumentations in Open Telemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[overview_of_open_telemetry | Open Telemetry]] is an open-source project maintained by the CNCF, standardizing [[cloud_observability_with_open_telemetry | cloud observability]] by defining how to handle [[logging_metrics_and_tracing_in_cloud_applications | logging, metrics, and tracing]] <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. Beyond being a protocol, [[overview_of_open_telemetry | Open Telemetry]] is an ecosystem that includes Software Development Kits (SDKs) and Instrumentations <a class="yt-timestamp" data-t="03:23:59">[03:23:59]</a>.

## SDKs (Software Development Kits)

SDKs provide the means to manually send out [[logging_metrics_and_tracing_in_cloud_applications | logs, metrics, and traces]] from an application <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. This requires developers to explicitly add code to send the desired data <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. [[overview_of_open_telemetry | Open Telemetry]] currently supports SDKs in 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="03:37:37">[03:37:37]</a>.

## Instrumentations

Instrumentations offer an automatic way to obtain observability data <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Unlike SDKs, they do not require manual code changes to send data <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.

### How Instrumentations Work
Instrumentations automatically provide visibility into specific parts of an application <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. For example, an instrumentation for a database like PostgreSQL can automatically provide [[logging_metrics_and_tracing_in_cloud_applications | logs, metrics, and traces]] related to its operations <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

The mechanism behind instrumentations involves "monkey patching" the client library used within an application <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This allows the instrumentation to emit relevant data to the observability platform <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. All of this processing occurs on the application side <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. Instrumentations are designed with high engineering standards, resulting in an almost negligible latency impact while providing a comprehensive view of system activities <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

### Instrumentations in [[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]]
[[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]] extends [[overview_of_open_telemetry | Open Telemetry]] by building instrumentations specifically for Gen AI frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. The community has contributed to over 40 different providers, including:
*   **Foundation Models**: OpenAI, Anthropic, Cohere, Gemini, Bedrock <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>
*   **Vector Databases**: Pinecone, Chroma <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>
*   **Frameworks**: LangChain, LlamaIndex, CrewAI, Haystack <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>

These instrumentations automatically emit [[logging_metrics_and_tracing_in_cloud_applications | logs, metrics, and traces]], which can then be connected to any preferred observability platform, offering out-of-the-box observability <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

#### Example: Pinecone Instrumentation
An instrumentation for Pinecone would provide visibility into:
*   Queries sent to Pinecone <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>
*   Indexing processes within Pinecone <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>
*   Details of vectors returned from Pinecone, such as data, distances, scores, and latencies <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>

All this data is available in the standard [[overview_of_open_telemetry | Open Telemetry]] format <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>.

Using [[overview_of_open_telemetry | Open Telemetry]]'s standard protocol means users are not tied to a specific observability platform and can switch easily via configuration changes, as all supporting platforms adhere to the same format <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.