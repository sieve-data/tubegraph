---
title: Benchmarks for evaluating software development lifecycle
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have seen a surge in popularity, prompting investigations into their efficacy for tasks like finding and fixing bugs and software maintenance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Evaluating these agents requires benchmarks that cover the full spectrum of the Software Development Lifecycle (SDLC) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Current Benchmarking Landscape

While there are existing benchmarks for evaluating Large Language Models (LLMs) in code writing, such as Human Eval, Polyglot Benchmark, and LiveCodeBench <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, these only cover a fraction of the SDLC <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Significant gaps exist in benchmarking other critical stages:
*   **Initial Scoping and Planning** Requires broad business context and knowledge of existing systems, which is a distinctly different task from development <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Code Review** Largely unbenchmarked, despite the emergence of LLM-based tools in this area <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This is the first part of the benchmark discussed by Bismouth <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **Deployment** A separate task involving configuration, monitoring, and integration with existing systems <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   [[role_of_ai_in_software_maintenance_and_improvement | Software Maintenance Tasks]] This includes bug fixes, dependency upgrades, and migrations <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This area, at its core, involves code writing but in a distinctly different way from feature development <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. The ability to deeply reason through a codebase to find bugs is crucial here, requiring an understanding of system architecture and connectedness, often deeper than when the feature was originally written <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Limitations of Existing Bug Detection Benchmarks
Existing bug detection benchmarks, primarily from the software security space, are not well-suited for evaluating modern [[role_of_reasoning_models_in_application_development | agentic AI systems]] <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Simplistic Bugs** They often focus on relatively simple bugs and common patterns (e.g., null pointer dereferences, buffer overflows, SQL injection) that can be found statically <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Limited Language Support** Many are limited to specific languages, like Java, due to historical prevalence in enterprise software <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Security Bias** There is a bias towards security issues, whereas bugs appear in many forms beyond security defects (e.g., copy-paste bugs that break software for end-users) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## SM-100: A New Benchmark for Software Maintenance

Bismouth developed the SM-100 benchmark to address the limitations of existing evaluation methods and focus on software maintenance tasks <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Benchmark Development and Characteristics
*   **Bug Collection** Painstakingly gathered 100 triaged, validated, and classified bugs from over 84 public repositories <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. These bugs were already remediated and represented real-world issues in open-source projects <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Issue Variety** The bugs span a range of difficulty, from those requiring obvious, low-specific domain knowledge to those demanding senior staff-level engineering knowledge and significant depth of understanding for a given project <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Multi-Language** Includes Python, TypeScript, JavaScript, and Go, chosen to assess performance across popular languages and a low-level systems engineering language <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Objective Bug Definition** An "objective bug" is an explicit security issue or logical issue that could cause data loss or system crashes <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. This definition removes ambiguity and harmless issues, and ensures reproducibility across evaluations <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Excludes feature requests, optimizations, style formatting, or design decisions, as these are often subjective and debated even by humans <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Metadata Annotation** Each bug is annotated with metadata, including:
    *   Severity <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
    *   Context where it was defined and called <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
    *   Amount of system-specific domain knowledge a human would require to find it <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
    *   Difficulty to find the bug even with said knowledge <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>
    *   Implication of the bug (e.g., data loss, crash, security exploit) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
These classifications help understand which level of bugs AI agents can regularly find <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Evaluation Metrics
For each system benchmarked on SM-100, four key metrics are derived <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>:
1.  **Needle in the Haystack** Can the system discover the bug without any prior knowledge <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>?
2.  **False Positive Rate (FPR)** Manually measured to assess the overall effectiveness and prevent overwhelming developers with irrelevant reports <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
3.  **Bug Finding at Time of Introduction** Can the system identify the bug when given the pull request or commit that introduces it, leveraging the immediate context <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>?
4.  **Remediation Suggestion** For each discovered bug, the agent is asked to fix it, and the fix's efficacy in addressing the bug without breaking other code is evaluated <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### "Needle in the Haystack" Methodology
To avoid biasing agents while still scoping the problem, repositories are broken into subsystems containing interrelated files (e.g., part of a front-end or a specific API point) <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. The LLM is then fed only the files within the subsystem that contains the "golden PR commit" where the bug was introduced, providing a reduced list of files without hinting at the specific bug location <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

## Performance and Challenges of AI Agents

Building a good agent for identifying bugs and working on code is challenging, requiring a combination of model, system, [[prompt_engineering_importance | prompting]], information feeding, and navigation strategy <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

### Benchmarking Results
*   **Needle in a Haystack:** Bismouth led the pack, finding 10 out of 100 bugs, with the next best finding 7 <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. This highlights significant room for growth in this area <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **True Positive Rate:** Codeex achieved 45%, Bismouth 25%, and Claude Code 16% <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. These solutions showed a tighter scoping, producing significantly less "random nonsense" compared to others <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
    *   Agents like Devon, Cursor Agent, and Cosign found between 900 and 1,300 items, with a true positive rate of only 3-10% <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>, indicating a high false positive rate.
*   **PR Review:** Codeex was strong at 27% "needle in the haystack" found, followed by Devon at 21% and Bismouth at 17% <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. Even the best model only got 27%, indicating a long way to go for both PR review and bug detection <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   **Basic Agents (Simple Loop):**
    *   Open-source models like DeepSec R1 and Llama for Maverick showed very low true positive rates (1% and 2% respectively) <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   Sonnet 4 found 6 "needles" and 03 found 2, with 3% and 6% true positive rates respectively <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
    *   The highest popular agent score outside Bismouth was 7% on SM-100 <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. This implies that most used agents are currently poor at finding and fixing complex bugs <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Common Agent Limitations
*   **Narrow Thinking** Agents exhibit narrow thinking, even when using "thinking models," and do not go deep enough in their evaluations <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.
*   **Lack of Holistic Evaluation** The total number of bugs found per run remains consistent, but the specific bugs change, suggesting LLMs do not holistically inventory everything in a file <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
*   **High False Positive Rates** Some agents produce an astounding number of false reports (e.g., 70 reports for one issue), which no human engineer would sift through <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   **Missing Simple Bugs** Even simple bugs, like a form clearing state issue that impacts user experience, are often missed by most agents <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.

### Future Directions
Despite relatively high scores on benchmarks like Sweet Edenge for upfront software creation, agents still struggle significantly with software maintenance tasks as evaluated by SM-100 <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>. This points to a major challenge in managing and fixing deployed software with AI <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>.

[[ai_product_development_iteration | Iterative improvement of evaluation processes]] and agents will require:
*   Targeted search <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>
*   Better program comprehension <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>
*   Cross-file reasoning <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>
*   Bug pattern recognition <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>

Newer agents, including Bismouth and Codeex, are beginning to show promise with tighter, more narrow bands of bug solving and the ability to find complex issues <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. The stability of these newer agents is nascent but encouraging, showing an increased ability to reason through code and effectively use context for evaluation <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Continued effort and different techniques can lead to significant improvements across the industry <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

For more details, visit bismouth.sh <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.