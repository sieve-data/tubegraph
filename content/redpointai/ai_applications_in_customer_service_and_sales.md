---
title: AI applications in customer service and sales
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

Salesforce AI, under the Einstein GPT brand, has developed generative [[AI applications in the legal industry | AI applications]] tailored for enterprise use, particularly in customer service and sales. Salesforce is seen as an incumbent that holds significant data and has rapidly adopted AI [00:00:10].

## Key AI Applications in Salesforce Products

Salesforce has incorporated AI across its product suite, including:
*   **Service GPT** for customer service [00:01:59].
*   **Sales GPT** for sales cloud users [00:02:02].

Specific features that have shown significant impact include:
*   **Service reply recommendations** and **case summaries** [00:02:10]. These features automate time-consuming tasks for customer service representatives and reduce waiting times for customers [00:02:15]. This approach allows humans to focus on tasks they excel at, while AI handles repetitive elements [00:02:40].
*   **Einstein Co-pilot**, a natural language conversational assistant grounded in customer data, metadata, and existing Salesforce flows [00:05:21].
*   **Co-pilot Studio**, which enables customization of co-pilots, creation of "golden prompts" that reference specific data fields, and integration of custom predictive models [00:05:37].

AI is increasingly blurring the traditional lines between job roles, for example, transforming customer service representatives into augmented salespeople [00:02:57].

## Case Study: Gucci

Gucci, an early adopter of Salesforce AI, implemented Service GPT for its service team, which operates from Florence, Italy, and New Jersey [00:03:04].
*   The implementation led to a **reduction in average handle time** for customer inquiries [00:03:15].
*   AI augmented customer service agents in real-time, enabling them to become **salespeople and brand storytellers** [00:03:24]. For instance, if a customer called about a belt issue, the AI could recommend other products like handbags based on their browsing history or items left in a cart [00:03:59].
*   This augmentation resulted in **double-digit increases in conversion rates** [00:04:20].
*   The customer service team, traditionally a cost center, began to operate as a **revenue center** [00:04:22].
*   Customer service representatives felt empowered and reported doing "the best work of their careers," with their careers taking on a new life [00:04:43].

The rapid deployment of Service GPT (60 days) was possible due to a year and a half of prior research and development, including early collaboration with Gucci starting in November 2021 [00:14:06].

## Impact on Workforce and User Education

The introduction of AI tools like Einstein GPT and co-pilots has addressed fears about job replacement by focusing on empowering users and replacing undesirable job tasks [00:11:02]. Salesforce emphasizes that AI acts as a "co-pilot," not an "autopilot," serving as a coworker that users can interact with via natural language to request actions or information [00:11:51].

User education is crucial, involving ethnographic research like sitting with call center users to understand their concerns and addressing them through product design or learning modules [00:11:23]. Initial product messages and the "co-pilot" naming convention are designed to clarify the AI's role as an empowering tool [00:11:44].

## Data and Trust in AI Deployment

Salesforce's unique position is underpinned by four types of data crucial for AI:
1.  **Structured CRM data**: Traditional data records like sales forces' heritage [00:16:38].
2.  **Unstructured data**: Includes knowledge articles, conversation transcripts from Slack channels, contact center voice calls, chats, and emails [00:16:49]. Salesforce's Data Cloud is expanding with vector search and hybrid reranking to work across both structured and unstructured data [00:17:09].
3.  **Metadata layer**: Created 25 years ago for multi-tenancy, this layer provides context to AI, guiding which data objects, tables, or functions to use [00:17:35].
4.  **Feedback data**: Salesforce captures customer outcomes (e.g., sales opportunity stages, marketing campaign results) as a data pipeline in Data Cloud. This data serves as a reward function for any AI model, whether predictive or generative [00:18:01].

Salesforce emphasizes that it's the customer's data, not Salesforce's product, and adheres to a strict "zero retention prompts" policy [00:16:19].

### Guardrails and Trust Layer

Trust is a primary barrier to enterprise AI adoption [00:24:12]. Salesforce addresses this through a multi-layered approach:
1.  **Technology (Einstein Trust Layer)**: Features include data masking, data grounding with Data Cloud to reduce hallucinations, citations, audit trails, prompt defense, and zero retention prompts [00:07:56]. Data masking, for example, has been used for years to proactively hide sensitive data fields (like name, gender, zip code) to prevent bias in AI models [00:09:23].
2.  **Acceptable Use Policy**: Requires AI bots to self-identify as AI when interacting with consumers [00:08:16].
3.  **Stakeholder Engagement**: Developed open-source "trusted AI guiding principles" (accuracy, honesty, empowerment) shared with the industry and government regulators [00:08:36].

## Model Selection and Customization

Salesforce adopts an open architecture approach, allowing customers to choose models from their service, bring their own, or integrate third-party models via their Model Builder [00:19:12]. Different models are expected to be used for different tasks and use cases over time [00:19:28].

Salesforce's own research models are fine-tuned for industry and domain-specific use cases, such as code generation, Salesforce flow generation, or financial services sales [00:19:37]. Customers can select models like Google's Gemini or OpenAI's Azure OpenAI [00:19:53]. The goal is to track and benchmark models based on cost, performance, and latency for specific tasks [00:20:01].

Salesforce builds industry-specific benchmarks (e.g., for Pharma or wealth management sales) to evaluate model performance, recognizing that domain-specific evaluation is more relevant than general evaluation [00:20:19].

## Barriers to Enterprise Adoption

The biggest barriers to scaling AI adoption in enterprises are:
1.  **Trust**: Concerns around data security, data privacy, and ensuring AI respects internal sharing rules and entitlements within a company [00:24:12].
2.  **Business Case**: Enterprises need to clearly define the business case, focusing on productivity gains and margin expansion to justify investment [00:24:48]. For instance, the Gucci example highlights reduced average handle time and incremental revenue lift [00:25:07].

Salesforce addresses these barriers by providing turnkey AI use cases (e.g., Service GPT) that are easy to set up and demonstrate immediate business value [00:25:27]. They also allow customers to customize AI behavior, such as brand voice and referencing custom data fields unique to their business [00:25:50]. This customization is facilitated by features like the Prompt Builder and Co-pilot Studio [00:26:29].

## Future of AI in the Enterprise

Beyond current "killer use cases" like [[Impact of AI on Customer Support | customer support]], chat-your-documents, and code generation, AI is expected to permeate every department [00:31:37]. Every job description will likely need to be rewritten, with functional leads and first-line managers guiding employees on how to leverage AI, similar to how workers learned to use the internet and email in the 1990s [00:32:00].

Salesforce uses generative AI internally for V2MOM (Vision, Values, Methods, Obstacles, Measures) planning in Slack, helping brainstorm initiatives and summarize methods [00:32:36]. This highlights the emerging trend of "team plus AI" workflows, such as group chatting with AI or group coding with AI, where AI augments human conversations and decision-making in real-time [00:33:57].

Slack is seen as a perfect interface for generative AI [00:34:30]. Salesforce has launched Slack AI with conversation and channel summaries [00:34:47]. They are also bringing Einstein Co-pilot into Slack, allowing users to get service reply recommendations or summarize all open support tickets, marketing engagement, and events related to a customer before a meeting, visible to the entire account team [00:35:00].

While the percentage of customer support questions answerable by AI varies by industry, AI's utility extends beyond mere question answering to workflow orchestration (e.g., initiating returns and sending shipping labels) [00:36:16]. Governance and control layers are crucial, allowing administrators to designate which existing workflows their co-pilot has access to, starting with less harmful actions like data lookups before potentially enabling more impactful actions like issuing refunds [00:36:56].