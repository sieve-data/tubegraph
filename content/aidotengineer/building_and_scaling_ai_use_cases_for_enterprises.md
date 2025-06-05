---
title: Building and scaling AI use cases for enterprises
videoId: joHR2pmxDQE
---

From: [[aidotengineer]] <br/> 

This article discusses the journey of [[implementing_ai_in_enterprises | implementing AI in enterprises]], focusing on how to build and [[scaling_ai_solutions_in_production | scale use cases]] with OpenAI's technologies and insights into agentic workflows <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## OpenAI's Operating Model <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

OpenAI operates with two core engineering teams:
*   **Research Team:** Comprising 1,200 researchers, this team is responsible for inventing and deploying foundational AI models <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **Apply Team:** This team takes the foundational models and builds them into products like ChatGPT and the API, making GPT models available for deployment <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

Beyond engineering, a "go-to-market" team helps deliver these products to end-users, automating internal operations and integrating AI into the workforce <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This process includes an iterative loop where feedback from the field directly improves products and core models through a "research flywheel" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This represents [[openais_approach_to_ai_deployment_and_enterprise_integration | OpenAI's approach to AI deployment and enterprise integration]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## The AI Customer Journey in Enterprise <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>

The [[ai_in_enterprise_applications | AI customer journey]] for enterprises typically unfolds in three phases:

1.  **Building an AI-Enabled Workforce:** This initial step involves getting AI tools into the hands of employees to foster AI literacy and encourage daily use in their work <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. OpenAI's ChatGPT is a primary product for this phase <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
2.  **Automating AI Operations:** Enterprises then graduate to [[integrating_ai_into_business_operations | automating internal AI operations]], such as building automation or co-pilot type use cases <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. While ChatGPT can partially assist, the OpenAI API is typically used for more complex or customized needs <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
3.  **Infusing AI into End Products:** The final phase involves [[integrating_ai_into_business_operations | infusing AI]] into end-user facing products, primarily through API use cases <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Crafting an Enterprise AI Strategy <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>

When enterprises craft their AI strategy, the process often includes:

*   **Top-Down Strategic Guidance:** It's crucial to first define the broader business strategy and then determine where AI technology aligns with that strategy <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Identifying High-Impact Use Cases:** After setting the strategy, identify one or two high-impact use cases to scope out and deliver upon <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Building Divisional Capability:** This involves [[building_ai_teams | enabling teams]] and infusing AI throughout the organization through enablement programs, establishing centers of excellence, or building a centralized technological platform for others to build upon <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## The Use Case Journey <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>

A typical use case journey, illustrated as a three-month example, involves several key phases:

1.  **Ideation & Scoping:** This includes initial ideation, detailed scoping, architectural review to understand how AI fits into the existing stack, and clearly defining success metrics and KPIs <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
2.  **Development:** This is the bulk of the time, involving iterative development, refining prompting strategies, and implementing techniques like Retrieval Augmented Generation (RAG) to continuously improve the use case <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. OpenAI's team engages closely during this phase through workshops, office hours, paired programming, and webinars to accelerate progress <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
3.  **Testing & Evaluation:** After development, the focus shifts to testing and evaluation, including A/B testing and beta rollouts, against the predefined evaluation metrics <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
4.  **Production:** This phase includes the launch rollout and [[scaling_ai_solutions_in_production | scale optimization testing]] to ensure the solution performs effectively for many end-users <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
5.  **Maintenance:** Ongoing maintenance ensures continued performance and improvement <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

### OpenAI's Partnership Approach <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>

OpenAI partners with enterprises by providing:
*   A dedicated team, expecting a dedicated team from the enterprise as well <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   Early access to new models and features, offering a glimpse into upcoming developments <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   Access to internal experts from research, engineering, and product teams to accelerate development <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   Joint roadmap sessions to align on future plans <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Case Study: Morgan Stanley <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>

Morgan Stanley partnered with OpenAI to build an internal knowledge assistant for its wealth managers <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. The goal was to provide highly accurate information from their vast knowledge corpus (research reports, live stock data) to respond to clients <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Initial accuracy was around 45% <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

Through collaboration, OpenAI introduced new methods during development, such as:
*   **Hybrid Retrieval:** <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
*   **Fine-tuned Embeddings:** <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>
*   **Different Chunking Strategies:** <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>
*   **Reranking and Classification Steps:** <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>
*   **Prompt Engineering and Query Expansion:** <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>

These interventions significantly improved accuracy, reaching 85% and ultimately 98%—surpassing their 90% goal <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Building Agents and Agentic Workflows <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>

The year 2025 is anticipated to be the "year of Agents," where GenAI truly graduates from an assistant to a co-worker <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

An **agent** is defined as an AI application consisting of:
*   A **model** with instructions, typically in the form of a prompt <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Access to tools** for retrieving information and interacting with external systems <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   An **execution loop** whose termination is controlled by the model itself <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

In each cycle, an agent receives natural language instructions, decides whether to issue tool calls, runs those tools, synthesizes a response with the tool return values, and provides an answer to the user <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. The agent can also determine if its objective has been met and terminate the loop <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Lessons Learned in [[best_practices_for_building_ai_systems | Building AI Systems]] (Agents) <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>

OpenAI has identified four key lessons or [[best_practices_for_building_ai_systems | best practices]] for [[building_scalable_ai_systems | building scalable AI systems]], specifically agents:

1.  **Use Abstractions Minimally: Start Simple, Optimize When Needed** <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
    *   Starting with frameworks can be enticing but often obscures how the system behaves and what primitives it uses, deferring design decisions before constraints are understood <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   A better approach is to first build with primitives to understand task decomposition, failure points, and necessary improvements <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Abstraction should only be introduced when reinventing the wheel (e.g., re-implementing embedding strategies or model graders) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The focus should be on understanding data, failure points, and constraints, not just choosing a framework <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

2.  **Start with a Single Agent** <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>
    *   Teams often jump into designing complex multi-agent systems too soon, creating unknowns and yielding little insight <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
    *   It's recommended to start with a single agent purpose-built for a single task, deploy it to production with limited users, and observe its performance <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This approach helps identify real bottlenecks like hallucinations, low adoption due to latency, or inaccuracy from poor retrieval <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. Complexity should only increase as more intense failure cases and constraints are discovered <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

3.  **Graduate to a Network of Agents with Handoffs for Complexity** <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>
    *   For more complex tasks, a **network of agents** is a collaborative system where multiple agents work in concert to resolve complex requests or perform interrelated tasks <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. These are specialized agents handling subflows within a larger agentic workflow <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   **Handoffs** are the process by which one agent transfers control of an active conversation to another agent, preserving the entire conversation history for the new agent <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   **Example:** A fully automated customer service flow can use a network of agents and handoffs. A GPT-4o mini model can perform initial triage, then a GPT-4o dispute agent can manage the conversation, and finally, an O3 mini reasoning model can handle accuracy-sensitive tasks like checking refund eligibility <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. Handoffs allow swapping out the model, prompt, and tool definitions while maintaining context, offering flexibility for a wide range of scenarios <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

4.  **Keep Prompts Simple and Focused, Use Guardrails for Edge Cases** <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>
    *   **Guardrails** are mechanisms that enforce safety, security, and reliability within an application, preventing misuse and ensuring system integrity <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
    *   Model instructions should be kept simple and focused on the target task to ensure maximum interoperability and predictable accuracy <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
    *   Guardrails should **not** necessarily be part of the main prompts but should be run in parallel <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. The availability of faster and cheaper models like GPT-4o mini makes this more accessible <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.
    *   High-stakes tool calls or user responses (e.g., issuing refunds, showing personal account information) can be deferred until all guardrails have returned a safe result <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. An example includes running an input guardrail to prevent prompt injection and output guardrails on the agent's response <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

In summary, for [[building_scalable_ai_systems | building and scaling AI systems]], particularly agents, the key lessons are to use abstractions minimally, start with a single agent, graduate to a network of agents when necessary, and keep prompts simple while using guardrails for edge cases <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.