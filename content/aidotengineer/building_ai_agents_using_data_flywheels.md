---
title: Building AI agents using data flywheels
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

[[Building and Improving AI Agents | AI agents]] are increasingly becoming a part of the workforce as new digital employees, appearing in various forms such as customer service, software security, and research agents, among others <a class="yt-timestamp" data-t="00:50:53">[00:50:53]</a>. At their core, [[components_of_ai_agents | AI agents]] are systems capable of perceiving, reasoning, and acting on underlying tasks <a class="yt-timestamp" data-t="01:12:14">[01:12:14]</a>. This means they can analyze data, develop a plan based on a user query, and utilize tools and external systems to complete the task <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>. For [[Building and Improving AI Agents | AI agents]] to complete their cycle effectively, they must also be able to capture and learn from user feedback, refining themselves to be more accurate and useful over time <a class="yt-timestamp" data-t="01:36:19">[01:36:19]</a>.

## Challenges in Building and Scaling AI Agents

[[Developing and optimizing AI agents | Building AI agents]] can be challenging, and [[scaling_ai_agents_in_production | scaling them]] presents increasing difficulties <a class="yt-timestamp" data-t="01:56:19">[01:56:19]</a>. Key challenges include:
*   **Rapidly changing data**: Enterprise customers using [[Building and Improving AI Agents | agentic systems]] constantly encounter new data and business intelligence flowing into their systems <a class="yt-timestamp" data-t="02:04:01">[02:04:01]</a>.
*   **Evolving user preferences**: User preferences and customer needs are constantly changing <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **High inference costs**: Deploying larger language models to support use cases can lead to increased inference costs, as increased usage drives up expenses <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>.

## [[data_flywheels_and_their_importance_in_ai_agents | What are Data Flywheels?]]

[[data_flywheels_and_their_importance_in_ai_agents | Data flywheels]] are continuous loops or cycles crucial for [[Building and Improving AI Agents | AI agents]] to remain relevant and helpful <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. They start with enterprise data and involve:
*   Data processing and curation <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   Model customization <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
*   Evaluation <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   Guardrailing for safer interactions <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   Building state-of-the-art RAG (Retrieval-Augmented Generation) pipelines alongside enterprise data to provide accurate responses <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

As [[Building and Improving AI Agents | AI agents]] operate in production environments, the [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] cycle continuously curates ground truth data using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This enables continuous experimentation and evaluation of models, surfacing efficient, smaller models that offer comparable accuracy to larger models but with lower latency, faster inference, and reduced total cost of ownership <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

## NVIDIA Nemo Microservices

NVIDIA offers Nemo Microservices, an end-to-end platform designed for [[Building and Improving AI Agents | building powerful agentic]] and generative [[Building and Improving AI Agents | AI systems]], as well as the [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] that support them <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. These microservices are exposed as simple API endpoints for ease of use <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>. Key components include:
*   **Nemo Curator**: Helps curate high-quality training datasets, including multimodal data <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
*   **Nemo Customizer**: Facilitates fine-tuning and customizing underlying models using state-of-the-art techniques like LoRa, P-tuning, and full SFT <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Nemo Evaluator**: Used for benchmarking models on academic and institutional benchmarks, and for evaluation using LLM as a judge <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Nemo Retriever**: Aids in building state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

These microservices can be run anywhere, including on-premise, in the cloud, on data centers, or at the edge, with enterprise-grade stability and support from NVIDIA <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

## Sample Data Flywheel Architecture

A [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] architecture can be assembled using Nemo microservices like Lego pieces <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. For an [[Building and Improving AI Agents | AI agent]] (e.g., a customer service agent) interacting with an end-user, the system is guardrailed for safer interactions <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>. On the backend, a model is served via NVIDIA NIM for optimized inference <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.

To identify the most suitable model without sacrificing accuracy, a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] loop is set up to continuously:
1.  Curate data <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
2.  Store it in a Nemo data store <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
3.  Use Nemo Customizer and Evaluator to trigger continuous retraining and evaluation <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>.

Once a model meets target accuracy, an IT administrator or AI engineer can promote it to power the [[Building and Improving AI Agents | agentic]] use case as the underlying NVIDIA NIM <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

## Real-World Case Study: NV Info Agent

NVIDIA adopted and built a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] for their NV Info agent, an internal employee support agent that provides access to enterprise knowledge across various domains, such as HR benefits, financial earnings, IT help, and product documentation <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

In this system, when an employee submits a query, it's guardrailed for safety and secure interaction <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>. A router agent, run by an LLM, orchestrates multiple expert agents <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. Each expert agent excels in its specific domain and is augmented with a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.

To select the models powering these expert agents, a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] loop is set up, constantly building on user feedback and production data inference logs <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. Ground truth data is continuously curated using subject matter experts and human-in-the-loop feedback <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>. Nemo Customizer and Evaluator are used to evaluate multiple models, promoting the most effective one to power the router agent <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>.

### Router Agent Case Study

The router agent's problem statement is to accurately route a user query to the correct expert agent using a fast and cost-effective LLM <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.

Initial comparisons showed:
*   **70B Llama Variant**: Achieved a 96% baseline accuracy for routing queries <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>, but with a latency of 26 seconds to generate the first token response <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   **8B Variant**: Showed a subpar accuracy of less than 14% without fine-tuning <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>, but its latency was almost 70% lower <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.

Enterprises often mistakenly conclude that only larger models are viable due to their higher initial accuracy <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. However, [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] can change this <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>.

NVIDIA ran the 70B Llama variant and collected user feedback from employees via a feedback form <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>. Out of 1,224 data points, 495 were unsatisfactory responses <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>. Using Nemo Evaluator and LLM as a judge, 140 of these were attributed to incorrect routing <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. Manual analysis with a subject matter expert confirmed 32 instances were truly due to incorrect routing <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.

This led to the creation of a ground truth dataset of 685 data points, split 60/40 for training (fine-tuning smaller models) and testing/evaluation <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

**Results After Fine-tuning with Data Flywheel**:
*   The 8B variant, after fine-tuning with just 685 data points, was able to match the 96% accuracy of the 70B variant <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
*   A 1B variant achieved 94% accuracy, only 2% below the 70B model <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

By deploying a 1B model, NVIDIA achieved 98% savings in inference cost, 70x model size reduction, and 70x lower latency <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>. This demonstrates the power of [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] in enabling continuous evaluation and fine-tuning, allowing smaller, more efficient models to replace larger ones in production <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

## [[Framework for creating effective data flywheels | Framework for Building Effective Data Flywheels]]

To build effective [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]], consider the following framework:

### 1. Monitor User Feedback
*   Focus on intuitive ways to collect user feedback signals <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>.
*   Consider intuitive user experience, privacy compliance, and both implicit and explicit signals <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>.
*   This helps identify model drift or inaccuracies in the [[Building and Improving AI Agents | agentic system]] <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

### 2. Analyze and Attribute Errors
*   Spend time analyzing and attributing errors or model drift to understand why the [[Building and Improving AI Agents | agent]] behaves in a certain way <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>.
*   Classify errors and attribute failures <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.
*   Create a ground truth dataset from this analysis for further use <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>.

### 3. Plan
*   Identify different models suitable for the task <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
*   Generate synthetic datasets for experimentation <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.
*   Experiment with and fine-tune models <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.
*   Optimize resources and costs <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.

### 4. Execute
*   Trigger the [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] cycle <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
*   Set up a regular cadence and mechanism to track accuracy, latency, and performance <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
*   Monitor production logs and manage the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.

By continuously learning from ongoing production logs and knowledge to train smaller models, the power of the [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] is truly unleashed <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>.