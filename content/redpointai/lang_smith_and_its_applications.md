---
title: Lang Smith and its applications
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

[[Lang chain AI development | LangChain]], the popular framework for building LLM applications, recognized early on that an orchestration layer alone wasn't enough to simplify the development process. A significant need emerged around the observability, testing, and evaluation of these applications, leading to the creation of Lang Smith <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>.

## Core Functionality

Lang Smith operates as a separate Software as a Service (SaaS) platform, focused on making it easy to build, test, and understand LLM applications <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>. Its primary value propositions are:

*   **Tracing and Observability**: Lang Smith logs all steps of a chain or agent, including inputs, outputs, and their exact sequence <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This is particularly valuable for complex applications with multiple LLM calls or steps, providing immediate insight into what's happening and aiding in debugging <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Even for single LLM calls, it helps visualize templated prompts, conversational history, and trimmed content <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Testing and Evaluation (Eval)**: Lang Smith supports testing across the entire spectrum of an application, from end-to-end user interactions to individual components <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This includes evaluating specific steps like routing choices in an agent <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. The platform makes it easy to visualize and understand the thought processes of agents, as well as the inputs and outputs of each step, which is crucial for developers to "grock" these complex systems <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

## Addressing Evaluation Challenges

Evaluation in LLM applications presents several challenges:

*   **Data Set Creation**: Teams typically start by hand-labeling a small set of examples (e.g., 20) and then integrate production data that caused failures into their test sets <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. Lang Smith connects production traces that fail (either via user feedback like "thumbs down" or system flags) directly into the evaluation set <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. Creating an evaluation dataset also forces developers to consider specific desired behaviors and edge cases for the system <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **Judging Single Data Points**: While some simple classification tasks are straightforward, many require LLMs to act as judges <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. However, LLM-based judging isn't perfect, necessitating a human-in-the-loop component <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. Lang Smith invests heavily in facilitating human interaction to best support the evaluation process <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Aggregating Metrics**: How to aggregate evaluation metrics depends on the application. Some teams require perfect scoring for critical data points, while others need to confirm improvement over previous iterations <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Frequency of Evaluation**: Due to the expense and time involved, evaluations are often conducted largely before releases <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. Lang Smith aims to reduce the manual component to enable running evaluations in a continuous integration (CI) environment, similar to software unit tests <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Distinction from Traditional Observability

While there are parallels with traditional observability platforms like Datadog, Lang Smith addresses unique aspects of LLM applications <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>. LLMs are non-deterministic, and their applications involve APIs and prompting, which are new areas compared to traditional systems <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>.

Lang Smith focuses on helping users understand what LLM applications are doing to iterate faster and with confidence <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>. In contrast, tools like Datadog excel at system-level monitoring and aggregate metrics like latency <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. Companies have been observed using both platforms together, indicating different value propositions <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>.

## Integration and Development

Lang Smith is framework-agnostic, meaning it can be used with or without [[Lang chain AI development | LangChain]] <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>. It treats the system being scored simply as a function, making no assumptions about the number of LLM calls or internal workings <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.

The development of Lang Smith was prioritized because observability, testing, and evaluation were identified as bigger pain points for developers than hosting platforms <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. Lang Smith is a crucial component of [[Lang chain AI development | LangChain]]'s mission to make building LLM applications as easy as possible <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. It also ties into other [[Lang chain AI development | LangChain]] components, as evaluation is needed for both retrieval and agents, and agents can even be used to perform evaluation <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

Lang Smith was generally available as of recently (referring to the time of the podcast recording), after six months of iteration <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The team continually seeks to provide the most value by allocating resources to areas of greatest need, such as improving documentation and use cases <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.