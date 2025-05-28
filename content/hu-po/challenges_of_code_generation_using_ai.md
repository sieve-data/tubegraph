---
title: Challenges of code generation using AI
videoId: tFwYD1UPIfM
---

From: [[hu-po]] <br/> 

The field of automated task solving through multi-agent systems driven by large language models (LLMs) has seen significant progress <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. However, existing LLM-based multi-agent systems often struggle with complex tasks due to issues like hallucination <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

## LLM Hallucination and Cascading Errors
A primary [[challenges_in_evaluating_AIgenerated_research | challenge]] in complex AI code generation is the "LLM hallucination problem" <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This refers to LLMs generating incorrect or nonsensical information <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. When these hallucinations are fed into other LLMs within a multi-agent framework, they can create a cascading effect, leading to the entire system spouting nonsense and failing to address complex problems effectively <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. This issue is akin to the "dagger in RL" problem in reinforcement learning, where going off-policy leads to random actions or hallucinations <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## MetaGPT's Proposed Solution
MetaGPT, an innovative framework, attempts to mitigate these issues by incorporating efficient human workflows as a metaprogramming approach <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. It encodes standard operating procedures (SOPs) into prompts to enhance structured coordination <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. The framework assigns diverse roles to various agents, mirroring a human software development team's assembly line paradigm, to validate outputs and minimize compounded errors <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. Each agent, such as a product manager, architect, project manager, engineer, and QA engineer, is prompted to "pretend to be" a specific archetype and perform distinct tasks <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.

### MetaGPT Framework Components
The MetaGPT framework is organized into two layers <a class="yt-timestamp" data-t="00:30:52">[00:30:52]</a>:
1.  **Foundational Component Layer:** Includes elements essential for agent operations and system-wide communication <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>:
    *   **Environment:** Enables shared workspace and communication <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
    *   **Memory:** Stores and retrieves historical messages <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.
    *   **Roles:** Encapsulate domain-specific skills and workflows <a class="yt-timestamp" data-t="00:31:46">[00:31:46]</a>, defined by "anchor agents" with specialized role prompts <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.
    *   **Actions:** Execute modular subtasks <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.
    *   **Tools:** Provide common services and utilities <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
2.  **Collaboration Layer:** Facilitates agent coordination through knowledge sharing and workflow encapsulation <a class="yt-timestamp" data-t="00:33:48">[00:33:48]</a>. This layer allows agents to exchange information effectively, contributing to a shared knowledge base <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. Agents interact with the environment using subscription and publication methods, similar to a pub-sub messaging framework <a class="yt-timestamp" data-t="00:34:24">[00:34:24]</a>.

## Limitations and Criticisms of Multi-Agent Code Generation
Despite its theoretical advantages, practical application of MetaGPT for code generation reveals several [[challenges_and_improvements_in_animated_AI_models | challenges]] and limitations:

### Overly Verbose and Non-Specific Output
When tasked with generating a Gradio frontend for a robotic AI cat toy, MetaGPT produced:
*   **Product Requirement Document (PRD):** Included generic requirements and superficial competitive analysis, such as a "quadrant chart" with meaningless axes like "more user-friendly" versus "less user-friendly" <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.
*   **System Design:** The architect's output included the use of Flask for a backend, which was considered overkill for a local project <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>. File structures were arbitrary, separated by requirement rather than dependency <a class="yt-timestamp" data-t="00:49:38">[00:49:38]</a>. API specs were bare bones and "kind of nonsense," using vague terms like "control params" or "schedule params" <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>. Sequence flow diagrams were criticized as meaningless, showing "thing one does thing one, returns thing one answer" <a class="yt-timestamp" data-t="00:51:16">[00:51:16]</a>.
*   **Code Generation:** The engineer's code was largely "nonsense," using arbitrary objects and lacking error checking or smart defaults <a class="yt-timestamp" data-t="00:57:40">[00:57:40]</a>. It failed to use consistent time formats and created pointless "static methods" <a class="yt-timestamp" data-t="01:06:57">[01:06:57]</a>. The generated Flask code was syntactically incorrect (missing imports) and had unorthodox design choices, like defining routes inside a class's `__init__` function <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.
*   **Missing Outputs:** The QA engineer role, expected to create test files, did not produce any visible test file <a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

### Cost and Efficiency Concerns
The execution of the MetaGPT demo to generate code cost about 87 cents in tokens <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>, using tens of thousands of tokens <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>. In contrast, a direct query to ChatGPT with a simple prompt generated a more functional and usable Gradio interface for "significantly less amount of tokens" (estimated 100-500 tokens) <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>. This suggests that the multi-agent framework might be an "extra way to waste your tokens" without providing superior results <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.

### Inappropriate Benchmarking
MetaGPT's evaluation uses benchmarks like HumanEval and MBPP <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a>. These benchmarks primarily evaluate the ability to write individual functions from docstrings, akin to "simple coding benchmarks" or "LeetCode" problems <a class="yt-timestamp" data-t="01:35:07">[01:35:07]</a>. However, they do not assess "system design" or the creation of entire software products <a class="yt-timestamp" data-t="01:36:34">[01:36:34]</a>. This misalignment suggests the benchmarks are not fully representative of the complex, multi-role software engineering tasks MetaGPT claims to address <a class="yt-timestamp" data-t="01:58:08">[01:58:08]</a>. The claim that MetaGPT outperforms GPT-4 on these benchmarks despite generating less usable code when directly tested raises questions about the evaluation methodology <a class="yt-timestamp" data-t="01:38:11">[01:38:11]</a>.

### Industry Implications
The observed inefficiencies in AI code generation through simulated multi-agent structures prompt a critical look at real-world software engineering organizations <a class="yt-timestamp" data-t="01:58:49">[01:58:49]</a>. If direct prompting of an LLM yields better code than a complex, multi-stage AI process, it raises questions about the necessity and effectiveness of highly specialized roles and waterfall methodologies in human-led software development <a class="yt-timestamp" data-t="01:59:07">[01:59:07]</a>. The argument is made that such structures might be more a result of historical legacy, bureaucracy, and compensation models rather than optimal code creation strategies <a class="yt-timestamp" data-t="01:59:50">[01:59:50]</a>.

It is suggested that an iterative approach, where the LLM can critically review and refine its code multiple times, might yield better results than a single pass through a complex multi-agent system <a class="yt-timestamp" data-t="01:18:10">[01:18:10]</a>.