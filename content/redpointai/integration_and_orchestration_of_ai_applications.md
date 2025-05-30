---
title: Integration and orchestration of AI applications
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

Integrating and orchestrating AI applications, particularly those involving Large Language Models (LLMs), presents a dynamic landscape of opportunities and challenges. LangChain, a popular framework, plays a significant role in enabling developers to build and deploy these complex systems.

## LangChain's Role in AI Orchestration

LangChain is designed as a framework for building LLM applications, serving as an orchestration layer to facilitate the development of diverse applications <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. Its core function is to connect LLMs to external sources of data and computation <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

Key aspects of LangChain's orchestration include:
*   **Broad Functionality** LangChain supports a wide range of applications due to the general-purpose nature of LLMs <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   **Foundation for Complexity** The framework has evolved to include flexible lower-level components, such as LangChain Expression Language (LCEL) and LangGraph, which allow for greater customization of internals <a class="yt-timestamp" data-t="30:41:00">[30:41:00]</a>.
*   **Key Focus Areas** LangChain's development has primarily centered on retrieval, agents, and evaluation, recognizing their interconnectedness and importance <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>. For instance, agents can be used for retrieval, and retrieval is a common tool for agents <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

## Types of AI Applications and Use Cases

The versatility of LLMs enables a multitude of [[enterprise_applications_for_ai_including_business_intelligence_and_data_extraction | AI applications]]:

*   **Chatbots over Data** The most common application involves building chatbots that can query and interact with a user's specific data <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. This includes features like streaming and retrieval <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Data Extraction** A significant [[enterprise_applications_for_ai_including_business_intelligence_and_data_extraction | enterprise use case]] for LLMs is data extraction <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Assistant-like Applications** These can facilitate natural language queries for databases (e.g., natural language to query sports stats, text to SQL) <a class="yt-timestamp" data-t="04:40:00">[04:40:40]</a>.
*   **Creative Applications** Generating sports commentary or personalizing it for viewers are examples of creative uses of LLMs <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a> <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Internal Operations** Companies like NBA teams use LangChain for internal operations, such as querying organizational data <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. Elastic is an example of a large company successfully deploying an [[enterprise_ai_adoption_and_deployment_models | assistant]] in production <a class="yt-timestamp" data-t="20:53:00">[20:53:00]</a>.
*   **Advanced Chatbots (State Machines)** Looking ahead, more complex chatbots are emerging, represented as state machines that handle different stages, like a customer support bot or an AI therapist <a class="yt-timestamp" data-t="42:00:00">[42:00:00]</a> <a class="yt-timestamp" data-t="23:10:00">[23:10:00]</a>.
*   **Longer-Running Jobs** Applications like GPT researcher and GPT newsletter generate first drafts of reports or articles, taking a minute or two to complete <a class="yt-timestamp" data-t="42:19:00">[42:19:00]</a>. These require different user experiences where instantaneous responses are not necessary <a class="yt-timestamp" data-t="42:48:00">[42:48:00]</a>.
*   **AI-Native Spreadsheets** A novel application involves an AI-native spreadsheet where each cell is populated by a separate agent executing in parallel, demonstrating how many different tasks can run and then be inspected for results <a class="yt-timestamp" data-t="43:50:00">[43:50:00]</a>.

## LangSmith and LangServe: Supporting the AI Development Lifecycle

Beyond the core orchestration framework, LangChain offers platforms to support the entire AI application development lifecycle:

### LangSmith for Observability, Testing, and Evaluation
LangSmith is a SaaS platform crucial for bridging the gap from prototype to production <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

*   **Observability and Tracing** Its primary value lies in tracing and observability, logging every step of a chain or agent with inputs and outputs, which is invaluable for debugging complex multi-step applications <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>. Even for single LLM calls, it helps visualize prompts with multiple variables or conversational history <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.
*   **Testing and Evaluation** LangSmith supports testing end-to-end applications as well as individual components <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
    *   **Data Set Creation** Teams typically start by hand-labeling a small data set, then incorporate production data and failed edge cases <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. LangSmith facilitates pulling failed production traces into the evaluation set <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.
    *   **Evaluation Techniques** While simple cases can use traditional ML metrics, LLMs are increasingly used as judges for more complex scenarios, although human-in-the-loop remains vital due to LLM imperfections <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
    *   **Aggregation and Frequency** Teams must decide how to aggregate metrics and how often to perform evaluations, which can be expensive and slow <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. The goal is to reduce the manual component to enable running evaluations in CI/CD pipelines <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
*   **Generalizability** LangSmith focuses on low-level, important functionalities like data gathering and monitoring, exposed via API and framework-agnostic <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>. It treats the system being scored as a function, making minimal assumptions about its internal structure <a class="yt-timestamp" data-t="18:18:00">[18:18:00]</a>.

### LangServe for Application Deployment
LangServe aims to be the easiest way to deploy LangChain applications <a class="yt-timestamp" data-t="36:47:00">[36:47:00]</a>.

*   **Deployment Framework** It wraps Fast API and other technologies, integrating into common Python stacks <a class="yt-timestamp" data-t="37:24:00">[37:24:00]</a>.
*   **Standardized Interfaces** With LangChain Expression Language, runnables have a common input/output schema with `invoke`, `batch`, and `stream` endpoints, simplifying deployment <a class="yt-timestamp" data-t="37:34:00">[37:37:00]</a>.
*   **Playground for Collaboration** LangServe quickly spins up a playground for interacting with the application, facilitating cross-functional collaboration and feedback from non-technical subject matter experts <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>.

## [[Strategic considerations for AI application developers | Strategic Considerations for AI Application Developers]]

*   **Build First, Optimize Later** Given the rapid pace of AI development, focusing on building applications even with "hacks" is crucial <a class="yt-timestamp" data-t="30:26:00">[30:26:00]</a>. A key piece of advice is "no GPUs before PMF" (product market fit), meaning build with powerful models like GPT-4 first, then worry about optimization <a class="yt-timestamp" data-t="45:42:00">[45:42:00]</a>.
*   **Embrace Human-in-the-Loop** While automation is a goal, directly reviewing data and exceptions (the "manual part" of eval) is invaluable for understanding how models work and identifying unexpected behaviors <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
*   **Prioritize Evaluation Data Sets** Creating an evaluation data set forces developers to think about what the system should do, expected behaviors, and edge cases, which is a crucial part of the product-building journey <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>.
*   **Underrated Techniques** [[Strategic considerations for AI application developers | Few-shot prompting]] and [[strategic_considerations_for_ai_application_developers | example selectors]] are powerful but often underutilized ways to improve application performance, especially for structured output or complex instructions <a class="yt-timestamp" data-t="28:23:00">[28:23:00]</a>. This can also lead to [[strategic_considerations_for_ai_application_developers | continual learning]] and personalization <a class="yt-timestamp" data-t="29:01:00">[29:01:00]</a>.

## [[Challenges and opportunities in AI integration | Challenges and Opportunities in AI Integration]]

The AI landscape is characterized by its early stage and rapid movement <a class="yt-timestamp" data-t="34:30:00">[34:30:00]</a>.

*   **Evolving Models** Models are constantly improving (e.g., context windows increasing), which might obviate some current techniques like conversation history summarization <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a>. However, core elements like retrieval are expected to remain <a class="yt-timestamp" data-t="47:11:00">[47:11:00]</a>.
*   **Multimodality** While highly anticipated, multimodal models are not yet precise enough for detailed knowledge work or spatial awareness in extraction <a class="yt-timestamp" data-t="46:43:00">[46:43:00]</a>.
*   **Agent Landscape** The initial hype around autonomous agents (like AutoGPT) has shifted towards more focused, controlled agents that function more like state machines <a class="yt-timestamp" data-t="22:00:00">[22:00:00]</a> <a class="yt-timestamp" data-t="23:53:00">[23:53:00]</a>. Multi-agent frameworks like Autogen are seen as controlled flows between specific prompts and tools <a class="yt-timestamp" data-t="22:58:00">[22:58:00]</a>.
*   **UX Innovation** The most interesting work currently is in user experience (UX) for AI applications, figuring out how people want to interact with these new systems <a class="yt-timestamp" data-t="43:28:00">[43:28:00]</a>.
*   **[[Challenges in Enterprise AI deployment | Enterprise Adoption]]** Large enterprises are actively building internal AI applications, which allows them to take more risks compared to external, consumer-facing products <a class="yt-timestamp" data-t="26:02:00">[26:02:00]</a>. This includes platforms similar to the GPT store, but hooked into internal data and APIs <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>. Regulated industries, in particular, show hesitation in releasing user-facing AI products too early <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>.
*   **Personalization and Memory** A future wave of AI applications is expected to focus heavily on personalization, tailoring content and interactions to individual users <a class="yt-timestamp" data-t="53:23:00">[53:23:00]</a>. Applications like a journal app that remembers personal details and conversations could leverage this <a class="yt-timestamp" data-t="55:01:00">[55:01:00]</a>. The ability to render personalized content on the fly, as opposed to static information, is a significant opportunity <a class="yt-timestamp" data-t="01:01:24">[01:01:24]</a>.
*   **Open Source Models** Open-source models are expected to become more ubiquitous, particularly for personalized local applications like "ask your documents" or coach/mentor personas, due to user desire for local control <a class="yt-timestamp" data-t="51:58:00">[51:58:00]</a>.