---
title: Dependency injection and testing in TypeScript
videoId: sXXl3YMU7ZI
---

From: [[aidotengineer]] <br/> 

The [[TypeScript and Effect Library usage | Effect]] library, used by 14.ai for its AI-native customer support platform, incorporates a robust dependency injection (DI) system that significantly enhances testing and code maintainability in [[TypeScript and Effect Library usage | TypeScript]] projects <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This approach contributes to building stable, testable, and maintainable code at scale <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## Benefits of Dependency Injection for Testing

Effect's dependency injection system provides several advantages for testing:
*   **Mocking Providers** Heavy use of dependency injection allows for mocking Large Language Model (LLM) providers and simulating various failure scenarios <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This means service providers can be easily swapped with mock versions without altering the internal logic of the system <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Service Provisioning** Services are provided at the entry point of the system, enabling flexible composition and straightforward mocking for testing purposes <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Compile-Time Guarantees** Dependencies are defined at the type level, ensuring at compile time that all necessary services are provided <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **Modularity and Composability** Services are modular and composable, simplifying the process of overriding behavior or substituting different implementations without impacting the system's core <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Developer Experience

The dependency injection system is a strong point in the developer experience, contributing to a schema-centric approach where input, output, and error types are defined upfront, providing strong type safety and automatic documentation <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. Furthermore, [[TypeScript and Effect Library usage | Effect]] provides robust "guard rails," allowing engineers new to [[TypeScript and Effect Library usage | TypeScript]] to become productive quickly by helping prevent common mistakes <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Lessons Learned

While powerful, using dependency injection effectively requires discipline <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Complexity at Scale** Grasping dependency injection at scale can be challenging <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Tracing where services are provided, especially across multiple layers or subsystems, can become difficult to follow <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Learning Curve** [[TypeScript and Effect Library usage | Effect]] presents a significant learning curve due to its extensive ecosystem and numerous concepts <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. However, once the initial hurdle is overcome, the benefits compound <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.