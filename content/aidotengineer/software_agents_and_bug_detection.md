---
title: Software agents and bug detection
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

[[AI agents in DevOps | AI agents for software engineering]] have seen a surge in popularity over the past year, prompting investigation into their effectiveness at finding and fixing bugs, and their reliability for software maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Bismouth's Background
Bismouth has been working on software agents for over a year <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Ian (CEO)**: Background in data engineering, machine learning, and search, previously at Zillow on the A/B testing platform. This is his second time working on dev tooling startups, having started with technical documentation search in 2019 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   **Nick (CTO)**: Primarily worked in the software security space before Bismouth, previously at Google on an internal tools team building endpoint security software, and as a research scientist focused on detecting software exploitation <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Many tools and techniques from the security space are transferable to building intelligent agentic code tools <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

## The Problem: Gaps in Existing Benchmarks
While several benchmarks exist to measure how effective Large Language Models (LLMs) are for writing code (e.g., Human Evaluator, Polyglot Benchmark, Live Codebench), these primarily cover feature development and testing, which is only one part of the software development life cycle (SDLC) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Other crucial SDLC stages are often overlooked:
*   **Initial Scoping and Planning**: Requires broader business context, knowledge of existing systems and designs, and exploration of potential solutions. This is a distinct task from development <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Code Review**: Largely unbenchmarked, despite the rise of LLM-based tools in this area <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Deployment**: A separate task involving configuration, monitoring setup, and integration with existing systems <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Software Maintenance Tasks**: Includes bug fixes, dependency upgrades, and migrations. While still involving code writing, it differs significantly from feature development <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The ability to deeply reason through a codebase to find bugs is directly transferable to producing features, as both require an understanding of the system architecture and its connectedness <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Challenges with AI Agent Reasoning for Bugs
Maintenance often requires a deeper understanding of the system than when the feature was originally written <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   [[semantic_and_behavioral_evaluation_of_agents | Agents struggle with holistic evaluation of files and systems]], often finding only subsets of bugs per run <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   Even with "thinking models," reasoning can be narrow, exploring a limited number of avenues at a time <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. This leads to LLMs missing bugs that human developers would immediately spot, and confirming false bugs <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   While agents often patch simple bugs with ease due to their simplicity, this doesn't indicate a high level of capability for complex issues <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Limitations of Existing Bug Detection Benchmarks
Existing bug detection benchmarks from the software security space are not suitable for [[evaluating_ai_agents_and_assistants | new agentic AI systems]] because they were built for classic static analysis or program repair tools <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Simplicity**: They focus on simplistic bugs in common patterns (e.g., null pointer dereferences, buffer overflows, SQL injection), which can often be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Language Limitations**: Many are limited to specific languages, like Java, due to its prevalence in enterprise software <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Security Bias**: A bias towards security issues exists, largely because classic static analysis tools focused on this area. However, bugs appear in many ways beyond security defects, such as copy-paste errors that break software for end-users <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Bismouth's SM100 Benchmark
To address these limitations, Bismouth developed the SM100 benchmark <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Dataset**: 100 triaged, validated, and classified bugs were painstakingly gathered from over 84 public repositories <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. These are remediated "in the wild" bugs from open-source projects, spanning a range of issue types from obvious low-domain knowledge to senior staff-level engineering knowledge <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Multi-language Focus**: The benchmark includes Python, TypeScript, JavaScript (due to popularity and LLM performance), and Go (as a control for low-level systems engineering languages) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Objective Bugs**: Bugs are defined as explicit security issues or logical issues that could cause data loss or system crashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This definition removes ambiguity, harmless issues, or cases where issues are correctly handled by calling code higher up <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The benchmark explicitly excludes feature requests, optimizations, style formatting, or design decisions to reduce ambiguity and ensure reproducibility <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Metadata Annotation**: Each bug is annotated with metadata, including its severity, context, required human domain knowledge, difficulty to find, and its implication (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This helps understand what level of bugs [[multiagent_systems_and_their_applications | AI agents]] can regularly find <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. While agents occasionally find zero-day exploits, this usually requires many runs over the same context <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

## SM100 Evaluation Metrics
For each system benchmarked, four key numbers are derived:
1.  **Needle in the Haystack Result**: Measures if the system can discover bugs without any prior knowledge <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   **Methodology**: Repositories are broken into subsystems of interrelated files (e.g., a front-end part or specific API). The list of files in subsystems that were modified in the "golden PR commit" (the commit that introduced the bug) are fed to the LLM. This reduces the search scope without biasing the agent about the specific bug <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
2.  **False Positive Rate**: Manually measured to assess the overall effectiveness of the system's bug reports <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  **Time of Introduction**: Evaluates if the system can find the bug when given the pull request or commit that introduced it. Here, the agent has more immediate context and doesn't need to search as widely <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
4.  **Remediation Suggestion**: For each discovered bug, the agent is asked to fix it, and the result is checked to ensure it fixes the bug without breaking other codebase parts <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

## Building Effective Agents for Bug Detection
Basic agent implementations (e.g., a simple loop with shell, search/replace, report, finish tools) are trivial <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. While they might find some bugs (Bismouth found 5-6 in a basic loop), they suffer from an extremely high false positive rate (97%) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Most basic agents, equipped with tools from Anthropic or OpenAI model card releases, are not up to the task of truly finding and triaging bugs <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

Building a good agent for identifying bugs and working on code is challenging, requiring a combination of:
*   Model <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>
*   System <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>
*   Prompting <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>
*   Information <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>
*   The way information is fed to the model <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>
*   Navigation strategy <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Benchmark Performance Comparisons
Bismouth's performance is often based on Anthropic models, which are easier to serve for their customers from Vertex <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

*   **Needle in a Haystack**: Bismouth leads by finding 10 out of 100 "needles," with the next best solution finding 7 <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
*   **True Positive Rate (Detection)**: Codeex performs highest at 45%, Bismouth at 25%, and Claude Code at 16% <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. These three solutions also exhibit significantly less "random nonsense" compared to others <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **False Positives**: Devin, Cursor Agent, and CoSign reported between 900 and 1300 items with only a 3-10% true positive rate, indicating a need for improvement in tightening their output scope <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. One agent even gave 70 reports for a single issue, which is impractical for human engineers to sift through <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **PR Review (Needle in a Haystack)**: Codeex was strong at 27%, followed by Devin at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. These numbers do not include false positives <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Performance of Basic and Open-Source Agents
Open-source models have a long way to go <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   R1 had a 1% true positive rate <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   Lava Maverick had a 2% true positive rate <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   R1 managed to find one needle in a haystack <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   Sonnet 4 found six needles, and 03 found two, with 3% and 6% true positive rates respectively in a basic loop <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   The highest popular agent score (outside Bismouth) was 7% on SM100 <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This indicates that most widely used agents are currently poor at finding and fixing complex bugs <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

Some simple bugs are still missed; for instance, only Bismouth and Codeex found a state issue where a form's "is dirty" flag was not reset, preventing it from clearing after submission <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. This type of bug, though not critical, affects user experience and would be immediately caught by a human developer <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Key Challenges and Future Outlook
A notable commonality among agents is their narrow thinking, even when using thinking models <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. They don't go deep enough in their evaluations <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   **Requirement**: Broader thinking chains and deeper thinking along selected chains are needed to effectively find bugs <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
*   **Inconsistency**: The total number of bugs found remains roughly consistent per run, but the specific bugs found change, indicating that LLMs are not holistically inventorying everything in a file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This pervasive problem across the industry suggests models apply different biases or contexts with each run <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>.

Despite scores of 60-80% on other benchmarks like Sweet Edenge, agents still struggle with SM100 <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This implies that while existing agents can create software upfront, managing and fixing deployed software remains a major challenge <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. This requires targeted search, better program comprehension, cross-file reasoning, and bug pattern recognition, which are currently lacking in depth <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

While the current state indicates that most frequently used agents carry a high risk of introducing bugs <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>, newer agents like Codeex and Bismouth are showing improvements in tighter, more narrow bands of bug solving and handling complex issues <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. The stability of these newer agents is nascent but encouraging, showing an increased ability to reason through code and effectively use context <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This benchmark aims to clearly demonstrate progress and highlight that effort and different techniques can lead to significant improvements across the industry <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.