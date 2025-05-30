---
title: Agentic workflows and AI technology
videoId: jSDLMYZAfac
---

From: [[colemedin]] <br/> 

## Understanding AI Agents and Workflows

The landscape of AI technology is rapidly evolving, with a key distinction emerging between AI agents and traditional AI workflows. This distinction lies primarily in their decision-making capabilities <a class="yt-timestamp" data-t="01:54:45">[01:54:45]</a>.

### [[difference_between_ai_agents_and_llm_workflows | AI Agents vs. AI Workflows]]

*   **AI Agents**: These are given the ability to reason about their actions <a class="yt-timestamp" data-t="01:54:47">[01:54:47]</a>. The number and type of actions they take can differ based on how they determine they need to achieve a goal <a class="yt-timestamp" data-t="01:54:55">[01:54:55]</a>. This makes them non-deterministic, meaning the exact outcome isn't always known beforehand <a class="yt-timestamp" data-t="01:55:03">[01:55:03]</a>. [[understanding_ai_agents | Agents]] decide things for themselves <a class="yt-timestamp" data-t="01:55:48">[01:55:48]</a>.
*   **AI Workflows**: These are deterministic, following a predefined, sequential set of steps <a class="yt-timestamp" data-t="01:55:11">[01:55:11]</a>. An AI workflow might include a Large Language Model (LLM) summarizing information as one step, but that step will always occur the same way, every time <a class="yt-timestamp" data-t="01:55:29">[01:55:29]</a>. Workflows are always the same, regardless of input <a class="yt-timestamp" data-t="01:55:50">[01:55:50]</a>.

## [[building_ai_agents | Building AI Agents]]

[[building_ai_agents | Building AI agents]] effectively requires understanding their core components and leveraging appropriate frameworks and tools <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

### Key Components of AI Agents
Common components for [[building_ai_agents | AI agents]] include <a class="yt-timestamp" data-t="02:30:09">[02:30:09]</a>:
*   **System Prompts**: Used to describe to the agent how it should behave and the desired tone <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>.
*   **Tools**: Allow agents to perform specific actions, such as executing code for data analytics <a class="yt-timestamp" data-t="02:33:40">[02:33:40]</a>.
*   **Agentic RAG**: Provides agents with the ability to reason about how to interact with a knowledge base, rather than just performing a single lookup <a class="yt-timestamp" data-t="02:09:53">[02:09:53]</a>. This involves looking up information in a knowledge base and allowing the agent to perform additional actions on top of it <a class="yt-timestamp" data-t="02:10:07">[02:10:07]</a>.
*   **Long-Term Memory**: Essential for personalized agents to remember user context across conversations <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>. Mem Zero is an open-source library that enables agents to store and retrieve memories, segmenting them by user <a class="yt-timestamp" data-t="01:04:19">[01:04:19]</a>.
*   **Fine-tuning**: A more advanced method to establish an agent's behavior and tone by providing hundreds or thousands of examples of prompts and desired responses <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>.

### Frameworks for Agent Development

*   **Pyantic AI**: A preferred framework for [[building_ai_agents | AI agents]] due to its balance between simplicity and control <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. It allows for direct integration with libraries and frameworks <a class="yt-timestamp" data-t="01:11:40">[01:11:40]</a>.
*   **LangGraph**: Ideal for implementing [[examples_of_agentic_workflows_with_langgraph | multi-agent architectures]] <a class="yt-timestamp" data-t="01:0:31">[01:0:31]</a>. It enables connecting different agents in a graph structure with a global state that all agents can use for communication <a class="yt-timestamp" data-t="01:0:50">[01:0:50]</a>. LangGraph supports loops, allowing agents to reason back and forth <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>. It also notably supports TypeScript, unlike most other frameworks <a class="yt-timestamp" data-t="01:42:03">[01:42:03]</a>.
*   **Google's Agent Development Kit (ADK)**: An impressive framework with built-in features for monitoring agents <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. While powerful, it might still require further development <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Llama Index**: More suited for knowledge-focused, RAG-based agents <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **LangChain**: Was foundational when [[understanding_ai_agents | AI agents]] were new, but became complex due to rapid development <a class="yt-timestamp" data-t="01:43:10">[01:43:10]</a>. LangGraph evolved as a more organized and production-ready alternative <a class="yt-timestamp" data-t="01:43:40">[01:43:40]</a>.

### Tools for Building and Prototyping

*   **[[creating_custom_ai_workflows_with_n8n | n8n]]**: A powerful no-code tool ideal for prototyping [[building_ai_agents | AI agents]] quickly and for building internal automations <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. While it offers extensibility via MCP servers, there are limitations in terms of full customization and direct library integration compared to coded solutions <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. [[using_n8n_for_api_workflows_in_ai_agents | n8n]] also supports advanced scaling with worker nodes for handling high concurrent user requests <a class="yt-timestamp" data-t="01:24:23">[01:24:23]</a>.
*   **AI Coding Assistants (e.g., Cursor, Windsurf, Lovable)**: These tools can significantly speed up development by handling the "first 90%" of coding, leaving the last "10%" for human refinement, bug fixing, and productionization <a class="yt-timestamp" data-t="01:18:24">[01:18:24]</a>. They can also aid in learning to code by explaining generated code and concepts <a class="yt-timestamp" data-t="01:31:16">[01:31:16]</a>.
*   **Archon**: An open-source project designed to build agents using other agents <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>. Its current iteration focuses on [[agentic_workflows_and_human_in_the_loop_concept | agentic workflows]] for [[building_ai_agents | building agents]] with frameworks like Pyantic AI, but future plans include evolving it into a more general RAG agent like Context 7, with local execution capabilities <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>.
*   **Context 7**: A powerful, experimental framework that uses a RAG knowledge base for documentation, but it's not fully open source and has potential monetization <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.
*   **Pipedream**: An API aggregator tool that allows integration of APIs, AI, and databases for event-driven automations, similar in function to [[creating_custom_ai_workflows_with_n8n | n8n]] but with potentially different specializations <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.

## Multi-Agent Architectures

To enable [[examples_of_ai_agents_and_workflows | AI agents]] to interact with each other, multi-agent architectures are essential <a class="yt-timestamp" data-t="01:0:31">[01:0:31]</a>.

*   **LangGraph**: The preferred framework for multi-agent implementation <a class="yt-timestamp" data-t="01:0:33">[01:0:33]</a>. It allows for setting up tools to create different agents that can communicate and work together by sharing a global state and passing parts of that state into prompts for subsequent LLMs <a class="yt-timestamp" data-t="01:0:50">[01:0:50]</a>.
*   **Google's A2A Protocol**: A revolutionary protocol that enables communication between agents by setting them up as API endpoints that can discover and learn each other's capabilities <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>. This protocol aims to standardize inter-agent communication, akin to how microservices revolutionized software architecture <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>.

## Practical Considerations for AI Agents

### Data Privacy and Local AI

For private companies and enhanced data privacy, self-hosting and using local AI solutions are crucial <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.
*   The speaker's "local AI package" is an open-source solution designed for private data use <a class="yt-timestamp" data-t="00:49:14">[00:49:14]</a>.
*   Local models like Mistral 3.1 small (24 billion parameters) can be run on powerful GPUs and are suitable for offline operations <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   Fine-tuning locally hosted LLMs offers control over training data and can be more cost-effective than fine-tuning cloud models <a class="yt-timestamp" data-t="01:26:45">[01:26:45]</a>.

### Enterprise Adoption Challenges

*   Corporate environments often have "red tape" and restrictions on tool choice, forcing reliance on established cloud providers like AWS or Azure and their associated AI services (e.g., AWS Bedrock) <a class="yt-timestamp" data-t="01:32:06">[01:32:06]</a>.
*   Despite restrictions, platforms like Google Agent Space and Salesforce Agent Force are important for enterprise adoption because they integrate with existing corporate ecosystems <a class="yt-timestamp" data-t="01:36:17">[01:36:17]</a>.

### Evaluating and Improving RAG Agents

*   **Langfuse**: An open-source LLM engineering platform that aids in tracing (monitoring agent actions and failures) and evaluating agents <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>. It allows setting benchmarks for expected responses and using LLMs as judges to assess retrieval relevance <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
*   **Ragas**: A specific library for evaluating RAG agents <a class="yt-timestamp" data-t="01:02:33">[01:02:33]</a>.
*   **Improvement Strategies**: Often involves adjusting the chunking strategy, implementing [[agentic_workflows_and_human_in_the_loop_concept | agentic RAG]], or building knowledge graphs <a class="yt-timestamp" data-t="01:02:56">[01:02:56]</a>. Techniques like query expansion or re-ranking can also enhance accuracy depending on the use case <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>.

### Handling Tabular Data
Traditional RAG performs poorly with tabular data because it struggles with retrieving all necessary values for calculations and LLMs are not good at mathematical computations <a class="yt-timestamp" data-t="01:49:31">[01:49:31]</a>. A solution involves converting tabular files (CSV, Excel) into SQL tables, allowing agents to write SQL queries for data analysis (e.g., computing sums or averages) <a class="yt-timestamp" data-t="01:50:27">[01:50:27]</a>. If using RAG for directed lookups, chunking should be done by not splitting rows in half <a class="yt-timestamp" data-t="01:51:16">[01:51:16]</a>.

## The Role of Humans in the Loop

The relationship between [[understanding_ai_agents | AI agents]] and human expertise is expected to evolve towards more collaboration rather than direct replacement <a class="yt-timestamp" data-t="01:45:07">[01:45:07]</a>. While AI can augment human capabilities, allowing smaller teams to achieve what previously required larger ones, essential human tasks like understanding stakeholder requirements, architecting solutions, and documenting remain vital <a class="yt-timestamp" data-t="01:45:52">[01:45:52]</a>.

> "When you are a software engineer, you're doing a lot more than coding... You learn about the full process of software engineering, the whole development life cycle and how to architect solutions well and document them well, how to work with stakeholders to figure out requirements, the kind of things that you can synthesize and give to an AI coding assistant to help, but you never want to trust it entirely." <a class="yt-timestamp" data-t="01:17:29">[01:17:29]</a>

## Staying Up-to-Date with AI Technology

Keeping up with new AI technology releases is crucial <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Primary sources include YouTube channels focusing on AI news (e.g., Matthew Berman, Matt Wolf, World of AI, The AI Code King) and curated news sources <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Engaging with the community, such as through emails and comments, also helps in staying informed about new frameworks and LLMs <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.

## Dynamus AI Mastery Community

The Dynamus AI Mastery Community offers resources for those looking to deep dive into [[building_ai_agents | AI agents]] and [[agentic_workflows_and_human_in_the_loop_concept | agentic workflows]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It provides:
*   **AI Agent Mastery Course**: Covers [[building_ai_agents | building AI agents]] from start to finish, including single and [[examples_of_agentic_workflows_with_langgraph | multi-agent workflows]] with LangGraph, Pyantic AI, and [[creating_custom_ai_workflows_with_n8n | n8n]] <a class="yt-timestamp" data-t="01:12:10">[01:12:10]</a>.
*   **Live Events and Workshops**: Practical sessions for [[building_ai_agents | building agents]] in real-time for specific use cases (e.g., GitHub integration, customer support) <a class="yt-timestamp" data-t="02:24:50">[02:24:50]</a>.
*   **Office Hours**: Dedicated time for technical support and project-specific guidance on [[building_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>.
*   **Community Section**: For networking, sharing ideas, and staying updated on new technologies <a class="yt-timestamp" data-t="02:21:07">[02:21:07]</a>.
*   **Templates and Resources**: Downloadable code and resources from the course <a class="yt-timestamp" data-t="02:23:33">[02:23:33]</a>.
*   **Future Courses**: Planned courses include local AI, RAG, and real-world use cases <a class="yt-timestamp" data-t="02:54:51">[02:54:51]</a>.