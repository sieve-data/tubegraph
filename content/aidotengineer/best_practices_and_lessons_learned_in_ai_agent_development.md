---
title: Best practices and lessons learned in AI agent development
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

OpenAI observes that 2025 is expected to be the year of AI agents, with generative AI transitioning from an assistant role to a co-barker [00:08:41]. Through work with customers and internal product development, OpenAI has identified key patterns and anti-patterns in [[developing_and_optimizing_ai_agents | AI agent development]] [00:08:51].

## Defining an AI Agent
An AI agent is an application comprising a model with instructions (usually a prompt), access to tools for information retrieval and external system interaction, all within an execution loop controlled by the model [00:09:04]. In each cycle, the agent receives natural language instructions, decides whether to issue tool calls, runs those tools, synthesizes a response, and provides an answer to the user [00:09:26]. The agent can also determine when its objective is met and terminate the loop [00:09:43].

## OpenAI's Enterprise AI Customer Journey
OpenAI typically sees the enterprise AI customer journey in three phases [00:01:47]:
1.  **AI-Enabled Workforce**
    *   Getting AI into employees' hands to foster AI literacy and daily use [00:01:54].
    *   This typically starts with products like ChatGPT [00:02:30].
2.  **Automating AI Operations**
    *   Building internal automation and co-pilot use cases [00:02:11].
    *   More complex or customized internal use cases often utilize the API [00:02:40].
3.  **Infusing AI into End Products**
    *   Integrating AI into end-user-facing products, primarily via API use cases [00:02:22].

OpenAI's approach to enterprise strategy involves [00:03:07]:
*   **Top-Down Strategic Guidance**
    *   Aligning AI initiatives with the broader business strategy [00:03:17].
*   **Identify High-Impact Use Cases**
    *   Scoping one or two significant use cases to deliver initial value [00:03:36].
*   **Build Divisional Capability**
    *   Enabling teams and infusing AI throughout the organization through enablement, Centers of Excellence, or centralized technological platforms [00:03:52].

### The Use Case Journey
A typical use case journey, illustrated over a three-month example, involves [00:04:31]:
1.  **Ideation & Scoping**
    *   Initial ideation, scoping, architecture review, and defining success metrics/KPIs [00:04:40].
2.  **Development**
    *   The bulk of the time, involving iterative prompting strategies, RAG, and continuous improvement [00:04:53].
    *   OpenAI's team provides close interaction through workshops, office hours, paired programming, and webinars [00:05:06].
3.  **Testing & Evaluation**
    *   Performing A/B testing and beta rollouts based on predefined evaluation metrics [00:05:24].
4.  **Production & Maintenance**
    *   Launch, rollout, scale optimization testing, followed by ongoing maintenance [00:05:37].

OpenAI supports this process by providing dedicated teams, early access to new models and features, internal experts from research and engineering, and joint roadmap sessions [00:05:55].

### Case Study: Morgan Stanley Internal Knowledge Assistant
Morgan Stanley built an internal knowledge assistant to help wealth managers query a large corpus of information, including research reports and stock data, to provide highly accurate information to clients [00:06:54]. Initially, accuracy was around 45% [00:07:21]. By introducing methods like [00:07:23]:
*   High retrieval
*   Fine-tuning embeddings
*   Different chunking strategies
*   Reranking
*   Classification steps
*   Prompt engineering
*   Query expansion

Accuracy improved significantly, reaching 85% and ultimately 98% (surpassing the 90% goal) [00:07:33]. This [[case_study_of_ai_interview_agent_development | case study]] demonstrates the iterative approach to improving core metrics through the use case journey [00:07:48].

## [[best_practices_for_building_ai_systems | Best Practices for Building AI Systems]]: Four Lessons in AI Agent Development
When designing AI agents, OpenAI has identified four key lessons to address [[challenges_in_developing_ai_agents | challenges in developing AI agents]] and improve performance [00:09:51].

### 1. Start Simple, Optimize, and Abstract Minimally
When orchestrating models, retrieving data, and generating output, teams have two choices: start with primitives (raw API calls, manual logging) or a framework (abstractions handling details) [00:10:00]. While frameworks are enticing for quick proof-of-concepts, they can obscure system behavior and underlying primitives, deferring [[design_challenges_for_ai_agents | design decisions]] before constraints are understood, hindering optimization [00:10:33].

A better approach is to [00:10:50]:
*   **Build with Primitives First**: Understand how the task decomposes, where failures occur, and what needs improvement [00:10:53].
*   **Introduce Abstraction When Necessary**: Only abstract when reinventing the wheel (e.g., re-implementing an embedding strategy or model graders) [00:11:05].

> "[[best_practices_for_building_ai_systems | Developing agents]] in a scalable way isn't so much about choosing the right abstraction, it's really about understanding your data, understanding your failure points, and your constraints" <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### 2. Start with a Single Agent, Then Incrementally Improve
Teams often jump directly into designing multi-agent systems, but this can create unknowns and limit insights [00:11:48]. A recommended approach is to [00:12:08]:
*   **Start with a Purpose-Built Single Agent**: Deploy it into production with a limited user set and observe its performance [00:12:10].
*   **Identify Bottlenecks**: This allows identification of real issues like hallucinations over conversation trajectories, low adoption due to latency, or inaccuracy from poor retrieval performance [00:12:21].
*   **Incrementally Improve**: Knowing how the system underperforms and what's important to users allows for targeted, incremental improvements [00:12:33].

Complexity should increase as more intense failure cases and constraints are discovered, as the goal is to build a working system, not just a complicated one [00:12:44].

### 3. Graduate to a Network of Agents with Handoffs for Complex Tasks
For more complex tasks, a network of agents and the concept of handoffs become valuable [00:13:03].
*   **Network of Agents**: A collaborative system where multiple agents work in concert to resolve complex requests or perform a series of interrelated tasks. This allows for specialized agents to handle sub-flows within a larger agentic workflow [00:13:17].
*   **Handoffs**: The process by which one agent transfers control of an active conversation to another agent, preserving the entire conversation history and context [00:13:38].

For example, a fully automated customer service flow could use [00:14:03]:
*   A GPT-4o mini call for triage on incoming requests [00:14:16].
*   A GPT-4o on a "dispute agent" to manage the conversation [00:14:23].
*   An O3 mini reasoning model for accuracy-sensitive tasks like checking refund eligibility [00:14:30].

Handoffs are effective because they keep the conversation history and context intact while allowing the model, prompt, and tool definitions to be swapped, providing flexibility for a wide range of scenarios [00:14:39].

### 4. Implement Guardrails in Parallel, Not in Prompts
Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and maintaining system integrity [00:14:55].
*   **Keep Prompts Simple**: Model instructions should be simple and focused on the target task to ensure maximum interoperability, accuracy, and predictable performance [00:15:12].
*   **Run Guardrails in Parallel**: Guardrails should not typically be part of the main prompts but rather run in parallel, a practice made more accessible by faster and cheaper models like GPT-4o mini [00:15:25].
*   **Defer High-Stakes Actions**: Tool calls and user responses that are high-stakes (e.g., issuing a refund, showing personal account information) should be deferred until all guardrails have returned their results [00:15:42].

An example involves running a single input guardrail to prevent prompt injection and a couple of output guardrails on the agent's response [00:15:57].