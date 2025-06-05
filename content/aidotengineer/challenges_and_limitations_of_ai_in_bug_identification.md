---
title: Challenges and limitations of AI in bug identification
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen a surge in popularity, leading to questions about their efficacy in finding and fixing bugs and their reliability for software maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores the current state of AI agents in bug detection, highlighting existing limitations and the [[challenges_in_ai_agent_development | challenges in AI agent development]] for this critical area of software development.

## The Software Development Life Cycle (SDLC) and AI Coverage

While existing benchmarks measure the effectiveness of Large Language Models (LLMs) for writing code (e.g., Human Evaluator, Polyglot Benchmark, Live Codebench), this only covers one part of the SDLC <a class="yt-timestamp" data-t="01:23:23">[01:23:23]</a>. Other crucial stages, such as initial scoping and planning (requiring broader business context and system knowledge) <a class="yt-timestamp" data-t="01:40:41">[01:40:41]</a>, and deployment (involving configuration, monitoring, and integration) <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>, are distinct tasks.

Of particular focus is the software maintenance phase, which includes bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>. This area, along with the code review process, is largely unbenchmarked by existing work, despite the increasing presence of LLM-based tools in these spaces <a class="yt-timestamp" data-t="02:04:14">[02:04:14]</a>.

## The Nature of Software Maintenance and Bug Finding

Software maintenance tasks, though still involving code writing, differ significantly from feature development <a class="yt-timestamp" data-t="02:39:07">[02:39:07]</a>. The ability to deeply reason through a codebase to find bugs directly relates to understanding system architecture and its connectedness <a class="yt-timestamp" data-t="02:48:58">[02:48:58]</a>. In fact, finding bugs often requires a deeper understanding of the system than when the feature was originally written <a class="yt-timestamp" data-t="03:09:02">[03:09:02]</a>.

### Observed Challenges for AI Agents in Bug Identification

Maintenance requires the AI to first deeply reason through a system and identify potential bugs <a class="yt-timestamp" data-t="03:16:11">[03:16:11]</a>. However, agents exhibit several [[challenges_in_ai_agent_development | challenges in AI agent development]]:

*   **Holistic Evaluation Issues**: AI agents struggle with a holistic evaluation of files and systems, typically finding only subsets of bugs per run <a class="yt-timestamp" data-t="03:21:05">[03:21:05]</a>.
*   **Narrow Reasoning**: Even with thinking models, reasoning appears somewhat narrow, exploring a limited number of potential avenues at a single time <a class="yt-timestamp" data-t="03:26:01">[03:26:01]</a>. This leads to LLMs missing bugs human developers would immediately pick up and confirming bugs human developers would immediately discard <a class="yt-timestamp" data-t="03:33:41">[03:33:41]</a>.
*   **Simplicity of Patches**: While agents usually manage to patch identified bugs with little effort, this is often because the bugs themselves are not particularly complex <a class="yt-timestamp" data-t="03:47:29">[03:47:29]</a>.

## Limitations of Existing Bug Detection Benchmarks

Current bug detection benchmarks from the software security space are not suitable for evaluating agentic AI systems, as they were built for classic static analysis or program repair tools <a class="yt-timestamp" data-t="04:00:03">[04:00:03]</a>. Their limitations include:

*   **Simplistic Bugs**: They focus on relatively simplistic bugs in common patterns (e.g., null pointer dereferences, buffer overflows, SQL injection), which can often be found statically <a class="yt-timestamp" data-t="04:16:10">[04:16:10]</a>.
*   **Language Limitations**: Many benchmarks are limited to specific languages, like Java, where a vast majority of enterprise software was traditionally written <a class="yt-timestamp" data-t="04:29:05">[04:29:05]</a>.
*   **Security Bias**: There's a bias towards security issues, largely due to the focus of classic static analysis tools, despite bugs appearing in many other forms (e.g., copy-paste bugs that break software for end-users) <a class="yt-timestamp" data-t="04:46:04">[04:46:04]</a>.

## The SM-100 Benchmark: A New Approach

Bismouth developed the SM-100 benchmark to specifically measure how good software agents are at coding tasks outside of normal feature development <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>.

### Benchmark Methodology

The SM-100 benchmark involves:
*   **Curated Bug Set**: 100 triaged, validated, and classified bugs from over 84 public open-source repositories <a class="yt-timestamp" data-t="05:11:32">[05:11:32]</a>. These are remediated real-world bugs <a class="yt-timestamp" data-t="05:19:02">[05:19:02]</a>.
*   **Issue Variety**: The bugs range from those requiring obvious low-specific domain knowledge to senior staff-level engineering knowledge <a class="yt-timestamp" data-t="05:28:13">[05:28:13]</a>.
*   **Multi-Language Focus**: Includes Python, TypeScript, JavaScript, and Go, chosen to evaluate performance across popular and lower-level systems languages <a class="yt-timestamp" data-t="05:39:07">[05:39:07]</a>.
*   **Objective Bugs**: Focuses on explicit security or logical issues that could cause data loss or system crashes, explicitly excluding ambiguous issues like feature requests, optimizations, style formatting, or design decisions <a class="yt-timestamp" data-t="06:04:10">[06:04:10]</a>.
*   **Metadata Annotation**: Each bug is annotated with metadata including severity, context, required human domain knowledge, difficulty to find, and the bug's implication (data loss, crash, security exploit) <a class="yt-timestamp" data-t="07:00:36">[07:00:36]</a>. This helps understand what level of bugs AI agents can regularly find <a class="yt-timestamp" data-t="07:25:01">[07:25:01]</a>.

### Key Metrics Measured

For each system benchmarked, SM-100 assesses four key areas:
1.  **Needle in a Haystack**: Can the system discover bugs without prior knowledge? <a class="yt-timestamp" data-t="07:55:04">[07:55:04]</a> To manage large repositories, agents are given a reduced list of files within likely inter-related subsystems, rather than the entire codebase <a class="yt-timestamp" data-t="09:36:20">[09:36:20]</a>.
2.  **False Positive Rate**: A manual measurement of incorrect bug reports to gauge overall effectiveness <a class="yt-timestamp" data-t="08:08:08">[08:08:08]</a>.
3.  **Bug Introduction Detection**: Can the system find the bug at the time of its introduction (e.g., given the pull request or commit)? <a class="yt-timestamp" data-t="08:24:06">[08:24:06]</a>
4.  **Remediation Suggestions**: For each discovered bug, can the agent fix it without breaking other parts of the codebase? <a class="yt-timestamp" data-t="08:50:49">[08:50:49]</a>

## Performance and Observed Limitations

Building a good agent for identifying bugs and working on code is challenging, requiring a combination of model, system, prompting, information feeding, and navigation strategy <a class="yt-timestamp" data-t="11:07:35">[11:07:35]</a>.

### Comparative Performance on SM-100

*   **Needle in a Haystack**: Bismouth led by finding 10 out of 100 bugs, with the next best solution finding seven <a class="yt-timestamp" data-t="11:23:07">[11:23:07]</a>.
*   **True Positive Rate**: Codeex achieved the highest at 45%, followed by Bismouth at 25%, and Claude Code at 16% <a class="yt-timestamp" data-t="11:46:17">[11:46:17]</a>. These solutions show tighter scoping with significantly less "random nonsense" reports <a class="yt-timestamp" data-t="11:57:02">[11:57:02]</a>.
*   **PR Review (Needle in Haystack)**: Codeex was strong at 27%, then Devon at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="12:23:44">[12:23:44]</a>. Even the best model only found about a third of the bugs, indicating a long way to go <a class="yt-timestamp" data-t="12:43:08">[12:43:08]</a>.

### Basic Agents and Open-Source Models

Basic agents (simple loops with shell tools) often have a 97% false positive rate <a class="yt-timestamp" data-t="10:53:13">[10:53:13]</a>. Open-source models showed significant [[challenges_in_ai_development | challenges in AI development]] in this space:
*   R1 had a 1% true positive rate <a class="yt-timestamp" data-t="13:30:17">[13:30:17]</a>.
*   Llama Maverick had a 2% true positive rate <a class="yt-timestamp" data-t="13:38:09">[13:38:09]</a>.
*   Sonnet 4 found 6 bugs with a 3% true positive rate <a class="yt-timestamp" data-t="13:46:05">[13:46:05]</a>.
*   03 found 2 bugs with a 6% true positive rate <a class="yt-timestamp" data-t="13:46:05">[13:46:05]</a>.

The highest popular agent score for complex bugs was 7% on SM-100, meaning most used agents are currently the worst at finding and fixing complex bugs <a class="yt-timestamp" data-t="13:59:01">[13:59:01]</a>. Many agents report a massive number of issues with very low true positive rates (e.g., 70 reports for one issue from a single agent), making them impractical for engineers <a class="yt-timestamp" data-t="14:26:07">[14:26:07]</a>. Simple bugs are also often missed; for example, only Bismouth and Codeex found a state issue that prevents a form from clearing after submission <a class="yt-timestamp" data-t="14:59:17">[14:59:17]</a>.

### Fundamental Challenges

A notable commonality among agents is their **narrow thinking** <a class="yt-timestamp" data-t="15:38:01">[15:38:01]</a>. Even with thinking models, they are narrow in their evaluation and don't go deep enough <a class="yt-timestamp" data-t="15:42:01">[15:42:01]</a>. The total number of bugs found per run remains consistent, but the *specific* bugs change, indicating that LLMs are not holistically inventorying everything in a file <a class="yt-timestamp" data-t="16:08:04">[16:08:04]</a>. Different biases seem to cause models to view files in different ways on different runs <a class="yt-timestamp" data-t="16:26:02">[16:26:02]</a>.

Despite high scores on benchmarks like Sweet Edenge (60-80%), agents struggle significantly with SM-100 <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>. This suggests that while existing agents can create software upfront, managing and fixing it after deployment remains a major challenge <a class="yt-timestamp" data-t="16:55:02">[16:55:02]</a>.

## Required Improvements for AI Agents

Addressing these [[challenges_in_ai_agent_development | challenges in AI agent development]] for bug identification demands:
*   **Targeted Search** <a class="yt-timestamp" data-t="17:09:47">[17:09:47]</a>
*   **Better Program Comprehension** <a class="yt-timestamp" data-t="17:12:12">[17:12:12]</a>
*   **Cross-File Reasoning** <a class="yt-timestamp" data-t="17:13:30">[17:13:30]</a>
*   **Deeper Bug Pattern Recognition** <a class="yt-timestamp" data-t="17:14:28">[17:14:28]</a>

## Conclusion

The most frequently used agents today carry a high risk of introducing bugs <a class="yt-timestamp" data-t="17:44:03">[17:44:03]</a>. However, newer agents, including Bismouth and Codeex, are beginning to show an increased ability to reason through code and more effectively use context to evaluate concerns <a class="yt-timestamp" data-t="17:49:03">[17:49:03]</a>. While the capability is still in its infancy <a class="yt-timestamp" data-t="03:43:08">[03:43:08]</a>, progress is encouraging, and improvements in this area will have broad benefits across the software industry <a class="yt-timestamp" data-t="18:01:04">[18:01:04]</a>.