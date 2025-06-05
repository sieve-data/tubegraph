---
title: Testing and evaluation of AI models
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

Anthropic, an AI safety and research company, focuses on building the world's best and safest large language models (LLMs) <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. Their Sonnet 3.5 model, launched in late October of the previous year, is recognized as a leading model in the code space, topping leaderboards for agentic coding evaluations like sbench <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

A core differentiating factor for Anthropic is their interpretability research, which involves reverse engineering models to understand their thought processes and steer them for specific use cases <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>. This research progresses through stages:
*   **Understanding**: Grasping AI decision-making <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Detection**: Identifying specific behaviors and labeling them <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Steering**: Influencing AI input <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
*   **Explainability**: Unlocking business value from interpretability methods <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
This deep understanding contributes to significant improvements in AI safety, reliability, and usability <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

## Anthropic's Approach to Customer Success and Evaluation

The Applied AI team at Anthropic works at the intersection of product research, customer interaction, and internal research <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. They provide technical support for use cases, assisting with architecture design, evaluations, and prompt tweaking to optimize model performance <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. Insights gained from customer interactions are fed back into Anthropic to improve products <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

The team closely collaborates with customers facing niche challenges, helping them apply the latest research and maximize model output through prompting <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. This often involves:
1.  Kicking off a Sprint when customers encounter tricky challenges, such as LLM Ops architectures or evaluations <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
2.  Helping define key metrics for evaluating the model against specific use cases <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
3.  Assisting in deploying the iterative loop into an A/B test environment and eventually into production <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
The importance of evaluations is a crucial part of this process <a class="yt-timestamp" data-t="10:42:00">[10:42:00]</a>.

### Case Study: Intercom's Finn AI Agent

Intercom, an AI customer service platform, developed an AI agent named Finn <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>. Anthropic partnered with Intercom to enhance Finn's capabilities:
*   **Initial Sprint**: An Applied AI lead worked with Intercom's data science team on a two-week sprint, comparing Finn's hardest prompt against a Claude-assisted prompt <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.
*   **Optimization Phase**: Following positive initial results, a two-month sprint focused on fine-tuning and optimizing all of Intercom's prompts for Claude's best performance <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
*   **Outcome**: Anthropic's model outperformed the previous LLM in benchmarks <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>. Intercom subsequently launched Finn 2, powered by Anthropic's models <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

Finn 2 has demonstrated significant results:
*   Can resolve up to 86% of customer support volume (51% out-of-the-box) <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
*   Anthropic's own support team adopted Finn, observing similar resolution rates and enhanced human-like qualities like tone adjustment and answer length <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.
*   Improved policy awareness, such as handling refund policies, unlocking new capabilities <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>.

## Common Mistakes in [[testing_and_optimization_of_ai_coding_agents | Testing and Evaluation of AI Agents]]

Organizations frequently encounter several common pitfalls in [[evaluation_and_feedback_in_ai_systems | evaluation and feedback in AI systems]]:
*   **Retroactive Evaluations**: Building a robust workflow first and only then attempting to build evaluations <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. Evaluations should guide the development process from the outset <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.
*   **Data Problems**: Struggling to design evaluations due to poor data quality, which can be mitigated by using LLMs like Claude for data cleaning and reconciliation <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
*   **"Trusting The Vibes"**: Relying on a few queries that "look good" without testing on a statistically significant or representative sample <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. This can lead to unexpected outliers and poor performance in production <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.

It's crucial to consider the "latent space" of a use case, where different functions (e.g., prompt engineering, caching) move the model's position. The only way to find an optimized point is empirically, through [[improving_ai_evaluation_methods | evaluations]] <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. Evaluations are considered a form of "intellectual property" that allows companies to navigate this space and find optimal solutions faster than competitors <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.

## [[best_practices_for_ai_evaluation | Best Practices for AI Evaluation]]

### 1. Set Up Telemetry and Design Representative Test Cases
Invest in telemetry to back-test architecture in advance <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>. Design representative test cases that include expected user queries as well as "silly examples" or edge cases that might occur in reality (e.g., an off-topic question for a customer support agent) to ensure appropriate model responses <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.

### 2. Identify Key Metrics and Trade-offs
Acknowledge the "intelligence-cost-latency" triangle of trade-offs <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. Most organizations can optimize for one or two of these, but rarely all three <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>. The balance should be defined in advance, driven by the stakes and time sensitivity of the decision for the specific use case <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>. For example:
*   **Customer Support**: Latency is critical; a response within 10 seconds is vital to prevent user abandonment <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. UX design can help manage perceived latency <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
*   **Financial Research**: Accuracy is paramount; a 10-minute response time might be acceptable if the subsequent financial decision is high-stakes <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.

### 3. Consider Fine-Tuning Carefully
Fine-tuning is not a "silver bullet" and comes at a cost, potentially limiting the model's reasoning in areas outside of what it was fine-tuned for <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>. It's recommended to:
*   **Try other approaches first**: Many issues can be resolved with prompt engineering or architectural adjustments <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
*   **Establish clear success criteria**: Fine-tuning should only be pursued if other methods fail to meet specific intelligence domain requirements <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.
*   **Justify the cost and effort**: The significant variance in fine-tuning outcomes requires a clear justification for its implementation <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
*   **Avoid delaying deployment**: Don't let the pursuit of fine-tuning hinder initial deployment. Implement existing solutions, and if fine-tuning becomes necessary, integrate it later <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.

### 4. Explore Alternative Methods for Performance Improvement
Beyond basic prompt engineering, various features and architectures can drastically improve use case success without necessarily sacrificing intelligence for speed:
*   **Prompt Caching**: Can significantly reduce cost and increase speed <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>.
*   **Contextual Retrieval**: Improves the effectiveness of retrieval mechanisms by feeding information more efficiently to the model, reducing processing time <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   **Citations**: An out-of-the-box feature that can enhance reliability <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>.
*   **Agentic Architectures**: Architectural decisions that involve using AI agents to perform tasks <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>.

These [[improving_ai_evaluation_methods | methods for AI evaluation]] and [[custom_model_building_and_code_evaluation_for_ai_systems | custom model building and code evaluation for AI systems]] are crucial for [[building_custom_evaluations_for_better_ai_performance | building custom evaluations for better AI performance]] and achieving successful AI implementations.