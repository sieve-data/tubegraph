---
title: Functional programming principles with TypeScript and Effect
videoId: sXXl3YMU7ZI
---

From: [[aidotengineer]] <br/> 

Effect is a [[TypeScript for robust and composable system design | TypeScript]] library designed for building [[TypeScript for robust and composable system design | robust, type-safe, and composable systems]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It is particularly useful for [[Building reliable AI systems using Effect TypeScript | building reliable AI systems]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, especially those that interact directly with end-users, rely on [[benefits of using Effect in TypeScript for AI and LLM systems | LLMs]] in production, and must operate reliably under uncertain conditions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Why Effect?

While the [[TypeScript for robust and composable system design | TypeScript]] language itself provides a strong foundation, it can fall short when dealing with <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>:
*   Unreliable APIs <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Complex dependencies between systems <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   Non-deterministic model outputs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   Long-running workflows <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

Effect provides the tools to handle such situations confidently as a platform evolves <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Key Features

Effect helps in [[benefits of using Effect in TypeScript for AI and LLM systems | building more stable, testable, and maintainable code at scale]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a> by offering:
*   Strong type guarantees across the stack <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
*   Powerful composition primitives <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   Built-in concurrency, streaming, interruptions, and retry mechanisms <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Structured error modeling <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   A clean dependency injection system that simplifies testing and modernization <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
*   Easy observability via OpenTelemetry <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>

Effect can be gradually adopted into an existing codebase and feels like a natural extension of [[TypeScript for robust and composable system design | TypeScript]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Architectural Integration (14.ai Example)

At 14.ai, Effect is used across the entire stack <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **React Front End**: Powers dashboards, agent UIs, knowledge management, insights, analytics, and SDKs <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Internal RPC Server**: Handles app logic, built on Effect RPC and a modified TanStack Query <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Public API Server**: Uses Effect HTTP with auto-generated OpenAPI docs from annotated schemas <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Data Processing Engine**: Syncs data from CRM, docs, and databases for real-time analytics and reporting <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   **Agent Workflows**: Written in a custom DSL built on Effect, allowing a mix of deterministic and non-deterministic behavior <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Database**: PostgreSQL is used for data and vector storage, with Effect SQL handling queries <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

All data is modeled using Effect schemas, providing runtime validation, encoding, decoding, type-safe input/output handling, and auto-generated documentation <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Agent Workflow Design

Agents are designed as planners that take user input, devise a plan, choose actions, workflows, or sub-agents, execute them, and repeat until the task is complete <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Actions**: Small, focused units of execution, similar to tool calls (e.g., fetching payment info, searching logs) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Workflows**: Deterministic multi-step processes (e.g., canceling a subscription involves collecting a reason, offering retention, checking eligibility, and performing cancellation) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Sub-agents**: Group related actions and workflows into larger, domain-specific modules (e.g., a billing agent or log retrieval agent) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

This complexity is modeled using a domain-specific language for workflows built on Effect's functional pipe-based system. This allows expressing concepts like branching, sequencing, retries, state transitions, and memory in a clear and composable way <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Reliability and Testing

For mission-critical systems, reliability is key <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Effect facilitates this by:
*   **Fallback Mechanisms**: If one [[benefits of using Effect in TypeScript for AI and LLM systems | LLM]] provider fails, the system can fall back to another with similar performance characteristics (e.g., GPT-4 Mini to Gemini Flash 2.0 for tool calling) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This is modeled with retry policies that track state to avoid retrying failed providers <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Stream Duplication**: Answers streamed to end-users can be duplicated, sending one stream directly to the user and another for internal storage (e.g., analytics) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Effect makes this process easy <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Dependency Injection**: Heavy use of dependency injection allows mocking [[benefits of using Effect in TypeScript for AI and LLM systems | LLM]] providers and simulating failure scenarios for testing. Services can be swapped with mock versions without affecting system internals <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Developer Experience

Effect provides an excellent developer experience for [[Building reliable AI systems using Effect TypeScript | building agentic systems]] <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>:
*   **Schema-centric Design**: Input, output, and error types are defined upfront, providing powerful encoding/decoding, strong type safety guarantees, and automatic documentation <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Dependency Injection**: Services are provided at the system's entry point, allowing easy composition and mocking for testing. Dependencies are guaranteed at the type level at compile time <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Modularity and Composability**: Services are modular, making it easy to override behavior or swap implementations without impacting system internals <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Strong Guard Rails**: Effect helps prevent common mistakes, allowing engineers new to [[TypeScript for robust and composable system design | TypeScript]] to become productive quickly <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Lessons Learned

While powerful, using Effect effectively requires discipline <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Error Handling**: It's easy to accidentally catch errors upstream or out of sight, silently losing important failures if not careful <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Dependency Injection at Scale**: Tracing where services are provided across multiple layers or subsystems can become challenging <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Learning Curve**: Effect has a significant ecosystem with many concepts. It can be overwhelming initially, but benefits compound once the initial learning curve is overcome <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Ultimately, Effect helps build predictable and resilient systems, but it requires thoughtful design <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Incremental Adoption and Benefits

A significant advantage of Effect is its incremental adoptability <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. One can start with a single service or endpoint and expand from there <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

Effect is particularly useful for [[benefits of using Effect in TypeScript for AI and LLM systems | LLM and AI based systems]] where reliability and coping with non-determinism are crucial <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. It provides the tools to make systems predictable and observable <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

It brings the rigor of [[TypeScript for robust and composable system design | functional programming into real-world TypeScript]] in a practical way for production use <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. One doesn't need to be a functional programming purist to gain significant value; starting small allows benefits to build up over time <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.