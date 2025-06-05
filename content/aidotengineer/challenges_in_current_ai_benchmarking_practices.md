---
title: Challenges in current AI benchmarking practices
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

The game of AI benchmarks is often rigged, with significant players having strong incentives to maintain the status quo <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Darius, CEO of Scorecard, who built evaluation systems for Waymo, Uber ATG (OG [[Challenges in creating effective AI agents | AI agents]]), and SpaceX, notes that his team has observed "every eval trick in the book" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

At its core, a benchmark consists of three components:
*   The model being tested <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   A set of questions, referred to as the test set <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
*   A metric to keep score <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

A benchmark is essentially a bundle of many individual evaluations <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Their key function is to standardize the test set and metrics across different models, making them comparable, similar to the SAT <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Why Benchmarks Control Billions <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>
Benchmark scores significantly influence market value, investment decisions, and public perception <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Simon Willis highlights that billions of dollars in investment are now based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When companies like OpenAI or Anthropic claim the top spot, it affects not only funding but also enterprise contracts, developer mind share, and market dominance <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. A single benchmark result, like Auto Rover's strong performance on SWE, can lead to acquisitions <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This means a single number can define market leaders and eliminate competitors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## [[Common tricks companies use to manipulate AI benchmark results | Common Tricks to Manipulate AI Benchmark Results]]
When the stakes are high, companies employ creative methods to win <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### 1. Apples-to-Oranges Comparisons <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
Companies often compare their best configurations against other models' standard configurations <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For example, XAI released benchmark results for Grok 3, showing it beating competitors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, it was later observed that XAI didn't show OpenAI's 03 model's high performance at "consensus 64" (running the model 64 times and taking the consensus answer), which is much more computationally expensive <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. True performance leadership requires comparing the best to the best, or standard to standard <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This selective reporting is a common issue <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 2. Privileged Access to Test Questions <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
Another controversial trick is gaining privileged access to benchmark test questions <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Frontier Math, an "impossible to game" benchmark for advanced mathematics, was funded by OpenAI, which in turn gained access to its entire dataset <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. While there was a verbal agreement not to train on the data, and OpenAI employees publicly stated it was a "strongly held out evaluation set" <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, the optics are problematic. A company funding a benchmark has access to all questions, evaluates its models internally, and announces scores before independent verification, creating a [[Controversies and trust issues in AI benchmark systems | trust problem]] <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Financial ties between benchmark creators and model companies undermine the entire system <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### 3. Optimizing for Style Over Substance <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
Models can be optimized for style over accuracy, which is a subtle yet significant trick <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Meta, for instance, entered 27 different versions of Llama 4 Maverick into LM Arena, each tweaked for "appeal, not necessarily accuracy" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. An example showed a private version of the model giving a long, emoji-filled, flattering, yet nonsensical response to a math riddle, beating Claude's correct answer simply because it was "chatty and engaging" <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Companies are effectively training models to be "wrong, but charming" <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

Researchers at LM Arena have shown that controlling for style effects (length, formatting, personality) can drastically change rankings, with models like GBD40 Mini and Grok 2 dropping, and Claude 3.5 Sonnet tying for first <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This indicates that benchmarks often measure charm rather than accuracy <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This issue is akin to human SATs, where essay length significantly impacts scores <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The industry currently prioritizes measuring "what sells" over "what matters" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## The Fundamental Problem: Goodhart's Law <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>
These issues are a natural outcome of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. By turning benchmarks into targets worth billions, they have inevitably stopped measuring what truly matters, driven by incentives <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Expert Confirmation <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>
Leaders in AI confirm this [[Controversies and trust issues in AI benchmark systems | evaluation crisis]]:
*   **Andre Karpathy (Co-founder of OpenAI)**: "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **John Yang (Creator of Sweetbench)**: "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Martin Sat (CMU)**: "The yard sticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

When the creators and leaders of AI acknowledge that benchmarks are broken and metrics cannot be trusted, it signals a serious problem <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## How to Fix Public Metrics <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
Addressing the [[Challenges in AI Agent Evaluation | challenges in AI Agent Evaluation]] requires improvements across all three components of a benchmark:

### Model Comparisons
*   Require "apples-to-apples" comparisons: models should have the same computational budget and constraints, with no cherry-picking of configurations <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Transparently show cost-performance trade-offs <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

### Test Sets
*   Demand transparency: open-source data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   Ensure no financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   Implement regular rotation of test questions to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Metrics
*   Control for style effects to measure substance over engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   Require all attempts to be public to prevent cherry-picking of the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made, with LM Arena's style-controlled rankings and the emergence of independent, open-source benchmarks in specific domains like LegalBench, MedQA, and FinTech <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Cross-cutting efforts like Agent Eval and BetterBench are also working to benchmark benchmarks <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## Building Your Own Meaningful Evaluations <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>
To truly win the evaluation game, it's advised to stop chasing public benchmarks and instead build evaluations that are relevant to your specific use case <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This approach helps in [[Challenges in building AI applications | building AI applications]] that are reliable.

Here’s a five-step process:
1.  **Gather Real Data**: Five actual queries from a production system are more valuable than 100 academic questions <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Real user problems consistently outperform synthetic benchmarks <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
2.  **Choose Your Metrics**: Select what truly matters for your application (e.g., quality, cost, latency). A chatbot's metrics differ from a medical diagnosis system <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Test the Right Models**: Don't rely solely on leaderboards. Test the top models on your specific data, as a model that tops generic benchmarks might fail on your unique legal documents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This is critical for [[Challenges in AI agent development | AI agent development]].
4.  **Systematize It**: Implement consistent, repeatable evaluation processes. This can be built in-house or using platforms like Scorecard <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating**: As models improve and needs change, evaluation must be a continuous process, not a one-time event <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

This continuous cycle involves identifying issues, building improvements, running pre-deployment evaluations, getting feedback, and only deploying when quality bars are met <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This "pre-deployment evaluation loop" distinguishes teams that ship reliable AI from those constantly firefighting production issues <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. While more work than checking a leaderboard, it's the only way to build AI that truly serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. This is part of addressing the broader [[Challenges in AI Development | challenges in AI Development]].

The AI benchmarks game is rigged due to the immense stakes involved: market caps, acquisitions, and developer mind share <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. However, companies don't have to participate in this game. Instead, they can build evaluations that genuinely help ship better products by measuring what matters to their users, not just what garners attention on social media <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. All benchmarks are flawed, but some are useful; the key is discerning which ones <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.