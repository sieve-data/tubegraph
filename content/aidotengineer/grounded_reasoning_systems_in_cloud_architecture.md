---
title: Grounded reasoning systems in cloud architecture
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

Immani, co-founding head of AI at Cat.io, discusses how to build an AI copilot using [[using_reasoning_models_and_tool_calls_in_ai | multi-agent orchestration]] for grounded reasoning systems in cloud architecture <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## The Need for Reasoning in Cloud Architecture
Cloud architecture requires reasoning, not just automation, due to its increasing complexity driven by users, developers, tools, and rising expectations <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Existing synergistic tools do not scale across the diverse decisions needed for cloud architecture <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Systems are needed that can understand, debate, justify, and plan to solve these complex problems, which goes beyond simple automation and into the realm of reasoning <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The architecture stack is not only technical but also highly cognitive <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Architects constantly negotiate tradeoffs based on defined requirements, available time, and resources <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. They rely on scattered and implicit context for decisions, and for AI to capture this, it must understand how architects think <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Challenges at the Intersection of AI and Architecture
Cat.io addresses three high-level challenges in solving architecture design problems with AI:
1.  **Requirement Understanding**: Identifying the format, important pieces, and scope (global or specific) of requirements <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Architecture Identification**: Understanding the functions of various components within an architecture <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
3.  **Architecture Recommendation**: Providing recommendations that match requirements or improve the existing architecture based on best practices <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

These challenges translate into specific AI-related hurdles:
*   **Mixing Semantic and Graph Context**: Combining textual requirement documents with inherently graph-structured architecture data <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Complex Reasoning Scenarios**: Handling vague, broad, and complex questions that require breakdown and proper planning for accurate answers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Evaluation and Feedback**: Developing methods to evaluate and provide feedback to large AI systems with many moving parts <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Grounding Agents in Specific Contexts
Effective AI systems require proper context for architecture reasoning <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Translating natural language into meaningful architecture retrieval tasks is difficult, especially when speed is critical <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

Approaches explored:
*   **Semantic Enrichment of Architecture Data**: Collecting relevant semantic information for each component to make it more searchable in vector search <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Graph-Enhanced Component Search**: Utilizing graph algorithms to retrieve the right information pieces from an architecture when searching for components <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Early Score Enrichment of Requirement Documents**: Scoring documents based on important concepts for faster retrieval from large text corpora <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Learnings on Grounding Agents
*   Semantic grounding improves reasoning but doesn't always work, sometimes falling short in scalability or providing overly detailed responses <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Right design is critical for "soft grounding," telling the agent what to focus on and retrieve <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Graph memory supports continuity, not just accuracy, by connecting different nodes in searches and adding context for reasoning <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Semantic search has limitations for graph data, leading to a shift towards graph-based searches and knowledge graphs <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

For requirement understanding, Cat.io initially used requirement templates to structure extracted information for downstream tasks, which helped with fast retrieval and structuring business requirements <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. However, this approach had limitations, as context can be lost when increasing the number of documents, indicating a potential role for graph analysis here too <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Complex Reasoning Scenarios with Multi-Agent Systems
Good design involves conflicting goals, tradeoffs, and debates <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. AI agents are needed that can collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

### Multi-Agent System Design
Cat.io built a [[using_reasoning_models_and_tool_calls_in_ai | multi-agent orchestration]] system with role-specific agents <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. Key elements include:
*   **Structured Message Format**: Using structured messages (e.g., JSON, moving away from XML) helps build better workflows and enables multiple agents to work together in longer chains <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Conversation Management**: Isolating conversations between agents prevents token waste and avoids "hostination" (a term for increased hallucination) observed with increased memory <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Agent Cloning for Parallel Processing**: Cloning agents for specific tasks speeds up processes and requires careful memory management <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Learnings on Complex Reasoning
*   Structured outputs improve clarity and control, which is super important for better programming <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. While there's a tradeoff with reasoning abilities, the results are good <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   Agents should resolve tradeoffs dynamically, not just execute static plans <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. More dynamic orchestration leads to higher creativity in planning and reaching results <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   Successful [[using_reasoning_models_and_tool_calls_in_ai | multi-agent orchestration]] requires control flow; simply letting agents work together without guidance is not sufficient <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

### Multi-Agent Workflow Example
Cat.io's production system for architecture recommendations uses a multi-agent system <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.
The system includes:
*   **Chief Architect**: Oversees and coordinates higher-level tasks <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   **10 Staff Architects**: Each specialized in a domain (e.g., infrastructure, API, IAM) <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Requirement Retriever**: Accesses requirements data <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   **Architecture Retriever**: Understands the current architecture state and can answer questions about components <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

The workflow consists of three main sequential tasks to generate recommendations <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>:
1.  **List Generation**: Staff architects, requested by the Chief Architect, send parallel requests to the Architecture State Agent and Requirements Agent. The results are gathered and sent back to the Chief Architect as a list of possible recommendations <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
2.  **Conflict Resolution**: The Chief Architect reviews the generated list for conflicts or redundancies, pruning it <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
3.  **Design Proposal**: For each recommendation topic, staff architects generate a full design proposal, including gap analysis and proposed improvements <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. During this step, staff architects are cloned for each recommendation they need to generate, with each clone having access to past history and generating its own separated current history <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Evaluation and Feedback
Evaluating the quality of recommendations from a complex [[using_reasoning_models_and_tool_calls_in_ai | multi-agent system]] with many rounds of conversations is a challenge <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. The loop needs to be closed with human scoring, structured feedback, and revision cycles <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### Learnings on Evaluation
*   Human evaluation is currently the best method, as LLM evaluations, while good, don't provide the necessary insights for improvement <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.
*   Cat.io developed an internal human evaluation tool called "Eagle Eye" to review specific cases, extracted architecture/requirements, agent conversations, and generated recommendations <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. This tool allows for relevance, visibility, and clarity studies, helping focus future development <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.
*   Confidence is not correctness; while it can help, it cannot always be trusted <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   Human feedback is essential early on when building systems from scratch <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   Evaluation must be baked into system design from the start, not added later <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. This means designing for evaluability, whether through human tools, monitoring dashboards, or LLM-based feedback loops <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   The evaluation tool helps identify issues like hallucination, where an agent might generate irrelevant requests <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.

## Conclusion and Future Outlook
Building a copilot is about designing a system that can reason, not just generate answers <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. The goal is to build a system with a comprehensive view of large amounts of data (thousands or millions of architecture components, numerous documents) to answer diverse questions from various stakeholders, from developers to CTOs <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

Achieving this requires defining roles, workflows, memories, and structure <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. Extensive experimentation is crucial to discover patterns that work best with existing data <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. Graphs are becoming increasingly important in Cat.io's designs <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

Cat.io is currently using LangChain's LangGraph for building some agent workflows, managed by a higher-level manager, and using graphs to capture as much memory as possible to ensure the AI always has the right context per task <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>. The team believes this approach will fundamentally change how AI designs software <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.