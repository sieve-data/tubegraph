---
title: Strategies for implementing data flywheels
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

AI agents are rapidly becoming integral digital employees within the workforce, taking various forms such as customer service, software security, and research agents <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. At their core, agents are systems designed to perceive, reason, and act on specific tasks, utilizing tools, functions, and external systems <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. What completes the cycle for effective AI agents is their ability to continuously learn from user feedback, preferences, and data, thereby refining themselves to be more accurate and useful over time <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This continuous learning and refinement process is enabled by [[understanding_data_flywheels | data flywheels]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Challenges in Building and Scaling AI Agents

Building and scaling AI agents presents several significant challenges <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>:
*   **Rapidly Changing Data**: Enterprise data and business intelligence continuously flow into systems <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Evolving User Preferences**: Customer needs and user preferences are constantly changing <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **High Inference Costs**: Deploying larger language models (LLMs) to support use cases can lead to increased inference costs, as increased usage drives higher expenses <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

These challenges highlight the necessity of [[understanding_data_flywheels | data flywheels]] <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## What are Data Flywheels?

A [[understanding_data_flywheels | data flywheel]] is a continuous loop or cycle that starts with enterprise data <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. It encompasses:
1.  **Data processing and curation** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
2.  **Model customization** <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>
3.  **Evaluation** <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>
4.  **Guardrailing** for safer interactions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>
5.  **Building state-of-the-art RAG pipelines** alongside enterprise data <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>

This cycle aims to provide relevant and accurate responses <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. As AI agents operate in production, the data flywheel continuously curates ground truth data using inference data, business intelligence, and user feedback <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This process allows for continuous experimentation and evaluation of existing and newer models, enabling the identification and promotion of efficient, smaller models that achieve accuracy comparable to larger LLMs but with lower latency, faster inference, and reduced total cost of ownership <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## [[Nvidias AI and data flywheel tools | NVIDIA's AI and Data Flywheel Tools]]

NVIDIA has developed [[nvidias_ai_and_data_flywheel_tools | Nemo microservices]] as an end-to-end platform for building powerful agentic and generative AI systems, including robust [[understanding_data_flywheels | data flywheels]] <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. These microservices offer various components for each stage of the data flywheel loop:
*   **Nemo Curator**: Helps curate high-quality training datasets, including multimodal data <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **Nemo Customizer**: Facilitates fine-tuning and customizing models using techniques like LoRa, P-tuning, and full SFT <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Nemo Evaluator**: Used for benchmarking on academic and institutional standards, as well as using LLMs as judges <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Nemo Retriever**: Aids in building state-of-the-art RAG pipelines <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

These microservices are exposed as simple API endpoints, allowing users to customize, evaluate, and guardrail LLMs with minimal calls <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. They offer deployment flexibility across on-premise, cloud, data center, and edge environments, with enterprise-grade stability and support <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Sample Data Flywheel Architecture

A typical [[designing_ai_networks_and_data_centers | data flywheel architecture]] leveraging [[nvidias_ai_and_data_flywheel_tools | Nemo microservices]] can be conceptualized as Lego pieces assembled to form a complete system <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. An end-user interacts with the front end of an agent (e.g., a customer service agent) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This interaction is guardrailed for safety, and the underlying model is served as an NVIDIA NIM for optimized inference <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

To determine the optimal model without compromising accuracy, a [[understanding_data_flywheels | data flywheel]] loop is established to:
*   Continuously curate data and store it in a data store <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   Use Nemo Customizer and Evaluator to trigger continuous retraining and evaluation <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   Once a model meets target accuracy, IT administrators or AI engineers can promote it to power the agentic use case as the underlying NIM <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Real-World Case Study: NVIDIA's NV Info Agent

NVIDIA adopted and built a [[understanding_data_flywheels | data flywheel]] for its internal employee support agent, "NV Info Agent," which provides access to enterprise knowledge across various domains like HR benefits, financial earnings, IT help, and product documentation <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

### Architecture of the NV Info Agent's Data Flywheel

When an employee submits a query, it is guardrailed for safety <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. A router agent, orchestrated by an LLM, routes the query to one of multiple expert agents <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Each expert agent specializes in a specific domain and is augmented with a RAG pipeline to fetch relevant information <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

To select and power these expert models, a data loop is set up that builds on user feedback and production data inference logs <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Ground truth data is continuously curated using subject matter experts and human-in-the-loop feedback <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Nemo Customizer and Evaluator are used to continually assess multiple models and promote the most effective one as a NIM to power the router agent <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Optimizing the Router Agent

The problem statement for the router agent was to accurately route user queries to the correct expert agent using a fast and cost-effective LLM <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   Initial deployment of a 70B variant LLM showed a 96% baseline accuracy in routing but had a latency of 26 seconds to generate the first token response <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   Smaller 8B variants showed subpar accuracy (below 14%) without fine-tuning <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

Many enterprises mistakenly choose larger models solely based on initial high accuracy <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. However, [[understanding_data_flywheels | data flywheels]] enable significant improvements for smaller models <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

### Data Flywheel in Action: The Results

1.  **Feedback Collection**: A feedback form was circulated among NVIDIA employees to capture user feedback on query usefulness <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
2.  **Data Curation**: 1,224 data points were curated, with 729 satisfactory and 495 unsatisfactory responses <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
3.  **Error Analysis**: Nemo Evaluator, using LLM as a judge, investigated the 495 unsatisfactory responses, identifying 140 due to incorrect routing <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. Further manual analysis with subject matter experts confirmed 32 actual incorrect routings <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
4.  **Ground Truth Dataset**: A ground truth dataset of 685 data points was established, split 60/40 for training/fine-tuning and testing/evaluation <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

**The Results**: With just 685 data points and the [[understanding_data_flywheels | data flywheel]] setup, the results were outstanding <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>:
*   The 70B variant maintained 96% accuracy but with 26 seconds latency <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   The 8B variant, initially 14% accurate, after fine-tuning, was able to match the 70B variant's accuracy <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   A 1B variant achieved 94% accuracy, only 2% below the 70B model <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

This demonstrates that by deploying a 1B model, significant savings can be achieved:
*   **98% lower inference cost** <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>
*   **10x-70x model size reduction** <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>
*   **70x lower latency** <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>

The power of data flywheels lies in building an automated, continuous cycle of periodic evaluation and fine-tuning, allowing smaller models to replace larger ones in production while continuously learning from ongoing production logs and knowledge <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

## Framework for Building Effective Data Flywheels

To build effective [[understanding_data_flywheels | data flywheels]], consider the following framework <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>:

### 1. Monitor User Feedback
*   Implement intuitive ways to collect user feedback signals <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   Consider intuitive user experience, privacy compliance, and both implicit and explicit signals <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   This helps identify model drift or inaccuracies in the agentic system <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### 2. Analyze and Attribute Errors
*   Spend time analyzing and attributing errors or model drift to understand why the agent behaves a certain way <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   Classify errors, attribute failures, and create ground truth datasets <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

### 3. Plan for Improvement
*   Identify different models for experimentation <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   Generate synthetic datasets and fine-tune models <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.
*   Optimize resource utilization and cost <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### 4. Execute the Plan
*   Trigger the [[understanding_data_flywheels | data flywheel]] cycle <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
*   Establish a regular cadence and mechanism to track accuracy, latency, and performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   Monitor production logs and manage the end-to-end GenAI Ops pipeline <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

By implementing these [[strategies_for_effective_ai_implementation | strategies for effective AI implementation]], organizations can build resilient AI workflows and ensure their agents remain relevant and efficient.