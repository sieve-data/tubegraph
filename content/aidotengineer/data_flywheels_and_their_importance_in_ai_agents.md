---
title: Data flywheels and their importance in AI agents
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

[[AI agents]] are gaining significant attention and are being integrated into the workforce as new digital employees <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. They serve various functions, including customer service, software security, and research <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. An [[components_of_ai_agents | AI agent]] is defined as a system capable of perceiving, reasoning, and acting on an underlying task <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. They process data, develop plans based on user queries, and utilize tools, functions, and external systems to achieve their goals <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A complete [[developing_and_optimizing_ai_agents | AI agent]] cycle involves capturing and learning from user feedback to continuously refine performance, ensuring accuracy and usefulness <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Challenges in Building and Scaling AI Agents

[[Design challenges for AI agents | Building and scaling AI agents]] can be difficult <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a> due to several factors:
*   **Rapid Data Change**: Enterprise customers constantly receive new data and business intelligence <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Evolving User Preferences**: User preferences and customer needs frequently change <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Increased Inference Cost**: Deploying larger language models (LLMs) to support use cases leads to higher inference costs, where increased usage directly drives up expenses <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This is where data flywheels provide a solution <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## What are Data Flywheels?

A data flywheel is a continuous loop or cycle that ensures [[AI agents]] remain relevant and helpful over time <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It's not about relying solely on the latest LLM, but rather about incorporating simple data flywheels <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

At its core, a data flywheel starts with enterprise data and involves:
*   **Data processing and curation**: Continuously refining data <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Model customization**: Adapting models to specific needs <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Evaluation**: Benchmarking and assessing model performance <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Guardrailing**: Ensuring safer interactions for privacy, security, and safety <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Building state-of-the-art RAG (Retrieval Augmented Generation) pipelines**: To provide relevant and accurate responses <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

As [[Stateful AI Agents | AI agents]] operate in production, this cycle is triggered, leading to continuous data curation from inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This enables experimentation and evaluation of existing and newer models to identify efficient, smaller models that maintain accuracy comparable to larger LLMs but offer lower latency, faster inference, and reduced total cost of ownership <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## NVIDIA Nemo Microservices

NVIDIA has introduced Nemo Microservices as an end-to-end platform for [[building_ai_agents_using_data_flywheels | building powerful agentic and generative AI systems]] and robust data flywheels around them <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. These microservices offer various components for each stage of the data flywheel loop:
*   **Nemo Curator**: Helps curate high-quality training data sets, including multimodal data <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Nemo Customizer**: Facilitates fine-tuning and customizing models using advanced techniques like LoRA, P-tuning, and full SFT <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Nemo Evaluator**: Used for evaluating models on academic and institutional benchmarks, as well as using LLM as a judge <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Nemo Retriever**: Enables the creation of state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

These microservices are exposed as simple API endpoints, allowing users to customize, evaluate, and guardrail LLMs with minimal calls <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. They can be deployed anywhere – on-premises, in the cloud, in data centers, or at the edge – with enterprise-grade stability and support from NVIDIA <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Sample Data Flywheel Architecture

A typical data flywheel architecture leveraging Nemo Microservices can be visualized as "Lego pieces" <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. An end-user interacts with the front end of an agent (e.g., a customer service agent), which is guarded for safety <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. On the backend, a model served as an NVIDIA NIM (NVIDIA Inference Microservice) provides optimized inference <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

To identify the most suitable model without compromising accuracy, a data flywheel loop is established <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This loop continuously curates data, stores it in Nemo data store, and uses Nemo Customizer and Evaluator to trigger cycles of retraining and evaluation <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Once a model meets the desired accuracy, an IT admin or AI engineer can promote it to power the agentic use case <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Case Study: NVIDIA NVInfo Agent

NVIDIA adopted and [[Building and Improving AI Agents | built a data flywheel]] for its internal employee support agent, NVInfo, which provides access to enterprise knowledge across various domains like HR, finance, IT help, and product documentation <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

The NVInfo agent's data flywheel architecture involves:
*   An employee submits a query to the agent <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   The query is guardrailed for safety and security <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   A "router agent," powered by an LLM, orchestrates multiple "expert agents" <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Each expert agent specializes in a specific domain and uses a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   A data flywheel loop continuously builds on user feedback and production inference logs to determine which models power these expert agents <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   Ground truth data is curated using subject matter experts and human-in-the-loop feedback <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   Nemo Customizer and Evaluator are used to constantly evaluate models and promote the most effective one as an NIM to power the router agent <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Focus: The Router Agent

The router agent, an example of a mixture-of-agents architecture, understands user intent and context to route queries to the appropriate expert agent, which then uses a RAG pipeline <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. The goal is to ensure accurate routing using a fast and cost-effective LLM <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.

Initially, a 70B variant LLM achieved a 96% baseline accuracy in routing without fine-tuning, but smaller variants (e.g., 8B) had subpar accuracy (below 14%) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This often leads enterprises to choose larger, more expensive models <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

Using a data flywheel, the team:
1.  **Collected User Feedback**: Employees submitted queries and feedback on response usefulness <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
2.  **Curated Data**: From 1224 data points, 495 were unsatisfactory <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
3.  **Investigated Errors**: Nemo Evaluator, using LLM as a judge, found 140 unsatisfactory responses were due to incorrect routing <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. Manual analysis by subject matter experts confirmed 32 of these were true routing errors <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
4.  **Created Ground Truth Dataset**: An 868-data-point dataset was created, split 60/40 for training/fine-tuning and testing/evaluation <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

### Results

With just 685 data points for fine-tuning, the results were significant <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>:
*   The 70B variant had 96% accuracy but a latency of 26 seconds for the first token response <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   The 8B variant initially had 14% accuracy but much lower latency (70% lower) <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   After fine-tuning, the 8B variant matched the 70B variant's accuracy <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   Even the 1B variant achieved 94% accuracy, only 2% below the 70B model <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

This demonstrated a trade-off between accuracy and cost/resource management <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Deploying a 1B model, for example, could lead to:
*   98% savings in lower inference cost <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   70x model size reduction <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   70x lower latency <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

This highlights the power of data flywheels in automating continuous evaluation and fine-tuning, surfacing smaller, more efficient models that can replace larger, more costly ones in production workflows <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

## [[framework_for_creating_effective_data_flywheels | Framework for Creating Effective Data Flywheels]]

To build effective data flywheels, consider this four-step framework <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>:

1.  **Monitor User Feedback**: Implement intuitive ways to collect user feedback signals (implicit or explicit) to detect model drift or inaccuracies in your agentic system <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
2.  **Analyze & Attribute Errors**: Investigate and classify errors or model drift to understand why the agent is behaving in a certain way <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. Attribute failures and create a ground truth dataset from this analysis <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
3.  **Plan**: Identify different models, generate synthetic datasets, and experiment with fine-tuning them <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. Optimize resource and cost considerations during this phase <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.
4.  **Execute**: Put the plan into action by triggering the data flywheel cycle <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>. This includes setting up a regular cadence to track accuracy, latency, performance monitoring, and production logs, effectively managing the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.

This framework helps in [[importance_and_progress_of_ai_agents | building and improving AI agents]] that are continuously learning and adapting based on real-world interactions <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.