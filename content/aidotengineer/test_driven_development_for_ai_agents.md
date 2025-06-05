---
title: Test driven development for AI agents
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

Companies that have successfully deployed [[challenges_in_building_reliable_ai_agents | reliable AI Solutions]] in production have adopted a [[testing_and_optimization_of_ai_coding_agents | test-driven development approach]] <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This method enables the creation of stronger, more [[challenges_in_building_reliable_ai_agents | reliable systems]] <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.

## Evolution of AI and the Need for TDD

While models have improved significantly, particularly in coding <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, and [[developing_and_optimizing_ai_agents | AI adoption]] has skyrocketed <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, there are clear limits to model performance, including hallucinations <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a> and overfitting <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. Major advancements in model capabilities, like the jump between GPT-3.5 and GPT-4, have slowed down <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. Models began to hit limits on existing tasks despite more data <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.

New training methods, such as real reinforcement learning (e.g., DeepSeek R1) <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, and the use of Chain of Thought thinking in reasoning models (like 01 and 03) <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>, have pushed the field forward, allowing models to solve more complex reasoning problems <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. Models are also gaining more capabilities like tool use and improved OCR accuracy <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

However, success for an AI product in production relies less on just the models and more on how they are built around <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. Techniques such as prompt engineering (e.g., Chain of Thought) <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>, Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>, managing memory for multi-threaded conversations <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>, graph RAG <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>, and agentic RAG <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a> are crucial. These techniques, while evolving, are not enough on their own <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>. A deep understanding of the problem and a [[testing_and_optimization_of_ai_coding_agents | test-driven development approach]] are essential to finding the right mix of techniques, models, and logic <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

## Test-Driven Development for AI Products

The [[best_practices_and_lessons_learned_in_ai_agent_development | best AI teams]] follow a structured approach involving experimentation, evaluation, deployment, and continuous monitoring <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

### 1. Experimentation
Before building anything production-grade, extensive experimentation is needed to prove if AI models can solve the use case <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Try different prompting techniques** <a class="yt-timestamp" data-t="06:23:00">[06:23:00]</a>:
    *   Few-shot prompting.
    *   Chain of Thought for more complex reasoning <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
*   **Test various techniques** <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>:
    *   Prompt chaining, splitting instructions into multiple prompts <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.
    *   [[developing_and_optimizing_ai_agents | Agentic workflows]] like React, which involve planning, reasoning, and refining <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.
*   **Involve domain experts** <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>: Engineers should not be the sole prompt tweakers <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>; their involvement saves engineering time <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Stay model agnostic** <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>: Incorporate and test different models based on the use case, e.g., Gemini 2.0 Flash for OCR <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

### 2. Evaluation
Once initial proof of concept is established, [[testing_and_evaluation_of_ai_models | evaluation]] is crucial for production readiness, especially when dealing with high request volumes <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Create a data set** of hundreds of examples for testing workflows <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **Balance quality, cost, latency, and privacy** <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. Define priorities early, as no AI system perfects all aspects <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   **Use ground truth data** <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>: Subject matter experts designing databases and testing models against them is very useful <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   **Utilize LLMs for evaluation** <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>: Even without ground truth, an LLM can reliably evaluate another model's response <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.
*   **Use a flexible testing framework** <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>: AI systems are dynamic, so workflows need to be dynamic, capable of capturing non-deterministic responses, defining custom metrics, and writing metrics in Python or TypeScript <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.
*   **Run evaluations at every stage** <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>: Implement guardrails to check internal nodes and ensure correct responses at each step <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>. [[testing_and_evaluation_of_ai_models | Evaluate]] during prototyping and use real data later <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.

### 3. Deployment
After extensive evaluation, deploying to production requires specific considerations <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.
*   **Monitor beyond deterministic outputs** <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>: Log all LLM calls, track inputs, outputs, and latency to understand and debug unpredictable AI behavior <a class="yt-timestamp" data-t="10:39:00">[10:39:00]</a>. This is especially critical for [[developing_and_optimizing_ai_agents | agentic workflows]] due to their complexity and decision-making paths <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>.
*   **Handle API reliability** <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>: Maintain stability with retries and fallback logic to prevent outages <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. For example, during an OpenAI outage, a fallback model could be used <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.
*   **Use Version Control and staging** <a class="yt-timestamp" data-t="11:35:00">[11:35:00]</a>: Deploy in controlled environments first to avoid regressions when updating prompts or workflows <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.
*   **Decouple deployments** from scheduled app deployments <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>, as AI features often need more frequent updates <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

### 4. Continuous Improvement
Deployment is not the end; continuous monitoring and feedback loops are vital for improvement <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.
*   **Capture user responses** to identify edge cases in production <a class="yt-timestamp" data-t="12:26:00">[00:26:00]</a>, then run [[testing_and_evaluation_of_ai_models | evaluations]] again with new prompts to address them <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>.
*   **Build a caching layer** <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>: For repeat queries, caching drastically reduces costs and improves latency by storing and serving frequent responses instantly <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
*   **Fine-tune custom models** <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>: Use accumulated production data to fine-tune models for specific use cases, reducing reliance on API calls and lowering costs <a class="yt-timestamp" data-t="13:19:00">[13:19:00]</a>.

## Levels of Agentic Behavior

Every AI workflow has some level of agentic behavior, differing in control, reasoning, and autonomy <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. A framework defines different levels:

*   **L0: Basic LLM Call** <a class="yt-timestamp" data-t="15:19:00">[15:19:00]</a>: An LLM call retrieves data, with inline evaluations, and produces a response. Reasoning and decision-making are entirely within the model's prompt and behavior, with no external agent organizing actions <a class="yt-timestamp" data-t="15:30:00">[15:30:00]</a>.
*   **L1: Tool Use** <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>: The AI system can now use various tools and decide when to call them <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>. This introduces more agentic behavior as the model chooses specific tools or retrieves more data <a class="yt-timestamp" data-t="16:10:00">[16:10:00]</a>. Memory becomes crucial for multi-threaded conversations, and [[evaluating_ai_agent_performance_and_reliability | evaluation]] is needed at every step to ensure correct decisions and accurate responses <a class="yt-timestamp" data-t="16:25:00">[16:25:00]</a>.
    *   Many production-grade solutions currently fall within the L1 segment <a class="yt-timestamp" data-t="20:41:00">[20:41:00]</a>. The focus here is on orchestrating models to interact with systems and data effectively <a class="yt-timestamp" data-t="21:01:00">[21:01:00]</a>.
*   **L2: Structured Reasoning** <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>: Workflows move beyond simple tool use to structured reasoning <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>. The system notices triggers, plans actions, and executes tasks in a structured sequence <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. It can break down tasks, retrieve information, call other tools, and refine its output in a continuous loop <a class="yt-timestamp" data-t="17:37:00">[17:37:00]</a>. Agentic behavior becomes more intentional, as the system actively decides what needs to be done and spends more time thinking <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. The process is still finite, terminating after completing its planned steps <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
    *   This year is expected to see significant innovation in L2, with AI agents being developed for planning and reasoning using models like 01, O3, or DeepSeek <a class="yt-timestamp" data-t="21:41:00">[21:41:00]</a>.
*   **L3: Autonomy** <a class="yt-timestamp" data-t="18:33:00">[18:33:00]</a>: The system proactively takes actions without waiting for direct input <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>. Instead of terminating after a single request, it continuously monitors its environment and reacts as needed <a class="yt-timestamp" data-t="18:52:00">[18:52:00]</a>. It can access external services like email, Slack, or Google Drive, plan next moves, and execute actions or ask for human input <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. AI workflows become independent systems rather than mere tools <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>.
*   **L4: Fully Creative** <a class="yt-timestamp" data-t="19:38:00">[19:38:00]</a>: The AI moves beyond automation and reasoning to become an inventor <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. It can create its own new workflows, utilities (agents, prompts, function calls, tools), and solve problems in novel ways <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>. True L4 is currently out of reach due to constraints like overfitting and inductive bias in models <a class="yt-timestamp" data-t="20:08:00">[20:08:00]</a>.

## Case Study: SEO AI Agent

An example of an [[case_study_of_ai_interview_agent_development | AI agent]] that automates the entire SEO process (keyword research, content analysis, content creation) demonstrates a workflow between L1 and L2 levels of agentic behavior <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>.

### Workflow Overview
The SEO agent workflow involves multiple interconnected components:
1.  **SEO Analyst and Researcher**: Takes a keyword, calls Google Search, and analyzes top-performing articles <a class="yt-timestamp" data-t="23:43:00">[23:43:00]</a>. It identifies good components to amplify and missing segments for improvement <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>. The researcher then uses these identified gaps to make further searches and gather more data <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.
2.  **Writer**: Takes the information from the research phase and creates a first draft of the article <a class="yt-timestamp" data-t="24:13:00">[24:13:00]</a>. The content is generated using the context from analyzed articles <a class="yt-timestamp" data-t="26:21:00">[26:21:00]</a>.
3.  **Editor (LLM-based Judge)**: An embedded evaluator that assesses the first draft based on predefined rules <a class="yt-timestamp" data-t="24:21:00">[24:21:00]</a>.
4.  **Feedback Loop and Memory**: The editor's feedback is passed back to the writer via a memory component (chat history), creating a continuous loop until certain criteria are met (e.g., article quality, number of iterations) <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>.

This workflow highlights the importance of [[evaluating_ai_agent_performance_and_reliability | evaluating]] agent behavior to ensure it makes the right decisions and follows intended logic <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>. The agent can decide whether to use tools and has an embedded evaluator <a class="yt-timestamp" data-t="23:12:00">[23:12:00]</a>.

## Tools and Frameworks

Bellum offers workflows and an SDK designed to bridge product and engineering teams, speeding up [[developing_and_optimizing_ai_agents | AI development]] while adhering to the [[testing_and_optimization_of_ai_coding_agents | test-driven approach]] <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>. The workflow SDK provides building blocks, infinite customizability, and a self-documenting syntax, allowing developers to understand agent behavior directly from the code <a class="yt-timestamp" data-t="28:14:00">[28:14:00]</a>. The UI and code remain synchronized for alignment across teams during definition, debugging, and improvement <a class="yt-timestamp" data-t="28:34:00">[28:34:00]</a>. The SDK is open-source and free <a class="yt-timestamp" data-t="28:43:00">[28:43:00]</a>.