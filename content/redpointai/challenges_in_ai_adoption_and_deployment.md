---
title: Challenges in AI Adoption and Deployment
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

Adopting and deploying AI solutions, particularly large language models (LLMs), presents several significant [[challenges_and_strategies_in_enterprise_ai_deployment | challenges]] for companies, including technical hurdles, cost considerations, and internal and external skepticism <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. Intercom, a customer support platform, rapidly integrated AI after the launch of ChatGPT, recognizing the potential for AI to revolutionize customer support <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Their experience offers valuable lessons on navigating these [[enterprise_ai_adoption_challenges_and_solutions | challenges]].

## Key Challenges in AI Adoption

### Cost Optimization
One of the immediate [[challenges_and_opportunities_in_ai_development | challenges]] encountered by Intercom was the prohibitive cost of running LLMs at scale <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Automatically summarizing 500 million conversations a month, for instance, would be fiscally unsustainable <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This forces companies to be strategic about where and when to apply AI, often leading to a "button in the UI" approach rather than full automation <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. While prices have come down significantly, cost remains a primary consideration for enterprises <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

Despite cost concerns, Intercom remains in "deep exploration mode," prioritizing building the best possible product over immediate cost optimization <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. The belief is that technology generally gets cheaper and faster, and current models are still rapidly improving <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. Cost optimization will become a greater focus once model improvements plateau <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Hallucinations and Guardrails
A significant concern, especially with earlier models like GPT 3.5, was the issue of "hallucinations"—where the AI generates factually incorrect or inappropriate information <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. To address this, Intercom focused on:
*   **Building trust and reliability**: Ensuring the AI stays on topic and avoids recommending competitors or expressing political opinions <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   **Torture testing**: Creating extensive scenarios, questions, and contexts to test the AI's behavior and identify potential misbehaviors <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This includes evaluating the AI's ability to prioritize specific contextual information over its general knowledge <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Model selection**: Continuously evaluating different models (e.g., GPT-3.5, GPT-4, Anthropic's Claude, Llama) based on trust, cost, reliability, stability, uptime, malleability, and speed <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Latency
Speed is a crucial factor in AI applications, especially in real-time interactions like customer support <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. Current AI interactions can sometimes feel slow, like "modem internet days" <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. The expectation is that this will improve, particularly if companies like Apple begin integrating LLMs directly into devices <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. Latency requirements might even become a driving force for exploring smaller, more efficient models before cost optimization becomes the primary focus <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

### Missing Tooling and Infrastructure
When transitioning to an AI-first company, organizations often find themselves building much of the necessary tooling themselves because it doesn't yet exist off-the-shelf <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Key areas identified include:
*   **Prompt management**: Tools for subtle changes to prompts, versioning prompts across different models, and A/B testing <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
*   **Robust infrastructure**: Dealing with geographical data residency (e.g., EU server requirements) and ensuring seamless integration with existing systems <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>. For Intercom, this meant forming relationships with providers like Microsoft Azure for European operations <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **Developer experience**: The broader ecosystem of tools supporting AI development, similar to how cloud computing gave rise to various multi-billion dollar categories in operations, engineering, and analytics <a class="yt-timestamp" data-t="00:18:06">[00:18:06]</a>.

### Organizational Structure and Risk Management
Deciding whether to have a centralized AI/ML team or embed AI expertise within product teams is a common question <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. Intercom adopted a centralized AI/ML team (around 17-20 people initially, growing from 9) that enables "regular product engineers" (around 150) to build on their foundational AI capabilities <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

A key [[challenges_in_ai_product_development | challenge in AI product development]] is the inherent uncertainty <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Unlike traditional software development where design can de-risk a project, AI projects have a "second wave" of uncertainty: whether the desired outcome is even possible <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. This requires a portfolio approach to AI bets, acknowledging that some projects (e.g., text summarization) have a high probability of success, while others (e.g., generating vector graphics for direct import and editing) have lower probabilities <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>.

### Customer Skepticism and Trust
Customers often start with a "pilot mode" or "dip-your-toe" approach to AI features, using them for low-risk scenarios like weekend support or non-paying users <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. Overcoming this skepticism requires:
*   **Gradual rollout strategies**: Offering options to apply AI to specific user segments (e.g., free users, users who have been with the product for over a year) or during off-peak times <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.
*   **Demonstrating value**: Showcasing high-quality answers and tangible benefits, like instant support, which can lead to customers wanting to apply AI more broadly <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.
*   **Normalizing AI interaction**: The widespread adoption of LLMs by major tech companies like Apple and Google in consumer products is expected to normalize the idea of "talking to software" and increase general acceptance of AI-enriched applications <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.

### Automating Actions
Beyond answering questions, a significant [[challenges_in_deploying_ai_models_effectively | challenge in deploying AI models effectively]] is enabling them to take "actions" (e.g., issuing a refund in Stripe or canceling an order) <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. This is a complex problem requiring extensive software development for authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. While technically feasible, it often involves a large amount of hand-coded logic or requires the AI to learn from documentation, presenting a deep engineering challenge <a class="yt-timestamp" data-t="00:37:27">[00:37:27]</a>.

## Shifting Product Landscape for Startups and Incumbents

AI is fundamentally changing the product landscape, creating both existential threats and massive opportunities:

### For Startups
Startups should target product areas where incumbent technology stacks are "irrelevant" <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. This means finding domains where, if starting fresh, the product would be built "entirely differently" with AI at its core, rendering existing UIs and features obsolete <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>. An example is advertising optimization, where AI could automate the entire process from ad generation to performance measurement, making the human-centric dashboards of today's products unnecessary <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.

Conversely, startups should be wary of entering spaces where incumbents have a deep-rooted, non-AI-centric competitive advantage, such as email delivery platforms (like Mailchimp or Klaviyo) <a class="yt-timestamp" data-t="00:40:33">[00:40:33]</a>. While AI can assist in email design and writing, the core [[challenges_of_building_ai_infrastructure_companies | infrastructure challenges]] of sending millions of emails (reputation, compliance, deliverability) remain, giving incumbents a significant lead that is hard to overcome <a class="yt-timestamp" data-t="00:40:43">[00:40:43]</a>.

### For Incumbents
Larger companies need a clear algorithm for AI integration:
1.  **Remove what AI can automate**: Identify workflows where AI can reliably perform tasks better than humans and delete the old processes <a class="yt-timestamp" data-t="00:43:04">[00:43:04]</a>. For example, automatically generating video hashtags or project titles <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>.
2.  **Optimize what remains**: For workflows that AI cannot fully remove, use AI to augment human efficiency or reduce complex tasks to simple decisions <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>. An example is an AI proposing a detailed solution (e.g., refund, credit, apology email) for a manager to approve with a simple "yes" or "no" <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.
3.  **Sprinkle AI where beneficial**: Add AI-powered features for convenience or minor improvements, even if not transformative, to ensure a comprehensive AI offering <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.
4.  **Educate customers**: Actively communicate the value of AI features to customers to drive adoption and shift their mindset from skepticism to full embrace <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

## Overhyped vs. Underhyped AI Trends

*   **Overhyped**: Productivity tools focused on generating content like emails or sales pitches <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>. The belief is that people will learn to detect AI-generated content, and genuine human writing will regain value <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.
*   **Underhyped**: The transformative impact of AI on creativity <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. Just as Instagram filters democratized photography, AI tools like Kai, Refusion (for sound), and Synthesia (for video) are enabling new forms of creativity that are yet to be fully understood <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

## Impressive and Disappointing Incumbents in AI Adoption

*   **Impressive**: Adobe, Figma, and Miro have been quick to integrate useful AI features that make sense for their products <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>. Shopify and HubSpot have also done well <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>.
*   **Disappointing**: Apple and Amazon (specifically with Siri and Alexa) have been surprisingly slow to integrate advanced LLM capabilities into their voice assistants, which still feel primitive compared to conversational AIs like ChatGPT <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>. This slow pace is a source of frustration, as widespread adoption by these giants is expected to significantly accelerate general AI acceptance <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>.