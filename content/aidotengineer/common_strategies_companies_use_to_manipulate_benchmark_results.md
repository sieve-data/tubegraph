---
title: Common strategies companies use to manipulate benchmark results
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

AI benchmarks are a critical component in the AI industry, controlling billions in market value, influencing investment decisions, and shaping public perception <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. When major players like OpenAI or Anthropic claim a top spot, it impacts enterprise contracts, developer mind share, and market dominance <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, Sona acquired Auto Rover because it showed strong results on SWE benchmarks <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This highlights a system where a single number can define market leaders and destroy competitors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

A benchmark consists of three main components:
1.  **A model being tested** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
2.  **A test set (questions)** <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.
3.  **A metric (how the score is kept)** <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

The key insight is that benchmarks standardize the test set and metrics across models, making them comparable, similar to the SAT <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. However, when the stakes are high, companies employ various strategies to manipulate benchmark results <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Common Tricks to Gain the System

### 1. Apples-to-Oranges Comparisons
This trick involves comparing a company's best-configured model against other models' standard configurations <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. For instance, XAI released benchmark results for Grok 3, showing it beating competitors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, it was later observed that XAI did not show OpenAI's GPT-3's high performance at "consensus 64," which involves running the model 64 times and taking the consensus answer <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. While more expensive, claiming performance leadership requires comparing "best to best" or "standard to standard," not mixing configurations <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### 2. Privileged Access to Test Questions
This strategy involves gaining early or exclusive access to benchmark data <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. Frontier Math, a benchmark for advanced mathematics, was supposed to be highly protected <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. However, OpenAI funded Frontier Math and gained access to the entire dataset <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Despite verbal agreements not to train on the data and public statements calling it a "strongly held out evaluation set," the optics create a [[challenges_and_trust_issues_with_ai_benchmarks | trust problem]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The company funding the benchmark can see all questions, evaluate models internally, and announce scores before independent verification <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This undermines the entire system when benchmark creators accept money from the companies they are evaluating <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### 3. Optimizing for Style Over Substance
Models can be optimized to perform well on human preference benchmarks by focusing on stylistic elements rather than accuracy <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Meta, for example, entered 27 different versions of Llama 4 Maverick into LM Arena, each tweaked to maximize appeal, not necessarily accuracy <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One private version gave a long, emoji-filled, flattering response that made no sense but beat Claude's correct answer because it was chatty and engaging <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

This means companies are training models to be "wrong, but charming" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Researchers at LM Arena proved this can be controlled; when style effects (length, formatting, personality) were filtered out, rankings completely changed <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. GPT-4o Mini and Grok 2 dropped, while Claude 3.5 Sonnet jumped up and tied for first <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This indicates that current public benchmarks often measure which model is most charming, not most accurate <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. The industry prefers measuring what sells rather than what matters <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## The Fundamental Problem: Goodhart's Law
These issues are a natural outcome of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Benchmarks have become targets worth billions, leading them to stop measuring what truly matters because the incentives guarantee it <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Expert Consensus on Broken Benchmarks
Experts and creators of these benchmarks acknowledge the problem:
*   **Andre Karpathy (Co-founder of OpenAI):** "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **John Yang (Creator of Sweetbench):** "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **Martin Sat (CMU):** "The yardsticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

When the very people who build and lead AI models distrust the [[challenges_and_trust_issues_with_ai_benchmarks | metrics]], it signifies a serious problem <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## How to Fix Public Metrics
To improve [[improving_benchmark_systems_for_accurate_evaluation | public benchmarks]]:
*   **Model Comparisons**: Require "apples-to-apples" comparisons with the same computational budget and constraints, no cherry-picking configurations, and transparent cost-performance trade-offs <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Test Sets**: Demand transparency, open-source data, clear methodologies and code, and no financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. Regular rotation of test questions is also needed to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Metrics**: Implement controls for style effects to measure substance over engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. All attempts should be made public to prevent cherry-picking the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made with LM Arena's style-controlled rankings and the emergence of more independent, open-source benchmarks in specific domains like Legal Bench, MedQA, Fintech, Agent Eval, and Better Bench <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

## Building Evaluations That Actually Matter
Instead of chasing public benchmarks, companies should focus on building evaluations that truly matter for their specific use case <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. This approach involves:

1.  **Gather Real Data**: Use actual queries from your production system, as real user problems are more valuable than synthetic benchmarks <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
2.  **Choose Your Metrics**: Select [[metrics_for_rag_evaluation | metrics]] (e.g., quality, cost, latency) that are relevant to your application; a chatbot needs different metrics than a medical diagnosis system <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Test the Right Models**: Don't rely solely on leaderboards; test the top models on your specific data, as a model that tops generic benchmarks might fail on your unique legal documents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
4.  **Systematize It**: Establish consistent, repeatable evaluation processes, either by building in-house or using a platform <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating**: Make evaluation a continuous process, not a one-time event, as models improve and needs change <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

This continuous pre-deployment evaluation loop, including identifying issues, building improvements, running evaluations, and monitoring post-deployment, is essential for teams that ship reliable AI rather than constantly firefighting production issues <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. While this requires more effort than simply checking a leaderboard, it is the only way to build AI that genuinely serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Ultimately, the [[how_ai_benchmarks_influence_market_value_and_perception | benchmarks game]] is rigged due to the high stakes involved, including market caps, acquisitions, and developer mind share <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. However, companies can choose to build evaluations that help them ship better products by measuring what matters to their users, not what sells on public forums <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.