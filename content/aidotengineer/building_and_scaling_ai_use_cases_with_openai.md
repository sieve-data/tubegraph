---
title: Building and scaling AI use cases with OpenAI
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

This article outlines OpenAI's approach to [[Building and scaling AI use cases with OpenAI | building and scaling AI use cases]] within enterprises, detailing their internal structure, the customer journey, strategic implementation, and specific lessons learned from [[building_effective_ai_agents | building effective AI agents]].

## OpenAI's Operational Structure

OpenAI operates with two core engineering teams:
*   **Research Team** This team consists of 1,200 researchers who invent and deploy foundational models [00:00:48]. These models are considered the "core" technology [00:01:36].
*   **Apply Team** This team takes the foundational models and builds them into products such as ChatGPT and the API, making GPT models available for deployment [00:01:00].

OpenAI also has a "go-to-market" team responsible for getting these products into the hands of end-users, enabling workforce automation and streamlining internal operations [00:01:11].

An iterative feedback loop is crucial to OpenAI's process, where field feedback is used to directly improve products and enhance core models through a "research flywheel" [00:01:27].

## The AI Customer Journey for Enterprises

OpenAI observes the enterprise AI customer journey typically unfolds in three phases, though not strictly sequential [00:01:47]:

1.  **Building an AI-Enabled Workforce**
    *   **Goal**: To make employees AI literate and integrate AI into their daily work [00:01:54].
    *   **Product**: ChatGPT is the primary tool for enabling the workforce [00:02:30].

2.  **Automating AI Operations**
    *   **Goal**: To implement internal use cases, build automation, or create co-pilot-type solutions within the workforce [00:02:11].
    *   **Product**: ChatGPT can be used partially, but the API is typically employed for more complex or customized use cases [00:02:38].

3.  **Infusing AI into End Products**
    *   **Goal**: To integrate AI directly into end-user-facing products [00:02:22].
    *   **Product**: Primarily involves API use cases [00:02:48].

## Crafting an Enterprise AI Strategy

OpenAI emphasizes that enterprises should not focus solely on an "AI strategy" but rather on their "broader business strategy," identifying where AI technology can align and support it [00:03:17]. The strategic process involves:

1.  **Top-Down Strategic Guidance**: Determine the overall strategy from a high level [00:03:10].
2.  **Identify High-Impact Use Cases**: Select one or two significant use cases with high potential impact to begin with [00:03:36].
3.  **Build Divisional Capability**: After executing initial use cases, enable teams and infuse AI throughout the organization [00:03:52]. This can be achieved through enablement programs, establishing centers of excellence, or building centralized technological platforms [00:03:59].

## Use Case Development Journey

A typical use case journey, illustrated over approximately three months, follows these phases [00:04:31]:

1.  **Ideation & Definition**
    *   Initial scoping and architecture review to integrate AI into the existing tech stack [00:04:42].
    *   Clearly define success metrics and KPIs [00:04:50].
2.  **Development**
    *   The bulk of the time is spent here, involving iterative prompting strategies and RAG (Retrieval Augmented Generation) improvements [00:04:53].
    *   OpenAI's team (e.g., solution architects) closely collaborates through workshops, office hours, paired programming, and webinars to accelerate the use case [00:05:06].
3.  **Testing & Evaluation**
    *   Utilize pre-defined evaluations (evals) to conduct A/B testing and beta rollouts to assess real-world performance [00:05:24].
4.  **Production**
    *   Involves launch rollout and scale optimization testing to ensure functionality for many end-users [00:05:37].
    *   Followed by ongoing maintenance [00:05:45].

For successful collaboration, OpenAI brings a dedicated team and asks partners to commit a dedicated team as well [00:05:55]. Key benefits of partnering with OpenAI include:
*   **Early Access**: Customers gain early access to new models and features, offering insight into OpenAI's roadmap (typically 6 months out) to enable future innovation [00:06:05].
*   **Expert Engagement**: Internal experts from research, engineering, and product teams assist in accelerating development [00:06:35].
*   **Joint Roadmap Sessions**: Collaborative sessions ensure alignment with the customer's future roadmap [00:06:42].

### Case Study: Morgan Stanley

OpenAI partnered with Morgan Stanley to develop an internal knowledge assistant for their wealth managers [00:06:54].
*   **Problem**: Wealth managers needed to ask questions of a vast knowledge corpus (research reports, live stock data) and receive highly accurate information to respond to clients [00:07:00]. Initial accuracy was low, around 45% [00:07:19].
*   **Solution**: OpenAI introduced various methods throughout development [00:07:23]:
    *   High-retrieval techniques [00:07:26]
    *   Fine-tuning and embeddings [00:07:28]
    *   Different chunking strategies [00:07:29]
    *   Reranking and classification steps [00:07:36]
    *   Prompt engineering and query expansion [00:07:44]
*   **Result**: Accuracy significantly improved, reaching 85% with reranking and classification, and ultimately 98% (surpassing the 90% goal) through continued method introduction [00:07:37].

## The Rise of AI Agents

There's a strong belief that 2025 will be "the year of Agents," where generative AI truly transitions from being an assistant to a co-worker [00:08:02]. OpenAI has gathered best practices and "battle scars" from building these [[scaling_ai_agents_in_production | agentic workflows]] in the field [00:08:14].

### Defining an AI Agent

OpenAI defines an agent as an AI application comprising [00:09:02]:
*   A model with instructions, typically in the form of a prompt [00:09:04].
*   Access to tools for retrieving information and interacting with external systems [00:09:11].
*   An execution loop, controlled by the model, that determines its termination [00:09:16].

In each cycle, an agent receives natural language instructions, decides whether to call tools, runs them, synthesizes a response using tool return values, and provides an answer to the user. The agent can also determine when it has met its objective and terminate the execution loop [00:09:24].

### Lessons Learned in [[building_effective_ai_agents | Building Effective AI Agents]]

OpenAI has identified four key lessons in [[building_effective_ai_agents | building effective AI agents]]:

1.  **Use Abstractions Minimally: Build with Primitives First**
    *   **Problem**: Starting with frameworks is enticing for quick proofs of concept but often hides how the system behaves or what primitives it uses, deferring design decisions before constraints are understood [00:10:23]. This prevents optimization [00:10:48].
    *   **Solution**: First, [[scaffolding_ai_agents_for_scalability | build with primitives]] to understand task decomposition, failure points, and necessary improvements [00:10:53]. Introduce abstractions only when re-implementing common components (e.g., embedding strategies, model graders) [00:11:05].
    *   **Insight**: [[scaling_ai_agents_in_production | Developing agents in a scalable way]] is less about choosing the right framework and more about understanding data, failure points, and constraints [00:11:23]. The lesson is to start simple, optimize when needed, and abstract only when it improves the system [00:11:35].

2.  **Start with a Single Agent, Graduate to a Network**
    *   **Problem**: Jumping directly into multi-agent systems with dynamic reasoning and long trajectories creates many unknowns and provides little insight [00:11:48].
    *   **Solution**: Begin with a single agent purpose-built for a single task and deploy it to a limited user set [00:12:10]. Observe its performance to identify real bottlenecks such as hallucinations, high latency, or inaccuracy due to poor retrieval [00:12:21]. Incrementally improve the system based on user needs and underperformance [00:12:35].
    *   **Insight**: Complexity should increase as more intense failure cases and constraints are discovered. The goal is to build a system that works, not a complicated one [00:12:44].

3.  **Network of Agents and Handoffs for Complex Tasks**
    *   **Definition**: A **network of agents** is a collaborative system where multiple agents work together to resolve complex requests or perform interrelated tasks, often as specialized agents handling subflows within a larger workflow [00:13:17]. **Handoffs** are the process by which one agent transfers control of an active conversation to another agent, preserving the entire conversation history and context [00:13:38].
    *   **Application**: In a fully automated customer service flow, for example, different models can be used for different stages: a smaller model (GPT-4o mini) for triage, a larger model (GPT-4o) for managing the conversation, and a reasoning model (GPT-3 mini) for accuracy-sensitive tasks like checking refund eligibility [00:14:03].
    *   **Benefit**: Handoffs effectively swap out the model, prompt, and tool definitions while maintaining conversation history, providing flexibility for a wide range of scenarios [00:14:39].

4.  **Implement Guardrails in Parallel**
    *   **Definition**: Guardrails are mechanisms enforcing safety, security, and reliability within an application, preventing misuse and maintaining system integrity [00:14:55].
    *   **Principle**: Keep model instructions simple and focused on the target task to ensure maximum interoperability, accuracy, and predictable performance [00:15:12].
    *   **Implementation**: Guardrails should not be part of the main prompts but run in parallel [00:15:25]. The availability of faster and cheaper models (like GPT-4o mini) makes this more accessible [00:15:31]. High-stakes tool calls or user responses (e.g., issuing a refund, sharing personal information) can be deferred until all guardrails have returned their results [00:15:42]. For example, an input guardrail can prevent prompt injection, and output guardrails can monitor the agent's response [00:15:57].

These lessons collectively help navigate the [[challenges_in_building_ai_applications | challenges in building AI applications]] and [[challenges_in_scaling_ai_products | scaling AI products]], emphasizing practical, iterative development over premature complexity.

## Summary of Agent Building Lessons

To summarize the lessons for [[building_effective_ai_agents | building effective AI agents]] [00:16:08]:
*   Use abstractions minimally [00:16:12].
*   Start with a single agent [00:16:13].
*   Graduate to a network of agents for more intense use cases [00:16:16].
*   Keep prompts simple and focused on the "happy path" [00:16:19].
*   Utilize guardrails to handle edge cases [00:16:21].