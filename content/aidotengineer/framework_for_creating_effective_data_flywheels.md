---
title: Framework for creating effective data flywheels
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

Effective [[building_ai_agents_using_data_flywheels | AI agents]] that remain relevant and helpful over time are not solely dependent on the largest available Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>. Instead, they require simple [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a>. This article explores what [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] are, how they can be applied, and a framework for building them <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

## What are AI Agents?

[[building_ai_agents_using_data_flywheels | AI agents]] are systems capable of perceiving, reasoning, and acting on underlying tasks <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. They process data, devise reasonable plans for user queries, and utilize tools, functions, and external systems <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. A complete agent cycle involves capturing and learning from user feedback, preferences, and data, continuously refining themselves for accuracy and usefulness <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. [[building_ai_agents_using_data_flywheels | AI agents]] are emerging as new digital employees in various forms, such as customer service, software security, and research agents <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

## Challenges in Building and Scaling AI Agents

Building and scaling [[building_ai_agents_using_data_flywheels | AI agents]] can be challenging <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. Key difficulties include:
*   **Rapidly changing data**: Enterprise systems constantly receive new data and business intelligence <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   **Evolving user preferences**: Customer needs and user preferences change over time <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.
*   **Increased inference cost**: Deploying larger LLMs leads to higher inference costs, as increased usage drives up expenses <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

## How Data Flywheels Help

[[data_flywheels_and_their_importance_in_ai_agents | Data flywheels]] offer a solution to these challenges <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. At its core, a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] is a continuous loop of data processing, curation, model customization, evaluation, and guardrailing <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. It integrates state-of-the-art RAG (Retrieval Augmented Generation) pipelines with enterprise data to provide accurate responses <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

As [[building_ai_agents_using_data_flywheels | AI agents]] operate in production, this cycle is triggered, leading to:
*   **Continuous data curation**: Ground truth data is curated using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>.
*   **Model evaluation and selection**: Existing and newer models are continuously experimented with and evaluated <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.
*   **Efficiency**: The process aims to surface smaller, more efficient models that match the accuracy of larger models but offer lower latency, faster inference, and a [[costeffective_solutions_for_data_processing | lower total cost of ownership]] <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

### NVIDIA Nemo Microservices

NVIDIA offers Nemo microservices, an end-to-end platform for building powerful [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agentic]] and generative AI systems, including [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. These microservices are exposed as simple API endpoints and include components for each stage of the data flywheel loop:
*   **Nemo Curator**: Curates high-quality training data, including multimodal data <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
*   **Nemo Customizer**: Fine-tunes and customizes models using techniques like LoRa, P-tuning, and full SFT <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Nemo Evaluator**: Benchmarks models against academic and institutional benchmarks, and can use LLMs as judges <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Nemo Retriever**: Builds state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

These microservices offer flexibility, allowing deployment on-prem, in the cloud, in data centers, or at the edge <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

## Case Study: NVIDIA NVInfo Agent

NVIDIA built a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] for their internal NVInfo agent, an employee support agent that provides access to enterprise knowledge across various domains, such as HR benefits, financial earnings, and IT help <a class="yt-timestamp" data-t="06:45:00">[06:45:00]</a>.

### Router Agent Problem

The NVInfo agent architecture features a main router agent, orchestrated by an LLM, that routes employee queries to multiple underlying expert agents <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>. Each expert agent specializes in a specific domain and uses a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. The problem was to accurately route user queries to the correct expert agent using a fast and [[costeffective_solutions_for_data_processing | cost-effective]] LLM <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.

### Initial Model Comparison and Data Curation

Initially, a 70B variant of an LLM achieved 96% baseline accuracy in routing queries <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. However, smaller variants like the 8B model showed subpar accuracy, below 14% <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

To improve smaller models, a feedback loop was implemented:
1.  The 70B Llama variant was used in production <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.
2.  NVIDIA employees submitted queries, and feedback was collected on whether responses were useful <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>.
3.  1,224 data points were curated, with 729 satisfactory and 495 unsatisfactory responses <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.
4.  Nemo Evaluator, with an LLM as a judge, investigated the unsatisfactory responses <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.
5.  140 errors were attributed to incorrect routing, and further manual analysis by subject matter experts confirmed 32 were truly due to this <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
6.  A ground truth dataset of 685 data points was created, split 60/40 for training/fine-tuning and testing/evaluation <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.

### Results

With only 685 data points and the [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] setup, the results were significant:
*   The 70B variant had 96% accuracy but a latency of 26 seconds to generate the first token <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.
*   The 8B variant initially had 14% accuracy but much lower latency <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.
*   After fine-tuning, the 8B model was able to match the accuracy of the 70B variant <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.
*   Even the 1B variant achieved 94% accuracy, only 2% below the 70B model <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

Deploying a 1B model resulted in 98% savings in [[costeffective_solutions_for_data_processing | lower inference cost]], a 70x model size reduction, and 70x lower latency <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>. This demonstrates the power of a [[data_flywheels_and_their_importance_in_ai_agents | data flywheel]] in continuously learning from production logs and surfacing smaller, more efficient models to replace larger ones <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.

## Framework for Building Effective Data Flywheels

Building effective [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] involves a four-step framework:

### 1. Monitor User Feedback
Start by establishing intuitive ways to collect user feedback signals <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>. This includes:
*   **Intuitive user experience**: Making it easy for users to provide feedback <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>.
*   **Privacy compliance**: Ensuring feedback collection adheres to privacy standards <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
*   **Implicit and explicit signals**: Gathering both indirect (e.g., usage patterns) and direct (e.g., ratings, comments) feedback <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
This helps understand if the agent's models are experiencing model drift or inaccuracies <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

### 2. Analyze and Attribute Errors
Dedicate time to analyze and attribute the errors or model drift observed <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>.
*   **Classify errors**: Categorize the types of inaccuracies <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.
*   **Attribute failures**: Determine the root causes of the agent's undesirable behavior <a class="yt-timestamp" data-t="15:23:00">[15:23:00]</a>.
*   **Create ground truth data**: Develop a high-quality ground truth dataset from the analysis, which will be used in subsequent steps <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>.

### 3. Plan
This stage involves strategizing the improvements based on the analyzed data <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
*   **Identify different models**: Determine which models could be used or experimented with <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.
*   **Generate synthetic data sets**: Create additional data points to augment training <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **Experiment and fine-tune**: Test different approaches and fine-tune models using the curated data <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.
*   **Optimize resource and cost**: Plan for efficient resource allocation and cost management <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.

### 4. Execute
The final step is to put the plan into action and manage the ongoing process <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>.
*   **Trigger data flywheel cycle**: Initiate the continuous process of data curation, model training, and evaluation <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.
*   **Set up regular cadence**: Establish a routine for tracking accuracy, latency, and performance <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
*   **Monitor production logs**: Continuously monitor the agent's behavior in production <a class="yt-timestamp" data-t="16:02:00">[16:02:00]</a>.
*   **Manage end-to-end GenAI Ops pipeline**: Oversee the entire pipeline for generative AI operations <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>.

This framework provides a structured approach to building effective [[data_flywheels_and_their_importance_in_ai_agents | data flywheels]] for [[building_ai_agents_using_data_flywheels | AI agents]] <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>.