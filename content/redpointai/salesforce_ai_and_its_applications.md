---
title: Salesforce AI and its applications
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

Salesforce AI is led by CEO Clara Shih and is featured on the Unsupervised Learning AI podcast [00:00:06]. As an incumbent technology company, Salesforce is recognized for holding significant data and for its rapid advancements in artificial intelligence adoption [00:00:10]. Discussions with Clara Shih covered how AI is integrated into Salesforce products, its utilization by companies like Gucci, and the challenges in [[enterprise_adoption_of_ai_agents | enterprise adoption of AI]].

## The Future of Work with AI

Clara Shih believes that within ten years, current work methods will appear as outdated as practices from the early 1990s, such as physical filing cabinets or dictation [00:01:22]. The pervasive impact of AI is expected to transform nearly every aspect of the modern workforce [00:01:39].

## Key AI Products and Capabilities

Salesforce launched its first set of [[generative_ai_for_business_applications | generative AI applications]] under the Einstein GPT brand in the summer of 2023 [00:01:54]. These include:
*   **Service GPT** for customer service [00:01:57].
*   **Sales GPT** for Sales Cloud users [00:02:03].

Notable early successes include service reply recommendations and case summaries, which significantly reduce time-consuming tasks for customer service personnel and waiting times for customers [00:02:10]. These applications are designed to work "out of the box" by grounding responses in customer data within Salesforce [00:02:30].

Recently, Salesforce announced the general availability (GA) of:
*   **Einstein Co-pilot** - A natural language conversational assistant automatically grounded in a customer's Salesforce data, metadata, and flows [00:05:21].
*   **Co-pilot Studio** - A platform allowing customers to customize their own co-pilots through a prompt builder for creating "golden prompts" referencing specific Salesforce data fields, and a model builder for fine-tuning or integrating their own predictive models [00:05:37].

AI's role is shifting work from "deterministic" to "stochastic," implying a different way of thinking and building [00:10:16].

### Customer Service Transformation at Gucci

Gucci, one of Salesforce's initial customers for Service GPT, implemented the AI in their service teams located in Florence, Italy, and New Jersey [00:03:04]. The AI helped reduce average handle time for customer issues [00:03:15]. Beyond efficiency, the AI enabled service representatives to [[ai_product_market_fit_and_emerging_applications | uplevel their roles]] and transition into salespeople and brand storytellers [00:03:21]. For instance, after resolving a belt issue, the AI might coach a service representative to recommend a handbag the customer previously browsed, leading to double-digit conversion rate increases [00:04:01]. This transformed the customer service department from a cost center into a revenue center [00:04:22]. This use case highlights how AI can empower employees to do "the best work of their careers," rather than replacing jobs [00:04:46].

## Organizational Structure for AI Development

Salesforce's approach to AI development has evolved:
*   Initially, AI teams were largely decentralized within each application cloud (e.g., Service Cloud [00:06:22]).
*   Recognizing the need for shared infrastructure across all applications (like the Einstein Trust Layer and model Gateway), Salesforce created a new shared services AI platform team [00:06:34]. This central team builds core components like the Trust Layer, Gateway, Prompt Builder, and Einstein Co-pilot [00:06:54].
*   Specific product teams (e.g., Sales Cloud, Service Cloud, Slack) continue to own predictive AI for their use cases and build actions on top of the shared Einstein Co-pilot platform [00:07:09].

## Trust and Governance in AI Deployment

Salesforce prioritizes trust, especially when dealing with high-stakes use cases involving real customer interactions [00:07:28]. Their approach to trust is threefold:
1.  **Technology:** The **Einstein Trust Layer** is engineered into the product, offering:
    *   Data masking [00:07:56].
    *   Data grounding with Salesforce Data Cloud to reduce hallucinations [00:08:01].
    *   Citations and audit trails [00:08:03].
    *   Prompt defense [00:08:05].
    *   Zero retention prompts to mitigate data security, privacy, and ethical risks [00:08:06]. Data masking, for example, has been a feature since predictive AI days to prevent bias from sensitive data fields like name, gender, or zip code [00:09:23].
2.  **Acceptable Use Policy:** For AI bots deployed to customers, Salesforce policy requires the AI to self-identify as an AI [00:08:16].
3.  **Stakeholder Engagement:** Salesforce has developed open-source trusted AI guiding principles focusing on accuracy, honesty, and empowerment, shared with the industry and government regulators [00:08:39].

The development of these trust features involves a combination of internal building and partnerships with startups [00:09:11].

## Data Strategy and Unique Data Types

Salesforce emphasizes that the data within its systems belongs to its customers, not Salesforce [00:16:19]. Salesforce has four unique types of data crucial for AI:
1.  **Structured CRM Data:** Traditional customer relationship management records, a core part of Salesforce's heritage [00:16:39].
2.  **Unstructured Data:** This includes knowledge articles, exponentially growing conversation transcripts from Slack channels, contact center voice calls, chats, and emails [00:16:47]. Salesforce's Data Cloud is expanding to include vector search and hybrid reranking across both structured and unstructured data [00:17:09].
3.  **Metadata Layer:** Created 25 years ago to support multi-tenancy, this layer is now vital for providing context to AI, helping it identify relevant data objects, tables, and functions [00:17:35].
4.  **Feedback Data:** Salesforce acts as the world's largest database of customer outcomes, capturing data like sales opportunity stages, marketing campaign results (opens, clicks, conversions) [00:18:01]. This feedback data serves as a "reward function" for any AI model, whether predictive or [[generative_ai_for_business_applications | generative]], and is captured via the Data Cloud pipeline [00:18:21]. This allows models to continually learn and improve the advice or assistance they provide [00:18:36].

Salesforce also has [[enterprise_partnerships_and_ai_application_deployment | zero ETL partnerships]] with major data lake providers (e.g., BigQuery, Redshift, Snowflake, Databricks) to integrate data from across the customer's enterprise environment [00:17:18].

## AI Model Strategy

Recognizing the rapid evolution of the AI model space, Salesforce adopts an open architecture approach [00:19:12]. Customers can choose from models on Salesforce's service, bring their own models, or integrate third-party models [00:19:16]. The Model Builder facilitates this, enabling customers to plug their models directly into their Salesforce AI stack [00:19:24].

Salesforce believes different models will be optimal for different tasks [00:19:28]. Their internal Salesforce AI research group, which has worked on large language models since 2018 (shortly after the Google Transformer paper), is fine-tuning models for industry-specific and domain-specific use cases, such as code generation, Salesforce flow generation, financial services sales, and high-tech sales [00:19:35]. Customers can select models like Google's Gemini, OpenAI, or Azure OpenAI [00:19:53]. Salesforce also tracks and benchmarks models for cost, performance, and latency across various tasks [00:20:01]. They are developing sales-specific benchmarks for industries like Pharma and wealth management to evaluate model performance within specific domains [00:20:16].

## Challenges and Opportunities in AI Integration

The biggest [[challenges_and_opportunities_in_ai_integration | barriers to enterprise adoption]] of AI revolve around trust, due to real data security and privacy risks [00:24:12]. This includes preventing data leakage and ensuring AI respects internal sharing rules and entitlements within a company [00:24:19]. Once trust is established, customers are eager to [[experimenting_and_testing_ai_use_cases | experiment and use prompt builders]] [00:24:39].

The second major barrier is establishing a clear business case [00:24:48]. It's not just about cost, but about demonstrating productivity gains and margin expansion [00:24:52].

Salesforce facilitates adoption by offering "turnkey AI use cases" with pre-built prompts (e.g., Service GPT, Sales GPT, Commerce GPT) that can be set up in minutes, allowing customers to immediately see business value [00:25:27]. Customers then seek to customize these to their brand voice and reference their specific custom data fields [00:25:50]. This customization can often be achieved through prompt engineering rather than extensive fine-tuning of models [00:26:49].

User education is also crucial, especially to address fears that AI will replace jobs [00:10:49]. Salesforce aims to empower users by automating undesirable tasks rather than replacing their roles, as evidenced by naming their product "Co-pilot" instead of "Autopilot" [00:11:13]. This understanding comes from ethnographic research and direct engagement with users [00:11:23].

## Internal AI Usage at Salesforce

Salesforce extensively uses [[generative_ai_for_business_applications | generative AI internally]]. For example, they use their secure version of generative AI in Slack to brainstorm V2MOM (Vision, Values, Methods, Obstacles, Measures) planning [00:32:33]. AI acts as a co-pilot in Slack channels, facilitating brainstorming and collaboration among teammates [00:33:07].

### AI's Role in Slack

Salesforce has launched Slack AI, featuring conversation and channel summaries [00:34:47]. They are also bringing Einstein Co-pilot into Slack to enable features like service reply recommendations or summarizing customer information (support tickets, web engagement, marketing events) before meetings [00:34:58]. This integration supports a "team plus AI" future where AI augments human conversations and workflows, such as group coding or sales account management, by chiming in with suggestions [00:34:00].

## The Broader AI Landscape

Salesforce believes there is immense space for innovation and value creation in AI, both for incumbents like themselves and for new startups [00:28:29]. They actively invest in companies through Salesforce Ventures, hoping startups will build within the Salesforce ecosystem and leverage its Data Cloud and UI [00:28:52].

Clara Shih, herself a former entrepreneur, notes that if her previous company, Hearsay Systems (founded 2009), were started today, the "hearing" (mining signals from communications) aspect would be significantly easier due to advanced NLP capabilities compared to the past's reliance on regular expressions [00:31:00]. This allows for deeper insights from millions of regulated text messages and social posts [00:31:12].

Current killer [[ai_product_market_fit_and_emerging_applications | use cases for generative AI in the enterprise]] include:
*   Chatting with documents [00:31:40].
*   Customer support [00:31:41].
*   Code generation [00:31:46].

In the near future, AI is expected to impact every department, prompting a "rewriting of job descriptions" [00:32:01].

AI is not just for question answering but also for workflow orchestration [00:36:27]. For example, a co-pilot can be empowered to initiate a return merchandise authorization (RMA) and send shipping labels, though administrators must explicitly grant the co-pilot access to existing flows and Apex actions [00:36:31]. This allows for a cautious, phased approach to AI deployment, starting with less harmful actions like lookups before issuing refunds [00:37:17]. Salesforce's existing permissioning and workflow logic provides a significant advantage in enabling enterprises to selectively deploy AI [00:42:08].