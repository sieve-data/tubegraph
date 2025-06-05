---
title: Building reliable AIbased customer support systems
videoId: sXXl3YMU7ZI
---

From: [[aidotengineer]] <br/> 

Building an AI-native customer support platform presents unique challenges, particularly concerning reliability and managing complexity in systems that interact directly with end-users and rely on Large Language Models (LLMs) in production <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Traditional TypeScript, while a strong foundation, can fall short when dealing with unreliable APIs, complex dependencies, non-deterministic model outputs, or long-running workflows <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Leveraging Effect for Robust Systems

To address these challenges, the TypeScript library 'Effect' is utilized for [[best_practices_for_building_resilient_ai_workflows | building robust, type-safe, and composable systems]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Effect provides essential tools to handle complex situations confidently as a platform evolves <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

Key features of Effect include:
*   Strong type guarantees across the stack <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Powerful composition primitives <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   Built-in concurrency, streaming, interruptions, and retry mechanisms <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   Structured error modeling <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   A clean dependency injection system that simplifies testing and modernization <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Easy observability via OpenTelemetry <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

Effect enables the creation of more stable, testable, and maintainable code at scale <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Its gradual adoption capability makes it a natural extension of TypeScript for existing codebases <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Architectural Implementation with Effect

Effect is used across the entire stack of an AI-native customer support platform. Key components include:
*   **React front end**: Powers dashboards, agent IDE, knowledge management, insights, analytics, and SDKs <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Internal RPC server**: Handles application logic, built on Effect RPC and a modified TanStack Query on the front end <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Public API server**: Uses Effect HTTP with auto-generated OpenAPI documentation from annotated schemas <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Data processing engine**: Syncs data from CRMs, documents, and databases, processing it for real-time analytics and reporting <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Agent workflows**: Written in a custom Domain Specific Language (DSL) built on Effect, allowing for a mix of deterministic and non-deterministic behavior <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **PostgreSQL database**: Used for both data and vector storage, with Effect SQL handling queries <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

All data is modeled using Effect schemas, which provide runtime validation, encoding, decoding, type-safe input/output handling, and auto-generated documentation <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Agentic Systems and Workflows

[[building_effective_ai_agents | AI agents]] act as planners, taking user input, devising a plan, selecting the appropriate action, workflow, or sub-agent, executing it, and repeating until the task is complete <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

*   **Actions**: Small, focused units of execution, akin to tool calls (e.g., fetching payment info, searching logs) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Workflows**: Deterministic multi-step processes (e.g., canceling a subscription involves collecting a reason, offering retention, checking eligibility, and performing cancellation) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Sub-agents**: Group related actions and workflows into larger, domain-specific modules (e.g., a billing agent or a log retrieval agent) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

To model this complexity, a DSL for workflows was built using Effect's functional pipe-based system, allowing for clear and composable expression of branching, sequencing, retries, state transitions, and memory <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Ensuring Reliability and Testability

Reliability is paramount for mission-critical systems <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **LLM Provider Fallbacks**: If one LLM provider fails, the system falls back to another with similar performance characteristics (e.g., GPT-4 mini to GD Flash 2.0 for tool calling) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This is modeled with retry policies that track state to avoid retrying failed providers <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Stream Duplication**: When answers are streamed to the end-user, token streams are duplicated; one directly to the user and another for internal storage (e.g., for analytics), which Effect facilitates <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Testing**: Heavy use of dependency injection enables mocking LLM providers and simulating failure scenarios <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This approach allows swapping service providers with mock versions without affecting internal system logic <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Enhancing Developer Experience

Effect significantly improves the [[best_practices_for_building_ai_agents | developer experience for building agentic systems]]:
*   **Schema-centric development**: Input, output, and error types are defined upfront with powerful encoding/decoding, providing strong type safety and auto-generated documentation <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Dependency Injection (DI)**: Services are provided at system entry points, allowing for flexible composition and easy mocking for testing <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Dependencies are guaranteed at compile time, ensuring all required services are provided <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Modularity and Composability**: Services are modular, enabling easy override of behavior or swapping implementations without altering system internals <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Strong Guard Rails**: Effect helps prevent common mistakes, allowing engineers new to TypeScript to become productive quickly and avoid bad patterns after the initial learning curve <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Lessons Learned and Adoption Strategy

While powerful, using Effect effectively requires discipline <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Error Handling**: It's crucial to be careful not to accidentally catch errors silently upstream, as this can lead to losing important failure information <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Dependency Injection at Scale**: Tracing where services are provided across multiple layers or subsystems can become challenging <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Learning Curve**: Effect has a significant ecosystem and many concepts, which can be overwhelming initially. However, once the initial learning curve is overcome, the benefits compound <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Effect helps build predictable and resilient systems, but it is not a magic solution; developers still need to apply critical thinking <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

A key advantage of Effect is its incremental adoption strategy <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Developers can start with a single service or endpoint and expand its use from there <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. Effect is particularly useful for LLM and [[developing_ai_agents_for_productivity | AI-based systems]] where reliability and coping with non-determinism are critical <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. It provides tools for building predictable and observable systems <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

Effect introduces the rigor of functional programming into real-world TypeScript in a practical way <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, allowing developers to gain value without being functional programming purists <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Starting small allows benefits to accrue over time <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.