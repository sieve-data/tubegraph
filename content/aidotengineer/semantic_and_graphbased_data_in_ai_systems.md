---
title: Semantic and graphbased data in AI systems
videoId: 9mzfioh1Zag
---

From: [[aidotengineer]] <br/> 

AI systems, particularly those designed for cloud architecture, necessitate advanced reasoning capabilities beyond mere automation to manage increasing complexity <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Cloud systems are growing in complexity due to diverse users, developers, tools, constraints, and ever-rising expectations <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Synergistic tools struggle to scale across the wide variety of decisions required for cloud architecture <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This demand calls for systems that can understand, debate, justify, and plan, which is indicative of reasoning, not just automation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Architectural design is not solely technical; it is also highly cognitive, involving constant negotiation of trade-offs based on requirement definition, available time, and resources <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Architects rely on scattered and implicit context to make these decisions, making it crucial for AI to comprehend their thought processes <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Challenges at the Intersection of AI and Architecture

Key [[challenges_and_solutions_in_ai_driven_data_processing | challenges]] arise when AI meets architecture design:
*   **Requirement Understanding** How to process requirements from various formats, identifying crucial, global, or specific elements <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Architecture Identification** Understanding the functions of diverse components within an architecture to grasp its overall operation <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Architecture Recommendation** Combining requirements and current architecture state to provide recommendations that either meet needs or improve adherence to best practices <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

These high-level problems translate into specific AI challenges involving a blend of semantic and graphic context <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Requirements are primarily textual, representing semantic context, while architecture is inherently graph data <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. The challenge lies in integrating these disparate data sources to enable higher-level reasoning and handle complex, vague, and broad queries that require breakdown and planning <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Evaluating and providing feedback to such large, multi-component AI systems is also crucial <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Grounding AI Agents in Specific Context

Effective reasoning by large language models (LLMs) requires proper context about architecture <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Translating [[natural_language_processing_and_ai | natural language]] into meaningful architecture retrieval tasks, especially quickly, is challenging <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Strategies employed include:
*   **Semantic Enrichment of Architecture Data** Collecting relevant semantic information for each component to make it more searchable and findable in vector search <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Graph-Enhanced Component Search** Utilizing graph algorithms to retrieve specific components or types of components within an architecture <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This approach allows not only finding nodes but also connecting them and adding context for proper reasoning <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Early Score Enrichment of Requirement Documents** Scoring documents based on important concepts to facilitate faster retrieval, particularly when dealing with a large corpus of text <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. Initial iterations used requirement templates to structure extracted information for downstream tasks <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### Learnings on Grounding Agents
*   Semantic grounding improves reasoning but has limitations, especially when dealing with complex graph data, where it may not [[scaling_paradigms_in_ai_research | scale]] or can lead to overly detailed responses <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   The exact structure and focus for retrieval are critical for agents <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   [[conversational_and_experiential_memory_in_ai_systems | Graph memory]] supports continuity in understanding relationships between different nodes <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

Initial architecture retrieval designs involved breaking down JSON architecture data into natural language, enriching it with connection data, embedding, and storing it in a vector database for semantic search <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. While yielding some good results, semantic search proved limited for graph data, leading to a shift towards more [[graphbased_fraud_detection_and_ai_technology | graph-based]] searches and the development of a [[use_of_knowledge_graphs_in_generative_ai | knowledge graph]] approach <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Similarly, while requirement templates aided fast retrieval, context can be lost in larger searches, suggesting a potential role for graph analysis here as well <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Complex Reasoning Scenarios with Multi-Agent Orchestration

Architectural design inherently involves conflicting goals, trade-offs, and debates <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. AI agents need to collaborate, argue, and converge on justified recommendations <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

To achieve this, the following were implemented:
*   **Role-Specific Multi-Agent Orchestration** A system where multiple agents with distinct roles work together, supporting dynamic resolution of trade-offs rather than just executing static plans <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Structured Message Format** Transitioning from XML to structured messages improved workflow and inter-agent collaboration, enabling longer agent chains <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Context Management** Isolating conversations between agents to conserve tokens and prevent increased hallucination observed with larger shared memories <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Cloning Agents for Parallel Processing** Duplicating agents for specific tasks, managing memory at the cloning point, to speed up processes <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

### Learnings on Multi-Agent Systems
*   Structured outputs are critical for clarity and control, despite potential concerns about reducing the model's reasoning abilities <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   Dynamic orchestration encourages higher creativity in planning and reaching results <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   Successful multi-agent orchestration requires robust control flow, not just hopeful interaction <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.

The production system generates recommendations using a multi-agent setup <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. This includes:
*   A **Chief Architect** overseeing and coordinating high-level tasks <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
*   Ten **Staff Architects**, each specializing in a domain (e.g., infrastructure, API, IAM) <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   A **Requirement Retriever** accessing requirement data <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   An **Architecture Retriever** understanding the current architecture state and components <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

The workflow involves three main sequential tasks:
1.  **List Generation** Staff architects request information from retrievers (in parallel) to generate a list of possible recommendations <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.
2.  **Conflict Resolution** The Chief Architect prunes the generated list for conflicts or redundancies <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
3.  **Design Proposal** Cloned staff architects (each with access to past history but generating separate current histories) write full design proposals for each recommendation topic, detailing gap analysis and proposed improvements <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

## Evaluation and Feedback

Determining the quality of AI-generated recommendations, especially within complex multi-agent systems with rounds of conversations, is a significant challenge <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

Key findings regarding evaluation:
*   Human evaluation is the most effective approach, especially in early development stages, as LLM evaluations do not provide the necessary depth for improvement <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   An internal human evaluation tool, "Eagle Eye," allows detailed analysis of specific cases, architectures, extracted requirements, agent conversations, and generated recommendations to assess relevance, visibility, and clarity <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.
*   Confidence in AI output does not equate to correctness <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.
*   Evaluation must be integrated into the system design from the outset, not added as an afterthought <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. This includes considering human evaluation tools, monitoring dashboards, or LLM-based feedback loops <a class="yt-timestamp" data-t="00:21:28">[00:21:28]</a>.
*   Monitoring conversations can help identify issues like hallucinations, where agents might deviate or propose irrelevant actions <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.

## Conclusion: Reasoning Systems, Not Just Assistance

Building an AI co-pilot for cloud architecture is about designing a system that can reason, rather than merely generating answers <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. This requires handling vast amounts of data, including thousands or millions of architecture components and numerous documents, to answer diverse questions from various stakeholders <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

Key elements for building such a reasoning system include:
*   Defining clear roles and workflows for agents <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>.
*   Implementing effective memory management strategies <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.
*   Establishing clear structures for data and communication <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

Experimentation is crucial to discover patterns that work best with existing data <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>. [[benefits_of_graph_databases_in_ai_applications | Graphs are increasingly important]] in these designs, influencing agent interactions and the level of autonomy granted to each agent <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. Frameworks like LangGraph are being utilized for building agent workflows, often with a manager layer for higher-level control <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. Capturing as much memory as possible in graphs ensures AI always has the right context <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. This ongoing development is seen as the future of AI-driven software design <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>.