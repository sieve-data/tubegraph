---
title: Challenges and testing with language models
videoId: x2WtHZciC74
---

From: [[fireship]] <br/> 

Language models, particularly in the realm of programming, present various challenges related to their performance, cost, and the veracity of their output. Evaluating their effectiveness requires specific benchmarks and practical testing.

## Performance Evaluation and Benchmarks

Assessing the performance of large language models (LLMs) is crucial, though it can be difficult to keep track of the numerous [[google_open_source_ai_models | AI models]] available <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. For web development, Web Dev Arena serves as a good indicator of performance <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Software Engineering Benchmark
The Software Engineering Benchmark is another important evaluation tool <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This benchmark is human-verified and based on real GitHub issues <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Claude 3.5, a previous version, was competitive with other state-of-the-art models on this benchmark <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. The newer Claude 3.7 model significantly outperformed other models, including [[comparison_of_llama_31_with_openais_gpt_models | OpenAI's]] O3 Mini High and Deep Seek, solving 70.3% of GitHub issues <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The credibility of these benchmarks can be further validated through practical use <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Practical Testing and Limitations

Testing LLMs, such as Claude, can be expensive, burning through millions of tokens <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The Anthropic API for Claude is notably costly, being over 10 times more expensive than models like Gemini Flash and DeepSeek, at $15 per million output tokens <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Code Generation Challenges
When generating code, models like Claude Code can create files and dedicated testing files, which is crucial for validating code written by AI <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The process allows for an iterative feedback loop where failed tests lead to code rewrites until it functions correctly <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

However, even advanced models exhibit limitations:
*   **Inconsistent Tool Adherence**: When prompted to build a frontend UI, Claude failed to use Typescript or Tailwind CSS, despite knowing they were part of the text stack <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. It also didn't use the new Svelte 5 Rune syntax <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Cost of Iteration**: A single session for a moderately complex UI cost about 65 cents <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **Difficulty with Complex Tasks**: Attempts to have Claude Code fix "garbage code" for an end-to-end encrypted application in JavaScript failed, leaving the code non-functional <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This highlights a dependency issue where users might struggle to fix errors without AI assistance <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Broader Implications
Despite these challenges, AI is increasingly impacting the labor force. A paper by Anthropic indicated that while AI makes up only 3.4% of the workforce, over 37% of prompts are related to math and coding <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. While AI hasn't fully replaced human programmers, it has significantly impacted resources like Stack Overflow <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The goal of tools like Claude Code, which creates an infinite feedback loop for code building, testing, and execution, is to theoretically replace programmers <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.