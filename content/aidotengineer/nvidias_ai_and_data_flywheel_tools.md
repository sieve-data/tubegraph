---
title: Nvidias AI and data flywheel tools
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

Silendrin from [[Nvidia AI model deployment and architecture | Nvidia]]'s generative AI platforms team discusses how to build effective AI agents that remain relevant and helpful over time, emphasizing the role of [[Understanding data flywheels | data flywheels]] over simply using the next biggest LLM [00:00:05].

## What are AI Agents?

AI agents are generating significant interest and are beginning to integrate into the workforce as "digital employees" [00:00:48]. They come in various forms, such as customer service agents, software security agents, and research agents, depending on their use case [00:00:57].

Fundamentally, agents are systems that can perceive, reason, and act on a given task [00:01:12]. This involves:
*   Looking at data [00:01:20].
*   Reasoning to form a plan for user queries [00:01:22].
*   Utilizing [[Using tools and function calls with AI SDK | tools]], functions, and external systems to complete tasks [00:01:27].

Crucially, effective AI agents should also be able to capture and learn from user feedback, continuously refining themselves for improved accuracy and usefulness [00:01:36].

## Challenges in Building and [[Scaling generative AI workloads | Scaling]] Agents

Building and [[Scaling generative AI workloads | scaling]] AI agents can be challenging due to several factors [00:01:56]:
*   **Rapid Data Changes**: Enterprise data, including business intelligence, constantly flows into systems [00:02:05].
*   **Evolving User Preferences**: Customer needs and preferences are continually changing [00:02:16].
*   **Increased Inference Cost**: Deploying larger language models (LLMs) to support use cases leads to higher inference costs, where increased usage drives increased cost [00:02:20].

## [[Understanding data flywheels | Data Flywheels]] as a Solution

[[Understanding data flywheels | Data flywheels]] are continuous loops or cycles designed to address the challenges of building and [[Scaling generative AI workloads | scaling]] AI agents [00:02:38].

At their core, [[Understanding data flywheels | data flywheels]] involve a continuous cycle of:
*   Data processing and curation [00:02:44].
*   Model customization [00:02:48].
*   Evaluation [00:02:50].
*   Guardrailing for safer interactions [00:02:52].
*   Building state-of-the-art Retrieval Augmented Generation (RAG) pipelines alongside enterprise data to provide accurate responses [00:02:56].

As AI agents operate in production, this cycle is triggered to curate ground truth data using inference data, business intelligence, and user feedback [00:03:07]. This allows for continuous experimentation and evaluation of existing and newer models [00:03:20]. The goal is to surface efficient, smaller models that can match the accuracy of larger LLMs but offer lower latency, faster inference, and a reduced total cost of ownership [00:03:26].

## [[Nvidia AI model deployment and architecture | Nvidia]] Nemo Microservices

[[Nvidia AI model deployment and architecture | Nvidia]] introduced Nemo Microservices as an end-to-end platform for building powerful agentic and generative AI systems, as well as robust [[Understanding data flywheels | data flywheels]] [00:03:52]. This platform features various components for each stage of the data flywheel loop [00:04:07]:

*   **Nemo Curator**: Helps curate high-quality training datasets, including multimodal data [00:04:13].
*   **Nemo Customizer**: Facilitates fine-tuning and customizing models using techniques like LoRA, P-tuning, and full SFT, with continuous additions of more fine-tuning capabilities [00:04:21].
*   **Nemo Evaluator**: Used for benchmarking on academic and institutional benchmarks, and for using LLMs as judges [00:04:34].
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety [00:04:47].
*   **Nemo Retriever**: Aids in building state-of-the-art RAG pipelines [00:04:51].

Nemo Microservices are designed for ease of use, exposed as simple API endpoints [00:04:57]. With minimal API calls, users can customize, evaluate, and guardrail LLMs for specific use cases [00:05:04]. They offer deployment flexibility, running anywhere from on-prem to cloud, data centers, or even the edge [00:05:14]. [[Nvidia AI model deployment and architecture | Nvidia]] also provides enterprise-grade stability and support [00:05:22].

### Sample [[Nvidia AI model deployment and architecture | Data Flywheel Architecture]]

A sample [[Nvidia AI model deployment and architecture | data flywheel architecture]] leveraging Nemo Microservices can be thought of as "Lego pieces" that can be assembled [00:05:29].
In such an architecture:
*   An end-user interacts with an agent's front end (e.g., a customer service agent) [00:05:43].
*   The system is guardrailed for safer interactions [00:05:50].
*   On the backend, a model is served as an [[Nvidia AI model deployment and architecture | Nvidia]] NIM for optimized inference [00:05:55].
*   A data flywheel loop is set up to continuously curate data and store it in a Nemo data store [00:06:02].
*   Nemo Customizer and Evaluator trigger a continuous cycle of retraining and evaluation [00:06:15].
*   Once a model meets target accuracy, an IT admin or AI engineer can promote it to power the agentic use case as the underlying [[Nvidia AI model deployment and architecture | NIM]] [00:06:23].

## Real-World Case Study: [[Nvidia AI model deployment and architecture | NV]] Info Agent

[[Nvidia AI model deployment and architecture | Nvidia]] implemented a [[Understanding data flywheels | data flywheel]] for their internal [[Nvidia AI model deployment and architecture | NV]] Info agent, an employee support agent providing access to enterprise knowledge across various domains [00:06:44]. This chatbot assists [[Nvidia AI model deployment and architecture | Nvidia]] employees with queries related to HR benefits, financial earnings, IT help, and product documentation [00:07:02].

The underlying [[Nvidia AI model deployment and architecture | data flywheel architecture]] for the [[Nvidia AI model deployment and architecture | NV]] Info agent involves:
*   An employee submitting a query, which is guardrailed for safety [00:07:26].
*   A main router agent, run by an LLM, orchestrates multiple expert agents [00:07:37].
*   Each expert agent specializes in a specific domain and is augmented with a RAG pipeline to fetch relevant information [00:07:47].
*   A data flywheel loop continuously builds upon user feedback and production inference logs [00:08:09].
*   Subject matter experts and human-in-the-loop feedback continuously curate ground truth data [00:08:20].
*   Nemo Customizer and Evaluator are used to evaluate multiple models and promote the most effective one to power the router agent [00:08:27].

### The Router Agent Problem Statement

The core problem for the router agent is to accurately route a user query to the correct expert agent while [[Efficiency and smart execution engines in AI applications | using faster and cost-effective LLMs]] [00:09:27].

Initial comparisons showed:
*   A 70B variant achieved 96% baseline accuracy in routing queries, but with a latency of 26 seconds to generate the first token [00:09:55].
*   Smaller 8B variants showed subpar accuracy, falling below 14% [00:10:22].

Many enterprises might stop here and conclude that larger models are necessary due to the accuracy gap [00:10:33]. However, [[Understanding data flywheels | data flywheels]] demonstrate a different approach [00:10:57].

### [[Strategies for implementing data flywheels | Data Flywheel Implementation]] and Results

1.  **Feedback Collection**: The 70B Llama variant was run, and a feedback form was circulated among [[Nvidia AI model deployment and architecture | Nvidia]] employees to submit queries and rate usefulness [00:11:02].
2.  **Data Curation**: 1,224 data points were curated, with 729 satisfactory and 495 unsatisfactory responses [00:11:24].
3.  **Error Analysis**: Nemo Evaluator, using LLM as a judge, investigated the 495 unsatisfactory responses [00:11:44]. It was found that 140 were due to incorrect routing, and further manual analysis identified 32 truly due to incorrect routing [00:11:52].
4.  **Ground Truth Dataset**: A ground truth dataset of 685 data points was created, split 60/40 for training/fine-tuning and testing/evaluation [00:12:09].

Surprisingly, with just 685 data points and the [[Understanding data flywheels | data flywheel]] setup, significant results were achieved [00:12:27]:
*   Fine-tuning smaller variants like the 8B and 3B models demonstrated that the 8B model could match the 70B variant's accuracy [00:13:04].
*   The 1B variant also achieved 94% accuracy, only 2% below the 70B model [00:13:22].

This allows for a trade-off between accuracy and cost/resource management [00:13:31]. Deploying a 1B model, for instance, leads to:
*   98% savings in lower inference cost [00:13:42].
*   10x to 70x model size reduction [00:13:50].
*   70x lower latency [00:13:56].

The power of a [[Understanding data flywheels | data flywheel]] lies in building an automated loop for continuous and periodic evaluation and fine-tuning as new models emerge [00:13:59]. This process surfaces smaller models that can replace larger, more costly models in production workflows, continuously learning from ongoing production logs [00:14:02].

## [[Strategies for implementing data flywheels | Framework for Building Effective Data Flywheels]]

To build effective [[Understanding data flywheels | data flywheels]], consider the following framework [00:14:43]:

1.  **Monitor User Feedback**:
    *   Focus on intuitive ways to collect user feedback signals [00:14:48].
    *   Consider intuitive user experience, privacy compliance, implicit signals, and explicit signals [00:14:57].
    *   Identify model drift or inaccuracies [00:15:08].
2.  **Analyze and Attribute Errors**:
    *   Dedicate time to analyze and attribute errors or model drift [00:15:12].
    *   Classify errors and attribute failures [00:15:23].
    *   Create ground truth datasets for subsequent steps [00:15:26].
3.  **Plan**:
    *   Identify different models [00:15:34].
    *   Generate synthetic datasets [00:15:36].
    *   Experiment with and fine-tune models [00:15:38].
    *   Understand and optimize resource and cost implications [00:15:41].
4.  **Execute**:
    *   Trigger the [[Understanding data flywheels | data flywheel]] cycle [00:15:48].
    *   Set up a regular cadence and mechanism to track accuracy, latency, and monitor performance and production logs [00:15:53].
    *   Effectively manage the end-to-end GenAI Ops pipeline [00:16:05].

This framework, combined with tools like [[Nvidia AI model deployment and architecture | Nvidia]] Nemo Microservices and [[Nvidia AI model deployment and architecture | NVIDIA NIM]], helps in building and [[Scaling generative AI workloads | scaling]] agentic AI use cases with robust [[Understanding data flywheels | data flywheels]] [00:16:12].