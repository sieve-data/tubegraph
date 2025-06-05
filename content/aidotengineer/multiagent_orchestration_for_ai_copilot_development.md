---
title: Multiagent orchestration for AI copilot development
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Immani, Co-founding Head of AI at Cat.io, discusses the development of an AI copilot using multi-agent orchestration for grounded reasoning systems in cloud architecture <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Cloud architecture requires reasoning, not just automation, due to its increasing complexity driven by users, developers, tools, constraints, and rising expectations <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Traditional synergistic tools struggle to scale with the diversity of decisions needed in cloud architecture <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Systems are needed that can understand, debate, justify, and plan to solve these complex problems, which goes beyond simple automation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The architecture stack is both technical and cognitive <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Architects constantly negotiate trade-offs based on requirement definition, available time, and resources <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. They rely on scattered and implicit context for decisions, and capturing this for AI requires understanding how architects think <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Challenges in AI-Driven Architecture Design

Cat.io identifies three high-level challenges when AI meets architecture design:
*   **Requirement Understanding**: Determining the origin, format, importance, and scope (global or specific) of requirements from textual documents <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Architecture Identification**: Understanding the functionality of various architectural components and their roles based on their context within the architecture <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Architecture Recommendation**: Generating recommendations that match requirements or improve the architecture to align with best practices, based on current architecture state and understood requirements <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

These problems translate into specific AI challenges:
*   **Mixing Semantic and Graph Context**: Combining textual requirements with inherently graph-based architecture data to enable higher-level reasoning <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Complex Reasoning Scenarios**: Breaking down vague, broad, or complex questions into manageable parts and planning their resolution <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Evaluation and Feedback**: Assessing and providing feedback to large [[components_of_ai_agents | AI systems]] with many moving parts <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Grounding AI Agents in Specific Context

For [[developing_and_optimizing_ai_agents | AI agents]] to reason effectively, they need proper context about architecture <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Translating natural language into meaningful architecture retrieval tasks quickly is difficult <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### Architecture Retrieval
Approaches for architecture retrieval include:
*   **Semantic Enrichment**: Collecting relevant semantic information for each architecture component to make it more searchable and findable in vector search <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Graph-Enhanced Component Search**: Utilizing graph algorithms to retrieve the correct information pieces when searching for specific components or types of components within an architecture <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

An early design for architecture retrieval involved breaking down JSON architecture data into natural language, enriching it with connection data, embedding it, and storing it in a vector database for search <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. While this showed good results, semantic search proved limited for graph data, leading to a shift towards graph-based searches and knowledge graphs <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Requirement Retrieval
For requirements, early score enrichment of documents was used for faster retrieval <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This involved identifying important concepts within a large organization's requirements, scoring documents based on these concepts, and thereby speeding up retrieval tasks <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

An initial design for requirement understanding involved taking documents, pre-processing, splitting, and embedding them <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. An extra step included using requirement templates with specific structures to extract relevant information, which was called "pods" <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This helped with fast retrieval and structuring business requirements for agents <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

### Key Learnings
*   **Semantic grounding** improves reasoning but has limitations and does not always scale well or provide sufficiently detailed responses <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Prompt design** is critical for soft grounding, specifically in guiding the agent on what to focus on and retrieve <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   **Graph memory** supports continuity, not just accuracy, by allowing agents to find and connect different nodes in a graph, providing more context for reasoning <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   However, limitations appeared when increasing the number of requirement documents, leading to loss of context in larger searches, suggesting a potential role for graph analysis here too <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Complex Reasoning Scenarios with Multi-Agent Orchestration

Good architecture design involves conflicting goals, trade-offs, and debates <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. [[role_of_ai_agents_in_planning_and_executing_tasks | AI agents]] need to collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

Cat.io's approach involves building a [[agent_frameworks_and_orchestration_layers_in_ai_engineering | multi-agent orchestration]] system with role-specific agents <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Structured Message Format**: Initially involved XMLs, now using structured messages which greatly improve workflow and enable multiple agents to work together in longer chains <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Conversation Management**: Agent conversations are isolated to save tokens and prevent increased hallucination observed with larger memory <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Cloning of Agents**: For parallel processing of certain tasks, agents are cloned, requiring memory management to duplicate relevant history while keeping new history separate <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Key Learnings
*   **Structured outputs** are crucial for improving clarity and control, and for better programming, despite potential concerns about reducing reasoning abilities <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   Allowing agents to dynamically resolve trade-offs rather than executing static plans leads to higher creativity in planning and reaching results <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   Successful [[agent_frameworks_and_orchestration_layers_in_ai_engineering | multi-agent orchestration]] absolutely requires **control flow**; simply letting agents interact freely is insufficient <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### AI Copilot System Example
Cat.io's production system generates recommendations based on a [[agent_frameworks_and_orchestration_layers_in_ai_engineering | multi-agent orchestration]] system <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Recommendations are categorized (e.g., architecture, messaging, API integration) and broken down into description, target state, gap analysis, and recommended actions <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.

The system consists of:
*   **Chief Architect**: Oversees and coordinates higher-level tasks <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **Staff Architects**: Ten specialized agents, each in a specific domain (e.g., infrastructure, API, IM) <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Retrievers**:
    *   **Requirement Retriever**: Accesses requirements data <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
    *   **Architecture Retriever**: Understands the current architecture state and can answer questions about components <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

### Multi-Agent Workflow
The workflow for generating recommendations involves three main sequential tasks <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>:
1.  **List Generation**: The Chief Architect requests recommendations from Staff Architects. Staff Architects parallelly reach out to the Architecture State Agent and Requirements Agent multiple times based on budgets <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Tens of calls can happen concurrently among multiple Staff Architects <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
2.  **Conflict Resolution**: The Chief Architect reviews the generated list of recommendations to identify and prune conflicts or redundancies <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
3.  **Design Proposal**: After conflict resolution, Staff Architects are tasked with writing full design proposals for each recommendation topic, including gap analysis and proposed architecture improvements <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. During this step, each Staff Architect is cloned for each recommendation it needs to generate. Each clone has access to past history but maintains its own separate current history, allowing the agent to leverage existing knowledge for optimal design proposals <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Evaluation and Feedback

A significant challenge is determining the quality of a recommendation in a complex [[agent_frameworks_and_orchestration_layers_in_ai_engineering | multi-agent system]] with numerous conversation rounds <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Human Evaluation**: The best form of evaluation, especially in early stages <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>. LLM evaluations are useful but often don't provide the depth needed for system improvements <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   **Internal Human Eval Tool (Eagle Eye)**: Built to allow examination of specific cases, including architecture, extracted requirements, agent conversations, and generated recommendations <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. This tool facilitates relevance, visibility, and clarity studies, helping make decisions on future focus areas <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.

### Key Learnings
*   **Confidence is not correctness**: An agent's confidence doesn't guarantee accuracy <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   **Human feedback is essential early on**: Especially when building systems from scratch <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   **Evaluation must be baked into system design**: Rather than being an afterthought, evaluation mechanisms (human eval tools, monitoring dashboards, LLM-based feedback loops) should be considered from the initial design phase of any new [[integration of AI agents into existing infrastructure | AI system]] <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Hallucinations** can be detected and managed through careful monitoring of agent conversations and structured outputs <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Conclusion

Building an AI copilot is about designing a system that can reason, not just generate answers or provide assistance <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>. This involves handling large amounts of data, such as thousands or millions of architectural components and numerous documents, to answer varied questions from diverse stakeholders <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

Developing such a [[techniques and patterns in AI orchestration and prompt engineering | reasoning system]] requires:
*   Clearly defined **roles** for agents <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Robust **workflows** <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Effective **memory** management <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   Structured interactions <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

Extensive experimentation is needed to find patterns that work best with existing data, with graphs becoming increasingly important in design <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. Experimentation also guides the nature of inter-agent interactions and the level of autonomy granted to each agent <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>.

Cat.io has experimented with various [[agent_frameworks_and_orchestration_layers_in_ai_engineering | frameworks for building multi-agents]], settling on LangGraph for agent workflows, with a manager layer on top, and Slang for higher-level management <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>. Graphs are used to capture as much memory as possible, ensuring the AI always has the correct context per task <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. The belief is that this approach represents the future of AI in software design <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.