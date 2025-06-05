---
title: Benchmarking LLMs for software development
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen an explosion in popularity over the last year, leading to questions about their efficacy in finding and fixing bugs, and their reliability for software maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Bismouth, a company specializing in software agents, has been working for over a year to address these questions <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

## Limitations of Existing Benchmarks

While there are existing benchmarks for evaluating large language models (LLMs) in code writing, such as Human Evaluator's polyglot benchmark and Live Codebench, these only cover a single part of the software development life cycle (SDLC) <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

Significant portions of the SDLC remain unbenchmarked by existing work:
*   **Initial Scoping and Planning** Requires broad business context, knowledge of existing systems, and exploration of solutions, making it distinct from development <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   **Code Review** Despite the rise of LLM-based tools in this space, code review is largely unbenchmarked <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.
*   **Deployment** A separate task involving configuration, monitoring setup, and integration with existing systems <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Software Maintenance Tasks** Including bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. This area, while still involving code writing, differs significantly from feature development <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

Software maintenance demands the ability to deeply reason through a codebase to identify bugs <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This requires understanding system architecture and its connectedness, often more deeply than when the feature was originally written <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. LLM agents often struggle with holistic evaluation, finding only subsets of bugs per run <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. Their reasoning can be narrow, exploring a limited number of avenues at a time, leading to missed bugs that humans would immediately detect and confirming bugs that humans would discard <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. While patching simple bugs is relatively easy for agents, the overall capability is still in its infancy <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

Existing bug detection benchmarks, often from the software security space, have major limitations for evaluating modern agentic AI systems:
*   **Simplistic Bugs** They focus on common, statically detectable patterns like null pointer dereferences or buffer overflows <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Limited Languages** Many are Java-only, reflecting historical enterprise software trends <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.
*   **Security Bias** They are biased towards security issues, overlooking other common bug types like copy-paste errors that break software for users <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

## Bismouth's SM-100 Benchmark

To address these gaps, Bismouth developed a benchmark over several months to explore the capabilities of software agents in coding tasks beyond normal feature development <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

### Data Collection and Characteristics
The SM-100 benchmark painstakingly gathered 100 triaged, validated, and classified bugs from over 84 public repositories <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. These bugs were real-world issues already remediated in open-source projects <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.
The goal was to provide a range of issue types, from those requiring minimal domain knowledge to those needing senior staff-level engineering expertise and significant project understanding <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.

The benchmark is multi-language, focusing on:
*   **Python, TypeScript, JavaScript**: Selected for their popularity and supposed better LLM performance <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
*   **Go**: Chosen as a control to balance performance on a low-level systems engineering language <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

### Objective Bugs
The SM-100 focuses exclusively on "objective" bugs, meaning explicit security or logical issues that could cause data loss or system crashes <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. This approach removes ambiguity and harmless issues, such as a function not checking bounds when the calling code ensures input never exceeds those bounds <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. It explicitly excludes:
*   Feature requests <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>
*   Optimizations <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>
*   Style formatting <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>
*   Design decisions <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>

This strict definition helps ensure reproducibility across evaluations <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>. Each bug is annotated with metadata, including severity, context, required system-specific domain knowledge, difficulty to find, and the bug's implication (data loss, crash, security exploit) <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. These classifications help understand which levels of bugs AI agents can regularly find <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>. While agents might occasionally surprise, like finding a zero-day exploit after 100 runs, the benchmark aims to evaluate their everyday utility <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.

### Evaluation Metrics
For each system benchmarked, four key metrics are extracted:

1.  **Needle in the Haystack**: Can the system discover the bugs without any prior knowledge of their location? <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a> To avoid biasing agents or making the search too broad for large repositories, Bismouth breaks down repositories into inter-related subsystems (e.g., a front end or specific API point) <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>. Only files within these subsystems that were modified in the "golden PR commit" (where the bug was introduced) are fed to the LLM, reducing the search space without revealing the bug's exact location <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.
2.  **False Positive Rate**: The rate of irrelevant bugs reported by the agent, manually measured to assess overall effectiveness <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
3.  **Time of Introduction Detection**: Can the system identify the bug at the time it was introduced, given the relevant pull request or commit? This provides an optimistic starting point with immediate context <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
4.  **Remediation Suggestion**: For each discovered bug, can the agent suggest a fix that resolves the issue without introducing new problems or breaking the codebase? <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>

## Key Findings and Challenges

Building a robust agent for identifying bugs and working with code is challenging, requiring a combination of model choice, system design, prompting strategies, information feeding mechanisms, and navigation strategies <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>. Basic agent implementations using simple loops and tools (like shell, search-and-replace, think, report, finish) can find some bugs but often suffer from extremely high false positive rates, making them impractical for real-world use <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>. For example, a basic loop agent might find 5-6 bugs but have a 97% false positive rate <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

### Performance Comparisons
Bismouth's benchmark results indicate:
*   **Needle in the Haystack**: Bismouth led the pack, finding 10 out of 100 "needles," with the next best solution finding 7 <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. This highlights significant room for growth in this area <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.
*   **True Positive Rate**: Codeex achieved the highest true positive rate at 45%, followed by Bismouth at 25% and Claude Code at 16% <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>. These solutions also generated significantly less "random nonsense" compared to others <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   **PR Review (Time of Introduction Detection)**: Codeex was strong at 27% (needle in haystack found), followed by Devin at 21% and Bismouth at 17% <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. Even the best model only found about a third of the bugs in this context, indicating a long way to go <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.

Bismouth's solution, while model-agnostic, typically runs on Anthropic models and was able to outperform their own Claude Code solution in several categories <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

### Performance of Basic and Open-Source Agents
Open-source models generally have a long way to go in this space <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>:
*   R1: 1% true positive rate <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>.
*   Lava Maverick: 2% true positive rate <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.
*   Sonnet 4 (basic loop): 6 needles found, 3% true positive rate <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
*   O3 (basic loop): 2 needles found, 6% true positive rate <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

The highest popular agent score outside of Bismouth was 7% on SM-100 <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>. This means that the most used agents struggle significantly with finding and fixing complex bugs, which represents 90% of software engineering work <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>. Three out of six agents had 10% or less true positives out of a massive number of reports <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>; for instance, one agent generated 70 reports for a single issue, which no human engineer would sift through <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>.

Even simple bugs, like a form not clearing due to an `isDirty` flag not being reset, are missed by most agents. Only Bismouth and Codeex found this specific state issue, highlighting a gap in handling real-world user experience consequences that human developers would immediately catch <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>.

### Common Agent Weaknesses
A notable commonality across agents is their **narrow thinking**, even when employing thinking models <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>. They evaluate a limited range of issues and don't go deep enough <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>. Broader and deeper thinking chains are needed to effectively find bugs <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. Interestingly, the total number of bugs found per run remains consistent, but the specific bugs change, suggesting LLMs are not holistically inventorying issues within a file due to biases in context <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.

Despite scoring 60-80% on benchmarks like Sweet Edenge (likely related to initial code generation), agents still struggle with SM-100 <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>. This implies that while existing agents can create software upfront, managing and fixing deployed software remains a major challenge <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>. Overcoming this requires targeted search, better program comprehension, cross-file reasoning, and bug pattern recognition that many solutions currently lack <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>.

## Conclusion

The most frequently used agents today carry a high risk of introducing bugs <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. However, newer agents, including Bismouth's, are beginning to demonstrate an increased ability to reason through code and more effectively use context to identify concerns <a class="yt-timestamp" data-t="17:49:00">[17:49:00]</a>. While the stability of these systems is nascent, the progress is encouraging <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. The SM-100 benchmark provides a clear path to measure and drive improvements in this critical area, which will benefit the entire industry <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>.