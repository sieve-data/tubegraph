---
title: Improving benchmark systems for accurate evaluation
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

AI benchmarks play a crucial role in shaping market value, investment decisions, and public perception within the artificial intelligence industry <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Billions of dollars are evaluated based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When a company claims the top spot, it influences enterprise contracts, developer mind share, and market dominance <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For instance, Sona acquired Auto Rover due to its strong performance on SWE benchmarks <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. However, this high-stakes environment leads to manipulation and a fundamental crisis in evaluation <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

## What is an AI Benchmark?

A benchmark is typically composed of three key components <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
1.  **A model** being tested <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  **A test set** (a set of questions) <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
3.  **A metric** for scoring <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Crucially, a benchmark combines many individual evaluations and standardizes the test set and metrics across models, making them comparable <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This is analogous to the SAT exam, which uses the same questions and scoring system for different test-takers <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## [[common_strategies_companies_use_to_manipulate_benchmark_results | Challenges and Trust Issues with AI Benchmarks]]

The current system has significant flaws, leading to a situation where a single number can define market leaders <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Key experts, including OpenAI co-founder Andre Karpathy, acknowledge an "evaluation crisis," stating they don't know which metrics to trust <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. John Yang, creator of Sweetbench, admits these benchmarks were "made up," and Martin Sat from CMU describes the yardsticks as "fundamentally broken" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

Common manipulation strategies include:

### 1. Apples-to-Oranges Comparisons
Companies often compare their best-performing configurations against competitors' standard ones <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For example, XAI released benchmark results for Grok 3, showing it beating competitors. However, they compared Grok 3's best configuration (e.g., using consensus at 64, which is more expensive) against other models' standard configurations <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. To ensure fair comparison, models should be evaluated best-to-best or standard-to-standard <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### 2. Privileged Access to Test Questions
Some companies gain unfair advantages by having early or exclusive access to benchmark datasets <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. OpenAI, for instance, funded Frontier Math and received access to its entire dataset <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While there was a verbal agreement not to train on the data, the optics of the funding company evaluating its models internally and announcing scores before independent verification create a trust problem <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### 3. Optimizing for Style Over Substance
Models can be trained to perform well on benchmarks by focusing on stylistic elements rather than accuracy <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Meta entered 27 versions of Llama 4 Maverick into LM Arena, each tweaked for "appeal" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One version, asked to make a riddle, provided a long, emoji-filled, flattering, but nonsensical response that scored higher than a correct, concise answer from Claude <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This happens because models are rewarded for being chatty and engaging, not necessarily correct <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Researchers at LM Arena found that when style effects (like length, formatting, personality) were filtered out, model rankings completely changed, with accurate models like Claude 3.5 Sonnet jumping up, while others dropped <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

This phenomenon is captured by Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. When benchmarks become targets worth billions, they stop measuring what truly matters <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## [[improving_ai_evaluation_methods | Best Practices for AI Evaluation]]

To fix public metrics and ensure genuine progress in AI, a multi-faceted approach is needed:

### 1. For Model Comparisons
*   **Require Apple-to-Apple Comparisons:** Mandate evaluation with the same computational budget and constraints <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Avoid cherry-picking configurations <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Transparent Cost-Performance Trade-offs:** Clearly show the relationship between performance and operational costs <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The Arc Prize is an example of transparent cost-performance reporting <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### 2. For Test Sets
*   **Transparency and Open Source:** Open source the data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **No Financial Ties:** Ensure no financial connections between benchmark creators and the companies whose models are being evaluated <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Regular Rotation:** Implement regular rotation of test questions to prevent models from overfitting to specific datasets <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### 3. For Metrics
*   **Control for Style Effects:** Develop metrics that can distinguish between substantive accuracy and superficial engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. LM Arena's style-controlled rankings are a step in this direction <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   **Public Reporting of All Attempts:** Require all evaluation attempts to be publicly available to prevent cherry-picking of the best results <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made with the emergence of more independent, open-source benchmarks in specific domains, such as LegalBench, MedQA, and FinTech <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Cross-cutting efforts like Agent Eval and BetterBench are also working to benchmark benchmarks themselves <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## [[building_custom_evaluations_for_better_ai_performance | Building Custom Evaluations for Better AI Performance]]

Instead of relying solely on public benchmarks, a more effective strategy is to build a tailored set of evaluations relevant to a specific use case <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This approach focuses on shipping better products rather than just winning a "rigged game" <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

The steps to building effective custom evaluations are:

1.  **Gather Real Data:** Prioritize actual queries and problems from production systems over academic questions <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. Real user problems are invaluable compared to synthetic benchmarks <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
2.  **Choose Your Metrics:** Define metrics (e.g., quality, cost, latency) that are most critical for your specific application <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. A medical diagnosis system, for example, will have different metric priorities than a chatbot <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
3.  **Test the Right Models:** Don't just follow leaderboards <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Test the top models against your specific data, as a model that tops generic benchmarks might fail on domain-specific documents <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
4.  **Systematize It:** Establish consistent, repeatable evaluation processes, either by building in-house tools or using platforms like Scorecard <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating:** Evaluation should be a continuous process, not a one-time event, to adapt to model improvements and changing needs <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

This systematic approach involves identifying issues, building improvements, running evaluations before deployment, and continuously monitoring performance. This pre-deployment evaluation loop is key to shipping reliable AI and avoiding constant firefighting of production issues <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. While it requires more effort than simply checking a leaderboard, it is the only way to build AI that truly serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Ultimately, "All benchmarks are wrong, but some are useful" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The key is to measure what matters to your users, not what sells or gains mind share <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.