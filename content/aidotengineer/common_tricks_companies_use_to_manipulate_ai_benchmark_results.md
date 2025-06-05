---
title: Common tricks companies use to manipulate AI benchmark results
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

Darius, CEO of Scorecard, with experience in evaluation systems at Waymo, Uber ATG, and SpaceX, highlights how the AI benchmarks game is rigged [00:00:01]. His team works with leaders in AI across various sectors and has observed numerous evaluation tricks [00:00:22].

## Understanding AI Benchmarks
A benchmark is composed of three components: a model being tested, a set of questions (test set), and a metric for scoring [00:00:48]. Benchmarks standardize the test set and metrics across models to make them comparable, similar to the SAT [00:01:04].

### Why Benchmarks Control Billions
These scores control billions in market value, influence investment decisions, and shape public perception [00:01:22]. Simon Willis states that billions of dollars of investment are now evaluated based on these scores [00:01:31]. When companies like OpenAI or Anthropic claim the top spot, it influences funding, enterprise contracts, developer mind share, and market dominance [00:01:40]. Andre Karpathy's tweets about benchmarks, with millions of followers, can shape entire ecosystems [00:01:47]. For example, Sona acquired Auto Rover because it showed strong results on SWE benchmarks [00:01:54]. A single number can thus define market leaders and destroy competitors [00:02:02]. This significant impact leads to incentives for manipulation, contributing to [[How AI benchmarks influence market value and public perception | how AI benchmarks influence market value and public perception]].

## Common Manipulation Tricks
When stakes are high, companies find creative ways to win [00:02:11].

### 1. Apples-to-Oranges Comparisons
This trick involves comparing models with different configurations or computational budgets [00:02:22].
*   **Example: XAI's Grok 3**
    XAI released benchmark results for Grok 3, showing it beating competitors [00:02:27]. However, OpenAI engineers discovered that XAI was comparing their best configuration against other models' standard configurations [00:02:37]. This is akin to comparing a sports car with nitrous boost against regular cars without it [00:02:43]. Specifically, XAI did not show OpenAI's GPT-3 models' high performance at "consensus 64," which involves running the model 64 times and taking a consensus answer [00:02:49]. While "consensus 64" is more expensive, claiming performance leadership requires comparing the best to the best, or standard to standard, not the best against a competitor's standard [00:03:00]. This selective reporting is a common issue [00:03:13].

### 2. Privileged Access to Test Questions
This more controversial trick involves gaining early or exclusive access to benchmark data sets, which can lead to [[Controversies and trust issues in AI benchmark systems | controversies and trust issues in AI benchmark systems]].
*   **Example: OpenAI and Frontier Math**
    Frontier Math was designed as a super-secret, difficult-to-game benchmark for advanced mathematics [00:03:25]. However, OpenAI, which funded Frontier Math, gained access to the entire data set [00:03:38]. While there was a verbal agreement not to train on the data, and OpenAI employees publicly stated it was a "strongly held out evaluation set" [00:03:47], the optics create a trust problem [00:03:55]. The company funding the benchmark could see all questions, evaluate their models internally, and announce scores before independent verification [00:03:57]. When OpenAI announced GPT-3 had scored a "surprisingly strong 25%" [00:04:06], it raised eyebrows. When benchmark creators accept money from the companies they evaluate, it undermines the entire system [00:04:20].

### 3. Optimizing for Style Over Substance
This subtle trick involves models being optimized for appealing style rather than accuracy [00:04:35].
*   **Example: Meta's Llama 4 Maverick and LM Arena**
    Meta released Llama 4 Maverick publicly, but entered 27 different private versions into LM Arena, each tweaked to maximize appeal, not necessarily accuracy [00:04:40]. One private version, when asked to make a riddle with the answer 3.145, gave a long, emoji-filled, flattering, but nonsensical response [00:04:53]. This answer beat Claude's correct response because it was chatty and engaging, not because it was right [00:05:04]. Companies are training models to be "wrong, but charming" [00:05:09]. Researchers at LM Arena proved this can be controlled for; when they filtered out style effects (length, formatting, personality), rankings completely changed [00:05:14]. GPT-4o Mini and Grok 2 dropped, while Claude 3.5 Sonnet jumped to tie for first [00:05:22]. This indicates that current public benchmarks often measure which model is most charming, not most accurate [00:05:30]. This issue is even present in human SATs, where 39% of score variance is attributed to essay length [00:05:40]. The industry often measures "what sells" over "what matters" [00:05:50].

## The Fundamental Problem: Goodhart's Law
All these issues are an outcome of Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" [00:05:57]. Benchmarks have become targets worth billions, leading them to stop measuring what truly matters [00:06:09].

Experts acknowledge this issue, highlighting [[Challenges in current AI benchmarking practices | challenges in current AI benchmarking practices]]:
*   **Andre Karpathy (Co-founder of OpenAI)**: "My reaction is that there is an evaluation crisis. I don't really know what metrics to look at right now" [00:06:26].
*   **John Yang (Creator of Sweetbench)**: "It's sort of like we kind of just made these benchmarks up" [00:06:40].
*   **Martin Sat (CMU)**: "The yard sticks are like pretty fundamentally broken" [00:06:44].

When the creators and leaders of AI acknowledge that benchmarks are broken and metrics cannot be trusted, it signals a serious problem [00:06:53].

## Fixing Public Metrics
To fix public metrics, all three components of a benchmark (model comparisons, test sets, and metrics) need to be addressed [00:07:06]. This forms part of [[Strategies for AI evaluation and troubleshooting | strategies for AI evaluation and troubleshooting]].

*   **Model Comparisons**: Require "apples-to-apples" comparisons with the same computational budget and constraints, no cherry-picking configurations [00:07:14]. Cost-performance trade-offs should be transparently shown [00:07:24].
*   **Test Sets**: Demand transparency, open-sourcing data, methodologies, and code [00:07:34]. There should be no financial ties between benchmark creators and model companies [00:07:39]. Regular rotation of test questions is necessary to prevent overfitting [00:07:45].
*   **Metrics**: Implement controls for style effects to measure substance over engagement [00:07:51]. All attempts should be publicly required to prevent cherry-picking the best run [00:07:59].

Progress is being made, with LM Arena's style-controlled rankings offering a way to remove style as a component [00:08:11]. Independent benchmarks in specific domains like Legal Bench, MedQA, and Fintech are emerging [00:08:20].

## Building Effective Internal Evaluations
Instead of chasing rigged public benchmarks, companies should build a set of evaluations that matter for their specific use case [00:08:53]. This aligns with [[Strategies for effective AI implementation | strategies for effective AI implementation]].

Here's how to build custom evaluations:
1.  **Gather Real Data**: Five actual queries from a production system are more valuable than 100 academic questions, as real user problems surpass synthetic benchmarks [00:09:04].
2.  **Choose Your Metrics**: Select quality, cost, and latency metrics relevant to the application [00:09:21]. A chatbot needs different metrics than a medical diagnosis system [00:09:27].
3.  **Test the Right Models**: Don't rely solely on leaderboards [00:09:34]. Test the top five models on specific data, as a model excelling on generic benchmarks might fail on domain-specific documents [00:09:37].
4.  **Systematize It**: Build consistent, repeatable evaluation processes internally or use a platform like Scorecard [00:09:47].
5.  **Keep Iterating**: Evaluation should be a continuous process, not a one-time event, as models and needs evolve [00:09:55].

Scorecard employs a continuous workflow: identify issues, build improvements, run evaluations before deployment, get feedback, improve, and deploy only when quality bars are met, then monitor and restart the cycle [00:10:05]. This pre-deployment evaluation loop distinguishes teams that ship reliable AI from those constantly firefighting production issues [00:10:25]. While more work, this is the only way to build AI that truly serves users [00:10:37]. This continuous iteration supports [[Strategies to Mitigate AI Errors | strategies to mitigate AI errors]].

## Conclusion
The AI benchmarks game is rigged due to the high stakes involved, including market capitalization, acquisitions, and developer mind share [00:10:45]. However, companies don't have to play this game [00:10:54]. By building evaluations that measure what matters to their users, rather than what gains attention on social media, they can ship better products [00:10:57]. The key is understanding that "all benchmarks are wrong, but some are useful," and knowing which ones are valuable [00:11:04].