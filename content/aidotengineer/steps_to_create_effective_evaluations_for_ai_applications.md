---
title: Steps to create effective evaluations for AI applications
videoId: EnT4Wej5M5k
---

From: [[aidotengineer]] <br/> 

Public benchmarks for AI systems, while seemingly useful, are often prone to manipulation and can be misleading, controlling billions in market value and public perception <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This environment creates an [[challenges_in_ai_agent_evaluation | evaluation crisis]] where even experts question which metrics to trust <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. Instead of chasing these potentially "rigged" public benchmarks, the focus should shift to building custom evaluations tailored to specific use cases <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a>.

## Understanding Benchmarks

A benchmark is composed of three main elements <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>:
1.  **Model**: The AI system being tested <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
2.  **Test Set**: A collection of questions or data used for testing <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>.
3.  **Metric**: The method by which the score is kept <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

The key insight is that benchmarks standardize the test set and metrics across various models to enable comparability, similar to how the SAT uses the same questions and scoring system for different test-takers <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

## The Flaws of Public AI Benchmarks

When billions of dollars in investment, enterprise contracts, and developer mind share hinge on benchmark scores, there's a strong incentive for companies to manipulate the system <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. Common "tricks" include:

*   **Apples-to-Oranges Comparisons**: Companies may compare their best, often more expensive, configurations against competitors' standard ones, selectively reporting results to appear superior <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. For example, XAI released benchmarks for Grok 3 showing it beating competitors, but they were comparing their best configuration (using consensus at 64, running the model 64 times) against standard configurations of other models <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
*   **Privileged Access to Test Questions**: Organizations funding benchmarks may gain early or full access to test data, allowing them to evaluate their models internally and announce scores before independent verification <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>. This creates a trust problem, even if no explicit training on the data occurs <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   **Optimizing for Style Over Substance**: Models can be trained to produce chatty, engaging, or flattering responses that appeal to evaluators, even if the content is incorrect <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. Research shows that filtering out style effects (length, formatting, personality) can completely change model rankings, indicating that often, "we're measuring which model is most charming" instead of most accurate <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.

These issues highlight Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure" <a class="yt-timestamp" data-t="06:03:00">[06:03:00]</a>. Experts like Andrej Karpathy and John Yang acknowledge an [[evaluations_versus_traditional_metrics_in_ai | evaluation crisis]] and that current benchmarks are "pretty fundamentally broken" <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.

## Principles for Fixing Public AI Metrics

To improve public metrics, it's necessary to address their three components <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>:
*   **Model Comparisons**: Require "apples-to-apples" comparisons with the same computational budget and constraints, no cherry-picking, and transparently show cost-performance trade-offs <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.
*   **Test Sets**: Demand transparency through open-sourced data, methodologies, and code, with no financial ties between benchmark creators and model companies <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>. Regular rotation of test questions is also crucial to prevent overfitting <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.
*   **Metrics**: Implement controls for style effects to measure substance over engagement <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. All attempts should be publicly disclosed to prevent cherry-picking the best run <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.

Progress is being made with style-controlled rankings in platforms like LM Arena and the emergence of independent, open-source benchmarks in specific domains like legal tech, health tech, and finance <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

## Building Custom, Effective AI Evaluations

Instead of relying on flawed public benchmarks, organizations should create a set of [[importance_of_evaluations_in_ai_projects | evaluations]] that genuinely matter for their specific use case <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.

### Five Steps to Effective Custom Evaluations

1.  **Gather Real Data**: Focus on actual queries from your production system. Five real user problems are significantly more valuable than 100 academic questions, as they reflect genuine needs <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
2.  **Choose Your Metrics**: Define what truly matters for your application. This might include quality, cost, or latency. A chatbot, for example, requires different metrics than a medical diagnosis system <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
3.  **Test the Right Models**: Do not solely depend on public leaderboards. Test the top five models directly on your specific data. A model like GPT-4 might excel on generic benchmarks but fail when applied to your unique legal documents <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a>.
4.  **Systematize It**: Establish consistent and repeatable [[evaluating_ai_system_performance | evaluation]] processes. This can be built internally or by utilizing a dedicated platform like Scorecard <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.
5.  **Keep Iterating**: Recognize that models evolve and business needs change. [[evaluations_and_finetuning_in_ai_development | Evaluation]] should be a continuous process, not a one-time event <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

### The Continuous Evaluation Workflow

A robust [[strategies_for_ai_evaluation_and_troubleshooting | evaluation strategy]] integrates seamlessly into the AI development lifecycle <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>:
*   **Identify Issues**: Pinpoint problems within your AI system.
*   **Build Improvements**: Develop solutions based on identified issues.
*   **Run Evaluations Before Deployment**: Critically, evaluations are performed *before* new versions are deployed to production <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   **Continuous Cycle**: This creates a cycle where you run evaluations, get feedback, improve the model, and only deploy once your quality bar is met. Post-deployment, monitoring continues, leading to further iterations <a class="yt-timestamp" data-t="10:16:00">[10:16:00]</a>.

This pre-deployment [[evaluating_ai_systems_at_scale | evaluation loop]] is crucial for teams that consistently ship reliable AI, preventing constant firefighting of production issues <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>. While this approach demands more effort than merely checking a leaderboard, it is the only way to build AI that truly serves its users <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.

## Conclusion

The benchmarks game is heavily influenced by high stakes like market capitalization, acquisitions, and developer mind share <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. However, companies don't have to participate in this rigged system. By building custom [[role_of_human_and_automated_evaluators_in_ai_assessment | evaluations]] that measure what matters to *your users* rather than what generates buzz, organizations can ship superior products and achieve effective [[strategies_for_effective_ai_implementation | AI implementation]] <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. As the saying goes, "All benchmarks are wrong, but some are useful. The key is knowing which ones" <a class="yt-timestamp" data-t="11:04:00">[11:04:00]</a>.