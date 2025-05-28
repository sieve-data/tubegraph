---
title: evaluation of AI coding through benchmarks
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

The evaluation of AI coding capabilities, particularly with the advent of large language models (LLMs) and multi-agent frameworks, is a critical area of research. One such framework, MetaGPT, aims to automate complex software development tasks by mimicking human team structures <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## MetaGPT Framework Overview

MetaGPT, a trending GitHub repository, focuses on leveraging multi-agent systems driven by LLMs for automated task solving <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. It proposes an "assembly line paradigm" where diverse roles, similar to a human software development team, are assigned to various agents <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. This approach aims to decompose high-level tasks into detailed, actionable components handled by distinct roles, thereby facilitating role-specific expertise and coordination <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

The framework is structured into two layers:
1.  **Foundational Component Layer:** Provides core components for agent operations and system-wide communication, including environment, memory, roles, actions, and tools <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>.
2.  **Collaboration Layer:** Facilitates agent coordination through mechanisms like knowledge sharing and workflow encapsulation <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>. Agents possess capabilities such as thinking, reflection, and knowledge accumulation, interacting through a publish-subscribe (pub/sub) messaging framework <a class="yt-timestamp" data-t="00:34:26">[00:34:26]</a>.

### Roles in MetaGPT
MetaGPT encodes standard operating procedures (SOPs) into prompts, defining specific job roles and workflows <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. These roles include:
*   **Product Manager (Alice):** Determines user requirements and creates product requirement documents (PRD) <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Architect (Bob):** Determines the system design based on requirements <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Project Manager:** Determines specific tasks <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
*   **Engineer:** Writes the code <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **QA Engineer:** Creates test files for validation <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

This mirrors the "waterfall method" of software development, where tasks flow sequentially from analysis to delivery <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

## Challenges in [[Benchmarking AI Agents with OSWorld and Web Arena | AI Coding Evaluation]]

A significant challenge in evaluating LLM-based multi-agent systems is the "hallucination problem," where LLMs generate incorrect or nonsensical information <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. In a multi-agent framework, if one LLM hallucinates, it can lead to "cascading" errors, where subsequent LLMs taking that output as input also produce nonsensical results <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

The presenter critiques the traditional waterfall model, suggesting that such a fragmented approach, driven by roles like Product Manager or Architect who may not actively code, can lead to inefficiencies and "overly verbose, non-specific" outputs <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. This implies that the complexity introduced by multiple specialized roles might not always lead to better outcomes for highly capable AI engineers.

## [[AI benchmarks and evaluation | Benchmarks for AI Coding]]

MetaGPT evaluates its performance using two primary benchmarks:
*   **[[AI benchmarks and evaluation | HumanEval]]**: A problem-solving dataset originally from a paper on evaluating LLMs trained on code. It measures functional correctness by synthesizing programs from docstrings, akin to LeetCode problems <a class="yt-timestamp" data-t="01:34:51">[01:34:51]</a>.
*   **[[AI benchmarks and evaluation | MBPP (Mostly Basic Python Problems)]]**: A dataset of 1,000 crowdsourced Python programming problems designed for entry-level programmers, also similar to competitive programming challenges <a class="yt-timestamp" data-t="01:35:26">[01:35:26]</a>.

MetaGPT claims to significantly outperform existing chat-based multi-agent systems, [[comparison_of_language_models_in_coding_tasks | GPT-4]], and Codex on these benchmarks, with a claimed 82.5% success rate on HumanEval and 82.9% on MBPP for pass@1 <a class="yt-timestamp" data-t="01:37:19">[01:37:19]</a>. This implies that MetaGPT's multi-agent approach leads to a higher likelihood of getting the correct answer on the first try <a class="yt-timestamp" data-t="01:39:15">[01:39:15]</a>.

## Critique of MetaGPT's Evaluation and Approach

### Practical Application vs. Benchmarks
Despite the claimed benchmark improvements, a live demonstration of MetaGPT's performance for a complex task (writing a Gradio frontend for a robotic AI cat toy) yielded largely nonsensical and incorrect code <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. In contrast, directly prompting [[comparison_of_language_models_in_coding_tasks | GPT-4]] produced a simpler, working Gradio interface with meaningful parameters like "direction" and "speed" <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. This suggests that while MetaGPT uses significantly more tokens for context (tens of thousands) <a class="yt-timestamp" data-t="01:37:58">[01:37:58]</a>, this elaborate process may lead to "overly verbose and non-specific" code, rather than practical, working solutions <a class="yt-timestamp" data-t="01:12:15">[01:12:15]</a>.

The cost of running MetaGPT for a demo was approximately $0.87, primarily due to the high token usage <a class="yt-timestamp" data-t="01:47:49">[01:47:49]</a>.

### Benchmark Limitations
The benchmarks (HumanEval and MBPP) used by MetaGPT are designed for evaluating the generation of individual functions based on docstrings or simple problem statements <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>. They do not evaluate a system's ability to perform complex system design, build entire products, or handle the iterative refinement process essential in real-world software development <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>. This mismatch between the advertised capabilities of MetaGPT (a full "startup" simulator with business strategy and requirements) and its evaluation methods raises questions about the applicability of its reported success <a class="yt-timestamp" data-t="01:57:56">[01:57:56]</a>.

### [[Selfimprovement in AI models | Iterative Refinement]]
One potential area for improvement in multi-agent AI systems, highlighted by the live demo, is the lack of iterative refinement <a class="yt-timestamp" data-t="01:18:12">[01:18:12]</a>. While LLMs can critically analyze and suggest improvements to code, MetaGPT's process appeared to be a single, sequential pass <a class="yt-timestamp" data-t="01:18:02">[01:18:02]</a>. Incorporating multiple feedback loops where agents continuously refine their outputs could potentially lead to much better results <a class="yt-timestamp" data-t="01:18:38">[01:18:38]</a>.

## Broader Implications for Software Development
The discussion extended to the nature of human software organizations. The presenter argues that the traditional, hierarchical "waterfall" structure with rigidly defined roles (Product Manager, Architect, Project Manager) might be inefficient and contribute to bureaucracy, rather than optimal product creation <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a>. This suggests that if LLMs are simply mimicking these human inefficiencies, then the benefit of multi-agent frameworks like MetaGPT might be limited unless they fundamentally rethink or streamline these processes <a class="yt-timestamp" data-t="01:58:53">[01:58:53]</a>.

Ultimately, the effectiveness of [[benchmarking_ai_agents_with_osworld_and_web_arena | AI coding agents]] may depend on the sophistication of the underlying LLMs and the efficiency of the interaction patterns, rather than merely simulating complex human workflows <a class="yt-timestamp" data-t="01:56:57">[01:56:57]</a>.