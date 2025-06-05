---
title: Features and Functions of OpenTelemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[introduction_to_opentelemetry | OpenTelemetry]] is a significant open-source project maintained by the CNCF, standardizing methods for [[cloud_observability_with_opentelemetry | cloud observability]] in cloud environments <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It is one of the largest projects under the CNCF, second only to Kubernetes <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. It is widely supported by major observability platforms including Splunk, DataDog, Dynatrace, New Relic, Grafana, and Honeycomb <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Core Components and Data Types

OpenTelemetry defines a protocol that standardizes logging, metrics, and tracing in cloud applications <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Logging
Logging involves sending arbitrary events at any point in an application's lifecycle <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. These events are emitted as is and can be viewed later, potentially with associated metadata <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Metrics
Metrics are used for aggregate-level data, allowing observation of behavior across different timeframes or users <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
*   **Traditional Cloud Metrics**: Common metrics include CPU usage, memory usage, and latency <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Gen AI Specific Metrics**: For Gen AI-based applications, relevant metrics include token usage, latency, and error rate <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Tracing
Tracing involves tracking multi-step processes <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. In cloud environments, this means observing a process that spans across multiple microservices, showing how a user request is processed <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. [[traces_and_logs_for_performance_improvement | Tracing]] is particularly useful for Gen AI applications due to their use of multi-step processes like chains, workflows, and agents <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## OpenTelemetry Ecosystem

Beyond the protocol, OpenTelemetry offers an ecosystem comprising SDKs, instrumentations, and collectors <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### SDKs (Software Development Kits)
SDKs enable manual sending of logs, metrics, and traces from applications <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. OpenTelemetry SDKs support 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Instrumentations
Instrumentations provide automatic collection of observability data <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. They work by "monkey patching" the client library used within an application (e.g., an SQL Server like PostgreSQL) to automatically emit logs, metrics, and traces <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. This process occurs on the application side with negligible latency impact, offering a comprehensive view of system activities without manual configuration <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Collectors
Collectors are self-deployable components that can be placed in a cloud environment (e.g., Kubernetes) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. They provide pre-processing capabilities for observability data before it's sent to a platform <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Data Filtering**: Can filter out unimportant data <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Data Obscuration**: Can obscure or hide Personally Identifiable Information (PII) or sensitive data <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   **Multi-Provider Export**: Allows sending observability data to multiple providers simultaneously <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
These collectors are open-source and come with many built-in features <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## OpenTelemetry for Gen AI

[[integration_of_opentelemetry_with_gen_frameworks | OpenTelemetry]] has been extended to support Gen AI frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This extension leverages the existing OpenTelemetry standard, allowing users to obtain observability data (logs, metrics, traces) automatically in their preferred platforms like DataDog, Sentry, Grafana Tempo, or Dynatrace <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

Key integrations include over 40 different providers <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>:
*   **Foundation Models**: OpenAI, Anthropic, Cohere, Gemini, Bedrock <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Vector Databases**: Pinecone, Chroma <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   *Example (Pinecone)*: An instrumentation for Pinecone can show queries, indexing, and allow investigation of returned vectors, including data, distances, and scores <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Frameworks**: LangChain, LlamaIndex, CrewAI, Haystack <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The use of instrumentations ensures that data emission is automatic <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. A significant [[benefits_of_using_opentelemetry_for_llm_applications | benefit of OpenTelemetry]] is that it acts as a standard protocol, preventing vendor lock-in and allowing easy switching between different observability platforms through simple configuration changes <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.