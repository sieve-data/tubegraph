---
title: Integration of OpenTelemetry with Gen Frameworks
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[introduction_to_opentelemetry | OpenTelemetry]] is an open-source project maintained by the CNCF, standardizing [[cloud_observability_with_opentelemetry | cloud observability]] in cloud environments <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It is supported by major observability platforms like Splunk, Datadog, Dynatrace, Grafana, and Honeycomb <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Core Concepts of OpenTelemetry

[[introduction_to_opentelemetry | OpenTelemetry]] primarily defines a protocol to standardize logging, metrics, and traces in cloud applications <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

*   **Logging**: Arbitrary events that can be sent anytime in an application's lifecycle and viewed later, possibly with metadata <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Metrics**: Data points seen at an aggregate level, showing behavior across time or users <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. In traditional cloud, these include CPU or memory usage and latency <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For GenAI applications, metrics might include token usage, latency, and error rate <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Tracing**: Tracking a multi-step process, such as requests spanning across multiple microservices in a cloud environment <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. For GenAI, tracing is common for multi-step processes like chains, workflows, or [[agentic_frameworks_and_tool_integration | agents]] that interact with tools <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Beyond the protocol, [[introduction_to_opentelemetry | OpenTelemetry]] is an ecosystem that includes SDKs, instrumentations, and collectors <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>:

*   **SDKs (Software Development Kits)**: Allow manual sending of logs, metrics, and traces from applications, supporting 11 different languages <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Instrumentations**: Enable automatic collection of observability data by monkey patching client libraries within an application <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. These are designed with negligible latency impact <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Collectors**: Self-deployable components that provide pre-processing capabilities for observability data, such as filtering, obscuring PII, or sending data to multiple providers, before it's sent to an observability platform <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## OpenELe.AI: Extending OpenTelemetry for GenAI

TraceLoop developed "OpenELe.AI" (referred to as "open elemetry" in the transcript) by extending the existing [[introduction_to_opentelemetry | OpenTelemetry]] project to support GenAI frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This extension leverages the existing [[features_and_functions_of_opentelemetry | OpenTelemetry]] infrastructure, allowing users to obtain observability data in any compatible platform (e.g., Datadog, Sentry, Grafana Tempo, Dynatrace) simply by configuring [[introduction_to_opentelemetry | OpenTelemetry]] <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Supported Integrations

OpenELe.AI has developed over 40 different providers through community collaboration <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. These include:

*   **Foundation Models**: OpenAI, Anthropic, Cohere, Gemini, Bedrock <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Vector Databases**: Pinecone, Chroma <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Frameworks**: LangChain, LlamaIndex, CrewAI, Haystack <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The instrumentations automatically emit logs, metrics, and traces, which can then be connected to any desired observability platform <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### Example: Pinecone Instrumentation

An instrumentation for Pinecone, a vector database, would provide visibility into:
*   Queries sent to Pinecone <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   Indexing processes within Pinecone <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   Investigation of returned vectors, including data, distances, and scores <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   Latencies <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

All this information is available in the standard [[introduction_to_opentelemetry | OpenTelemetry]] format <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

## Benefits

A key advantage of using [[introduction_to_opentelemetry | OpenTelemetry]] for integrating GenAI applications with observability platforms is its standardization <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This ensures users are not tied to a specific platform and can easily switch between providers with a simple configuration change, as all supporting platforms adhere to the exact same format <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.