---
title: Software agents and bug detection
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

[[ai_agents_beyond_chatbots | AI agents]] designed for software engineering have seen a significant rise in popularity over the past year. A key question is their effectiveness at identifying and resolving bugs, and whether they can be relied upon for software maintenance tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Bismouth's Work in Software Agents

Bismouth, a company specializing in software agents, has been actively working in this field for over a year <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

*   **Ian (CEO)**: Has a background in data engineering, machine learning, and search, with previous experience at Zillow on the A/B testing platform <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. His prior work includes technical documentation search and [[ai_agents_and_agentic_workflows | AI]] summarization for internal knowledge bases <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Nick (CTO)**: Primarily worked in the software security space before co-founding Bismouth <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. He was on an internal tools team at Google building endpoint security software and conducted research focused on detecting software exploitation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Techniques from this space are transferable to building intelligent [[ai_agents_and_agentic_workflows | agentic]] code tools <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

Bismouth acknowledges Base10 for providing credits and compute for their benchmarks <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## The SM100 Benchmark

To assess the capabilities of [[ai_agents_beyond_chatbots | software agents]] in coding tasks beyond typical feature development, Bismouth developed a benchmark called SM100 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Gaps in Existing Benchmarks

While several benchmarks exist for measuring LLM effectiveness in writing code (e.g., Human Eval, Polyglot, Live Codebench), these only cover a fraction of the Software Development Life Cycle (SDLC) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Other critical SDLC phases, like initial scoping, planning, code review, and deployment, are largely unbenchmarked <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Focus on Software Maintenance

The SM100 benchmark specifically targets software maintenance tasks, including bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. These tasks require deep reasoning through a codebase to identify bugs <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Understanding system architecture and connectedness is crucial for both finding bugs and developing features <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Often, understanding a system to find a bug requires even deeper knowledge than initially writing the feature <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Limitations of Prior Bug Detection Benchmarks

Existing bug detection benchmarks from the software security space are not suitable for evaluating new [[ai_agents_and_agentic_workflows | agentic AI systems]] due to several limitations <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>:
*   **Simplistic Bugs**: They often focus on simple, common patterns like null pointer dereferences, buffer overflows, or SQL injection, which can be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Limited Languages**: Many are restricted to languages like Java, reflecting the historical prevalence of enterprise software in that language <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Security Bias**: There's a bias towards security issues because classic static analysis tools historically focused there <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. However, bugs appear in many forms beyond security defects, such as copy-paste errors that break functionality <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### SM100 Methodology

The SM100 benchmark was designed to overcome these limitations <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>:
*   **Real-World Bugs**: It includes 100 carefully gathered, triaged, validated, and classified bugs from over 84 public open-source repositories <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. These bugs were already remediated in the wild <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Range of Difficulty**: Bugs span from obvious issues requiring low domain knowledge to complex problems demanding senior staff-level engineering knowledge <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Multi-Language Focus**: The benchmark includes Python, TypeScript, JavaScript, and Go, acknowledging that LLMs perform differently across languages. Go serves as a control for low-level systems engineering languages <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Objective Bugs**: Only explicit security or logical issues causing data loss or system crashes are included, removing ambiguity or harmless cases. This excludes feature requests, optimization, style, and design decisions <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Metadata Annotation**: Each bug is annotated with metadata such as severity, context, required domain knowledge, difficulty, and implication (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This allows understanding which level of bugs [[multiagent_systems_in_ai | AI agents]] can regularly find <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. While agents occasionally find zero-day exploits, the focus is on everyday performance <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Evaluation Metrics

Four key numbers are extracted from the benchmark for each system <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>:
1.  **Needle in the Haystack**: Can the system discover bugs without prior knowledge <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>? This involves feeding the LLM only the files within the relevant subsystem of the bug, rather than the entire repository, to avoid biasing the agent while still scoping the problem <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
2.  **False Positive Rate**: A manual measurement of incorrect bug reports generated by the agents <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
3.  **Bug Detection at Introduction**: Can the system identify the bug when given the specific pull request or commit that introduced it <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>?
4.  **Remediation Suggestion**: For each discovered bug, can the agent suggest a fix that resolves the issue without introducing new problems <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>?

## Challenges in Building Effective Software Agents

Developing a proficient [[ai_agents_beyond_chatbots | agent]] for bug identification and code work is complex <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **High False Positives in Basic Agents**: Simple [[ai_agents_and_agentic_workflows | agent]] implementations (e.g., using basic shell, search-and-replace, or reporting tools in a loop) can find some bugs, but often suffer from extremely high false positive rates (e.g., 97%) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. These basic agents, often equipped with tools from Anthropic or OpenAI model card releases, are generally inadequate for finding and triaging bugs in real systems <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Complexity of Effective Agents**: Success requires a combination of model, system design, prompting techniques, information feeding strategies, and navigation strategies <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   [[challenges_and_limitations_of_ai_in_bug_identification | **Narrow and Superficial Reasoning**]]: A common issue across agents is their narrow thinking. Even with "thinking models," the evaluation types are limited, and the depth of analysis is often insufficient <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. This leads to agents missing bugs that human developers would quickly spot and confirming false positives that humans would immediately discard <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Inconsistent Bug Detection**: On a per-run basis, the total number of bugs found by an LLM might be consistent, but the specific bugs identified can change. This suggests that LLMs do not holistically evaluate a file or system, potentially due to internal biases <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. This remains a pervasive problem in the industry <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.

## Performance Comparisons

The SM100 benchmark reveals significant differences in [[evaluating_ai_agents_and_assistance | AI agent performance]]:
*   **Needle in a Haystack**: Bismouth leads, finding 10 out of the 100 "needles," with the next best solution finding 7 <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This highlights that there's substantial room for growth in this area <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **True Positive Rate (TPR)**: Codeex shows the highest TPR at 45%, followed by Bismouth at 25%, and Claude Code at 16% <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. These solutions also exhibit tighter scoping, generating significantly less "random nonsense" compared to others <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **High False Positives in Other Agents**: Agents like Devon, Cursor Agent, and Cosign reported between 900 and 1,300 items, but with very low true positive rates (3-10%) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. This means a lot of noise that engineers would have to sift through <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **PR Review Performance**: Codeex performed strongly at 27% "needle in a haystack" detection during PR review, followed by Devon at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. Even the best model only achieved 27%, indicating a long way to go for both PR review and bug detection <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   **Bismouth's Model Agnosticism**: Bismouth's solution, while model-agnostic, typically runs on Anthropic models and was able to outperform Claude Code (Anthropic's own solution) in multiple categories <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### Basic and Open-Source Agent Performance

Open-source models currently lag significantly in this space <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>:
*   R1 showed a 1% true positive rate over hundreds of bugs <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   Llama Maverick had a 2% true positive rate <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Sonnet 4 (6%) and O3 in a loop (3%) performed better but still had low true positive rates <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The highest-scoring popular agent outside of Bismouth achieved only 7% on SM100 <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This suggests that the most widely used [[ai_agents_beyond_chatbots | agents]] are currently poor at finding and fixing complex bugs, posing a significant problem for the industry <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Example: The State Issue Bug

A simple state issue, where a form's "is dirty" flag was not reset, causing it to never clear after submission, was only found by Bismouth and Codeex <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This type of bug, while not severe, impacts user experience and would be immediately caught by a human developer, highlighting the gap in current [[ai_agents_beyond_chatbots | agent]] capabilities <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

## Conclusion and Future Outlook

Despite reported high scores on benchmarks like Sweet Code (60-80% success), [[ai_agents_beyond_chatbots | agents]] still struggle significantly with SM100 <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This indicates that while existing agents can create software, managing and fixing deployed software remains a major challenge <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.

Overcoming these [[challenges_and_limitations_of_ai_in_bug_identification | limitations]] requires:
*   Targeted search <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>
*   Better program comprehension <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>
*   Cross-file reasoning <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>
*   Advanced bug pattern recognition <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>

While most frequently used agents today carry a high risk of introducing bugs, newer generation agents like Bismouth and Codeex are showing increased ability to reason through code and utilize context more effectively <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>. The stability of these agents is nascent but encouraging <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Continued effort and different techniques can lead to significant improvements across the entire industry, pushing forward this new generation of [[multiagent_systems_in_ai | agents]] <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.