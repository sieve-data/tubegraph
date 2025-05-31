---
title: Current state and future of AI agent frameworks
videoId: xLtZ2kyoYic
---

From: [[redpointai]] <br/> 

The AI landscape, particularly concerning agent frameworks, is rapidly evolving, driven by the emergence of large language models (LLMs) <a class="yt-timestamp" data-t="03:52:54">[03:52:54]</a>. LangChain, founded by Harrison Chase, has become a prominent framework for working with LLMs, facilitating the creation of AI applications <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Current State of AI Agents

Initially, there was an "explosion of interest" in AI agents, spearheaded by concepts like AutoGPT <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>. However, early autonomous, highly generalizable agents proved to be less practical for immediate use <a class="yt-timestamp" data-t="21:56:00">[21:56:00]</a>. The focus has since shifted towards more focused agents that are "more practically ready today" <a class="yt-timestamp" data-t="22:08:00">[22:08:00]</a>.

Multi-agent frameworks, such as Autogen and Crew AI, have emerged, which are often described as controlled flows between specific prompts and tools <a class="yt-timestamp" data-t="22:58:00">[22:58:00]</a>. This approach treats agents as a "state machine," allowing for more control over transitions and behavior <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>. This state machine mental model helps developers enforce specific transition probabilities and define distinct states, making agents more palatable and reliable for production <a class="yt-timestamp" data-t="23:14:00">[23:14:00]</a>. LangChain's own `LangGraph` framework, for example, allows constructing agents as graphs or state machines <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a>.

## Future of AI Agents and Applications

The [[future_of_ai_agents_in_software_development | future of AI agents in software development]] and [[future_potential_of_autonomous_ai_agents_in_various_fields | future potential of autonomous AI agents in various fields]] is expected to involve:

*   **More Complex Chatbots**: Applications will likely evolve into more complex chatbots that operate as state machines, guiding users through different stages, such as a customer support bot with various debugging phases or an AI therapist <a class="yt-timestamp" data-t="41:55:00">[41:55:00]</a>.
*   **Longer-Running Jobs**: There will be an increase in applications designed for longer-running, non-instantaneous tasks, such as generating a first draft of a research report or a newsletter (e.g., GPT Researcher, GPT Newsletter) <a class="yt-timestamp" data-t="42:19:00">[42:19:00]</a>. These applications require new user experience (UX) designs that accommodate delayed responses <a class="yt-timestamp" data-t="42:48:00">[42:48:00]</a>.
*   **Personalization and Memory**: A significant area of innovation is in personalization and memory for AI applications <a class="yt-timestamp" data-t="53:24:00">[53:24:00]</a>. The goal is to develop applications that remember details about individual users and tailor experiences, potentially through techniques like Retrieval-Augmented Generation (RAG) or fine-tuning <a class="yt-timestamp" data-t="53:51:00">[53:51:00]</a>. An example of a future application could be a journal app that remembers personal details and initiates conversations based on entries and past interactions <a class="yt-timestamp" data-t="55:01:00">[55:01:00]</a>.
*   **Improved Multimodal Capabilities**: While currently considered "overhyped" for precise knowledge work, multimodal models are expected to improve, particularly in areas like spatial awareness for tasks such as extraction from images <a class="yt-timestamp" data-t="46:43:00">[46:46:40]</a>.
*   **Better Structured Extraction**: The need for specific phrasing like "write this in JSON" will hopefully diminish as models become better at structured extraction <a class="yt-timestamp" data-t="48:32:00">[48:32:00]</a>.

Despite advancements, some core techniques are likely to remain. Retrieval, for instance, is expected to continue being essential <a class="yt-timestamp" data-t="46:11:00">[46:11:00]</a>. The state machine model for agents is also seen as a "really helpful mental model" for [[developers_approach_to_ai_models_and_agents | developers approaching AI models and agents]], suggesting it will persist even with more capable models <a class="yt-timestamp" data-t="48:05:00">[48:05:00]</a>.

## LangChain's Role and Evolution

LangChain positions itself as an orchestration layer for building LLM applications, connecting LLMs to external data and computation <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. Its core focus areas include:
*   **Retrieval**: Functionality around chat, streaming, and data retrieval <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Agents**: Frameworks for building agents, moving from general autonomous agents to more focused, controlled state machines <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>.
*   **Evaluation**: Providing tools for testing and evaluating LLM applications <a class="yt-timestamp" data-t="06:59:00">[06:59:00]</a>.

LangChain has developed several products:
*   **LangChain (Open Source)**: The primary framework for building LLM applications <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. It has evolved to include more flexible, lower-level components like LangChain Expression Language and `LangGraph`, which facilitate building complex orchestration layers <a class="yt-timestamp" data-t="30:47:00">[30:47:00]</a>.
*   **LangSmith**: A separate SaaS platform for observability, testing, and evaluation of LLM applications <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. It tracks multiple LLM calls, inputs, and outputs, aiding in debugging complex applications <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **LangGraph**: A framework specifically designed for constructing agents as graphs or state machines, providing more control over agent behavior <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a>.
*   **LangServe**: Launched to simplify the deployment of LangChain applications, wrapping them in a FastAPI backend and providing playgrounds for testing <a class="yt-timestamp" data-t="36:36:00">[36:36:00]</a>. This tool also facilitates cross-functional collaboration by allowing non-technical team members to interact with and provide feedback on applications <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>.
*   **OpenGPTs**: A project by LangChain that recreates the functionality of the GPT store experience in an open-source manner, enabling companies to build internal chatbot platforms connected to their own data and APIs <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>.

A key challenge for LangChain is balancing building for the "here and now" with remaining "nimble and flexible" for future advancements, given the rapid pace of [[the_future_and_current_state_of_ai_agents | AI development]] <a class="yt-timestamp" data-t="30:03:00">[30:03:00]</a>. The organization focuses on providing the most value by investing in areas where users face significant blockers, such as composability and observability <a class="yt-timestamp" data-t="41:01:00">[41:01:00]</a>.

## Evaluation and Testing of AI Agents

Evaluation (eval) is a critical component for ensuring the reliability of LLM applications. Key challenges and practices in eval include:
*   **Data Set Creation**: Teams typically start with hand-labeled examples (around 20), then incorporate edge cases identified from production failures <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. This process forces developers to clarify what the system should do and how it should handle edge cases <a class="yt-timestamp" data-t="14:52:00">[14:52:52]</a>.
*   **LLM as a Judge**: For complex tasks where traditional machine learning classification is difficult, LLMs are increasingly used to judge the quality of responses, though this method is not perfect and still requires human oversight <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
*   **Human-in-the-Loop**: A significant manual component remains in evaluation, especially for understanding why models behave unexpectedly <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>. This manual review offers deeper insights into the system's workings <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>.
*   **Aggregation and Frequency**: Decisions must be made on how to aggregate metrics and how often to perform evaluations, as the process can be expensive and slow <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. The goal is to reduce the manual component to enable more frequent testing, ideally in continuous integration (CI) pipelines <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
*   **Generalizability**: Evaluation tools aim to be low-level, code-first, and framework-agnostic to support diverse use cases <a class="yt-timestamp" data-t="18:04:00">[18:04:00]</a>.

## Advice for Startups Building in AI

For startups, the [[developers_approach_to_ai_models_and_agents | approach to AI models and agents]] and [[future_of_software_development_and_ai | future of software development and AI]] should be pragmatic:
*   **Build Now**: Despite the rapid changes and perceived "hacks" in the space, it's crucial to start building applications immediately <a class="yt-timestamp" data-t="30:20:00">[30:20:00]</a>.
*   **Focus on Product-Market Fit (PMF)**: Prioritize building with powerful models like GPT-4 to achieve PMF, rather than prematurely optimizing for cost or latency <a class="yt-timestamp" data-t="45:22:00">[45:22:00]</a>. The mantra "no GPUs before PMF" emphasizes this <a class="yt-timestamp" data-t="45:42:00">[45:42:00]</a>.
*   **Leverage Few-Shot Prompting**: This technique is currently "underhyped" but powerful for improving application performance, especially for structured output or complex instructions <a class="yt-timestamp" data-t="49:17:00">[49:17:00]</a>.
*   **Embrace Open Source**: [[the_future_of_ai_models_and_open_source_development | Open source models]] are becoming increasingly ubiquitous and will enable personalized, local applications (e.g., desktop apps that run locally) <a class="yt-timestamp" data-t="51:58:00">[51:58:00]</a>.
*   **Innovate on UX**: A major area for innovation is in designing user experiences for AI applications, as how people want to interact with these systems is still being discovered <a class="yt-timestamp" data-t="43:30:00">[43:30:00]</a>. An "AI-native spreadsheet" that spins up agents for each cell is an example of such a novel UX <a class="yt-timestamp" data-t="43:53:00">[43:53:00]</a>.

## Implications of Autonomous AI Agents

The [[implications_of_autonomous_ai_agents | implications of autonomous AI agents]] are far-reaching. While truly autonomous agents are still developing, more controlled, state-machine-based agents are moving into production <a class="yt-timestamp" data-t="23:40:00">[23:40:00]</a>. Industries are increasingly using AI internally, especially larger enterprises, for assistant-like platforms that allow employees to create chatbots with their own data and APIs, often with lower risk than consumer-facing products <a class="yt-timestamp" data-t="26:05:00">[26:05:00]</a>.

The overall [[the_future_and_current_state_of_ai_agents | future and current state of AI agents]] is characterized by rapid change and immense opportunity, with much value yet to be created <a class="yt-timestamp" data-t="34:44:00">[34:44:00]</a>. While the concept of [[future_of_artificial_general_intelligence_agi | AGI]] is often discussed, the immediate focus is on building practical, reliable applications <a class="yt-timestamp" data-t="22:13:00">[22:13:00]</a>. The current period might be more stable than the chaotic "super hectic" phase of previous months, allowing for more focus on improving documentation, use cases, and scaling <a class="yt-timestamp" data-t="33:34:00">[33:34:00]</a>. The development of AI applications, especially in areas like [[future_of_ai_in_vr_and_personal_agents | AI in VR and personal agents]], is analogous to the early days of the iPhone, where killer apps took time to emerge <a class="yt-timestamp" data-t="1:03:00">[1:03:00]</a>.