---
title: Challenges and strategies in AI production
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 
AI product success is not just about the underlying models, but how solutions are built around them <a class="yt-timestamp" data-t="04:15:01">[04:15:01]</a>. Building reliable and stronger AI systems in production is achievable through a test-driven development (TDD) approach <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

### The Evolution of AI and its Current State
In 2023, many AI wrappers were developed, with debates about their defensibility <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. Today, Cursor AI, an AI-powered IDE, has achieved significant growth, demonstrating the potential of AI applications <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>. This success is partly due to models improving at coding and a surge in AI adoption <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. More importantly, new techniques and patterns have emerged to orchestrate these models, enabling them to work better with data and effectively in production <a class="yt-timestamp" data-t="01:26:01">[01:26:01]</a>.

Key challenges with model performance persist, including hallucinations and overfitting <a class="yt-timestamp" data-t="01:41:01">[01:41:01]</a>. While model providers have shipped better tooling, significant leaps in raw model performance, similar to the jump from GPT-3.5 to GPT-4, have slowed down <a class="yt-timestamp" data-t="01:48:01">[01:48:01]</a>. For years, making models bigger and adding more data made them smarter, but this approach has hit a wall, with improvements slowing and models reaching their limits on existing tests <a class="yt-timestamp" data-t="02:01:01">[02:01:01]</a>.

However, new training methods have emerged in recent months, pushing the field forward <a class="yt-timestamp" data-t="02:32:01">[02:32:01]</a>:
*   **Deepseek R1 Model**: The first model trained without labeled data, using "real reinforcement learning," allowing it to learn autonomously <a class="yt-timestamp" data-t="02:42:01">[02:42:01]</a>.
*   **Reasoning Models**: Models like OpenAI's O1 and O3 use Chain of Thought thinking at inference time to generate answers, enabling them to "think" before responding and solve more complex reasoning problems <a class="yt-timestamp" data-t="02:57:01">[02:57:01]</a>.
*   **Enhanced Capabilities**: Model providers are offering more capabilities, including tool use, research capabilities, and near-perfect OCR accuracy (e.g., Gemini 2.0 Flash) <a class="yt-timestamp" data-t="03:24:01">[03:24:01]</a>.

As traditional benchmarks become saturated, new ones are being introduced to capture the performance of these advanced reasoning models, such as the Humanities Last Exam, which measures performance on truly difficult tasks <a class="yt-timestamp" data-t="03:41:01">[03:41:01]</a>.

### Evolution of AI Techniques
Alongside model training, techniques for interacting with and orchestrating models have evolved <a class="yt-timestamp" data-t="04:20:01">[04:20:01]</a>:
*   **Prompting Techniques**: More advanced methods like Chain of Thought were developed <a class="yt-timestamp" data-t="04:25:01">[04:25:01]</a>.
*   **Retrieval Augmented Generation (RAG)**: Important for grounding model responses with proprietary data <a class="yt-timestamp" data-t="04:31:01">[04:31:01]</a>.
*   **Memory**: Critical for multi-threaded conversations in AI workflows <a class="yt-timestamp" data-t="04:42:01">[04:42:01]</a>.
*   **Long Context Models**: Enabled new use cases <a class="yt-timestamp" data-t="04:47:01">[04:47:01]</a>.
*   **Graph RAG**: Experimentation with hierarchy of responses <a class="yt-timestamp" data-t="04:52:01">[04:52:01]</a>.
*   **Agentic RAG**: Making workflows more powerful and autonomous <a class="yt-timestamp" data-t="05:12:01">[05:12:01]</a>.

### The Test-Driven Development Approach
To build an AI product that truly works in production, it's crucial to understand the problem deeply and adopt a [[strategies_for_effective_ai_implementation | test-driven development]] approach to find the right mix of techniques, models, and logic <a class="yt-timestamp" data-t="05:22:01">[05:22:01]</a>.

The best AI teams follow a structured approach:
1.  **Experiment** <a class="yt-timestamp" data-t="05:52:01">[05:52:01]</a>
2.  **Evaluate** <a class="yt-timestamp" data-t="05:54:01">[05:54:01]</a>
3.  **Scale** <a class="yt-timestamp" data-t="05:54:01">[05:54:01]</a>
4.  **Deploy** <a class="yt-timestamp" data-t="05:56:01">[05:56:01]</a>
5.  **Continuously Monitor, Observe, and Improve** <a class="yt-timestamp" data-t="06:01:01">[06:01:01]</a>

#### 1. Experimentation Phase
Before building anything production-grade, extensive experimentation is needed to prove whether AI models can solve the use case <a class="yt-timestamp" data-t="06:14:01">[06:14:01]</a>.
*   **Try different prompting techniques**: Few-shot or Chain of Thought, suitable for simple to complex reasoning tasks <a class="yt-timestamp" data-t="06:23:01">[06:23:01]</a>.
*   **Test various techniques**: Prompt chaining (splitting instructions into multiple prompts) or agentic workflows like ReAct (plan, reason, refine) <a class="yt-timestamp" data-t="06:33:01">[06:33:01]</a>.
*   **Involve domain experts**: Engineers shouldn't be the sole prompt tweakers; domain experts save engineering time <a class="yt-timestamp" data-t="06:53:01">[06:53:01]</a>.
*   **Stay model agnostic**: Incorporate and test different models, selecting those best suited for specific tasks (e.g., Gemini 2.0 Flash for OCR) <a class="yt-timestamp" data-t="07:13:01">[07:13:01]</a>.

#### 2. Evaluation Phase
This stage ensures the workflow will work in production under high request volumes <a class="yt-timestamp" data-t="07:44:01">[07:44:01]</a>.
*   **Create a dataset**: Develop a dataset of hundreds of examples for testing models and workflows <a class="yt-timestamp" data-t="07:57:01">[07:57:01]</a>.
*   **Balance trade-offs**: Prioritize quality, cost, latency, and privacy, as no AI system perfects all <a class="yt-timestamp" data-t="08:06:01">[08:06:01]</a>. Define priorities early <a class="yt-timestamp" data-t="08:27:01">[08:27:01]</a>.
*   **Use ground truth data**: Subject matter experts designing databases and testing against them is highly beneficial <a class="yt-timestamp" data-t="08:32:01">[08:32:01]</a>. Synthetic benchmarks are less effective for specific use cases <a class="yt-timestamp" data-t="08:46:01">[08:46:01]</a>.
*   **LLM evaluation**: If ground truth data is unavailable, an LLM can evaluate another model's response <a class="yt-timestamp" data-t="08:58:01">[08:58:01]</a>.
*   **Flexible testing framework**: Ensure the framework is dynamic, capable of capturing non-deterministic responses, defining custom metrics, and writing metrics in Python or TypeScript <a class="yt-timestamp" data-t="09:14:01">[09:14:01]</a>. Customizability is crucial <a class="yt-timestamp" data-t="09:42:01">[09:42:01]</a>.
*   **Run evaluations at every stage**: Implement guard rails to check internal nodes and ensure correct responses at every step of the workflow <a class="yt-timestamp" data-t="09:48:01">[09:48:01]</a>. Test during prototyping and re-evaluate with real data <a class="yt-timestamp" data-t="10:03:01">[10:03:01]</a>.

#### 3. Scaling and Deployment
Once satisfied with the product, it's ready for production <a class="yt-timestamp" data-t="10:23:01">[10:23:01]</a>.
*   **Monitor more than deterministic outputs**: Log all LLM calls, track inputs, outputs, and latency due to AI models' unpredictability <a class="yt-timestamp" data-t="10:35:01">[10:35:01]</a>. This is especially important for [[challenges_in_ai_agent_development | agentic workflows]] <a class="yt-timestamp" data-t="10:56:01">[10:56:01]</a>.
*   **Handle API reliability**: Maintain stability with retries and fallback logic to prevent outages (e.g., switching to another model during downtime) <a class="yt-timestamp" data-t="11:09:01">[11:09:01]</a>.
*   **Version control and staging**: Deploy in controlled environments before wider public release to prevent regressions from prompt updates <a class="yt-timestamp" data-t="11:35:01">[11:35:01]</a>.
*   **Decouple deployments**: AI features may need more frequent updates than the overall application, so deployment schedules should be separate <a class="yt-timestamp" data-t="12:00:01">[12:00:01]</a>.

#### 4. Continuous Improvement
After deployment, capture user feedback to identify edge cases and continuously improve the workflow <a class="yt-timestamp" data-t="12:21:01">[12:21:01]</a>.
*   **Feedback loop**: Use captured responses to run evaluations again and test new prompts for new cases <a class="yt-timestamp" data-t="12:26:01">[12:26:01]</a>.
*   **Caching layer**: For repeat queries, caching can significantly reduce costs and improve latency by serving frequent responses instantly instead of calling expensive LLMs <a class="yt-timestamp" data-t="12:46:01">[12:46:01]</a>.
*   **Fine-tune custom models**: Use reliable production data to fine-tune a custom model for specific use cases, reducing reliance on API calls and lowering costs <a class="yt-timestamp" data-t="13:16:01">[13:16:01]</a>.

### [[Challenges and Solutions in Building AI Agents | Challenges and Evolution of Agentic Workflows]]
The TDD process becomes even more crucial with [[challenges_in_ai_agent_development | agentic workflows]], which use a wide range of tools, call different APIs, and may have multi-agent structures executing tasks in parallel <a class="yt-timestamp" data-t="13:34:01">[13:34:01]</a>. Evaluation must not only measure performance at every step but also assess the behavior of agents to ensure correct decisions and intended logic <a class="yt-timestamp" data-t="13:53:01">[13:53:01]</a>.

Every AI workflow has some level of agentic behavior, differing in control, reasoning, and autonomy <a class="yt-timestamp" data-t="14:40:01">[14:40:01]</a>. A framework defines different levels of agentic behavior:

*   **L0: Basic LLM Call with RAG**
    *   An LLM call retrieves data from a vector database, with some inline evaluations <a class="yt-timestamp" data-t="15:19:01">[15:19:01]</a>.
    *   No external agenda organizes decisions or plans actions; the model performs all reasoning within the prompt <a class="yt-timestamp" data-t="15:32:01">[15:32:01]</a>.

*   **L1: Tool Use**
    *   The AI system can use tools and decide *when* to call APIs or retrieve data from a vector database <a class="yt-timestamp" data-t="15:56:01">[15:56:01]</a>.
    *   This shows more agentic behavior <a class="yt-timestamp" data-t="16:10:01">[16:10:01]</a>.
    *   Memory is key for multi-threaded conversations, capturing context throughout the workflow <a class="yt-timestamp" data-t="16:23:01">[16:23:01]</a>.
    *   Evaluation is needed at every step to ensure correct decisions and accurate responses <a class="yt-timestamp" data-t="16:37:01">[16:37:01]</a>. These workflows can range from simple to complex, with multiple branching paths and numerous tools <a class="yt-timestamp" data-t="16:50:01">[16:50:01]</a>.
    *   Current production-grade solutions often fall within L1, focusing on orchestration <a class="yt-timestamp" data-t="20:53:01">[20:53:01]</a>.

*   **L2: Structured Reasoning**
    *   Workflows move from simple tool use to structured reasoning <a class="yt-timestamp" data-t="17:15:01">[17:15:01]</a>.
    *   The system notices triggers, plans actions, and executes tasks in a structured sequence, breaking down tasks into multiple steps <a class="yt-timestamp" data-t="17:28:01">[17:28:01]</a>.
    *   It can retrieve information, call tools, evaluate their usefulness, and refine as needed in a continuous loop <a class="yt-timestamp" data-t="17:41:01">[17:41:01]</a>.
    *   Agentic behavior becomes more intentional, with the system actively deciding what needs to be done and spending more time "thinking" <a class="yt-timestamp" data-t="17:55:01">[17:55:01]</a>.
    *   The process is still finite, terminating once steps are completed <a class="yt-timestamp" data-t="18:16:01">[18:16:01]</a>.
    *   L2 is expected to see significant innovation this year, with AI agents developed for planning and reasoning using advanced models <a class="yt-timestamp" data-t="21:41:01">[21:41:01]</a>.

*   **L3: Proactive Autonomy**
    *   Systems proactively take actions without waiting for direct input, continuously monitoring their environment and reacting as needed <a class="yt-timestamp" data-t="18:33:01">[18:33:01]</a>.
    *   They can access external services (email, Slack, Google Drive) to plan next moves and execute actions or ask for human input <a class="yt-timestamp" data-t="19:02:01">[19:02:01]</a>.
    *   AI workflows become less of a tool and more of an independent system, such as a marketer preparing a video <a class="yt-timestamp" data-t="19:19:01">[19:19:01]</a>.

*   **L4: Fully Creative/Inventor AI**
    *   This stage moves beyond automation and reasoning, with AI becoming an inventor <a class="yt-timestamp" data-t="19:39:01">[19:39:01]</a>.
    *   Instead of predefined tasks, it creates its own new workflows, utilities, agents, prompts, function calls, and tools <a class="yt-timestamp" data-t="19:50:01">[19:50:01]</a>.
    *   It solves problems in novel ways <a class="yt-timestamp" data-t="20:06:01">[20:06:01]</a>.
    *   True L4 is currently out of reach due to model constraints like overfitting (models loving their training data) and inductive bias (models making assumptions based on training data) <a class="yt-timestamp" data-t="20:12:01">[20:12:01]</a>.
    *   The goal is AI that invents, improves, and solves problems in unforeseen ways <a class="yt-timestamp" data-t="20:30:01">[20:30:01]</a>.

L3 and L4 are still limited by current models and surrounding logic, though innovation is occurring in these areas <a class="yt-timestamp" data-t="22:22:01">[22:22:01]</a>.

### Practical Example: SEO Agent Workflow
An SEO agent automates the SEO process from keyword research to content analysis and creation <a class="yt-timestamp" data-t="23:04:01">[23:04:01]</a>. This specific agent lies between an L1 and L2 type of agentic workflow <a class="yt-timestamp" data-t="23:37:01">[23:37:01]</a>.

**Workflow Steps**:
1.  **SEO Analyst**: Takes a keyword, writing style, and audience parameters. Calls Google Search to analyze top-performing articles, identifying strong points to amplify and missing segments for improvement <a class="yt-timestamp" data-t="23:43:01">[23:43:01]</a>.
2.  **Researcher**: Utilizes the identified missing opportunities to perform further searches and capture more data <a class="yt-timestamp" data-t="25:53:01">[25:53:01]</a>.
3.  **Writer**: Takes all collected information as input to create a comprehensive first draft. The content is not generic but intelligently uses context from analyzed articles; it can also connect to a RAG database of internal articles and learnings <a class="yt-timestamp" data-t="26:02:01">[26:02:01]</a>.
4.  **Editor (LLM-based judge)**: Evaluates the first draft based on predefined rules in its prompt and provides feedback <a class="yt-timestamp" data-t="24:19:01">[24:19:01]</a>.
5.  **Refinement Loop**: The feedback is passed back to the writer via a memory component (chat history). This loop continues until a specific criterion is met (e.g., the editor designates the post as "excellent" or a maximum number of loops is reached) <a class="yt-timestamp" data-t="24:31:01">[24:31:01]</a>.
6.  **Final Article**: Produces a useful and impressive first draft <a class="yt-timestamp" data-t="24:49:01">[24:49:01]</a>.

This workflow saves significant time by providing a strong foundation for content creation <a class="yt-timestamp" data-t="27:47:01">[27:47:01]</a>.

### Tools for AI Development
Platforms like Bellum Workflows are designed to bridge the gap between product and engineering teams, speeding up AI development while adhering to the test-driven approach <a class="yt-timestamp" data-t="27:49:01">[27:49:01]</a>. An SDK offers building blocks, infinite customization, and self-documenting syntax for developers to own their definitions in the codebase <a class="yt-timestamp" data-t="28:13:01">[28:13:01]</a>. Key features include:
*   **Code-UI Synchronization**: The UI and code stay in sync for workflow definition, debugging, and improvement, ensuring team alignment <a class="yt-timestamp" data-t="28:34:01">[28:34:01]</a>.
*   **Open Source and Free**: Available on GitHub <a class="yt-timestamp" data-t="28:43:01">[28:43:01]</a>.