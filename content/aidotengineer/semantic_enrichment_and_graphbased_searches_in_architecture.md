---
title: Semantic enrichment and graphbased searches in architecture
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Immani, Co-founding Head of AI at Cat.io, discusses grounded reasoning systems for cloud architecture and the use of multi-agent orchestration to build an AI copilot <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## The Need for Reasoning in Cloud Architecture
Cloud systems are growing in complexity due to increasing user and developer numbers, tools, constraints, and rising expectations <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Current synergistic tools do not scale across the diversity of decisions needed for cloud architecture <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Systems are required that can understand, debate, justify, and plan to solve these problems, moving beyond mere automation to true reasoning <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The architecture stack is not only technical but also cognitive <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Architects constantly negotiate tradeoffs based on requirement definition, time availability, and resources <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. They rely on scattered and implicit context to make decisions, and capturing this for AI requires understanding their thought processes <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Challenges Where AI Meets Architecture
At a high level, Cat.io identifies three key challenges in solving architecture design problems with AI:
1.  **Requirement Understanding**: Determining the origin, format, important pieces, and scope (global vs. specific) of requirements <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Architecture Identification**: Understanding the functions of various components within an architecture, given that their roles can differ based on their placement and type <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
3.  **Architecture Recommendation**: Providing recommendations to match requirements or improve the architecture based on best practices, given the current architecture state and understood requirements <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Technical Challenges: Semantic vs. Graph Context
To address these higher-level problems, specific AI-related challenges arise:
*   **Mixed Semantic and [[Graph data structures in AI and its benefits | Graph data structures in AI and its benefits | Graphical Context]]**: Requirements are often textual, while architecture is inherently [[Graph data structures in AI and its benefits | graph data]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Integrating these diverse data sources for higher-level reasoning is crucial <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Complex Reasoning Scenarios**: Queries can be vague, broad, and require breakdown and proper planning to yield accurate answers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Evaluation and Feedback**: Developing robust methods to evaluate and provide feedback to a large AI system with multiple moving parts <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Grounding Agents in a Specific Context
Large Language Models (LLMs) need proper context to reason effectively <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Translating natural language into meaningful architecture retrieval tasks, and doing so quickly, is challenging <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

Cat.io experimented with approaches for both architecture and requirement retrieval:
*   **Semantic Enrichment of Architecture Data**: Collecting relevant semantic information for each component to make it more searchable and findable in vector search <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **[[Graph data structures in AI and its benefits | Graph data structures in AI and its benefits | Graph-enhanced Component Search]]**: Utilizing [[Graph data structures in AI and its benefits | graph algorithms]] to retrieve the correct information pieces when searching for specific components within an architecture <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Early Score Enrichment of Requirement Documents**: For faster retrieval, important concepts within requirements were identified and documents were scored, simplifying the initial retrieval task for a large corpus of text <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Learnings from Early Approaches
*   Semantic grounding improves reasoning but has limitations, especially when scaling or requiring highly detailed responses <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   The design of the grounding mechanism is critical for soft grounding, specifically instructing the agent on what to focus on and retrieve <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   [[Graph data structures in AI and its benefits | Graph memory]] supports continuity and not just accuracy, allowing connections between different nodes to provide additional context for reasoning <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

An early design for architecture retrieval involved breaking down JSON architecture data into natural language, enriching it with connection data, embedding it, and storing it in a vector database <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. While this showed good results, it was found that semantic search has limitations for graph data, leading to a shift towards [[GraphRAG systems and applications | graph-based searches]] and a [[Graph data structures in AI and its benefits | knowledge graph]] approach <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

An initial design for understanding requirements involved pre-processing, splitting, and embedding documents <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. An extra step involved using requirement templates to structure extracted information into "pods," ensuring relevance for downstream tasks <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. This helped with fast retrieval and structuring business requirements <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. However, limitations were observed with an increasing number of documents, leading to context loss in larger searches, suggesting that [[Graph data structures in AI and its benefits | graph analysis]] could help <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Addressing Complex Reasoning Scenarios
Good architecture design inherently involves conflicting goals, trade-offs, and debates <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Agents need to be able to collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

Cat.io's approach included:
*   **[[Agentic architectures and systems design | Multi-agent orchestration]] with Role-Specific Agents**: Building a system where multiple agents work together with distinct properties <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Structured Message Format**: Moving from XML to structured messages improved workflow building and enabled multiple agents to work together in longer chains <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Context Management**: Isolating conversations between agents to save tokens and prevent increased hallucination observed with larger memory <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Cloning Agents for Parallel Processing**: Duplicating agents for specific tasks to speed up processes, requiring careful memory management at the cloning point <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Learnings
*   Structured outputs significantly improve clarity and control, which is crucial for better programming, despite potential trade-offs in reasoning abilities <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   [[Agentic architectures and systems design | Multi-agent systems]] allow agents to dynamically resolve trade-offs rather than executing static plans <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Making the orchestration more dynamic fosters higher creativity in planning and reaching results <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   Successful [[Agentic architectures and systems design | multi-agent orchestration]] requires control flow; simply letting agents work without guidance is not feasible <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

## Kato's Multi-Agent Recommendation System
Cat.io's production stack delivers recommendations based on a [[Agentic architectures and systems design | multi-agent system]] <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Recommendations are categorized (e.g., architecture messaging, API integration) and include a description, target state, gap analysis, and recommended actions <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

The system comprises:
*   **Chief Architect**: Oversees and coordinates higher-level tasks <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **10 Staff Architects**: Each specialized in a domain (e.g., infrastructure, API, IM) <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Requirement Retriever**: Accesses requirements data <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Architecture Retriever**: Understands the current architecture state and can answer questions about components <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

The multi-agent workflow operates in three main sequential tasks:
1.  **List Generation**: The Chief Architect requests a list of possible recommendations from Staff Architects, who parallelly send requests to the Architecture State Agent and Requirements Agent. The Staff Architects then return possible recommendations to the Chief <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
2.  **Conflict Resolution**: The Chief Architect reviews the generated list for conflicts or redundancies and prunes it <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
3.  **Design Proposal**: For each recommendation topic, a full design proposal is written, detailing gap analysis and improvement proposals. During this step, each Staff Architect is cloned based on the number of recommendations they need to generate. Each clone has access to past history but generates its own isolated current history, ensuring comprehensive proposals <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.

## Evaluation and Feedback
A key challenge is determining if a recommendation is good, especially with multiple agents and rounds of conversation <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. The solution involves closing the loop with human scoring, structured feedback, and revision cycles <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

### Learnings
*   Human evaluation is the most effective method, particularly in early stages of system development <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   LLM evaluations are helpful but do not provide the necessary insights for making critical improvements <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.
*   Confidence displayed by the system does not equate to correctness <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   Evaluation mechanisms must be integrated into the system design from the outset, not added as an afterthought <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.

Cat.io developed an internal human evaluation tool called "Eagle Eye" <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. This tool allows review of specific cases, extracted architecture and requirements, agent conversations, and generated recommendations to assess relevance, visibility, and clarity, and assign scores <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. The tool has helped identify issues like hallucinations, where agents might make requests that are not relevant to their actual task <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.

## Conclusion: Designing Reasoning Systems
Building an AI copilot is about designing a system that can *reason*, not just generate answers <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Such a system needs a comprehensive view of large datasets, like thousands or millions of architecture components and numerous documents, to answer varied questions from diverse stakeholders (developers to CTOs) <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

Achieving this requires:
*   Clearly defined roles <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Structured workflows <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Effective memory management <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   Structured interactions <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

Experimentation is vital to discover patterns that work best with existing data <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. [[Graph data structures in AI and its benefits | Graphs]] are increasingly important in Cat.io's designs <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. They also explore the level of autonomy to grant each agent <a class="yt-timestamp" data-t="00:24:46">[00:24:46]</a>. LangGraph is used for building agent workflows, with SLAM managing higher-level aspects <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>. [[Graph data structures in AI and its benefits | Graphs]] are utilized to capture as much memory as possible, ensuring the AI maintains the right context for tasks <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>.

The belief is that AI will fundamentally change how software is designed <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.