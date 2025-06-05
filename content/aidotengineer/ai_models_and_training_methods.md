---
title: AI models and training methods
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

Vellum has observed that companies successfully deploying reliable AI solutions, from simple to advanced [[building_effective_ai_agents | agentic workflows]], adopt a test-driven development approach to build robust systems <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This approach is key to building effective [[building_effective_ai_agents | agentic workflows]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Evolution of AI Models and Applications
In 2023, many were building "AI wrappers," leading to arguments about a lack of defensibility strategy <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. However, the success of Cursor AI, an [[choosing_and_implementing_ai_models_for_data_analysis | AI-powered IDE]] that hit $100 million ARR in 12 months, demonstrated a shift <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This success was driven by models improving at coding, skyrocketing [[ai_implementation_and_best_practices | AI adoption]], and coding being an obvious first target for disruption by [[choosing_and_implementing_ai_models_for_data_analysis | AI models]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

More importantly, new [[techniques_for_improving_ai_model_efficiency | techniques]] and patterns emerged for orchestrating these models to work better, sync with data, and perform effectively in production <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Limitations of Early AI Models
These [[techniques_for_improving_ai_model_efficiency | techniques]] became crucial due to clear limits in model performance <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>:
*   Hallucinations <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>
*   Overfitting <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>
*   Need for more structured outputs for developers <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

While model providers shipped better tooling, significant "leaps" like that between GPT 3.5 and GPT-4 slowed down <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For years, making models bigger and fitting more data made them smarter, but eventually, improvements started to slow down, and models seemed to reach limits on existing tests <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### New Training Methods
Recent advancements in [[ai_model_training_and_inference | AI model training methods]] have pushed the field forward <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>:
*   **DeepSeek R1 Model**: The first model reportedly trained without labeled data, using "real [[custom_model_training_and_reinforcement_learning | reinforcement learning]]" where the model learns on its own <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Chain of Thought (CoT) Thinking**: Used by reasoning models (e.g., OpenAI's 01 and 03) at inference or response time to generate answers <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This allows models to "think" before responding, solving more complex reasoning problems <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

Model providers are also enhancing capabilities, including tool use, research capabilities, and near-perfect OCR accuracy (e.g., Gemini 2.0 Flash) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

### Benchmarking Challenges
Traditional benchmarks are saturated, leading to the introduction of new benchmarks to capture the performance of new reasoning models <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The "Humanities Last Exam," for example, measures performance on truly difficult tasks, where even the latest smart models still struggle <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Beyond Model Performance: Building Around AI
For an [[ai_implementation_and_best_practices | AI product]] to work effectively in production, success is not just about the models themselves, but about how you build around them <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This "building around" has evolved in parallel to [[ai_model_training_and_inference | model training]] <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Key evolutions in [[techniques_for_improving_ai_model_efficiency | AI techniques]] and patterns:
*   **Prompting**: Learning to prompt models better and developing advanced [[techniques_for_improving_ai_model_efficiency | techniques]] like Chain of Thought <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Retrieval Augmented Generation (RAG)**: Grounding model responses with proprietary data became important <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Memory**: Crucial for multi-threaded conversations <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Long Context Models**: Enabled new use cases <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Graph RAG**: Experimenting with hierarchy of responses <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Reasoning Models**: Using models that take more time to think in real-time, developing new use cases <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
*   **[[building_effective_ai_agents | Agentic RAG]]**: Making workflows even more powerful <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

Even with these [[techniques_for_improving_ai_model_efficiency | techniques]], success requires understanding the problem deeply and adopting a test-driven development approach to find the right mix of [[techniques_for_improving_ai_model_efficiency | techniques]], [[ai_model_considerations | models]], and logic for a specific use case <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Test-Driven Development for Reliable AI Products
The most effective [[ai_implementation_and_best_practices | AI teams]] follow a structured approach: experiment, evaluate, scale, deploy, and then continuously monitor, observe, and improve their product <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### 1. Experimentation
Before building anything production-grade, extensive experimentation is needed to prove whether [[choosing_and_implementing_ai_models_for_data_analysis | AI models]] can solve the use case <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Try different prompting [[techniques_for_improving_ai_model_efficiency | techniques]]**: Few-shot or Chain of Thought, suitable for simple vs. complex reasoning tasks <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Test various [[techniques_for_improving_ai_model_efficiency | techniques]]**:
    *   **Prompt chaining**: Splitting instructions into multiple prompts <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   **[[building_effective_ai_agents | Agentic workflows]] (e.g., ReAct)**: Involve planning, reasoning, and refining before generating an answer <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Involve domain experts**: Engineers shouldn't be the sole prompt tweakers; involving experts saves engineering time <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Stay model agnostic**: Incorporate and test different [[ai_model_considerations | models]] to determine which are best for a specific use case (e.g., Gemini 2.0 Flash for OCR) <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### 2. Evaluation
Once models prove effective in experimentation, evaluation is critical to ensure performance under high request loads in production <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Create a dataset**: Develop a dataset of hundreds of examples to test models and workflows against <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Balance quality, cost, latency, and privacy**: No AI system achieves perfection in all areas, so defining priorities early is crucial (e.g., sacrificing speed for quality, or using a cheaper model if cost is critical) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **Use ground truth data**: Subject matter experts should design databases and test models against them. Synthetic benchmarks are less effective for specific use cases <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **LLM-based evaluation**: If ground truth data is unavailable, an LLM can evaluate another model's response; this is a standard and reliable method <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Flexible testing framework**: The framework should be dynamic to capture non-deterministic responses, allow custom metrics (Python, Typescript), and avoid strict structures <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Run evaluations at every stage**: Implement guardrails to check internal nodes and ensure correct responses at each step. Test during prototyping and re-evaluate with real data <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### 3. Deployment
Once satisfied with the product, deploy it to production <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   **Monitor more than deterministic outputs**: Log all LLM calls, track inputs, outputs, and latency <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
    *   [[ai_model_considerations | AI models]] are unpredictable; debugging and understanding behavior at every step is essential, especially with complex [[building_effective_ai_agents | agentic workflows]] that can take different paths and make their own decisions <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Handle API reliability**: Maintain stability with retries and fallback logic to prevent outages (e.g., using a different model if OpenAI goes down) <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Version control and staging**: Always deploy in controlled environments before wider public release. Ensure new updates don't introduce regressions or break existing workflows <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
*   **Decouple deployments**: Separate [[ai_implementation and best practices | AI feature]] updates from scheduled app deployments, as AI features often need more frequent updates <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

### 4. Continuous Improvement
After deployment, capture user responses to identify edge cases and continuously improve the workflow <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Feedback loops**: Capture responses, run evaluations again, and develop new prompts to solve new cases <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Caching layer**: For repeat queries, caching drastically reduces costs and improves latency by storing and serving frequent responses instantly instead of calling expensive LLMs <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Fine-tune custom models**: Use collected production data to [[custom_model_training and reinforcement learning | fine-tune custom models]] for specific use cases, reducing reliance on API calls and lowering costs <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## Agentic Workflows
The test-driven approach is even more critical for [[building_effective_ai_agents | agentic workflows]] due to their complexity, tool use, multiple APIs, and parallel execution <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Evaluation must not only measure performance at every step but also assess agent behavior to ensure correct decisions and adherence to intended logic <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

Every [[ai_implementation_and_best_practices | AI workflow]] has some level of [[building_effective_ai_agents | agentic behavior]], varying in control, reasoning, and autonomy <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>. A framework defines five levels of [[building_effective_ai_agents | agentic behavior]] <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>:

### Levels of Agentic Behavior
1.  **L0: Basic LLM Call** <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>
    *   Involves an LLM call, data retrieval from a vector database, and inline evaluations <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
    *   No external reasoning, planning, or decision-making beyond what's in the prompt or model behavior <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. The model itself does the reasoning within the prompt <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

2.  **L1: Tool Use** <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>
    *   The [[ai_implementation_and_best_practices | AI system]] uses tools (APIs) and decides *when* to call them and *when* to make actions <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.
    *   The model decides whether to call a tool or a vector database for data retrieval <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
    *   Memory plays a key role for multi-threaded conversations, capturing context <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
    *   Evaluation is needed at every step to ensure correct decisions, tool usage, and accurate responses <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
    *   Workflows can be simple or complex with branching and many tools <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
    *   Many production-grade solutions currently fall within the L1 segment (e.g., Redfin, Headspace) <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Focus is on orchestration: how models interact with systems and data <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.

3.  **L2: Structured Reasoning** <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>
    *   Workflows move beyond simple tool use to structured reasoning <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   The workflow notices triggers, plans actions, and executes tasks in a structured sequence <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
    *   Can break down tasks, retrieve info, call tools, evaluate usefulness, refine, and continuously loop to generate output <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.
    *   [[building_effective_ai_agents | Agentic behavior]] becomes more intentional; the system actively decides what needs to be done and spends more time thinking <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.
    *   The process is still finite, terminating after completing planned steps <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
    *   Most innovation this year is expected to happen at L2, with AI agents planning and reasoning using models like 01, 03, or DeepSeek <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

4.  **L3: Proactive Autonomy** <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>
    *   The system proactively takes actions without waiting for direct input <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
    *   Instead of terminating after a single request, it stays alive, continuously monitors its environment (e.g., email, Slack, Google Drive), and reacts as needed <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
    *   Can plan next moves, execute actions in real-time, or ask humans for input <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   [[ai_implementation_and_best_practices | AI workflows]] become less of a tool and more of an independent system, truly easing work <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

5.  **L4: Fully Creative/Inventor** <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>
    *   Goes beyond automation and reasoning to become an inventor <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>.
    *   Creates its own new workflows, utilities (agents, prompts, function calls, tools) <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
    *   Solves problems in novel ways <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
    *   Currently out of reach due to model constraints like overfitting (models loving their training data) and inductive bias (models making assumptions based on training data) <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. The goal is AI that invents, improves, and solves problems in unforeseen ways <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

L3 and L4 levels are still limited by current [[ai_model_considerations | models]] and surrounding logic <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

## Practical Example: SEO Agent
An SEO agent automates the entire SEO process, from keyword research to content analysis and creation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. It decides when to use tools and has an embedded evaluator <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. This workflow lies between L1 and L2 [[building_effective_ai_agents | agentic workflows]] <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

### Workflow Steps:
1.  **SEO Analyst & Researcher**:
    *   Takes a keyword (e.g., "Chain of Thought prompting") and parameters (writing style, audience) <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.
    *   Calls Google search to analyze top-performing articles for the keyword <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.
    *   Identifies strong components to amplify in the new article and missing segments/areas for improvement <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>.
    *   The researcher utilizes missing opportunities to perform further searches and gather more data, aiming for a superior article <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.
2.  **Writer**:
    *   Receives all research and planning information as context <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.
    *   Creates a comprehensive first draft, using context from analyzed articles <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
    *   Can connect to a RAG system to look into a database of articles and learnings <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>.
3.  **Editor**:
    *   An LLM-based judge that evaluates the first draft against predefined rules <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.
    *   Provides feedback to the writer <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.
    *   The feedback is passed back to the writer via a memory component (chat history) <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
    *   This feedback loop continues until specific criteria are met (e.g., editor deems the post "excellent," or a set number of loops are completed) <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
4.  **Final Article**: The process yields a useful, contextually rich article, not a generic, unhelpful piece <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.

This workflow saves significant time by providing a strong foundation for content creation <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>. Products like Vellum Workflows are designed to bridge product and engineering teams, speeding up [[ai_implementation_and_best_practices | AI development]] while adhering to a test-driven approach <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. The Vellum workflow SDK offers building blocks, customizability, and self-documenting syntax, keeping UI and code in sync for alignment across teams <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>.