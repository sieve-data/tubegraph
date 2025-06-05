---
title: Building effective AI agents
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

To [[building_effective_agents | build effective AI agents]] that remain relevant and helpful over time, the focus should not be on simply powering them with the next biggest Large Language Model (LLM) <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Instead, they require simple data flywheels <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This article explores what data flywheels are, how they were applied to an internal agent at NVIDIA, lessons learned, and a framework for building data flywheels for AI agent use cases <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## What Are AI Agents?
AI agents are currently generating significant buzz and are beginning to integrate into the workforce as new digital employees <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. They manifest in various forms and sizes depending on their specific use case, such as customer service agents, software security agents, or research agents <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Fundamentally, agents are systems capable of perceiving, reasoning, and acting on an underlying task <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. This means they can analyze data, formulate a reasonable plan to address a user query, and utilize tools, functions, and external systems to complete the task <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. A complete cycle for AI agents involves capturing and learning from user feedback, continuously refining themselves based on user preferences and data to become more accurate and useful <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## [[challenges_in_ai_agent_development | Challenges in AI Agent Development]]
[[building_effective_agents | Building effective agents]] can be difficult, and scaling them presents increasing [[technical_challenges_in_ai_agent_development | technical challenges in AI agent development]] <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Key challenges include:
*   **Rapid Data Change**: Enterprise data, such as business intelligence, flows into systems constantly <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Evolving User Preferences**: User preferences and customer needs are always changing <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Increased Inference Cost**: Deploying larger, "chunkier" language models to support use cases drives up inference costs <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Greater usage directly leads to higher costs <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Data Flywheels: The Solution
Data flywheels are a continuous loop or cycle of data processing and curation <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. They involve:
1.  Model customization <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
2.  Evaluation <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
3.  Guardrailing for safer interactions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
4.  Building state-of-the-art Retrieval-Augmented Generation (RAG) pipelines alongside enterprise data to provide relevant and accurate responses <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

As AI agents operate in production environments, this data flywheel cycle continuously curates ground truth data using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This process enables continuous experimentation and evaluation of existing and newer models to identify efficient, smaller models that provide comparable accuracy to larger models but offer lower latency, faster inference, and reduced total cost of ownership <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## NVIDIA Nemo Microservices
NVIDIA has announced Nemo Microservices, an end-to-end platform designed to [[building_effective_agents | build effective agents]] and generative AI systems, as well as powerful data flywheels around them <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Nemo Microservices offer various components for each stage of the data flywheel loop:
*   **Nemo Curator**: Helps curate high-quality training datasets, including multimodal data <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Nemo Customizer**: Facilitates fine-tuning and customizing underlying models using state-of-the-art techniques like LoRa, Ptuning, and full SFT <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Nemo Evaluator**: Used for benchmarking on academic and institutional benchmarks, as well as using LLMs as judges <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Nemo Retriever**: Enables building state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

These microservices are exposed as simple-to-use API endpoints, allowing users to customize, evaluate, and guardrail large language models with just a few API calls <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. They offer flexibility to run on-prem, in the cloud, on data centers, or even at the edge, with enterprise-grade stability and support from NVIDIA <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Sample Data Flywheel Architecture
A data flywheel architecture can be constructed using Nemo Microservices like Lego pieces <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. In a typical setup, an end-user interacts with the front end of an agent (e.g., a customer service agent) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This interaction is guardrailed for safety, and on the back end, a model served as an NVIDIA NIM (NVIDIA Inference Microservice) provides optimized inference <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

To identify the optimal model without compromising accuracy, a data flywheel loop is established to continuously curate data, store it in a Nemo data store, and use Nemo Customizer and Evaluator to trigger continuous retraining and evaluation <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Once a model meets the target accuracy, an IT admin or AI engineer can promote it to power the agent's use case as the underlying NVIDIA NIM <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

## Real-World Case Study: NVInfo Agent
NVIDIA adopted and built this data flywheel for their NVInfo agent, an internal employee support agent <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. This agent assists NVIDIA employees with access to enterprise knowledge across various domains, acting as a customer service or employee support chatbot <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. It can answer queries spanning HR benefits, financial earnings, IT help, product documentation, and other internal employee needs <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

The NVInfo agent's data flywheel architecture involves an employee submitting a query, which is guardrailed for safety <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. A crucial router agent, orchestrated by an LLM, manages multiple underlying expert agents <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Each expert agent specializes in a specific domain and is augmented with a RAG pipeline to retrieve relevant information <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

To determine which models power these expert agents, a data flywheel loop is set up <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This loop continuously builds upon user feedback and production data inference logs generated when the router is active <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. Using subject matter experts and human-in-the-loop feedback, ground truth data is curated <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Nemo Customizer and Evaluator then continuously evaluate multiple models to promote the most effective one as an NIM to power the router agent <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Router Agent Optimization
The router agent's core problem is to accurately route a user query to the correct expert agent using a fast and cost-effective LLM <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Initial comparisons of various models to power the router agent revealed that a 70B variant achieved a 96% baseline accuracy for query routing without any fine-tuning <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. In contrast, smaller variants, like the 8B model, showed subpar accuracy, falling below 14% <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

The common misconception in enterprise evaluations is to solely rely on larger models due to their higher initial accuracy <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. However, this is precisely where data flywheels provide a significant advantage <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

NVIDIA employees were asked to submit queries and provide feedback on the usefulness of the responses generated by the 70B variant <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. This process curated 1,224 data points, with 729 satisfactory and 495 unsatisfactory responses <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. Using Nemo Evaluator and an LLM as a judge, 495 unsatisfactory responses were investigated <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. It was found that 140 were due to incorrect routing, and further manual analysis by subject matter experts confirmed 32 were truly due to this <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

A ground truth dataset of 685 data points was created, split 60/40 for training (fine-tuning smaller models) and testing/evaluation <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. The results, achieved with only 685 data points, were outstanding, a testament to the data flywheel setup <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

While the 70B variant offered 96% accuracy with a latency of 26 seconds to generate the first token, the 8B variant initially had 14% accuracy but 70% lower latency <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>. After fine-tuning, the 8B model was able to match the 70B variant's accuracy <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Even the 1B variant achieved 94% accuracy, just 2% below the 70B model <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

This demonstrates a trade-off between accuracy and cost/resource management <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Deploying a 1B model, for example, could result in 98% savings in lower inference costs, a 70x model size reduction, and 70x lower latency <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. This is the power of data flywheels: an automated loop for continuous evaluation and fine-tuning, leveraging production logs and knowledge to train smaller, more efficient models that can replace larger ones <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

## [[best_practices_for_building_ai_agents | Best Practices for Building AI Agents]]: A Framework for Data Flywheels
To [[building_effective_agents | build effective agents]] and data flywheels, consider this four-step framework:

### 1. Monitor User Feedback
Focus on intuitive ways to collect user feedback signals <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This includes intuitive user experience, privacy compliance, and both implicit and explicit signals to detect model drift or inaccuracies in the agentic system <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

### 2. Analyze & Attribute Errors
Spend time analyzing and attributing errors or model drift to understand why the agent is behaving a certain way <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. Classify these errors, attribute failures, and create a ground truth data set for subsequent steps <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

### 3. Plan
Identify different models, generate synthetic datasets, experiment with them, fine-tune them, and optimize resources and costs <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

### 4. Execute
Execution involves not only triggering a data flywheel cycle but also establishing a regular cadence or mechanism to track accuracy, latency, and monitor performance in production logs <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. This effectively manages the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.

This framework provides a robust approach for [[best_practices_for_building_ai_agents | best practices for building AI agents]] and their data flywheels <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.