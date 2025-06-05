---
title: Grounded reasoning systems in cloud architecture
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Immani, co-founding head of AI at Cat.io, discusses grounded reasoning systems for cloud architecture and their application in building an AI copilot at K.O. <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

## Why Reasoning is Essential for Cloud Architecture
Cloud architecture increasingly requires [[role_of_reasoning_models_in_application_development | reasoning]] beyond mere automation due to growing complexity <a class="yt-timestamp" data-t="00:20:00">[00:00:20]</a>. This complexity stems from:
*   Increasing numbers of users and developers <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   A rise in tools, constraints, and expectations <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   Existing synergistic tools not scaling to the diverse decisions needed for cloud architecture <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.

Systems are needed that can understand, debate, justify, and plan to solve these problems, which goes beyond simple automation <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. The [[ai_application_frameworks_and_architecture | architecture stack]] is not just technical but also cognitive, involving architects constantly negotiating tradeoffs based on requirements, time, and resources <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. Capturing this for AI requires understanding how architects think <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

## Challenges at the Intersection of AI and Architecture Design
Cat.io addresses three primary challenges in solving architecture design problems with AI:
1.  **Requirement Understanding** <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>: Identifying the source, format, important pieces, and scope (global or specific) of requirements <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
2.  **Architecture Identification** <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>: Understanding the functions of various components within an architecture based on their type and location <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
3.  **Architecture Recommendation** <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>: Providing recommendations to match requirements or improve the architecture to meet best practices, based on current requirements and architecture state <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

These challenges translate into specific AI-related problems:
*   **Mixing Semantic and Graph Context**: Requirements are often textual, while architecture is inherently graph data. Connecting these disparate data sources for higher-level [[role_of_reasoning_models_in_application_development | reasoning]] is crucial <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.
*   **Complex Reasoning Scenarios**: Handling vague, broad, and complex questions that need to be broken down and planned properly <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Evaluation and Feedback**: How to effectively evaluate and provide feedback to a large AI system with many moving parts <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## Grounding Agents in Specific Context
LLMs require proper context for effective architecture [[role_of_reasoning_models_in_application_development | reasoning]] <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. Translating natural language into meaningful architecture retrieval tasks is difficult, especially when speed is required <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

### Strategies for Context Grounding
1.  **Semantic Enrichment of Architecture Data**: Collecting relevant semantic information for each component to make it more searchable and findable in vector search <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
2.  **Graph-Enhanced Component Search**: Utilizing graph algorithms to retrieve the right information pieces from an architecture when searching for components <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
3.  **Early Score Enrichment of Requirement Documents**: Scoring documents based on important concepts within requirements for faster retrieval, particularly for large text corpora <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

### Learnings from Context Grounding
*   Semantic grounding improves [[role_of_reasoning_models_in_application_development | reasoning]] but has limitations, especially with graph data, leading to a shift towards graph-based searches and knowledge graphs <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   Proper design is critical for soft grounding, guiding the agent on what to focus on and retrieve <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.
*   Graph memory supports continuity, enabling the system to connect different nodes and add context for subsequent [[role_of_reasoning_models_in_application_development | reasoning]] steps <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   Structured requirement templates helped organize extracted information for downstream tasks, but context can be lost with increasing document numbers <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.

## Complex Reasoning Scenarios with Multi-Agent Orchestration
Good design involves conflicting goals, tradeoffs, and debates, necessitating agents that can collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.

### Strategies for Complex Reasoning
1.  **Multi-Agent Orchestration with Role-Specific Agents**: Building a system where multiple agents work together with specific properties <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
2.  **Structured Message Format**: Using structured messages, which significantly improves workflows and enables multiple agents to work together in longer chains <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
3.  **Isolated Conversation Management**: Ensuring conversations between agents are isolated to optimize token usage and prevent increased hallucination observed with larger memories <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
4.  **Cloning Agents for Parallel Processing**: Duplicating agents for specific tasks to speed up processes, requiring careful memory management at the cloning point <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

### Learnings from Complex Reasoning
*   Structured outputs are crucial for clarity and control, despite potential trade-offs with the model's [[role_of_reasoning_models_in_application_development | reasoning]] abilities <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.
*   Agents should dynamically resolve tradeoffs, not just execute static plans, fostering higher creativity in planning and results <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.
*   Successful multi-agent orchestration requires control flows; agents cannot simply work together hoping for the best outcome <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

### Cat.io's Multi-Agent System Architecture
The production stack uses a multi-agent system for recommendations <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>. Recommendations are categorized (e.g., architecture messaging, API integration) and broken down into descriptions, target states, gap analysis (showing what requirements were and what wasn't found in the architecture), and recommended actions <a class="yt-timestamp" data-t="14:31:00">[14:31:00]</a>.

The system comprises:
*   **Chief Architect**: Oversees and coordinates higher-level tasks <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.
*   **Ten Staff Architects**: Each specialized in a domain (e.g., infrastructure, API, IM) <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.
*   **Requirement Retriever**: Accesses requirements data <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.
*   **Architecture Retriever**: Understands the current architecture state and can answer questions about components <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>.

#### Multi-Agent Workflow
1.  **List Generation**: Staff architects request information from architecture state and requirements agents in parallel, generating a list of possible recommendations for the Chief Architect <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
2.  **Conflict Resolution**: The Chief Architect prunes the list by identifying and resolving conflicts or redundancies among the generated recommendations <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.
3.  **Design Proposal**: Cloned staff architects (each clone having access to past history and a separated current history) generate full design proposals for each recommendation topic, detailing gap analysis and improvement proposals <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>.

## Evaluation and Feedback
Determining if a recommendation is good in a multi-agent system with many interacting engines is challenging <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>.

### Evaluation Strategies
*   **Human Evaluation**: At the current stage, human evaluation is considered the most effective for making necessary improvements, as LLM evaluations often fall short <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.
*   **Internal Human Eval Tool ("Eagle Eye")**: This tool allows looking at specific cases, extracted architecture and requirements, agent conversations, and generated recommendations to perform relevance, visibility, and clarity studies, and assign scores <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>.

### Learnings from Evaluation
*   Confidence does not equate to correctness <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>.
*   Human feedback is essential early in building such systems from scratch <a class="yt-timestamp" data-t="20:49:00">[20:49:00]</a>.
*   Evaluation must be "baked into" system design from the start, rather than added later <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>. This includes planning for human eval tools, monitoring dashboards, or LLM-based feedback loops <a class="yt-timestamp" data-t="21:28:00">[21:21:28]</a>.

## Key Learnings and Future Directions
Building an AI copilot is about [[role_of_reasoning_models_in_application_development | designing a system that can reason]], not just generate answers <a class="yt-timestamp" data-t="23:06:00">[23:06:00]</a>. This system needs a comprehensive view of large amounts of data, such as thousands or millions of architecture components and numerous documents, to answer varied questions from diverse stakeholders <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>.

To achieve this, it requires:
*   Defined roles <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>.
*   Structured workflows <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>.
*   Effective memory management <a class="yt-timestamp" data-t="24:06:00">[24:06:00]</a>.
*   Clear structure <a class="yt-timestamp" data-t="24:06:00">[24:06:00]</a>.

Experimentation is key, with certain patterns (like graphs) proving more effective based on existing data <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>. The type of agent interactions and level of agent autonomy are also important considerations <a class="yt-timestamp" data-t="24:39:00">[24:39:00]</a>.

Cat.io is exploring [[ai_application_frameworks_and_architecture | AI application frameworks]] like LangGraph for agent workflows, with a manager layer on top, and using Slite for higher-level management <a class="yt-timestamp" data-t="24:56:00">[24:56:00]</a>. Graphs are increasingly used to capture memory, ensuring AI always has the right context per task <a class="yt-timestamp" data-t="25:34:00">[25:34:00]</a>.

This approach signifies a shift in how [[future_directions_for_software_architecture_using_ai | AI will design software]] <a class="yt-timestamp" data-t="25:50:00">[25:50:00]</a>.