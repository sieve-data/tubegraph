---
title: AI model selection and evaluation for businesses
videoId: j_zQHo-M8yY
---

From: [[redpointai]] <br/> 

The world of AI is rapidly evolving, leading to a shift from deterministic systems to more stochastic models, which presents new challenges and opportunities for businesses <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Salesforce, an incumbent company with extensive and diverse data, is actively navigating this landscape by integrating AI into its core products and developing strategies for model selection and evaluation to meet enterprise needs <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

## Salesforce's AI Product Strategy

Salesforce has shipped its first set of generative AI applications under the Einstein GPT brand, including Service GPT for customer service and Sales GPT for sales cloud users <a class="yt-timestamp" data-t="01:54:39">[01:54:39]</a>. A notable example is service reply recommendations and case summaries, which have significantly reduced time-consuming tasks for customer service representatives <a class="yt-timestamp" data-t="02:10:10">[02:10:10]</a>. These applications leverage a "Retrieval Augmented Generation" (RAG) approach, grounded in customer data within Salesforce <a class="yt-timestamp" data-t="02:27:39">[02:27:39]</a>.

The company recently launched Einstein Co-pilot, a natural language conversational assistant automatically grounded in customer data, metadata, and Salesforce flows <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>. Alongside this, Co-pilot Studio was released, enabling customers to customize their own co-pilot through a prompt builder and a model builder, allowing them to fine-tune or bring their own predictive models <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

### Organizational Structure for AI Development
Salesforce's approach to integrating AI has evolved from largely decentralized AI teams within each application cloud to a shared services AI platform team <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. This central team builds foundational components like the Einstein Trust Layer and the Model Gateway, which are essential for every Salesforce application <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>. Product-specific teams now focus on predictive AI for their use cases and build on this shared platform, creating specialized actions for Einstein Co-pilot within their respective clouds (e.g., Sales Cloud building sales actions) <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.

## Trust and Guardrails in Enterprise AI
For enterprises, especially those dealing with sensitive customer data like Gucci, trust is paramount when deploying AI <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. Salesforce addresses this through a multi-layered approach:

1.  **Technology Integration:** The Einstein Trust Layer is engineered into the product, offering features like data masking, data grounding to reduce hallucinations, citations, audit trails, prompt defense, and zero data retention prompts <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. Data masking, for instance, has been used for years to mitigate bias from sensitive data fields like name, gender, or zip code <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.
2.  **Acceptable Use Policy:** This policy requires AI bots to self-identify as AI to customers <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
3.  **Stakeholder Engagement:** Salesforce has developed and open-sourced a set of trusted AI guiding principles centered on accuracy, honesty, and empowerment, shared across the industry and with government regulators <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.

A significant challenge in enterprise AI adoption is addressing data security, data privacy, and ethical risks, including preventing data leaks and honoring internal sharing rules and entitlements within the organization <a class="yt-timestamp" data-t="0:24:12">[0:24:12]</a>. Once these trust concerns are alleviated, customers are typically eager to experiment with AI <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

## [[enterprise_use_of_ai_and_model_specialization | AI Model Selection and Customization]] for Businesses
Salesforce adopts an open architecture approach for [[enterprise_use_of_ai_and_model_specialization | AI model selection]], allowing customers to choose from models on their service, bring their own models, or integrate third-party models <a class="yt-timestamp" data-t="0:19:12">[0:19:12]</a>.

### Data Types Supporting AI
Salesforce's strength in AI is underpinned by four types of unique data:
1.  **Structured CRM data records:** Traditional salesforce heritage <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.
2.  **Unstructured data:** Knowledge articles, conversation transcripts from Slack, contact center voice calls, chats, and emails <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. Salesforce's Data Cloud is expanding to include vector search and hybrid reranking for both structured and unstructured data, with zero ETL partnerships with major data lake providers <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
3.  **Metadata layer:** Created 25 years ago for multi-tenancy, this layer is crucial for providing context to AI, indicating which data objects, tables, or functions to use <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
4.  **Feedback data:** As the world's largest database of customer outcomes (e.g., sales opportunity stage, marketing campaign results), this data serves as a reward function for any AI model, whether predictive or generative, and is captured in the Data Cloud <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

### Model Choice and Specialization
The current model landscape is dynamic, with no clear winner <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. Salesforce believes different models will be optimal for different tasks and use cases over time <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

*   **Salesforce's internal models** are being built and fine-tuned for industry-specific and domain-specific use cases, such as code generation, Salesforce flow generation, or financial services sales <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
*   **Customer choices** often align with existing cloud providers (e.g., Google Cloud customers preferring Gemini) or depend on the complexity of the task (e.g., GPT-4 for complex agentic planning) <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

Rather than fine-tuning models for specific brand voices (like Gucci vs. Ford), it's often simpler and more effective to adjust the prompt itself <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

## [[ai_model_evaluation_and_benchmarking | AI Model Evaluation and Benchmarking]]
[[ai_model_evaluation_and_benchmarking | Evaluating AI models]] is complex due to variables like fine-tuning and the RAG pipeline <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Salesforce focuses on tracking and benchmarking models for cost, performance, and latency for each specific task <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

*   **Domain-Specific Benchmarking:** Salesforce creates sales-specific benchmarks tailored to industries like pharma or wealth management <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. This approach recognizes that performance in one domain (e.g., general question answering) may not reflect performance in a highly specific business context (e.g., upselling a handbag after a belt issue) <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **Feedback Loops:** The vast amount of customer outcome data collected by Salesforce allows for continuous feedback loops to make models "smarter and smarter" by acting as a reward function <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

## Barriers to Enterprise AI Adoption

While the potential for AI is immense, businesses face significant hurdles in scaling deployment beyond initial piloting:
1.  **Trust (Data Security and Privacy):** This is the biggest barrier <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. Enterprises worry about data leakage and ensuring that AI adheres to existing internal data sharing rules and entitlements <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
2.  **Business Case:** Clearly defining the business case and demonstrating productivity gains or margin expansion is crucial for justifying AI investment <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. AI adoption is about whether the return on investment (ROI) outweighs the cost <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. For example, Gucci saw reduced average handle time in customer service and increased conversion rates, transforming a cost center into a revenue center with AI <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
3.  **User Education:** Addressing user fears about job displacement is vital <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Salesforce emphasizes that AI is meant to empower users and handle undesirable tasks, rather than replacing roles <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Products are designed with clear onboarding experiences and "co-pilot" naming to reinforce AI as a helpful coworker <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
4.  **Cost:** While costs are decreasing, they remain a consideration for scaling AI solutions across an entire contact center or for multiple use cases <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Salesforce addresses this by routing tasks to the appropriate model size and emphasizing clear business cases <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

To facilitate adoption, offering turnkey AI use cases that are easy to get up and running, like service reply recommendations, allows customers to immediately see the business value <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## Future Outlook for Enterprise AI

AI is expected to transform every department within a company, necessitating a re-evaluation of job descriptions and the learning of new skills, similar to the adoption of the internet and email in the 1990s <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

Key areas of growth for generative AI in the enterprise include:
*   Chatting with documents <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   Customer support <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   Code generation <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

Beyond these, AI will move into workflow orchestration, allowing co-pilots to initiate actions like processing returns or sending shipping labels based on defined workflows and administrator permissions <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. This requires careful governance and control, allowing admins to select which existing flows and functions the co-pilot can access <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

The future of work will increasingly involve "team plus AI" collaborations, as seen in platforms like Slack <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. Slack AI already provides conversation and channel summaries <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>. Integrating Einstein Co-pilot into Slack will enable real-time assistance, such as generating service reply recommendations, summarizing customer activity, or assisting with sales account closing by providing insights to the entire team <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. This "multiplayer" AI experience will shift from single-user interactions to collaborative engagements with AI bots as team members <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.