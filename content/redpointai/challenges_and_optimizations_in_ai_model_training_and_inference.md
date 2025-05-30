---
title: Challenges and optimizations in AI model training and inference
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Baris Gekken, Head of AI at Snowflake, leads the company's extensive AI initiatives, including products like Cortex AI, the Data Cloud, and their own LLM, Arctic. His work focuses on the infrastructure that supports AI tools in production, offering unique insights into common use cases and effective strategies for AI deployment <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Snowflake's AI Offerings

Snowflake's AI product portfolio is broad, with a core focus on enabling customers to leverage AI directly on their data.

### Arctic LLM
Snowflake developed its own large language model, Arctic, specifically for enterprise needs <a class="yt-0timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Purpose**: Primarily designed for generating SQL (text-to-SQL) and following instructions, enabling business intelligence (BI) type experiences <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. It excels in SQL capabilities where other models might struggle with complexities <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Development**: Built by a relatively small team in about three to four months, starting around December <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Key researchers from DeepSpeed and vLLM contributed to its development <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Optimizations**: Arctic's architecture is highly efficient for both training and inference, costing 1/8 of similar models <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. A significant amount of time was spent on perfecting the "data recipe" to ensure high-quality output <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Cortex AI
Cortex is Snowflake's managed service that allows customers to run various large language models, including Arctic, Mistral, and Meta models <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Customers typically use Cortex for three main purposes <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>:
1.  **AI for BI**: Text-to-SQL generation for business intelligence <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
2.  **Chatbots**: Building chatbots to interact with unstructured data like documents and PDFs <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
3.  **Data Extraction & NLP**: Using natural language to extract and process data from text (structured and semi-structured), such as sales call logs, customer support tickets, and other text analytics <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This often involves batch processing <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Specific Cortex Products
*   **Cortex Search**: A hybrid search system combining vector search and lexical keyword search, crucial for Retrieval-Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. It emphasizes quality to reduce hallucinations <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
    *   **Arctic Embed**: Snowflake's proprietary embedding model, which is state-of-the-art, highly efficient (one-quarter the size of OpenAI's embedding model), and achieves higher benchmark scores than competitors <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Cortex Analyst**: A BI product designed to answer complex BI questions using a combination of three to four LLMs working together <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. It can ask for clarifications and self-heal by generating and validating SQL <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## [[Challenges and strategies in AI model development | Challenges in AI Model Development]] and Optimizations

### Challenges in AI for BI (SQL Generation)
The BI use case is considered the "Iceberg problem" due to its deceptive simplicity in demos versus real-world complexity <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Messy Real-World Data**: Enterprises often have tens of thousands of tables and hundreds of thousands of columns with inconsistent or ambiguous naming conventions (e.g., "rev one," "rev two" for revenue) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Complex Joins and Semantic Understanding**: The hardest part is correctly handling complex database joins and achieving semantic understanding of a company's unique data model <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Hallucinations and Errors**: Models can hallucinate column names, generate incorrect joins, or produce queries that won't execute <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. LLMs will often provide an answer even when they shouldn't <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   **Trust and Accuracy**: While quality can reach 90-95%, it's not yet sufficient for critical business decisions like a CFO trusting revenue numbers without human oversight <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Optimizations for AI for BI
*   **Multi-LLM Systems**: Stitching together a series of systems, including multiple LLMs, to increase overall quality <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Precision over Recall**: Consciously focusing on precision, meaning the system knows when *not* to answer a question or when to ask for clarification, rather than trying to answer everything and risking inaccuracies <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This is especially important for business users who cannot tolerate frequent errors <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Human-in-the-Loop**: Incorporating human oversight and feedback loops, allowing customers to create "verified queries" to increase confidence <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Data Extraction Use Cases
This area is performing "pretty good" <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Summarization**: Effectively summarizes large open-ended datasets, such as employee surveys or call logs, providing categories, examples, and quotes <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. This can reduce hours of manual work to a simple prompt <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Ease of Use**: Snowflake focuses on making these processes simple for customers by building task-specific functions that reduce the need for extensive prompting and data pipeline work <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### Search and RAG Applications
*   **Hybrid Search**: Combining vector search and lexical keyword search helps reduce hallucinations <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Use Cases**:
    *   **External RAG**: Focus on quality, reduced hallucinations, and knowing when to abstain from answering <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   **Internal Productivity**: Most common use case, offering increased productivity with lower hallucination risk <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
    *   **Enterprise Search**: Upgrading existing enterprise search stacks <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

## [[Challenges and strategies in AI model evaluation | Challenges in AI Model Evaluation]] and Deployment

### Data Governance and Security
A major advantage for Snowflake is running AI systems right next to customer data, ensuring data security and governance <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   **Trust and Policy**: Enterprises have AI governance boards that prioritize a platform's comfort, data security, governance, and policy adherence <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.
*   **Granular Access Controls**: Snowflake has built-in, granular access controls for database objects, which are deeply integrated into AI features like search. This ensures that users only access documents or data they are permitted to see, preventing data leakage (e.g., an HR chatbot providing different answers based on user permissions) <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
*   **Production Readiness**: The move from Proof-of-Concepts (POCs) to production systems, especially for internal productivity and analysis, is increasing. For external use cases, more confidence is still needed <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Timeline for Widespread Internal Deployment**: Requires both increased comfort with the technology and product innovations to help end-users manage when answers might not be perfectly right, along with mechanisms to check accuracy. Hallucination risks remain, especially in regulated industries <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.

### Model Selection and Customization
*   **Brand over Capability**: Customers often select models based on brand recognition rather than their actual capabilities, even when less recognized models are highly capable <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>.
*   **Deployment Strategy**:
    1.  **Start with Large Models + RAG**: Recommended for initial POCs, as this combination usually goes "quite far" <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
    2.  **Fine-tuning Smaller Models**: For production systems, fine-tuning smaller models offers latency and cost advantages <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. Snowflake makes fine-tuning simple <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
    3.  **Custom Pre-trained Models**: Makes sense for companies with large, unique datasets, especially in regulated industries (e.g., healthcare) where full control over training data and specific language understanding are critical <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. Arctic's efficient build process makes building custom models more feasible <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

### [[Challenges in AI model training and deployment | Inference Challenges]] and Optimizations
*   **Cost**: While LLMs are known to be expensive, the rapid decrease in costs due to distillation into smaller, more efficient models means it's not a major blocker for most current internal, lower-volume use cases <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
*   **Supporting New Models**: Snowflake benefits from having founders of the vLLM team as employees, which helps in ensuring their inference stack supports new models efficiently. Optimizations, like multi-node inference, are built into vLLM and upstreamed to the project <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **LLaMA 3.1 405B**: A very capable large model, useful for fine-tuning or distilling other models, and for synthetic data generation <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>. Its broad availability provides significant advantages to the ecosystem <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.

### [[Challenges and strategies in AI model evaluation | Evaluation and Observability]]
*   **Truera Acquisition**: Snowflake acquired Truera, which includes the open-source product Trulens, an observability and LLM evaluation platform <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>. This is crucial for customers to evaluate system performance at scale, using LLMs as judges <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. This addresses a core need for production systems, moving beyond simple POCs <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Missing Pieces**: Hallucinations remain a concern. Measurement tools for LLM quality are still not mature, especially for complex scenarios like text-to-SQL. The emergence of agentic systems introduces new, uncharted territory <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>.

## Future Outlook and Market Dynamics

### The Rise of Agents
*   **Individualized Assistants**: The long-term vision for assistants is not a single general-purpose AI but many small, specific agents that users can easily create using natural language to perform tasks on their behalf <a class="yt-timestamp" data-t="00:38:29">[00:38:29]</a>. This caters to the unique needs of individuals, beyond generic actions like setting alarms <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.
*   **Early Implementations**: Snowflake customers are starting to implement agentic systems, such as the multi-step process in BI for SQL generation, evaluation, and data reasoning <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>.
*   **Hype Cycle**: Agents have already experienced a full hype cycle, from peak excitement to disillusionment, but are now climbing back up as capabilities improve <a class="yt-timestamp" data-t="00:40:59">[00:40:59]</a>.

### Open Source vs. Closed Source Models
*   Open-source models, especially from companies like Meta and Mistral, have been highly influential in demonstrating that the AI industry is not limited to a few players <a class="yt-timestamp" data-t="00:42:11">[00:42:11]</a>.
*   The flexibility they offer allows a vibrant ecosystem to emerge around them, fostering innovation <a class="yt-timestamp" data-t="00:42:31">[00:42:31]</a>.

### Opportunities for Startups
*   The AI market is massive and growing, with ample opportunities for startups across various parts of the stack <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>.
*   While end-to-end platforms offer value to customers, significant innovation is still occurring in the infrastructure layers <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   For assistance startups, the "platform" challenge means they must initially focus on nailing a couple of "really deep use cases" rather than trying to be broadly general <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a> (e.g., building an "engineer" like Devin or a "salesperson") <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>.
*   The application space is just forming, and over the next two years, customers will increasingly demand end-to-end products rather than just building blocks <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>.

### Future of AI Infrastructure
*   The inference stack is rapidly developing, with each improvement leading to cost reductions, which is a welcome development <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>.
*   While there are many companies in the inference space, Baris Gekken believes there will be a "scale play" meaning not many successful businesses will emerge due to dramatic cost reduction pressure <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.
*   Snowflake aims to enable the full ecosystem by making it easy to share and leverage AI-ready data across the Data Cloud, fostering an environment where companies can build complex applications like chatbots on shared financial or other industry data <a class="yt-timestamp" data-t="00:34:33">[00:34:33]</a>.