---
title: Role of AI in software maintenance and improvement
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen a surge in popularity, raising questions about their effectiveness in finding and fixing bugs, and their reliability for software maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While benchmarks exist for measuring Large Language Model (LLM) effectiveness in writing new code, evaluating their performance in other critical aspects of the Software Development Life Cycle (SDLC), particularly maintenance, remains a challenge <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Current State of AI in the SDLC <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>

Existing benchmarks primarily focus on feature development and testing <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. However, other crucial stages like initial scoping and planning, code review, deployment, and especially software maintenance, are less explored <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Software maintenance tasks include bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This differs from feature development as it requires deep reasoning through a codebase to identify issues, often needing a more profound understanding of the system architecture than when the feature was initially written <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Challenges in AI Bug Detection <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>

AI agents currently struggle with the holistic evaluation of files and systems, frequently finding only subsets of bugs per run <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Their reasoning can be narrow, exploring a limited number of avenues, leading to them missing bugs that human developers would immediately identify or confirming false positives <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. While they can often patch simple bugs, this is not indicative of their ability to handle complex issues <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Existing bug detection benchmarks from the software security space have significant limitations for evaluating new [[the_evolution_and_current_state_of_ai_engineering | agentic AI systems]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>:
*   **Simplistic Bugs:** They focus on basic bugs (e.g., null pointer dereferences, buffer overflows) that can often be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Limited Languages:** Many are restricted to languages like Java <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Security Bias:** There's a bias towards security issues, despite bugs appearing in many other forms, such as copy-paste errors that break software without being security defects <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Bismouth's SM100 Benchmark <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>

To address these gaps, Bismouth developed the SM100 benchmark, consisting of 100 triaged, validated, and classified bugs from over 84 public open-source repositories <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Benchmark Goals <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>
*   **Range of Issue Types:** Bugs range from obvious issues requiring low domain knowledge to those demanding senior-staff level understanding <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Multi-Language:** Includes Python, TypeScript, JavaScript, and Go, acknowledging differing LLM performance across languages <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Objective Bugs:** Focuses on explicit security or logical issues causing data loss or system crashes, avoiding ambiguous or harmless issues <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. It explicitly excludes feature requests, optimizations, style, or design decisions <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Metadata and Classification <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>
Each bug is annotated with metadata, including:
*   Severity and context <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
*   Required system-specific domain knowledge to find it <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
*   Difficulty of discovery even with knowledge <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>
*   Implication of the bug (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>

These classifications help understand what level of bugs [[role_of_ai_engineering_in_reliability | AI agents]] can regularly find <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. While AI can occasionally find complex exploits (e.g., a zero-day exploit by 03, which took 100 runs), the benchmark assesses everyday usage <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Evaluation Metrics <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>
The SM100 benchmark measures four key aspects:
1.  **Needle in a Haystack:** Can the system discover bugs without prior knowledge <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>? This involves feeding LLMs a reduced list of files within relevant subsystems, avoiding bias while scoping the search <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
2.  **False Positive Rate:** Manual measurement of incorrect bug reports <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
3.  **Time of Introduction Detection (PR Review):** Can the system identify the bug when given the pull request or commit that introduced it <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>? This provides an optimistic scenario with immediate context <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
4.  **Remediation Suggestion:** For each discovered bug, can the agent suggest a fix that resolves the issue without breaking the rest of the codebase <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>?

## AI Agent Performance Findings <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>

Basic implementations of AI agents, while trivial to set up, often result in high false positive rates (e.g., 97%) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Building an effective agent for bug identification requires a combination of model, system, prompting, information feeding, and navigation strategy <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

### Benchmark Results <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>
*   **Needle in a Haystack:** Bismouth led by finding 10 bugs, with the next best finding 7 <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **True Positive Rate (Detection):** Codeex showed 45%, Bismouth 25%, and Claude Code 16% <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. These solutions also generated significantly less "random nonsense" compared to others <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. Some agents generated an astounding 70 reports for a single issue, making it impractical for human review <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **PR Review (Needle in a Haystack):** Codeex was strong at 27%, followed by Devon at 21%, and Bismouth at 17% <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. Even the best model only found about a third of the bugs in this context <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Challenges for Current Agents <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>
*   **High False Positive Rates:** Many popular agents scored 7% or less true positives on SM100 <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, indicating they are currently ill-equipped for complex bug finding and fixing <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   **Narrow and Shallow Thinking:** Agents, even with thinking models, evaluate a narrow range of options and do not go deep enough into selected reasoning chains <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Lack of Holistic Evaluation:** The total number of bugs found per run remains consistent, but the specific bugs found change, suggesting LLMs do not holistically inventory issues within a file <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

## Conclusion and Future Directions <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>

Despite decent scores on feature creation benchmarks, existing AI agents significantly struggle with software maintenance tasks like finding and fixing bugs <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

> "Existing agents are able to create software upfront, but to manage and fix software after it's been deployed will be a major struggle as far as we see it." <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>

Overcoming these challenges requires:
*   Targeted search <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>
*   Better program comprehension <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>
*   Cross-file reasoning <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>
*   Improved bug pattern recognition <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>

While the most frequently used agents today risk introducing new bugs <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>, newer agents, including Bismouth, are showing an increased ability to reason through code and effectively use context for evaluation <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. This emerging stability is encouraging, and with continued effort and new techniques, significant [[enhancing_existing_systems_with_ai_capabilities | improvements]] in [[impact_of_ai_on_organizational_operations_and_efficiency | AI for software maintenance]] are anticipated, benefiting the entire industry <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.