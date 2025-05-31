---
title: Challenges and innovations in SQL generation and BI applications
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 
Baris Gokkekan, Snowflake's Head of AI, leads the company's extensive AI initiatives, including products like Cortex AI, their data cloud, and their own Large Language Model (LLM) named Arctic <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Gokkekan's work focuses on the infrastructure supporting AI tools in production, offering insights into common use cases and the effectiveness of techniques like fine-tuning and Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

### Arctic LLM: Tailored for Enterprise BI

Snowflake decided to build its own LLM, Arctic, primarily because many customers sought to develop Business Intelligence (BI) type experiences using AI <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. A key need was for text-to-SQL capabilities, converting natural language into SQL queries to interact with data effectively <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. While existing models were good, they often struggled with the complexities of SQL <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

Arctic was developed by a relatively small team, including researchers from DeepSpeed and vLLM, in approximately three to four months <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. It was designed specifically for enterprise needs, excelling at SQL co-pilot functionalities and high-quality chatbots, rather than general tasks like composing poetry <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. This optimization was achieved through an innovative, efficient architecture for both training and inference, allowing the model to be built at one-eighth the cost of similar models, and a meticulously crafted "data recipe" <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

### Snowflake Cortex AI and Key Use Cases

Snowflake Cortex is a managed service that hosts various LLMs, including Arctic, as well as models from Mistral and Meta <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. It supports three primary use cases:
*   **AI for BI**: Generating SQL queries from natural language <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
*   **Chatbots for Unstructured Data**: Building chatbots to interact with documents and PDFs <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   **Data Extraction and NLP**: Using natural language to extract and process data from semi-structured text like sales call logs or customer support tickets <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.

### [[Challenges in AI Adoption and Deployment|Challenges in SQL Generation and BI Applications]]

Generating SQL from natural language is particularly challenging, described as an "Iceberg problem" where demos are easy but real-world implementation is messy <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. Key challenges include:
*   **Complex Data Environments**: Enterprise data often involves tens of thousands of tables and hundreds of thousands of columns with inconsistent or "weird names" (e.g., "rev one," "rev two" for revenue) <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Accuracy of Complex Joins**: LLMs struggle to correctly identify and implement complex joins, which are unique to each company's data model <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Semantic understanding of these unique data spaces is a significant hurdle <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
*   **Hallucinations and Errors**: Models may hallucinate column names, get joins wrong, or generate non-executable queries <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>. LLMs are prone to providing answers even when they shouldn't, leading to potential inaccuracies <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
*   **Trust in Critical Applications**: For BI use cases, especially financial reporting, a 90-95% accuracy rate may not be sufficient for a CFO to fully trust the results <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
*   **Defining the Problem**: The classic machine learning challenge of defining the problem and what "good" looks like remains critical in the LLM world <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

### Innovations and Solutions in BI

To address these challenges, Snowflake has developed several innovations within Cortex:
*   **Cortex Analyst**: This product is a sophisticated system that orchestrates multiple LLMs (three to four) to answer BI questions <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.
*   **Self-Healing Systems**: The system generates SQL, checks its validity, and knows when to ask for clarifications or abstain from answering questions it cannot confidently resolve <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>.
*   **Human-in-the-Loop and Verified Queries**: To ensure high quality, particularly for critical BI, systems incorporate human oversight. Customers can create "verified queries" which the system can then prioritize, increasing confidence in the results <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
*   **Precision Over Recall**: Snowflake consciously prioritizes precision in its BI applications, choosing not to answer all questions but instead focusing on accuracy and knowing when to seek clarification or decline to answer <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>. This approach tailors the experience for business users who require high quality, unlike analysts who might accept less precise results for exploration <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

For data extraction, things are "pretty good" <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>. An example includes summarizing open-ended employee survey responses, categorizing them, and providing example quotes, a task that previously took hours <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. Snowflake aims to make these processes very simple and easy to use, building task-specific functions that minimize the need for complex prompting or data pipeline work by customers <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.

### [[Enterprise AI use cases and data governance in Snowflake|Data Governance and AI in Snowflake]]

A significant advantage for Snowflake is its inherent data governance capabilities <a class="yt-timestamp" data-t="13:09:00">[13:09:00]</a>. For enterprises, the first step in AI adoption is often ensuring comfort with the platform's security and data governance policies <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. Snowflake's models run directly within the platform, right next to the customer's data, offering a strong value proposition <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>.

Snowflake's granular access controls, built from the ground up, are crucial <a class="yt-timestamp" data-t="17:02:00">[17:02:00]</a>. For example, in an HR chatbot, different users receive different answers based on their access permissions, preventing data leakage and ensuring accuracy <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>. This pre-existing data governance infrastructure is a huge benefit for customers building AI applications <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.

### [[Challenges and opportunities in AI development|AI Evaluation and Production Readiness]]

Transitioning from Proof of Concepts (POCs) to production systems is a current focus for enterprises <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. Snowflake acquired TruEra, an open-source LLM evaluation and observability platform (TruLens), to help customers assess and improve their AI systems at scale <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.

While internal productivity use cases are seeing slower transitions to production, external-facing applications still require more confidence due to risks like hallucination, especially in regulated industries <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>. Future product innovations are needed to make end-users more comfortable with AI answers that might not always be right, and to provide mechanisms for checking validity <a class="yt-timestamp" data-t="15:49:00">[15:49:00]</a>.

Regarding costs, while everyone is aware that LLMs are expensive, they haven't been a major blocker yet for internal use cases, as volumes aren't massive and costs are rapidly decreasing <a class="yt-timestamp" data-t="25:20:00">[25:20:00]</a>.

### Future of AI at Snowflake

Snowflake's goal with Arctic is not to build a general-purpose model like GPT-5, but rather to continue focusing on specific needs of Snowflake customers, such as SQL generation and RAG quality <a class="yt-timestamp" data-t="26:17:00">[26:17:00]</a>. They also offer flexible options for customers to fine-tune existing models or even train their own custom models, particularly for regulated industries with unique datasets <a class="yt-timestamp" data-t="20:07:00">[20:07:00]</a>.

A future area of excitement is enabling agents to plug into the system, leveraging Snowflake's data platform to allow customers, like asset managers, to easily build chatbots that connect to vast financial ecosystems (e.g., S&P, FactSet data) <a class="yt-timestamp" data-t="34:41:00">[34:41:00]</a>. This emphasizes the value of having data already consolidated within Snowflake, complete with governance and security guarantees <a class="yt-timestamp" data-t="35:36:00">[35:36:00]</a>.