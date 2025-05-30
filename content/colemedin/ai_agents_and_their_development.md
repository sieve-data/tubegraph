---
title: AI agents and their development
videoId: jSDLMYZAfac
---

From: [[colemedin]] <br/> 

## [[Understanding AI agents | Understanding AI Agents]]
[[Defining AI agents | AI agents]] are defined by their ability to reason about their actions, meaning the number and type of actions they take can differ depending on how they think they need to achieve a goal <a class="yt-timestamp" data-t="01:54:47">[01:54:47]</a>. This behavior is considered "non-deterministic" because the exact outcome of an agent's execution is not always predictable <a class="yt-timestamp" data-t="01:55:03">[01:55:03]</a>. In contrast, "AI workflows" are deterministic, consisting of a fixed sequence of steps that always occur, even if an [[AI agents and large language models | LLM]] is part of that sequence for a specific task <a class="yt-timestamp" data-t="01:55:11">[01:55:11]</a>.

## [[Building AI Agents | Building AI Agents]]
The process of [[Building AI Agents | building AI agents]] can involve various tools and approaches, from no-code solutions to programming frameworks.

### Prototyping with No-Code Tools
No-code tools like N8N are highly powerful for prototyping [[Building AI Agents | AI agents]] and creating internal automations rapidly <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. N8N has significantly advanced no-code, offering capabilities similar to more expensive platforms like Zapier, but with greater power and better agent integration <a class="yt-timestamp" data-t="01:21:36">[01:21:36]</a>. While N8N can be used for production-ready agents, it has limitations in customization, control, and flexibility compared to coding frameworks <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>.

N8N also supports a distributed architecture using "worker nodes" in "Queue mode," enabling it to handle thousands of concurrent user requests for enterprise-level scaling <a class="yt-timestamp" data-t="01:24:23">[01:24:23]</a>.

### Coding with Frameworks
For production-ready [[Building AI Agents | AI agents]], coding offers greater flexibility and control <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>.

*   **Pyantic AI:** This is a preferred framework due to its balance of simplicity in [[Building AI Agents | building agents]] and not over-abstracting underlying processes <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>.
*   **Langraph:** This framework is excellent for implementing multi-agent architectures, allowing the connection of different agents (built with frameworks like Pyantic AI or Crew AI, or even without a framework) into a graph of nodes <a class="yt-timestamp" data-t="01:09:42">[01:09:42]</a>. Langraph enables a global state to be managed, facilitating communication and reasoning loops between agents <a class="yt-timestamp" data-t="01:57:40">[01:57:40]</a>. It is one of the few [[Frameworks and tools for AI agent development | AI agent development frameworks]] that supports TypeScript <a class="yt-timestamp" data-t="01:42:03">[01:42:03]</a>.

### Core Components of [[Building AI Agents | AI Agents]]
When [[Building AI Agents | building AI agents]], key components include:
*   **System Prompts:** Essential for defining an agent's behavior and tone <a class="yt-timestamp" data-t="01:04:50">[01:04:50]</a>.
*   **Tools:** Allow agents to perform specific actions, such as executing code for data analytics <a class="yt-timestamp" data-t="02:29:40">[02:29:40]</a>.
*   **Long-Term Memory:** Frameworks like Mem Zero enable agents to store and retrieve memories, providing context for personalized interactions across different conversations <a class="yt-timestamp" data-t="01:04:16">[01:04:16]</a>.
*   **[[RAG AI agent development | Agentic RAG]]:** This approach gives agents the ability to reason about how to consult a knowledge base, rather than performing a single, static lookup <a class="yt-timestamp" data-t="02:09:54">[02:09:54]</a>.

## [[RAG AI agent development | RAG AI Agent Development]]
[[RAG AI agent development | RAG]] (Retrieval Augmented Generation) is a critical component for [[Building AI Agents | AI agents]] to access and utilize external knowledge bases.

### Challenges with Tabular Data
Traditional [[RAG AI agent development | RAG]] performs poorly with tabular data because its directed lookup often retrieves only partial information, preventing comprehensive analysis of columns (e.g., summing all values) <a class="yt-timestamp" data-t="01:49:31">[01:49:31]</a>. Additionally, [[AI agents and large language models | LLMs]] are not proficient at mathematical computations <a class="yt-timestamp" data-t="01:50:14">[01:50:14]</a>. A solution involves converting tabular files (CSV, Excel) into SQL tables, allowing agents to write SQL queries for data analysis <a class="yt-timestamp" data-t="01:50:25">[01:50:25]</a>. When embedding tables for directed lookups, it's crucial to chunk data in a way that doesn't split rows in half <a class="yt-timestamp" data-t="01:51:16">[01:51:16]</a>.

### Evaluating and Improving [[RAG AI agent development | RAG Agents]]
Evaluating and improving [[RAG AI agent development | RAG agents]] involves using various tools and strategies:
*   **Langfuse:** An open-source tool for tracing and monitoring agent actions, it can also be used for evaluation by setting benchmarks and performing "LLM as a judge" assessments <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.
*   **Ragas:** A powerful library specifically designed for evaluating [[RAG AI agent development | RAG agents]] <a class="yt-timestamp" data-t="01:02:30">[01:02:30]</a>.
*   **Improvement Strategies:** Common improvement areas include refining chunking strategies and implementing advanced [[RAG AI agent development | RAG]] techniques like query expansion or re-ranking, depending on the specific use case <a class="yt-timestamp" data-t="01:02:56">[01:02:56]</a>.

## [[AI agents and large language models | AI Agents and Large Language Models]]
[[AI agents and large language models | LLMs]] are fundamental to [[Building AI Agents | AI agents]], providing their reasoning capabilities.

### Fine-Tuning LLMs
Fine-tuning [[AI agents and large language models | LLMs]] is an advanced method to further establish an agent's behavior and tone beyond system prompts <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>. This involves providing hundreds or thousands of prompt-response examples for the model to learn from <a class="yt-timestamp" data-t="01:27:26">[01:27:26]</a>.

*   **Local Fine-Tuning:** Fine-tuning local [[AI agents and large language models | LLMs]] (e.g., Mistral 3.1 small <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>) is beneficial for data privacy and can be more cost-effective than cloud-based solutions <a class="yt-timestamp" data-t="01:26:45">[01:26:45]</a>.
*   **Distilled Models:** This concept involves using a more powerful [[AI agents and large language models | LLM]] to generate training data for a weaker [[AI agents and large language models | LLM]], allowing the smaller model to improve its performance and mimic the capabilities of the larger one <a class="yt-timestamp" data-t="02:00:53">[02:00:53]</a>.

## [[Frameworks and tools for AI agent development | Frameworks and Tools for AI Agent Development]]
Beyond Pyantic AI and Langraph, other [[Frameworks and tools for AI agent development | frameworks and tools]] were mentioned:

*   **Google ADK (Agent Development Kit):** Appears impressive, particularly for built-in agent monitoring features, but may have been released prematurely and might still be missing some elements <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Google A2A Protocol:** Considered revolutionary for enabling communication between agents by setting them up as API endpoints that can discover each other's capabilities <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. This aims to standardize inter-agent communication, akin to microservices for traditional software architecture <a class="yt-timestamp" data-t="01:56:42">[01:56:42]</a>.
*   **Manis / Open Manis:** Manis initially generated hype but was not revolutionary, with open-source alternatives like Open Manis quickly replicating its functionalities <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Crew AI:** Another framework for multi-agent architectures <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a>.
*   **Llama Index:** More suited for knowledge-focused agents, especially those based on [[RAG AI agent development | RAG]] <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>.
*   **Lightragg:** A knowledge graph implementation that also supports traditional [[RAG AI agent development | RAG]] <a class="yt-timestamp" data-t="01:55:04">[01:55:04]</a>.
*   **Local AI Package:** An open-source solution for self-hosting AI services to ensure data privacy in [[Building AI Agents | AI applications]] <a class="yt-timestamp" data-t="01:08:05">[01:08:05]</a>. This package is continuously updated with features like Langfuse integration for agent observability <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>.
*   **AI IDEs (e.g., Cursor, Windsurf, Lovable):** These tools leverage [[RAG AI agent development | RAG]] under the hood to allow users to chat with their codebase and generate code <a class="yt-timestamp" data-t="01:40:36">[01:40:36]</a>. They are evolving to include specialized chat modes for explaining generated code and helping users understand the codebase <a class="yt-timestamp" data-t="01:32:53">[01:32:53]</a>.
*   **Pipedream:** An open-source platform for integrating APIs, [[AI agents and large language models | AIs]], and databases to develop event-driven automations, appearing similar to N8N but with potentially unique capabilities <a class="yt-timestamp" data-t="00:49:52">[00:49:52]</a>.

## [[AI Agent Development Challenges | AI Agent Development Challenges]]
Several [[AI Agent Development Challenges | challenges]] exist in [[Building AI Agents | AI agent development]]:

*   **Vendor Lock-in:** Many platforms (e.g., Google Agent Space, Salesforce Agent Force, MindPal, Relevance AI) confine [[Building AI Agents | AI agents]] to their ecosystem, limiting integrations and control <a class="yt-timestamp" data-t="01:35:28">[01:35:28]</a>. Open-source tools are generally preferred to avoid this <a class="yt-timestamp" data-t="01:35:54">[01:35:54]</a>.
*   **"Vibe Coding":** Relying solely on [[AI agents and large language models | AI coding assistants]] without understanding the generated code can lead to unmaintainable or insecure applications <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. While [[AI agents and large language models | AI coding assistants]] can speed up development, the developer must still validate the code and handle productionization, maintenance, and refactoring <a class="yt-timestamp" data-t="01:17:59">[01:17:59]</a>.
*   **Enterprise Adoption:** Corporate environments often have strict tool choices and approval processes, making it difficult to implement cutting-edge [[Frameworks and tools for AI agent development | AI agent development tools]] <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>. Using tools aligned with existing corporate infrastructure (e.g., AWS Bedrock if on AWS) is often necessary <a class="yt-timestamp" data-t="01:33:51">[01:33:51]</a>.
*   **Security:** Exposing local instances of tools like N8N to the internet carries security risks, even with built-in authentication, if underlying vulnerabilities exist <a class="yt-timestamp" data-t="01:35:55">[01:35:55]</a>. For high-security needs, entirely local file storage solutions are recommended <a class="yt-timestamp" data-t="01:37:39">[01:37:39]</a>.

## Future of [[AI Agents and Large Language Models | AI Agents]]
The relationship between [[AI agents and large language models | AI agents]] and human expertise is expected to evolve more towards collaboration rather than outright replacement in the next one to two years <a class="yt-timestamp" data-t="01:45:07">[01:45:07]</a>. [[AI agents and large language models | AI agents]] will augment human capabilities, allowing smaller teams to accomplish what previously required larger ones <a class="yt-timestamp" data-t="01:45:47">[01:45:47]</a>. Human roles will remain crucial for understanding requirements, documentation, solution architecture, and providing the necessary human touch in areas where [[AI agents and large language models | AI]] may lack context <a class="yt-timestamp" data-t="01:46:27">[01:46:27]</a>.