---
title: AI production and evaluation techniques
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

## LangChain and LangSmith Overview

LangChain is a popular framework for working with Large Language Models (LLMs) and serves as an orchestration layer for building LLM applications <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It has gained significant traction, with over 38,000 Discord members and adoption by major companies like Elastic, Dropbox, and Snowflake <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. The core idea behind LangChain is to connect LLMs to external data sources and computation <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

LangSmith is a separate SaaS platform developed by LangChain, focusing on [[ai_evaluation_and_benchmarking | observability, testing, and evaluation]] for LLM applications <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. It was developed to address the significant need for teams to transition from prototype to production with confidence <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Core Focus Areas

LangChain and LangSmith primarily focus on three interconnected areas:
*   **Retrieval** <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>
*   **Agents** <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>
*   **Evaluation** <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>

Agents can be used for retrieval, retrieval is a popular tool for agents, and evaluation is crucial for both <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Agents can also be used to perform evaluation <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## LangSmith for Production Applications

LangSmith is particularly valuable for applications involving multiple LLM calls or steps <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Its tracing and observability features log all steps of a chain or agent, including inputs and outputs, which is crucial for understanding and debugging complex systems <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Even for single LLM calls, LangSmith provides value by visualizing templated prompts and conversational history <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

On the testing side, LangSmith supports testing across the entire spectrum, from end-to-end applications to individual components <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

## Current State of Evaluation

The process of [[ai_evaluation_and_benchmarking | evaluating LLM applications]] involves several key questions for teams:

### Data Set Gathering
Teams typically start by hand-labeling 20 or so examples <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. They then incorporate edge cases from production data that cause failures, using systems like "thumbs down" feedback or flagging mechanisms <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. LangSmith connects production traces with evaluation sets, allowing for continuous improvement <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### Single Data Point Evaluation
For simple classification tasks, traditional machine learning techniques can be used <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. However, for more complex scenarios, using [[ai_model_evaluation_and_benchmarking | LLMs to judge]] is emerging as a popular technique, though it's not perfect and still requires a human-in-the-loop component <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Many teams still manually review and score individual data points <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Aggregating Metrics
The approach to aggregating metrics varies, from precise scoring to simply determining if a new prompt performs better than a previous one <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

### Frequency of Evaluation
Evaluation is often done before releases due to its expense and manual components <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. The goal is to reduce manual effort enough to allow for continuous integration (CI) testing, similar to software unit tests <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.

### Value of Manual Review
Despite the desire for automation, manual review of exceptions is where significant value comes from, as it helps teams understand how models behave and what causes unexpected outcomes <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. It provides deeper insight into the system, which is crucial in the early, fast-moving stages of [[ai_models_and_the_product_development_process | AI model development]] <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.

### Best Practices
*   **Look at the data**: This is underrated and provides valuable insights <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.
*   **Come up with an evaluation data set**: This forces teams to define expectations for the system, including edge cases and user interactions, which is a key part of the product-building journey <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. In traditional machine learning, this was a prerequisite for building models, and it remains important for LLMs <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

### Future of Evaluation
While manual review is crucial now, the future of evaluation with advanced models like GPT-7 is uncertain <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. It is currently more important in this early, fast-moving space, but will likely remain somewhat important even as models mature <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.

The generalizability of evaluation across different use cases is a challenge <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. While core components like data gathering and understanding system behavior are general, specific metrics and evaluations are often use-case dependent <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. LangSmith aims for simple, generalizable components while providing scaffolding for common patterns like LLM-as-a-judge <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

## The Agent Landscape

There are generally two types of agents:
*   **Super generalizable autonomous agents** (e.g., AutoGPT, BabyAGI) <a class="yt-timestamp" data-t="00:21:58">[00:21:58]</a>
*   **More focused agents** <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>

Initial hype was around autonomous agents, but more focused agents appear more practical for today's use cases <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>. Multi-agent frameworks (e.g., AutoGen, CrewAI) are gaining traction, but their success lies in controlled flows between specific prompts and tools, rather than fully autonomous general agents <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>. LangChain's LangGraph views agents as state machines, allowing for enforced control over transitions and states, which is proving reliable in production for applications like customer support chatbots <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

## Complex Applications and UX Innovation

There's a noticeable shift towards more complex LLM applications <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

### Categories of Builders
1.  **Super early Gen-native startups**: Building cutting-edge, often consumer-facing agents <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
2.  **Digital native startups**: Initially shipped single LLM calls, but are now moving towards more sophisticated applications like Notion QA <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
3.  **Larger Enterprises**: A significant amount of work is internal, building assistant-like platforms (similar to a private GPT store) hooked up to internal data and APIs <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. These internal applications allow for more risk-taking due to lower exposure <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.

### Application Archetypes for the Future
*   **More complex chatbots**: Moving beyond simple RAG bots to state machine-represented chatbots with different stages (e.g., customer support bots, AI therapists) <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>.
*   **Longer-running jobs**: Applications like GPT researcher or GPT newsletter that generate first drafts of reports or articles over minutes rather than seconds <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>. These require different user experiences (UX) where instantaneous responses are not expected <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.

### UX as a Bottleneck
The most interesting work in [[ai_in_education_and_human_interaction | AI applications]] currently lies in user experience, as it's not yet clear how people want to interact with these new systems <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>. An example of innovative UX is an AI-native spreadsheet that spins up a separate agent for each cell, populating it in parallel <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>.

## Development and Deployment

### LangServe
LangServe was released to simplify the deployment of LangChain applications <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>. It wraps Fast API and leverages LangChain's common orchestration layer (LangChain Expression Language) for consistent input/output schemas and endpoints (invoke, batch, stream) <a class="yt-timestamp" data-t="00:37:24">[00:37:24]</a>. LangServe also provides a playground for interacting with the application, facilitating cross-functional collaboration and feedback from non-technical subject matter experts <a class="yt-timestamp" data-t="00:38:17">[00:38:17]</a>.

### Balancing Fast-Moving Space and Stability
Building in the rapidly evolving AI space requires a balance between delivering current solutions ("you have to build" even if it's a "hack") and maintaining flexibility for future advancements <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>. LangChain has evolved towards more flexible, lower-level abstractions (like LangChain Expression Language and LangGraph) to allow for customization, moving away from rigid, higher-level chains <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. The approach for base class abstractions is simple, avoiding assumptions about specific implementations (e.g., retries handled at individual class level) <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.

Multimodal models were a concern for abstractions, but fortunately, their integration didn't require massive changes <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. LangChain 0.1 was released after multimodal capabilities stabilized, aiming for more solid abstractions <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>. The current focus is on improving documentation and use cases now that the core orchestration layer is more solid <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>.

### Inference Costs
For startups, the advice is to focus on building with powerful models like GPT-4 to achieve product-market fit (PMF) first <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>. Costs and latency are expected to decrease over time <a class="yt-timestamp" data-t="00:45:10">[00:45:10]</a>. A key principle is "no GPUs before PMF" <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>.

## Future Trends and Obviated Techniques

### What might go away
*   **Context window management**: As context windows grow, some tricks for summarizing and managing conversational history might become less necessary <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>.
*   **Manual JSON/Poppy formatting instructions**: Hopefully, more robust function calling and structured extraction capabilities will eliminate the need to explicitly instruct models to output in specific formats <a class="yt-timestamp" data-t="00:48:32">[00:48:32]</a>.

### What might remain
*   **Retrieval**: Will continue to be needed <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>.
*   **State machine approach**: Even with better models, the state machine mental model is helpful for developers in building complex applications, especially where specific instructions or database access depend on the current state <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
*   **Multimodal capabilities**: Current multimodal models are not precise enough for many knowledge work tasks, particularly regarding spatial awareness in extraction <a class="yt-timestamp" data-t="00:46:43">[00:46:43]</a>. Improvements are expected in this area.

## Key Insights and Predictions

*   **Multimodal is currently overhyped**: While promising, it's not yet good enough for many real-world use cases <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>.
*   **Few-shot prompting is underhyped**: Teams having success are often utilizing few-shot examples, especially for structured output or complex instructions <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>. Dynamic selection of relevant examples from a database can enable continual learning and personalization <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   **Importance of streaming**: Essential for modern LLM applications, allowing for continuous output as the model processes information <a class="yt-timestamp" data-t="00:49:44">[00:49:44]</a>.
*   **Open-source models**: Expected to become more ubiquitous, with high interest in local models and agents for personalized applications (e.g., "ask your documents," coach/mentor personas) <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
*   **Personalization**: A crucial "killer app" for AI, where content is tailored to individual users based on their interests and past interactions <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>. Companies like New Computer and Hearth AI are exploring this space <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.
    *   An example of a personalized application would be a journal app that remembers user details and initiates conversations based on journal entries and past memories <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>.
*   **UX innovation**: The most significant area for advancement in AI applications, as designers figure out how users will best interact with these new capabilities <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.
*   **Build despite uncertainty**: In a fast-moving field, it's essential to build and iterate rather than waiting for perfect stability <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>.

### Competitive Landscape
The [[ai_model_selection_and_evaluation_for_businesses | AI space]] is too early for intense competition focus <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>. LLM technology differs from traditional applications due to its non-deterministic nature and reliance on APIs and prompting <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>. While traditional observability companies like DataDog offer LLM products, their value proposition might differ from specialized LLM evaluation platforms that focus on debugging complex chains and providing confidence in iteration <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>. Companies often use both types of tools in conjunction <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>.