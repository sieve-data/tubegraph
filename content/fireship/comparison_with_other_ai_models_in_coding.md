---
title: Comparison with other AI models in coding
videoId: x2WtHZciC74
---

From: [[fireship]] <br/> 

Anthropic released Claude 3.7 Sona, a highly anticipated large language model, on February 24, 2025 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is regarded as "straight gas" and is noted for being even better at programming <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The model also introduced a new thinking mode, mirroring the success of DeepSeek R1 and [[open_source_ai_models | open AO models]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Claude Code CLI Tool

Anthropic also released Claude Code, a command-line interface (CLI) tool <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This tool theoretically creates an infinite feedback loop that could replace programmers by allowing users to build, test, and execute code within any project <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

### Availability and Cost
Claude Code is currently in research preview <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> and can be installed via npm <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. It directly uses the Anthropic API and is significantly more expensive than other models, costing $15 per million output tokens <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This is over 10 times the cost of models like Gemini Flash and DeepSeek <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Functionality
The `claude` command in the terminal gives the tool full context of existing code in a project <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   The `in` command scans a project and generates a markdown file with initial context and instructions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   The `cost` command allows users to monitor their token expenditure <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

When prompted, Claude Code proposes actions and requires user confirmation <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. It can write new files to the file system and creates dedicated testing files <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This reliance on test-driven development and strongly typed languages enables the AI to validate its code and iterate on business logic based on test feedback until correct <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Performance Benchmarks and Real-World Usage

### Programming Capability
An Anthropic paper indicated that despite programmers making up only 3.4% of the workforce, over 37% of AI prompts are related to math and coding <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. While AI hasn't taken human programmer jobs yet, it has impacted platforms like Stack Overflow <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Claude 3.5, the previous version, topped the Web Dev Arena leaderboard, a strong indicator for web development, though it was roughly tied with other state-of-the-art models <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Software Engineering Benchmark
The new Claude 3.7 model significantly outperformed other models, including OpenAI O3 mini high and DeepSeek, in the software engineering benchmark <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This benchmark is human-verified and based on real GitHub issues <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Claude 3.7 is capable of solving 70.3% of GitHub issues based on this benchmark <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Practical Tests with Claude Code

1.  **Deno Random Name Generator**: Claude Code successfully created a "perfect" random name generator in Deno <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
2.  **Svelte Frontend UI (Microphone Waveform Visualizer)**: Claude Code built a moderately complex Svelte frontend UI that accessed a microphone and visualized its waveform <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   It understood the existing tech stack (TypeScript and Tailwind) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   While taking longer than direct web UI prompting, the visual result was good <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   [[comparison_of_ai_models_costs_and_effectiveness | A comparison]] with OpenAI O3 mini high generating the same UI showed O3 mini high produced an "embarrassing piece of crap" visually <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
    *   However, Claude's code had issues: it didn't use TypeScript or Tailwind as expected, nor did it use the new Svelte 5 Rune syntax <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This session cost about 65 cents <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
3.  **End-to-End Encrypted App Fix**: Claude Code attempted to fix "ChatGPT garbage code" for an end-to-end encrypted app but still failed to run, leaving the user unable to debug the error due to over-reliance on AI <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

### Synergy with Convex
Convex, an [[open_source_ai_models | open-source]] reactive database, offers features like typesafe queries and real-time data sync <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Its use of pure TypeScript for database queries creates a positive side effect: AI models like Claude can more easily understand and write Convex code with fewer errors, leading to higher productivity in autonomous coding <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.