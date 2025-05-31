---
title: Lang chain AI development
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

LangChain, founded by Harrison Chase, is the most popular framework for working with large language models (LLMs), boasting over 38,000 Discord members and adoption by companies like Elastic, Dropbox, and Snowflake <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The platform serves as a general-purpose, horizontal framework for building LLM applications, primarily focused on providing an orchestration layer that connects LLMs to external data and computation <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

## Core Functionality and Product Offerings

LangChain's open-source package revolves around enabling the creation of diverse LLM applications. Common use cases include:
*   **Chatbot over your data** <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Data extraction** for enterprise applications <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Assistant-like things**, such as natural language to query databases, text to SQL, or text to arbitrary APIs <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The framework's core areas of focus are **retrieval**, **agents**, and **evaluation**, which are highly interconnected. Agents can utilize retrieval, retrieval is a common tool for agents, and evaluation is crucial for both, with agents even being used to perform evaluation <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### [[advancements_in_ai_developer_tools | LangSmith]]: Observability and Testing for LLM Applications

LangSmith is a separate SaaS platform developed by LangChain, generally available as of recently, focusing on observability, testing, and evaluation <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Its primary value is seen in applications involving multiple LLM calls or complex, multi-step processes <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. LangSmith logs all steps of a chain or agent, including inputs and outputs, providing crucial tracing and debugging capabilities <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Even for single LLM calls, it offers value by allowing users to see templated variables, conversational history, and what enters the LLM <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

LangSmith supports testing across the spectrum, from end-to-end applications to individual components within a system (e.g., a routing step in an assistant) <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. This platform aims to provide the confidence and tools for rapid iteration in LLM development <a class="yt-timestamp" data-t="00:35:44">[00:35:44]</a>.

### Evaluation (Eval) in AI Development

Evaluation is a critical, yet complex, aspect of AI product development. Teams face several challenges:
1.  **Data Set Gathering**: Typically starts with hand-labeling a small set of examples, then incorporating edge cases identified from production data failures (e.g., flagged by user feedback) <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
2.  **Single Data Point Evaluation**: While some cases allow for traditional ML metrics, many require LLMs to act as judges, which, while popular, is not perfect and necessitates a human-in-the-loop component <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
3.  **Metric Aggregation**: How to combine scores and compare different iterations (e.g., comparing to a previous prompt) <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
4.  **Frequency of Evaluation**: Due to cost, time, and error-proneness, evaluations are often conducted before releases <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. The goal is to reduce the manual component to enable running evaluations in continuous integration (CI) <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

Manual review of data is considered underrated, providing deep understanding of system behavior and helping developers [[challenges_in_ai_product_development | grock]] how models work, especially in this early and fast-moving space <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. Creating an evaluation data set forces developers to define what the system should do, including handling edge cases and user interactions <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

While LLMs may become more reliable in the future (e.g., GPT-7), manual evaluation will likely remain somewhat important <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

### The Agent Landscape

The AI agent space has undergone a hype cycle. Initially, there was an explosion of interest in "super generalizable autonomous agents" like AutoGPT and Baby AGI <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. However, the focus has shifted to more "focused agents" that are practically ready for deployment <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.

Multi-agent frameworks like Autogen and Crew AI, while seeming to multiply the complexity, are often better understood as "controlled flows between a specific prompt that maybe has access to some specific tools" <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. LangChain conceptualizes this as a state machine, where agents transition between defined states with controlled probabilities <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. This mental model allows for greater control and reliability, evident in production systems like customer support chatbots with dedicated stages <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. LangChain's recently released **LangGraph** framework specifically supports constructing agents as graphs or state machines <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

## Evolution of AI Applications and Development Practices

The AI application landscape is moving towards more complex systems beyond basic "chat your docs" <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>. Harrison Chase identifies three main categories of builders:
1.  **Super early Gen AI native startups**: Building highly forward-thinking, often consumer-facing agents <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
2.  **Digital native startups**: Initially shipping single LLM calls, now moving to more sophisticated applications like Notion QA's personalized chat over a knowledge base <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
3.  **Larger Enterprises**: Significant internal work, including building internal assistant platforms (e.g., using [[advancements_in_ai_developer_tools | Open GPTs]] for custom chatbots with internal data and APIs) <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. This internal focus allows for greater risk-taking <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.

LangChain provides templates and use-case documentation (e.g., Q&A, SQL extraction) and dedicated use-case repositories like Chat LangChain and Open GPTs to help companies get started <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.

An underutilized part of LangChain is **example selectors**, which leverage few-shot prompting to dynamically select relevant examples for a given query <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. This can significantly improve application performance, especially for structured output or complex instructions, and could be a pathway to "continual learning" and personalization <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.

### [[challenges_in_ai_product_development | Development Philosophy]]

LangChain navigates the rapidly evolving AI space by balancing the need to build "here and now" with maintaining flexibility. Their approach includes:
*   **Building despite change**: Acknowledging that current solutions might be "hacks" but are necessary to build applications today <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>.
*   **Flexible abstractions**: Investing time in lower-level, flexible orchestration layers like LangChain Expression Language (LCEL) and LangGraph, which were not present in earlier versions <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>. LCEL, in particular, was designed with streaming as a first-class citizen <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>.
*   **Simple base classes**: For individual components (retrievers, vector stores, models), opting for very simple base abstractions to avoid making assumptions about implementation details (e.g., retries handled at the individual class level) <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.
*   **Strategic timing for releases**: Consciously waiting for advancements like multimodal models to stabilize before major releases (e.g., LangChain 0.1) to ensure robust abstractions <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>.

The space is characterized as "super early, super fast moving" with immense opportunity <a class="yt-timestamp" data-t="00:34:38">[00:34:38]</a>. The core focus remains on providing the most value to users by addressing the biggest blockers, such as understanding application behavior to iterate with confidence <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.

## LangServe: Deployment for LangChain Applications

LangServe is a new offering designed to be the easiest way to deploy LangChain applications <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>. It wraps around Fast API and other technologies, plugging into common Python stacks <a class="yt-timestamp" data-t="00:37:26">[00:37:26]</a>. LangServe leverages the common orchestration layer of LangChain Expression Language, which defines a consistent input/output schema and `invoke`, `batch`, and `stream` endpoints <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>.

A key feature of LangServe is its ability to quickly spin up a playground for interacting with the deployed application <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>. This facilitates cross-functional collaboration, allowing non-technical people and subject matter experts to test and provide feedback, improving the overall development process <a class="yt-timestamp" data-t="00:38:46">[00:38:46]</a>.

## Future of AI Applications

Looking ahead, Harrison Chase predicts several trends in AI applications:
*   **More complex chatbots**: Evolving into state machine representations with different stages (e.g., customer support bots, [[ai_in_language_learning | AI]] therapists) <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>.
*   **Longer-running jobs**: Applications like GPT-Researcher and GPT-Newsletter that generate first drafts of reports or articles over minutes <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>. This requires finding user experiences where instantaneous responses are not necessary, as multi-LLM calls and self-checking take time <a class="yt-timestamp" data-t="00:42:48">[00:42:48]</a>.
*   **Innovation in UX**: The most interesting work in AI applications lies in user experience design, as how people interact with these systems is still being figured out <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>. An example is an "AI-native spreadsheet" where individual cells are populated by separate agents in parallel, taking seconds rather than being instantaneous <a class="yt-timestamp" data-t="00:43:53">[00:43:53]</a>.

### [[ai_inference_and_compound_ai_systems | Inference Costs]] and Product-Market Fit

For startups, the advice is to focus on building with powerful models like GPT-4 to achieve product-market fit (PMF) first, rather than immediately optimizing for inference costs <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>. Costs and latency are expected to decrease over time. The mantra is "no GPUs before PMF" <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.

### Obviated Techniques

As models improve, some current techniques might become less necessary:
*   **Context window management**: Tricks for summarizing conversational history might diminish as context windows grow, allowing more direct input <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>.
*   **Structured output formatting**: The need to explicitly prompt models to "write this in JSON or poppy" will hopefully disappear with better function calling and structured extraction capabilities <a class="yt-timestamp" data-t="00:48:32">[00:48:32]</a>.

However, retrieval will likely always be needed <a class="yt-timestamp" data-t="00:47:11">[00:47:11]</a>. State machine concepts for agents might persist not only for technical reasons (models not being *that* good, complex instructions, dynamic database access) but also as a helpful mental model for developers <a class="yt-timestamp" data-t="00:47:39">[00:47:39]</a>.

### Overhyped and Underhyped in AI

*   **Overhyped**: Multimodal models, as they are "not quite good enough for a lot of the real use cases that people want" <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>.
*   **Underhyped**: Few-shot prompting, which successful teams are actively using <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

### Personalization in AI

Harrison Chase is particularly excited about personalization in AI, believing it could be the "second wave" of AI applications after initial, less personalized versions <a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>. Companies focusing on high levels of personalization, like New Computer (memory) and Hearth AI (relationship management), are of great interest <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>. A dream application would be a journal app that remembers personal details and past interactions, using them to initiate conversations with the user <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.

### Open Source Models

Open-source models are expected to become more ubiquitous, driven by interest in local models and agents for personalized applications (e.g., chat with a coach, pure knowledge access) where users want data to remain local <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. While not "quite there" yet compared to leading proprietary models, their advancement is anticipated to enable cool desktop applications running locally <a class="yt-timestamp" data-t="00:52:13">[00:52:13]</a>.

Harrison Chase's journey with LangChain has been an interesting experience, building an open-source project from scratch and engaging with a rapidly growing community <a class="yt-timestamp" data-t="00:56:25">[00:56:25]</a>. LangChain continues to invest in documentation and video content to help developers leverage the framework effectively <a class="yt-timestamp" data-t="00:57:13">[00:57:13]</a>.