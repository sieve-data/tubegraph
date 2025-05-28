---
title: meta GPT multi agent collaborative framework
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

MetaGPT, formally known as "Meta Programming for Multi-Agent Collaborative Framework," is a GitHub repository and paper that has garnered significant attention, reaching the top of trending repositories with over 20,000 stars <a class="yt-timestamp" data-t="01:07:10">[01:07:10]</a>. The associated paper was released on August 7, 2023 <a class="yt-timestamp" data-t="01:42:42">[01:42:42]</a>. The project involves affiliations with Deep Wisdom, Chinese University of Shenzhen, Nanjing, Shaman University, and Berkeley <a class="yt-timestamp" data-t="03:19:07">[03:19:07]</a>. Deep Wisdom, a startup, was founded in 2017 and is currently in its Series C funding round <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

## Core Concept: Metaprogramming and Role-Playing Agents

MetaGPT aims to solve complex tasks by incorporating human workflows as a metaprogramming approach into [[agent_frameworks_and_their_definitions | multi-agent frameworks]] <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a> <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>. The core idea is to have large language models (LLMs) in a multi-agent system pretend to be different people, corresponding to experts in a software team <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. This system leverages an "assembly line paradigm" to assign diverse roles to various agents, similar to how human software development teams function <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a> <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.

### Addressing LLM Hallucination

Existing LLM-based [[agent_frameworks_and_their_definitions | multi-agent systems]] often focus on simple dialogue tasks, with complex tasks rarely studied due to the LLM hallucination problem <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a> <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>. This hallucination can become cascading when chaining multiple intelligent agents, leading to system failure <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. MetaGPT proposes its framework to mitigate this cascading effect <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.

## Architecture and Components

The MetaGPT framework is structured into two distinct layers <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a> <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>:

1.  **Foundational Component Layer:** Essential for agent operations and system-wide communication <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. It includes:
    *   **Environment:** Provides a shared workspace and communication channels <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a> <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
    *   **Memory:** Stores and retrieves historical messages <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a> <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
    *   **Roles:** Encapsulate domain-specific skills and workflows, serving as the backstory for each agent <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a> <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
    *   **Actions:** Define modular subtasks that each agent can execute <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
    *   **Tools:** Provide common services and utilities <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.

2.  **Collaboration Layer:** Facilitates agent coordination through mechanisms like knowledge sharing and workflow encapsulation <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a> <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.
    *   **Knowledge Sharing:** Agents can exchange information effectively, contributing to a shared knowledge base <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. This public database is analogous to public thoughts in [[generative_agents_and_simulation_of_human_behavior | Generative agents and simulation of human behavior]] papers <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a> <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
    *   **Workflow Encapsulation:** Guides agents with specialized "role prompts" known as "anchor agents" <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. These roles include capabilities like thinking, reflection, and knowledge accumulation <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

Agents interact with the environment using a publish-subscribe (pub/sub) pattern, where individual nodes publish and subscribe to information, similar to the ROS (Robot Operating System) or modern social media platforms <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a> <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a> <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a> <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. The agent's internal loop follows an "observe, think, knowledge precipitation, act, state management, broadcast messages" sequence, which mirrors the "sense, plan, act" loop seen in robotics and [[the_role_of_reinforcement_learning_in_developing_agent_frameworks | reinforcement learning]] <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a> <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a> <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Simulated Software Development Roles

MetaGPT defines specific roles inspired by human software development teams:

*   **Product Manager (PM):** Determines tasks and creates product requirement documents (PRD) <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a> <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Architect:** Determines system design <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a> <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   **Project Manager:** Outlines steps from analysis to delivery <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a> <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Engineer:** Writes code <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   **QA Engineer:** Validates outputs and minimizes errors <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.

The process begins with a single-line requirement, like "write a classic and simple Flappy Bird game," which is then decomposed and handled by distinct roles, ultimately leading to executable code <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a> <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

## Practical Application and Evaluation

The framework was tested by generating a Gradio front end for a robotic AI cat toy <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a> <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

### Observed Process and Outputs

*   **Product Manager (Alice):** Generated a PRD with user requirements (e.g., control movements, customize behavior, schedule play sessions, monitor interactions), competitive analysis (quadrant chart), and prioritized requirements <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a> <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>. However, the competitive analysis quadrants were deemed "meaningless" as they just stated "more/less user friendly" or "feature rich" without actionable insights <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a> <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
*   **Architect (Bob):** Proposed using Gradio for the front end and Flask for backend services <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a> <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. It defined file structures and API specifications, but the API schemas were considered too bare-bones and generic, lacking specific details like `direction` or `speed` parameters for toy control <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a> <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a> <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a> <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.
*   **Project Manager:** Generated a task list and API specifications <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. Notably, it stated "no third-party packages required" for a robotic cat toy, which was criticized for missing essential robotics libraries like ROS or Dynamixel servos <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a> <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.
*   **Engineer:** Produced Python code for control, customization, monitor, schedule, and utility functions <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. The code was largely criticized for being generic, using arbitrary object structures, inconsistent time formats (string vs. `datetime` object), and employing a "pointless" utility class with static methods for simple JSON conversions <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a> <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a> <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a> <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a> <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>. The main Flask application code was deemed primitive and potentially incorrect due to issues like missing imports (`requests`) and unorthodox route registration within a class <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a> <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a> <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   **QA Engineer:** No test file was found to be generated by the QA engineer <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a> <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.

### Comparison to Direct LLM Prompting

[[comparison_of_direct_coding_prompts_to_multi_agent_frameworks | Directly prompting GPT-4]] and Claude to create the same Gradio interface yielded more useful and actionable code, even if not perfect <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a> <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. A direct prompt to GPT-4 generated a working Gradio interface with concepts like "direction" and "speed" sliders <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a> <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>. This suggests that MetaGPT's complex multi-agent simulation resulted in "overly verbose and non-specific" output, effectively "confusing the engineer" with unnecessary context <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a> <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a> <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a> <a class="yt-timestamp" data-t="10:30:00">[10:30:00]</a>. The entire process of MetaGPT for this task cost about 87 cents in tokens <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

### Benchmarking Results

MetaGPT claims to significantly outperform [[gpt4_ensemble_of_models | GPT-4]] and Codex on benchmarks like HumanEval and MBPP <a class="yt-timestamp" data-t="01:37:14">[01:37:14]</a> <a class="yt-timestamp" data-t="01:38:48">[01:38:48]</a>.
*   **HumanEval:** A problem-solving dataset used to measure functional correctness for synthesizing programs from docstrings <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a> <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   **MBPP (Mostly Basic Python Problems):** A benchmark of 1,000 crowdsourced Python programming problems designed for entry-level programmers <a class="yt-timestamp" data-t="01:35:26">[01:35:26]</a> <a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>.

The critique is that these benchmarks evaluate simple function writing rather than complex system design, which MetaGPT purports to solve <a class="yt-timestamp" data-t="01:36:26">[01:36:26]</a> <a class="yt-timestamp" data-t="01:36:53">[01:36:53]</a>. The improved performance of MetaGPT on these benchmarks might be attributed to the significantly larger number of tokens used to generate context, potentially increasing the chance of getting the answer right on the first try (`pass@1`) <a class="yt-timestamp" data-t="01:37:42">[01:37:42]</a> <a class="yt-timestamp" data-t="01:37:55">[01:37:55]</a>.

### Implications for Software Engineering

The observed inefficiencies of MetaGPT, compared to direct LLM prompting, raise questions about the efficacy of traditional, hierarchical software development processes (Product Manager, Architect, Project Manager, Engineer, QA) <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a> <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>. The argument is made that these bureaucratic structures, often driven by factors like seniority and compensation rather than optimal code creation, might be unnecessary when direct interaction with the "engineer" (the LLM) yields better results <a class="yt-timestamp" data-t="01:58:53">[01:58:53]</a> <a class="yt-timestamp" data-t="01:59:05">[01:59:05]</a>. This critique suggests a future where artificial intelligence may streamline or eliminate certain intermediary roles in the software development lifecycle.