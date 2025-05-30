---
title: Building AI agents with Google Anthropic and OpenAI
videoId: TlbcAphLGSc
---

From: [[colemedin]] <br/> 

The internet provides abundant information on [[understanding_ai_agents | what AI agents are]] and [[building_ai_agents | how to build them effectively]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, this vast amount of information can be overwhelming <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. To distill this knowledge, three key overarching resources explain agents very clearly: an agent white paper by Google, an article on building effective agents from Anthropic, and an agent guide from OpenAI <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

These articles combined exceed 14,000 words, making them difficult to go through in a single sitting <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This summary synthesizes that information into a concise presentation, allowing for an understanding of the fundamentals for [[building AI agents | building AI agents]] in about 20 minutes <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Mastering these fundamentals can put you ahead of 99% of people, making it easier to [[building_fullscale_ai_agents | build any agent]] in the future <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## What is an AI Agent?

All three guides define an agent as a system that uses a large language model (LLM) to reason, such as GPT, Gemini, or Claude <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. As it reasons, an agent decides to take actions on our behalf, like summarizing a Slack conversation, sending an email, or writing/executing code <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. After taking actions, it observes what happened, creating a reasoning loop where the LLM decides, acts, and then figures out what occurred to potentially take more follow-up actions or continue its process <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The number of actions an agent takes is flexible; it might take zero, two, or five, leveraging its reasoning power to decide <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

Specific definitions from the guides include:
*   **Google's Agent White Paper**: An agent can be defined as an application that attempts to achieve a goal by observing the world and acting upon it <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Anthropic's Article**: An agent is a system where the LLM dynamically directs its own processes and tool usage <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **OpenAI's Agent Guide**: Agents are systems that independently accomplish tasks on your behalf <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## When to Build an AI Agent (and When Not To)

After defining agents, the guides wisely cover when to [[building_ai_agents | build an AI agent]] versus when it's over-engineering <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Many automations are better suited for a traditional workflow, potentially including an LLM, but not necessarily an agent <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. Agents are powerful due to their extra reasoning capability, but giving them significant responsibility makes systems more dangerous and unpredictable <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

Consider the distinction using a workflow visualization tool like N8N <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>:
*   **Linear Workflow**: A linear workflow, where an LLM creates posts for X, LinkedIn, and a blog sequentially, uses LLMs but isn't an agent because it doesn't make decisions <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. It's a hardwired process that will always generate all three posts <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **AI Agent**: An AI agent, such as one interacting with GitHub repositories to analyze files, can decide how many files to look at (e.g., three, zero, or ten) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This reasoning capability to interact with its environment makes it an agent <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. However, agents can be unpredictable, potentially making mistakes like skipping a desired analysis <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

You should [[building_ai_agents | build agents]] when:
*   You need complex decision-making around the tools an agent uses to interact with the environment <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   Brittle logic is present, meaning system rules involve significant gray areas where an agent's reasoning capability is needed to navigate situations <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Do not over-engineer for an agent if your automations are predictable and stable logic (like regular code or workflow automation) is sufficient <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Four Components of Any AI Agent

Any AI agent consists of four core components <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>:
1.  **Large Language Model (LLM)**: The "brain" that provides reasoning power <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
2.  **Tools**: For the agent to interact with its environment <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
3.  **Instructions**: Usually a "system prompt" to guide the agent's behavior and tone <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
4.  **Memory**: Both short-term (conversation history) and long-term (remembering goals, preferences, instructions across conversations) <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

Comparing how these components are explained in the guides:
*   **Google**: Explains these four components the best, laying them out clearly <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Anthropic**: Covers almost as well, including all components except explicitly calling out the crucial system prompt <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **OpenAI**: Lists the model, tools, and instructions, but omits memory <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

These four components are crucial, as any issue with an agent generally stems from one of them <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. It's important to consider if the problem is with the LLM's reasoning, the tools, memory implementation, or the system prompt <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Reasoning Patterns for AI Agents

Different reasoning patterns inform how [[building_ai_agents | AI agents]] operate <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>:
*   **React (Reason, Act, Observe)**: The primary and standard pattern for most agents <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This cycle involves reasoning about what to do, taking action, observing the outcome, and then reflecting to adjust strategy or take additional actions <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. The Google paper highlights React as a significant focus <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Chain of Thought**: Involves step-by-step logic, similar to instructing an LLM to think through a problem incrementally, which generally yields better results <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Tree of Thought**: The most technical pattern, where an AI agent explores many different possibilities and outcomes in parallel <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Common Patterns for Building Agents and Multi-Agent Workflows

Several common patterns are used for [[building AI agents | building agents]] and multi-agent workflows <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>:
*   **Prompt Chaining**: Multiple agents running sequentially <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Routing**: One LLM routes requests to specialized agents <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Tool Use**: Agents decide how and when to leverage specific tools <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Evaluator Loops**: An LLM produces an output, and another LLM evaluates it, allowing for self-correction loops if necessary <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This is similar to the evaluator and optimizer pattern <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **Orchestrator and Worker Flow**: A primary agent manages many other agents, splitting up tasks <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Autonomous Loops**: The most dangerous pattern, where an AI agent makes all decisions without human involvement, managing its own inputs and outputs for the entire process <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

The Anthropic article on [[building productiongrade AI agents | building effective agents]] is highly recommended for understanding these patterns, providing clear diagrams <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Single Agent vs. Multi-Agent Systems

The OpenAI guide notes that single-agent systems are generally preferred due to their simplicity <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. However, issues like "tool overload" (more than 10-15 tools for one agent) or more complex logic necessitate splitting processes into multi-agent systems <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. Multi-agent systems can involve agent handoffs, manager agents like orchestrators, or decentralized operations where many agents work in tandem to solve a problem <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

## Safety and Guardrails for AI Agents

Regardless of how powerful an LLM is, it will hallucinate <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. Preventing these hallucinations from affecting the AI system depends entirely on robust guardrails <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

Key safety measures and guardrails include:
*   **Limiting Certain Actions**: For example, ensuring an agent interacting with a database can only use read-only tools <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Human Review**: Incorporating a human in the loop to approve actions and allow feedback to direct the agent <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Filtering Certain Outputs**: Implementing mechanisms to filter undesirable or irrelevant outputs <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   **Testing in Safe Environments**: Always test agents in a safe environment before deploying to production to prevent system failures where guardrails might not help <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

The OpenAI guide specifically covers guardrails comprehensively, discussing different types on page 26 <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. This can include filtering Personally Identifiable Information (PII) or using relevance classifiers for RAG (Retrieval Augmented Generation) applications to ensure answers are relevant to the user's question <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. An example of a guardrail implementation is a "critic node" that evaluates an agent's output against expectations and retries the process if it doesn't match <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. This looping guardrail ensures reliable systems <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

## Effective AI Agent Implementation

For effective [[building AI agents | AI agent implementation]]:
*   **Start Simple**: Begin with basic automation <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.
*   **Visibility into Agent's Reasoning**: Gain insight into an agent's decisions, such as how many times it uses different tools for a given query <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   **Clear Instructions**: This applies to both the system prompt and the descriptions provided for the agent's tools, ensuring effective and timely usage <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Constant Evaluation**: Evaluating agents is paramount, often constituting 75% of the effort, compared to 25% for coding or automating <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Achieving the first 90% of performance is easy, but making an agent truly great requires continuous evaluation and tweaking of tools, fine-tuning, system prompts, and knowledge bases <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Human Oversight**: Maintain human involvement, such as human-in-the-loop mechanisms, for more crucial decisions an agent makes, as full trust may not be appropriate for many use cases <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.

## Real-World Use Cases for AI Agents

The guides highlight several practical real-world use cases for AI agents, offering quick wins for businesses and personal automations <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>:
*   **Customer Service**: Classifying and responding to queries <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
*   **General Business Operations**: Approving refunds, reviewing documents, and automatically organizing files in platforms like SharePoint, Outlook, or Gmail <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Research Tasks**: LLMs are proficient at general research tasks <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
*   **Development Tools**: AI coding assistants are powerful examples <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **General Scheduling Tasks**: Managing calendars, planning invites, sending meeting details, inbox management, and managing tasks in software like ClickUp or Asana <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

## Frameworks and Tools Mentioned

While remaining framework-agnostic, the guides mention several tools and frameworks for [[building AI agents | building AI agents]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>:
*   **Google's Agent White Paper**: Discusses prompt templates, Vertex AI (their cloud offering with powerful agent capabilities), and tools like Langchain <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   [[googles_a2a_protocol_for_ai_agents | OpenAI's Agent Guide]]: Focuses on their Agents SDK, providing numerous code examples <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
*   **Other Notable Frameworks**: Langraph, Agno, Crew AI, Small agents from Hugging Face, and [[building_ai_agents_with_pydantic_ai | Pydantic AI]] <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. Each offers distinct pros and cons <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

## Final Thought: Focus on Outcomes, Not Complexity

When [[building AI agents | building agents]] or any automations, the focus should always be on outcomes, not complexity <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>. While it's tempting to focus on complex agent architectures, intricate guardrails, and advanced system prompting, what truly matters are the results achieved from implementing the agent <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Prioritize the return on investment (ROI) in time and money when developing an agent <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.

This summary condenses Google's agent white paper, OpenAI's practical guide to agents, and Anthropic's guide to [[building effective agents | building effective agents]] <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>. For deeper dives into these topics and [[building good AI agents | building good AI agents]], consider communities like Dynamis.ai <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.