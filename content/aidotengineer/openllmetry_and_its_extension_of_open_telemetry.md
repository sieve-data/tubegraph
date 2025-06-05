---
title: OpenLLMetry and its extension of Open Telemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

OpenLLMetry is an open-source project that extends [[overview_of_open_telemetry | Open Telemetry]] to support Generative AI (GenAI) frameworks, foundation models, and vector databases <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. It allows developers to gain observability into their LLM-based applications by leveraging the existing capabilities of [[overview_of_open_telemetry | Open Telemetry]] <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

## Understanding Open Telemetry

[[overview_of_open_telemetry | Open Telemetry]] is a significant open-source project maintained by the CNCF (Cloud Native Computing Foundation) <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. It standardizes [[cloud_observability_with_open_telemetry | cloud observability]] in cloud environments <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. It is supported by every major observability platform, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

### Core Observability Pillars

At its core, [[overview_of_open_telemetry | Open Telemetry]] defines a protocol for standardizing [[logging_metrics_and_tracing_in_cloud_applications | logging]], metrics, and traces within cloud applications <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>:

*   **Logging**: Refers to arbitrary events that can be sent at any time during an application's lifecycle, which can then be viewed with associated metadata <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   **Metrics**: Used for aggregate-level data, showing behavior across time or users <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. In traditional cloud contexts, metrics include CPU/memory usage or latency <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. For GenAI applications, relevant metrics might include token usage, latency, and error rates <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   **Tracing**: Involves tracking a multi-step process, especially useful in microservices architectures to see how a request spans across multiple services <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. For GenAI, tracing is common because many processes involve multi-step chains, workflows, or [[llm_access_to_tools_and_tool_integrations | agents]] interacting with [[llm_access_to_tools_and_tool_integrations | tools]] <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

### Open Telemetry Ecosystem Components

Beyond the protocol, [[overview_of_open_telemetry | Open Telemetry]] provides an ecosystem of tools <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>:

*   **[[sdks_and_instrumentations_in_open_telemetry | SDKs]]**: Enable manual sending of logs, metrics, and traces from applications <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. [[overview_of_open_telemetry | Open Telemetry]] supports [[sdks_and_instrumentations_in_open_telemetry | SDKs]] for 11 different languages, including Python, TypeScript, Go, and C++ <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
*   **[[sdks_and_instrumentations_in_open_telemetry | Instrumentations]]**: Offer automatic collection of observability data from parts of an application <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. They work by "monkey patching" client libraries (e.g., for SQL servers like Postgres) to automatically emit relevant data with negligible latency impact <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
*   **Collectors**: Self-deployable components in a cloud environment (e.g., Kubernetes) that allow pre-processing of observability data before it's sent to a platform <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. They can filter data, obscure PII or sensitive information, and even send data to multiple observability providers <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

## OpenLLMetry: Extending Observability to GenAI

OpenLLMetry builds upon this established [[overview_of_open_telemetry | Open Telemetry]] framework by extending its support to [[cloud_observability_with_open_telemetry | cloud observability]] for GenAI applications <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.

### Key Extensions and Supported Technologies

OpenLLMetry has developed [[sdks_and_instrumentations_in_open_telemetry | instrumentations]] to support a wide range of GenAI technologies <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>:

*   **Foundation Models**: Includes providers like OpenAI, Anthropic, Cohere, Gemini, and Bedrock <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   **Vector Databases**: Such as Pinecone and Chroma <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Frameworks**: Supports LangChain, LlamaIndex, CrewAI, and Haystack <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.

With over 40 different providers supported, OpenLLMetry's [[sdks_and_instrumentations_in_open_telemetry | instrumentations]] automatically emit logs, metrics, and traces <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. For example, a Pinecone instrumentation can capture queries, indexing operations, and details about returned vectors, including distances and scores, all in the standard [[overview_of_open_telemetry | Open Telemetry]] format <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

### Benefits of OpenLLMetry

*   **Automatic Observability**: By leveraging [[sdks_and_instrumentations_in_open_telemetry | instrumentations]], OpenLLMetry provides automatic [[logging_metrics_and_tracing_in_cloud_applications | logs]], metrics, and traces for GenAI components, reducing manual effort <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Platform Agnostic**: Because it relies on the standard [[overview_of_open_telemetry | Open Telemetry]] protocol, OpenLLMetry allows users to get observability data in any supported platform (e.g., DataDog, Sentry, Grafana Tempo, Dynatrace) without being tied to a specific vendor <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. Switching between platforms becomes a simple configuration change <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>.
*   **Comprehensive View**: Provides a holistic view of everything happening within an LLM-based system, including interactions with various models, databases, and frameworks <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.