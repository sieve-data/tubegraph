---
title: Building reliable AI systems using Effect TypeScript
videoId: sXXl3YMU7ZI
---

From: [[aidotengineer]] <br/> 

Building reliable AI systems, especially those interacting directly with end-users and relying on large language models (LLMs) in production, presents significant challenges due to uncertain conditions <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Effect, a TypeScript library, is designed to manage this complexity by enabling the creation of robust, type-safe, and composable systems <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Why Effect for AI and LLM Systems?

While the [[typescript_for_robust_and_composable_system_design | TypeScript language]] provides a strong foundation, it falls short when dealing with specific challenges inherent in AI system development <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These challenges include:
*   Unreliable APIs <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Complex dependencies between systems <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>
*   Non-deterministic model outputs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   Long-running workflows <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>

Effect provides the necessary tools to confidently handle these situations as AI platforms evolve <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Key Features of Effect for Building Reliable AI Systems

Effect offers several features that contribute to the reliability and maintainability of AI systems:
*   **Strong type guarantees** across the stack <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>
*   Powerful **composition primitives** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>
*   Built-in **concurrency, streaming, interruptions, and retry mechanisms** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
*   **Structured error modeling** <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   A clean **dependency injection system** that facilitates easier testing and modernization <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>
*   Easy **observability via OpenTelemetry** <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>

These [[benefits_of_using_effect_in_typescript_for_ai_and_llm_systems | benefits of using Effect in TypeScript for AI and LLM systems]] lead to more stable, testable, and maintainable code at scale <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Effect can also be gradually adopted into existing codebases, feeling like a natural extension of TypeScript <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Architecture and Implementation at 14.ai

At 14.ai, Effect is used across the entire stack for their AI-native customer support platform <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>:
*   **Internal RPC Server**: Handles application logic, built on Effect RPC and a modified TanStack Query <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   **Public API Server**: Utilizes Effect HTTP with auto-generated OpenAPI documentation from annotated schemas <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Data Processing Engine**: Syncs and processes data from CRM, documents, and databases for real-time analytics and reporting <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   **Agent Workflows**: Written in a custom DSL built on Effect, allowing for a mix of deterministic and non-deterministic behavior <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Database**: PostgreSQL is used for both data and vector storage, with Effect SQL handling queries <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Effect Schemas**: Model everything, providing runtime validation, encoding/decoding, type-safe input/output handling, and auto-generated documentation <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Agent Design and Workflow with Effect

AI agents at 14.ai are essentially planners that take user input, devise a plan, choose appropriate actions, workflows, or sub-agents, execute them, and repeat until a task is complete <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

*   **Actions**: Small, focused units of execution, such as fetching payment information or searching logs, comparable to tool calls <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Workflows**: Deterministic multi-step processes, like cancelling a subscription, which might involve collecting reasons, offering retention options, checking eligibility, and then performing the cancellation <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Sub-agents**: Group related actions and workflows into larger domain-specific modules, such as a billing agent or a log retrieval agent <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

To model this complexity, a domain-specific language (DSL) for workflows was built using Effect's [[functional_programming_principles_with_typescript_and_effect | functional programming principles]] (pipe-based system) as the foundation <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This allows for clear and composable expression of branching, sequencing, retries, state transitions, and memory <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Reliability Mechanisms

For mission-critical systems, reliability is paramount <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>:
*   **LLM Provider Fallbacks**: If one LLM provider fails, the system automatically falls back to another with similar performance characteristics (e.g., GPT-4 mini to GD Flash 2.0 for tool calling) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Retry Policies**: Modeled with Effect, these policies track state to avoid retrying failed providers <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Token Stream Duplication**: For streamed answers to end-users, token streams are duplicated, sending one directly to the user and another for internal storage (e.g., analytics) <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Effect facilitates this process <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Testing and Developer Experience

Effect significantly enhances testing and developer experience:
*   **Dependency Injection (DI)**: Heavily used for mocking LLM providers and simulating failure scenarios <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This approach allows swapping service providers with mock versions without affecting system internals <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Schema-Centric Design**: Input, output, and error types are defined upfront with powerful encoding/decoding built-in <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. This provides strong type safety and automatically documented schemas <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Modular and Composable Services**: Services are provided at the entry point of systems, allowing for easy composition, overriding behavior, or swapping implementations <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Dependencies are guaranteed at compile time via the type level <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Strong Guard Rails**: Effect helps prevent common mistakes, allowing engineers new to TypeScript to become productive quickly <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Once past the initial learning curve, it becomes harder to fall into bad patterns <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Lessons Learned

While powerful, using Effect effectively requires discipline <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Error Handling**: It's easy to accidentally catch errors upstream or out of sight, silently losing important failures if not careful <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **Dependency Injection at Scale**: While great in principle, tracing service provision, especially across multiple layers or subsystems, can become challenging to follow <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Learning Curve**: Effect has a significant ecosystem of concepts and tools that can be overwhelming initially <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. However, once the initial hurdle is overcome, the benefits compound <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

Ultimately, Effect helps [[building_scalable_ai_systems | build scalable AI systems]] that are predictable and resilient, but it is not magic and still requires careful thought <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## Conclusion

Effect allows for incremental adoption, starting with a single service or endpoint <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. It is particularly useful for LLM and [[building_and_improving_ai_agents | AI-based systems]] where reliability and coping with non-determinism are crucial <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Effect provides tools for predictable and observable systems <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

It brings the rigor of functional programming into real-world TypeScript in a practical way for production use <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. One does not need to be a functional programming purist to gain significant value; starting small allows benefits to build up over time <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.