---
title: Snowflakes AI strategy and products
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Baris Gencel, Head of AI at Snowflake, leads the company's extensive AI initiatives, including products like Cortex AI, the Data Cloud, and their large language model (LLM) Arctic [00:00:03]. Snowflake's work focuses on the infrastructure supporting AI tools in production, offering insights into common use cases and the effectiveness of techniques like fine-tuning and Retrieval-Augmented Generation (RAG) [00:00:15].

## Arctic LLM
Snowflake developed Arctic LLM to address specific customer needs, particularly in the realm of business intelligence (BI) [00:01:06]. The primary goal was to create an LLM exceptionally good at text-to-SQL generation and following instructions [00:01:14].

Key aspects of Arctic LLM:
*   **Development Timeline**: The effort began around December, with a relatively small team of researchers, and the model was built within three to four months [00:00:52].
*   **Enterprise Focus**: Arctic is designed for enterprise needs, excelling in SQL co-pilot functionalities and high-quality chatbots, rather than tasks like composing poetry [00:02:01].
*   **Efficiency**: The team developed an innovative architecture focused on efficiency in both training and inference, building the model at approximately 1/8th the cost of similar models [00:02:25]. This efficiency stems from an optimized data recipe and architecture [00:02:42].
*   **Future**: Arctic's goal is not to be a general-purpose model, but rather to focus on specific Snowflake customer needs, such as SQL generation and RAG quality [00:26:17].

## Snowflake Cortex
Cortex is Snowflake's managed service that runs various LLMs, including Arctic, [[Mistral AI and its competition with OpenAI | Mistral]], and Meta models [00:03:11].

### Key Product Offerings under Cortex:
1.  **AI for BI (Cortex Analyst)**: This product aims to enable users to interact with structured and semi-structured data using natural language [00:03:00].
    *   **Use Cases**: Generating SQL from natural language queries for BI, and extracting data from text for processing (e.g., analyzing sales call logs or customer support tickets) [00:03:00].
    *   **Challenges and Solutions**:
        *   **"Iceberg Problem"**: Demos are easy to build, but real-world data is messy, with potentially tens of thousands of tables and hundreds of thousands of columns with inconsistent naming conventions [00:04:30].
        *   **Quality**: Cortex Analyst is a complex system combining three to four LLMs to increase quality [00:05:05]. It knows when to ask for clarifications or abstain from answering questions it cannot confidently address [00:05:21].
        *   **Self-Healing Systems**: It includes systems that generate SQL, check its validity, and provide feedback loops for users to create "verified queries" [00:05:26].
        *   **Accuracy**: Achieves 90-95% quality in internal efforts, but human-in-the-loop systems are still necessary for critical BI data (e.g., CFO reports) [00:05:37].
        *   **Limitations**: Models struggle with complex joins, semantic understanding of unique company data models, hallucinating column names, and generating non-executable queries [00:06:39].
        *   **Product Choice**: Snowflake consciously focuses on precision, sacrificing recall, meaning the system will not answer all questions but will strive for high accuracy on those it does [00:07:55].
2.  **AI for Unstructured Data (Cortex Search)**: Focuses on enabling chatbots for unstructured data like documents and PDFs [00:03:32].
    *   **Core Component**: Features their own embedding model, Arctic Embed, which is state-of-the-art, highly efficient (one-quarter the size of OpenAI's embedding model), and offers higher benchmark scores [00:11:00].
    *   **Hybrid Search**: Cortex Search employs a hybrid approach, combining vector search with lexical keyword search to reduce hallucinations [00:12:14].
    *   **Use Cases**: External RAG applications (focusing on quality, reduced hallucinations), internal productivity tools, and enterprise search (e.g., upgrading existing search stacks) [00:11:58].
3.  **Natural Language for Data Extraction**: Utilizing natural language to extract and process data from text in batch [00:03:48].
    *   **Example**: Summarizing open-ended employee survey responses, categorizing feedback, and providing example quotes [00:09:07].
    *   **Ease of Use**: Snowflake focuses on providing task-specific functions that simplify the process, reducing the need for extensive prompt engineering or data pipeline work [00:09:55].

## AI Deployment and Strategy
[[Challenges and strategies in AI deployment | Deploying AI]] within enterprises involves several considerations:
*   **Governance and Trust**: Large companies have AI governance boards that prioritize data security, governance, and policy adherence [00:13:10]. Snowflake's built-in granular access controls are a significant advantage, ensuring that AI systems respect existing data permissions (e.g., HR chatbots providing different answers based on user roles and preventing data leakage) [00:17:02].
*   **Evaluation and Observability**: Snowflake acquired TruEra, which includes the open-source TruLens product, an LLM evaluation and observability platform [00:14:06]. This helps customers evaluate AI systems at scale, often using LLMs as judges [00:14:51]. This is crucial for transitioning from Proof-of-Concepts (POCs) to production [00:15:00].
*   **Model Selection**: Snowflake recommends starting with large models combined with RAG for POCs [00:19:23]. For production, fine-tuning smaller models for latency and cost advantages is often the next step [00:19:36]. Custom models make sense for companies with unique, large datasets or those in regulated industries (e.g., healthcare) who need full control over the training data [00:19:51].
    *   **Inference vs. Training**: Most customers primarily focus on inference due to the high capabilities of existing models [00:20:53]. Snowflake simplifies fine-tuning and offers support for training custom models for a smaller number of customers [00:21:06].
    *   **Brand Influence**: Currently, model selection is often influenced by brand recognition rather than solely on capability [00:21:36].
*   **Cost**: While enterprises are aware of the cost of LLMs, it hasn't been a significant blocker for current internal productivity-focused use cases, as volumes are not massive and costs are rapidly decreasing [00:25:08].
*   **[[AI integration and product development strategies | Product Innovation]]**: More product innovation is needed to make end-users comfortable with AI answers that may not always be correct, including mechanisms to check accuracy [00:15:47]. Hallucinations remain a concern, especially in regulated industries [00:16:06].

## Internal AI Use Cases at Snowflake
Snowflake leverages LLMs internally across various teams [00:30:20]:
*   **Sales**: Summarizing sales conversations to understand win/loss reasons [00:30:27].
*   **Employee Assistants**: Chatbots for querying internal data and documents [00:30:41].
*   **Documentation**: General chatbot use cases for documentation [00:30:52].
*   **Platform Optimization**: Integrating AI for SQL engine optimization and enhancing the Marketplace [00:31:14].

## Competitive Landscape
When comparing its AI strategy to DataBricks, Snowflake emphasizes its "single product" ethos, where everything is deeply integrated and easy to use [00:31:37]. Snowflake Cortex, including Cortex Analyst and Cortex Search, offers high-quality systems that sit alongside data, leveraging Snowflake's built-in governance tools [00:32:04]. While visions for an end-to-end platform might be similar, the approaches differ, with Snowflake notably integrating AI into SQL from the outset [00:32:45].

## Opportunities for Startups
The market for AI infrastructure is massive and growing, with significant opportunities for startups at various points of the stack [00:33:33]. While end-to-end platforms offer value, constant innovation in the AI stack ensures that new opportunities for startups will continue to emerge [00:34:02]. The inference stack, in particular, is still rapidly developing, with improvements directly translating to cost reductions [00:35:52].

## Future of AI at Snowflake
Snowflake is excited about enabling agents to plug into its system, allowing natural language interaction with both unstructured and structured data [00:34:27]. A key opportunity is leveraging Snowflake's Data Cloud to create an ecosystem where companies can easily build AI applications on shared, AI-ready data, such as financial data from S&P or FactSet [00:34:44].

## Quick Fire Round Insights
*   **Underhyped**: LLM Evaluation [00:40:43].
*   **Overhyped (in the short term)**: Agents, though they are expected to match the hype in the future [00:40:49].
*   **Biggest Surprise**: The profound challenge and informative process of defining the exact problem to solve in text-to-SQL [00:41:20].
*   **Open Source vs. Closed Source**: Companies like Meta and [[Mistral AI and its competition with OpenAI | Mistral]] have been influential in promoting open-source models, fostering a flexible ecosystem where developers can build innovative applications [00:42:11].
*   **Excited AI Startup**: [[Mistral AI and its competition with OpenAI | Mistral]], for its small, capable team building amazing models rapidly and effectively creating market awareness [00:42:56].
*   **Ideal AI Application to Build**: Something in the "assistance" space, focusing on nailing a couple of deep, specific use cases rather than trying to be a broad platform from the start [00:43:22]. Examples include specialized agents for engineering (like Devin) or sales [00:44:06].
*   **Most Interesting Company to Run AI (outside Snowflake)**: Platform companies, as they have the opportunity to build out capabilities into full platforms [00:44:47]. The application space is still forming, with a growing demand for end-to-end products [00:45:22].

To learn more about Snowflake's AI efforts, visit their AI website or watch videos from their recent Summit event on YouTube [00:46:06].