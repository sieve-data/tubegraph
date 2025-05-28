---
title: MetaGPT and multiagent collaborative frameworks
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

MetaGPT is an innovative framework that leverages large language models (LLMs) for multi-agent collaboration in software development, aiming to replicate human workflows <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. The GitHub repository for MetaGPT has gained significant traction, accumulating over 20,000 stars and consistently ranking at the top of trending repositories since its paper release around August 7, 2023 <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a> <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.

The project is a collaboration between various Chinese universities, including Chinese University of Shenzhen, Nanjing, Xiamen University, Berkeley, and the startup Deep Wisdom <a class="yt-timestamp" data-t="03:26:26">[03:26:26]</a>.

## Core Concepts and Architecture

MetaGPT aims to address the challenges of LLM hallucination in complex multi-agent tasks, where errors can cascade when agents are naively chained together <a class="yt-timestamp" data-t="05:29:29">[05:29:29]</a>. The framework approaches this by encoding efficient human workflows as a metaprogramming approach <a class="yt-timestamp" data-t="06:30:30">[06:30:30]</a>.

Key architectural features include:
*   **Standard Operating Procedures (SOPs)**: MetaGPT [[generative_ai_agents_and_human_behavior_simulation | encodes SOPs]] from human software teams into prompts to enhance structured coordination <a class="yt-timestamp" data-t="08:21:21">[08:21:21]</a>.
*   **Modular Outputs**: It mandates modular outputs, empowering agents with domain expertise comparable to human professionals <a class="yt-timestamp" data-t="08:26:26">[08:26:26]</a>.
*   **Assembly Line Paradigm**: The framework leverages an assembly line paradigm to assign diverse roles to various agents, mimicking how different specialists contribute to a final product, like in car manufacturing <a class="yt-timestamp" data-t="09:01:01">[09:01:01]</a>.

The MetaGPT [[agent_frameworks_and_their_applications | framework]] is designed with a two-layer architecture <a class="yt-timestamp" data-t="03:33:33">[03:33:33]</a>:
1.  **Foundational Component Layer**: Essential for agent operations and system-wide communication, comprising core elements such as:
    *   **Environment**: Enables a shared workspace and communication among agents <a class="yt-timestamp" data-t="03:41:41">[03:41:41]</a>.
    *   **Memory**: Stores and retrieves historical messages <a class="yt-timestamp" data-t="03:43:43">[03:43:43]</a>.
    *   **Roles**: Encapsulate domain-specific skills and workflows <a class="yt-timestamp" data-t="03:46:46">[03:46:46]</a>.
    *   **Actions**: Execute modular subtasks <a class="yt-timestamp" data-t="03:48:48">[03:48:48]</a>.
    *   **Tools**: Provide common services and utilities <a class="yt-timestamp" data-t="03:59:59">[03:59:59]</a>.
2.  **Collaboration Layer**: Facilitates agent coordination through mechanisms like knowledge sharing and workflow encapsulation <a class="yt-timestamp" data-t="03:50:50">[03:50:50]</a>. Agents communicate via an established publish/subscribe (pubsub) messaging framework <a class="yt-timestamp" data-t="03:24:24">[03:24:24]</a>.

Each "anchor agent" has a human-designed template including a name, profile, goal, and constraints, such as writing elegant, readable, and efficient code conforming to PEP 8 standards for an "engineer" agent <a class="yt-timestamp" data-t="03:57:57">[03:57:57]</a>. Agents operate in a loop similar to robotics, encompassing "observe, think, knowledge precipitation, act, state management, and broadcast messages" <a class="yt-timestamp" data-t="03:40:40">[03:40:40]</a>.

## Simulating Software Development Teams

MetaGPT simulates a traditional software development pipeline, involving distinct roles:
*   **Product Manager (PM)**: Defines requirements, conducts feasibility analysis, and creates user stories and competitive analyses <a class="yt-timestamp" data-t="13:30:30">[13:30:30]</a> <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.
*   **Architect**: Formulates the technical design and system architecture <a class="yt-timestamp" data-t="13:25:25">[13:25:25]</a> <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.
*   **Project Manager (PM)**: Breaks down tasks and illustrates sequence flow <a class="yt-timestamp" data-t="13:23:23">[13:23:23]</a> <a class="yt-timestamp" data-t="01:11:41">[01:11:41]</a>.
*   **Engineer**: Writes the actual code <a class="yt-timestamp" data-t="13:19:19">[13:19:19]</a>.
*   **QA Engineer**: Creates test files to validate outputs <a class="yt-timestamp" data-t="13:16:16">[13:16:16]</a>.

This "waterfall method" of software development is a key part of MetaGPT's approach <a class="yt-timestamp" data-t="13:54:54">[13:54:54]</a>.

## Practical Application and Observed Performance

The speaker tested MetaGPT by tasking it to "write a Gradio front end for a robotic AI cat toy" <a class="yt-timestamp" data-t="03:58:58">[03:58:58]</a>. The process generated several markdown files, including a Product Requirement Document (PRD), system design, and API specifications <a class="yt-timestamp" data-t="04:09:09">[04:09:09]</a> <a class="yt-timestamp" data-t="05:53:53">[05:53:53]</a>.

Observations from this test:
*   **Token Usage**: Running the demo cost approximately 87 cents, with subsequent requests using more tokens due to accumulating context (up to 10,000 tokens per request) <a class="yt-timestamp" data-t="04:47:47">[04:47:47]</a>.
*   **Generated Documents**: The PRD included user stories, competitor analysis (with a quadrant chart), and prioritized requirements <a class="yt-timestamp" data-t="04:26:26">[04:26:26]</a>. However, the competitive analysis chart was poorly formatted, and the chosen axes ("user-friendly" vs. "feature-rich") were criticized as "meaningless" <a class="yt-timestamp" data-t="04:49:49">[04:49:49]</a>. The system design provided generic and arbitrary file structures and API schemas (e.g., "control params" or "data" as a single property for an object) <a class="yt-timestamp" data-t="04:57:57">[04:57:57]</a> <a class="yt-timestamp" data-t="05:32:32">[05:32:32]</a>.
*   **Generated Code**: The Python code for the Gradio frontend was described as "nonsense" <a class="yt-timestamp" data-t="05:57:57">[05:57:57]</a>. It used inconsistent time formats and included a `Utils` class with two static methods that seemed pointless, suggesting a lack of grasp of Python design patterns <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>. The code for the Flask backend was also questionable, potentially suffering from design flaws and port conflicts <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a> <a class="yt-timestamp" data-t="01:16:02">[01:16:02]</a>.
*   **Missing Files**: The QA engineer phase did not produce a test file in the designated folder <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

## Comparison to Direct LLM Interaction

A direct query to [[using_gpt_api_for_conversation_generation | ChatGPT]] for the same Gradio interface produced significantly better and immediately working code, including relevant concepts like "direction" and "speed" for the toy's movement <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. This direct approach used far fewer tokens than the multi-agent MetaGPT process <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>.

When the MetaGPT-generated Flask code was fed back to ChatGPT for critique, it identified several issues:
*   Missing `requests` import from Flask <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>.
*   Unorthodox routing inside a class's `init` function <a class="yt-timestamp" data-t="01:15:27">[01:15:27]</a>.
*   Potential for repeated route registration if multiple instances of `Main` are created <a class="yt-timestamp" data-t="01:15:56">[01:15:56]</a>.
*   Port conflicts due to Flask and Gradio both attempting to serve web content <a class="yt-timestamp" data-t="01:16:02">[01:16:02]</a>.
*   Lack of error handling and data validation <a class="yt-timestamp" data-t="01:16:28">[01:16:28]</a>.

This critical feedback from a single LLM suggests that the "overly verbose process with overly defined rigid roles" in MetaGPT might actually "confuse the engineer" (LLM) rather than assist it <a class="yt-timestamp" data-t="01:31:31">[01:31:31]</a>.

## Evaluation and Benchmarks

The MetaGPT paper claims to generate "more coherent and correct" code compared to existing chat-based multi-agent systems <a class="yt-timestamp" data-t="09:54:54">[09:54:54]</a>. They evaluate their system using two benchmarks:
*   **HumanEval**: A problem-solving dataset for synthesizing programs from docstrings <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>.
*   **MBPP (Mostly Basic Python Problems)**: A dataset of 1,000 crowdsourced Python programming problems solvable by entry-level programmers <a class="yt-timestamp" data-t="01:35:36">[01:35:36]</a>.

The paper claims MetaGPT outperforms GPT-4 on these benchmarks, specifically stating a 31% "pass at 1" for a Salesforce model on HumanEval, placing it higher than other coding models like CodeGeeX <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. However, these benchmarks focus on individual function writing rather than complex system design, which is what MetaGPT purports to solve <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. The speaker expressed skepticism about MetaGPT's claimed superior performance over GPT-4 on these benchmarks, especially given the observed poor performance in the real-world test, suggesting that the "extra context" might not actually lead to better code or that the results might be cherry-picked <a class="yt-timestamp" data-t="01:38:11">[01:38:11]</a>.

## Broader Implications and Future Outlook

The speaker speculates on the implications of this experiment for real-world software engineering organizations <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a>. The observation that direct interaction with an LLM yields better results than a bureaucratic, multi-agent process raises questions about the efficiency of current corporate structures with their defined roles like Product Managers, Architects, and Project Managers <a class="yt-timestamp" data-t="01:59:01">[01:59:01]</a>.

The discussion also touches on the [[future_directions_for_multimodal_and_agi_development | future of AI development]], predicting a shift towards infinitely cheap cloud inference due to concentrated energy sources (e.g., fusion energy plants next to data centers) and massive GPU clusters <a class="yt-timestamp" data-t="01:43:55">[01:43:55]</a>. This centralization of AI inference could lead to a post-scarcity world where humans engage in work out of interest rather than financial necessity <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>.