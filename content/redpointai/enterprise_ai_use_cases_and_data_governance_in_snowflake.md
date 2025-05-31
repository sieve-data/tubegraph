---
title: Enterprise AI use cases and data governance in Snowflake
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Baris Gekken, Snowflake's Head of AI, oversees the company's extensive AI initiatives, including products like Cortex and the Arctic LLM, as well as the data cloud [00:00:03]. His insights highlight the infrastructure supporting AI tools in production, common use cases, and commentary on practices like fine-tuning and Retrieval Augmented Generation (RAG) [00:00:15]. Snowflake's goal is not to build a fully general-purpose model, but to focus on specific needs of its customers, such as SQL generation and RAG quality [00:26:17].

## Snowflake's AI Product Portfolio

Snowflake offers a broad AI product portfolio [00:36:00]. At its core is Cortex, their inference engine that runs various large language models (LLMs), including Snowflake's own Arctic and models from Mistral and Meta [00:10:29].

### Arctic LLM
Snowflake began developing Arctic LLM around December, driven by customer demand for business intelligence (BI) experiences using AI, particularly in text-to-SQL and natural language to SQL capabilities [00:00:59]. A relatively small team of researchers, including founders from DeepSpeed and vLLM, built the model in three to four months [00:01:37]. Arctic is specifically designed for enterprise needs, excelling in SQL co-pilot and high-quality chatbot functions, rather than tasks like composing poetry [00:01:59].

Its architecture focuses on efficiency, making it very efficient for both training and inference, reportedly built at 1/8th the cost of similar models [00:02:27]. This efficiency is crucial as the market pushes for cost reduction by distilling large models into smaller, effective ones [00:11:31].

### Cortex and its Applications
Cortex provides a managed service for running LLMs [00:03:11]. Customers typically use it for three main purposes:
1.  **AI for BI:** Such as text-to-SQL use cases [00:03:27].
2.  **Chatbots:** For interacting with unstructured data like documents and PDFs [00:03:32].
3.  **Data Extraction and Text Analytics:** Processing structured and semi-structured data from text, like sales call logs or customer support tickets, in batch [00:03:42].

#### Cortex Analyst (AI for BI)
This product, an [[strategic_uses_of_ai_in_enterprises | AI for BI]] solution, addresses the "Iceberg problem" where demos are easy but real-world data is messy, involving tens of thousands of tables and hundreds of thousands of columns with complex names [00:04:27]. Cortex Analyst combines multiple LLMs working together [00:05:12]. It is designed to know when to ask for clarifications, when not to answer, and includes self-healing systems for generating and validating SQL [00:05:19].

While achieving 90-95% quality in internal efforts, direct application for critical business decisions like CFO revenue reports still requires caution [00:05:37]. Therefore, Snowflake is building in human-in-the-loop systems and features like "verified queries" to increase confidence [00:05:53].

Challenges in the BI space include:
*   Getting complex joins right across unique company data models [00:06:39].
*   Semantic understanding of the data space [00:06:52].
*   Hallucinations regarding column names [00:07:03].
*   Generating non-executable queries [00:07:11].

Snowflake has made a conscious product choice to prioritize precision over recall, meaning it will not answer all questions but will know when to ask for clarification or abstain [00:07:55]. This approach is crucial for business users who cannot tolerate incorrect answers, unlike analysts who might explore and correct [00:08:26].

#### Cortex Search
Cortex Search focuses on high-quality search, essential for RAG applications [00:10:39]. It uses Snowflake's own embedding model, Arctic Embed, which is state-of-the-art, efficient, and a quarter the size of OpenAI's embedding model while maintaining higher benchmark scores [00:10:58]. Cortex Search is a hybrid system combining vector search and lexical keyword search to reduce hallucinations [00:12:14].

Use cases for Cortex Search include:
*   External RAG applications, where quality and hallucination reduction are key [00:12:02].
*   Internal RAG applications for increased productivity with lower hallucination risk [00:12:23].
*   Upgrading regular [[enterprise_adoption_and_use_cases_for_ai | enterprise search]] [00:12:33].

#### Data Extraction
In data extraction, LLMs are performing well [00:08:48]. Use cases include summarizing open-ended employee survey questions, categorizing them, and providing example quotes, a task that previously took hours [00:09:07]. Snowflake aims to make these processes simple for customers by providing task-specific functions that minimize prompting and data pipeline work [00:09:55].

## [[Enterprise ai adoption challenges and solutions | Enterprise AI Adoption Challenges and Solutions]]

### Trust and Data Governance
A primary challenge for large companies is gaining comfort with the chosen AI platform, especially concerning data security, governance, and policy adherence [00:13:10]. Snowflake emphasizes its built-in, granular access controls as a core advantage, allowing precise management of data access for AI systems [00:16:57]. An example given is an HR chatbot providing different promotion information based on the user's access rights, requiring no data leakage or hallucination [00:17:11]. For AI, this means deep integration of access controls into search systems to filter documents based on user permissions, and leveraging existing controls for data access in queries [00:18:21].

### LLM Evaluation
The acquisition of TruEra, and its open-source product Trulens, addresses the challenge of LLM evaluation and observability [00:14:06]. Trulens allows customers to build systems and evaluate their performance at scale, often using LLMs as judges [00:14:20].

### Transition from POCs to Production
While internal and productivity-focused use cases are transitioning from Proof of Concepts (POCs) to production, external use cases still require more confidence due to hallucination risks, especially in regulated industries where consequences can be catastrophic [00:15:07]. Widespread internal deployments require both increased user comfort with the technology and product innovations to help end-users cope with potentially incorrect answers and mechanisms to check them [00:15:40].

### Cost
Though everyone is aware that LLMs can be costly, it hasn't been a major blocker for enterprise adoption yet [00:25:20]. This is partly because current production use cases, primarily internal, do not involve massive volumes, and LLM costs have been decreasing rapidly [00:25:39].

### Hallucination and Measurement
Hallucinations remain a concern [00:28:05]. Furthermore, the measurement of AI system quality is still not mature for many companies, especially in complex scenarios like text-to-SQL [00:28:11].

## [[Enterprise ai deployment models | Enterprise AI Deployment Models]]

### Off-the-Shelf, Fine-Tuning, and Custom Models
Snowflake recommends that enterprises start with large models combined with RAG solutions for initial POCs [00:19:23]. Once a system is stable, optimization for production often involves fine-tuning a smaller model to gain latency and cost advantages [00:19:36].

[[building_custom_ai_models_for_enterprises | Building custom AI models]] makes sense for companies with large amounts of unique data, particularly in regulated industries like healthcare, where full control over training data and understanding specialized language is critical [00:19:51]. Snowflake supports fine-tuning and works with a small number of customers interested in pre-training their own models [00:21:06].

### LLM Ecosystem and Model Selection
Snowflake supports a range of models, including Mistral, Meta, and AI21 [00:29:38]. Model selection is often influenced by brand recognition rather than solely capability [00:21:36]. The vLLM team's presence at Snowflake helps in quickly supporting new models and optimizing the inference stack, especially for large models and multi-node inference [00:22:35]. The availability of capable open-source models like Meta's Llama and Mistral has fostered a more flexible ecosystem beyond just a few players [00:42:11].

## [[Strategic uses of AI in enterprises | Strategic Uses of AI Internally at Snowflake]]
Snowflake itself uses LLMs across various internal teams:
*   **Sales:** Summarizing sales conversations to understand win/loss reasons [00:30:27].
*   **Employee Assistants:** Chatbots for internal data and documents [00:30:41].
*   **Documentation:** General chatbot applications [00:30:52].
*   **Product Development:** Incorporating AI into core products, such as SQL engine optimization and Marketplace capabilities [00:31:07].

## Future of AI
Baris Gekken is excited about enabling natural language interaction with structured and unstructured data, and integrating agents into the Snowflake system [00:34:21]. Snowflake's position as a data platform allows for seamless data sharing and the creation of AI-ready data, enabling companies to build chatbots that leverage the entire ecosystem [00:34:46].

The inference stack in AI infrastructure continues to evolve rapidly, leading to significant cost reductions [00:35:52]. While there will be long-term businesses in the inference space, success will likely be concentrated among a few scale players [00:36:10].

Gekken believes the assistant space, where LLMs can call APIs to take action, is becoming incredibly powerful, moving beyond handcrafted use cases to more general-purpose utility [00:37:15]. He envisions a future with many small, specific agents easily created by users via natural language to perform unique tasks on their behalf, such as checking websites for specific information [00:38:29]. Agentic systems are beginning to emerge, particularly in BI workflows where models figure out when to generate, evaluate, and run SQL [00:39:17].

## Quick-Fire Round Insights
*   **Underhyped:** Evaluation of AI systems [00:40:43].
*   **Overhyped (short-term):** Agents, though they are expected to match the hype in the long run [00:40:49].
*   **Biggest Surprise in Building Snowflake AI:** The complexity of text-to-SQL and finding the exact problem to solve, reinforcing the classic machine learning challenge of problem definition [00:41:19].
*   **Most Exciting AI Startup (outside Snowflake's space):** Model startups like Mistral, for their capable teams, rapid innovation, and market awareness [00:42:52].
*   **AI Application to Build:** Something in the assistance space, focusing on nailing a couple of really deep use cases rather than many small ones [00:43:20].
*   **Most Interesting Company to Run AI Now (Platform):** Large platform companies have the opportunity to build platforms, while the application space for startups is just forming and will see more end-to-end solutions emerge in the next two years [00:44:52].