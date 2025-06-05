---
title: Challenges and trust issues with AI benchmarks
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

AI benchmarks, while intended to provide comparable metrics for artificial intelligence models, are often criticized for being "rigged" due to high stakes and misaligned incentives <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## What Are AI Benchmarks?

An AI benchmark is comprised of three core components <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
1.  **A model being tested** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  **A test set** (a set of questions) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
3.  **A metric** (how the score is kept) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Crucially, benchmarks standardize the test set and metrics across different models, enabling comparability, similar to how the SAT provides a standardized test for different students <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## How AI Benchmarks Influence Market Value and Perception

Scores derived from AI benchmarks control billions in market value, investment decisions, and public perception <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Investment and Funding** Billions of dollars are now evaluated based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Market Dominance** When companies like OpenAI or Anthropic claim the top spot, it influences enterprise contracts, developer mind share, and overall market dominance <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Acquisitions** For example, Sona acquired Auto Rover because Auto Rover showed strong results on the SWE benchmark <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Ecosystem Shaping** A tweet from a prominent figure like Andrej Karpathy about a benchmark can shape entire ecosystems <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

This system, where a single number can define market leaders, creates an environment ripe for manipulation <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This directly impacts [[how_ai_benchmarks_influence_market_value_and_perception | how AI benchmarks influence market value and perception]].

## Common Tricks and [[Challenges with Current AI Implementation | Challenges with Current AI Implementation]]

When the stakes are high, companies find creative ways to win <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### 1. Apples-to-Oranges Comparisons

Companies may compare their best, highly-optimized configurations against other models' standard configurations, leading to misleading results <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Example: XAI's Grok 3** XAI released benchmark results for Grok 3, showing it beating competitors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, OpenAI engineers noticed that XAI was comparing their best configuration (e.g., using consensus at 64, which is much more expensive) against other models' standard configurations, without transparently showing comparable high-performance results for competitors like OpenAI's GPT-3 <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This selective reporting can distort the true performance picture <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 2. Privileged Access to Test Questions

Gaining early or exclusive access to benchmark test data can give a significant, unfair advantage <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Example: Frontier Math** Frontier Math was intended as a secret, difficult benchmark for advanced mathematics <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. However, OpenAI, which funded Frontier Math, gained access to the entire dataset <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While there was a verbal agreement not to train on the data, and OpenAI employees called it a "strongly held out evaluation set," the optics create a trust problem <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. A company funding a benchmark, seeing all questions, evaluating models internally, and then announcing scores before independent verification undermines the system's integrity <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This contributes to the [[ai_trust_gap_in_user_experiences | AI trust gap in user experiences]].

### 3. Optimizing for Style Over Substance

Models can be optimized to perform well on benchmarks by focusing on superficial characteristics rather than accuracy, such as being chatty or engaging <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Example: Meta Llama 4 Maverick and LM Arena** Meta entered 27 tweaked versions of Llama 4 Maverick into LM Arena, each designed to maximize appeal rather than accuracy <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One version, when asked a riddle with a numerical answer, provided a long, emoji-filled, flattering, but nonsensical response that beat Claude's correct answer simply because it was chatty and engaging <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Impact** Companies are training models to be "wrong but charming" <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. When LM Arena researchers filtered out style effects (length, formatting, personality), rankings changed dramatically: GPT-4o Mini and Grok-2 dropped, while Claude 3.5 Sonnet jumped to tie for first <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This indicates benchmarks often measure charm rather than accuracy, akin to choosing a surgeon based on bedside manner instead of skill <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Even human SATs suffer from this; 39% of score variance is due to essay length <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The industry currently prefers measuring what sells over what truly matters <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## The Fundamental Problem: Goodhart's Law

These issues are a natural outcome of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Benchmarks have become targets worth billions, leading them to stop measuring what actually matters because the incentives guarantee it <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Expert Consensus on the Evaluation Crisis

Leaders in the AI field acknowledge the severity of the problem:
*   **Andrej Karpathy (Co-founder of OpenAI):** "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **John Yang (Creator of Sweetbench):** "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Martin Sat (CMU):** "The yard sticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

When benchmark builders and AI leaders distrust the metrics, it signals a serious problem <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Fixing Public Metrics

To address the [[challenges_in_ai_agent_evaluation | challenges in AI agent evaluation]], solutions require addressing all three components of a benchmark:
1.  **Model Comparisons**
    *   Require "apples-to-apples" comparisons with the same computational budget and constraints <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   Avoid cherry-picking configurations and transparently show cost-performance trade-offs <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
2.  **Test Sets**
    *   Require transparency by open-sourcing data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
    *   Eliminate financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   Implement regular rotation of test questions to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
3.  **Metrics**
    *   Control for style effects to measure substance, not just engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   Require all attempts to be public, preventing cherry-picking of the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made with style-controlled rankings like LM Arena and the emergence of independent, open-source benchmarks in specific domains (e.g., LegalBench, MedQA, FinTech) <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Cross-cut efforts like Agent Eval and Better Bench are also emerging to benchmark benchmarks themselves <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## Building Relevant Internal Evaluations: [[Best Practices for AI Evaluation | The Better Way]]

Instead of chasing potentially rigged public benchmarks, a better approach is to build evaluations that matter for your specific use case <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This approach directly addresses [[challenges_in_building_reliable_ai_agents | challenges in building reliable AI agents]].

Here's a five-step process:
1.  **Gather Real Data** <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>
    *   Five actual queries from a production system are more valuable than 100 academic questions <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Real user problems consistently outperform synthetic benchmarks <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
2.  **Choose Your Metrics** <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>
    *   Identify metrics like quality, cost, or latency that are crucial for your application <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. A chatbot needs different metrics than a medical diagnosis system <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
3.  **Test the Right Models** <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>
    *   Don't rely solely on leaderboards <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Test the top models on your specific data <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. A model like GPT-4 might top generic benchmarks but fail on specialized legal documents <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
4.  **Systematize It** <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>
    *   Build consistent, repeatable evaluation processes, either in-house or using platforms <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating** <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>
    *   Models and needs evolve, so evaluation should be a continuous process, not a one-time event <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

This iterative approach, involving identifying issues, building improvements, running evaluations before deployment, and continuous monitoring, is crucial for shipping reliable AI rather than constantly fighting production issues <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. While more work than checking a leaderboard, it is the only way to build AI that truly serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

The benchmarks game is rigged due to the immense stakes involved. However, companies can choose to build evaluations that genuinely help them ship better products by measuring what matters to their users, not just what garners attention on social media <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. As the saying goes, "All benchmarks are wrong, but some are useful," and the key is discerning which ones <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.