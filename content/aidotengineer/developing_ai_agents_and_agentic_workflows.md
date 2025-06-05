---
title: Developing AI agents and agentic workflows
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

The landscape of AI in enterprise is evolving, with a significant shift towards [[ai_agents_and_agentic_workflows | agentic workflows]] and the deployment of AI agents. OpenAI, as a foundational model developer, outlines its approach to bringing these advanced capabilities to production and shares key insights from its experience in the field <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## OpenAI's Operational Model <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>
OpenAI operates with two core engineering teams:
*   **Research Team:** Comprises 1,200 researchers focused on inventing and deploying foundational models <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Apply Team:** Takes these foundational models and builds them into products, such as ChatGPT and the API, making GPT models available for deployment <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

The go-to-market team then places these products into end-users' hands, assisting in automating internal operations and integrating AI into the workforce and products <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. A continuous iterative loop involves gathering feedback from the field to improve products and core models, completing a "research flywheel" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## The Enterprise AI Customer Journey <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
Enterprises typically navigate their AI journey in three phases:
1.  **Building an AI-Enabled Workforce:** Empowering employees to become AI literate and integrate AI into their daily work <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This often starts with products like ChatGPT <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Automating AI Operations:** Implementing internal use cases to build automation or co-pilot functionalities within the workforce <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. More complex or customized needs typically leverage the OpenAI API <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
3.  **Infusing AI into End Products:** Integrating AI into end-user-facing products, primarily through API use cases <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Crafting an Enterprise AI Strategy <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
A successful AI strategy within an enterprise should:
1.  **Determine Top-Down Strategic Guidance:** Identify how AI technology aligns with the broader business strategy, rather than solely focusing on an "AI strategy" <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
2.  **Identify High-Impact Use Cases:** Select one or two significant use cases that are high impact and scope them out for initial delivery <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
3.  **Build Divisional Capability:** Enable teams and infuse AI across the organization through enablement, building centers of excellence, or creating centralized technological platforms <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### The Use Case Journey <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>
A typical three-month use case journey involves:
*   **Ideation and Scoping:** Initial ideation, scoping, architecture review, and defining clear success metrics and KPIs <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Development:** The bulk of the time, involving iterative prompting strategies, RAG (Retrieval Augmented Generation), and continuous improvement <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. OpenAI teams often engage closely through workshops, office hours, and paired programming <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Testing and Evaluation:** Conducting AB testing and beta rollouts based on predefined evaluation metrics <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Production and Maintenance:** Launching the solution, performing scale optimization testing, and ongoing maintenance <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

OpenAI supports partners by providing early access to models and features, internal experts from research and product teams, and joint roadmap sessions <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

#### Case Study: Morgan Stanley's Internal Knowledge Assistant <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>
Morgan Stanley developed an internal knowledge assistant to help wealth managers quickly and accurately answer client questions using their vast corpus of research reports and live data <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. Initially, accuracy was low at 45% <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. Through collaboration with OpenAI, new methods were introduced, including:
*   Hybrid retrieval <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
*   Fine-tuning embeddings and different chunking strategies <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   Reranking and classification steps <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
*   Prompt engineering and query expansion <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>

These iterative improvements boosted accuracy from 45% to 85%, and ultimately to 98%, exceeding their 90% goal <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## [[developing_ai_agents_for_productivity | Developing AI Agents]] and [[ai_agents_and_agentic_workflows | Agentic Workflows]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
2025 is anticipated to be the year of [[ai_agents_and_agentic_workflows | agents]], where generative AI transitions from being merely an assistant to a co-worker <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. OpenAI has gathered [[best_practices_for_building_ai_agents | best practices]] and "battle scars" from building [[agentic_systems_and_workflows | agentic workflows]] in the field <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### What is an AI Agent? <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
An AI agent is defined as an AI application composed of:
*   A model with instructions (typically a prompt) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   Access to tools for information retrieval and external system interaction <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   An execution loop, where the model controls its termination <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

In each cycle, an agent receives natural language instructions, decides whether to call tools, runs them, synthesizes a response with the tool's return values, and provides an answer to the user. It can also determine when its objective is met and terminate the loop <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### [[best_practices_for_building_ai_agents | Best Practices for Building AI Agents]] <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>

#### 1. Use Abstractions Minimally: Start Simple, Optimize When Needed <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>
It's tempting to start with frameworks when [[building_effective_ai_agents | building AI agents]], as they offer quick proofs of concept <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. However, this often defers design decisions before understanding constraints, making optimization difficult <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

> [!TIP] Start with Primitives
> Build first with primitives (raw API calls) to understand how the task decomposes, where failures occur, and what needs improvement <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. Introduce abstractions only when you find yourself reinventing the wheel (e.g., embedding strategies or model graders) <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The focus should be on understanding data, failure points, and constraints, not just choosing the "right" framework <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

#### 2. Start with a Single Agent <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>
Jumping straight into multi-agent systems with dynamic coordination often introduces too many unknowns <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

> [!TIP] Incremental Complexity
> Begin with a single agent purpose-built for a specific task <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. Deploy it with a limited user set and observe its performance to identify real bottlenecks (e.g., hallucinations, latency, inaccuracy) <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. Complexity should increase only as more intense failure cases and constraints are discovered <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. The goal is to build a system that works, not necessarily a complicated one <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

#### 3. Graduate to a Network of Agents with Handoffs <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>
For more complex tasks, a network of agents allows multiple agents to collaborate on resolving complex requests or performing interrelated tasks <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. This can be viewed as specialized agents handling sub-flows within a larger [[agentic_systems_and_workflows | agentic workflow]] <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

**Handoffs:** This is the process where one agent transfers control of an active conversation to another agent, preserving the entire conversation history and context <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This allows for swapping out the model, prompt, and tool definitions, providing flexibility for a wide range of scenarios <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

> [!EXAMPLE] Customer Service Flow <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>
> A fully automated customer service flow can use a network of agents with handoffs:
> *   **Triage:** A smaller model (e.g., GPT-4o mini) performs initial triage on incoming requests <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
> *   **Conversation Management:** A more capable model (e.g., GPT-4o) manages the main conversation with the user <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.
> *   **Accuracy-Sensitive Tasks:** A different model (e.g., O3 mini reasoning model) handles tasks requiring high accuracy, such as checking refund eligibility <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

This approach ensures the right tools are brought to the right job <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

#### 4. Use Guardrails to Handle Edge Cases <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>
Guardrails are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and maintaining system integrity <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.

> [!TIP] Guardrail Implementation
> *   **Simple and Focused Prompts:** Keep the model instructions simple and focused on the target task for maximum interoperability and predictable accuracy improvements <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
> *   **Parallel Guardrails:** Guardrails should generally *not* be part of the main prompts but should instead run in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The availability of faster, cheaper models like GPT-4o mini makes this more accessible <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
> *   **Deferred High-Stakes Actions:** High-stakes tool calls or user responses (e.g., issuing refunds, sharing personal information) should be deferred until all guardrails have returned and verified safety <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

For example, input guardrails can prevent prompt injection, and output guardrails can evaluate the agent's response <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>.

## Conclusion <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>
To effectively develop and scale [[ai_agents_and_agentic_workflows | AI agents]] and [[agentic_systems_and_workflows | agentic workflows]]:
*   Use abstractions minimally <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   Start with a single agent <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.
*   Graduate to a network of agents when facing more intense challenges <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   Keep prompts simple and focused on the "happy path," using guardrails to manage edge cases <a class="yt-timestamp" data-t="00:16:19">[00:16:19]</a>.