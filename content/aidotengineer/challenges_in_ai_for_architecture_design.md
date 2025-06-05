---
title: Challenges in AI for architecture design
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Designing cloud architecture involves significant cognitive processes beyond mere technical assembly, as architects continuously negotiate trade-offs based on requirements, time, and available resources <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. This reliance on scattered and implicit context makes it challenging to capture for AI systems, requiring an understanding of how architects think <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Cat.io is developing grounded reasoning systems using multi-agent orchestration to build an AI copilot that addresses these [[challenges_in_ai_development | challenges in AI development]] for cloud architecture <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

## Why Reasoning is Essential for Cloud Architecture
Cloud systems are increasing in complexity due to factors like growing user and developer bases, as well as an escalation in tools, constraints, and expectations <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Current simplistic automation tools cannot scale to the diversity of decisions required for cloud architecture <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. There is a need for systems that can understand, debate, justify, and plan to solve these complex problems, which requires reasoning rather than just automation <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Key [[challenges_in_ai_development | Challenges in AI Development]] for Architecture Design
At a high level, Cat.io identifies three primary [[challenges_in_ai_development | challenges in AI development]] when applying AI to architecture design:
*   **Requirement Understanding**: AI needs to understand the origin, format, importance, and scope (global vs. specific) of requirements <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   **Architecture Identification**: AI must comprehend how an architecture works by identifying different components and their varied functions based on their context <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   **Architecture Recommendation**: The system needs to provide recommendations that align with requirements or improve the architecture to match best practices, integrating understanding of requirements and current architecture state <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Specific AI-Related [[technical_challenges_in_ai_agent_development | Technical Challenges]]
Translating these high-level problems into specific AI challenges reveals further complexities:
*   **Semantic and Graph Context**: Architecture design involves a mix of textual requirements (semantic context) and inherently graph-based architecture data. A key [[challenges_in_building_ai_applications | challenge in building AI applications]] is making these two different data sources integrate to enable higher-level reasoning <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Complex Reasoning Scenarios**: Questions posed to the system can be vague, broad, or highly complex, requiring breakdown into parts and proper planning to derive accurate answers <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Evaluation and Feedback**: A significant [[challenges_and_strategies_in_ai_production | challenge in AI production]] is evaluating and providing feedback to a large AI system with many moving parts <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## Addressing Challenges
### Grounding AI Agents in Specific Context
Effective reasoning by AI agents requires proper context about architecture <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>. Translating natural language into meaningful architecture retrieval tasks is not straightforward, especially when fast responses are needed <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.

Strategies implemented include:
*   **Semantic Enrichment of Architecture Data**: Collecting relevant semantic information for each component to make it more searchable and findable in vector search <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
*   **Graph-Enhanced Component Search**: Utilizing graph algorithms to retrieve the right pieces of information from an architecture when searching for components <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **Early Score Enrichment of Requirement Documents**: Scoring documents based on important concepts to enable faster retrieval from large corpora of text <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

Learnings in this area:
*   Semantic grounding improves reasoning but has limitations and doesn't always scale <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   "Soft grounding" design is critical, guiding the agent on what to focus on and retrieve <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>.
*   Graph memory supports continuity by connecting nodes and adding context for proper reasoning in subsequent steps <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
*   Initial designs using vector databases for architecture retrieval showed good results but highlighted that semantic search isn't ideal for graph data, leading to a shift towards graph-based searches and knowledge graphs <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.
*   For requirements, structured templates helped in extracting relevant information for fast retrieval, but context loss was observed when dealing with a larger number of documents, suggesting the potential for graph analysis here as well <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.

### Complex Reasoning Scenarios
Good design involves conflicting goals, trade-offs, and debates <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. [[Challenges in AI agent development | AI agent development]] must create agents that can collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>.

Solutions employed:
*   **Multi-Agent Orchestration**: Building a system with role-specific agents that can work together <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>.
*   **Structured Message Format**: Using structured messages (e.g., instead of XML) to build better workflows and enable multiple agents to work together in longer chains <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>.
*   **Conversation Management**: Isolating conversations between agents to avoid token waste and prevent increased hallucination observed with larger memories <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.
*   **Cloning Agents**: Cloning agents for parallel processing on certain tasks, which speeds up processes and requires careful memory management <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

Learnings regarding complex reasoning and multi-agent systems:
*   Structured outputs improve clarity and control, which is crucial for better programming, despite potential trade-offs in reasoning abilities <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.
*   Agents resolving trade-offs dynamically, rather than executing static plans, leads to higher creativity in planning and reaching results <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
*   Successful multi-agent orchestration necessitates control flows; agents cannot simply work together hoping for the best outcome <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

Cat.io's production stack utilizes a multi-agent system for recommendations, featuring:
*   A **Chief Architect** overseeing higher-level tasks and coordination <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.
*   Ten **Staff Architects**, each specialized in a specific domain (e.g., infrastructure, API, IM) <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.
*   Two **Retrievers**: a **Requirement Retriever** with access to requirements data, and an **Architecture Retriever** understanding the current architecture state <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

The workflow involves three main tasks in sequence:
1.  **List Generation**: Staff architects, in parallel, query the retriever agents for information and generate a list of possible recommendations, which is returned to the Chief Architect <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
2.  **Conflict Resolution**: The Chief Architect reviews the generated list for conflicts or redundancies and prunes it <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.
3.  **Design Proposal**: Cloned staff architects, each with access to past history but generating separate current histories, write full design proposals for each recommendation topic, including gap analysis and proposed actions <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

### Evaluation and Feedback
A critical [[challenges_and_solutions_in_building_ai_agents | challenge in building AI agents]] is determining the quality of recommendations in a complex multi-agent system with many rounds of conversations <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>.

Solutions and learnings:
*   Closing the loop with **human scoring, structured feedback, and revision cycles** is essential <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>.
*   **Human evaluation** is the most effective assessment, especially in early stages, as LLM evaluations do not provide the necessary insights for system improvements <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.
*   Cat.io developed an internal human evaluation tool called "Eagle Eye" to analyze specific cases, including architecture, extracted requirements, agent conversations, and generated recommendations, allowing for relevance, visibility, and clarity studies <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>.
*   **Confidence is not correctness**; while confidence can help, it cannot always be trusted <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>.
*   **Human feedback is essential early on** when building such systems from scratch <a class="yt-timestamp" data-t="20:51:00">[20:51:00]</a>.
*   **Evaluation must be baked into system design** from the outset, not added later, ensuring continuous assessment throughout development <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.
*   Hallucinations, like an agent scheduling a workshop, are part of the [[challenges_in_creating_effective_ai_agents | challenges in creating effective AI agents]] and are identified through such evaluation tools <a class="yt-timestamp" data-t="22:05:00">[22:05:00]</a>.

## Conclusion: Designing for Reasoning
Building an AI copilot for architecture is about designing a system that can reason, not just generate answers <a class="yt-timestamp" data-t="23:06:00">[23:06:00]</a>. This system needs to have a comprehensive view of large amounts of data, including thousands or millions of architecture components and numerous documents, to answer questions from diverse stakeholders ranging from developers to CTOs <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>.

Achieving this requires:
*   Defining clear roles, workflows, memories, and structure within the AI system <a class="yt-timestamp" data-t="24:04:00">[24:04:00]</a>.
*   Continuous experimentation to find patterns that work best with existing data, with graphs becoming increasingly important in designs <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>.
*   Carefully considering agent interactions and the level of autonomy granted to each agent <a class="yt-timestamp" data-t="24:39:00">[24:39:00]</a>. Cat.io is exploring frameworks like LangGraph for agent workflows and using graphs to capture as much memory as possible to ensure AI always has the right context per task <a class="yt-timestamp" data-t="25:04:00">[25:04:00]</a>.

These ongoing efforts are shaping the [[future_directions_for_software_architecture_using_ai | future directions for software architecture using AI]] <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.