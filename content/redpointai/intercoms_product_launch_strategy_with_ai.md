---
title: Intercoms product launch strategy with AI
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

Intercom, a company specializing in customer support, rapidly adopted AI following the launch of ChatGPT. Dez Trainer, co-founder and Chief Strategy Officer of Intercom, described their journey from an immediate "all hands on deck" response to becoming a leader in [[integration of voice AI in various industries | AI adoption]] within the customer support industry <a class="yt-timestamp" data-t="02:56:45">[02:56:45]</a>.

## Immediate Reaction to ChatGPT's Launch

When ChatGPT launched around 5:00 PM in Dublin, Ireland, Intercom's AI and ML team quickly recognized its potential <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Dez Trainer was alerted by his VP of AI, Fergo, who messaged him about the new technology <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. Initial reactions involved playing with the tool and being impressed by its ability to answer obscure questions and generate creative content, like songs in the style of Rage Against the Machine <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

The company recognized that customer support was "in the kill zone" of AI and Large Language Models (LLMs) due to their conversational abilities, fact-finding, and summarization capabilities <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. This led to a critical discussion about whether to "rip up the entire AI/ML roadmap" to go "all in" on this new technology <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>. Intercom decided to move quickly, shipping their first AI-powered product before Christmas, a reasonable release in January, and then launching "Finn" in March, followed by a broader release in July <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. This rapid pace was driven by the understanding that if they didn't lead, someone else would, potentially leaving little room for others in the support industry <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

## Phased AI Product Development

Intercom adopted a "crawl, walk, run" approach to product rollout, starting with low-risk features and gradually expanding <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

### Initial AI Features ("Crawl")

The first "tracer bullet" involved integrating "zero downside" [[AI integration and product development strategies | AI features]] into their existing inbox product <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. These included:
*   Summarizing conversations <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>
*   Translating messages for multilingual support <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>
*   Expanding or collapsing text <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>

This approach ensured that if users didn't like the AI-generated output (e.g., a summary), they could simply choose not to use the feature <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. However, the immediate user demand for automatic summarization highlighted significant cost implications. Automatically summarizing 500 million conversations a month would be prohibitively expensive, leading them to keep it as an optional button in the UI <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

### Launching Finn ("Walk")

The next major release was "Finn," a user-facing chatbot, enabled by access to the beta of GPT-4 <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. GPT-4 significantly helped in containing "hallucinations," a major concern with GPT 3.5 <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.

Finn was designed to answer questions based on a high confidence threshold, with significant work put into ensuring it was trustworthy, reliable, and stayed on topic, avoiding inappropriate responses like political opinions or competitor recommendations <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Expanding Capabilities ("Run")

Following Finn, "Inbox AI" was launched, building on the initial set of features with additions like adjusting the tone of voice to match Intercom's standard tone <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

Key aspects of developing these broader AI features included:

*   **Guardrails and Hallucination Prevention:** This involved creating "torture tests" with extensive scenarios, questions, and contexts to observe the AI's behavior and set internal weighting for acceptable misbehaviors <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. The team learned to prioritize context provided over the LLM's general knowledge <a class="yt-timestamp" data-t="08:22:00">[08:22:27]</a>.
*   **Model Selection:** Intercom continuously evaluates various LLMs (GPT 3.5, GPT-4, Anthropic's Claude, Llama) based on trust, cost, reliability, stability, uptime, malleability, and speed <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. They foresee a future where customers might even choose their preferred model <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

## Cost Optimization vs. Exploration

Intercom remains in a "deep exploration mode" rather than focusing heavily on cost optimization <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. Their primary goal is to build the "best possible product" by augmenting human agents, powering reporting, and enhancing message sending with AI <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>. They believe that technology will generally become cheaper and faster, and model improvements will inherently make their product better over time <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. The shift to cost optimization will likely occur when LLMs plateau, similar to the "S-curve" concept where rapid acceleration gives way to incremental improvements <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>.

Latency is a current forcing function that might drive the exploration of smaller, faster models <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.

## Challenges and Missing Tools

Intercom has had to build many tools themselves due to a lack of off-the-shelf solutions <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. Key missing areas include:
*   **Prompt Management:** Tools for subtle prompt changes, re-running tests, versioning prompts across different models, and A/B testing <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>.
*   **Robustness:** Challenges with deploying AI in different regions (e.g., EU servers), leading to partnerships like the one with Microsoft Azure <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.
*   **Developer Experience:** Opportunities for new tools and services to emerge, similar to how cloud computing spawned new categories in Ops and analytics <a class="yt-timestamp" data-t="18:06:00">[18:06:00]</a>.

A concern is OpenAI's multifaceted role as a lab, an "AWS of AI," and a consumer company (ChatGPT), which could lead to third-party tools being "sherlocked" <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>.

## Team Structure and Shipping Pace

Intercom maintains a centralized [[AI integration and product development strategies | AI/ML team]] of 17-20 people, comprising data scientists, AI, and ML engineers with deep domain expertise in [[building a successful AI product for developers | building and training models]] <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>. This core team enables over 150 "regular product engineers" who then build user-facing features on top of the AI team's endpoints <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>.

Dez Trainer distinguishes between:
1.  **AI-native startups:** Working on the bleeding edge of AI <a class="yt-timestamp" data-t="21:08:00">[21:08:00]</a>.
2.  **Companies that use AI:** Rebuilding or creating new product categories whose existence depends on LLMs <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>. Intercom falls into this category <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.
3.  **Companies that have a bit of AI:** Applying AI as "salt and pepper" to enhance existing products <a class="yt-timestamp" data-t="21:35:00">[21:35:00]</a>.

For companies in the first two categories, a dedicated AI/ML team with deep expertise is crucial <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>. [[Challenges and opportunities in AI integration | AI/ML projects]] introduce a "second wave" of uncertainty: after design, there's the question of whether the functionality is even *possible*, a question that might not have a clear "no" answer, leading to prolonged effort without guaranteed results <a class="yt-timestamp" data-t="23:01:00">[23:01:00]</a>. Therefore, AI/ML work needs to be viewed as a "portfolio of bets," with some high-probability and some low-probability endeavors <a class="yt-timestamp" data-t="23:39:00">[23:39:00]</a>.

An example of a challenging problem is agent-side sentence completion, which, despite appearing simple, struggles with distinguishing personal information and abstracting irrelevant context <a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>.

## Customer Adoption and Future of AI in Support

Intercom's strategy for customer adoption involves making it easy to "dip your toe in" rather than a "trust fall" <a class="yt-timestamp" data-t="27:06:00">[27:06:00]</a>. They allow customers to test AI with specific user segments (e.g., free users, weekend support, specific query types) <a class="yt-timestamp" data-t="27:22:00">[27:22:00]</a>. The value of instant and correct answers often leads customers to eventually go "all in" because their test groups receive better support than paid users <a class="yt-timestamp" data-t="28:09:00">[28:09:00]</a>.

The broader adoption of AI will be significantly influenced by major consumer tech companies like Apple and Google integrating LLMs into their products (e.g., Siri, Bard). This will normalize the idea of conversational software and make AI a competitive battleground in the B2B space <a class="yt-timestamp" data-t="29:26:00">[29:26:00]</a>.

Currently, Finn uses Retrieval Augmented Generation (RAG) and adjusts tone of voice via prompting rather than fine-tuning <a class="yt-timestamp" data-t="31:32:00">[31:32:00]</a>. Intercom's internal AI lab continually explores custom models and fine-tuning <a class="yt-timestamp" data-t="32:11:00">[32:11:00]</a>.

In the future, some support requests will be 100% handled by AI, especially in verticals like e-commerce with limited query types <a class="yt-timestamp" data-t="33:17:00">[33:17:00]</a>. More complex products will see higher volumes and diversity of queries, making 100% automation harder but still achieving high percentages (e.g., 80-90%) <a class="yt-timestamp" data-t="34:02:00">[34:02:00]</a>.

Beyond text-based answers, [[proactive AI interventions | AI will take actions]], such as issuing refunds or canceling orders, which requires building significant software for authentication, monitoring, and data logging <a class="yt-timestamp" data-t="35:06:00">[35:06:00]</a>. This could range from full automation to AI proposing actions for human approval <a class="yt-timestamp" data-t="35:58:00">[35:58:00]</a>.

## Shifting Product Landscape

AI will completely disrupt certain product categories by making entire workflows automatic, eliminating the need for complex user interfaces <a class="yt-timestamp" data-t="38:58:00">[38:58:00]</a>. For example, ad optimization software could become a background service with minimal user interaction <a class="yt-timestamp" data-t="39:34:00">[39:34:00]</a>.

### Advice for Startups
[[Strategy and competitive landscape in AIpowered communication tools | Startups]] should target areas where the incumbent technology stack is irrelevant and would be built "entirely differently" if redesigned with AI <a class="yt-timestamp" data-t="41:34:00">[41:34:00]</a>. This offers an advantage over incumbents who might only be able to add "cutesy little AI" features to existing complex systems <a class="yt-timestamp" data-t="41:21:00">[41:21:00]</a>.

### Advice for Incumbents and [[Enterprise partnerships and AI application deployment | Enterprise AI Application Deployment]]
Incumbents should:
1.  **Find Asymmetric Upside:** Start with simple AI features to understand costs and latency <a class="yt-timestamp" data-t="42:17:00">[42:17:00]</a>.
2.  **Workflow Analysis:** Break down their product into workflows and assess if AI can reliably perform them <a class="yt-timestamp" data-t="42:38:00">[42:38:00]</a>.
3.  **Remove or Optimize:** If AI can remove a workflow, it should be removed. If it can augment or simplify a workflow, it should be optimized <a class="yt-timestamp" data-t="43:04:00">[43:04:00]</a>.
4.  **Sprinkle AI:** Add AI enhancements even if not core to the workflow for completeness <a class="yt-timestamp" data-t="43:51:00">[43:51:00]</a>.
5.  **Sell the Value:** Focus on educating customers about the value of these AI transformations <a class="yt-timestamp" data-t="44:12:00">[44:12:00]</a>.

## AI Trends: Overhyped and Underhyped

*   **Overhyped:** Productivity tools that generate content (emails, sales pitches). Dez believes people will learn to detect AI-generated content, and filters will emerge, leading to a diminished value for such tools <a class="yt-timestamp" data-t="44:30:00">[44:30:00]</a>.
*   **Underhyped:** The impact of AI on creativity. Tools like Kaiber, Refusion, and Synthesia, similar to how Instagram filters enabled everyone to feel like a photographer, are unlocking new forms of creativity in art, music, and video <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>.

## Impressions of Incumbent AI Adoption

*   **Most Impressed:** Microsoft (beyond the obvious), Adobe (quick out of the blocks), Figma, and Miro for finding genuinely useful use cases instead of just putting AI on their homepage <a class="yt-timestamp" data-t="46:08:00">[46:08:00]</a>. Shopify also received a mention for nice work <a class="yt-timestamp" data-t="46:41:00">[46:41:00]</a>.
*   **Most Disappointed:** Apple and Amazon (Siri and Alexa). Despite their resources, their voice assistants seem primitive compared to advanced LLMs, highlighting a significant gap in [[the future of AI in human communication | conversational AI capabilities]] <a class="yt-timestamp" data-t="46:48:00">[46:48:00]</a>. This perceived disparity between highly advanced generative AI (ChatGPT) and basic voice assistants creates a jarring experience for users <a class="yt-timestamp" data-t="47:37:00">[47:37:00]</a>.

Intercom emphasizes the importance of going "all in" on AI, starting with "zero downside" features, and continuously exploring new capabilities rather than solely focusing on cost optimization. They believe the broad adoption of AI by major tech companies will normalize its use and shift the competitive landscape significantly.