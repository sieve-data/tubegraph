---
title: Best practices for AI deployment and optimization
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

This article outlines key insights and [[best_practices_for_building_ai_systems | best practices for implementing AI]], derived from hundreds of customer interactions at Anthropic. The information covers common mistakes and strategies for successful AI deployment, particularly focusing on large language models (LLMs) <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## Anthropic's Approach to AI Development
Anthropic is an AI safety and research company focused on building safe, large language models (LLMs) <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. Their most recent model, Sonnet 3.5, is a leading model in the code space, performing well on evaluations like sbench for [[testing_and_optimization_of_ai_coding_agents | agentic coding evaluations]] <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

A key differentiator for Anthropic is its focus on interpretability research, which involves reverse engineering models to understand how they "think" and why, and then steering them in desired directions <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. This research is conducted in stages:
*   **Understanding** Grasping AI decision-making <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Detection** Identifying specific behaviors and labeling them <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Steering** Influencing AI input (e.g., Golden Gate Claude example) <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
*   **Explainability** Unlocking business value from interpretability methods <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

This research aims to improve AI safety, reliability, and usability <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

## Solving Business Problems with AI
When considering AI implementation, organizations should focus on how AI can solve core product problems, moving beyond simple chatbots and summarization <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

### Examples of Transformative AI Use Cases
Instead of basic Q&A, consider:
*   **Hyper-personalization** Dynamically adapting course content based on individual employee context <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
*   **Adaptive Learning** Adjusting content difficulty dynamically if a user is breezing through material <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   **Dynamic Content Generation** Updating course material based on learning styles (e.g., creating visual content for visual learners) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

Companies are using AI to enhance customer experience, making products easier to use and more trustworthy, especially in critical industries like taxes, legal, and project management where hallucinations are unacceptable <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.

## Anthropic's Customer Support Model
Anthropic's Applied AI team focuses on technical aspects of use cases, helping customers design architectures, perform evaluations, and tweak prompts to optimize model performance <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. They also feed customer insights back into product development <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

Their approach involves:
1.  **Sprints** Kicking off focused Sprints when customers face niche challenges (e.g., LLM Ops, architectures, evals) <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
2.  **Defining Metrics** Helping customers define specific metrics for evaluating the model against their use case <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
3.  **Deployment** Supporting the deployment of iterative improvements into AB test environments and eventually production <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.

### Case Study: Intercom's Finn AI Agent
Intercom, an AI customer service platform, partnered with Anthropic to enhance their AI agent, Finn <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>.
*   **Initial Sprint** A two-week Sprint by the Applied AI team and Intercom's data science team compared Finn's hardest prompt against a Claude-optimized prompt, showing promising results <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.
*   **Extended Optimization** This led to a two-month Sprint focused on fine-tuning and optimizing all of Intercom's prompts for Claude <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
*   **Results** Anthropic's model outperformed Intercom's previous LLM, leading to the launch of Finn 2 <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>. Finn 2 can solve up to 86% of customer support volume (51% out-of-the-box), offers more human elements like tone adjustment and answer length, and provides strong policy awareness (e.g., refund policies) <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

## Best Practices for AI Deployment and Optimization

### 1. Testing and Evaluation
[[best_practices_for_ai_evaluation | Evaluations]] are crucial and should guide the development process from the outset, not be an afterthought <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

#### Common Mistakes:
*   **Building workflows first, then evaluations** This leads to inefficient development, as evaluations are meant to direct towards the desired outcome <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Struggling with data problems for evaluations** LLMs like Claude can be used for data cleaning and reconciliation to design effective evaluations <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **"Trusting the vibes"** Relying on a few queries without representative or statistically significant samples can lead to unforeseen outliers in production <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

#### Best Practices:
*   **Empirical Knowledge** The only way to truly understand model performance after changes (e.g., prompt engineering) is through empirical evaluations <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>.
*   **Evaluations as IP** Treat evaluations as core intellectual property, enabling faster navigation of the "latent space" of possible model behaviors to find optimal solutions <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.
*   **Set up Telemetry** Invest in telemetry for back-testing architectures <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.
*   **Design Representative Test Cases** Include diverse examples, even "silly" ones, to ensure the model responds appropriately or reroutes questions, reflecting real-world user behavior <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.

### 2. Identifying Metrics for [[strategies_for_ai_model_deployment | AI Model Deployment]]
Organizations typically optimize for one or two elements of the "intelligence-cost-latency triangle" (intelligence, cost, latency), as achieving all three simultaneously is difficult <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

#### Considerations:
*   **Define Balance in Advance** Clearly define the trade-offs for your specific use case <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.
*   **Time Sensitivity**
    *   **Customer Support:** Latency is critical (e.g., customer expects response within 10 seconds) <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>.
    *   **Financial Research:** Accuracy and depth are more important than speed, so a 10-minute response time might be acceptable <a class="yt-timestamp" data-t="16:55:00">[16:55:00]</a>.
*   **Stakes of Decision** The importance and time-sensitivity of the decision driven by the AI output should influence your optimization choices <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>.
*   **User Experience (UX)** Consider UX improvements like a "thinking box" or redirection to other pages to manage latency expectations <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.

### 3. Fine-Tuning
Fine-tuning is not a [[costeffective_ai_strategies | silver bullet]] and comes with costs and limitations <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>.

#### Common Mistakes:
*   **Viewing fine-tuning as a quick fix** It's like "brain surgery" on the model, potentially limiting its reasoning in areas outside the fine-tuned domain <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>.
*   **Attempting fine-tuning without clear success criteria or evaluation sets** This makes it difficult to justify the effort and cost <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>.

#### Best Practices:
*   **Explore Other Approaches First** Prioritize other optimization methods before resorting to fine-tuning <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
*   **Clear Success Criteria** Have predefined success criteria, only considering fine-tuning if those cannot be met through other means <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.
*   **Don't Let it Slow You Down** Pursue the use case, and if fine-tuning becomes necessary, integrate it later rather than waiting for it from the start <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.
*   **Justify the Cost** Ensure the expected performance difference justifies the effort and cost of fine-tuning <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>.

### 4. Alternative Methods for Optimization
Beyond basic prompt engineering, various features and architectures can significantly improve use case success and help with [[scaling_ai_solutions_in_production | scaling AI solutions in production]] <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>.

#### Examples:
*   **Prompt Caching** Can drastically reduce [[cost_and_efficiency_in_deploying_ai_systems | cost]] (e.g., 90% reduction) and increase speed (e.g., 50% increase) without sacrificing intelligence <a class="yt-timestamp" data-t="19:47:00">[19:47:00]</a>.
*   **Contextual Retrieval** Improves the effectiveness of retrieval mechanisms, allowing information to be fed to the model more efficiently, reducing processing time <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   **Citations** An out-of-the-box feature that enhances reliability <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>.
*   **[[developing_and_optimizing_ai_agents | Agentic Architectures]]** Architectural decisions that can lead to significant improvements in AI agent development <a class="yt-timestamp" data-t="20:11:00">[20:11:00]</a>.