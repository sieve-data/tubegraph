---
title: Enterprise AI adoption challenges
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

Enterprises face several [[challenges_in_enterprise_ai_deployment | challenges]] in adopting and scaling AI, despite the rapid advancements in the field <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. According to Clara Shih, CEO of Salesforce AI, these barriers range from fundamental concerns about trust to the practicalities of proving business value and managing costs <a class="yt-timestamp" data-t="00:24:06">[00:24:06]</a>.

## Key Barriers to [[enterprise_ai_adoption_and_deployment_models | Enterprise AI Adoption]]

### Trust and Governance
The biggest barrier to AI adoption in enterprises is trust <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>. This encompasses:
*   **Data Security and Privacy Risks** <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>: Concerns about data leaking out of an organization <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.
*   **Internal Sharing Rules and Entitlements** <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>: Ensuring AI honors permissions for different employees and departments who have access to varying workflows and data sets <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.
*   **Ethical Risks** <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>: For example, the requirement for AI bots to self-identify to consumers <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Business Case and ROI
After trust, the second significant barrier is establishing a clear business case <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. Enterprises need to demonstrate how AI investments lead to productivity gains and margin expansion, ensuring the return on investment (ROI) outweighs the spending <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>. Specific business cases, such as reducing average time to resolve customer issues or driving incremental revenue, are crucial for investment <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

### Cost Considerations
While costs are decreasing (e.g., 10x year-over-year for inference) <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>, the expense of AI remains a consideration for customers when scaling deployments to their entire contact center or for multiple use cases <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. This drives the need for multi-model architectures that can route the right task to the right-sized model to optimize cost-performance <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

### User Education and Adoption
There is a fear among users that AI will replace certain jobs <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. User education is vital to clarify that AI is intended to empower users and replace undesirable parts of their jobs, rather than eliminate them <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. This requires ethnographic research to understand user concerns and address them through product design or learning modules <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. The naming "co-pilot" (vs. "autopilot") emphasizes this assistive role <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

### Shifting Paradigms
The transition from deterministic AI models to stochastic ones is a challenging new way of operating, thinking, and building <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This fundamental shift requires constant adaptation and presents daily [[challenges_and_strategies_in_ai_deployment | challenges]] <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Model Evaluation and Benchmarking
The rapidly evolving model space makes it too early to call a winner <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. Different models will be used for different tasks and use cases <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. A key [[challenges_and_strategies_in_ai_deployment | challenge]] is tracking and benchmarking which model offers the best cost, performance, and latency for specific tasks <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. This often requires domain-specific evaluations rather than general ones <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

### Workflow Integration and Permissioning
Integrating AI into existing workflows and defining clear permissioning (e.g., enabling certain actions for a co-pilot but not others) is complex <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. Enterprises need to cautiously, but optimistically, step into the AI landscape, configuring exactly what AI can and cannot do <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.

## Salesforce's Approach to Overcoming Challenges

Salesforce has developed several strategies and products to address these [[challenges_in_enterprise_ai_deployment | challenges]]:

### Einstein Trust Layer
This engineered solution builds trust directly into the product <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Key features include:
*   **Data Masking** <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>: Proactively surfaces sensitive data fields and recommends masking them to prevent bias <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Data Grounding with Data Cloud** <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>: Uses customer data in Salesforce to reduce hallucinations <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Citations and Audit Trail** <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>: Provides transparency on AI outputs <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
*   **Prompt Defense** <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>: Protects against malicious inputs.
*   **Zero Retention Prompts** <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>: Ensures data privacy.

### Acceptable Use Policy
Salesforce implements policies such as requiring AI Bots deployed to customers to self-identify as AI, ensuring transparency for consumers <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Trusted AI Guiding Principles
Salesforce has developed and open-sourced a set of trusted AI guiding principles centered around accuracy, honesty, and empowerment <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. These principles are shared with the industry and government regulators <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Product Offerings for Adoption
*   **Einstein GPT Brand** <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>: Includes applications like Service GPT, Sales GPT, and Commerce GPT, which offer generative AI capabilities <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.
*   **Einstein Co-pilot** <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>: A natural language conversational assistant grounded in customer data, metadata, and Salesforce flows <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Co-pilot Studio** <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>: Allows customers to customize their co-pilot, create and save "golden prompts" referencing specific Salesforce data fields, and bring their own predictive models <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Turnkey AI Use Cases** <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>: Offering pre-built prompts and applications that take five minutes to get up and running, immediately demonstrating business value <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.
*   **Customization for Brand Voice and Data** <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>: Enables companies like Gucci to ensure AI captures their unique brand voice and references custom data fields (e.g., customer style, shopping frequency) <a class="yt-timestamp" data-t="00:25:57">[00:25:57]</a>.

### Organizational Structure
Salesforce evolved its team structure from decentralized AI teams within each application cloud to a new shared services AI platform team <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This central team builds foundational elements like the Einstein Trust Layer and Model Gateway, while individual product teams own predictive AI for their use cases and build actions on the shared platform <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Open Model Architecture
Salesforce adopts an open architecture for models, allowing customers to choose from models on their service, bring their own, or integrate third-party models <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. They also build and fine-tune their own research models for industry-specific and domain-specific use cases, such as code generation or financial services sales <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

### Domain-Specific Benchmarking
Salesforce focuses on creating sales-specific benchmarks for various industries (e.g., Pharma, Wealth Management) to evaluate model performance, recognizing the complexity introduced by fine-tuning and the entire Retrieval-Augmented Generation (RAG) pipeline <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

## Impact and Future Outlook
AI is changing traditional job definitions, turning cost centers like customer service into revenue centers by augmenting employees to take on higher-value activities <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Salesforce has seen double-digit conversion rate increases in such cases <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. The company believes AI will revolutionize every department and require everyone to rewrite their job descriptions <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>. The future of AI interaction is seen as "team plus AI," with group chatting and coding augmented by AI co-pilots <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.