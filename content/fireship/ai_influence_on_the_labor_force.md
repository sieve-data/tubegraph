---
title: AI influence on the labor force
videoId: x2WtHZciC74
---

From: [[fireship]] <br/> 

The release of Anthropic's Claude 3.7 Sonnet has intensified discussions regarding the [[impact_of_ai_on_job_markets_and_education | impact of AI on job markets]], particularly within the programming sector <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This highly anticipated large language model, described as both loved and feared by programmers, has garnered significant attention due to its advanced capabilities <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Anthropic's Research Findings

A few weeks prior to the Claude 3.7 release, Anthropic published a paper examining how AI affects the labor force <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The study revealed that despite only making up 3.4% of the workforce, over 37% of AI prompts are related to math and coding <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

While AI has not yet displaced human programmer jobs, it has notably taken over tasks previously handled by platforms like Stack Overflow <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This highlights a shift in how information and solutions are being sourced in the programming community.

## Claude 3.7 Sonnet and Claude Code

Claude 3.7 Sonnet is touted as significantly improved for programming <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. It also introduces a new "thinking mode" to emulate the success of models like DeepSeek R1 and Open AI models <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Benchmarking Performance
In the Web Dev Arena, Claude 3.5, the previous version, already held a top position <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. However, the new Claude 3.7 model has "absolutely crushed" all other models, including OpenAI O3 Mini High and DeepSeek, in the software engineering benchmark <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This benchmark is human-verified and based on real GitHub issues <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Claude 3.7 is now reportedly capable of solving 70.3% of GitHub issues <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Claude Code: A CLI Tool
Anthropic also released "Claude Code," a Command Line Interface (CLI) tool designed to build, test, and execute code within any project <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This creates an "infinite feedback loop" that, in theory, "should replace all programmers" <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

> [!WARNING] Cost Consideration
> Installing Claude CLI uses the Anthropic API directly, which is not cheap <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It costs over 10 times more than models like Gemini Flash and DeepSeek, with $15 per million output tokens <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Once installed, the `cla` command in the terminal grants the AI full context of existing code in a project <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Claude Code can scan a project to create an initial context markdown file <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. It prompts for confirmation before generating new files and creates dedicated testing files, which is crucial for validation, especially when using strongly typed languages with test-driven development <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. If a test fails, the AI can use the feedback to rewrite the logic until it's correct <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Real-World Applications and Challenges

### Code Generation Examples
Claude Code has shown promising results in various tasks:
*   **Random Name Generator (Deno):** Successfully created a "perfect" code solution <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Visual Frontend UI (Svelte, TypeScript, Tailwind):** Generated a moderately complex application that accesses a microphone and visualizes a waveform <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. While the end result was functional and visually superior to an OpenAI O3 Mini High attempt, the generated code had issues, such as not using TypeScript or Tailwind despite the specified tech stack, and failing to use the new Svelte 5 Rune syntax <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Limitations and Emerging Dependencies
A more challenging task involved fixing "Chat GPT garbage code" for an end-to-end encrypted application <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. Despite significant changes, the code still failed to run <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This highlights a potential challenge for human programmers: over-reliance on AI can lead to a reduced ability to debug complex error messages independently <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## [[future_implications_of_deepthinking_ai_models_on_programming_jobs | Future Implications]]

The increasing sophistication of AI models like Claude 3.7 and tools like Claude Code suggests a significant [[impact_of_ai_on_coding_and_programming_skills | shift in coding and programming skills]]. The ability of AI to understand and generate code, particularly in type-safe environments, indicates a future where AI could streamline development processes and potentially reduce the need for certain manual coding tasks <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This raises questions about the evolving role of human programmers and the [[impact_of_ai_on_traditional_jobs | broader implications for traditional jobs]] in the software engineering field.