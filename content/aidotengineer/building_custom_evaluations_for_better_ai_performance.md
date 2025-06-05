---
title: Building custom evaluations for better AI performance
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

Public AI benchmarks are often criticized for being rigged, with significant incentives for major players to maintain the status quo <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. According to Darius, CEO of Scorecard, who built evaluation systems for autonomous cars at Waymo and Uber ATG, and for rockets at SpaceX, and holds patents on evaluating autonomous systems, companies across legal tech, health tech, and finance have employed various "eval tricks" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Influence and Flaws of Public Benchmarks

A benchmark is defined by three components: the model being tested, a test set of questions, and a metric for scoring <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The crucial aspect is that benchmarks standardize the test set and metrics across models to allow for comparability, similar to the SAT <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

However, these scores wield immense influence, controlling billions in market value, investment decisions, and public perception <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Simon Willis noted that billions of dollars are evaluated based on these scores <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. When a company like OpenAI or Anthropic claims the top spot, it affects funding, enterprise contracts, developer mind share, and market dominance <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. A single benchmark score can define market leaders and dismantle competitors <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. For example, Sona acquired Auto Rover largely because it showed strong results on SWE <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### Common Tricks to Game the System

When the stakes are high, companies find "creative ways to win" <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

#### 1. Apples-to-Oranges Comparisons
This trick involves comparing the best configuration of one model against the standard configuration of another <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Example:** XAI released benchmark results for Grok 3, showing it beating competitors <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, OpenAI engineers found that XAI compared their best configuration against other models' standard configurations <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. They specifically omitted showing OpenAI's GPT-3 models' high performance at "consensus 64," which involves running the model 64 times and taking the consensus answer, a much more expensive process <a class="yt-timestamp" data-t="00:02:49">[00:03:00]</a>. Claiming performance leadership requires comparing best-to-best or standard-to-standard <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

#### 2. Privileged Access to Test Questions
This trick involves companies gaining early or exclusive access to benchmark data <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Example:** Frontier Math was promoted as a highly protected benchmark for advanced mathematics <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. However, OpenAI, which funded Frontier Math, gained access to the entire dataset <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Although there was a verbal agreement not to train on the data, and OpenAI employees publicly called it a "strongly held out evaluation set," the optics create a trust problem <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. A company funding a benchmark seeing all questions, evaluating models internally, and announcing scores before independent verification undermines the system <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

#### 3. Optimizing for Style Over Substance
Models can be optimized to perform well on style rather than accuracy <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Example:** Meta entered 27 different versions of Llama 4 Maverick into LM Arena, each tweaked for maximum appeal, not necessarily accuracy <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. One version, when asked for a riddle with the answer "3.145", gave a long, emoji-filled, flattering, nonsensical response that still beat Claude's correct answer because it was "chatty and engaging" <a class="yt-timestamp" data-t="00:04:53">[00:05:01]</a>. This means companies are "literally training models to be wrong, but charming" <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   Researchers at LM Arena showed that filtering out style effects (length, formatting, personality) completely changed rankings, with GBD40 Mini and Grok 2 dropping, and Claude 3.5 Sonnet jumping to tie for first <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This indicates that benchmarks often measure charm rather than accuracy, akin to choosing a surgeon based on bedside manner instead of skill <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   Even human SATs have this issue, with 39% of score variance being attributed to essay length; writing more generally leads to higher scores <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   The industry tends to measure "what sells" rather than "what matters" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### The "Evaluation Crisis"

The fundamental problem is Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Benchmarks have become billion-dollar targets, naturally leading them away from measuring what truly matters <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

Experts and creators of these benchmarks acknowledge the problem:
*   **Andre Karpathy (Co-founder of OpenAI):** "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
*   **John Yang (Creator of Sweetbench):** "It's sort of like we kind of just made these benchmarks up" <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Martin Sat (CMU):** "The yard sticks are like pretty fundamentally broken" <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Fixing Public Metrics for [[improving_ai_evaluation_methods | Improving AI Evaluation Methods]]

To address the issues with public metrics, improvements are needed across model comparisons, test sets, and metrics <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

*   **Model Comparisons:** Require "apples-to-apples" comparisons with the same computational budget and constraints, avoiding cherry-picking configurations <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Cost-performance trade-offs should be transparently displayed, as seen in the Arc Prize <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Test Sets:** Demand transparency, open-sourcing data, methodologies, and code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. There should be no financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Regular rotation of test questions is necessary to prevent overfitting <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Metrics:** Implement controls for style effects to measure substance over engagement <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. All attempts should be publicly required to prevent cherry-picking the best run <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

Progress is being made through LM Arena's style-controlled rankings and the emergence of independent, domain-specific benchmarks like LegalBench, MedQA, and FinTech <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Cross-cut coding efforts like AgentEval and BetterBench are also working to benchmark benchmarks <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

## [[Building custom evaluations for better AI performance | Building Custom Evaluations]] for Specific Use Cases

Instead of chasing public benchmarks, a more effective approach is to [[custom_model_building_and_code_evaluation_for_ai_systems | build a set of evaluations]] that directly matter for a specific use case <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Steps to [[best_practices_for_ai_evaluation | Building and Improving AI Agents]] through Custom Evaluations

1.  **Gather Real Data:** Use actual queries from your production system. Five real user problems are more valuable than 100 academic questions <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
2.  **Choose Your Metrics:** Select metrics (e.g., quality, cost, latency) relevant to your application. A chatbot needs different metrics than a medical diagnosis system <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
3.  **Test the Right Models:** Don't rely solely on leaderboards. Test the top five models against your specific data, as a model that tops generic benchmarks might fail on your unique legal documents <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
4.  **Systematize It:** Establish consistent, repeatable [[implementation_of_evaluation_platforms_for_ai_agents | evaluation platforms for AI agents]]. This can be built in-house or using platforms like Scorecard <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
5.  **Keep Iterating:** Since models and needs evolve, make [[evaluating_ai_agent_performance_and_reliability | evaluation of AI agent performance and reliability]] a continuous process, not a one-time event <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

At Scorecard, this process forms a continuous workflow: identify issues, build improvements, run [[testing_and_evaluation_of_ai_models | evaluations of AI models]] before deployment, get feedback, improve, and deploy only when quality bars are met <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This pre-deployment evaluation loop distinguishes teams that ship reliable AI from those constantly firefighting production issues <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. While this requires more effort than checking a leaderboard, it is the only way to build AI that genuinely serves users <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

Ultimately, all benchmarks can be flawed, but some are useful <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The key is to know which ones, and to measure what truly matters to your users, not what sells on public forums <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.