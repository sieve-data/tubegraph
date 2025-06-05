---
title: Comparison of AI tools in code analysis
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

[[Impact of AI coding agents on software engineering | AI agents for software engineering]] have seen a surge in popularity over the last year, prompting investigations into their efficacy for identifying and resolving bugs <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article details the findings from Bismouth, a company specializing in software agents, regarding how well these tools perform at maintenance tasks like bug finding and fixing <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## The SM-100 Benchmark

Bismouth developed a comprehensive benchmark, named SM-100, over several months to evaluate the capabilities of software agents in coding tasks beyond typical feature development <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Existing benchmarks primarily focus on how effective Large Language Models (LLMs) are at writing code, such as Human Eval, Polyglot Benchmark, and Live Codebench <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. However, these only cover a fraction of the Software Development Life Cycle (SDLC) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### Limitations of Existing Benchmarks
Traditional bug detection benchmarks from the software security space, designed for classic static analysis or program repair tools, have significant limitations for evaluating modern [[impact_of_ai_coding_agents_on_software_engineering | agentic AI systems]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>:
*   **Simplistic Bugs**: They often focus on straightforward bugs in common patterns, like null pointer dereferences, buffer overflows, or SQL injection, which can be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Limited Languages**: Many are restricted to languages like Java, reflecting where much complex enterprise software was historically written <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Security Bias**: There's a bias towards security issues because classic static analysis tools historically focused on this area <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. However, bugs manifest in many forms beyond security defects, such as copy-paste errors that break user experience without necessarily being security vulnerabilities <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### Scope of SM-100
The SM-100 benchmark extends evaluation to other critical parts of the SDLC <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>:
*   **Code Review**: This crucial process is largely unbenchmarked by existing work, despite the rise of LLM-based tools in the space <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Software Maintenance**: This includes tasks like bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. While still involving code writing, it differs from feature development by requiring deep reasoning through a codebase to identify potential bugs <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Finding bugs requires an understanding of system architecture and connectedness, sometimes even deeper than when the feature was originally written <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

The SM-100 benchmark includes 100 validated and classified bugs from over 84 public repositories, representing real-world issues in open-source projects <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

The bugs are categorized by difficulty, ranging from obvious issues requiring low domain knowledge to complex problems demanding senior staff-level engineering understanding <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The benchmark is also multi-language, focusing on Python, TypeScript, JavaScript, and Go, as LLMs show varying performance across languages <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Defining "Objective Bugs"
The benchmark focuses on "objective bugs," defined as explicit security or logical issues that could lead to data loss or system crashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This strict definition avoids ambiguity and harmless issues <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

[!NOTE]
Issues explicitly *not* included are feature requests, optimizations, style formatting, or design decisions, as these are often subjective and debated even among humans <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

Each bug in the SM-100 is annotated with metadata, including:
*   Severity <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
*   Context where it was defined and called <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
*   Required system-specific domain knowledge for a human to find it <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
*   Difficulty of finding it, even with expert knowledge <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>
*   Implication of the bug (data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>

### Benchmark Metrics
The SM-100 benchmark measures four key aspects of an agent's performance <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>:
1.  **Needle in the Haystack**: The ability to discover bugs without any prior knowledge <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. To avoid biasing agents, the repositories are broken into subsystems, and the agent is fed files only from relevant subsystems (those modified in the original bug-introducing commit), rather than the entire repository <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
2.  **False Positive Rate**: The rate of incorrect bug identifications from the agent's output <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
3.  **Finding at Introduction**: Whether the agent can identify a bug given the pull request (PR) or commit that introduced it <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This gives the agent more immediate context <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
4.  **Suggesting Remediations**: The ability of the agent to suggest a fix for identified bugs that resolves the issue without breaking other parts of the codebase <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

## Performance Comparison of AI Agents

Building an effective [[testing_and_optimization_of_ai_coding_agents | AI agent for code analysis]] is challenging, requiring a sophisticated combination of model selection, system design, prompting strategies, information feeding, and navigation <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Basic implementations, often using simple tools like `shell`, `tool`, `sir`, `replace`, `think`, and `report bug` in a loop, can find some bugs but typically have an extremely high false positive rate (e.g., 97%) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

### Leading Solutions
*   **Bismouth**: Leads in the "needle in a haystack" metric, finding 10 out of the 100 test bugs <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. It achieved a 25% true positive rate in bug detection <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Bismouth's solution, often running on Anthropic models, has outperformed Anthropic's own Claude Code in multiple categories <a class="yt-timestamp" data-t="00:12:56">[00:13:15]</a>.
*   **Codeex**: Achieved the highest true positive rate in bug detection at 45% <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. It was also strong in PR review, finding 27% of "needle in a haystack" bugs <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Claude Code**: Showed a 16% true positive rate in bug detection <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
*   **Devon**: Found 21% of "needle in a haystack" bugs in PR review <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.
*   **Cursor Agent** and **Cosign**: Along with Devon, these agents reported between 900 and 1,300 items, but with low true positive rates (3-10%) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

### Basic Agents and Open-Source Models
The performance of basic agents and open-source models is significantly lower <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>:
*   **DeepSec R1**: 1% true positive rate over hundreds of bugs <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **Llama for Maverick**: 2% true positive rate <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   **Sonnet 4 (in a loop)**: Found 6 "needle in a haystack" bugs with a 3% true positive rate <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   **03 (in a loop)**: Found 2 "needle in a haystack" bugs with a 6% true positive rate <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

[!WARNING]
The highest popular agent score (excluding Bismouth) on the SM-100 was 7% <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This indicates that the most widely used agents struggle with finding and fixing complex bugs, which represents a significant portion of software engineering work <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

Agents also frequently provide a massive number of reports, making it impractical for human engineers to sift through them <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. For example, one agent gave 70 reports for a single issue <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. This highlights a need for tighter scoping and improved accuracy in agent reporting <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. A simple state issue (a form not clearing) was only found by Bismouth and Codeex, demonstrating that even basic user experience bugs are often missed by other agents <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.

## Common Limitations and Future Directions

A notable commonality across all examined agents is their narrow thinking, even when [[using_reasoning_models_and_tool_calls_in_ai | using thinking models]] <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. They don't delve deep enough into issues, and their reasoning tends to explore only a limited number of avenues at a time <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This leads to agents missing bugs that human developers would quickly identify and confirming issues that humans would immediately discard <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Moreover, agents do not consistently evaluate files holistically; the specific bugs found can vary across different runs, suggesting biases in their contextual evaluation <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

> "Despite 60 to 70% 80% in some cases scores on Sweet Edenge, agents still struggle with SM 100. What does that mean? Existing agents are able to create software upfront, but to manage and fix software after it's been deployed will be a major struggle as far as we see it." <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>

This indicates a significant gap: while some agents excel at initial software creation, they are currently ill-equipped for post-deployment maintenance and bug fixing <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Addressing this problem requires targeted search, enhanced program comprehension, [[using_reasoning_models_and_tool_calls_in_ai | cross-file reasoning]], and advanced bug pattern recognition, capabilities that are currently lacking in depth across many solutions <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

However, newer agents like Codeex and Bismouth are showing promise by offering tighter, more focused bug solutions and demonstrating an increased ability to reason through code and effectively use context <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. The stability of these agents is nascent, but the early results are encouraging <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Continued effort and different [[evolution_of_ai_engineering_and_tools | techniques]] in this area are expected to yield significant benefits across the entire industry <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.