---
title: Techniques and patterns in AI orchestration and prompt engineering
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 
The success of AI products in production hinges not just on the models themselves, but on how systems are built and orchestrated around them <a class="yt-timestamp" data-t="04:15:15">[04:15:15]</a>. This involves evolving [[evolution_of_ai_engineering_and_tools | techniques and patterns]] for orchestrating models, syncing with data, and ensuring effective production <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Evolution of AI Engineering and Orchestration
In 2023, while many built "AI wrappers," the notion of defensibility was often questioned <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. However, the rapid growth of AI-powered tools like Cursor AI demonstrates that significant advancements have occurred <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. This progress is due to models improving at coding, increased AI adoption, and the development of new [[agent_frameworks_and_orchestration_layers_in_ai_engineering | techniques and patterns]] for orchestrating models <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Why Orchestration Techniques are Essential
Despite model advancements, fundamental limitations persist:
*   **Hallucinations** are still a concern <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Overfitting** remains a problem <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   Developers require more structured outputs <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   The "big jumps" in model performance, like between GPT-3.5 and GPT-4, have slowed down <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Models reached limits on existing tests, suggesting that making models bigger and adding more data hit a wall <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

New training methods, such as real reinforcement learning (e.g., DeepSeek R1 model trained without labeled data), have pushed the field forward <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Reasoning models (e.g., OpenAI's 01 and 03) utilize Chain of Thought thinking at inference time, allowing them to "think" before responding and solve complex reasoning problems <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Model providers are also adding more capabilities, such as tool use and near-perfect OCR accuracy (Gemini 2.0 Flash) <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. However, traditional benchmarks are saturated, leading to the introduction of new, more difficult benchmarks like the Humanities Last Last Exam <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Key Techniques and Patterns in AI Orchestration
Parallel to model training, [[evolution_of_ai_engineering_and_tools | AI engineering]] has developed various techniques to build robust systems:
*   **Prompting Techniques**: Learning how to prompt models better, leading to advanced techniques like [[effective_design_of_ai_in_products | Chain of Thought]] <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
*   **Retrieval Augmented Generation (RAG)**: Grounding model responses with proprietary data became crucial <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Memory**: Essential for multi-threaded conversations to capture context <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Long Context Models**: Enabled new use cases due to extended context windows <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Graph RAG**: Experimenting with hierarchical responses <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Reasoning Models**: Utilizing models that take more time to think in real-time, opening new development areas <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.
*   **Agentic RAG**: Making workflows more powerful and autonomous <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Test-Driven Development for Reliable AI Products
To build AI products that truly work in production, a deep understanding of the problem and a [[best_practices_for_building_ai_systems | test-driven development]] (TDD) approach are essential <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. The [[best_practices_for_building_ai_systems | best AI teams]] follow a structured approach involving experimentation, evaluation, deployment, and continuous improvement <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

### Stages of Test-Driven AI Development

#### 1. Experimentation
Before building production-grade solutions, extensive experimentation is needed to prove if AI models can solve a specific use case <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Prompting Techniques**: Try different approaches like few-shot or [[effective_design_of_ai_in_products | Chain of Thought]] prompting. Some work well for simple tasks, others for complex reasoning <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   **Workflow Techniques**: Test prompt chaining (splitting instructions into multiple prompts) or agentic workflows (e.g., ReAct, which involves planning, reasoning, and refining) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.
*   **Domain Experts**: Involve domain experts early to tweak prompts and save engineering time, ensuring the solution addresses the actual problem <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.
*   **Model Agnosticism**: Incorporate and test different models to identify which ones perform best for specific use cases (e.g., Gemini 2.0 Flash for OCR) <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

#### 2. Evaluation
Once initial proofs of concept are established, evaluation ensures scalability and reliability in production <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Data Set Creation**: Create a dataset of hundreds of examples to test models and workflows against <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **Trade-offs**: Balance quality, cost, latency, and privacy. Define priorities early, as no AI system perfectly achieves all <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. For example, high quality might sacrifice speed, or cost-critical applications might use lighter, cheaper models <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **Ground Truth Data**: Use ground truth data designed by subject matter experts to evaluate workflows <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. Synthetic benchmarks are helpful but don't fully capture real-world use case performance <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.
*   **LLM as Evaluator**: If ground truth data is unavailable, an LLM can reliably evaluate another model's response <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Flexible Testing Framework**: Use a framework that is dynamic and customizable to handle non-deterministic responses, define custom metrics, and allow scripting in languages like Python or TypeScript <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Multi-Stage Evaluation**: Run evaluations at every stage, including internal nodes of the workflow, to ensure correctness and test during prototyping and with real data <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

#### 3. Deployment
Deployment requires careful monitoring and robust infrastructure <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
*   **Monitoring**: Log all LLM calls, track inputs, outputs, and latency.The success of AI products in production hinges not just on the models themselves, but on how systems are built and orchestrated around them <a class="yt-timestamp" data-t="04:15:15">[04:15:15]</a>. This involves evolving [[evolution_of_ai_engineering_and_tools | techniques and patterns]] for orchestrating models, syncing with data, and ensuring effective production <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Evolution of AI Engineering and Orchestration
In 2023, while many built "AI wrappers," the notion of defensibility was often questioned <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. However, the rapid growth of AI-powered tools like Cursor AI demonstrates that significant advancements have occurred <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>. This progress is due to models improving at coding, increased AI adoption, and the development of new [[agent_frameworks_and_orchestration_layers_in_ai_engineering | techniques and patterns]] for orchestrating models <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

### Why Orchestration Techniques are Essential
Despite model advancements, fundamental limitations persist:
*   **Hallucinations** are still a concern <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Overfitting** remains a problem <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   Developers require more structured outputs <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   The "big jumps" in model performance, like between GPT-3.5 and GPT-4, have slowed down <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Models reached limits on existing tests, suggesting that making models bigger and adding more data hit a wall <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

New training methods, such as real reinforcement learning (e.g., DeepSeek R1 model trained without labeled data), have pushed the field forward <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. Reasoning models (e.g., OpenAI's 01 and 03) utilize [[effective_design_of_ai_in_products | Chain of Thought]] thinking at inference time, allowing them to "think" before responding and solve complex reasoning problems <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Model providers are also adding more capabilities, such as tool use and near-perfect OCR accuracy (Gemini 2.0 Flash) <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. However, traditional benchmarks are saturated, leading to the introduction of new, more difficult benchmarks like the Humanities Last Last Exam <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Key Techniques and Patterns in AI Orchestration
Parallel to model training, [[evolution_of_ai_engineering_and_tools | AI engineering]] has developed various techniques to build robust systems:
*   **Prompting Techniques**: Learning how to prompt models better, leading to advanced techniques like [[effective_design_of_ai_in_products | Chain of Thought]] <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
*   **Retrieval Augmented Generation (RAG)**: Grounding model responses with proprietary data became crucial <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Memory**: Essential for multi-threaded conversations to capture context <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Long Context Models**: Enabled new use cases due to extended context windows <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Graph RAG**: Experimenting with hierarchical responses <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.
*   **Reasoning Models**: Utilizing models that take more time to think in real-time, opening new development areas <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>.
*   **Agentic RAG**: Making workflows more powerful and autonomous <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Test-Driven Development for Reliable AI Products
To build AI products that truly work in production, a deep understanding of the problem and a [[best_practices_for_building_ai_systems | test-driven development]] (TDD) approach are essential <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. The [[best_practices_for_building_ai_systems | best AI teams]] follow a structured approach involving experimentation, evaluation, deployment, and continuous improvement <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

### Stages of Test-Driven AI Development

#### 1. Experimentation
Before building production-grade solutions, extensive experimentation is needed to prove if AI models can solve a specific use case <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Prompting Techniques**: Try different approaches like few-shot or [[effective_design_of_ai_in_products | Chain of Thought]] prompting. Some work well for simple tasks, others for complex reasoning <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>.
*   **Workflow Techniques**: Test prompt chaining (splitting instructions into multiple prompts) or agentic workflows (e.g., ReAct, which involves planning, reasoning, and refining) <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.
*   **Domain Experts**: Involve domain experts early to tweak prompts and save engineering time, ensuring the solution addresses the actual problem <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>.
*   **Model Agnosticism**: Incorporate and test different models to identify which ones perform best for specific use cases (e.g., Gemini 2.0 Flash for OCR) <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

#### 2. Evaluation
Once initial proofs of concept are established, evaluation ensures scalability and reliability in production <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Data Set Creation**: Create a dataset of hundreds of examples to test models and workflows against <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **Trade-offs**: Balance quality, cost, latency, and privacy. Define priorities early, as no AI system perfectly achieves all <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. For example, high quality might sacrifice speed, or cost-critical applications might use lighter, cheaper models <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **Ground Truth Data**: Use ground truth data designed by subject matter experts to evaluate workflows <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. Synthetic benchmarks are helpful but don't fully capture real-world use case performance <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.
*   **LLM as Evaluator**: If ground truth data is unavailable, an LLM can reliably evaluate another model's response <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>.
*   **Flexible Testing Framework**: Use a framework that is dynamic and customizable to handle non-deterministic responses, define custom metrics, and allow scripting in languages like Python or TypeScript <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Multi-Stage Evaluation**: Run evaluations at every stage, including internal nodes of the workflow, to ensure correctness and test during prototyping and with real data <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.

#### 3. Deployment
Deployment requires careful monitoring and robust infrastructure <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
*   **Monitoring**: Log all LLM calls, track inputs, outputs, and latency. Since AI models are unpredictable, detailed monitoring is crucial for debugging and understanding behavior at every step, especially with [[agent_frameworks_and_orchestration_layers_in_ai_engineering | agentic workflows]] <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.
*   **API Reliability**: Implement retries and fallback logic to maintain stability and prevent outages (e.g., switching models if one API is down) <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>.
*   **Version Control and Staging**: Always deploy in controlled environments before public rollout to prevent regressions when updating prompts or workflows <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>.
*   **Decoupled Deployments**: Decouple AI feature deployments from the main app deployment schedule, as AI features often require more frequent updates <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.

#### 4. Continuous Improvement
After deployment, the work continues by capturing user feedback and refining the system <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.
*   **Feedback Loop**: Capture user responses to identify edge cases in production and continuously improve workflows <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. Rerun evaluations with this new data to test solutions for identified issues <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.
*   **Caching Layer**: Implement caching for repeat queries to drastically reduce costs and improve latency by storing and serving frequent responses instantly instead of calling expensive LLMs repeatedly <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   **Fine-tuning Custom Models**: Over time, use accumulated production data to fine-tune custom models, which can create better responses for specific use cases, reduce reliance on API calls, and lower costs <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

## Agentic Workflows
[[agent_frameworks_and_orchestration_layers_in_ai_engineering | Agentic workflows]] are becoming increasingly important, especially since they can use a wide range of tools, call different APIs, and have multi-agent structures executing tasks in parallel <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>. For agentic workflows, evaluation not only measures performance but also assesses agent behavior, ensuring they make correct decisions and follow intended logic <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>.

Every AI workflow has some level of agentic behavior; it's a question of control, reasoning, and autonomy <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. A framework defines different levels of agentic behavior:

### Levels of Agentic Behavior
*   **L0: Basic LLM Call with Retrieval** <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>:
    *   Involves an LLM call, data retrieval from a vector database, and inline evaluations <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.
    *   No explicit reasoning, planning, or decision-making beyond what's defined in the prompt <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a>. The model performs all reasoning within the prompt <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>.
*   **L1: Tool Use** <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>:
    *   The AI system can use tools and decides when to call APIs or retrieve more data <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.
    *   Memory becomes key for multi-threaded conversations, capturing context throughout the workflow <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.
    *   Evaluation is needed at every step to ensure correct decisions and accurate responses when using tools <a class="yt-timestamp" data-t="16:37:00">[16:37:00]</a>. These workflows can range from simple to highly complex with multiple branching paths and tools <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>.
    *   Many production-grade solutions currently fall within the L1 segment <a class="yt-timestamp" data-t="20:40:00">[20:40:00]</a>. The focus here is on [[agent_frameworks_and_orchestration_layers_in_ai_engineering | orchestration]]: how models interact with systems and data <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.
*   **L2: Structured Reasoning** <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>:
    *   Workflows move beyond simple tool use to structured reasoning <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.
    *   The system notices triggers, plans actions, and executes tasks in a structured sequence, breaking down tasks into multiple steps, retrieving information, calling tools, and refining its process in a continuous loop <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>.
    *   Agentic behavior is more intentional, actively deciding what needs to be done and spending more time to think <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>.
    *   The process is still finite, terminating once steps are completed <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
    *   This is where most innovation is expected to happen, with many AI agents developed to plan and reason using models like 01 or 03 <a class="yt-timestamp" data-t="21:41:00">[21:41:00]</a>.
*   **L3: Proactive Autonomy** <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>:
    *   The system proactively takes actions without waiting for direct input <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.
    *   Instead of terminating after a single request, it stays alive, continuously monitors its environment (e.g., email, Slack, Google Drive), and reacts as needed <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
    *   This makes AI workflows less of a tool and more of an independent system, capable of making work easier <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>.
*   **L4: Fully Creative / Inventor** <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>:
    *   The AI moves beyond automation and reasoning to become an inventor <a class="yt-timestamp" data-t="19:44:00">[19:44:00]</a>.
    *   It can create its own new workflows, utilities (agents, prompts, function calls, tools), and solve problems in novel ways <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>.
    *   Currently, true L4 is "Out Of Reach" due to model constraints like overfitting and inductive bias <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>. The goal is AI that invents, improves, and solves problems in unforeseen ways <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>.

L3 and L4 are still limited by current models and surrounding logic, though innovation is occurring in these areas as well <a class="yt-timestamp" data-t="22:22:00">[22:22:00]</a>.

### Example: SEO Agent
An example of an [[multiagent_orchestration_for_ai_copilot_development | AI agent]] that automates the SEO process (keyword research, content analysis, content creation) lies between an L1 and L2 type of agentic workflow <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>.

The agent's workflow components and process:
1.  **SEO Analyst** and **Researcher**: Takes a keyword, writing style, and audience parameters. Calls Google Search to analyze top-performing articles, identifying strong points to amplify and missing segments for improvement <a class="yt-timestamp" data-t="23:43:00">[23:43:00]</a>. The researcher then conducts further searches to capture more data on missing pieces <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.
2.  **Writer**: Takes the gathered information as context to create a detailed first draft <a class="yt-timestamp" data-t="26:02:00">[26:02:00]</a>. This content utilizes all the provided context intelligently, potentially integrating with a RAG system of internal articles and learnings <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>.
3.  **Editor**: An LLM-based judge evaluates the first draft against predefined rules and provides feedback <a class="yt-timestamp" data-t="24:19:00">[24:19:00]</a>.
4.  **Loop and Memory**: The feedback is passed back to the writer via a memory component (chat history) between the writer and editor. This loop continues until a specific criterion is met (e.g., "excellent post" evaluation, or a set number of iterations) <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>.
5.  **Final Article**: The process yields a useful, well-informed piece of content, saving significant time <a class="yt-timestamp" data-t="24:49:00">[24:49:00]</a>.

This example highlights the complexity of orchestrating multiple AI components and tools within a single workflow, where [[best_practices_and_lessons_learned_in_ai_agent_development | continuous improvement]] and evaluation are paramount <a class="yt-timestamp" data-t="25:25:00">[25:25:00]</a>. Tools like Bellum Workflows and their SDK are designed to bridge the gap between product and engineering teams, speeding up AI development while adhering to a [[best_practices_for_building_ai_systems | test-driven approach]] <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>. They provide building blocks, flexibility, and self-documenting syntax, keeping UI and code in sync for collaborative definition, debugging, and improvement of workflows <a class="yt-timestamp" data-t="28:14:00">[28:14:00]</a>.