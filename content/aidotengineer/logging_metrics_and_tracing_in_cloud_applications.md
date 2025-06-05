---
title: Logging metrics and tracing in cloud applications
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[overview_of_open_telemetry | Open Telemetry]] is a significant open-source project maintained by the CNCF, standardizing [[cloud_observability_with_open_telemetry | cloud observability]] in cloud environments <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It is one of the largest projects under the CNCF, second only to Kubernetes <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. [[overview_of_open_telemetry | Open Telemetry]] defines a protocol for logging, metrics, and traces, which are essential for understanding the behavior of cloud applications <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This standard is supported by all major observability platforms, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Observability Signals

### Logging
Logging involves recording arbitrary events that can be sent at any time during an application's lifecycle <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. These events are emitted as is and can be viewed later, potentially with associated metadata <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. For example, simply using a "print" statement in a Python script is a form of logging <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Metrics
Metrics represent data observed at an aggregate level, showing how a system behaves over time, across users, or other dimensions <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. In traditional cloud environments, common metrics include CPU usage, memory usage, and latency <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For [[ai_applications_and_customer_success_stories | GenAI applications]], relevant metrics might include token usage, latency, and error rates <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Tracing
Tracing involves tracking a multi-step process <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. In cloud environments with microservices, tracing allows visibility into a process that spans multiple services, showing how a user request is processed across them <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. Tracing is particularly common for [[ai_applications_and_customer_success_stories | GenAI applications]] due to their use of multi-step processes like chains, workflows, or agents that interact with tools <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## [[sdks_and_instrumentations_in_open_telemetry | Open Telemetry Ecosystem]]

Beyond defining a protocol, [[overview_of_open_telemetry | Open Telemetry]] also provides an ecosystem of tools including [[sdks_and_instrumentations_in_open_telemetry | SDKs]], [[sdks_and_instrumentations_in_open_telemetry | instrumentations]], and collectors <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### [[sdks_and_instrumentations_in_open_telemetry | SDKs]]
[[sdks_and_instrumentations_in_open_telemetry | SDKs]] (Software Development Kits) enable manual sending of logs, metrics, and traces from an application <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. [[overview_of_open_telemetry | Open Telemetry]] currently supports [[sdks_and_instrumentations_in_open_telemetry | SDKs]] in 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### [[sdks_and_instrumentations_in_open_telemetry | Instrumentations]]
[[sdks_and_instrumentations_in_open_telemetry | Instrumentations]] automate the collection of observability data <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Unlike [[sdks_and_instrumentations_in_open_telemetry | SDKs]] which require manual calls, [[sdks_and_instrumentations_in_open_telemetry | instrumentations]] can automatically provide visibility into parts of an application <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. For example, an [[sdks_and_instrumentations_in_open_telemetry | instrumentation]] for PostgreSQL can automatically generate logs, metrics, and traces related to SQL Server interactions <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. These work by monkey-patching client libraries used within the application and emitting desired data <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. They are designed to have a negligible latency impact <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Collectors
Collectors are self-deployable components that can be run in a cloud environment (e.g., Kubernetes) to pre-process observability data before sending it to a platform <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. They can be used to filter irrelevant data, obscure Personally Identifiable Information (PII) or sensitive data, and send data to multiple observability providers simultaneously <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. These open-source components come with many built-in features <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## [[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]] for GenAI Observability

[[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]], a project by Trace Loop, extends [[overview_of_open_telemetry | Open Telemetry]] to support various [[ai_applications_and_customer_success_stories | GenAI]] frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This extension leverages [[overview_of_open_telemetry | Open Telemetry]]'s existing capabilities to provide observability for AI systems <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

[[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]] provides [[sdks_and_instrumentations_in_open_telemetry | instrumentations]] for over 40 different providers <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>, including:
*   **Foundation models**: OpenAI, Anthropic, Cohere, Gemini, Bedrock <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>
*   **Vector databases**: Pinecone, Chroma <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>
*   **Frameworks**: LangChain, LlamaIndex, CrewAI, Haystack <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>

These [[sdks_and_instrumentations_in_open_telemetry | instrumentations]] automatically emit logs, metrics, and traces that can be connected to any preferred observability platform, offering an out-of-the-box solution <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. For example, the Pinecone [[sdks_and_instrumentations_in_open_telemetry | instrumentation]] can track queries, indexing, and allow investigation of returned vectors, including data, distances, and scores <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

By using [[overview_of_open_telemetry | Open Telemetry]], applications are not tied to a specific observability platform, allowing for easy switching through configuration changes, as all supporting platforms adhere to the same standard format <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.