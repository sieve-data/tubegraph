---
title: Claude 37 release and impact on programming
videoId: x2WtHZciC74
---

From: [[fireship]] <br/> 

Anthropic officially released Claude 3.7 Sona on February 25, 2025 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This highly anticipated large language model is described as both "most loved and most feared by programmers" <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Early testing indicates that Claude 3.7 has significantly improved its programming capabilities compared to its base model, and it introduces a new "thinking mode" which emulates the success of DeepSeek R1 and OpenAI models <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Claude Code CLI

One of the most notable releases alongside Claude 3.7 is [[claude_code_cli_features_and_capabilities | Claude Code]], a Command Line Interface (CLI) tool designed to build, test, and execute code within any project <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This tool theoretically creates an "infinite feedback loop" that could potentially replace programmers <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Features and Usage
[[claude_code_cli_features_and_capabilities | Claude Code]] is currently in research preview and can be installed via npm <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. It directly utilizes the Anthropic API, which is relatively expensive, costing over 10 times more than models like Gemini Flash and DeepSeek, at $15 per million output tokens <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Once installed, the `claude` command is available in the terminal, granting the AI full context of the existing code in a project <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **`in` command**: Scans the project and generates a Markdown file with initial context and instructions <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **`cost` command**: Allows users to track the cost incurred from prompts <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Code Generation Process
When a prompt is entered, [[claude_code_cli_features_and_capabilities | Claude Code]] identifies the necessary actions and requires user confirmation (yes/no) before proceeding <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. It can generate new files, write them to the file system, and create dedicated testing files <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The use of strongly typed languages and test-driven development allows the AI to validate its code and iteratively refine business logic based on test feedback <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Benchmarks and Performance

Anthropic's research indicates that while AI use for math and coding comprises 37% of prompts, it only accounts for 3.4% of the workforce <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Although AI has not yet taken human programmer jobs, it has significantly impacted platforms like Stack Overflow <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

*   **Web Dev Arena**: Claude 3.5, the previous version, already topped the Web Dev Arena leaderboard <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Software Engineering Benchmark**: This benchmark is human-verified and based on real GitHub issues <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The new Claude 3.7 model achieved a remarkable 70.3% success rate in solving GitHub issues, significantly outperforming other models like OpenAI O3 Mini High and DeepSeek <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Real-World Application and Challenges

### Simple Code Generation
In a test to create a random name generator in Deno, [[claude_code_cli_features_and_capabilities | Claude Code]] successfully wrote "perfect code" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Complex UI Development (Svelte)
For a more complex task, generating a Svelte-based front-end UI that could access a microphone and visualize a waveform, [[claude_code_cli_features_and_capabilities | Claude Code]] showed promising results <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Despite a lengthy confirmation process (around 20 confirmations), it successfully generated multiple new components <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The resulting application allowed interaction with waveform frequency and a circular graphic visualizing sound <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

However, closer inspection revealed issues:
*   The code did not utilize TypeScript or Tailwind, despite being part of the defined tech stack <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   It failed to use the new Svelte 5 Rune syntax <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   The session cost approximately 65 cents <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### End-to-End Encrypted App (JavaScript)
A challenging task was to fix "ChatGPT garbage code" for an end-to-end encrypted app in JavaScript <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Despite significant changes made by [[claude_code_cli_features_and_capabilities | Claude Code]], the application still failed to run <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This highlights a growing concern: reliance on AI can lead to [[programmer_dissatisfaction | programmer dissatisfaction]] when facing errors that one no longer knows how to debug manually, leading to dependence on the next AI model for solutions <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Autonomous AI Coding with Convex

Convex, an open-source reactive database, is highlighted as beneficial for autonomous AI coding <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Its features include:
*   Typesafe queries <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>
*   Scheduled jobs <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>
*   Server functions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>
*   Real-time data sync <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>

Convex's database queries are written in pure TypeScript, providing IDE autocomplete across the entire stack <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This design makes Convex code easier for AI models like Claude to understand and write with fewer errors, thereby increasing productivity <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.