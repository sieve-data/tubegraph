---
title: Enterprise AI adoption challenges and solutions
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

In the rapidly evolving landscape of artificial intelligence, enterprises face significant [[challenges_in_ai_adoption_and_deployment | challenges in AI adoption and deployment]]. However, with strategic approaches and innovative solutions, these barriers can be overcome, leading to successful integration and transformative outcomes <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Current State of Enterprise AI
AI is already profoundly impacting how companies operate, with expectations that current work methodologies will seem "ridiculous" in a decade, much like filing papers in the early 1990s <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Salesforce, an incumbent with extensive and valuable data, has moved quickly to integrate AI into its product offerings <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

### Key Use Cases
Salesforce's first generative AI applications, under the Einstein GPT brand, include Service GPT for customer service and Sales GPT for sales users <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

Notable examples include:
*   **Service Reply Recommendations and Case Summaries**: These generative AI applications have been particularly impactful for customer service, automating time-consuming tasks and reducing customer wait times <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. They ground responses in customer data within Salesforce, making the process feel "magical" for users <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Customer Support Transformation (Gucci Example)**: For Gucci, AI transformed their customer service team from a cost center into a revenue center <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Service agents, augmented by AI, could seamlessly transition from resolving issues to becoming salespeople and brand storytellers, leading to double-digit increases in conversion rates <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This shift empowers employees, enabling them to engage in higher-value activities and feel more fulfilled in their careers <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Code Generation**: Beyond customer support, code generation is another "killer use case" for generative AI in the enterprise <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>.

### Recent Product Launches
Salesforce recently announced the general availability (GA) of:
*   **Einstein Co-pilot**: A natural language conversational assistant automatically grounded in customer data, metadata, and workflows within Salesforce <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Co-pilot Studio**: Enables customization of co-pilots through a prompt builder for creating "golden prompts" that reference specific Salesforce data fields, and a model builder allowing customers to fine-tune or integrate their own predictive models into the Salesforce AI stack <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## [[Challenges and Strategies in Enterprise AI Deployment | Challenges and Strategies in Enterprise AI Deployment]]

### 1. Trust and Security
The biggest barrier to enterprise AI adoption is trust, encompassing data security, data privacy, and ethical risks <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. Concerns include data leakage and maintaining internal sharing rules and entitlements for different employees and departments <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

**Solutions:**
*   **Einstein Trust Layer**: Engineered into the product, it offers features like data masking, data grounding with Data Cloud (to reduce hallucinations), citations, audit trails, prompt defense, and zero retention prompts <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Acceptable Use Policy**: Requires AI bots to self-identify as AI, ensuring transparency for consumers <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Trusted AI Guiding Principles**: Open-source principles (accuracy, honesty, empowerment) shared with industry and government regulators <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Cautious Implementation**: Start with "least harmful" actions like data lookups before enabling more sensitive actions like issuing refunds <a class="yt-timestamp" data-t="00:37:17">[00:37:17]</a>. Administrators control which existing workflows (flows and Apex) co-pilots can access <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>.

### 2. Business Case and ROI
Defining a clear business case and demonstrating return on investment (ROI) is crucial <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. It's not just about cost, but about productivity gains and margin expansion <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

**Solutions:**
*   **Focus on Measurable Outcomes**: For example, reducing average time to resolve customer issues and driving incremental revenue lift through AI inferences <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
*   **Turnkey AI Use Cases**: Offering pre-built, easy-to-deploy use cases like Service GPT or Sales GPT allows customers to quickly see business value in just five minutes, which then prompts them to explore customization <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### 3. User Adoption and Education
There can be fear among users that AI will replace their jobs <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. User education and tailored user experiences are vital to show that AI empowers, rather than replaces, their roles, automating undesirable tasks <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

**Solutions:**
*   **Empowerment-Focused UX**: Naming features "co-pilot" instead of "autopilot" clearly communicates that AI is a collaborative tool <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. Initial in-product messages explain the feature's purpose and how it supports the user <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>.
*   **Ethnographic Research**: Spending time with users, like in call centers, helps understand their concerns and address them through product changes or learning modules <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### 4. Cost and Performance Optimization
While AI costs are decreasing, scaling solutions across an entire enterprise remains a significant consideration <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

**Solutions:**
*   **Multi-Model Architecture**: Salesforce uses an open architecture approach, allowing customers to choose from various models (Google, OpenAI, Azure OpenAI, or bring their own) or use Salesforce's fine-tuned models for industry-specific use cases <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This allows routing the right task to the right-sized model for optimal cost, performance, and latency <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.
*   **Vertical-Specific Benchmarks**: Salesforce develops specialized benchmarks (e.g., for Pharma sales or wealth management) to evaluate model performance, recognizing that general evaluations aren't sufficient for specific industry needs <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>.

### 5. Data Management and Context
Effective AI deployment relies on unique and relevant data. Salesforce's data assets are key:
*   **Structured CRM Data**: Traditional sales and customer data records <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Unstructured Data**: Knowledge articles, conversation transcripts from Slack, voice calls, chats, emails, etc. <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.
*   **Metadata Layer**: Provides crucial context for AI to understand which data objects, tables, and functions to use <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>.
*   **Feedback Data**: Captures customer outcomes (e.g., sales opportunity stage progression, marketing campaign conversions), which serves as a reward function for AI models <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.

**Solutions:**
*   **Data Cloud with Vector Search and Hybrid Reranking**: Expanded to work across both structured and unstructured data <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
*   **Zero ETL Partnerships**: With major data lake providers (BigQuery, Redshift, Snowflake, Databricks) to integrate data from across the customer's enterprise environment <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Custom Data Referencing**: AI can reference custom data fields (e.g., Gucci's "style" field or Ford's car make/model) to provide highly personalized interactions <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>. This personalization can be achieved through prompt engineering rather than extensive fine-tuning <a class="yt-timestamp" data-t="00:26:48">[00:26:48]</a>.

## Organizational Structure for AI Development
Salesforce initially decentralized AI efforts within each application cloud but transitioned to a shared services AI platform team <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This centralized team builds foundational components like the Einstein Trust Layer and model gateway, which are needed by every application <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Individual product teams now focus on predictive AI for their specific use cases and build on the shared platform by creating product-specific actions for Einstein Co-pilot <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Future Outlook
The shift from deterministic to stochastic models in AI marks a fundamental change in operation and thinking <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The internal AI research group, which has been working on large language models since 2018 and even published on prompt engineering, helps Salesforce stay at the forefront <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. A "Frontier AI group" is also formed, jointly run by the CEO of Salesforce AI and the chief scientist, to rapidly prototype new AI capabilities off the main Salesforce stack, graduating successful experiments into core products <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

The future of AI will involve:
*   **AI for Every Department**: Every role within a company will need to redefine its job description, as AI becomes an integral part of daily work, similar to how the internet and email were adopted <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.
*   **Team + AI Collaboration**: Workflows will increasingly involve a combination of human teams and AI. Slack is seen as an ideal interface for this, enabling features like conversation summaries and Einstein Co-pilot integration, allowing teams to brainstorm, code, and strategize with AI augmentation <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.
*   **Workflow Orchestration**: Beyond question answering, AI will excel at orchestrating complex workflows, such as initiating returns or sending shipping labels, provided with proper governance and admin permissions <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.

While the AI world is currently "hyped," it is believed that "we haven't seen anything yet," comparing the current stage to 1998 for the internet, but moving much faster <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>. The focus remains on ensuring that the tremendous benefits of AI are accessible to everyone, not just a select few <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.