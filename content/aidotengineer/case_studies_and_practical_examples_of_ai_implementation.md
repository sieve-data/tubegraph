---
title: Case studies and practical examples of AI implementation
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

This article explores how enterprises can build and scale AI use cases, focusing on OpenAI's approach, common customer journeys, strategic implementation, and lessons learned from deploying AI agents in the field.

## OpenAI's Operational Model
OpenAI operates with two core engineering teams:
*   **Research Team** A group of 1,200 researchers focused on inventing and deploying foundational models <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Apply Team** This team takes the foundational models and builds them into products, such as ChatGPT and the OpenAI API <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The go-to-market team then deploys these products to end-users, helping organizations automate internal operations and integrate AI into their workforce and products <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. An iterative loop ensures that feedback from the field directly improves both products and core models <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The Enterprise AI Customer Journey
OpenAI observes the enterprise AI customer journey typically happening in three phases <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:

1.  **Building an AI-Enabled Workforce** <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>: This initial step involves getting AI into the hands of employees to foster AI literacy and daily use <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. ChatGPT is typically the starting point for this phase <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Automating Internal Operations** <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>: This phase focuses on internal use cases, building automation, or implementing co-pilot type functionalities <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While ChatGPT can contribute, the API is often utilized for more complex or customized needs <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  **Infusing AI into End Products** <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>: The final step involves integrating AI into end-user facing products, primarily leveraging API use cases <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

## Crafting an Enterprise AI Strategy
[[strategies_for_effective_ai_implementation | Strategies for effective AI implementation]] for AI adoption within an enterprise typically follow a structured approach:

1.  **Define Broad Business Strategy First** <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>: The primary focus should be on the overarching business strategy, with AI technology serving as a tool to achieve those strategic goals <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
2.  **Identify High-Impact Use Cases** <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>: Select one or two significant, high-impact use cases to begin with, ensuring clear scope and deliverables <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
3.  **Build Divisional Capability** <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>: Enable teams and infuse AI throughout the organization through various means, including enablement programs, establishing Centers of Excellence, or building a centralized technological platform <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Use Case Journey Playbook
A typical use case journey, illustrated often over a three-month period, involves several key phases <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>:

1.  **Ideation & Scoping** <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>: This involves initial brainstorming, architecture review to fit AI into the existing stack, and clearly defining success metrics and KPIs <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Development** <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>: The bulk of the time is spent here, iterating on prompting strategies and Retrieval Augmented Generation (RAG) to continuously improve the use case <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. OpenAI teams often engage closely during this phase through workshops, office hours, and paired programming <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
3.  **Testing & Evaluation** <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>: Utilize pre-defined evaluation metrics for A/B testing and beta rollouts to understand real-world performance <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
4.  **Production** <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>: Involves launch rollout and scale optimization testing to ensure functionality when deployed to many users <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, followed by ongoing maintenance <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

OpenAI supports partners with early access to new models and features, insights into future roadmaps, and access to internal experts for acceleration and joint roadmap sessions <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Case Study: Morgan Stanley's Internal Knowledge Assistant
[[case_study_of_ai_application_in_documentation | Case study of AI application in documentation]]
Morgan Stanley collaborated with OpenAI to build an internal knowledge assistant for their wealth managers <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The goal was to provide highly accurate information from a vast corpus of knowledge, including research reports and live stock data, to enable wealth managers to respond to clients effectively <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

*   **Initial Accuracy:** The initial accuracy was low, around 45% <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Intervention & Improvement:** OpenAI introduced methods like:
    *   **Hybrid Retrieval** <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
    *   **Fine-tuning embeddings** <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
    *   **Different chunking strategies** <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
    *   **Reranking and classification steps** <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
    *   **Prompt engineering and query expansion** <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>
*   **Result:** The accuracy improved significantly, reaching 98% against a goal of 90% <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

## Emerging Trend: AI Agents
There's a growing focus on AI agents, with 2025 anticipated as "the year of Agents" where Generative AI truly graduates from being an assistant to a co-worker <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
An agent is defined as an AI application with:
*   A model that has instructions (usually a prompt) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   Access to tools for information retrieval and external system interaction <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   An execution loop, controlled by the model, allowing it to determine its objectives and terminate when met <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   In each cycle, an agent receives natural language instructions, decides whether to use tools, runs them, synthesizes a response with tool values, and provides an answer to the user <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

## Lessons Learned from Building AI Agents
[[implementing_ai_agents_in_daily_operations | Implementing AI agents in daily operations]]

OpenAI has identified four key insights for building scalable AI agents:

### 1. Start with Primitives, Abstract Minimally
Many teams are tempted to start with frameworks for rapid proof-of-concept, but this can obscure the system's behavior and underlying primitives <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Recommendation:** Begin building with primitives (raw API calls, manual logging) to understand task decomposition, failure points, and areas for improvement <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. Introduce abstractions only when re-implementing common elements like embedding strategies or model graders <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **Key Idea:** Scalable agent development is about understanding data, failure points, and constraints, not primarily about choosing the right abstraction <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### 2. Start Simple with a Single Agent
Jumping directly into complex multi-agent systems with dynamic reasoning often creates unknowns without yielding much insight <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
*   **Recommendation:** Start with a single agent purpose-built for a specific task, deploy it with limited users, and observe its performance <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This approach helps identify real bottlenecks like hallucinations, latency, or retrieval inaccuracies <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
*   **Key Idea:** Complexity should be introduced incrementally as more intense failure cases and constraints are discovered; the goal is a working system, not a complicated one <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### 3. Leverage Networks of Agents and Handoffs for Complexity
For more complex tasks, a network of agents collaborating can provide true value <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Network of Agents:** A collaborative system where multiple agents work together to resolve complex requests or perform interrelated tasks, often through specialized agents handling sub-flows <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   **Handoffs:** The process where one agent transfers control of an active conversation to another <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This is analogous to a phone call transfer but preserves the entire conversation history, allowing the new agent to seamlessly continue <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Example (Customer Service):** A fully automated customer service flow can use a network of agents. For instance, a GPT-4o mini performs triage, a GPT-4o dispute agent manages the conversation, and an O3 mini reasoning model handles accuracy-sensitive tasks like refund eligibility checks <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Handoffs effectively swap models, prompts, and tool definitions while retaining context <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

### 4. Implement Guardrails in Parallel
Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and maintaining integrity <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
*   **Recommendation:** Keep model instructions simple and focused on the target task for maximum interoperability and predictable performance <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. Guardrails should not be part of the main prompts but run in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The proliferation of faster, cheaper models like GPT-4o mini makes this more accessible <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Application:** High-stakes tool calls or user responses (e.g., issuing a refund, sharing personal information) can be deferred until all guardrails have returned a clear signal <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

> [!SUMMARY] Lessons from Building Agents
> 1.  Use abstractions minimally <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
> 2.  Start with a single agent <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
> 3.  Graduate to a network of agents for more intense scenarios <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
> 4.  Keep prompts simple and focused on the "happy path," using guardrails for edge cases <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.