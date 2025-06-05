---
title: Agentic workflows and their levels of autonomy
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

[[agentic_frameworks_and_their_applications | Agentic workflows]] are becoming increasingly important in the development of reliable AI solutions <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. These workflows are characterized by how much control, reasoning, and autonomy an AI system possesses <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. As models evolve, so too does the complexity and capability of these workflows, moving beyond simple API calls to proactive, decision-making systems <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. Success in production isn't solely about the models; it's about how the system is built around them <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

## Levels of Agentic Behavior

A framework has been developed to define different levels of [[agentic_frameworks_and_their_applications | agentic behavior]], recognizing that every AI workflow has some level of this behavior <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. This framework is not static and can expand as models evolve <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### L0: Basic LLM Call (No External Planning)

At Level 0, the workflow involves an LLM call retrieving data, potentially with inline evaluations, to generate a response <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.
*   **Characteristics**:
    *   No external reasoning, planning, or decision-making beyond what's embedded in the prompt and the model's inherent behavior <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    *   The model performs all reasoning within the prompt itself <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
    *   No external "agent" organizes decisions or plans actions <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
    *   Some reasoning and [[agentic_frameworks_and_their_applications | agentic behavior]] still exist at the model level <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.

### L1: Tool Use

Moving to Level 1, workflows gain the ability to use various tools <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
*   **Characteristics**:
    *   The AI system decides *when* to call APIs and take actions <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.
    *   The model decides whether to call a specific tool or a vector database to retrieve more data before generating an output <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
    *   Memory plays a crucial role for multi-threaded conversations, capturing context throughout the workflow <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
    *   Evaluation is necessary at every step to ensure models make correct decisions and use the right tools <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
    *   Workflows can range from simple to complex, with multiple branching paths and numerous tools <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
    *   The focus is on orchestration: how models interact with the system and data, and how to ensure correct context from databases <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

### L2: Structured Reasoning

At Level 2, workflows demonstrate structured reasoning, moving beyond simple [[agentic_frameworks_and_tool_integration | tool use]] <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.
*   **Characteristics**:
    *   Workflows notice triggers, plan actions, and execute tasks in a structured sequence <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
    *   Tasks are broken down into multiple steps, involving information retrieval, calling tools, evaluating usefulness, and refining outputs in a continuous loop <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
    *   [[agentic_frameworks_and_their_applications | Agentic behavior]] becomes more intentional, as the system actively decides what needs to be done and spends more time "thinking" <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.
    *   The process is still finite; the workflow terminates once its planned steps are completed <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
    *   Significant innovation is expected here, with [[agentic_enterprise_and_ai_agents | AI agents]] developed for planning and reasoning using advanced models like 01 or O3 <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

### L3: Proactive Autonomy

Level 3 introduces greater autonomy and decision-making not explicitly defined by human creators <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.
*   **Characteristics**:
    *   Systems proactively take actions without waiting for direct input <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
    *   Instead of terminating after a single request, the system remains active, continuously monitoring its environment and reacting as needed <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
    *   Can interact with external services (e.g., email, Slack, Google Drive) to plan and execute next moves in real-time, or request human input <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
    *   AI workflows become less of a tool and more of an independent system <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.

### L4: Fully Creative/Inventive

Level 4 represents the most advanced stage, where AI moves beyond automation and reasoning to become an inventor <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>.
*   **Characteristics**:
    *   Creates its own new workflows, utilities, [[agentic_enterprise_and_ai_agents | agents]], prompts, function calls, and tools <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
    *   Solves problems in novel ways <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
    *   Currently "Out Of Reach" due to constraints with models like overfitting (models favoring training data) and inductive bias (models making assumptions based on training data) <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
    *   The goal is AI that invents, improves, and solves problems in unforeseen ways <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

### Current State and Future Outlook

Most production-grade AI solutions currently fall within the L1 segment, focusing on robust orchestrations that enable models to interact effectively with systems and data <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Significant innovation is anticipated in L2 workflows this year, with the development of [[agentic_enterprise_and_ai_agents | AI agents]] capable of planning and reasoning for complex tasks <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. L3 and L4 are still limited by current models and surrounding logic <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

## Example: SEO Agent Workflow

An example of an [[agentic_frameworks_and_their_applications | agentic workflow]] that lies between L1 and L2 is an SEO agent designed to automate the entire SEO process from keyword research to content creation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

*   **Components**:
    *   **SEO Analyst and Researcher**: Takes a keyword and analyzes top-performing articles using Google Search <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>. It identifies good components to amplify and missing segments for improvement <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>. The researcher conducts further searches based on identified gaps <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.
    *   **Writer**: Uses the research and planning output to create a first draft <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>. This content is context-rich, drawing from analyzed articles and potentially a RAG database of existing articles and learnings <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.
    *   **Editor (LLM-based Judge)**: Evaluates the first draft against predefined rules in its prompt <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
    *   **Feedback Loop**: The editor's feedback is passed back to the writer via a memory component (chat history), continuously looping until a specific criterion is met (e.g., the editor deems it an "excellent post" or a set number of iterations are completed) <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
    *   **Memory Component**: Captures all previous conversations between the writer and the editor <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.
*   **Outcome**: Produces a useful and impressive first draft that leverages context smartly <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. This system saves significant time by automating content foundations <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.

This example highlights the importance of a test-driven approach for building reliable and continuously improving [[agentic_frameworks_and_their_applications | agentic systems]] <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.