---
title: Developing AI coding assistants with contextawareness
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

The field of AI in coding has rapidly evolved, with companies like Sourcegraph leading the way in developing tools that significantly enhance developer productivity by providing deep context awareness.

## The Role of AI in Coding Today <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>

Coding is recognized as one of the most effective use cases for AI to date, evidenced by over a million paying users for GitHub Co-pilot <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. AI's primary impact currently lies in accelerating the "inner loop" of software development <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This refers to the frequent cycle a developer goes through multiple times a day: understanding a task, writing code, testing it, and repeating <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Tools that assist in these frequent, commonplace tasks, such as code completion or context-aware chat, are in heavy day-to-day use <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

## Sourcegraph's Approach: Cody, the AI Coding Assistant <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>

Sourcegraph, a leader in the space, offers two main products for developers:
1.  **Code Search Engine:** This tool helps human developers understand vast codebases by allowing them to search, navigate definitions, and find references, thereby acquiring necessary context <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
2.  **Cody:** An [[The current state and future potential of AI in coding | AI coding assistant]] that provides <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>:
    *   **Inline completion:** Autocompletes thoughts as code is typed <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
    *   **Chat:** Enables asking high-level questions about code and generating code for specific tasks <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
    *   **Menu of commands:** Targets specific, often tedious, actions like writing doc strings or high-quality unit tests <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Context-Awareness as a Differentiator <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
Cody's key differentiator is its ability to perform these functions with the benefit of context and awareness about the user's specific codebase <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. Unlike general models that might provide "median" answers from open-source code, Cody understands the specific frameworks, libraries, and production environments relevant to a developer's project <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This deep contextual understanding is crucial for applying AI effectively within an existing codebase <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## Advancements in AI Models and Retrieval <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>

The progression of large language models (LLMs) from GPT-3.5 to GPT-4 and Claude 3 has significantly enhanced Cody's reliability <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Newer models show improved ability to incorporate given context and integrate it into working code examples <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This allows for more consistent "wow moments" in daily usage, such as zero-shot application building using specific libraries and APIs <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

### The Role of [[Retrieval augmented generation and contextual AI | Retrieval Augmented Generation (RAG)]] <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>
Sourcegraph heavily utilizes [[Retrieval augmented generation and contextual AI | RAG]] to tie queries to the customer's actual codebase <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. While larger context windows in LLMs are helpful, they are not a complete solution. The best application architectures will always combine large context windows with more tailored information retrieval mechanisms <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. Sourcegraph has extensively evolved its search techniques for RAG, even finding that classical keyword search, combined with clever chunking strategies, was highly effective early on, often outperforming naive vector database approaches <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

## The Path to Full Automation (Agents) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>

While current AI tools excel at accelerating the inner loop, the next frontier is full automation through agents. This involves systems that can perform multi-step, bot-driven development where the AI drives the process, and humans primarily advise <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Achieving this requires:
*   **Evaluational language models:** To make and refine code changes towards a desired pull request <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
*   **Context acquisition:** The ability to fetch detailed information about the surrounding code and existing patterns <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Recollection of actions:** A feedback loop where the AI learns from trials, errors, and observed results <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Virtual execution environment:** To try things, make changes, and observe results in a controlled setting <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Efficiency:** Reducing the number of "cycles" needed to reach a correct answer, which relies on better observation, learning, prediction, and context retrieval <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.

Code offers a natural environment for this exploration due to its clearer "did this work?" evaluation <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. Sourcegraph is actively building systems targeting specific problems amenable to full automation, combining existing context providers with an execution loop <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>. This work, including developing subroutines like test generation, benefits both outer-loop automation and inner-loop assistance <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.

## Model Strategy and Evaluation <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>

Sourcegraph's philosophy is to "do the dumb thing first" <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>, prioritizing ease of implementation and rapid iteration. This meant focusing on [[Retrieval augmented generation and contextual AI | RAG]] initially rather than complex fine-tuning <a class="yt-timestamp" data-t="00:27:26">[00:27:26]</a>. However, fine-tuning is now being explored to address language-specific code generation where base models underperform (e.g., Rust, Ruby) <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

For model evaluation, Sourcegraph emphasizes product metrics over traditional benchmarks <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. They prioritize metrics like:
*   **Acceptance rate and overall volume** for code completions <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>.
*   **Engagement and usage** for explicit actions like chat and test generation <a class="yt-timestamp" data-t="00:42:33">[00:42:33]</a>.

This user-centric approach allows them to quickly understand actual value, as user acceptance directly reflects utility <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. When new models like GPT-5 are released, Sourcegraph's plan is to enable them quickly in Cody, allow users to choose, and observe product usage metrics to gauge effectiveness <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## Impact on Developers <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>

AI coding tools show varying benefits across developer experience levels <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>:
*   **Junior developers** tend to find inline completions highly beneficial, viewing them as a pedagogical tool that provides useful starting points <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Senior engineers** often prefer chat-based interactions, as inline completions can be disruptive if not consistently precise <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

Ultimately, AI helps automate the "toil and drudgery" of coding, freeing up developers to focus on higher-value, more creative tasks that differentiate their work <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

## The Future of AI in Coding and Developer Ecosystems <a class="yt-timestamp" data-t="01:05:46">[01:05:46]</a>

The number of engineers is expected to grow, but the definition of "engineering" and the day-to-day experience of a software developer will change drastically <a class="yt-timestamp" data-t="01:06:11">[01:06:11]</a>. The "outer loop" of software development, encompassing the full lifecycle from ideation to deployment, is where more automation will eventually happen <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

Key trends include:
*   **Local Inference Models:** A growing demand for running models locally (e.g., using Olama or LM Studio) due to benefits like offline availability (e.g., on an airplane), privacy, and cost <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>. As GPU and model speeds improve, local inference could reduce latency even further, which is critical for developer experience <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.
*   **Evolving Product Roadmaps:** Sourcegraph prioritizes adding value over over-optimizing costs, anticipating that inference costs will decrease over time <a class="yt-timestamp" data-t="00:31:33">[00:31:33]</a>.
*   **Open Ecosystems:** Sourcegraph believes in enabling an open ecosystem where developers have freedom of choice regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. They aim to provide building blocks (like Cody's custom commands for prompt engineering) that allow any developer to leverage AI, not just a specialized class of AI developers <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>. This contrasts with a future where large players might vertically integrate and force adoption of proprietary platforms <a class="yt-timestamp" data-t="01:12:16">[01:12:16]</a>.
*   **Complimentary Technologies:** Formal specifications and languages will remain crucial alongside AI, as natural language often lacks the precision needed for complex tasks like programming <a class="yt-timestamp" data-t="01:15:32">[01:15:32]</a>.
*   **Underhyped Areas:** The development of tools that are complementary to AI, particularly formal specifications and languages, is seen as underhyped. These are not replaced by AI but work in tandem to achieve precise outcomes <a class="yt-timestamp" data-t="01:15:32">[01:15:32]</a>.

### Milestones for AI in Coding <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>
A significant milestone for AI in coding would be when classes of problems, such as simple bug fixes derived from production logs, become automatically solvable by fully automated systems in production, moving from near-zero to a high percentage like 80% <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>. This requires continuous improvements in model quality and controllability <a class="yt-timestamp" data-t="01:04:36">[01:04:36]</a>.

## Conclusion

The development of AI coding assistants like Cody, with their emphasis on context-awareness and effective use of [[Retrieval augmented generation and contextual AI | RAG]], is transforming the daily experience of software developers. The future promises further automation, moving towards comprehensive AI agents, while maintaining an open ecosystem that empowers all developers. This shift will allow humans to focus on the unique, creative aspects of software creation, leaving repetitive tasks to AI <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.