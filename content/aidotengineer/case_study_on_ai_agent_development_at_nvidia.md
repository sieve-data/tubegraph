---
title: Case study on AI agent development at NVIDIA
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

Silendrin, from Nvidia's generative AI platforms team, details the approach to [[building_and_improving_ai_agents | building effective AI agents]] that remain relevant and helpful over time, focusing on data flywheels rather than relying solely on the latest large language models (LLMs) <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article explores what data flywheels are, how they were applied to an internal agent at NVIDIA, and the lessons learned <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## What Are AI Agents?

AI agents are systems capable of perceiving, reasoning, and acting on an underlying task <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. They process data, develop plans to address user queries, and utilize tools, functions, and external systems to achieve their goals <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Crucially, effective AI agents capture and learn from user feedback, continuously refining themselves to improve accuracy and usefulness based on user preferences and data <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## [[challenges_in_developing_ai_agents | Challenges in Developing AI Agents]]

[[developing_and_optimizing_ai_agents | Building and scaling agents]] can be challenging due to several factors <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   **Rapid Data Change**: Enterprise data, including business intelligence, constantly evolves <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Evolving User Preferences**: Customer needs and user preferences change over time <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **High Inference Costs**: Deploying larger LLMs for complex use cases leads to increased inference costs, where greater usage directly translates to higher expenses <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Data Flywheels: A Solution

Data flywheels offer a solution to these [[challenges_in_developing_ai_agents | challenges]] <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. At their core, a data flywheel is a continuous cycle involving <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:
1.  **Data Processing and Curation**: Gathering and organizing data.
2.  **Model Customization**: Adapting models for specific tasks.
3.  **Evaluation**: Assessing model performance.
4.  **Guardrailing**: Ensuring safe and secure interactions.
5.  **RAG Pipelines**: Building state-of-the-art Retrieval Augmented Generation (RAG) pipelines alongside enterprise data to provide accurate responses <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

As AI agents operate in production, this cycle continuously curates ground truth data using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This enables continuous experimentation and evaluation of existing and newer models, leading to the identification of smaller, more efficient models that match the accuracy of larger LLMs but offer lower latency, faster inference, and reduced total cost of ownership <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Nvidia Nemo Microservices

Nvidia provides **Nemo Microservices**, an end-to-end platform designed to [[building_and_improving_ai_agents | build powerful agentic and generative AI systems]] and the data flywheels around them <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. These microservices offer components for each stage of the data flywheel loop:
*   **Nemo Curator**: For curating high-quality training datasets, including multimodal data <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Nemo Customizer**: For fine-tuning and customizing models using techniques like LoRa, P-tuning, and full SFT <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Nemo Evaluator**: For benchmarking models against academic and institutional standards, and using LLMs as judges <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Nemo Guardrails**: For providing safe interactions related to privacy, security, and safety <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Nemo Retriever**: For [[building_and_improving_ai_agents | building state-of-the-art RAG pipelines]] <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

These microservices are exposed as easy-to-use API endpoints, allowing users to customize, evaluate, and guardrail LLMs with minimal calls <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. They offer deployment flexibility across on-prem, cloud, data centers, and even the edge, with enterprise-grade stability and support <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Sample Data Flywheel Architecture

A typical data flywheel architecture using Nemo Microservices involves an end-user interacting with an agent's front end, which is guarded for safe interactions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Behind the scenes, an optimized model served as an Nvidia NIM powers the agent <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. The data flywheel continuously curates data, stores it in a Nemo data store, and uses Nemo Customizer and Evaluator to trigger continuous retraining and evaluation <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Once a model meets target accuracy, it can be promoted by an IT admin or AI engineer to power the agent's use case <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## [[case_study_of_ai_interview_agent_development | Case Study]]: NV Info Agent

Nvidia adopted and [[building_and_improving_ai_agents | built a data flywheel]] for their internal **NV Info Agent**, an employee support agent designed to provide Nvidia employees with access to enterprise knowledge across multiple domains <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This chatbot answers queries ranging from HR benefits, financial earnings, and IT help to product documentation <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### NV Info Agent Architecture

The NV Info Agent's data flywheel architecture involves an employee submitting a query, which is then guardrailed for safety <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. A **router agent**, orchestrated by an LLM, guides the query to one of multiple underlying expert agents <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Each expert agent specializes in a specific domain and uses a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

A data flywheel loop is set up to determine which models power these expert agents <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. This loop continuously incorporates user feedback and production data inference logs <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Ground truth data is curated using subject matter experts and human-in-the-loop feedback <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. Nemo Customizer and Evaluator are used to continually assess models and promote the most effective one as a NIM to power the router agent <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Router Agent Problem Statement and Solution

The core challenge for the router agent was to accurately route a user query to the correct expert agent using a fast and cost-effective LLM <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

Initially, a 70B variant of a model achieved a 96% baseline accuracy in routing queries to the correct expert agent without fine-tuning <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. However, smaller variants like the 8B model showed subpar accuracy, below 14% <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

To address this, Nvidia implemented the data flywheel approach <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>:
1.  **User Feedback Collection**: The 70B model was run, and Nvidia employees were asked to submit queries and provide feedback on response usefulness <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
2.  **Data Curation**: This led to 1,224 data points, with 729 satisfactory and 495 unsatisfactory responses <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
3.  **Error Analysis**: Nemo Evaluator, using an LLM as a judge, investigated the 495 unsatisfactory responses <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. It was found that 140 were due to incorrect routing, and further manual analysis by subject matter experts confirmed 32 were truly due to this issue <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
4.  **Ground Truth Dataset**: A ground truth dataset of 685 data points was created, split 60/40 for training (fine-tuning smaller models) and testing/evaluation <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.

### Results and Benefits

The results from fine-tuning with just 685 data points were significant <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>:
*   The 70B model had 96% accuracy but a latency of 26 seconds to generate the first token <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   The 8B model initially had 14% accuracy but a latency 70% lower than the 70B model <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   After fine-tuning, the **8B model was able to match the 70B model's accuracy** <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   Even the 1B variant achieved 94% accuracy, only 2% below the 70B model <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

By deploying smaller models, such as the 1B model, Nvidia achieved <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>:
*   98% savings in lower inference cost <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   10x to 70x model size reduction <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   70x lower latency <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

This demonstrates the power of a data flywheel: continuously learning from production logs and knowledge to train smaller, more efficient models that can replace larger ones while maintaining or even improving performance <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.

## Framework for [[building_and_improving_ai_agents | Building and Improving AI Agents]]

To [[building_and_improving_ai_agents | build effective data flywheels]], consider this four-step framework <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>:

1.  **Monitor User Feedback**:
    *   Implement intuitive ways to collect user feedback signals (implicit and explicit) <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
    *   Identify model drift or inaccuracies in the agent's behavior <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

2.  **Analyze and Attribute Errors**:
    *   Spend time analyzing and attributing errors or model drift to their root causes <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
    *   Classify errors, attribute failures, and create ground truth datasets <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

3.  **Plan**:
    *   Identify different models suitable for the task <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
    *   Generate synthetic datasets and experiment with them <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
    *   Fine-tune models and optimize resource allocation and cost <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

4.  **Execute**:
    *   Trigger the data flywheel cycle <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   Set up a regular cadence or mechanism to track accuracy, latency, and monitor performance and production logs <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
    *   Manage the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.

This framework helps in [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] and maintaining their effectiveness over time <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.