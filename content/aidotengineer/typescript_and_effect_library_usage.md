---
title: TypeScript and Effect Library usage
videoId: sXXl3YMU7ZI
---

From: [[aidotengineer]] <br/> 
The Effect library is a TypeScript library designed for building robust, type-safe, and composable systems <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. While TypeScript provides a strong foundation, it can fall short when dealing with unreliable APIs, complex inter-system dependencies, non-deterministic model outputs, or long-running workflows <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Effect provides tools to handle these situations confidently <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

14.ai, a company building an AI-native customer support platform, uses Effect to manage the complexity of systems that interact directly with end-users and rely on LLMs in production under uncertain conditions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Benefits of Effect

The Effect library offers several key features:
*   Strong type guarantees across the stack <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
*   Powerful composition primitives <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   Built-in concurrency, streaming, interruptions, and retry mechanisms <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   Structured error modeling <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   A clean [[dependency_injection_and_testing_in_typescript | dependency injection]] system that facilitates testing and modernization <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
*   Easy observability via [[sdks_and_instrumentations_in_open_telemetry | Open Telemetry]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>
*   The ability for [[incremental_adoption_of_effect_in_typescript_projects | gradual adoption]] into existing codebases <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   It feels like a natural extension of TypeScript <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

## 14.ai Architecture and Effect Integration

14.ai utilizes Effect across its entire stack <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Key components include:
*   **Front End**: A React front end powers dashboards, the agents ID, knowledge management, insights, analytics, and [[sdks_and_instrumentations_in_open_telemetry | SDKs]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Internal RPC Server**: Handles application logic, built on Effect RPC and a modified version of TanStack Query <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Public API Server**: Uses Effect HTTP, with Open API documentation automatically generated from annotated schemas <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Data Processing Engine**: Synchronizes data from CRMs, documents, and databases for real-time analytics and reporting <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Agent Workflows**: Written in a custom Domain Specific Language (DSL) built on Effect, enabling a mix of deterministic and non-deterministic behaviors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Database**: PostgreSQL is used for both data and vector storage, with Effect SQL handling queries <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Schema Validation**: Everything is modeled using Effect Schemas, providing runtime validation, encoding, decoding, type-safe input/output handling, and auto-generated documentation <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Agentic Systems and Workflows

14.ai's agents function as planners, taking user input, devising a plan, choosing actions, workflows, or sub-agents, executing them, and repeating until a task is complete <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

*   **Actions**: Small, focused units of execution, similar to [[using_tools_and_function_calls_with_ai_sdk | tool calls]], such as fetching payment information or searching logs <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Workflows**: Deterministic, multi-step processes, like canceling a subscription, which might involve collecting a reason, offering retention options, checking eligibility, and performing the cancellation <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Sub-agents**: Group related actions and workflows into larger, domain-specific modules, such as a billing agent or a log retrieval agent <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

To model this complexity, a domain-specific language for workflows was built using Effect's functional, pipe-based system. This allows for clear and composable expression of branching, sequencing, retries, state transitions, and memory <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Reliability and Testing

Reliability is paramount for mission-critical systems <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Fallback Mechanisms**: If one LLM provider fails, the system falls back to another with similar performance characteristics (e.g., GPT-4 mini to GD Flash 2.0 for [[tool_usage_and_development_in_ai_frameworks | tool calling]]) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Retry Policies**: These policies model and track state to avoid retrying failed providers <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Streaming**: Answers are streamed to the end-user, with token streams duplicated for direct user delivery and internal storage (e.g., for analytics), a process facilitated by Effect <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Testing**: Heavy use of [[dependency_injection_and_testing_in_typescript | dependency injection]] allows mocking LLM providers and simulating failure scenarios. This approach enables easy swapping of services with mock versions without affecting system internals <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Developer Experience

Effect significantly enhances developer experience when building agentic systems:
*   **Schema-Centric**: Inputs, outputs, and error types are defined upfront using schemas with built-in encoding/decoding, strong type safety, and automatic documentation <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Dependency Injection**: Services are provided at system entry points, are composable, and easily mockable for testing. Dependencies are guaranteed at compile time at the type level <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Modularity**: Services are modular and composable, allowing easy overriding of behavior or swapping implementations without internal system changes <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Guard Rails**: Effect helps prevent common mistakes, allowing engineers new to TypeScript to become productive quickly and making it harder to fall into bad patterns after the initial learning curve <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Lessons Learned

While powerful, using Effect effectively requires discipline <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Error Handling**: It's easy to accidentally catch errors upstream or out of sight, silently losing important failures if not careful <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Dependency Injection at Scale**: While great in principle, tracing service provision, especially across multiple layers or subsystems, can become challenging <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Learning Curve**: Effect has a significant ecosystem with many concepts and tools, which can be overwhelming initially. However, once the initial bump is overcome, the benefits compound <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Effect helps build predictable and resilient systems but is not a magical solution; developers still need to think critically <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Incremental Adoption and Conclusion

A key advantage of Effect is its support for [[incremental_adoption_of_effect_in_typescript_projects | incremental adoption]]. Users can start with a single service or endpoint and build from there <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

Effect is particularly useful for LLM and AI-based systems where reliability and coping with non-determinism are crucial <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. It provides tools for predictable and observable systems <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. It also brings the rigor of [[functional_programming_and_schema_validation | functional programming]] into real-world TypeScript in a practical way for production use, without requiring users to be [[ocaml_and_functional_programming | functional programming]] purists <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.