---
title: How AI benchmarks influence market value and public perception
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

AI benchmarks are designed to compare models, but their significant influence extends to market value, investment decisions, and public perception, often leading to a "rigged game" where the biggest players have incentives to maintain the current system <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## What is a Benchmark?
A benchmark is composed of three core components <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:
1.  **Model**: The AI system being tested <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  **Test Set**: A collection of questions or scenarios <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
3.  **Metric**: The method used to keep score <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Crucially, benchmarks standardize the test set and metrics across different models, allowing for comparable results, much like the SAT exam uses the same questions and scoring system for different test takers <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Benchmarks' Control Over Billions
The scores from these benchmarks wield immense power, controlling billions in market value, influencing investment decisions, and shaping public perception <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. According to Simon Willis, billions of dollars of investment are now evaluated based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

When companies like OpenAI or Anthropic claim a top spot in benchmarks, it directly impacts funding, enterprise contracts, developer mind share, and market dominance <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. For example, Andrej Karpathy's tweets about benchmarks can shape entire ecosystems due to his millions of followers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A recent acquisition saw Sona acquire Auto Rover because Auto Rover showed strong results on SWE benchmarks <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This demonstrates how a single number can define market leaders and potentially undermine competitors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## [[common_tricks_companies_use_to_manipulate_ai_benchmark_results | Common Tricks Companies Use to Manipulate AI Benchmark Results]]
When the stakes are high, companies often find "creative ways to win" in the benchmarking game <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### 1. Apples-to-Oranges Comparisons
This trick involves comparing a company's best-configured model against competitors' standard configurations <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Example**: XAI released benchmark results for Grok 3, showing it beating competitors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, it was later discovered that XAI compared their best configuration (e.g., using "consensus at 64," which means running the model 64 times and taking the consensus answer, a much more expensive method) against OpenAI models' standard configurations <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This selective reporting presents a misleading picture of performance <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### 2. Privileged Access to Test Questions
This involves a company gaining early or exclusive access to benchmark test data, potentially undermining the integrity of the evaluation <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **Example**: Frontier Math was promoted as a highly secure benchmark for advanced mathematics <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. However, OpenAI, which funded Frontier Math, gained access to the entire dataset <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. While there was a verbal agreement not to train on the data, and OpenAI employees stated it was a "strongly held out evaluation set," the optics create a [[controversies_and_trust_issues_in_ai_benchmark_systems | trust problem]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. The company funding the benchmark could evaluate its models internally and announce scores before independent verification <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This financial tie between benchmark creators and evaluated companies can undermine the entire system <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### 3. Optimizing for Style Over Substance
Models can be optimized to perform well on style aspects of responses rather than accuracy, especially in human-preferred benchmarks <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Example**: Meta entered 27 different versions of Llama 4 Maverick into LM Arena, each tweaked for "appeal" rather than strict accuracy <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One private version, when asked for a riddle with the answer 3.145, provided a long, emoji-filled, flattering, but nonsensical response <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This "charming" but incorrect answer still beat Claude's correct answer because it was chatty and engaging <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. Companies are effectively training models to be "wrong, but charming" <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   Researchers at LM Arena have shown that filtering out style effects (length, formatting, personality) completely changes rankings <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. When controlled, models like GBD40 Mini and Grok 2 dropped, while Claude 3.5 Sonnet tied for first <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This highlights that benchmarks often measure charm rather than accuracy <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## The Fundamental Problem: Goodhart's Law
The core issue stems from Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Benchmarks have become targets worth billions, leading them to stop measuring what truly matters, an outcome guaranteed by the existing incentives <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Expert Consensus on the Evaluation Crisis
Leading [[influential_ai_researchers | AI researchers]] and benchmark creators acknowledge the severity of the problem:
*   **Andrej Karpathy (Co-founder of OpenAI)**: "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **John Yang (Creator of Sweetbench)**: "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Martin Sat (CMU)**: "The yard sticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

When the creators and leaders of AI admit the metrics are untrustworthy, it signals a serious [[challenges_in_current_ai_benchmarking_practices | problem with AI benchmarking practices]] <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Fixing Public Metrics
To improve public benchmarks, all three components (model comparisons, test sets, and metrics) need reform <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **Model Comparisons**:
    *   Require apple-to-apple comparisons with the same computational budget and constraints, avoiding cherry-picking configurations <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   Transparently show cost-performance trade-offs <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Test Sets**:
    *   Demand transparency through open-sourced data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
    *   Eliminate financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   Implement regular rotation of test questions to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Metrics**:
    *   Control for style effects to measure substance rather than just engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   Require all attempts to be publicly recorded to prevent cherry-picking the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made, with LM Arena developing style-controlled rankings <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Additionally, independent benchmarks are emerging in specific domains, including Legal Bench, MedQA, FinTech, and cross-cutting efforts like Agent Eval and Better Bench, which aim to benchmark the benchmarks themselves <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## Building Effective Internal [[evaluations_versus_traditional_metrics_in_ai | Evaluations]]
Instead of solely relying on public benchmarks, companies can build their own evaluation systems tailored to their specific use cases <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

1.  **Gather Real Data**: Five actual queries from a production system are more valuable than 100 academic questions, as real user problems consistently outperform synthetic benchmarks <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
2.  **Choose Your Metrics**: Select metrics (e.g., quality, cost, latency) that are relevant to the application; a chatbot's needs differ from a medical diagnosis system <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Test the Right Models**: Don't just follow leaderboards. Test the top five models on specific data, as a model excelling in generic benchmarks might fail on domain-specific documents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
4.  **Systematize It**: Establish consistent, repeatable evaluation processes, either by building in-house systems or using platforms like Scorecard <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating**: Evaluation should be a continuous process, not a one-time event, as models improve and needs evolve <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

Scorecard, for instance, implements a continuous pre-deployment evaluation loop: identify issues, build improvements, run evaluations before deployment, get feedback, improve, deploy only when quality bars are met, then monitor and restart the cycle <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This continuous process differentiates teams that ship reliable AI from those constantly firefighting production issues <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. While this requires more effort than checking a leaderboard, it's the only way to build AI that truly serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

The benchmarks game remains rigged due to high stakes like market caps, acquisitions, and developer mind share <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. However, companies can choose to build evaluations that genuinely help them ship better products by measuring what matters to their users, not what sells on social media platforms <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. As the saying goes, "All benchmarks are wrong, but some are useful. The key is knowing which ones" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.