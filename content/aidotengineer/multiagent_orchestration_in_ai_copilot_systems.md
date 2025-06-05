---
title: Multiagent orchestration in AI copilot systems
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

AI copilot systems for cloud architecture require grounded reasoning rather than mere automation to navigate increasing complexity in cloud systems, tools, constraints, and expectations <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. These systems need to understand, debate, justify, and plan solutions <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Cloud architecture is not just technical but also cognitive, involving constant negotiation of trade-offs based on requirements, time, and available resources <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Capturing the scattered and implicit context architects rely on for decision-making is crucial for AI <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Challenges at the Intersection of AI and Architecture

Key challenges in solving architecture design problems with AI include:
*   **Requirement Understanding** <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>: Identifying the source, format, important pieces, and scope of requirements <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Architecture Identification** <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>: Understanding the functionalities of various components within an architecture <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Architecture Recommendation** <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>: Providing recommendations that match requirements or improve the architecture based on best practices <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

More specific AI-related challenges arise from:
*   **Mixing Semantic and Graph Context** <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>: Requirements are typically textual, while architecture is graph data; effectively integrating these sources for higher-level reasoning is vital <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.
*   **Complex Reasoning Scenarios** <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>: Handling vague, broad, and complex questions that require breakdown and proper planning <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Evaluation and Feedback** <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>: Providing feedback to large AI systems with many moving parts <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## Grounding AI Agents in Specific Context

To enable AI agents to reason effectively, providing proper context about architecture is essential <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
Approaches for grounding agents include:
*   **Semantic Enrichment of Architecture Data** <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>: Collecting relevant semantic information for each component to make it more searchable <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Graph-Enhanced Component Search** <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>: Utilizing graph algorithms to retrieve the correct information from an architecture when searching for components <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Early-Score Enrichment of Requirement Documents** <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>: Scoring documents based on important concepts to facilitate faster retrieval of relevant information <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Learnings from Grounding
*   Semantic grounding improves reasoning but has limitations in scalability and producing detailed responses <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Prompt design is critical for effective soft grounding, guiding the agent on what to focus on and retrieve <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Graph memory supports continuity, allowing agents to connect different nodes in a graph and add context for proper reasoning <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Initial designs using vector DBs for architecture retrieval showed limitations for graph data, leading to a shift towards graph-based searches and knowledge graphs <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Structuring requirements using templates helps with fast retrieval and structuring business needs but can lose context in larger searches <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Addressing Complex Reasoning Scenarios with Multiagent Orchestration

Architecture design involves conflicting goals, trade-offs, and debates <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. AI agents need to collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

Key strategies for managing [[complex_reasoning_scenarios_in_ai|complex reasoning scenarios]] involve:
*   **[[multiagent_systems_in_ai|Multiagent orchestration]] with Role-Specific Agents** <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>: Building a [[multiagent_systems_in_ai|multiagent system]] that allows multiple agents to work together and possess specific properties <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Structured Message Format** <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>: Using structured messages (e.g., beyond XML) to facilitate better workflows and agent interactions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Conversation Management** <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>: Isolating conversations between agents to manage memory, prevent wasted tokens, and avoid "hostination" (a phenomenon where increased memory leads to poorer results) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Cloning of Agents for [[agent_orchestration_and_parallel_processing|parallel processing]]** <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>: Duplicating agents for specific tasks to speed up processes, requiring careful memory management <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Learnings from Complex Reasoning
*   Structured outputs significantly improve clarity and control in programming, despite potential concerns about reducing reasoning abilities <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   [[dynamic_planning_and_execution_in_ai|Dynamic planning and execution in AI]]: [[multiagent_systems_in_ai|Multiagent systems]] should be allowed to resolve trade-offs dynamically rather than executing static plans, leading to higher creativity in planning and results <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   Successful [[agent_orchestration_and_parallel_processing|agent orchestration]] requires control flow; simply letting agents work together without guidance is insufficient <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

## K.O.'s Multi-Agent AI Copilot System

K.O. employs a [[multiagent_systems_in_ai|multiagent system]] for architecture recommendations <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This system generates recommendations categorized by areas like architecture messaging and queuing, API integration, etc., breaking each recommendation into descriptions, target states, gap analysis, and recommended actions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

The system's agents include:
*   **Chief Architect** <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>: Oversees and coordinates higher-level tasks <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **10 Staff Architects** <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>: Each specialized in a domain (e.g., infrastructure, API, IM) <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   **Requirement Retriever** <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>: Accesses requirements data <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.
*   **Architecture Retriever** <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>: Understands the current architecture state and can answer questions about components <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Multi-Agent System Workflow
The [[modus_agent_orchestration_framework|multiagent system]] workflow consists of three main sequential tasks to generate recommendations:
1.  **List Generation** <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>: The Chief Architect requests possible recommendations from Staff Architects <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Staff Architects, in parallel, query the Architecture State Agent and Requirements Agent multiple times <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
2.  **Conflict Resolution** <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>: The Chief Architect reviews the generated list of recommendations for conflicts or redundancies, pruning the list <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  **Design Proposal** <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>: Staff Architects generate full design proposals for each recommendation topic, including gap analysis and proposed improvements <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>. During this step, [[agent_orchestration_and_parallel_processing|cloning of agents]] occurs, with each staff architect cloned for the number of recommendations it needs to generate <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>. Each clone has access to past history but maintains its own separate current history <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.

## Evaluation and Feedback

To determine if a recommendation is good and to monitor the many rounds of conversations within the [[multiagent_systems_in_ai|multiagent system]], a feedback loop with human scoring and structured feedback is necessary <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

### Learnings from Evaluation
*   Human evaluation is the most effective method, especially in early stages of [[developing_ai_agents_and_agentic_workflows|developing AI agents and agentic workflows]] from scratch <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. LLM evaluations are good but often lack the specific insights needed for improvements <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   An internal human evaluation tool (e.g., "Eagle Eye") helps review specific cases, extracted requirements, agent conversations, and generated recommendations for relevance, visibility, and clarity scoring <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   Confidence is not correctness <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   Evaluation must be integrated into system design from the outset, not added later, to ensure continuous assessment as the system evolves <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. Hallucinations can occur in agent interactions, highlighting the importance of monitoring <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Key Takeaways

Building an AI copilot is about designing a system that can reason, not just generate answers or provide assistance <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This involves handling vast amounts of data (thousands to millions of components, large document corpuses) to answer questions from diverse stakeholders <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

Effective [[ai_agents_and_agentic_workflows|AI agents and agentic workflows]] require:
*   Defined roles <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Structured workflows <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Robust memory management <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   Structured outputs <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

Continuous experimentation is vital to identify effective patterns based on existing data <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. Graphs are becoming increasingly important in design, especially for capturing memory and maintaining context for the AI <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. The level of [[multiple_levels_of_ai_agent_autonomy|autonomy]] given to each agent is a key learning area <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. Frameworks like LangGraph are being explored for building agent workflows, often managed by a higher-level system <a class="yt-timestamp" data-t="00:24:59">[00:24:59]</a>.