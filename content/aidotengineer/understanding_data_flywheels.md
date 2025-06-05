---
title: Understanding data flywheels
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

AI agents are gaining significant traction and are being integrated into the workforce as new digital employees, appearing in various forms such as customer service, software security, and research agents <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. At their core, agents are systems capable of perceiving, reasoning, and acting on underlying tasks <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This means they can process data, devise a plan based on a user query, and utilize tools, functions, or external systems to complete the task <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. Crucially, effective AI agents must also learn from user feedback, adapt to user preferences, and continuously refine themselves for greater accuracy and usefulness <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

## Challenges in Building and Scaling AI Agents

Building and scaling AI agents presents several difficulties <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>:
*   **Rapid Data Change** Enterprise data, including business intelligence, flows into systems constantly, leading to rapid data evolution <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   **Evolving Preferences** User preferences and customer needs are not static and change over time <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **High Inference Costs** Deploying large language models (LLMs) to support use cases can lead to high inference costs, where increased usage directly correlates with increased expense <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>.

These challenges highlight the need for a mechanism to keep agents relevant and cost-effective, which is where [[strategies_for_implementing_data_flywheels | data flywheels]] become essential <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.

## What are Data Flywheels?

A data flywheel is a continuous loop or cycle that encompasses data processing, curation, model customization, evaluation, and guardrailing for safer interactions <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. It integrates state-of-the-art Retrieval-Augmented Generation (RAG) pipelines with enterprise data to deliver relevant and accurate responses <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

As AI agents operate in production environments, the data flywheel cycle continuously curates ground truth data using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This process facilitates continuous experimentation and evaluation of both existing and newer models. The goal is to identify and surface efficient, smaller models that can provide comparable accuracy to larger LLMs but offer lower latency, faster inference, and a reduced total cost of ownership <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

## [[Nvidias AI and data flywheel tools | NVIDIA's Tools for Data Flywheels]]

NVIDIA offers Nemo microservices, an end-to-end platform designed to build powerful agentic and generative AI systems, as well as robust data flywheels around them <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. These services are exposed as simple API endpoints, making them easy to use <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. They can be run on-prem, in the cloud, in data centers, or even at the edge, with enterprise-grade stability and support <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

Key components of Nemo microservices include:
*   **Nemo Curator** Helps in curating high-quality training datasets, including multimodal data <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
*   **Nemo Customizer** Facilitates fine-tuning and customizing underlying models using state-of-the-art techniques such as LoRa, P-tuning, and full SFT <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Nemo Evaluator** Used to benchmark models against academic and institutional standards, and can also leverage LLMs as a judge <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Nemo Guardrails** Provides guardrail interactions to ensure privacy, security, and safety <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Nemo Retriever** Used to build state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## Sample Data Flywheel Architecture

A data flywheel architecture can be constructed by combining these Nemo microservices like Lego pieces <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. For example, in a customer service agent scenario:
1.  An end-user interacts with the agent's front end <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
2.  The interaction is guardrailed for safety <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
3.  A model, served as an NVIDIA NIM (NVIDIA Inference Microservice), powers the agent for optimized inference <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
4.  A data flywheel loop is set up to constantly curate data, store it in a Nemo data store, and use Nemo Customizer and Evaluator <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
5.  This triggers a continuous cycle of retraining and evaluation <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
6.  Once a model meets target accuracy, an IT admin or AI engineer can promote it to power the agent's use case <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.

## Case Study: NVIDIA's Internal NV-Info Agent

NVIDIA adopted a data flywheel for its internal NV-Info agent, an employee support agent that provides access to enterprise knowledge across various domains like HR, finance, IT, and product documentation <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.

The architecture for this agent involves:
1.  An employee submits a query to the agent, which is guardrailed for safety and secure interaction <a class="yt-timestamp" data-t="07:28:00">[07:28:00]</a>.
2.  A router agent, run by an LLM, orchestrates multiple underlying expert agents <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.
3.  Each expert agent specializes in a specific domain and is augmented with a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
4.  A data flywheel loop is set up to decide which models power these agents, building on user feedback and production data inference logs <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>.
5.  Ground truth data is continuously curated using subject matter experts and human-in-the-loop feedback <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
6.  Nemo Customizer and Evaluator are used to constantly evaluate models and promote the most effective one as an NIM to power the router agent <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.

### Router Agent Problem Statement and Solution

The core problem for the router agent is to accurately route a user query to the correct expert agent using a fast and cost-effective LLM <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. Initially, a 70B LLM variant achieved a 96% baseline accuracy in routing queries, but smaller variants (e.g., 8B) showed subpar accuracy (below 14%) <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>. While larger models offer higher accuracy, they come with higher latency and inference costs <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.

To address this, the data flywheel approach was implemented:
1.  The 70B Llama variant was deployed, and user feedback (satisfactory/unsatisfactory responses) from NVIDIA employees was collected <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.
2.  Out of 1,224 data points, 495 were unsatisfactory <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.
3.  Nemo Evaluator, using an LLM as a judge, investigated these unsatisfactory responses, identifying that 140 were due to incorrect routing <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.
4.  Further manual analysis with subject matter experts confirmed 32 queries were truly due to incorrect routing <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
5.  A ground truth dataset of 685 data points was created, split 60/40 for training/fine-tuning and testing/evaluation <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

Remarkably, with just 685 data points, fine-tuning smaller models yielded significant results <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. While the 70B variant offered 96% accuracy at 26 seconds latency, the 8B variant initially had 14% accuracy but much lower latency <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>. After fine-tuning, the 8B model was able to match the 70B variant's accuracy <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. Even the 1B variant achieved 94% accuracy, which is only 2% below the 70B <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

Deploying a smaller model like the 1B variant could lead to 98% savings in inference costs, a 70x model size reduction, and 70x lower latency <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>. This demonstrates the power of data flywheels in achieving high accuracy with smaller, more efficient models, continuously learning from production logs and knowledge <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

## [[Strategies for implementing data flywheels | Framework for Building Effective Data Flywheels]]

Building effective data flywheels involves a four-step framework:

1.  **Monitor User Feedback**
    *   Implement intuitive ways to collect user feedback signals, including explicit and implicit signals <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>.
    *   Monitor for model drift or inaccuracies in the agentic system <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>.

2.  **Analyze and Attribute Errors**
    *   Spend time analyzing and attributing errors or model drift to understand why the agent is behaving in a certain way <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>.
    *   Classify errors, attribute failures, and create ground truth datasets <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.

3.  **Plan**
    *   Identify different models and generate synthetic datasets for experimentation <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
    *   Fine-tune models and optimize resources and costs <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.

4.  **Execute**
    *   Trigger the data flywheel cycle <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
    *   Set up a regular cadence for tracking accuracy, latency, and performance <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
    *   Manage the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.