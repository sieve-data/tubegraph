---
title: Building and utilizing large language models
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Snowflake's Head of AI, Baris Gorken, leads the company's extensive AI efforts, including products like Cortex AI and their own large language model (LLM) called Arctic [00:00:03]. Snowflake focuses on the infrastructure that supports [[developing_and_utilizing_ai_models_in_the_tech_industry | AI tools in production]] [00:00:15].

## Snowflake's Arctic LLM: Development and Purpose

Snowflake developed Arctic LLM to address specific enterprise needs, particularly for Business Intelligence (BI) experiences [00:01:06]. The primary goal was to build a [[understanding_language_models | large language model]] highly proficient in SQL generation and instruction following, differentiating it from general-purpose LLMs [00:01:12]. While it performs well on common tasks, its specialization is in SQL co-pilot and high-quality chatbot functionalities for enterprise [00:02:00].

The development of Arctic LLM was a relatively small effort compared to others in the market, starting around December [00:00:52]. It was built in approximately three to four months by a small team that included researchers from DeepSpeed and vLLM [00:01:46]. The team focused on an innovative and efficient architecture, allowing the model to be trained at 1/8th the cost of similar models [00:02:27]. A significant amount of time was dedicated to perfecting the data recipe for training [00:02:49].

## Snowflake Cortex: A Managed Service for LLMs

Snowflake's core AI offering is Cortex, a managed service designed to run various [[understanding_language_models | large language models]], including Arctic, Mistral, and Meta models [00:01:11]. Cortex aims to simplify AI deployment for customers by providing an integrated, easy-to-use platform [00:09:42].

Within Cortex, Snowflake offers:
*   **Cortex Search** A high-quality search system crucial for Retrieval-Augmented Generation (RAG) [00:10:39]. It utilizes Snowflake's own embedding model, Arctic Embed, which is efficient (one-quarter the size of OpenAI's embedding model) yet achieves high benchmark scores [00:11:00]. Cortex Search is a hybrid system, combining vector search with lexical keyword search to reduce hallucinations [00:12:14].
*   **Cortex Analyst** A BI product that combines multiple LLMs to answer BI questions [00:10:49]. It is designed to know when to ask for clarifications or abstain from answering questions it cannot confidently address [00:05:19].

## Key Use Cases for LLMs on Snowflake

Snowflake customers are primarily [[use_and_evaluation_of_large_language_models_llms | utilizing LLMs]] for three main areas within Cortex:

### AI for Business Intelligence (BI) and Text-to-SQL
This use case involves using AI to build BI experiences, particularly converting natural language to SQL queries and data insights [00:01:09]. While demos are easy, real-world data presents complexities like tens of thousands of tables and hundreds of thousands of columns with inconsistent naming conventions [00:04:30]. Snowflake's Cortex Analyst aims to overcome this by stitching together multiple LLMs and systems to increase quality [00:05:05].

Challenges in text-to-SQL include complex joins, hallucinating on column names, and generating non-executable queries [00:06:39]. Snowflake addresses this by prioritizing precision over recall, meaning the system is designed to know when *not* to answer a question or to ask for clarification, rather than attempting to answer everything and risk inaccuracy [00:08:06]. A feedback loop allows customers to create "verified queries" to increase confidence [00:06:08].

### Chatbots and Unstructured Data
Customers build chatbots to interact with their unstructured data, such as documents and PDFs [00:03:32].

### Data Extraction and Natural Language Processing
This involves using natural language to extract data from text and then process it in batch [00:03:48]. Examples include analyzing sales call logs, customer support tickets, and summarizing open-ended questions from employee surveys [00:03:59]. This capability can condense tasks that would take hours into a single prompt [00:09:22]. Snowflake focuses on providing task-specific functions that minimize the need for complex prompting or data pipeline work from customers [00:09:55].

### Enterprise Search
A re-emerging use case, enterprise search leverages LLMs for internal information retrieval and upgrading existing search stacks [00:12:33].

## [[challenges_in_building_and_deploying_ai_features | Challenges and Considerations for LLM Deployment]]

### Ensuring Quality and Reliability
Hallucinations remain a significant concern, especially in regulated industries where they can be catastrophic [00:16:06]. For BI, the accuracy needs to be extremely high (e.g., for CFOs reviewing revenue figures), which is why human-in-the-loop systems are being integrated [00:05:44]. Measurement and evaluation frameworks for LLMs are still maturing [00:28:11]. Snowflake acquired TruEra, an LLM evaluation platform with an open-source product called Trulens, to help customers evaluate their systems at scale [00:14:06].

### Data Governance, Privacy, and Security
A major advantage for Snowflake is its existing data governance framework, which includes granular access controls [00:13:55]. This allows LLMs running within Snowflake to respect established data security policies. For instance, a chatbot answering HR questions would provide different responses based on the user's access permissions, preventing data leakage [00:17:11]. This built-in governance is a huge advantage, as many customers spend years getting their data governance in place [00:18:52].

Concerns also exist around prompt injections and the perceived guardrails of [[open_source_vs_closed_source_large_language_models | open-source vs. proprietary models]] [00:26:47]. Snowflake's Cortex Guard, which uses Llama Guard, provides additional reassurances regarding model behavior and brand alignment [00:27:14].

### Model Selection and Customization
Snowflake advises customers to start with large, readily available models and RAG solutions for Proof-of-Concepts (POCs) [00:19:23]. Once a system is proven, optimization for production can involve fine-tuning a smaller model for latency and cost advantages [00:19:36]. For companies with large amounts of unique data, particularly in regulated industries like healthcare, building custom, pre-trained models makes sense for full control over the training data and understanding specialized language [00:19:49]. Snowflake supports fine-tuning and, for a small number of customers, full model training within their platform [00:21:06].

Model selection by customers is sometimes influenced more by brand recognition than by actual capability [00:21:36].

## The Role of AI Infrastructure and Ecosystem

Snowflake's strategy involves supporting a wide range of LLMs and continuously optimizing its inference stack [00:22:42]. The vLLM team, now part of Snowflake, is instrumental in ensuring that the inference stack efficiently supports new and very large models, including multi-node inference [00:23:03]. These optimizations are often upstreamed back to the vLLM project, benefiting the broader ecosystem [00:23:20].

The cost of running LLMs is decreasing rapidly due to model distillation and optimization [00:11:31]. While companies are aware of LLM costs, it hasn't been a significant blocker for internal use cases, as volumes are not yet massive [00:25:52].

Snowflake partners with model providers (e.g., Mistral, Reka AI, AI21) and companies offering end-to-end solutions like Landing AI [00:29:38]. These partners can run their applications directly within the Snowflake boundary, ensuring data security and preventing data egress [00:30:00]. This approach leverages Snowflake's unique position as a data platform where customer data already resides, enabling seamless AI integration and data sharing within the ecosystem [00:35:12].

## Internal Applications of LLMs at Snowflake

Snowflake uses LLMs internally for various purposes:
*   Sales teams analyze sales conversations to understand wins and losses [00:30:27].
*   Employee assistants answer questions based on internal data and documents [00:30:41].
*   Documentation generation and general chatbot use cases [00:30:52].
*   Optimizing their SQL engine and integrating AI capabilities into their Marketplace [00:31:14].

## Future Outlook: Agents and AI Assistants

Baris Gorken is excited about the future of AI assistants, particularly how LLMs enable them to move beyond hand-crafted use cases to more general-purpose actions by calling APIs [00:37:06]. He envisions a future with many small, specific agents, easily set up using natural language, performing tasks on a user's behalf [00:38:29]. This contrasts with general-purpose assistants that apply to everyone, focusing instead on unique, personalized needs [00:38:52].

While still early, Snowflake's customers are beginning to implement agentic systems, such as the multi-step process in their BI solution that generates, evaluates, runs, and reasons about SQL queries [00:39:17]. He compares this to ChatGPT's data analysis feature, which offers an interesting glimpse into the future of BI and data analysis [00:39:44].

Agentic systems are currently overhyped in the short term but are expected to match that hype as they mature [00:40:49]. For startups in the assistant space, the challenge is that it needs to be a platform, but a startup cannot begin as one [00:43:39]. The key is to nail a couple of really deep, specific use cases, like building an "engineer" (Devin) or a "salesperson" agent, rather than trying to do many small things [00:43:54].

## [[open_source_vs_closed_source_large_language_models | Open Source vs. Closed Source Models]]

Companies like Meta and Mistral have been instrumental in fostering an ecosystem around [[open_source_vs_closed_source_large_language_models | open-source models]], offering flexibility and enabling further innovation [00:42:11]. There is a lot of gratitude for Meta's efforts in aligning models like Llama [00:42:40]. Baris Gorken remains excited about model startups, citing Mistral as an example of a small, capable team building amazing models and creating awareness [00:42:52].

## Opportunities in AI Infrastructure

The inference stack in AI infrastructure is developing rapidly, with each improvement leading to cost reduction [00:35:52]. While it's a hard question whether long-term businesses can be built solely on the inference side, there is a scale play, and some businesses will succeed, though likely not many [00:36:10].

The market for AI infrastructure is massive and growing, with opportunities for startups at various points in the stack [00:33:33]. Despite the value of end-to-end platforms, innovation continues across the entire stack [00:34:02]. Over the next two years, the focus is expected to shift from providing building blocks to delivering end-to-end products that customers want, with the application space blooming [00:45:28].