---
title: Evaluating AI agents methods and metrics
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen a rapid increase in popularity, prompting investigations into their efficacy for tasks like finding and fixing bugs, and general maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Bismouth, a company specializing in software agents, developed a benchmark to assess these capabilities <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Limitations of Existing AI Evaluation Benchmarks
Existing benchmarks for [[evaluating_ai_system_performance | evaluating AI system performance]] of large language models (LLMs) primarily focus on feature development and code writing <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Examples include Human Evaluators Polyglot benchmark and Live Codebench <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. However, these benchmarks only cover a limited part of the software development life cycle (SDLC) <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Key areas of the SDLC that are not well-covered by existing benchmarks include:
*   **Initial Scoping and Planning** <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>: Requires broader business context, knowledge of existing systems, and exploration of solutions, making it a distinct task from development <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Code Review Process** <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>: Largely unbenchmarked despite the emergence of LLM-based tools in this area <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Deployment** <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>: Involves configuration, monitoring setup, and integration with existing systems <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **Software Maintenance Tasks** <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>: Includes bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This core task, though involving code writing, differs significantly from feature development <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Challenges in AI Agent Evaluation for Maintenance
The ability to deeply reason through a codebase to find bugs is transferable to producing features, as both require understanding system architecture and connectedness <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Often, finding bugs demands an even deeper understanding than original feature creation <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

Current AI agents, even with thinking models, often exhibit narrow reasoning, exploring only a limited number of avenues at a time <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This translates to LLMs missing bugs that human developers would quickly identify, and confirming false positives that humans would discard <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. While patching simple bugs is relatively easy for agents due to their simplicity, this doesn't indicate advanced capability <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Existing bug detection benchmarks from the software security space have significant limitations for [[evaluating_ai_agents_and_assistance | evaluating AI agents]]:
*   **Simplistic Bugs**: They focus on basic bugs like null pointer dereferences, buffer overflows, or SQL injection, which can often be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Limited Languages**: Many are restricted to languages like Java <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Security Bias**: A bias towards security issues neglects other common bug types, such as copy-paste errors, which disrupt software functionality for end-users <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Bismouth's SM-100 Benchmark
Bismouth developed the SM-100 benchmark specifically to address the gaps in [[evaluating_ai_agents_and_assistance | evaluating AI agents]] for software maintenance <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Methodology
The SM-100 benchmark consists of 100 manually triaged, validated, and classified bugs from over 84 public repositories <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. These bugs represent real-world issues already remediated in open-source projects <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

The benchmark aims to provide:
*   **Range of Issue Types**: From obvious issues requiring low specific domain knowledge to senior staff-level engineering knowledge demanding significant project understanding <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Multi-language Support**: Focuses on Python, TypeScript, JavaScript (popular languages where LLMs perform well), and Go (as a control for low-level systems engineering) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Defining an "Objective Bug"
SM-100 defines an "objective bug" as an explicit security issue or logical issue that could cause data loss or system crashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This definition avoids ambiguity and harmless issues or those corrected by higher-level callers <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The benchmark explicitly excludes feature requests, optimizations, style formatting, or design decisions to reduce ambiguity and ensure reproducibility <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

Each bug is annotated with metadata, including:
*   Severity <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
*   Context where it was defined and called <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
*   Amount of system-specific domain knowledge a human would require to find it <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
*   Difficulty of finding it even with the required knowledge <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>
*   Implication of the bug (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>

These classifications help understand which level of bugs AI agents can regularly find <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. While agents occasionally surprise with discoveries like zero-day exploits (e.g., GPT-3 with 100 runs), the benchmark focuses on everyday usage capabilities <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Metrics for [[evaluating_ai_agents_and_assistance | Evaluating AI Agents]]
For each system benchmarked on SM-100, four key metrics are assessed:

1.  **Bug Discovery ("Needle in the Haystack")**: Can the system discover bugs without prior knowledge? <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>
    *   **Methodology**: To avoid biasing the agent while scoping the search, repositories are broken into interrelated subsystems (e.g., front-end, specific API points) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The agent is then fed only the files within the subsystem that contain modifications from the original "golden PR commit" where the bug was introduced <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This provides a reduced, relevant list of files without hinting at the exact bug <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
2.  **False Positive Rate**: The rate of irrelevant bugs reported by the agent, measured manually <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
3.  **Bug Identification at Introduction (PR Review)**: Can the system find the bug when given the pull request or commit that introduces it? <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a> This provides a more optimistic starting point with immediate context <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
4.  **Remediation Suggestion**: For each discovered bug, can the agent suggest a fix that resolves the bug without breaking the rest of the codebase? <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>

### Performance and Challenges
[[building_effective_ai_agents | Building effective AI agents]] for bug identification is challenging, requiring a sophisticated combination of model, system, prompting, information feeding, and navigation strategy <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>. Basic agent implementations (simple loops with shell tools) often yield a 97% false positive rate <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

Key findings from the SM-100 benchmark include:
*   **"Needle in the Haystack"**: Bismouth led by finding 10 out of 100 bugs, while the next best solution found 7 <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. This highlights significant room for growth in this area <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **True Positive Rate (Detection)**: Codex achieved 45%, Bismouth 25%, and Claude Code 16% <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Many other agents (Devon, Cursor Agent, Cosign) generated hundreds or thousands of reports with very low true positive rates (3-10%), indicating a need for tighter scoping and accuracy <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   **PR Review**: Codex performed strongest at 27%, followed by Devon at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. Even the best model only found 27% of bugs in PR reviews, showing a long way to go <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   **Open-Source Models**: Open-source models like DeepSec R1 (1% true positive rate) and Llama for Maverick (2% true positive rate) showed considerably weaker performance compared to proprietary models <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Prevalence of Issues**: The highest-scoring popular agent achieved only 7% on SM-100, suggesting that most widely used agents are currently poor at finding and fixing complex bugs, which represent a significant portion of software engineering work <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **Missed Simple Bugs**: Even relatively simple bugs, like a form not clearing due to a `is_dirty` state issue, were missed by most agents (only Bismouth and Codex found it) <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Common Agent Behaviors and Future Directions
A notable commonality across agents is their narrow thinking, even when using "thinking models" <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. They don't go deep enough in their evaluations <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. Broader and deeper thinking chains are needed to effectively find bugs <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Additionally, the specific bugs found by an LLM vary across runs, suggesting they don't holistically evaluate files or inventory all issues <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

Despite high scores on benchmarks like SweetEnge (60-80%), agents struggle with SM-100 <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. This implies that while existing agents can create software upfront, managing and fixing deployed software remains a major challenge <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. Solving this requires targeted search, better program comprehension, cross-file reasoning, and bug pattern recognition capabilities <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.

Newer agents, like Bismouth's, are starting to show improved abilities to reason through code and use context more effectively <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. While the technology is nascent, the progress is encouraging, and continued effort with different techniques can lead to industry-wide benefits in software maintenance <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.