---
title: Lang chain as a framework for AI development
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

LangChain is a popular framework designed for working with Large Language Models (LLMs) and building various AI applications <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It boasts significant traction with 38,000 Discord members and adoption by companies such as Elastic, Dropbox, and Snowflake <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Evolution and Core Purpose
LangChain began as a framework for building LLM applications, focusing on an orchestration layer to facilitate the creation of complex applications <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. Its broad and horizontal nature mirrors the general-purpose capabilities of LLMs themselves <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The overarching goal of LangChain is to simplify the development of LLM applications <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Key Focus Areas
LangChain primarily focuses on three interconnected areas: retrieval, agents, and evaluation <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. These components are deeply related; for instance, agents can be used for retrieval, retrieval is a common tool for agents, and evaluation is essential for both, with agents even being able to perform evaluation <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## LangSmith: Observability, Testing, and Evaluation
LangSmith is a separate SaaS platform that emerged from the critical need for observability, testing, and evaluation in LLM application development <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. It became generally available after six months of iteration <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

### Observability
LangSmith provides tracing and observability by logging all steps of a chain or agent, including inputs, outputs, and their exact sequence <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This is especially valuable for [[compound_ai_systems_and_their_development | complex applications]] with multiple or uncertain steps, allowing for better understanding and debugging <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. Even for single LLM calls, LangSmith helps visualize templated prompts, conversational history, and trimmed parts <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The value of observability in LangSmith is often evident within seconds of setup <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

### Testing and Evaluation
LangSmith supports testing across the spectrum, from end-to-end applications to individual components <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. This includes testing an assistant's final output or intermediate steps like tool selection <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

#### Current State of Evaluation
The basic premise of evaluation involves testing a system against a dataset <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. Key questions teams grapple with include:
*   **Data Set Creation**: Teams typically start by hand-labeling about 20 examples, then incorporating production data and edge cases that cause failures <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. LangSmith connects production traces that fail (marked by thumbs down or flags) into the evaluation set <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Single Data Point Evaluation**: For simple classification, traditional ML tricks work <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. However, for more complex scenarios, using LLMs as judges is emerging, though this requires a human-in-the-loop component due to imperfections <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Metric Aggregation**: Teams decide whether to aim for perfectly scored results or simply compare improvements against previous prompts <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **Evaluation Frequency**: Due to cost, slowness, and error-proneness, evaluations are often conducted before releases <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. The goal is to reduce the manual component to enable continuous integration (CI)-like execution <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

#### Best Practices in Evaluation
Looking at data and developing an evaluation dataset is highly valuable <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This process forces developers to clarify what the system should do, how it should handle edge cases, and how users are expected to interact with it <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. Unlike traditional ML, where data preparation precedes model building, LLMs allow for quick starts, but defining clear expectations through an evaluation set remains crucial <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Observing unexpected model behavior during manual review is essential for understanding how these models work <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

LangChain aims to provide generalizable and simple components for evaluation, focusing on data gathering and understanding system behavior <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. While the ideal of fully automated LLM self-evaluation is a future goal, human involvement remains vital for gaining deeper system understanding in this early, fast-moving space <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

## The Agent Landscape
Initially, there was an explosion of interest in generalized autonomous agents like AutoGPT <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>. However, the focus has shifted towards more specific agents, emphasizing practical readiness <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.

### Multi-Agent Frameworks and State Machines
The emergence of multi-agent frameworks like AutoGen and CrewAI, initially met with skepticism, is rooted in the concept of controlled flows <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. LangChain views agents as state machines, allowing for controlled transitions between specific prompts and tools <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>. This mental model enables enforcing specific transition probabilities and defining states, which is beneficial for production systems, such as customer support chatbots with distinct stages <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. LangGraph is a recent LangChain release that allows constructing agents as graphs or state machines <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>.

## LangServe: Simplifying Deployment
LangServe is designed to be the easiest way to deploy LangChain applications <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>. It wraps around Fast API and other technologies, integrating into common Python stacks <a class="yt-timestamp" data-t="00:37:24">[00:37:24]</a>. The decision to release LangServe came after prioritizing observability and testing (LangSmith) due to their immediate pain points for developers <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

LangServe benefits from the common orchestration layer and interfaces provided by LangChain Expression Language and LangGraph, enabling consistent input/output schemas and `invoke`, `batch`, and `stream` endpoints <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. A notable feature is the quick spin-up of a playground for interacting with the application, facilitating cross-functional collaboration and feedback from non-technical stakeholders <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

## Development Philosophy
The AI space moves incredibly fast <a class="yt-timestamp" data-t="00:34:29">[00:34:29]</a>. LangChain's development balances building for current needs while remaining flexible for future advances <a class="yt-timestamp" data-t="00:30:03">[00:30:03]</a>.

### Abstraction Layers and Flexibility
Initially, LangChain's orchestration layer relied on higher-level chains that were less customizable <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>. Recognizing the need for customization, LangChain introduced more flexible, lower-level components like LangChain Expression Language and LangGraph, which allow for greater control over the internal workings of chains <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. Abstractions for individual components (e.g., retrievers, vector stores, models) are designed to be dead simple base classes, opting for simplicity over making assumptions about specific implementations (e.g., retries) <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.

### Iteration and Stability
LangChain released version 0.1 in early January, consciously waiting for multimodal capabilities to emerge to avoid disruptive abstraction changes <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>. The team believes the abstractions are now more solid <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. While there are plans for future versions, the current focus is on improving existing features, documentation, and use cases, as the environment is perceived as more stable than previous periods <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

### Resource Allocation
LangChain's team of 18 people is split roughly 50/50 between LangSmith and other initiatives, primarily existing open-source projects, with some efforts on new exploratory areas like LangGraph and OpenGPTs <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>. Resource allocation is driven by where the company can provide the most value to users <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>.

## Future Outlook and Trends
### Application Archetypes
Harrison Chase predicts that the coming year will see more complex chatbots, often structured as state machines with different stages (e.g., customer support bots, AI therapists) <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>. There will also likely be more longer-running jobs, such as GPT researcher or GPT newsletter, which generate first drafts of reports or articles over minutes <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>. These require different UX considerations, as instant responses are not expected <a class="yt-timestamp" data-t="00:42:48">[00:42:48]</a>.

### UX Innovation
The most interesting work in AI applications currently lies in user experience (UX) <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>. Innovation is needed to figure out how people want to interact with these new capabilities <a class="yt-timestamp" data-t="00:43:35">[00:43:35]</a>. An example is an "AI native spreadsheet" where a separate agent is spun up to populate each cell, allowing for parallel execution of many tasks that take a few seconds to complete <a class="yt-timestamp" data-t="00:43:50">[00:44:14]</a>.

### Inference Costs
For startups, the advice is to focus on achieving product-market fit (PMF) with powerful models like GPT-4, as costs and latency are expected to decrease over time <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>. The mantra "no GPUs before PMF" applies <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.

### Obviated Techniques
As models improve, some current techniques may become less necessary <a class="yt-timestamp" data-t="00:45:58">[00:45:58]</a>. Context window improvements may reduce the need for complex conversation history management and summarization <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. However, retrieval is expected to remain important <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>. While models might eventually recognize states automatically, the state machine mental model for developers is so helpful that the approach will likely persist <a class="yt-timestamp" data-t="00:47:21">[00:47:21]</a>. Better function calling and structured extraction should eliminate the need for explicit JSON formatting prompts <a class="yt-timestamp" data-t="00:48:32">[00:48:32]</a>. Multimodal models are currently overhyped, as they are not yet precise enough for complex knowledge work or fine-grained spatial awareness <a class="yt-timestamp" data-t="00:46:43">[00:46:43]</a>.

### Personalization
A significant missing piece for AI applications to truly take off is user-level personalization <a class="yt-timestamp" data-t="00:53:44">[00:53:44]</a>. This could manifest as content tailored to individual user interests, similar to a dynamic Wikipedia page that adapts to the viewer <a class="yt-timestamp" data-t="01:00:52">[01:01:27]</a>. An example of a future personalized application could be a journal app that remembers user details and prompts conversations based on past entries and interactions <a class="yt-timestamp" data-t="00:55:01">[00:56:02]</a>. This high level of personalization, whether through RAG or fine-tuning, presents a complex yet highly interesting challenge <a class="yt-timestamp" data-t="00:54:22">[00:54:27]</a>.

### Open Source Models
Open-source models are expected to become more ubiquitous <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>. While proprietary models currently dominate for advanced tasks, there is strong interest in local models and agents for personalized applications (e.g., chat with documents, coaches, mentors) that users prefer to keep private and local <a class="yt-timestamp" data-t="00:52:03">[00:52:33]</a>.

## Learning More
For more information about LangChain, individuals can visit the blog at blog.langchain.dev, follow their Twitter, or explore their YouTube channel, which offers series on RAG concepts and building applications from scratch <a class="yt-timestamp" data-t="00:57:05">[00:57:33]</a>. They also encourage checking out LangSmith GA for its tracing and observability features <a class="yt-timestamp" data-t="00:57:42">[00:58:00]</a>.