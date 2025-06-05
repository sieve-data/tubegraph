---
title: Introduction to OpenTelemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[cloud_observability_with_opentelemetry | OpenTelemetry]] is an [[open_sourcing_and_applications_in_realworld_tasks | open source project]] maintained by the CNCF, standardizing cloud observability within cloud environments <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. It is one of the largest projects under the CNCF, second only to Kubernetes <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Core Purpose
[[cloud_observability_with_opentelemetry | OpenTelemetry]] serves as a protocol that standardizes how logging, metrics, and traces are handled in cloud applications <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. It is supported by every major observability platform, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb, allowing for seamless integration <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## [[features_and_functions_of_opentelemetry | Key Observability Signals]]

### Logging
Logging involves sending arbitrary events at any point in an application's lifecycle, which can be viewed later, often with metadata <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. It is comparable to simple print statements in programming <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Metrics
Metrics are used for aggregate-level data, showing how something behaves over time, across users, or other desired dimensions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Traditional Cloud Metrics:** Typically include CPU usage, memory usage, or latency <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Generative AI (GenAI) Metrics:** For GenAI-based applications, relevant metrics include token usage, latency, and error rate <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Tracing
Tracing tracks multi-step processes, which is crucial for understanding how requests are processed across multiple microservices in a cloud environment <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. For GenAI applications, tracing is particularly common due to the use of multi-step processes like chains, workflows, or agents that interact and run tools <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. [[traces_and_logs_for_performance_improvement | Traces]] were the first element defined by OpenTelemetry <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## [[features_and_functions_of_opentelemetry | OpenTelemetry Ecosystem]]
Beyond a protocol, [[cloud_observability_with_opentelemetry | OpenTelemetry]] is an ecosystem that includes:

### SDKs (Software Development Kits)
SDKs provide the means to manually send logs, metrics, and traces from applications <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. OpenTelemetry currently supports SDKs in 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Instrumentations
Instrumentations automatically gather observability data, providing visibility into specific parts of an application <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. For example, an instrumentation for an SQL Server like PostgreSQL can automatically emit logs, metrics, and traces <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. These work by "monkey patching" the client library used by the application, ensuring a negligible latency impact and providing a comprehensive view of system activity without manual intervention <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Collectors
Collectors are self-deployable components that can be deployed in a cloud environment (e.g., Kubernetes) to preprocess observability data before it is sent to an observability platform <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. They can be used to filter out unimportant data, obscure Personally Identifiable Information (PII) or sensitive data, and send data to multiple providers <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. These ready-made, [[open_sourcing_and_applications_in_realworld_tasks | open source]] components offer many built-in features <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

## OpenTelemetry and Generative AI
Trace Loop has extended [[cloud_observability_with_opentelemetry | OpenTelemetry]] to support various GenAI frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This [[integration_of_opentelemetry_with_gen_frameworks | integration]] allows users to automatically obtain logs, metrics, and traces from their GenAI applications within their preferred observability platforms <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

With over 40 different providers supported through community-built instrumentations, this includes:
*   **Foundation Models:** OpenAI, Anthropic, Cohere, Gemini, Bedrock, and others <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Vector Databases:** Pinecone, Chroma, and others <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Frameworks:** LangChain, LlamaIndex, CrewAI, and Haystack <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

For instance, a Pinecone instrumentation can capture queries, indexing activities, and allow investigation of returned vectors, including data, distances, and scores <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## [[benefits_of_using_opentelemetry_for_llm_applications | Advantages]]
[[cloud_observability_with_opentelemetry | OpenTelemetry]] provides a standardized way to connect LLM-based applications to existing observability platforms <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Being a standard protocol, it prevents vendor lock-in, enabling easy switching between platforms through simple configuration changes, as all supporting platforms use the same format <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.