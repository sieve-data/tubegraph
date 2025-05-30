---
title: Enterprise applications for AI including business intelligence and data extraction
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Snowflake, led by Head of AI Baris Gakkan, focuses on developing infrastructure that supports AI tools in production, offering significant insights into real-world AI use cases for businesses <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Snowflake's comprehensive AI product portfolio includes Cortex AI, the data cloud, and their own Large Language Model (LLM) Arctic <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Snowflake's AI Product Portfolio

Snowflake's core AI offering is Cortex, an inference engine that runs various large language models, including Arctic, Mistral, and Meta models <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Built on top of Cortex are two key products:
*   **Cortex Search** – A high-quality search system essential for Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. It uses Arctic Embed, Snowflake's embedding model, which is noted for its efficiency and state-of-the-art performance <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Cortex Search is a hybrid system, combining vector search and lexical keyword search to reduce hallucinations <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Cortex Analyst** – A business intelligence (BI) product designed for interacting with structured data <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

Snowflake's strategic acquisitions, such as Neva (which brought its CEO and Neva technology for embedding models and search) and Trulens (an observability and LLM evaluation platform), have been instrumental in building out their AI capabilities <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>, <a class="yt-timestamp" data-t="00:28:55">[00:28:55]</a>.

## [[generative_ai_for_business_applications | Generative AI for Business Applications]]

Snowflake's customers leverage AI for three primary use cases <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>:

### AI for Business Intelligence (BI) and Text-to-SQL
This use case focuses on creating BI-type experiences using natural language to SQL to data <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. Snowflake’s Arctic LLM was specifically developed to excel at SQL generation and follow instructions effectively <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

#### Challenges in AI for BI
*   **"Iceberg Problem"**: Demos are easy to build, but real-world data is "incredibly messy" <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Data Complexity**: Companies often have tens of thousands of tables and hundreds of thousands of columns with inconsistent naming conventions (e.g., "rev one," "rev two") <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Accuracy and Hallucinations**: LLMs might hallucinate column names, get complex joins wrong, or generate non-executable queries <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. LLMs will provide answers even when they shouldn't <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Trust in Business Criticality**: For BI uses like reporting revenue to a CFO, 90-95% accuracy is often insufficient; complete trust is required <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

#### Solutions and Approaches
*   **Stitching Multiple Systems**: Cortex Analyst combines three to four LLMs working together to answer BI questions <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Self-Healing Systems**: These systems generate SQL, check its validity, and learn when to ask for clarifications or abstain from answering questions it cannot answer <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Human-in-the-Loop**: Systems are being built to ensure human oversight and correction <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Verified Queries**: Customers can create "verified queries" which, if used, are returned with increased confidence via the API <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Prioritizing Precision over Recall**: Snowflake consciously makes a product choice to prioritize precision, meaning they focus on providing correct answers even if it means not answering all questions <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This contrasts with an open-ended approach suitable for analysts, but not business users <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Data Extraction and Text Analytics
This involves using natural language to extract data from text for later processing <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This is seen as a well-working application of AI <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

#### Use Cases
*   **Analyzing Unstructured Data**: Processing documents, PDFs, sales call logs, customer support tickets, and other semi-structured text in batch <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Employee Survey Analysis**: An LLM can summarize open-ended employee survey questions, categorize responses, and provide example quotes, tasks that previously took hours <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Simplifying Workflows**: Snowflake focuses on providing simple, easy-to-use, task-specific functions that reduce the need for customers to manage prompts and data pipelines <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### Other Enterprise AI Applications
*   **Chatbots**: Building chatbots for interacting with unstructured data <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Internal Productivity Tools**: Internal use cases for AI, such as summarizing sales conversations, employee assistants for internal documents, and documentation-oriented chatbots, are common and carry lower risk from hallucinations <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>, <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>.
*   **Enterprise Search**: Upgrading existing enterprise search stacks with AI capabilities <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## [[enterprise_ai_adoption_challenges | Challenges in Enterprise AI Deployment]] and Solutions

### Data Governance, Security, and Access Control
A major initial step for large companies is ensuring comfort with the chosen AI platform, focusing on trust, data security, respect for data governance, and acceptable policies <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

*   **Running AI next to data**: Snowflake's advantage lies in running all models inside Snowflake, right next to customer data, ensuring data security and adherence to granular access controls <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Granular Access Controls**: Snowflake's existing granular access controls for database objects extend to AI systems. For instance, search systems filter results based on user access to documents <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. This prevents data leakage and ensures role-based information access (e.g., in an HR chatbot, responses differ based on who asks "who got promoted?") <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

### Model Selection and Optimization
*   **Starting Point**: Enterprises are advised to begin with large models and RAG solutions for proofs of concept (POCs) <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   **Optimization for Production**: For production systems, fine-tuning smaller models offers latency and cost advantages <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>.
*   **Custom Models**: Building custom pre-trained models makes sense for companies with large amounts of unique data, especially in regulated industries like healthcare, where full control over training data and understanding specialized language is crucial <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>, <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>.
*   **Brand vs. Capability**: A "somewhat surprising" pattern is that customers often select models based on brand recognition rather than actual capability <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
*   **Cost**: While LLM costs are a concern, they haven't been a major blocker for enterprise adoption yet, as most current use cases are internal, leading to non-massive volumes. Costs are also rapidly decreasing <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

### Evaluation and Observability
*   **Transition from POCs to Production**: Enterprises are slowly moving from POCs to production for internal productivity and analysis use cases, but external use cases still require more confidence <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **LLM Evaluation**: Evaluation of LLMs is still not mature <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>. Trulens, an acquired open-source observability and LLM evaluation platform, is critical for customers to evaluate systems at scale, often using LLMs as judges <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   **Guardrails**: Companies like Snowflake are building additional guardrails into models (e.g., Cortex Guard using Llama Guard) to manage unscripted responses and ensure brand and policy alignment in uncharted territory <a class="yt-timestamp" data-t="00:27:33">[00:27:33]</a>.

## Future Outlook

*   **Agents**: Agentic systems are an "uncharted new territory" with "super exciting" potential <a class="yt-timestamp" data-t="00:28:24">[00:28:24]</a>. While early, customers are beginning to implement them for specific use cases like BI workflows, where a system orchestrates multiple steps (SQL generation, evaluation, data retrieval, reasoning) <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
*   **Specialized Agents**: The vision includes "many small, specific agents" set by natural language to perform tasks on behalf of users, like checking websites regularly for unique needs <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>.
*   **Ecosystem Play**: Snowflake aims to enable a full ecosystem for customers by making it easy to use and share AI-ready data within the data platform <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>. This allows companies like Morgan Stanley to build chatbots that leverage existing data from the financial ecosystem (e.g., S&P, FactSet) with built-in governance and security <a class="yt-timestamp" data-t="00:35:07">[00:35:07]</a>.
*   **[[ai_applications_and_market_potential_across_various_industries | Application Space Maturing]]**: The market is transitioning from providing building blocks to demanding end-to-end products, with customer service being an obvious application area <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.
*   **Startups in [[integration_and_orchestration_of_ai_applications | AI Infrastructure]]**: Despite the convergence towards end-to-end platforms, there are still "massive" opportunities for startups across various aspects of the AI infrastructure stack, driven by ongoing innovation <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. The inference stack, in particular, continues to develop rapidly, translating directly to cost reductions <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>.
*   **Assistant Platforms**: The assistant space is challenging for startups because it needs to be a platform but cannot start as one. The key for startups is to "nail a couple of really deep use cases" rather than attempting many small ones <a class="yt-timestamp" data-t="00:43:41">[00:43:41]</a>. Examples include specialized "engineer" or "salesperson" agents <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.