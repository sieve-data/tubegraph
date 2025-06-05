---
title: Overview of Open Telemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[Cloud observability with Open Telemetry | Open Telemetry]] is a large, open-source project maintained by the CNCF, standardizing [[Cloud observability with Open Telemetry | cloud observability]] within cloud environments <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. It is one of the largest projects under the CNCF, second only to Kubernetes <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The project is supported by all major observability platforms, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This broad support means that [[Cloud observability with Open Telemetry | Open Telemetry]] can be used in conjunction with any of these platforms <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## What [[Cloud observability with Open Telemetry | Open Telemetry]] Standardizes

At its core, [[Cloud observability with Open Telemetry | Open Telemetry]] is a protocol that standardizes how [[Logging metrics and tracing in cloud applications | logging]], [[Logging metrics and tracing in cloud applications | metrics]], and [[Logging metrics and tracing in cloud applications | traces]] are handled in cloud applications <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### [[Logging metrics and tracing in cloud applications | Logging]]
[[Logging metrics and tracing in cloud applications | Logging]] refers to sending arbitrary events at any point in an application's lifecycle <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. These logs are emitted as-is and can be viewed later, potentially with metadata <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### [[Logging metrics and tracing in cloud applications | Metrics]]
[[Logging metrics and tracing in cloud applications | Metrics]] are designed for aggregate-level viewing, allowing users to observe behavior across days or users <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. In traditional cloud environments, [[Logging metrics and tracing in cloud applications | metrics]] typically include CPU usage, memory usage, and latency <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For Gen AI applications, relevant [[Logging metrics and tracing in cloud applications | metrics]] include token usage, latency, and error rate <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### [[Logging metrics and tracing in cloud applications | Tracing]]
[[Logging metrics and tracing in cloud applications | Tracing]] involves tracking multi-step processes, which was the first capability defined by [[Cloud observability with Open Telemetry | Open Telemetry]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. In cloud environments, [[Logging metrics and tracing in cloud applications | tracing]] is used to monitor processes that span across multiple microservices, showing how a user request is processed across them <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. For Gen AI, [[Logging metrics and tracing in cloud applications | tracing]] is particularly common due to the prevalence of multi-step processes like chains, workflows, and agents that interact with tools <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## The [[Cloud observability with Open Telemetry | Open Telemetry]] Ecosystem

Beyond being a protocol, [[Cloud observability with Open Telemetry | Open Telemetry]] is also an ecosystem comprising [[SDKs and instrumentations in Open Telemetry | SDKs]], [[SDKs and instrumentations in Open Telemetry | instrumentations]], and collectors <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### [[SDKs and instrumentations in Open Telemetry | SDKs]]
[[SDKs and instrumentations in Open Telemetry | SDKs]] (Software Development Kits) allow developers to manually send [[Logging metrics and tracing in cloud applications | logs]], [[Logging metrics and tracing in cloud applications | metrics]], and [[Logging metrics and tracing in cloud applications | traces]] from their applications <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. [[Cloud observability with Open Telemetry | Open Telemetry]] currently supports [[SDKs and instrumentations in Open Telemetry | SDKs]] in 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### [[SDKs and instrumentations in Open Telemetry | Instrumentations]]
[[SDKs and instrumentations in Open Telemetry | Instrumentations]] provide an automated way to gather [[Cloud observability with Open Telemetry | observability]] data <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Unlike [[SDKs and instrumentations in Open Telemetry | SDKs]] which require manual implementation, [[SDKs and instrumentations in Open Telemetry | instrumentations]] can automatically capture [[Logging metrics and tracing in cloud applications | logs]], [[Logging metrics and tracing in cloud applications | metrics]], and [[Logging metrics and tracing in cloud applications | traces]] from specific parts of an application <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. They function by "monkey patching" the client library used within an application to emit relevant data <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. These [[SDKs and instrumentations in Open Telemetry | instrumentations]] are engineered to have a negligible latency impact <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Collectors
Collectors are self-deployable components that can be placed in a cloud environment (e.g., Kubernetes) to preprocess [[Cloud observability with Open Telemetry | observability]] data before it is sent to an [[Cloud observability with Open Telemetry | observability]] platform <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. They can be used for tasks such as filtering unimportant data, obscuring Personally Identifiable Information (PII), or hiding sensitive data <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Collectors are open source and come with many built-in features <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. They also allow for sending [[Cloud observability with Open Telemetry | observability]] data to multiple providers simultaneously <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Extension for Generative AI: [[OpenLLMetry and its extension of Open Telemetry | OpenLLMetry]]

[[OpenLLMetry and its extension of Open Telemetry | OpenLLMetry]] is an open-source project that extends [[Cloud observability with Open Telemetry | Open Telemetry]] to support Generative AI (Gen AI) frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. By leveraging the existing [[Cloud observability with Open Telemetry | Open Telemetry]] standard, [[OpenLLMetry and its extension of Open Telemetry | OpenLLMetry]] enables [[Cloud observability with Open Telemetry | observability]] in any platform supporting [[Cloud observability with Open Telemetry | Open Telemetry]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

[[OpenLLMetry and its extension of Open Telemetry | OpenLLMetry]] has developed over 40 different [[SDKs and instrumentations in Open Telemetry | instrumentations]] for various providers <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>:
*   **Foundation models**: OpenAI, Anthropic, Cohere, Gemini, Bedrock, and others <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Vector databases**: Pinecone, Chroma, and others <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Frameworks**: LangChain, LlamaIndex, CrewAI, and Haystack <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

These [[SDKs and instrumentations in Open Telemetry | instrumentations]] automatically emit [[Logging metrics and tracing in cloud applications | logs]], [[Logging metrics and tracing in cloud applications | metrics]], and [[Logging metrics and tracing in cloud applications | traces]] that can be connected to any desired platform for out-of-the-box [[Cloud observability with Open Telemetry | observability]] <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. For example, a Pinecone [[SDKs and instrumentations in Open Telemetry | instrumentation]] can show queries, indexing activity, and allow investigation of returned vectors, including distances, scores, and latencies, all in the standard [[Cloud observability with Open Telemetry | Open Telemetry]] format <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

Because [[Cloud observability with Open Telemetry | Open Telemetry]] is a standard protocol, it prevents vendor lock-in, allowing users to easily switch between platforms with a simple configuration change <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.