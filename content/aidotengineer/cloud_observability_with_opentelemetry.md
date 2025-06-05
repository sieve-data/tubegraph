---
title: Cloud Observability with OpenTelemetry
videoId: KVgbERRPU4M
---

From: [[aidotengineer]] <br/> 

[[introduction_to_opentelemetry | OpenTelemetry]] is an [[open_sourcing_and_applications_in_realworld_tasks | open source]] project maintained by the CNCF, one of the largest projects after Kubernetes [00:00:31]. Its primary purpose is to standardize cloud [[development_and_deployment_of_observability_platforms | observability]] [00:00:40]. It is supported by every major [[development_and_deployment_of_observability_platforms | observability]] platform, including Splunk, Datadog, Dynatrace, New Relic, Grafana, and Honeycomb [00:00:50]. Using [[introduction_to_opentelemetry | OpenTelemetry]] allows seamless integration with any of these platforms [00:00:57].

## What is OpenTelemetry?

At its core, [[introduction_to_opentelemetry | OpenTelemetry]] is a protocol that standardizes how [[traces_and_logs_for_performance_improvement | logging]], metrics, and [[traces_and_logs_for_performance_improvement | traces]] are handled in cloud applications [00:01:05].

### Logging
[[traces_and_logs_for_performance_improvement | Logging]] refers to an arbitrary event that can be sent at any point in an application's lifecycle [00:01:29]. These logs are emitted as is and can be viewed later, potentially with associated metadata [00:01:37].

### Metrics
Metrics are designed for aggregate-level viewing, allowing users to observe behavior across different timeframes (e.g., days) or user groups [00:01:44]. In traditional cloud environments, common metrics include CPU usage, memory usage, and latency [00:01:56]. For Gen AI-based applications, relevant metrics might include token usage, latency, and error rates [00:02:08].

### Traces
Tracing involves tracking a multi-step process [00:02:31]. In cloud environments with microservices interacting, traces allow users to monitor a process that spans across multiple services, observing how a request is processed from the user through various microservices [00:02:35]. For Gen AI applications, tracing is particularly common due to the prevalence of multi-step processes like chains, workflows, or [[zero_ops_resilient_agent_powered_apps | agents]] that interact and run tools [00:02:54].

## OpenTelemetry as an Ecosystem

Beyond being a protocol, [[introduction_to_opentelemetry | OpenTelemetry]] functions as an ecosystem, offering various components to facilitate [[telemetry_and_monitoring_in_ai_data_centers | telemetry]] data collection [00:03:23]. This ecosystem includes SDKs, instrumentations, and collectors [00:03:25].

### SDKs
SDKs (Software Development Kits) provide a way to manually send logs, metrics, and [[traces_and_logs_for_performance_improvement | traces]] from an application [00:03:32]. [[introduction_to_opentelemetry | OpenTelemetry]] currently supports SDKs in 11 different languages, including Python, TypeScript, Go, and C++ [00:03:40].

### Instrumentations
Instrumentations automate the process of collecting [[telemetry_and_monitoring_in_ai_data_centers | observability]] data [00:03:55]. Unlike SDKs, which require manual implementation, instrumentations automatically gather data from specific parts of an application, such as an SQL server (e.g., PostgreSQL) [00:03:58]. They achieve this by monkey patching client libraries used within the application, emitting desired data with negligible latency impact [00:04:54].

### Collectors
Collectors are self-deployable components that can be deployed in a cloud environment (e.g., Kubernetes) [00:05:25]. They provide pre-processing capabilities for [[telemetry_and_monitoring_in_ai_data_centers | observability]] data before it is sent to a chosen [[development_and_deployment_of_observability_platforms | observability platform]] [00:05:36]. Collectors can be used to filter out unimportant data, obscure PII, or route [[telemetry_and_monitoring_in_ai_data_centers | observability]] data to multiple providers [00:05:42].

## OpenElemetry: Extending OpenTelemetry for Gen AI

OpenElemetry is an extension of [[introduction_to_opentelemetry | OpenTelemetry]] specifically designed to support Gen AI frameworks, foundation models, and vector databases [00:06:20]. By leveraging [[introduction_to_opentelemetry | OpenTelemetry]], OpenElemetry enables users to obtain [[development_and_deployment_of_observability_platforms | observability]] within any preferred platform (e.g., Datadog, Sentry, Grafana Tempo, Dynatrace) [00:06:42]. This setup automatically provides logs, metrics, and [[traces_and_logs_for_performance_improvement | traces]] [00:07:01].

The OpenElemetry community has developed over 40 different providers and instrumentations [00:07:10]. These include support for:
*   **Foundation models:** OpenAI, Anthropic, Cohere, Gemini, Bedrock, and others [00:07:16].
*   **Vector databases:** Pinecone, Chroma, and others [00:07:23].
*   **[[integration_of_opentelemetry_with_gen_frameworks | Frameworks]]:** LangChain, LlamaIndex, Crew AI, and Haystack [00:07:28].

For example, the Pinecone instrumentation provides visibility into queries, indexing, and the ability to investigate returned vectors, including data, distances, and scores [00:07:58].

A significant [[benefits_of_using_opentelemetry_for_llm_applications | benefit of using OpenTelemetry for LLM applications]] is that its standardized protocol prevents vendor lock-in [00:08:41]. Users can easily switch between [[development_and_deployment_of_observability_platforms | observability platforms]] through a simple configuration change, as all supporting platforms adhere to the exact same format [00:08:44].