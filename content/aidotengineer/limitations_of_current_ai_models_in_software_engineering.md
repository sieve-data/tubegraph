---
title: Limitations of current AI models in software engineering
videoId: wAQK7O3WGEE
---

From: [[aidotengineer]] <br/> 

AI agents for software engineering have gained significant popularity, but their effectiveness in finding and fixing bugs, and their reliability for software maintenance, are crucial questions <a class="yt-timestamp" data-t="00:00:00"></a>. Bismouth, a company specializing in software agents, has been investigating these [[challenges_in_developing_ai_agents | challenges]] through their own benchmark, SM 100 <a class="yt-timestamp" data-t="00:01:15"></a>.

## Current Scope of AI Benchmarks

Existing benchmarks primarily measure the effectiveness of Large Language Models (LLMs) for writing new code, focusing on [[impact_of_ai_coding_agents_on_software_engineering | feature development]] and testing <a class="yt-timestamp" data-t="00:01:23"></a>. However, the software development life cycle (SDLC) encompasses much more, including:
*   **Initial scoping and planning**: Requires broader business context, knowledge of existing systems, and exploration of solutions, which is a distinct task from development <a class="yt-timestamp" data-t="00:01:40"></a>.
*   **Code review**: Largely unbenchmarked, despite the rise of LLM-based tools in this area <a class="yt-timestamp" data-t="00:02:04"></a>.
*   **Deployment**: A separate task involving configuration, monitoring, and integration with existing systems <a class="yt-timestamp" data-t="00:02:17"></a>.
*   **Software maintenance**: Includes bug fixes, dependency upgrades, and migrations. While still involving code, it requires a different approach than feature development <a class="yt-timestamp" data-t="00:02:29"></a>.

## Challenges in Bug Detection and Maintenance

Maintenance tasks, particularly bug finding, demand a deep understanding of a codebase and system architecture <a class="yt-timestamp" data-t="00:02:49"></a>. [[challenges_in_building_reliable_ai_agents | AI agents]] exhibit several key limitations in this area:

### Narrow and Insufficient Reasoning
*   Agents struggle with holistic evaluation of files and systems, typically finding only subsets of bugs per run <a class="yt-timestamp" data-t="00:03:20"></a>.
*   Even with "thinking models," reasoning tends to be narrow, exploring a limited number of potential avenues at a time <a class="yt-timestamp" data-t="00:03:27"></a>. This can lead LLMs to miss bugs that human developers would identify immediately, or confirm false positives <a class="yt-timestamp" data-t="00:03:34"></a>.
*   The ability to patch bugs, while often successful due to the relative simplicity of the identified bugs, does not signify advanced capabilities in complex bug scenarios <a class="yt-timestamp" data-t="00:03:47"></a>.
*   A pervasive problem across agents is that they do not look holistically at a file and inventory everything happening within it, showing different biases per run <a class="yt-timestamp" data-t="00:16:17"></a>.

### Limitations of Existing Benchmarks for AI Agents
Traditional bug detection benchmarks, often from the software security space, are not well-suited for evaluating new agentic AI systems <a class="yt-timestamp" data-t="00:04:01"></a>:
*   **Simplistic Bugs**: They focus on relatively simplistic bugs in common patterns (e.g., null pointer dereferences, buffer overflows, SQL injection) that can be found statically <a class="yt-timestamp" data-t="00:04:16"></a>.
*   **Limited Languages**: Many benchmarks are restricted to a single language, such as Java <a class="yt-timestamp" data-t="00:04:29"></a>.
*   **Security Bias**: There's a bias towards security issues, overlooking other common bug types like copy-paste errors that break software for end-users <a class="yt-timestamp" data-t="00:04:46"></a>.

### High False Positive Rates
Basic implementations of AI agents, while trivial to set up and capable of finding some bugs, exhibit extremely high false positive rates <a class="yt-timestamp" data-t="00:10:53"></a>.
*   Initial tests showed a 97% false positive rate <a class="yt-timestamp" data-t="00:10:53"></a>.
*   Some agents, like R1 and Llama Maverick, had true positive rates of only 1% and 2% respectively <a class="yt-timestamp" data-t="00:13:33"></a>.
*   Three out of six agents tested achieved 10% or less true positives out of a massive number of reports <a class="yt-timestamp" data-t="00:14:27"></a>.
*   One agent generated an astounding 70 reports for a single issue, which is impractical for human engineers to sift through <a class="yt-timestamp" data-t="00:14:36"></a>. This highlights a need to tighten the amount and accuracy of information reported by agents <a class="yt-timestamp" data-t="00:14:48"></a>.

### Difficulty with Complex and Real-World Bugs
Bismouth's SM 100 benchmark, comprising 100 triaged, validated bugs from 84 public repositories, aims to evaluate agents on a range of issue types and languages (Python, TypeScript, JavaScript, Go) <a class="yt-timestamp" data-t="00:05:11"></a>. These objective bugs include explicit security or logical issues causing data loss or system crashes, excluding ambiguous elements like feature requests or style <a class="yt-timestamp" data-t="00:06:04"></a>.
*   The performance of leading solutions on the "needle in a haystack" problem (discovering bugs without prior knowledge in a reduced context) shows significant room for growth <a class="yt-timestamp" data-t="00:11:27"></a>. Bismouth found 10 bugs, with the next leading solution finding 7 <a class="yt-timestamp" data-t="00:11:29"></a>.
*   In PR review, the best model only found 27% of the "needle in the haystack" bugs <a class="yt-timestamp" data-t="00:12:43"></a>.
*   Even simple bugs, such as a state issue preventing a form from clearing, are missed by most agents <a class="yt-timestamp" data-t="00:15:01"></a>. Only Bismouth and CodeEx successfully identified this issue <a class="yt-timestamp" data-t="00:15:05"></a>.

## The Broader Problem

Despite impressive scores on code generation benchmarks like SweetEden, agents still struggle significantly with maintenance tasks as evaluated by SM 100 <a class="yt-timestamp" data-t="00:16:45"></a>. This indicates that while existing agents can create software, managing and fixing it post-deployment remains a major challenge <a class="yt-timestamp" data-t="00:16:55"></a>. Addressing this requires:
*   Targeted search <a class="yt-timestamp" data-t="00:17:09"></a>
*   Better program comprehension <a class="yt-timestamp" data-t="00:17:13"></a>
*   Cross-file reasoning <a class="yt-timestamp" data-t="00:17:13"></a>
*   Complex bug pattern recognition <a class="yt-timestamp" data-t="00:17:15"></a>

## Future Outlook

The current generation of agents carries a high risk of introducing new bugs <a class="yt-timestamp" data-t="00:17:44"></a>. However, newer agents, including Bismouth's, are beginning to demonstrate an increased ability to reason through code and more effectively use context to evaluate concerns, showing encouraging stability <a class="yt-timestamp" data-t="00:17:50"></a>. This progress in [[challenges_and_innovations_in_ai_engineering | AI engineering]] suggests that with focused effort and new techniques, significant improvements are possible across the industry <a class="yt-timestamp" data-t="00:18:11"></a>.