---
title: Evaluating AI system performance
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

Companies that adopt a test-driven development approach are able to build reliable and stronger AI systems for production, from simple to more advanced agentic workflows <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Success for an AI product in production is not just about the models, but about how the system is built around them <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## The Evolution of AI and the Need for Evaluation

Initially, in 2023, many built AI wrappers, with arguments against their defensibility <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. However, companies like Cursor AI, an AI-powered IDE, achieved significant growth, demonstrating the impact of AI adoption <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This was partly due to models improving at coding and coding being an obvious target for disruption <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. More importantly, new techniques and patterns were developed to orchestrate models to work better, sync with data, and perform effectively in production <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

These techniques are crucial due to clear limits in model performance, such as hallucinations and overfitting <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. While model providers improved tooling, significant leaps in model capabilities, similar to the jump from GPT-3.5 to GPT-4, started to slow down <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Models began reaching limits on existing tests, despite more data <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Recently, new training methods like self-reinforced learning, which trains models without labeled data, have pushed the field forward <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Reasoning models now use Chain of Thought thinking at inference time, allowing them to "think" before answering and solve complex reasoning problems <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Model providers are also adding capabilities like tool use, research capabilities, and near-perfect OCR accuracy <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

However, traditional benchmarks are saturated, leading to the introduction of new ones to capture the performance of these reasoning models, especially for truly difficult tasks <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Test-Driven Development for Reliable AI Products

The best AI teams follow a structured, test-driven approach: they experiment, [[evaluating_ai_systems_at_scale | evaluate at scale]], deploy in production, and continuously monitor, observe, and improve their product <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This process is even more critical with [[evaluating_ai_agents_and_assistance | agentic workflows]] <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Stages of Evaluation

#### 1. Experimentation (Prototyping)
Before building anything production-grade, extensive experimentation is needed to prove if AI models can solve a given use case <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Try different prompting techniques:** Explore few-shot or Chain of Thought for simple or complex reasoning tasks <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.
*   **Test various techniques:** Prompt chaining can be effective by splitting instructions into multiple prompts, or adopt [[evaluating_ai_agents_and_assistance | agentic workflows]] like ReAct, which plan, reason, and refine answers <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Involve domain experts:** Engineers should not be the sole prompt tweakers; involving domain experts saves engineering time and validates the approach <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Stay model-agnostic:** Incorporate and test different models to find which performs best for the specific use case <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

#### 2. Evaluation (At Scale)
Once proof of concept is established, the next stage involves [[evaluating_ai_systems_at_scale | evaluating at scale]] to ensure production readiness for hundreds or millions of requests per minute <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Create a dataset:** Build a dataset of hundreds of examples to test models and workflows against <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Balance quality, cost, latency, and privacy:** Define priorities early, as trade-offs are inevitable. For example, high quality might sacrifice speed, or cost-critical applications might use lighter, cheaper models <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Use ground truth data:** Subject matter experts designing databases and testing models against them is very useful <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Synthetic benchmarks help but may not fully evaluate for specific use cases <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Utilize LLMs for evaluation:** If ground truth data is unavailable, an LLM can reliably evaluate another model's response <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Flexible testing framework:** The framework should be dynamic to capture non-deterministic responses, allow custom metric definitions (e.g., using Python or TypeScript), and avoid strict limitations <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Run evaluations at every stage:** Implement guard rails to check internal nodes and ensure correct responses at every step of the workflow <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. [[steps_to_create_effective_evaluations_for_ai_applications | Evaluations]] should be run during prototyping and revisited with real data after deployment <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

#### 3. Deployment (Production)
Once satisfied with evaluation, the product can be deployed <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Monitor beyond deterministic outputs:** Log all LLM calls, track inputs, outputs, and latency, as AI models are unpredictable <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This is especially important for [[evaluating_ai_agents_and_assistance | agentic workflows]] which can take different paths and make decisions <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Handle API reliability:** Maintain stability in API calls with retries and fallback logic to prevent outages <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
*   **Version control and staging:** Always deploy in controlled environments before wider public rollout to prevent regressions when updating prompts or other workflow parts <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Decouple AI feature deployments from overall app deployment schedules, as AI features may need more frequent updates <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

#### 4. Continuous Improvement
After deployment, capture user responses to create a feedback loop for identifying edge cases and continuously improving the workflow <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **Re-run evaluations:** Use captured production data to re-evaluate and test new prompts that address emerging cases <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Build a caching layer:** For repeat queries, caching can drastically reduce costs and improve latency by storing and serving frequent responses instantly <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Fine-tune custom models:** Over time, use production data to fine-tune custom models, which can create better responses for specific use cases, reduce reliance on API calls, and lower costs <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## Evaluating AI Agents

When it comes to [[evaluating_ai_agents_and_assistance | agentic workflows]], evaluation is not just about measuring performance at every step, but also about assessing the agents' behavior to ensure they make correct decisions and follow intended logic <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

A framework for [[evaluating_ai_agents_methods_and_metrics | agentic behavior]] defines different levels based on control, reasoning, and autonomy:
*   **L0: Simple LLM Call + RAG:** An LLM call retrieves data (e.g., from a vector database) with inline evaluations. Reasoning is primarily within the prompt and model behavior, with no external agent organizing decisions <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   **L1: Tool-Using Agent:** The AI system uses tools, deciding when to call APIs or retrieve data from a vector database. Memory plays a key role for multi-threaded conversations, and evaluation is needed at every step to ensure correct decisions and accurate responses when using tools <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
*   **L2: Structured Reasoning Agent:** Workflows move beyond simple tool use to structured reasoning. They notice triggers, plan actions, and execute tasks in a structured sequence, breaking down tasks into multiple steps, retrieving information, calling tools, and refining as needed. The agent's behavior is more intentional, actively deciding what needs to be done <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. This process is finite; the workflow terminates after completing its planned steps <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
*   **L3: Proactive & Autonomous Agent:** These systems proactively take actions without direct input, continuously monitoring their environment and reacting as needed. They can interact with external services (email, Slack, Google Drive) and plan next moves, either executing actions or requesting human input. They act less as tools and more as independent systems <a class="yt-timestamp" data-t="00:18:33">[00:18:33]</a>.
*   **L4: Fully Creative/Inventor Agent:** The AI moves beyond automation and reasoning to invent, creating its own new workflows, utilities (agents, prompts, function calls, tools), and solving problems in novel ways. This level is currently out of reach due to model constraints like overfitting and inductive bias <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

Currently, many production-grade solutions are at the L1 segment, focusing on orchestrating models to interact better with systems and data <a class="yt-timestamp" data-t="00:20:41">[00:20:41]</a>. Significant innovation is expected at L2 this year, with AI agents developing to plan and reason for complex tasks <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. L3 and L4 are still limited by current models and surrounding logic <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.

### Practical Example: An SEO Agent
An SEO agent demonstrates [[strategies_for_ai_evaluation_and_troubleshooting | evaluation]] in practice by automating keyword research, content analysis, and creation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. This workflow operates between L1 and L2 <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>:
1.  **SEO Analyst/Researcher:** Takes a keyword and other parameters (writing style, audience), calls Google Search, and analyzes top-performing articles <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>. It identifies strengths to amplify and missing segments or areas for improvement <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. The researcher then uses these identified missing pieces to perform additional searches and gather more data <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>.
2.  **Writer:** Uses the research and planning information as context to create a first draft <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  **Editor (LLM-based Judge):** Evaluates the first draft against predefined rules (set in its prompt). This feedback is passed back to the writer through a memory component (chat history) <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>. This forms a continuous loop until certain criteria are met, ensuring a useful and impressive first draft <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a>. This agent features an embedded evaluator that tells the agent if it's performing well <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>, which is a form of [[human_reviews_of_ai_outputs | human review of AI outputs]] (or LLM as human review substitute).

This iterative process of analysis, writing, and LLM-based [[evaluations_versus_traditional_metrics_in_ai | evaluation]] allows for the creation of high-quality content that leverages comprehensive context <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.