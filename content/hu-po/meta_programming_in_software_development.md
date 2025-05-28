---
title: meta programming in software development
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

[[meta_gpt_multi_agent_collaborative_framework | MetaGPT]], a GitHub repository, has garnered significant attention, accumulating over 20,000 stars and maintaining a top trending position <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This project introduces a framework that incorporates human workflows as a [[meta_gpt_multi_agent_collaborative_framework | metaprogramming]] approach for multi-agent collaboration <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

## What is Metaprogramming?

[[meta_gpt_multi_agent_collaborative_framework | Metaprogramming]] refers to programming "the level above" normal programming <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Similar concepts include "metagaming" (playing the game of playing a game) and "meta-learning" (learning how to learn) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. In the context of MetaGPT, it aims to encode standard operating procedures (SOPs) into prompts to enhance structured coordination among [[exploring_functionality_and_limitations_of_aidriven_coding_tools | AI]] agents <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## MetaGPT's Approach

MetaGPT utilizes an "assembly line paradigm" to assign diverse roles to various agents, mirroring human software development teams <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This approach aims to:
*   Decompose high-level tasks into detailed, actionable components <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   Empower agents with domain expertise comparable to human professionals <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   Validate outputs and minimize compounded errors <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

The framework's design is organized into two distinct layers <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>:

1.  **Foundational Component Layer**: Provides essential functionalities for agent operations and system-wide communication. It includes:
    *   **Environment**: A shared workspace for communication <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
    *   **Memory**: Stores and retrieves historical messages <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.
    *   **Roles**: Encapsulate domain-specific skills and workflows <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>.
    *   **Actions**: Executes modular subtasks <a class="yt-timestamp" data-t="00:31:48">[00:31:48]</a>.
    *   **Tools**: Provide common services and utilities <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>.
2.  **Collaboration Layer**: Facilitates agent coordination through knowledge sharing and workflow encapsulation <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>. Agents exchange information effectively, contributing to a shared knowledge base <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>.

Agents within MetaGPT, referred to as "anchor agents," are guided by specialized role prompts (e.g., Engineer, Product Manager). These roles possess capabilities such as thinking, reflection, and knowledge accumulation, interacting with the environment via "pub-sub" (publish-subscribe) methods <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

## Mimicking Human Software Teams

MetaGPT is designed to handle complex tasks and promote clear role delineations, mirroring the traditional "waterfall method" of software development <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. The roles mimicked by MetaGPT agents include <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>:
*   **Product Manager (Alice)**: Defines requirements and creates product requirement documents (PRDs) <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Architect (Bob)**: Determines the system design <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.
*   **Project Manager**: Breaks down tasks and outlines steps <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Engineer**: Writes code <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
*   **QA Engineer**: Tests the code and validates outputs <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

A task, such as "write a classic and simple Flappy Bird game," is fed into the system, which then produces the final code <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>.

## Practical Application and Critique

To evaluate MetaGPT, the speaker provided it with the task: "Write a Gradio front end for a robotic AI cat toy" <a class="yt-timestamp" data-t="00:39:58">[00:39:58]</a>.

### Generated Documents and Design
*   **Product Requirement Document (PRD)**: Created by the Product Manager agent, it included user stories, proposed names (Robocat, Play Purr), and a competitive analysis quadrant chart comparing the proposed product to competitors based on "user friendly" and "feature rich" axes <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. The speaker found these axes "meaningless" as no company desires "less user friendly" or "less feature rich" <a class="yt-timestamp" data-t="00:44:39">[00:44:39]</a>.
*   **System Design Document**: Created by the Architect agent, it proposed using [[Rust_programming_language | Gradio]] for the frontend and Flask for the backend <a class="yt-timestamp" data-t="00:48:10">[00:48:10]</a>. The speaker questioned the choice of Flask, considering it overkill for a local Raspberry Pi project <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>. The file organization and API schema definitions were noted as "arbitrary and basic" and "bare bones" <a class="yt-timestamp" data-t="00:49:35">[00:49:35]</a>.
*   **Task List**: Created by the Project Manager agent, it suggested "no third-party packages required," which was surprising given the robotics context, as it didn't mention any common robotics frameworks or libraries <a class="yt-timestamp" data-t="00:55:42">[00:55:42]</a>.

### Code Quality and Efficacy
The generated code was criticized for being "nonsense" and "primitive" <a class="yt-timestamp" data-t="00:57:40">[00:57:40]</a>. Issues included:
*   Arbitrary object structures <a class="yt-timestamp" data-t="00:58:09">[00:58:09]</a>.
*   Inconsistent time formats (string vs. `datetime` objects) <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.
*   Pointless utility functions that merely wrapped existing Python functionalities <a class="yt-timestamp" data-t="01:07:51">[01:07:51]</a>.
*   Syntactical errors (missing `requests` import in Flask code) <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.
*   Unorthodox Flask routing that could lead to issues <a class="yt-timestamp" data-t="01:15:27">[01:15:27]</a>.
*   Potential port conflicts due to multiple Gradio interfaces and Flask <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.
*   Lack of error handling <a class="yt-timestamp" data-t="01:16:29">[01:16:29]</a>.

Furthermore, the QA Engineer stage, responsible for generating test files, appeared to be missing from the MetaGPT output <a class="yt-timestamp" data-t="01:11:18">[01:11:18]</a>.

### [[comparison_of_direct_coding_prompts_to_multi_agent_frameworks | Comparison with Direct LLM Prompting]]
A key finding was that directly asking [[metas_codellama_model_overview | GPT-4]] (or Claude or Bard) to create the Gradio interface yielded a functional and more specific piece of code with significantly fewer tokens <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. This led to the conclusion that the multi-agent system, with its numerous documentation steps, might introduce "overly verbose non-specific things" that confuse the engineer agent, resulting in less functional code <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.

### Evaluation Benchmarks
MetaGPT was evaluated using HumanEval and MBPP benchmarks <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a>.
*   **HumanEval**: A problem-solving dataset for synthesizing programs from docstrings, similar to LeetCode <a class="yt-timestamp" data-t="01:34:56">[01:34:56]</a>.
*   **MBPP (Mostly Basic Python Problems)**: A dataset of 1,000 crowdsourced Python problems solvable by entry-level programmers <a class="yt-timestamp" data-t="01:35:32">[01:35:32]</a>.

The speaker noted that these benchmarks assess the ability to write individual functions rather than complex system design, which MetaGPT claims to address <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>. Despite MetaGPT purportedly outperforming GPT-4 on these benchmarks, the speaker expressed skepticism, suggesting that MetaGPT's higher token usage for generating extensive context might artificially inflate its performance on these simple function-writing tasks <a class="yt-timestamp" data-t="01:37:30">[01:37:30]</a>.

### Implications for Software Engineering
The observations led to a broader commentary on the [[limitations_of_traditional_software_engineering_roles | limitations of traditional software engineering roles]] and large, hierarchical organizations <a class="yt-timestamp" data-t="01:40:56">[01:40:56]</a>. The speaker argued that roles like product managers, architects, and project managers, who often no longer write code, might introduce unnecessary bureaucracy and "pointless" documentation, leading to less effective software development <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. This perspective suggests that smaller, more agile teams with engineers directly involved in all stages of product creation might be more efficient <a class="yt-timestamp" data-t="01:59:03">[01:59:03]</a>.

The overall sentiment was that while the concept of a multi-agent system mimicking a software company is interesting, its current implementation in MetaGPT generates overly verbose and often incorrect code, suggesting that direct prompting of advanced LLMs remains more effective for many coding tasks <a class="yt-timestamp" data-t="01:56:57">[01:56:57]</a>.