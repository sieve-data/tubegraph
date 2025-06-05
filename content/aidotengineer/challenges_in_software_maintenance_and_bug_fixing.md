---
title: Challenges in software maintenance and bug fixing
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen a surge in popularity, leading to questions about their effectiveness in finding and fixing bugs and their reliability for [[Challenges of maintaining large codebases | maintenance]] tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Bismouth, a company specializing in [[software_agents_and_bug_detection | software agents]], has been working on this area for over a year <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Limitations of Existing Benchmarks

While several benchmarks exist for evaluating Large Language Models (LLMs) in writing code (e.g., Human Eval, Polyglot Benchmark, LiveCodeBench), these only cover a fraction of the [[developing_and_using_software_automation_tools | software development life cycle]] (SDLC) <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>. Other critical phases, such as initial scoping, planning, code review, and deployment, are largely unbenchmarked <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

A significant gap lies in [[Challenges of maintaining large codebases | software maintenance]] tasks, including bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. Although these tasks involve writing code, they differ from feature development <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Finding bugs requires a deep understanding of the system architecture and its connectedness, often more profoundly than when the feature was initially written <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

Existing bug detection benchmarks, primarily from the software security space, were designed for classic static analysis or program repair tools and have significant limitations for [[agentic editors in software development | agentic AI systems]] <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>:
*   **Simplistic Bugs:** They focus on basic bugs like null pointer dereferences or buffer overflows, which can often be found statically <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Limited Languages:** Many benchmarks are Java-only, despite software being written in diverse languages <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.
*   **Security Bias:** There's a bias towards security issues, neglecting other common bug types like copy-paste errors that break software for end-users <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

## The SM-100 Benchmark

To address these limitations, Bismouth developed the SM-100 benchmark over several months <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

### Benchmark Development

The SM-100 benchmark involves a painstakingly gathered set of 100 triaged, validated, and classified bugs from over 84 public repositories <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. These are real-world bugs that have already been remediated <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.
*   **Range of Difficulty:** The bugs span various issue types, from those requiring low domain-specific knowledge to those needing senior staff-level engineering understanding <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
*   **Multi-language:** The benchmark includes Python, TypeScript, JavaScript, and Go, acknowledging that LLMs perform differently across languages <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
*   **Objective Bugs:** The benchmark focuses on "objective bugs"—explicit security or logical issues that could cause data loss or system crashes <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. This excludes ambiguous issues like feature requests, optimizations, style formatting, or design decisions <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.
*   **Metadata:** Each bug is annotated with metadata such as severity, context, required domain knowledge, difficulty, and implication (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>. These classifications help understand which levels of bugs [[Impact of AI coding agents on software engineering | AI agents]] can regularly find <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

### Benchmark Metrics

The SM-100 benchmark measures four key aspects of an agent's performance <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>:
1.  **Needle in the Haystack (Discovery):** Can the system discover bugs without prior knowledge <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>? To make this feasible without hinting, repositories are broken into subsystems, and only files within the relevant subsystems are fed to the LLM <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
2.  **False Positive Rate:** The benchmark manually measures the false positive rate of reported bugs to assess overall effectiveness <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
3.  **Time of Introduction:** Can the system find a bug at the time it's introduced, given the pull request or commit <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>?
4.  **Remediation Suggestion:** For each discovered bug, the agent is asked to fix it, and the fix is evaluated to ensure it resolves the bug without breaking other code <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.

## Challenges in Building Effective AI Agents for Bug Fixing

Building a high-performing agent for identifying bugs and working on code is challenging, requiring a sophisticated combination of <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>:
*   Model selection
*   System design
*   Prompting strategies
*   Information management and feeding to the model
*   Navigation strategy

Basic agent implementations, often simple loops with shell and reporting tools, tend to have an extremely high false positive rate (e.g., 97%) <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>. This means they are not currently suitable for real-world bug finding and triaging <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.

### Performance Observations

Performance comparisons on the SM-100 benchmark highlight significant room for improvement <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>:
*   **Needle in a Haystack:** Bismouth led by finding 10 out of 100 bugs, with the next best finding 7 <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
*   **True Positive Rate:** CodeX showed a true positive rate of 45%, Bismouth 25%, and Claude Code 16% <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a>. These agents also showed significantly less "random nonsense" in their reports <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   **High False Reports:** Agents like Devon, Cursor Agent, and Cosign reported between 900 and 1,300 items with true positive rates between 3% and 10% <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. One agent generated an astounding 70 reports for a single issue, which is unmanageable for human engineers <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.
*   **PR Review:** CodeX was strong at 27%, followed by Devon at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. Even the best model only found about a third of the bugs in PR review <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.
*   **Open-Source Models:** Open-source models (R1 and Llama Maverick) showed very low true positive rates (1-2%) <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Complex Bugs:** The most widely used agents scored only 7% on SM-100, indicating they are poor at finding and fixing complex bugs <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>. Simple bugs, such as a state issue preventing a form from clearing, are often missed by most agents <a class="yt-timestamp" data-t="14:59:00">[14:59:00]</a>.

### Common Agent Shortcomings

A notable commonality among agents is their narrow thinking, even when using "thinking models" <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>. They evaluate a limited number of avenues and do not go deep enough <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>.
*   **Lack of Holistic Evaluation:** On a per-run basis, the total number of bugs found might be consistent, but the specific bugs change, indicating that LLMs are not holistically evaluating a file and inventorying all issues <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. This suggests inherent biases in how models process context <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>.
*   **Maintenance vs. Feature Creation:** Despite high scores on benchmarks for upfront software creation (like Sweet Eden), agents struggle significantly with [[Challenges of maintaining large codebases | managing]] and fixing software after deployment <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. This problem requires targeted search, better program comprehension, cross-file reasoning, and bug pattern recognition, which are currently lacking in depth <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>.

## Conclusion and Future Outlook

Currently, most frequently used [[software_agents_and_bug_detection | AI agents]] carry a high risk of introducing new bugs <a class="yt-timestamp" data-t="17:44:00">[17:44:00]</a>. However, a new generation of agents, including Bismouth and CodeX, are starting to show increased ability to reason through code and effectively use context to evaluate concerns <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>. While their stability is nascent, the progress is encouraging <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.

The SM-100 benchmark provides a clear way to measure progress in this domain <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>. Targeted effort and different techniques can lead to significant improvements that will benefit the entire industry, particularly in [[improving_developer_experience_and_productivity | software maintenance]] <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.