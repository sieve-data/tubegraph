---
title: AI agents and agentic workflows
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

[[Agentic systems and workflows | Agentic workflows]] represent advanced AI solutions that allow systems to go beyond simple API calls, incorporating reasoning, planning, and autonomous decision-making [00:15:59]. These workflows enable AI models to interact better with systems and data, deliver more structured outputs, and solve complex problems [00:01:29].

Leading companies have successfully deployed reliable AI solutions in production, from simple to more advanced [[agentic_systems_and_workflows | agentic workflows]] [00:00:08]. A key to building reliable and stronger systems for production has been adopting a test-driven development approach [00:00:18].

## Evolution and Need for Agentic Workflows

In 2023, many built AI wrappers, with initial arguments against their defensibility [00:00:44]. However, successes like Cursor AI, an AI-powered IDE that achieved significant growth, demonstrated the potential [00:00:52]. This success was driven by models improving at coding, a skyrocket in AI adoption, coding being an obvious first target for disruption, and, importantly, the development of new techniques and patterns to orchestrate models more effectively in production [00:01:11].

These techniques are crucial due to inherent limits in model performance, such as hallucinations and overfitting, and the developer need for more structured outputs [00:01:38]. While model providers have shipped better tooling, significant leaps in model capabilities (like the jump from GPT-3.5 to GPT-4) have slowed [00:01:48]. For years, making models bigger and fitting more data made them smarter, but this approach hit a wall as improvements slowed and models reached limits on existing tests [00:02:01].

Recent advancements in training methods, like real reinforcement learning (e.g., Deepseek R1, trained without labeled data), have pushed the field forward [00:02:38]. These methods enable models to learn autonomously [00:02:50] and utilize Chain of Thought thinking at inference time, allowing them to "think" before responding and solve more complex reasoning problems [00:03:03]. Model providers are also enhancing models with capabilities like tool use, research functionalities, and improved OCR accuracy [00:03:24].

However, traditional benchmarks are saturated, leading to the introduction of new ones that capture the performance of these reasoning models, especially for truly difficult tasks [00:03:41]. Success for an AI product in production is no longer just about the models but about how one builds around them [00:04:10].

## Evolving Techniques in AI Workflow Development

Alongside model training advancements, techniques for building around models have evolved:
*   **Prompting Techniques** Advanced methods like Chain of Thought for better model interaction [00:04:25].
*   **RAG (Retrieval Augmented Generation)** Grounding model responses with proprietary data [00:04:31].
*   **Memory** Crucial for multi-threaded conversations, capturing context throughout the workflow [00:04:42].
*   **Long Context Windows** Enabled new use cases [00:04:47].
*   **Graph RAG** Experimenting with hierarchy of responses [00:04:52].
*   **Reasoning Models** Utilizing models that take more time to think in real-time, opening new areas and use cases [00:04:59].
*   **[[Agentic systems and workflows | Agentic RAG]]** Making workflows even more powerful [00:05:12].

Despite these techniques, deeply understanding the problem and adopting a test-driven development approach is essential to find the right mix of techniques, models, and logic for a specific use case [00:05:22].

## Test-Driven Development for Reliable AI Products

The best AI teams follow a structured approach involving experimentation, evaluation, scaling, deployment, and continuous improvement [00:05:48].

### 1. Experimentation
Before building anything production-grade, extensive experimentation is needed to prove if AI models can solve the use case [00:06:14].
*   **Try Different Prompting Techniques** Such as few-shot or Chain of Thought, suitable for simple to complex tasks [00:06:23].
*   **Test Various Techniques** Prompt chaining (splitting instructions into multiple prompts) or [[agentic_systems_and_workflows | agentic workflows]] like ReAct, which involve planning, reasoning, and refining before generating an answer [00:06:33].
*   **Involve Domain Experts** Engineers should not be solely responsible for tweaking prompts; domain experts save engineering time by confirming proof-of-work [00:06:53].
*   **Stay Model Agnostic** Incorporate and test different models to find which performs best for the use case (e.g., Gemini 2.0 Flash for OCR) [00:07:13].

### 2. Evaluation
Once models show good performance on examples, evaluation determines if they will work in production under high request volumes [00:07:46].
*   **Create a Dataset** Build a dataset of hundreds of examples to test models and workflows [00:07:57].
*   **Balance Quality, Cost, Latency, and Privacy** Define priorities early, making tradeoffs (e.g., sacrificing speed for quality, or using lighter models if cost is critical) [00:08:06].
*   **Use Ground Truth Data** Subject matter experts should design databases and test models against them for robust evaluation [00:08:32].
*   **Utilize LLMs for Evaluation** If ground truth data isn't available, an LLM can evaluate another model's response [00:08:58].
*   **Employ a Flexible Testing Framework** The framework should be dynamic to capture non-deterministic responses, allow custom metrics (Python/TypeScript), and avoid strict limitations [00:09:14].
*   **Run Evaluations at Every Stage** Implement guard rails to check internal nodes and ensure correct responses at every step of the workflow, testing both during prototyping and with real data [00:09:48].

### 3. Deployment & Continuous Improvement
After extensive evaluation and satisfaction with the product, it's ready for production [00:10:15].
*   **Monitor Beyond Deterministic Outputs** Log all LLM calls, track inputs, outputs, and latency to debug issues and understand AI behavior [00:10:35]. This is crucial for [[agentic_systems_and_workflows | agentic workflows]], which are more complex and can take different paths [00:10:56].
*   **Handle API Reliability** Maintain API stability with retries and fallback logic to prevent outages (e.g., switching to another model if a primary service like OpenAI goes down) [00:11:09].
*   **Version Control and Staging** Deploy in controlled environments before wider public release to prevent regressions when updating prompts or workflow parts [00:11:35].
*   **Decouple Deployments** Separate AI feature updates from scheduled app deployments, as AI features often need more frequent updates [00:12:00].
*   **Create a Feedback Loop** Capture user responses from production to identify edge cases, run new evaluations, and continuously improve the workflow [00:12:26].
*   **Build a Caching Layer** For repeat queries, caching drastically reduces costs and improves latency by storing and instantly serving frequent responses instead of re-calling expensive LLMs [00:12:47].
*   **Fine-tune Custom Models** Use aggregated production data to fine-tune custom models for specific use cases, reducing reliance on API calls and lowering costs [00:13:16].

This process becomes even more critical for [[agentic_systems_and_workflows | agentic workflows]] due to their use of a wide range of tools, multiple API calls, and multi-agent structures that execute in parallel [00:13:34]. Evaluation must assess not only performance at every step but also the behavior of agents to ensure correct decisions and adherence to intended logic [00:13:53].

## Levels of Agentic Behavior

Every AI workflow has some level of [[agentic_systems_and_workflows | agentic behavior]], differing in control, reasoning, and autonomy [00:14:40]. A framework defines five levels of agentic behavior:

### L0: Basic LLM Call
*   **Behavior:** An LLM call retrieves data (e.g., from a vector database), with some inline evaluations, resulting in a response [00:15:19].
*   **Characteristics:** No external planning or decision-making beyond what's embedded in the prompt and model behavior [00:15:32]. The model performs all reasoning within the prompt itself [00:15:38]. Some [[agentic_systems_and_workflows | agentic behavior]] exists at the model's level [00:15:48].

### L1: Tool-Using Workflows
*   **Behavior:** The AI system can use tools and knows when to call them [00:15:56]. It can decide whether to call a specific tool or a vector database to retrieve more data before generating an output [00:16:13].
*   **Characteristics:** Starts to exhibit more [[agentic_systems_and_workflows | agentic behavior]] [00:16:10]. Memory becomes crucial for multi-threaded conversations to capture context [00:16:24]. Evaluation is needed at every step to ensure correct decisions, tool usage, and accurate responses [00:16:37]. These workflows can range from simple to very complex, with branching logic and multiple tools [00:16:50]. Many production-grade solutions currently fall into this category [00:20:41]. The focus is on orchestration: how models interact with systems and data, and retrieve the correct context [00:21:01].

### L2: Structured Reasoning and Task Breakdown
*   **Behavior:** Workflows move beyond simple tool use to structured reasoning [00:17:15]. The system notices triggers, plans actions, and executes tasks in a structured sequence [00:17:28]. It can break down a task into multiple steps, retrieve information, call other tools, evaluate their usefulness, and refine them in a continuous loop to generate a final output [00:17:37].
*   **Characteristics:** [[Agentic systems and workflows | Agentic behavior]] becomes more intentional; the system actively decides what needs to be done and spends more time thinking, rather than just deciding which tool to call [00:17:55]. The process is finite, terminating once steps are completed [00:18:16]. This is where most innovation is expected to happen, with [[developing_ai_agents_and_agentic_workflows | AI agents]] being developed to plan and reason using advanced models [00:21:41]. It can lead to new UI/UX experiences and true reasoners for complex tasks [00:21:58].

### L3: Proactive and Autonomous Systems
*   **Behavior:** Exhibits higher autonomy and decision-making not defined by the creator [00:18:33]. The system proactively takes actions without waiting for direct input [00:18:44]. Instead of terminating after a single request, it stays alive, continuously monitors its environment, and reacts as needed [00:18:52].
*   **Characteristics:** Can interact with external services (email, Slack, Google Drive) to plan and execute moves or request human input [00:19:02]. [[Role of AI agents in workflow automation | AI workflows]] become less of a tool and more of an independent system [00:19:19]. An example could be a marketer agent preparing a video or presentation autonomously [00:19:30]. This level, along with L4, is currently limited by existing models and surrounding logic [00:22:22].

### L4: Fully Creative and Inventive AI
*   **Behavior:** The AI moves beyond automation and reasoning to become an inventor [00:19:39]. Instead of executing predefined tasks or reasoning within bounds, it creates its own new workflows, utilities (agents, prompts, function calls, tools), and solves problems in novel ways [00:19:50].
*   **Characteristics:** A true L4 agent is currently Out Of Reach due to constraints like overfitting (models favoring training data) and inductive bias (models making assumptions based on training data) [00:20:08]. The goal is an AI that doesn't just follow instructions but invents, improves, and solves problems in unforeseen ways [00:20:30]. This level, along with L3, is currently limited by existing models and surrounding logic [00:22:22].

## Example: SEO Agent

An example of an [[developing_ai_agents_for_productivity | AI agent]] is an SEO agent that automates the entire SEO process, from keyword research to content analysis and content creation [00:23:04]. This agent decides when to use tools and has an embedded evaluator that provides feedback to the agent on its performance [00:23:14].

This particular SEO agent workflow lies between L1 and L2 [[agentic_systems_and_workflows | agentic workflow]] types [00:23:37].

The workflow consists of several components:
1.  **SEO Analyst & Researcher:** Takes a keyword (e.g., "Chain of Thought prompting"), writing style, and audience [00:25:14]. It calls Google search to analyze top-performing articles for the keyword, identifies strong points to amplify, and missing segments or areas for improvement [00:23:43]. The researcher then conducts further searches to capture more data based on identified missing pieces [00:25:53].
2.  **Writer:** Takes the analyzed information as input to create a first draft of the article [00:24:13]. The content is not generic but utilizes context from analyzed articles and can integrate with RAG for additional database knowledge [00:26:05].
3.  **Editor (LLM-based Judge):** Evaluates the first draft against predefined rules set in its prompt [00:24:19].
4.  **Feedback Loop:** The editor's feedback is passed back to the writer via a memory component (chat history) [00:24:31]. This loop continues until specific criteria are met (e.g., the editor deems the post "excellent" or a set number of iterations are completed) [00:24:33].

This workflow results in a useful first draft that incorporates relevant context from competing articles, providing a strong foundation for content creation and saving significant time [00:24:49].