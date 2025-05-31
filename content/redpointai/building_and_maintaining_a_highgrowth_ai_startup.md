---
title: Building and maintaining a highgrowth AI startup
videoId: GlBY-zbwaXU
---

From: [[redpointai]] <br/> 

Lorra is an AI company at the forefront of applying artificial intelligence to the legal industry. Led by CEO and co-founder Max Unistron, Lorra works with many top law firms globally, has raised over $100 million, and is recognized as one of the fastest-growing AI applications in the market <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Lorra's Early Journey and AI Adoption in Law

When Lorra started in 2020, applying AI to law was challenging; early BERT models were decent in English but "horrendously bad" in Swedish <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. The arrival of GPT-3.5 marked a "paradigm starter," shifting the focus from experimentation to implementing end-to-end work deliverables <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. For example, due diligence can now be fully automated by uploading documents to Lorra to find information and generate reports <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The most significant leverage comes from surrounding frameworks like function calling and tool calling <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

The legal software space has historically been fragmented, with separate tools for translations, document comparisons, searching, and reviewing <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. AI is now baking these functionalities together, enabling the automation of low-complexity tasks like data extraction, and gradually moving towards complex tasks such as drafting share purchase agreements <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Why Law is Uniquely Suited for AI <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>

*   **Lack of Prior Software Development**: The legal space has seen limited software innovation, often relying on basic templating systems <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Distinct Needs**: In-house councils handle repetitive tasks (e.g., NDA reviews), while law firms deal with one-off or complex projects <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. AI platforms like Lorra can address the "wall-to-wall" needs across reviewing, reading, drafting, writing, and researching <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Client Pressure**: Law firms are increasingly pressured by clients to adopt AI tools, as clients are using them internally <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This mitigates the traditional "hourly billing problem" incentive, as firms must keep pace with client expectations and competitor actions <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Tasks like due diligence, once expensive, now face significant price pressure, making automation essential for profitability <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Strategic Growth and Market Entry

Lorra's journey highlights unique [[the_evolution_of_ai_startup_strategies | AI startup strategies]]:

*   **Nordic Start**: Starting in the Nordics allowed Lorra to become a dominant player in a smaller market before expanding globally <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Fast Second Mover**: By entering the market slightly later, Lorra could observe what worked and didn't, avoiding early pitfalls like focusing on training proprietary LLMs <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. With limited initial funding ($50,000 angel round), Lorra prioritized building a user-centric application layer <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Humble and Client-Focused**: Coming from a non-legal background fostered a humble approach, prioritizing client feedback and understanding the evolving relationship between law firms and their clients <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This focus allowed Lorra to develop an outward-facing tool for the entire client relationship, not just internal operations <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Ambitious Product Scope**: Unlike niche legal tech solutions, Lorra aimed to serve "every lawyer" by offering broad end-to-end capabilities, a more ambitious approach that might have been curtailed by competitive pressure in the US market <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Enterprise Readiness**: Starting with enterprise clients in the local market, such as Manheim Schwartling (the largest law firm in the Nordics), prepared Lorra for global expansion, ensuring they were "enterprise ready" upon entering new markets like the US <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Lorra invested half of its initial angel funding in certifications (SOC, ISO) to secure large enterprise clients from day one <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. This strategy facilitated referrals among well-connected law firms <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## [[Product_development_and_prioritization_in_ai_startups | Product Development and Prioritization in AI Startups]]

Teaching lawyers to use AI tools takes significant effort, but Lorra has achieved high adoption rates (70-80%) because lawyers are actively seeking these solutions <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Balancing Current Needs with Future Model Improvements <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>

Lorra's product strategy is to avoid building features that AI labs (OpenAI, Claude, Gemini) are likely to incorporate directly into their models, effectively building "boats" that rise with the tide of improving models <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. For example, if LLMs become capable of directly interpreting playbooks to redline documents, the need for a separate feature diminishes <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Similarly, multi-step workflows, traditionally built with node-based tools, might become unnecessary as LLMs develop the ability to create their own plans and execute them with tools <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. Lorra has even deprecated its own code when LLM providers offered built-in features, such as citations <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

### Challenges in AI Product Development <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>

The hardest part of building AI products is prioritizing from a hundred high-value features and integrating them into a cohesive platform, rather than creating a "Frankenstein monster" of disconnected functionalities <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. This involves careful planning of the platform's structure and data architecture, especially as client needs are also evolving <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

## Pricing, Costs, and [[AI_infrastructure_and_startup_opportunities | Infrastructure]]

Lorra currently uses a seat-based pricing model, which is easy to buy and predict, but can lead to unpredictable LLM costs for high-usage clients (e.g., $10,000 in LLM costs for one user) <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>. The long-term vision may include a platform fee plus a usage element <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. While early expectations were that LLM prices would continuously decrease, better models like 03 are more expensive despite their effectiveness for legal work <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Lorra uses "model pickers" to select the most cost-effective model for a given task, balancing performance and expense <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.

Regarding [[challenges_of_building_ai_infrastructure_companies | AI infrastructure]], Max Unistron finds Multi-tool Co-operation (MCP) both underhyped and overhyped <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>. It's underhyped for its potential to enable universal applications but overhyped because it still requires significant development in areas like authentication for full production <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. Lorra is excited about the prospect of clients providing their own tools (CRM, knowledge bases, templates) for Lorra to access, greatly expanding its capabilities <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.

## Company Building in the AI Era

Lorra's experience in Y Combinator during the post-ChatGPT "AI craze" underscored the need to move fast <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>. Founders prioritized either building vector databases/PostgreSQL layers or application layers <a class="yt-timestamp" data-t="00:26:45">[00:26:45]</a>. Lorra was "very commercially focused" from the start, launching a private, compliant ChatGPT with RAG on client documents and Swedish legislation as soon as it was viable <a class="yt-timestamp" data-t="00:27:46">[00:27:46]</a>.

However, a crucial lesson for Lorra was the importance of product maturity before expanding into new markets <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. After raising $35 million, the team took 4-5 months off selling to focus on product development and reliability <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This decision, though unusual for a first board meeting, was deemed mature because lawyers are less forgiving of poor performance: if an attorney's query doesn't work, they often don't return, making reactivation difficult <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. Reliability, infrastructure (chunking, RAG system), and scaling to thousands of users daily were critical initial problems to solve <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>. As Lorra onboarded larger, global firms, expectations became "incredibly high," with the product becoming a system of record where immediate support is required for client deliverables <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

### High-Velocity Culture and Team Building <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>

Lorra fosters a high-velocity culture, driven by the founding team's intense work ethic (e.g., co-founder Sig coding 14 hours a day, 7 days a week) <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>. They explicitly recruit for this pace, stating upfront that it's "not a 9 to 5 job" and focusing on building for the future <a class="yt-timestamp" data-t="00:32:44">[00:32:44]</a>. The company emphasizes in-office work and full onboarding in Stockholm for all employees, fostering a culture where "momentum breeds momentum" and people love winning <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>. Lorra grew from 10 to 100 people in a year, a rapid expansion in line with the new expectations for how quickly an AI software company can grow <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>. Unlike traditional SaaS, AI companies often create entirely new categories, leading to accelerated growth for those with the highest velocity, best product, and service <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.

### Advice for Future Lawyers <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>

The future of law requires lawyers to be "entrepreneurial, creative people" who challenge existing methods <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>. They will need to be fluent in working with AI, essentially managing AI agents from day one, a different skill set than being a diligent associate <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>. Individual lawyers are expected to augment their own work with AI tools <a class="yt-timestamp" data-t="00:43:21">[00:43:21]</a>.

Lorra is committed to collaborating with law firms and legal professionals to build the future of AI in law <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.
More information can be found at Leguora.com <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>.