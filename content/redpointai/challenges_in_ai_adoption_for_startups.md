---
title: Challenges in AI adoption for startups
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

The adoption of AI, particularly large language models (LLMs), presents both immense opportunities and significant challenges for startups and established companies alike. Intercom, a customer support platform, offers insights into navigating these [[Enterprise AI adoption challenges | challenges]] based on their rapid integration of AI into their product, Finn, following the release of ChatGPT <a class="yt-timestamp" data-t="00:00:10"></a>.

## Initial Response and Strategic Pivoting

Upon the release of ChatGPT, Intercom recognized that customer support was "so in the kill zone of AI and these large language models" due to their conversational abilities, fact-finding, and summarization capabilities <a class="yt-timestamp" data-t="00:02:17"></a>. This immediate threat and opportunity led them to consider ripping up their entire AI/ML roadmap to go all-in on generative AI <a class="yt-timestamp" data-t="00:01:46"></a>. This aggressive pivot demonstrates a key challenge: the need for rapid strategic reassessment and commitment in a fast-evolving AI landscape.

## AI Product Development Philosophy

Intercom's approach to [[building_ai_startups_and_the_challenges_of_scaling | building AI startups and the challenges of scaling]] involved a "crawl, walk, run" strategy, starting with "zero downside" AI features <a class="yt-timestamp" data-t="00:02:22"></a>. This aligns with [[lean_startup_principles_in_ai | Lean Startup principles in AI]] by minimizing risk while exploring value <a class="yt-timestamp" data-t="00:03:32"></a>. Initial features included conversation summarization, message translation, and text expansion within their inbox <a class="yt-timestamp" data-t="00:03:57"></a>.

The logic behind this approach is that if users don't like a summary, they simply don't click the button, but if it's useful, demand for more automation quickly follows <a class="yt-timestamp" data-t="00:04:40"></a>.

## Technical Challenges in AI Adoption

### Cost Optimization
A significant [[challenges_in_ai_model_training_and_deployment | challenge in AI model training and deployment]] and [[challenges_and_strategies_in_ai_deployment | strategy in AI deployment]] identified was the cost associated with AI model usage. With 500 million conversations a month, automatically summarizing all of them would be prohibitively expensive <a class="yt-timestamp" data-t="00:04:56"></a>. This led to a "cost optimization" phase, where they had to be clever about what features to automate and when <a class="yt-timestamp" data-t="00:05:09"></a>.

Despite these cost considerations, Intercom remains in "deep exploration mode," prioritizing finding new AI opportunities over immediate cost optimization <a class="yt-timestamp" data-t="00:11:02"></a>. The belief is that technology generally gets "cheaper and faster," so prioritizing the best product first is key <a class="yt-timestamp" data-t="00:14:43"></a>.

### Guardrails and Hallucination Prevention
A major [[challenges_in_enterprise_ai_deployment | challenge in Enterprise AI deployment]] and a concern for businesses is controlling AI behavior, preventing hallucinations, and ensuring trustworthiness <a class="yt-timestamp" data-t="00:05:23"></a>. Key strategies include:
*   **Torture Tests:** Creating extensive scenarios to test for misbehaviors and desired behaviors <a class="yt-timestamp" data-t="00:06:57"></a>.
*   **Prioritization:** Training models to prioritize specific contexts over their general knowledge to prevent undesirable outputs (e.g., political opinions, competitor recommendations) <a class="yt-timestamp" data-t="00:08:22"></a>.
*   **Model Selection:** Continuously evaluating various LLMs (GPT-3.5, GPT-4, Anthropic's Claude, Llama) based on trust, cost, reliability, stability, uptime, malleability, and speed <a class="yt-timestamp" data-t="00:08:48"></a>. Speed is particularly highlighted as a critical factor <a class="yt-timestamp" data-t="00:09:25"></a>.

### Missing Tooling and Infrastructure
The rapid evolution of AI means essential tooling is often missing, forcing companies to build solutions themselves <a class="yt-timestamp" data-t="00:15:54"></a>. Examples include:
*   **Prompt Management:** Tools for subtle prompt changes, versioning, and A/B testing across different models <a class="yt-timestamp" data-t="00:16:18"></a>.
*   **Robust Infrastructure:** Challenges with server locations (e.g., EU data residency leading to a relationship with Microsoft Azure) <a class="yt-timestamp" data-t="00:17:00"></a>.
*   **Developer Experience:** Opportunities for new tools in the AI developer experience, similar to how cloud computing spawned new multi-billion dollar categories <a class="yt-timestamp" data-t="00:18:06"></a>. However, there's a risk of being "sherlocked" by foundational model providers like OpenAI if they build their own developer tools <a class="yt-timestamp" data-t="00:18:51"></a>.

## Organizational Structure for AI Development

Intercom operates with a centralized AI/ML team of about 17-20 people (initially 9), comprising data scientists and AI/ML engineers with deep domain expertise <a class="yt-timestamp" data-t="00:19:36"></a>. This central team enables "regular product engineers" (around 150 people) to build user-facing features on top of the AI team's provided endpoints <a class="yt-timestamp" data-t="00:20:20"></a>.

The choice of centralized vs. distributed AI teams depends on the company's AI maturity:
*   **AI-as-a-feature:** Companies applying AI as "salt and pepper" can use product engineers with some AI familiarity <a class="yt-timestamp" data-t="00:21:45"></a>.
*   **AI-first/AI-dependent:** Companies whose existence depends entirely on AI or are pushing the bleeding edge require dedicated data scientists and experienced AI engineers <a class="yt-timestamp" data-t="00:22:03"></a>.

A critical challenge is the inherent uncertainty in AI/ML projects compared to traditional software development. While design risks can be explored upfront in traditional software, AI projects introduce a "second wave" of uncertainty: "is any of this even possible?" <a class="yt-timestamp" data-t="00:23:01"></a>. This means projects must be viewed as a "portfolio of bets," with varying probabilities of success <a class="yt-timestamp" data-t="00:23:39"></a>.

## Strategic Considerations for AI Startups

For startups, a key [[challenges_and_opportunities_in_ai_integration | challenge and opportunity in AI integration]] is to identify areas where incumbent technology stacks are "irrelevant" <a class="yt-timestamp" data-t="00:41:39"></a>. This means finding domains where an AI-first approach would lead to an "entirely different" product, UI, and underlying architecture <a class="yt-timestamp" data-t="00:41:48"></a>. Startups should avoid areas where incumbents can easily copy AI features due to existing complex infrastructure (e.g., email sending platforms) <a class="yt-timestamp" data-t="00:40:41"></a>.

For incumbents, the recommended algorithm for AI adoption is:
1.  **Remove:** Identify and automate entire workflows that AI can reliably do, then delete the old manual processes <a class="yt-timestamp" data-t="00:43:04"></a>.
2.  **Optimize:** If AI cannot fully remove a workflow, use it to augment or reduce it to a simple decision set, massively increasing efficiency <a class="yt-timestamp" data-t="00:43:32"></a>.
3.  **Sprinkle:** Add "salt and pepper" AI features for a complete offering <a class="yt-timestamp" data-t="00:43:53"></a>.
4.  **Sell:** Focus on explaining and demonstrating the value to customers <a class="yt-timestamp" data-t="00:44:12"></a>.

## Future Outlook and Broader Adoption

A major [[challenges_and_advancements_in_ai_technology | challenge and advancement in AI technology]] for broader adoption is latency <a class="yt-timestamp" data-t="00:13:38"></a>. The current speed of AI interactions can feel like "modem internet days" <a class="yt-timestamp" data-t="00:12:27"></a>. Faster, on-device AI models (like Google's Gemini builds for phones or future Apple LLMs) are anticipated to normalize conversational interactions with software <a class="yt-timestamp" data-t="00:12:47"></a>. This normalization, much like the iPhone's impact on software design, is expected to make AI adoption a competitive battleground and reduce user skepticism <a class="yt-timestamp" data-t="00:29:32"></a>.

Intercom expects AI to handle a significant percentage of customer support requests, potentially 100% in certain verticals like e-commerce where queries are limited <a class="yt-timestamp" data-t="00:33:19"></a>. For more complex products (e.g., Google Docs), 80-90% automation might be achievable <a class="yt-timestamp" data-t="00:34:02"></a>. The future will also see AI taking actions (e.g., issuing refunds in Stripe), moving beyond just providing text answers <a class="yt-timestamp" data-t="00:35:07"></a>. This presents a new [[challenges_and_opportunities_in_ai_infrastructure_development | challenge and opportunity in AI infrastructure development]] in building robust systems for authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:37:57"></a>.

The ability to control human involvement in AI-driven decisions will also be crucial, allowing for full automation or human oversight for critical actions <a class="yt-timestamp" data-t="00:36:51"></a>.