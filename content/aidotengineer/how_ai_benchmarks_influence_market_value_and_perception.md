---
title: How AI benchmarks influence market value and perception
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

The way AI benchmarks are currently structured allows them to control billions in market value and mind share, influencing investment decisions and public perception <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Simon Willis highlights that billions of dollars of investment are evaluated based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Influence on the AI Ecosystem
When major players like OpenAI or Anthropic claim the top spot in a benchmark, it impacts not only their funding but also their enterprise contracts, developer mind share, and overall market dominance <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The influence extends to shaping entire ecosystems, as seen when Andre Karpathy, co-founder of OpenAI, tweets about a benchmark to millions of followers <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. A tangible example is Sona's acquisition of Auto Rover, which was driven by Auto Rover's strong performance on the SWE benchmark <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This demonstrates how a single number can define market leaders and potentially destroy competitors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## The Problem: A Rigged Game
The speaker asserts that the AI benchmarks game is "rigged" because the stakes are too high for it not to be <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>, <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>, <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This leads companies to employ creative ways to win, undermining the [[challenges_and_trust_issues_with_ai_benchmarks | trustworthiness of AI benchmarks]].

### Common Tricks to Game Benchmarks
1.  **Apples-to-Oranges Comparisons**: Companies may compare their best-performing, often more expensive, configurations against competitors' standard ones <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. For instance, XAI released Grok 3 benchmark results showing superiority, but they compared their model using high-performance configurations (like consensus at 64, running the model 64 times) against standard configurations of other models without disclosing this difference <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This "selective reporting" misrepresents true performance <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Privileged Access to Test Questions**: Some companies gain early or privileged access to benchmark datasets <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. An example is OpenAI funding Frontier Math and receiving access to its entire dataset <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Even with verbal agreements not to train on the data, the optics of a funding company having access to evaluation questions, performing internal evaluations, and announcing scores before independent verification creates a trust problem <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Optimizing for Style Over Substance**: Models are trained to optimize for style (e.g., chatty, engaging responses) rather than accuracy <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Meta's Llama 4 Maverick entered 27 versions into LM Arena, with some tweaked for "appeal" over "accuracy" <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One version, though incorrect, beat a correct answer from Claude due to its engaging, emoji-filled, flattering response <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This means companies are "literally training models to be wrong, but charming" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Researchers at LM Arena proved that when style effects (length, formatting, personality) are filtered out, rankings change dramatically, revealing that models are often measured for "charm" rather than accuracy <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### The "Evaluation Crisis"
This situation is an "natural outcome" of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Since benchmarks have become targets worth billions, they no longer accurately measure what matters <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. Experts in the field confirm this [[importance_of_evaluation_and_metrics_in_ai_systems | crisis]]:
*   **Andre Karpathy (co-founder of OpenAI)**: "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **John Yang (creator of Sweetbench)**: "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Martin Sat (CMU)**: "The yard sticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
These statements from the very people who build and lead AI indicate a serious problem with the trustworthiness of current metrics <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Fixing Public Metrics
To improve public metrics, adjustments are needed across three components of a benchmark: model comparisons, test sets, and metrics <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. This calls for [[improving_ai_evaluation_methods | improving AI evaluation methods]].

### Recommendations
*   **Model Comparisons**: Require "apples-to-apples" comparisons with the same computational budget and constraints, transparently showing cost-performance trade-offs <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Test Sets**: Demand transparency by open-sourcing data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Crucially, there should be no financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Regular rotation of test questions is also necessary to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Metrics**: Implement controls for style effects to measure substance over engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. All attempts should be public to prevent cherry-picking the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

There is progress, with LM Arena offering style-controlled rankings <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a> and the emergence of independent, open-source benchmarks in specific domains like LegalBench, MedQA, and FinTech <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## Building Useful Internal Evaluations
To truly win the evaluation game, it's advised to "stop playing" the rigged public benchmark game <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. Instead, companies should build [[best_practices_for_ai_evaluation | evaluations]] that directly matter for their specific use cases <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Steps for Effective Internal Evaluation
1.  **Gather Real Data**: Utilize actual queries from production systems, as a few real user problems are more valuable than many academic questions <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
2.  **Choose Your Metrics**: Select metrics relevant to the application, such as quality, cost, and latency. A chatbot's metrics differ from a medical diagnosis system's <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Test the Right Models**: Don't rely solely on leaderboards. Test the top models on your specific data, as a model that excels on generic benchmarks might fail on domain-specific documents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
4.  **Systematize It**: Implement consistent, repeatable evaluation processes, either by building in-house systems or using platforms like Scorecard <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
5.  **Keep Iterating**: Make evaluation a continuous process, adapting as models improve and needs change <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This involves a continuous cycle of identifying issues, building improvements, running evaluations before deployment, gathering feedback, and only deploying when quality bars are met <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

This pre-deployment evaluation loop is crucial for shipping reliable AI and avoiding constant production issues <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. While more work than checking a leaderboard, it's the only way to build AI that truly serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. The fundamental takeaway is that "all benchmarks are wrong, but some are useful. The key is knowing which ones" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.