---
title: AI Cost Optimization vs Exploration
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

The rapid advancement of AI, particularly with the release of ChatGPT, prompted companies like Intercom to re-evaluate their entire AI and machine learning (ML) roadmaps and go "all in" on new opportunities [01:46:27]. This shift brought to light the dynamic tension between exploring new AI capabilities and optimizing for cost efficiency.

## Initial Response and Product Development
When ChatGPT launched, Intercom's AI and ML team, based in Dublin, immediately recognized its potential impact on customer support [00:40:43]. Dez Trainer, co-founder and Chief Strategy Officer of Intercom, described the initial reaction as an "all hands on deck moment" [02:09:47]. This was because customer support is "in the kill zone of AI" due to large language models' (LLMs) conversational abilities, factual lookup, and summarization skills [02:16:30]. Intercom recognized that if they didn't lead in adopting this technology, someone else would, potentially leaving them behind [02:40:02].

Intercom quickly shipped its first AI-powered features, starting with "zero downside" additions to their inbox [03:39:48]. These initial features, powered by GPT-3.5 Turbo, included:
*   Summarizing conversations [03:57:46]
*   Translating messages for multilingual support [03:59:44]
*   Expanding or collapsing text [04:03:49]

These features, while seemingly basic, addressed real needs in customer support, such as summarizing issues for ticket creation [04:20:41]. This "tracer bullet" approach allowed them to test the waters without significant risk [03:40:48].

The next significant release was Finn, a user-facing chatbot, launched when Intercom gained access to the GPT-4 beta [05:17:02]. GPT-4 was crucial because it offered improved hallucination containment, which was a major concern with earlier models like GPT-3.5 [05:23:00]. To ensure customer excitement and trust, Intercom focused on making Finn reliable and on-topic, preventing it from offering political opinions or recommending competitors [05:47:05].

Inbox AI, a later development, enhanced the original inbox features with capabilities like matching the user's tone of voice [06:09:07].

## [[ai_production_and_evaluation_techniques | Guardrails and Hallucination Prevention]]
A significant challenge in deploying AI was building robust guardrails and preventing hallucinations [06:37:48]. Intercom's approach to this involved:
*   **Torture Tests**: A comprehensive set of scenarios, questions, and contexts to observe the AI's behavior [06:57:04]. This includes trying to trick the model to identify worst-case scenarios [07:42:47].
*   **Internal Weighting**: Determining acceptable levels of misbehavior versus the quality of answers (e.g., occasional political opinions if answers are highly accurate) [07:09:48].
*   **Context Prioritization**: Ensuring the LLM prioritizes specific company context over its general knowledge (e.g., sunbeds being illegal in Australia despite being legal elsewhere) [08:23:05].
*   **Prompt Engineering**: Extensive work in prompting the models to understand priorities and resolve conflicts between different data sources [08:33:04].

Intercom continuously evaluates various models like GPT-3.5 Turbo, GPT-4 (latest versions and builds), Anthropics Claude, and open-source models like Llama [08:52:00]. The evaluation criteria extend beyond just trust and accuracy to include:
*   Cost [09:14:04]
*   Reliability [09:17:05]
*   Stability [09:17:05]
*   Uptime [09:17:05]
*   Malleability (how much they can control the model) [09:20:49]
*   Speed (a critical factor) [09:25:35]

There's a consideration that in the future, customers might even be able to choose their preferred model based on these criteria [09:36:12].

## [[cost_efficiency_and_accessibility_in_ai | Cost Optimization vs. Exploration]]
Intercom initially faced significant cost challenges, especially with the idea of automatically summarizing 500 million conversations per month [04:56:07]. At the time, if they were to automatically summarize all conversations, it "would mean OpenAI's valuation would be a lot higher and Intercom would no longer exist" due to the cost [05:03:00]. This led them to implement a "button in the UI" for summarization rather than automatic default [05:56:56].

Despite this, Dez Trainer emphasizes that Intercom is still in "deep exploration mode" rather than primarily in [[posttraining_model_optimization_in_ai | cost optimization]] [11:02:22]. Their current focus is on maximizing the product's capabilities and exploring new [[experimentation_in_ai_and_data_science | opportunities]] for AI in areas like reporting, agent augmentation, and message composition [11:32:00].

The belief is that technology generally becomes cheaper and faster over time [14:43:00]. Therefore, their primary job is to build the best possible customer support platform enriched with AI [14:09:00]. [[evaluating_ai_progress_with_roi | Cost optimization]] is seen as a problem to be addressed once the product has achieved market fit and scale [14:22:42].

Latency, or speed, is currently a more significant "forcing function" than cost for considering smaller or more efficient models [13:38:00]. Dez Trainer noted that AI responses can feel slow, reminiscent of "modem internet days" [12:27:00]. The expectation is that this will improve, especially with advancements like Google's Gemini builds fitting on a phone or potential on-device LLMs from Apple [12:44:00].

The shift to intensive cost optimization is anticipated when the underlying AI models begin to plateau (e.g., when GPT-7 is only incrementally better than GPT-6) [15:12:00]. At that point, the focus will shift to optimizing existing capabilities rather than constant re-imagination [15:24:00].

## Organizational Structure and Pace of Development
Intercom operates with a centralized [[ai_coding_tools_and_market_dynamics | AI and ML team]] of about 17-20 people, comprising data scientists, AI/ML engineers, and experts in building, running, and training models [19:36:00]. This core team enables features, which are then built upon by around 150 "regular product engineers" within various product teams (e.g., inbox, messenger) [20:20:00].

Dez Trainer distinguishes between companies that:
1.  Are "AI as in they're literally working on the bleeding edge of AI" [21:08:00].
2.  "Use AI" by rebuilding or creating new product categories whose existence depends on foundational models like Anthropic or OpenAI [21:16:00].
3.  "Have a bit of AI" as "salt and pepper" to enhance existing features (e.g., summarizing a document) [21:35:00].

For the latter category, product engineers with some AI knowledge might suffice [21:53:00]. However, for the first two categories, a dedicated team of data scientists and engineers with deep domain expertise is necessary [22:03:00].

A key lesson for product managers and designers in AI/ML projects is the "second wave" of uncertainty [23:01:00]. Unlike traditional software where design de-risks a project, AI projects involve an additional layer of uncertainty regarding whether a feature is even *possible* to build, with no clear "no" answer [23:05:00]. This means AI/ML work should be viewed as a "portfolio of bets," with some high-probability outcomes (like text expansion) and others with much lower probabilities but higher potential impact (like generating vector graphics from Dolly-style technology) [23:39:00].

## Missing Tooling and Future of AI Products
Dez Trainer noted a gap in tooling, particularly around **prompt management** [16:16:00]. This includes subtle prompt changes, re-running tests, versioning prompts for different models, and AB testing for prompts [16:21:00]. While acknowledging many companies are entering this space, he questioned if it's a "billion dollar opportunity" or if major players like OpenAI (the "AWS of AI") might eventually build such tooling themselves, potentially "sherlocking" smaller companies [16:34:00].

Other missing elements include:
*   More robust infrastructure, especially for compliance (e.g., getting Finn to work in the EU was complex due to server locations) [16:55:00].
*   Cheaper and faster AI [17:16:00].
*   Improved developer experience around AI [18:06:00].

## Customer Adoption and Market Shifts
Customers often start with a "crawl, walk, run" approach to AI adoption [02:22:00]. Intercom facilitates this by allowing customers to "dip a toe" into AI [27:06:00]. For example, customers can choose to apply AI only to:
*   Free users [27:22:00]
*   Users who have used the product for over a year [27:35:00]
*   Weekend support [27:45:00]
*   Specific types of inquiries [27:47:00]

This gradual introduction helps customers gain confidence and see the value, often leading them to go "all in" when they realize AI-powered support (like Finn's instant answers) provides better service than human-only support [28:03:00].

The broader adoption of AI, particularly by major consumer platforms like Apple and Google integrating LLMs into Siri or Bard, is expected to normalize the idea of talking to software and accepting AI as a competitive differentiator [29:26:00]. This will likely reduce AI skepticism and make customers expect AI-enriched software [30:56:00].

## AI Capabilities and the Future of Customer Support
Currently, Intercom's Finn uses Retrieval Augmented Generation (RAG) rather than fine-tuning for each customer's specific voice or brand [31:32:00]. While fine-tuning for tone of voice is done via prompting, the AI organically picks up tone from existing documentation and past conversations [32:50:00].

The percentage of requests handled by AI in the future will vary significantly by industry [33:17:00]. For e-commerce, where queries are often repetitive (e.g., "where is my order?"), AI could handle nearly 100% of support [33:29:00]. For more complex products like Google Docs, where queries are diverse, AI might handle 80-90% [33:57:00]. The "automatability of support" is generally proportionate to the product's footprint and quality of service [34:49:00].

Beyond answering text queries, AI is expected to take actions (e.g., logging into Stripe to issue a refund or cancel an order) [35:06:00]. This is considered a "hard problem" primarily because it requires a lot of software to be written for authentication, monitoring, and data logging, not necessarily significant model advancements [37:19:00]. The future might involve AI proposing actions to human managers for approval, or even learning organically by observing support reps' actions in a browser [35:58:00].

## Shifting Product Landscape
Dez Trainer believes AI will fundamentally change or even eliminate entire product categories [38:58:00]. For instance, traditional advertising optimization platforms, which involve users logging in to manage ads, could be replaced by fully automated AI services that handle everything from ad generation to performance measurement and optimization without human intervention [39:15:00].

However, some product areas are less susceptible to overnight disruption by AI [40:17:00]. For example, an email marketing platform like MailChimp or Klaviyo, while potentially benefiting from AI-powered email design and writing, still requires a robust technical stack for sending hundreds of millions of emails, managing reputation, and ensuring compliance [40:33:00].

Dez Trainer offers advice for both startups and incumbents:
*   **For Startups**: Focus on areas where the incumbent tech stack is "irrelevant" because a truly AI-native solution would be built "entirely differently" from the ground up, rendering old UIs and features obsolete [41:34:00].
*   **For Incumbents**:
    1.  Start with "asymmetric upside" simple AI features to gain experience with costs and latency [42:15:00].
    2.  Break down the entire product into workflows and assess if AI can reliably and accurately remove them [42:38:00]. If so, delete the old manual processes [43:04:00].
    3.  If AI cannot remove a workflow, see if it can augment it or reduce it to a simple decision set, massively increasing efficiency [43:32:00].
    4.  Apply a "sprinkling" of AI where it offers minor enhancements, even if not transformative, to ensure a competitive offering [43:51:00].
    5.  Focus on learning how to sell the value of these AI changes to customers [44:12:00].

## Overhyped vs. Underhyped AI Trends
*   **Overhyped**: Productivity tools for writing emails, sales pitches, and similar content [44:30:00]. Dez Trainer believes people will learn to detect AI-generated content, and genuine human writing skills will be re-valued [44:42:00].
*   **Underhyped**: The transformative impact of AI on creativity [44:56:00]. Analogizing to Instagram's filters democratizing photography, he points to tools like Kaiber, Refusion, and Synthesia for artwork, music, and video as enabling new forms of creativity that are yet to be fully understood [45:22:00].

## Impressed by Incumbents
Beyond Microsoft and Google, Dez Trainer was impressed by Adobe's quick adoption of AI, and Figma and Miro for finding valuable and sensible AI use cases that genuinely enhance their products [46:11:00]. Atlassian and HubSpot were also noted for good AI implementations [46:41:00].

## Disappointed by Incumbents
Apple and Amazon were cited as disappointing due to their slow adoption of advanced AI capabilities [46:48:00]. The contrast between the primitive capabilities of Siri or Alexa (e.g., "play next song") and the advanced conversational abilities of ChatGPT (e.g., generating a multi-part story with emotive voice) highlights a significant gap [47:01:00]. Dez Trainer hopes for a "leveling out" in 2024, expecting this widespread adoption of AI to be a "big moment" [47:41:00].