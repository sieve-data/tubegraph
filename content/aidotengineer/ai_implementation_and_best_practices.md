---
title: AI implementation and best practices
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

This article summarizes key insights on [[strategies_for_effective_ai_implementation | AI implementation and best practices]], drawing from hundreds of customer interactions by Anthropic's applied AI and go-to-market teams <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. Presenters Alexander Bricken and Joe Bailey from Anthropic share their expertise on leveraging AI to solve business problems and common pitfalls to avoid <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Anthropic Overview
Anthropic is an AI safety and research company focused on building safe, large language models (LLMs) <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. Founded by leading AI experts, the company has released multiple iterations of Frontier models, emphasizing safety techniques, research, and policy <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

Their marquee model, Sonnet 3.5, launched in late October of the previous year, is noted as a leading model in the code space, topping leaderboards for agentic coding evaluations like sbench <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.

### AI Interpretability Research
Anthropic's research directions include model capabilities, product research, and [[ai_model_considerations | AI model considerations]] safety <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. A differentiating focus is interpretability, which involves reverse engineering models to understand how and why they "think," and how to steer them for specific use cases <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

Interpretability research is still in its early stages <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>, progressing through stages that build upon each other:
*   **Understanding** Grasping AI decision-making <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Detection** Identifying specific behaviors and labeling them <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Steering** Influencing AI input <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>. An example is "Golden Gate Claude," where the model's activation for the Golden Gate Bridge was amplified, leading it to recommend painting a bedroom "red like the Golden Gate Bridge" <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **Explainability** Unlocking business value from interpretability methods <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

Interpretability is expected to significantly improve AI safety, reliability, and usability <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. The interpretability team understands feature activations at the model level and has published research on "towards monosemanticity" and "scaling monosemanticity" <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

## Customer Engagement and Use Cases
Anthropic encourages customers, especially [[ai_in_enterprise_and_startups | AI-native or AI startups]], to focus on using AI to solve core product problems, moving beyond basic chatbots and summarization <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>.

### Example Use Case: Onboarding and Upskilling Platform
Instead of just summarizing course content or offering a Q&A chatbot <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>, an onboarding platform could leverage AI to:
*   Hyper-personalize course content based on individual employee context <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
*   Dynamically adapt content to be more challenging if a user is breezing through <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   Dynamically update course material based on learning styles (e.g., visual content for visual learners) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.

Leading companies are achieving industry-leading results by combining their domain expertise with Anthropic's models across various sectors like taxes, legal, and project management <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. These applications drastically enhance customer experience, making products easier to use and more trustworthy, especially for business-critical workflows where hallucination is unacceptable (e.g., tax preparation) <a class="yt-timestamp" data-t="07:22:00">[07:22:25]</a>.

### Intercom's Finn AI Agent Case Study
Intercom, an AI customer service platform, partnered with Anthropic to enhance their AI agent, Finn <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.
*   **Initial Engagement**: Anthropic's applied AI lead worked with Intercom's data science team on a two-week sprint, comparing their hardest prompt for Finn against a prompt optimized with Claude <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.
*   **Optimization Sprint**: Positive initial results led to a two-month sprint focused on fine-tuning and optimizing all of Intercom's prompts for Claude to achieve the best performance <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>.
*   **Results**: Anthropic's LLM outperformed the previous one <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>. Intercom's resolution-based pricing model incentivizes helpful models <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>. The updated Finn 2 can solve up to 86% of customer support volume (51% out of the box) <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>. It also allowed for a more "human" element, with adjustable tone and answer length, and improved policy awareness (e.g., refund policies) <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.

## Anthropic Products and Support
Anthropic offers:
*   **API**: For businesses that want to embed AI in their products and services <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.
*   **Claude for Work**: Empowers organizations to use AI in their daily work <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
They also partner with AWS and GCP, allowing access to Frontier models on Bedrock or Vertex AI, enabling deployment in existing environments without managing new infrastructure <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

The applied AI team works at the intersection of product research, customer interaction, and internal research <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. They support technical aspects of use cases, design architectures, conduct evaluations, and tweak prompts to optimize model performance <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. They also feed insights back into Anthropic to improve products <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. The team often kicks off a sprint when customers face niche challenges related to LLM Ops, [[ai_application_frameworks_and_architecture | AI application frameworks and architecture]], or evaluations <a class="yt-timestamp" data-t="10:19:00">[10:19:00]</a>. They help define metrics, evaluate models, and deploy iterative loops into A/B test environments and eventually production <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.

## [[strategies_for_effective_ai_implementation | Best Practices for AI Implementation]]

### Testing and Evaluation
A common mistake is building a robust workflow and *then* creating evaluations <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
*   **Evaluations are Directional**: Evaluations should direct towards the perfect outcome and be built from the outset or very shortly after starting workflow development <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.
*   **Avoid "Trusting the Vibes"**: Running a few queries and assuming performance is insufficient <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. Evaluations must be based on a statistically significant, representative sample to predict real-world performance <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>.
*   **Navigating the Latent Space**: Think of use cases as a "latent space" where applying different functions (e.g., prompt engineering, prompt caching) moves the model's position <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. Evaluations are the only empirical way to know how changes affect performance and find the optimized point or "attractor state" <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>.
*   **Evals as Intellectual Property**: Robust evaluations are a key competitive advantage, allowing faster navigation of the latent space <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>.
*   **Setting up Telemetry**: Invest in telemetry to back-test architectures in advance <a class="yt-timestamp" data-t="15:35:00">[15:35:00]</a>.
*   **Designing Representative Test Cases**: Include "silly examples" or edge cases in eval sets to ensure the model handles unexpected inputs appropriately (e.g., a customer support agent encountering an irrelevant question like "how to kill a zombie in Minecraft") <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.

### Identifying Metrics
Organizations often face a trade-off between intelligence, cost, and latency <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>. It's difficult to optimize for all three simultaneously, so this balance should be defined in advance for a specific use case <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>.
*   **Stakes and Time Sensitivity**: The importance and time-sensitivity of the decision should drive optimization choices <a class="yt-timestamp" data-t="17:10:00">[17:10:00]</a>. For example:
    *   A customer support agent prioritizes speed (e.g., response within 10 seconds), as longer waits can lead to customer abandonment <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. UX design can help circumvent latency issues (e.g., thinking boxes, redirecting to other pages) <a class="yt-timestamp" data-t="17:21:00">[17:21:00]</a>.
    *   A financial research analyst agent might tolerate a 10-minute response time, as the subsequent capital allocation decision is highly important <a class="yt-timestamp" data-t="16:56:00">[16:56:00]</a>.
*   **Trade-offs**: More instruction sets might lead to longer latency but higher performance <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>. Knowing the important indicators for your product allows for appropriate optimization <a class="yt-timestamp" data-t="17:43:00">[17:43:00]</a>.

### Fine-tuning
Fine-tuning is **not a silver bullet** and comes with costs <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>.
*   **Limitations**: It's like "brain surgery" on the model, which can limit its reasoning in fields outside of the specific fine-tuning domain <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>.
*   **Try Other Approaches First**: Most users attempt fine-tuning without even having an evaluation set <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>. There should be clear success criteria in advance, and fine-tuning should only be pursued if performance cannot be achieved through other methods in a specific intelligence domain <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.
*   **Justify the Cost**: The effort and cost of fine-tuning (e.g., team involvement, working with providers) must be justified by a clear difference in desired capabilities <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>.
*   **Avoid Delays**: Don't let the need for fine-tuning slow down initial implementation <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>. Pursue the use case, realize if fine-tuning is needed, and then substitute the fine-tuned model later <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.

### Alternative Methods and Architectures
Beyond basic prompt engineering, many other features or architectures can drastically improve a use case's success <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>:
*   **Prompt Caching**: Can lead to significant cost reduction (e.g., 90%) and speed increase (e.g., 50%) without sacrificing model intelligence <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.
*   **Contextual Retrieval**: Drastically improves the performance of retrieval mechanisms, feeding information more effectively to the model and reducing processing time <a class="yt-timestamp" data-t="19:54:00">[19:54:00]</a>.
*   **Citations**: An out-of-the-box feature that can enhance reliability <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>.
*   **[[best_practices_for_building_ai_agents | Agentic architectures]]**: Architectural decisions that can significantly impact performance <a class="yt-timestamp" data-t="20:13:00">[20:13:00]</a>.