---
title: NVIDIAs Nemo microservices for generative AI
videoId: 6lTxD_oUjXQ
---

From: [[aidotengineer]] <br/> 

NVIDIA's Nemo microservices provide an end-to-end platform designed to build powerful agentic and [[generative_ai_project_challenges_and_strategies | generative AI systems]], along with the "data flywheels" necessary to maintain their relevance and helpfulness over time [00:03:57]. These services are exposed as simple API endpoints, allowing for easy customization, evaluation, and guardrailing of large language models with minimal calls [00:05:02]. They offer deployment flexibility, running on-premises, in the cloud, in data centers, or at the edge, and come with enterprise-grade stability and support [00:05:14].

## Understanding AI Agents and Their Challenges

AI agents are generating significant interest and are emerging as new digital employees in various forms, including customer service, software security, and research agents [00:00:48]. By definition, agents are systems capable of perceiving, reasoning, and acting on underlying tasks [00:01:12]. They analyze data, formulate plans, and utilize tools and external systems to achieve user queries [00:01:20]. A crucial aspect that completes the AI agent cycle is their ability to capture and learn from user feedback, continuously refining themselves for improved accuracy and utility [00:01:38].

However, [[building_scalable_ai_systems | building and scaling agents]] presents significant [[challenges_in_scaling_generative_ai | challenges]] [00:01:56]. Data changes rapidly, especially for enterprise customers, with new business intelligence constantly flowing in [00:02:04]. User preferences and customer needs also evolve [00:02:16]. Furthermore, deploying larger, chunkier large language models (LLMs) can lead to high inference costs, where increased usage directly drives increased cost [00:02:20].

## The Role of Data Flywheels

Data flywheels are continuous loops or cycles that help AI agents stay relevant and cost-effective [00:00:21, 00:02:38]. They start with enterprise data and involve a continuous process of:
*   **Data processing and curation** [00:02:44]
*   **Model customization** [00:02:48]
*   **Evaluation** [00:02:50]
*   **Guardrailing** for safer interactions [00:02:52]
*   **Building state-of-the-art RAG (Retrieval Augmented Generation) pipelines** alongside enterprise data to provide relevant and accurate responses [00:02:54]

As AI agents operate in production, this data flywheel cycle triggers a continuous curation of ground truth data using inference data, business intelligence, and user feedback [00:03:07]. This allows for continuous experimentation and [[evaluating_generative_ai_workloads | evaluation]] of existing and newer models [00:03:20]. The goal is to identify efficient, smaller models that can deliver accuracy comparable to larger LLMs while offering lower latency, faster inference, and a reduced total cost of ownership [00:03:26].

## Nemo Microservices Components

Nemo microservices are designed to support each stage of the data flywheel loop [00:04:07]:

*   **Nemo Curator**: Aids in curating high-quality training datasets, including multimodal data [00:04:13].
*   **Nemo Customizer**: Facilitates fine-tuning and customizing models using advanced techniques like LoRa, Ptuning, and full SFT [00:04:21].
*   **Nemo Evaluator**: Used for benchmarking models against academic and institutional standards, and for using LLMs as judges [00:04:37].
*   **Nemo Guardrails**: Provides guardrail interactions for privacy, security, and safety [00:04:47].
*   **Nemo Retriever**: Enables the construction of state-of-the-art RAG pipelines [00:04:51].

## Sample Data Flywheel Architecture

A typical data flywheel architecture leveraging Nemo microservices involves an end-user interacting with an agent's front end, which is guarded for safe interactions [00:05:43]. The backend model is served as an NVIDIA NIM (NVIDIA Inference Microservice) for optimized inference [00:05:58].

To determine the optimal model for a use case without compromising accuracy, a data flywheel loop can be established [00:06:02]. This loop constantly curates data, stores it in a Nemo data store, and uses Nemo Customizer and Evaluator to trigger continuous retraining and evaluation cycles [00:06:09]. Once a model meets the desired accuracy targets, an IT administrator or AI engineer can promote it to power the agentic use case [00:06:26].

## Case Study: NVIDIA's NV-Info Agent

A [[case_study_on_ai_agent_development_at_nvidia | real-world case study]] demonstrates the application of this data flywheel for NVIDIA's internal NV-Info agent [00:06:42]. This agent serves as an employee support chatbot, providing access to enterprise knowledge across various domains such as HR benefits, financial earnings, IT help, and product documentation [00:06:47].

### Architecture of NV-Info Agent

The NV-Info agent's data flywheel architecture involves an employee submitting a query, which is then guardrailed for safety [00:07:28]. An LLM-powered router agent orchestrates multiple underlying expert agents [00:07:37]. Each expert agent specializes in a specific domain and is augmented with a RAG pipeline to fetch relevant information [00:07:47].

A data flywheel loop is set up to determine which models power these expert agents [00:08:03]. This loop continuously builds upon user feedback and production data inference logs [00:08:12]. Ground truth data is curated using subject matter experts and human-in-the-loop feedback [00:08:20]. Nemo Customizer and Evaluator are used to evaluate multiple models and promote the most effective one as an NIM to power the router agent [00:08:27].

### Optimizing the Router Agent

The problem statement for the router agent was to accurately and cost-effectively route user queries to the correct expert agent [00:09:27]. Initial comparisons of various LLM variants revealed a baseline accuracy of 96% for a 70B variant (without fine-tuning) [00:09:56]. However, smaller variants like the 8B model showed subpar accuracy, below 14% [00:10:24]. Many enterprises might conclude that a larger model is necessary based on such initial evaluations [00:10:33].

This is where data flywheels provide a solution [00:10:57]. By circulating a feedback form among NVIDIA employees after running the 70B variant, 1,224 data points were collected [00:11:02]. Of these, 495 were unsatisfactory responses [00:11:34]. Using Nemo Evaluator with LLM as a judge, 140 of these were identified as due to incorrect routing [00:11:44]. Further manual analysis by subject matter experts narrowed this down to 32 truly misrouted queries [00:11:58].

This led to the creation of a ground truth dataset of just 685 data points [00:12:09], split 60/40 for training/fine-tuning and testing [00:12:16]. Surprisingly, with this small dataset, significant improvements were achieved [00:12:27]:

| Model Variant | Initial Accuracy | Latency (to first token) | Fine-tuned Accuracy (with data flywheel) | Inference Cost Savings (vs. 70B) | Model Size Reduction (vs. 70B) | Latency Reduction (vs. 70B) |
| :------------ | :--------------- | :----------------------- | :--------------------------------------- | :--------------------------------- | :------------------------------- | :----------------------------- |
| 70B           | 96%              | 26 seconds               | N/A                                      | -                                  | -                                | -                              |
| 8B            | <14%             | 70% lower                | Comparable to 70B                        | High                               | Significant                    | Significant                    |
| 1B            | N/A              | N/A                      | 94%                                      | 98%                                | 10x - 70x                        | 70x                            |

*Note: While the 70B had 96% accuracy, its latency was 26 seconds [00:12:39]. The 8B, after fine-tuning, was able to match the 70B's accuracy, with significantly lower latency [00:13:11]. The 1B variant, after fine-tuning, achieved 94% accuracy, only 2% below the 70B, but with 98% savings in inference cost, 10x-70x model size reduction, and 70x lower latency [00:13:22, 00:13:44].*

This demonstrates the power of data flywheels in allowing smaller models to achieve comparable accuracy to larger ones, leading to substantial savings in inference cost and lower latency [00:13:56]. It also highlights the potential for automated, continuous evaluation and fine-tuning as new models emerge, enabling the replacement of larger, more expensive models with efficient, smaller ones in production [00:14:02].

## Framework for Building Effective Data Flywheels

To build effective data flywheels, consider the following framework [00:14:43]:

1.  **Monitor User Feedback**: Implement intuitive ways to collect user feedback signals, including implicit and explicit signals, to identify model drift or inaccuracies [00:14:50].
2.  **Analyze and Attribute Errors**: Spend time analyzing and attributing errors or model drift to understand why the agent is behaving a certain way [00:15:14]. Classify failures and create ground truth datasets [00:15:23].
3.  **Plan**: Identify different models, generate synthetic datasets, experiment with them, fine-tune them, and optimize resource and cost considerations [00:15:34].
4.  **Execute**: Trigger the data flywheel cycle and establish a regular cadence or mechanism to track accuracy, latency, and performance [00:15:48]. This involves managing the entire GenAI Ops pipeline [00:16:08].

By following this framework and utilizing tools like Nemo microservices and NVIDIA NIM, organizations can effectively build and manage [[ai_transcription_model_development_at_nvidia | AI agents]] that continuously learn, adapt, and remain relevant and cost-efficient [00:16:17, 00:16:30].