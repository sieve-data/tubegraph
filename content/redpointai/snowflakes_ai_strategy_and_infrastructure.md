---
title: Snowflakes AI strategy and infrastructure
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Snowflake's head of AI, Baris Gocken, leads the company's extensive AI initiatives, including products like Cortex AI, Data Cloud, and the proprietary LLM Arctic <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Snowflake's focus is on building the core [[evolution_of_ai_models_and_infrastructure | infrastructure]] that supports AI tools in production <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Snowflake's AI Product Portfolio

Snowflake offers a broad AI product portfolio designed to support various [[enterprise_ai_use_cases_and_data_governance_in_snowflake | enterprise AI use cases]] <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Cortex

Cortex is Snowflake's core inference engine and managed service for running Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. It supports Snowflake's own Arctic LLM, as well as models from providers like Mistral and Meta <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

### [[development_and_deployment_of_snowflakes_arctic_llm | Arctic LLM]]

Arctic is Snowflake's own open-source LLM, specifically designed for [[enterprise_ai_use_cases_and_data_governance_in_snowflake | enterprise needs]] <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Development**: The development began around December, driven by customer demand for BI-type experiences using AI, particularly text-to-SQL functionality <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. It was developed by a relatively small team of researchers, including founders from DeepSpeed and vLLM, in approximately three to four months <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Optimization**: Arctic features an innovative, efficient architecture, making it highly efficient for both training and inference. It was built at roughly 1/8 the cost of similar models <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. A significant effort was also placed on refining the "data recipe" to ensure optimal performance <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Purpose**: While capable of general tasks, Arctic is optimized for SQL co-piloting and high-quality chatbot functionality, rather than being a general-purpose model like GPT-5 <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
*   **Usage**: Customers leverage Arctic for various use cases, including AI for BI, building chatbots for unstructured data (documents, PDFs), and extracting data from semi-structured text like sales call logs and customer support tickets <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Cortex Analyst

Cortex Analyst is Snowflake's BI product, designed to answer business intelligence questions through natural language <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **System Design**: It is a complex system combining three to four LLMs working in concert <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. It's built with "self-healing" mechanisms, including generating SQL, checking its validity, and knowing when to ask for clarifications or abstain from answering <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Quality**: While achieving 90-95% quality in internal efforts, it's not yet fully reliable for critical financial reports, necessitating "human-in-the-loop" systems for validation <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. It also incorporates a feedback loop allowing customers to create "verified queries" to increase confidence <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **[[challenges_and_strategies_in_enterprise_ai_deployment | Challenges]]**: The primary difficulty lies in accurately handling complex SQL joins, particularly with large, messy real-world datasets containing tens of thousands of tables and hundreds of thousands of ambiguously named columns <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. LLMs may hallucinate column names, get joins wrong, or generate unexecutable queries <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Snowflake consciously prioritizes precision over recall, choosing not to answer all questions to maintain high quality <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Cortex Search

Cortex Search focuses on high-quality search capabilities, crucial for Retrieval Augmented Generation (RAG) applications <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
*   **Arctic Embed**: Snowflake's proprietary embedding model, Arctic Embed, is state-of-the-art, a quarter the size of OpenAI's embedding model, yet achieves higher benchmark scores <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Hybrid Search**: Cortex Search employs a hybrid approach, combining vector search with lexical keyword search to reduce hallucinations <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Use Cases**: It supports external RAG applications, internal productivity tools, and modernizing traditional [[enterprise_ai_use_cases_and_data_governance_in_snowflake | enterprise search]] <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

## Enterprise AI Adoption and Governance

Snowflake's strategy leverages its existing data platform to facilitate AI adoption by focusing on data governance, security, and integrated solutions <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### Data Governance and Security

A major advantage for Snowflake is its established data governance framework <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. All Snowflake models run within the Snowflake cloud, right next to the data, ensuring security and compliance <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
*   **Granular Access Controls**: Snowflake's platform is built with granular access controls from the ground up <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This means AI systems, including search, automatically respect existing data permissions, preventing data leakage and ensuring appropriate responses based on user roles (e.g., an HR chatbot providing different answers based on the inquirer's access) <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. Many customers spend years establishing their data governance, which now directly benefits their AI deployments <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
*   **Cortex Guard**: Using underlying technologies like Llama Guard, Cortex Guard provides an additional layer of security, addressing concerns around unscripted LLM responses and ensuring alignment with company policies and brand <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

### Transition to Production

While many [[enterprise_ai_use_cases_and_data_governance_in_snowflake | enterprise AI use cases]] are still in the Proof of Concept (POC) phase, there is a clear transition to production for internal productivity and analysis applications <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. Widespread external deployments require more confidence, product innovation (e.g., mechanisms for users to check answers), and further technological advancements to mitigate risks like hallucination, especially in regulated industries <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Model Selection and Optimization

Snowflake advises customers to [[starting_small_in_ai_projects | start small]] with large off-the-shelf models combined with RAG solutions for initial POCs <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   **Fine-tuning**: For production systems, fine-tuning smaller models is recommended for latency and cost advantages <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. Snowflake makes fine-tuning simple <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   **Custom Models**: For companies with large, unique datasets, particularly in regulated industries (e.g., healthcare with specialized language), building custom pre-trained models makes sense <a class="yt-timestamp" data-t="00:19:49">[00:19:49]</a>. Snowflake supports customers in this process, leveraging its efficient Arctic development approach <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   **Model Popularity**: Customers often select models based on brand recognition rather than solely on capability, though this is changing with better evaluation frameworks becoming available <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
*   **Cost**: While LLMs can be expensive, the rapid decline in costs and the internal-focused nature of current high-volume [[enterprise_ai_use_cases and data governance in snowflake | enterprise AI use cases]] mean cost is not yet a significant blocker for production deployment <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.

## Infrastructure and Acquisitions

Snowflake's AI infrastructure is bolstered by strategic acquisitions and an emphasis on efficient model deployment.

### vLLM Integration

Snowflake benefits from having the founders of the vLLM team as employees, which allows for robust support for new models <a class="yt-timestamp" data-t="00:22:36">[00:22:36]</a>. They continuously optimize the inference stack for efficiency, including multi-node inference and fine-tuning, and upstream these upgrades to vLLM <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>. This ensures that new, large models like Llama 3.1 405B can run efficiently <a class="yt-timestamp" data-t="00:22:56">[00:22:56]</a>.

### Strategic Acquisitions

*   **TruEra**: Snowflake acquired TruEra, which provides the open-source Trulens platform for LLM evaluation and observability <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This acquisition is crucial for customers to evaluate and monitor their AI systems at scale, especially as they move from POCs to production <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Neva**: The acquisition of Neva was instrumental, bringing in Snowflake's CEO and contributing core technology to Cortex Search and its underlying embedding model <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.

## Future of AI at Snowflake

Snowflake aims to be a leading AI platform, enabling users to interact with both structured and unstructured data using natural language <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>.
*   **Agents**: Snowflake plans to enable agents to plug into the system, recognizing the emerging importance of agentic systems for complex workflows like BI analysis <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>, <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
*   **Ecosystem Play**: Leveraging its "Data Cloud" model, Snowflake makes it easy for customers to integrate and build AI applications on existing data, including third-party datasets from the financial ecosystem, ensuring governance and security <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.
*   **Partnerships**: Snowflake partners with model providers (e.g., Mistral, Reka, AI21) and companies offering end-to-end solutions (e.g., Landing AI) to allow applications to run securely within the Snowflake environment, accessing data directly without needing to move it <a class="yt-timestamp" data-t="00:29:33">[00:29:33]</a>.
*   **Internal Use**: Snowflake extensively uses LLMs internally for sales call summaries, employee assistants querying internal documents, and optimizing its SQL engine and Marketplace <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>.

## Comparison with Databricks

Snowflake differentiates itself by its "single product" ethos, aiming for highly integrated and easy-to-use AI functionalities <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. Snowflake notably integrated AI into SQL from the outset with Cortex <a class="yt-timestamp" data-t="00:32:49">[00:32:49]</a>. High quality systems like Cortex Analyst and Cortex Search, along with a strong governance foundation, are key differentiators <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

## Opportunities in AI Infrastructure

While end-to-end platforms are growing in importance, there remain significant opportunities for startups in various aspects of the AI [[evolution_of_ai_models_and_infrastructure | infrastructure]] stack due to the market's massive growth and ongoing innovation <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. The inference stack, in particular, continues to see rapid advancements leading to cost reductions <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>. There is a shift towards customers wanting full end-to-end products rather than just building blocks <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>.

## Baris Gocken's Insights

*   **Underhyped/Overhyped**: Evaluation is currently underhyped, while agents are overhyped in the short term, though they are expected to match the hype in the future <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>.
*   **Biggest Surprise**: The core challenge of defining the exact problem to solve in text-to-SQL proved to be a critical and informative process <a class="yt-timestamp" data-t="00:41:20">[00:41:20]</a>.
*   **Open vs. Closed Source**: Open-source models, particularly from Meta and Mistral, have been highly influential in fostering a diverse ecosystem and providing flexibility for innovation <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>.
*   **Exciting AI Startup**: Baris is most excited about model startups like Mistral, noting their small, capable teams, rapid development, and effective awareness creation <a class="yt-timestamp" data-t="00:42:49">[00:42:49]</a>.
*   **Personal Application Interest**: Baris would build an AI application in the assistance space, focusing on "many small, specific agents" that act on users' behalf for unique tasks, rather than broad, general-purpose assistants <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. This requires nailing a few deep use cases rather than many small ones <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>.
*   **Interesting Platform**: Platform companies generally present compelling opportunities in AI, as current capabilities are awaiting true platformization <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.