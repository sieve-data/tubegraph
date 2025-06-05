---
title: Test driven development for AI
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

In the realm of AI solutions, from simple applications to advanced [[building_effective_ai_agents | agentic workflows]], a key differentiator for companies successfully deploying reliable AI in production has been the adoption of a test-driven development (TDD) approach <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This methodology enables the creation of stronger and more reliable systems for production <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Evolution of AI Development
Around 2023, many AI wrappers were being built, and questions arose about their defensibility strategy <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. However, the field progressed significantly, as exemplified by Cursor AI, an AI-powered IDE that achieved 100 million ARR in just 12 months <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This rapid growth was attributed to several factors:
*   Models improved at coding <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   AI adoption skyrocketed <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   Coding was an obvious target for AI disruption <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   Crucially, new techniques and patterns emerged for orchestrating models to work better with data and effectively in production <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

These techniques became vital due to inherent [[challenges_in_ai_development | limitations in model performance]], such as hallucinations and overfitting <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. While model providers have shipped better tooling, significant leaps in model performance, like the jump from GPT-3.5 to GPT-4, have slowed down <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For years, making models bigger and feeding them more data made them smarter, but this approach hit a wall, with improvements slowing down and models reaching limits on existing tasks <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

However, new training methods have emerged, pushing the field forward <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. For example, the DeepSeek-R1 model was trained using real reinforcement learning, meaning it learned autonomously without labeled data <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. This method is reportedly used by OpenAI for their reasoning models (e.g., O1, O3), which employ Chain of Thought thinking at inference time to enable complex reasoning <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Model providers are also adding more capabilities, such as [[tool_usage_and_development_in_ai_frameworks | tool usage]], research capabilities, and near-perfect OCR accuracy (e.g., Gemini 2.0 Flash) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

As traditional benchmarks become saturated, new ones are being introduced to capture the performance of these reasoning models, like the Humanities Last Exam, which measures performance on difficult tasks <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Beyond just model improvements, success in production AI products is increasingly about how systems are built around the models <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This has led to the evolution of several techniques:
*   **Prompting**: Advanced techniques like Chain of Thought for better model interaction <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Retrieval Augmented Generation (RAG)**: Grounding model responses with proprietary data <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Memory**: Essential for multi-threaded conversations and long context from models <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Graph RAG**: Experimentation with hierarchy of responses <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
*   **Agentic RAG**: Combining reasoning models with RAG for more powerful workflows <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

However, even with these techniques, deep understanding of the problem and a [[strategies_for_ai_evaluation_and_troubleshooting | test-driven development approach]] are necessary to find the right mix of techniques, models, and logic for a specific use case <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## The Test-Driven Development Approach in AI
The most effective AI teams follow a structured TDD approach <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>:
1.  **Experiment**: Explore initial concepts and proofs of concept <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Evaluate**: Rigorously test and refine the system <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
3.  **Scale**: Prepare for handling larger loads <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
4.  **Deploy**: Roll out the solution to production <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
5.  **Monitor, Observe, and Improve**: Continuously capture responses and feedback from production to refine the product <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Stages of TDD in AI

#### 1. Experimentation
Before building anything production-grade, extensive experimentation is crucial to prove that AI models can solve the specific use case <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   **Try different prompting techniques**: Explore few-shot, Chain of Thought, or prompt chaining, splitting instructions into multiple prompts for better results <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Adopt agentic workflows**: Techniques like React, which involve planning, reasoning, and refining before generating an answer <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Involve domain experts**: Engineers should not be the sole prompt tweakers; domain experts can save significant engineering time by validating proofs of concept <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Stay model agnostic**: Incorporate and test different models to identify which ones perform best for specific use cases (e.g., Gemini 2.0 Flash for OCR) <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

#### 2. [[Evaluations and finetuning in AI development | Evaluation]]
Once a proof of concept is established, the evaluation stage involves creating a dataset of hundreds of examples to test models and workflows against <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Balance quality, cost, latency, and privacy**: Define priorities early, as no AI system can perfectly optimize all these factors <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Trade-offs are necessary; for example, high quality might sacrifice speed, or critical cost might necessitate lighter models <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Use ground truth data**: Subject matter experts designing datasets and testing workflows against them is highly useful for accurate [[steps_to_create_effective_evaluations_for_ai_applications | evaluation]] <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Synthetic benchmarks can help but won't fully evaluate for specific use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Utilize LLMs for evaluation**: Even without ground truth data, an LLM can reliably evaluate another model's response <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Employ a flexible testing framework**: Whether in-house or external, the framework must be dynamic to capture non-deterministic responses, allow custom metrics (e.g., Python, Typescript), and avoid strict structures, emphasizing customizability <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Run evaluations at every stage**: Implement guardrails to check internal nodes and ensure models produce correct responses at every step of the workflow <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Test during prototyping and leverage the evaluation phase with real data <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

#### 3. Deployment
Once workflows are extensively evaluated and satisfactory, they are ready for production deployment <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Monitor non-deterministic outputs**: Log all LLM calls, track inputs, outputs, and latency <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. AI models are unpredictable, so debugging issues and understanding behavior at every step is critical, especially for complex [[technical_challenges_in_ai_agent_development | agentic workflows]] that can take different paths and make autonomous decisions <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   **Handle API reliability**: Maintain stability in API calls with retries and fallback logic to prevent outages (e.g., if a primary model provider experiences downtime) <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Version control and staging**: Always deploy in controlled environments before wider public rollouts <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. This ensures prompt updates don't introduce regressions or break existing production workflows <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Decouple deployments**: AI feature updates will likely be more frequent than overall app deployments, so independent deployment schedules are advisable <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

#### 4. Continuous Improvement
After deployment, the focus shifts to ongoing enhancement.
*   **Create feedback loops**: Capture user responses from production to identify edge cases for continuous improvement <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Re-run [[evaluations_and_finetuning_in_ai_development | evaluations]] with this new data to test new prompts or solutions <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Build a caching layer**: For systems handling repeat queries, caching significantly reduces costs and improves latency by storing and serving frequent responses instantly instead of repeatedly calling expensive LLMs <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **[[Evaluations and finetuning in AI development | Fine-tune]] custom models**: Once sufficient reliable production data is collected, it can be used to fine-tune custom models for better responses specific to the use case, potentially reducing reliance on API calls and lowering costs <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### Test-Driven Development for Agentic Workflows
The TDD process becomes even more critical for [[building_effective_ai_agents | agentic workflows]] <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a> because these workflows are characterized by:
*   Wide range of [[tool_usage_and_development_in_ai_frameworks | tool usage]] and API calls <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Multi-agent structures executing tasks in parallel <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   Complex decision-making and autonomous paths <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

For [[building_effective_ai_agents | agentic workflows]], evaluation is not just about measuring performance at every step, but also assessing the behavior of agents to ensure they make the right decisions and follow intended logic <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

#### Levels of Agentic Behavior
A framework defines different levels of agentic behavior based on their control, reasoning, and autonomy <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>:

*   **L0 (Basic LLM Call)**: An LLM call retrieves data from a vector database with inline evaluations, producing a response <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. Reasoning is baked into the prompt and model behavior; no external agent organizes decisions or plans <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **L1 (Tool Usage)**: The system can now use tools, deciding *when* to call APIs or retrieve data from a vector database <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. Memory plays a key role for multi-threaded conversations, capturing context throughout the workflow <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. Evaluation is needed at every step to ensure correct decisions and accurate responses <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. This can range from simple to very complex workflows with multiple tools and branching logic <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   **L2 (Structured Reasoning)**: Workflows move beyond simple tool use to structured reasoning <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. The system notices triggers, plans actions, and executes tasks in a structured sequence <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. It can break down tasks, retrieve information, call tools, evaluate their usefulness, and refine as needed in a continuous loop to generate a final output <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Agentic behavior is more intentional, actively deciding what needs to be done and spending more time thinking <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. The process is still finite, terminating once steps are completed <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **L3 (Autonomy)**: Systems proactively take actions without direct input <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>. Instead of terminating after a single request, they continuously monitor their environment and react as needed <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. They can access external services (email, Slack, Google Drive) to plan next moves or ask for human input <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. These become independent systems that ease work <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
*   **L4 (Creative/Inventor)**: The AI moves beyond automation and reasoning to become an inventor <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. It can create its own new workflows, utilities (agents, prompts, function calls, tools), and solve problems in novel ways <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. True L4 is currently out of reach due to model constraints like overfitting and inductive bias, but it represents the goal of AI that invents, improves, and solves problems in unforeseen ways <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

Currently, many production-grade AI solutions fall within the L1 segment, focusing on orchestrating models to interact better with systems and data <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. L2 is expected to see the most innovation in the near future, with AI agents being developed to plan and reason for complex tasks <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. L3 and L4 are still limited by current models and surrounding logic, though innovation continues in these areas <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

### Example: SEO Agent Workflow
An example of an [[developing_ai_agents_for_productivity | effective agentic workflow]] is an SEO agent that automates the SEO process from keyword research to content creation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. This agent, which sits between L1 and L2 type agentic workflows <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>, includes:
*   **SEO Analyst and Researcher**: Takes a keyword and calls Google Search to analyze top-performing articles <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>. It identifies strong components to amplify and missing segments for improvement <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. The researcher then conducts further searches to gather more data <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.
*   **Writer**: Uses the gathered information as context to create a first draft <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>. The content is designed to be useful and contextually relevant, not just generic <a class="yt-timestamp" data-t="00:26:13">[00:26:13]</a>.
*   **Editor**: An LLM-based judge evaluates the first draft against predefined rules <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. Feedback is passed back to the writer in a continuous loop until specific criteria are met <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
*   **Memory Component**: Captures all previous conversations between the writer and editor within the loop <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

This process ensures a useful and impressive first draft that leverages context intelligently <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.

## Bellum Workflows SDK
Bellum Workflows was designed to bridge the gap between product and engineering teams, accelerating AI development while adhering to a [[best_practices_for_implementing_ai_in_teams | test-driven approach]] <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. Recognizing developers' desire for more control and flexibility, the workflow SDK provides building blocks that are infinitely customizable, with a self-documenting syntax that reveals agent behavior directly in the code <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Its expressiveness ensures understanding at every stage, and the UI and code remain synchronized for team alignment during definition, debugging, or improvement <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. The SDK is open source and free <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>.