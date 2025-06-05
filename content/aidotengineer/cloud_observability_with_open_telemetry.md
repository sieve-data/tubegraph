---
title: Cloud observability with Open Telemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[Overview of Open Telemetry | Open Telemetry]] is a significant open-source project maintained by the CNCF, standardizing cloud observability [00:00:04][00:00:31][00:00:40]. It is one of the largest projects under the CNCF, second only to Kubernetes [00:00:33][00:00:37].

The project enables unified [[logging_metrics_and_tracing_in_cloud_applications | observability]] across various cloud environments and is supported by every major observability platform, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb [00:00:45][00:00:50][00:00:59].

## Open Telemetry as a Protocol

At its core, [[Overview of Open Telemetry | Open Telemetry]] is a protocol that standardizes how [[logging_metrics_and_tracing_in_cloud_applications | logging]], [[logging_metrics_and_tracing_in_cloud_applications | metrics]], and [[logging_metrics_and_tracing_in_cloud_applications | traces]] are managed in cloud applications [00:01:05][00:01:08][00:01:11].

*   **Logging**: Refers to arbitrary events that can be sent at any time during an application's lifecycle, often with associated metadata [00:01:16][00:01:29][00:01:40].
*   **Metrics**: Represents data intended to be viewed at an aggregate level, showing behavior over time or across various dimensions [00:01:42][00:01:46]. In traditional cloud environments, this might include CPU usage, memory usage, or latency [00:01:56][00:01:58][00:02:01]. For Gen AI applications, metrics could include token usage, latency, and error rates [00:02:05][00:02:08][00:02:13].
*   **Tracing**: Involves tracking a multi-step process, especially across distributed systems like microservices [00:02:21][00:02:31][00:02:37]. It allows users to observe how a request is processed across multiple services [00:02:40][00:02:46]. In Gen AI, tracing is particularly common for multi-step processes such as chains, workflows, or [[AI agents in DevOps | agents]] that interact with and run tools [00:02:54][00:02:59][00:03:03][00:03:06].

## Open Telemetry as an Ecosystem

Beyond being a protocol, [[Overview of Open Telemetry | Open Telemetry]] functions as an ecosystem, encompassing [[SDKs and instrumentations in Open Telemetry | SDKs]], [[SDKs and instrumentations in Open Telemetry | instrumentations]], and collectors [00:03:23][00:03:25][00:03:28].

### SDKs
[[SDKs and instrumentations in Open Telemetry | SDKs]] (Software Development Kits) are tools that allow developers to manually send [[logging_metrics_and_tracing_in_cloud_applications | logs]], [[logging_metrics_and_tracing_in_cloud_applications | metrics]], and [[logging_metrics_and_tracing_in_cloud_applications | traces]] from their applications [00:03:32][00:03:35]. Open Telemetry currently supports SDKs in over 11 different languages, including Python, TypeScript, Go, and C++ [00:03:37][00:03:40][00:03:43][00:03:47].

### Instrumentations
[[SDKs and instrumentations in Open Telemetry | Instrumentations]] provide a way to automatically gather observability data from specific parts of an application [00:03:55][00:03:58][00:04:10][00:04:30][00:04:32]. They achieve this by "monkey patching" client libraries used within the application, automatically emitting relevant data without manual intervention [00:04:54][00:04:55][00:04:59][00:05:02]. These are engineered to have a negligible latency impact, offering a comprehensive view of system activity [00:05:09][00:05:13][00:05:16][00:05:20].

An extension of [[Overview of Open Telemetry | Open Telemetry]], known as [[openllmetry_and_its_extension_of_open_telemetry | OpenLLMetry]], has built more than 40 instrumentations to support Generative AI frameworks, foundation models (e.g., OpenAI, Anthropic, Cohere, Gemini, Bedrock), and vector databases (e.g., Pinecone, Chroma), as well as AI frameworks like LangChain, LlamaIndex, CrewAI, and Haystack [00:06:16][00:06:20][00:06:23][00:06:25][00:06:29][00:06:32][00:06:36][00:07:09][00:07:12][00:07:16][00:07:17][00:07:20][00:07:23][00:07:25][00:07:28][00:07:29][00:07:34]. For instance, a Pinecone instrumentation can capture queries, indexing operations, and details about returned vectors such as data, distances, and scores [00:07:54][00:07:56][00:07:58][00:08:01][00:08:04][00:08:07][00:08:10][00:08:13][00:08:15][00:08:18][00:08:20].

### Collectors
Collectors are self-deployable components that can be deployed in a cloud environment (e.g., Kubernetes) to preprocess observability data before it is sent to an observability platform [00:05:25][00:05:30][00:05:32][00:05:34][00:05:36]. They can be used for tasks such as filtering unimportant data, obscuring Personally Identifiable Information (PII), or hiding sensitive data [00:05:40][00:05:43][00:05:45][00:05:47][00:05:49]. Collectors also allow sending observability data to multiple providers simultaneously [00:06:00][00:06:02][00:06:04]. These components are open-source and include many built-in features [00:05:52][00:05:54][00:05:55][00:05:57].

## Benefits of Open Telemetry

Using [[Overview of Open Telemetry | Open Telemetry]] ensures that applications are not tied to a specific observability platform [00:08:41][00:08:43]. Because it is a standardized protocol supported by many platforms, users can easily switch between them with a simple configuration change [00:08:44][00:08:47][00:08:48][00:08:51][00:08:53].