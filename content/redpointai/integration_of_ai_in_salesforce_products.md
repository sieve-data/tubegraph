---
title: Integration of AI in Salesforce products
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

Salesforce, an incumbent with extensive data, has rapidly advanced its [[integration_of_ai_and_data_platforms_in_enterprises | AI integration]] within its products, as discussed by Clara Shih, CEO of Salesforce AI on the "Unsupervised Learning" podcast <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The company aims to make AI an integral part of how businesses operate, predicting that in 10 years, current work methods will seem "completely different" due to AI's influence <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Key AI Products and Features

Salesforce has developed several generative AI applications under the **Einstein GPT** brand <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:
*   **Service GPT** for customer service <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>
*   **Sales GPT** for Sales Cloud users <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>
*   **Commerce GPT** for e-commerce <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>

Recently, Salesforce launched its **Einstein Co-pilot** and **Co-pilot Studio** <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **Einstein Co-pilot** is a natural language conversational assistant grounded in customer data, metadata, and Salesforce flows <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Co-pilot Studio** allows customers to customize their own co-pilot <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. It includes a prompt builder for creating and saving "golden prompts" referencing specific Salesforce data fields <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. It also features a model builder, enabling customers to fine-tune or integrate their own predictive models into the Salesforce AI stack <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## [[Impact of AI on Customer Support | AI's Impact on Customer Support]]

A standout application has been **service reply recommendations** and **case summaries** within Service GPT, which significantly reduce time-consuming tasks for customer service personnel <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This system grounds queries in customer data within Salesforce, making it feel "magical" for users <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Gucci Case Study
Gucci, an early adopter of Salesforce AI, deployed Service GPT to its customer service teams in Florence, Italy, and New Jersey <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The AI augmented service representatives in real-time, allowing them to:
*   **Reduce average handle time** for customer issues <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Uplevel to become salespeople and brand storytellers** <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, if a customer called about a belt issue, the AI could recommend new products like handbags they had browsed, coaching the representative in real-time <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   **Increase conversion rates by double digits** <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   **Transform the cost center of customer service into a revenue center** <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. This shift empowers customer service representatives, making them feel they are doing "the best work of their careers" <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Organizational Structure for AI Development

Salesforce's AI team structure has continuously evolved <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Initially, AI folks were largely decentralized within each application cloud <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. However, recognizing the need for shared infrastructure (like the Einstein Trust Layer and model gateway) across all apps, Salesforce created a **new shared services AI platform team** <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. This central team builds foundational AI components (Trust Layer, Gateway, Prompt Builder, Einstein Co-pilot) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, while individual product teams (e.g., Sales Cloud, Service Cloud, Slack) focus on predictive AI for their specific use cases and build actions on the central platform <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Trust and Guardrails in AI Deployment

Given its large enterprise client base, Salesforce prioritizes trust, security, and ethical considerations for AI deployment <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
1.  **Technology:** The **Einstein Trust Layer** is engineered into the product, providing features such as:
    *   Data masking <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>
    *   Data grounding with Data Cloud to reduce hallucinations <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
    *   Citations <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>
    *   Audit trails <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>
    *   Prompt defense <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>
    *   Zero retention prompts <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>
    These features mitigate data security, privacy, and ethical risks <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Salesforce also proactively surfaces sensitive data fields and recommends masking them to prevent bias in AI models <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
2.  **Acceptable Use Policy:** For AI Bots, the AI is required to self-identify as an AI <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
3.  **Stakeholder Engagement:** Salesforce has developed open-source **trusted AI guiding principles** (accuracy, honesty, empowerment), shared with the industry and government regulators <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## Data Strategy

Salesforce leverages four unique types of data crucial for AI <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>:
1.  **Structured CRM Data:** The traditional Salesforce heritage of data records <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>.
2.  **Unstructured Data:** Including knowledge articles, conversation transcripts from Slack, contact center voice calls, and emails <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. Salesforce is expanding its Data Cloud for vector search and hybrid reranking across both structured and unstructured data <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. They also have zero ETL partnerships with major data lake providers (e.g., BigQuery, Redshift, Snowflake, Databricks) <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
3.  **Metadata Layer:** Created 25 years ago for multi-tenancy, this layer is crucial for providing context to AI, helping it identify relevant data objects, tables, and functions <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
4.  **Feedback Data:** As the world's largest database of customer outcomes (e.g., sales opportunity stages, marketing campaign conversions), this data serves as a reward function for any AI model, both predictive and generative <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Model Strategy and [[Role of custom models and enterprise AI integration | Custom Model Integration]]

Salesforce adopts an **open architecture approach** to models, allowing customers to choose models on their service, or bring their own first-party or third-party models via the model builder <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This acknowledges that different models will be optimal for different tasks and use cases <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.

Salesforce's own research models are fine-tuned for industry-specific and domain-specific use cases, such as code generation, Salesforce flow generation, financial services sales, and high-tech sales <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. Customers can select models from providers like Google, OpenAI, or Azure OpenAI <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. Salesforce also benchmarks models for cost, performance, and latency per task, creating specific benchmarks for industries like Pharma or Wealth Management <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

## Barriers to Enterprise AI Adoption

While cost is a consideration, especially for scaling, it is not the primary barrier <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>.
The biggest barriers for enterprises to scale AI adoption are:
1.  **Trust:** Concerns around data security, data privacy risks, and honoring sharing rules and entitlements within the organization <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
2.  **Business Case:** Clearly defining how AI will drive productivity, margin expansion, and a positive ROI <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.

Salesforce addresses these by providing "turn-key AI use cases" with pre-built prompts, allowing customers to quickly see business value <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. Customers can then customize these prompts with their brand voice and custom data fields (e.g., Gucci's "style" field vs. Ford's "car model" field) <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.

## [[Role of AI in Future Business Operations | Future of AI in Business Operations]]

Salesforce envisions AI transforming every department and requiring everyone in a company to "rewrite their job description" <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. They believe the "team + AI" paradigm will be the future, where humans and AI collaborate seamlessly <a class="yt-timestamp" data-t="00:34:26">[00:34:26]</a>.

### Internal AI Use
Salesforce uses generative AI internally in various ways <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>:
*   **V2MOM Planning:** Brainstorming and summarizing Vision, Values, Methods, Obstacles, and Measures within departments and roles <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.
*   **Product Launch Planning:** Using AI as a co-pilot in Slack for brainstorming and collaboration <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.

### AI in Slack
Salesforce has launched **Slack AI**, which includes conversation and channel summaries <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>. They are working to bring Einstein Co-pilot into Slack, enabling features like service reply recommendations, summarizing customer data, and sales opportunities before meetings <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>. This allows entire account teams to access comprehensive customer information, augmenting collaborative workflows like group coding or sales account closing with AI insights <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.

### Workflow Orchestration
AI's utility extends beyond question answering to **workflow orchestration** <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>. For example, a co-pilot can be empowered to initiate returns or send shipping labels. However, this is done with a layer of governance: admins must explicitly designate which existing flows the co-pilot has access to, starting with "least harmful" actions <a class="yt-timestamp" data-t="00:36:57">[00:36:57]</a>. This permissioning ensures that the AI's actions align with organizational rules and entitlements <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>.

## Incumbents vs. Startups

Salesforce believes there is ample space for innovation and value creation in the AI ecosystem, both for incumbents and startups <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. While incumbents like Salesforce have an advantage due to existing data and platform logic, they also invest in startups through Salesforce Ventures <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. They encourage startups to build within the Salesforce ecosystem and on its platform, leveraging its data cloud and UI <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

For more information, visit salesforce.com/Einstein <a class="yt-timestamp" data-t="00:40:46">[00:40:46]</a>.