---
title: Nemo microservices for AI systems
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

Nemo microservices, announced by Nvidia, offer an end-to-end platform designed to build powerful agentic and generative AI systems [03:54:00]. These microservices also facilitate the creation of robust [[nvidias_ai_and_data_flywheel_tools | data flywheels]] around these AI agents [04:02:00].

## What are Data Flywheels?

A [[nvidias_ai_and_data_flywheel_tools | data flywheel]] is described as a continuous loop or cycle that encompasses data processing and curation, model customization, evaluation, and guardrailing for safe interactions, alongside the development of state-of-the-art RAG (Retrieval Augmented Generation) pipelines using enterprise data to deliver accurate responses [02:44:00].

## Core Components of Nemo Microservices

Nemo microservices comprise various components, each catering to a specific stage within the [[nvidias_ai_and_data_flywheel_tools | data flywheel]] loop [04:07:00]. These can be thought of as "Lego pieces" that can be assembled to build a complete [[nvidias_ai_and_data_flywheel_tools | data flywheel]] setup [05:34:00].

The key components include:
*   **Nemo Curator**: Aids in curating high-quality training datasets, including multimodal data [04:13:00].
*   **Nemo Customizer**: Facilitates the fine-tuning and customization of underlying models using advanced techniques like LoRa, Ptuning, and full SFT, with continuous additions of more fine-tuning capabilities [04:21:00].
*   **Nemo Evaluator**: Used for evaluating and benchmarking models against academic and institutional benchmarks, and even using LLMs as a judge [04:37:00]. This supports [[evaluating_ai_systems_at_scale | evaluating AI systems at scale]].
*   **Nemo Guardrails**: Provides guardrail interactions to ensure privacy, security, and safety [04:47:00].
*   **Nemo Retriever**: Enables the construction of state-of-the-art RAG pipelines [04:51:00].

## Ease of Use and Deployment

A key advantage of Nemo microservices is their ease of use, as they are exposed through simple API endpoints [04:57:00]. This allows users to customize, evaluate, and guardrail large language models with just a few API calls [05:04:00].

Furthermore, these microservices offer flexibility in deployment, capable of running anywhere, whether on-premises, in the cloud, in data centers, or even at the edge [05:14:00]. This enables [[leveraging_existing_infrastructure_for_ai_integration | leveraging existing infrastructure for AI integration]] and supports [[distributed_environments_for_scalable_ai_agent_operation | scalable AI agent operation]] across diverse environments. Nvidia's support further ensures enterprise-grade stability and reliability [05:22:00].

## Sample Data Flywheel Architecture

Nemo microservices can be integrated into a [[nvidia_ai_model_deployment_and_architecture | sample data flywheel architecture]]. In such an setup, an end-user interacts with an agent's front-end, which is guardrailed for secure interactions [05:43:00]. On the back end, a model is served as an Nvidia NIM (Nvidia Inference Microservice) for optimized inference [05:58:00].

Within this architecture, a [[nvidias_ai_and_data_flywheel_tools | data flywheel]] loop is established to continuously curate data, store it in a Nemo data store, and use Nemo Customizer and Evaluator to trigger ongoing cycles of retraining and evaluation [06:09:00]. Once a model achieves target accuracy, an IT administrator or AI engineer can promote it to power the agentic use case as the underlying Nvidia NIM [06:23:00].

## Real-World Application

Nvidia itself has adopted and built a [[nvidias_ai_and_data_flywheel_tools | data flywheel]] for its internal NV Info agent, an employee support agent that helps Nvidia employees access enterprise knowledge across various domains such as HR benefits, financial earnings, IT help, and product documentation [06:44:00]. This agent, designed as a multi-model agentic system, leverages a router agent orchestrated by an LLM to direct queries to multiple expert agents [07:37:00]. These expert agents are augmented with RAG pipelines to fetch relevant information [07:51:00]. The data flywheel loop, powered by Nemo Customizer and Evaluator, continuously uses user feedback and production inference logs to curate ground truth data, evaluate models, and promote the most effective smaller models to power the router agent, offering lower latency and cost compared to larger models [08:09:00]. A case study demonstrated that fine-tuning an 8B variant with a relatively small dataset of 685 data points could match the 96% accuracy of a 70B variant, while significantly reducing latency and inference costs [12:27:00]. For example, deploying a 1B model could achieve 94% accuracy, resulting in 98% savings in inference cost and a 70x lower latency compared to a 70B model [13:42:00].

## Framework for Building Effective Data Flywheels

Building effective [[nvidias_ai_and_data_flywheel_tools | data flywheels]] involves a structured approach [14:43:00]:
1.  **Monitor User Feedback**: Implement intuitive methods to collect user feedback signals, including implicit and explicit signals, to detect model drift or inaccuracies [14:48:00].
2.  **Analyze and Attribute Errors**: Spend time analyzing and attributing errors or model drift to understand why the agent behaves in a certain way. This involves classifying errors, attributing failures, and creating ground truth datasets [15:12:00].
3.  **Plan**: Identify different models, generate synthetic datasets, experiment with them, fine-tune them, and optimize resource and cost considerations [15:34:00].
4.  **Execute**: Trigger the [[nvidias_ai_and_data_flywheel_tools | data flywheel]] cycle and establish a regular cadence for tracking accuracy, latency, monitoring performance, and managing the end-to-end GenAI Ops pipeline [15:46:00].

This continuous learning cycle from production logs and knowledge enables the training of smaller, more efficient models to replace larger models already in production [14:20:00].