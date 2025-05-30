---
title: Building deterministic logic and modular AI systems
videoId: iMzEzLZ9gXw
---

From: [[customaistudio]] <br/> 

Building an AI company involves navigating complex challenges, particularly in designing effective and scalable AI systems. Key lessons learned revolve around the strategic use of prompting, model selection, custom tooling, and a shift from traditional automation to an "agentic" approach that emphasizes deterministic logic and modularity <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Agentic Prompting: From Step-by-Step to Decision Frameworks

Early approaches to [[prompt_engineering_and_modularity_in_ai_systems | prompt engineering]] for AI agents often mimicked chatbot prompting, attempting to embed all possible decisions and edge cases within a single, massive prompt <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Old Approach: Over-Specification
The initial strategy involved designing prompts with:
*   Step-by-step conditional instructions (e.g., "if this happens then do that") <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   Attempts to capture all possible edge cases in a single prompt <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   Thorough explanations for every tool call, including parameters, even when the data would be automatically inserted <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

This led to:
*   Constant hallucinations <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Continuous prompt tweaking <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   Massive, overly conditional prompts (e.g., "if X, run tool A, respond with template B") <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

An example was listing every parameter for creating a calendar event directly in the prompt <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. However, it's important to note that the schema for an API call often gets appended to the prompt when an agent calls a tool anyway, so the agent already knows the parameters for that specific tool <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### New Approach: Hardcoded Logic and LLM Thinking Space
The current strategy shifts towards building AI agents with a foundation of deterministic logic, leveraging [[building_efficient_ai_agents_with_prompts | efficient prompting]] and [[data_management_and_prompt_engineering_for_ai_agents | data management]]:
*   **Hardcoding Deterministic Logic**: If a decision doesn't require the flexible reasoning of an LLM, it's handled by explicit programming (e.g., "if node," "switch," or "filter") <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The goal is to boil down the problem to identify where the LLM's flexibility is truly needed <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Structuring Input Data**: Emphasis is placed on preparing and packaging necessary context (like customer records from a CRM or order history) *before* it reaches the LLM <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Giving LLM Thinking Space**: Prompts now define overarching objectives, macro KPIs, and strict boundaries or "guardrails" <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Within these defined rules, the LLM is allowed to act as the "playmaker," making decisions and planning steps, similar to how AlphaGo uncovered new ways to win in Go <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
*   **Using Emotion in Prompts**: Adding emotional cues (e.g., "all caps," "exclamation points," "do not do this," "always remember") can heighten the LLM's attention to specific instructions, improving adherence <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

The core lesson is that over-specifying prompts often leads to underperforming results <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. Designing the "rules of the game" and letting the LLM play within those boundaries, using KPIs as a scoreboard, is more effective <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

> [!NOTE] Prompts as Hypotheses
> Unlike traditional code, prompts are hypotheses that require execution and scaling to measure performance <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. For example, a customer success bot saw a 20% improvement in output appropriateness after a framework swap from step-by-step instructions to a decision-making framework focused on avoiding refunds <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

## Causality is Slippery

Understanding *why* a prompt did or did not work is challenging with LLMs, unlike traditional code which provides clear syntax errors <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This non-deterministic nature means that changes can have unforeseen effects, and it's difficult to pinpoint the exact cause of performance shifts <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This is often a point of frustration for traditional developers <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

Roadmap for prompt optimization includes:
*   Live KPI monitoring and auto-triggering A/B prompt versions <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.
*   Developing an auto-optimization workflow for prompts, though this is challenging due to the slippery nature of causality <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>.

## Model Selection

The choice of LLM model significantly impacts whether a system is production-ready or merely a proof of concept <a class="yt-timestamp" data-t="00:22:14">[00:22:14]</a>.

### Evolution of Model Strategy
Initially, the focus was on using the "best" model available, primarily OpenAI's GPT-4, for simplicity <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. This worked for simpler automations but proved insufficient for more robust, high-stakes [[building_and_deploying_ai_agents | agentic systems]] <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. As other models like Anthropic's Claude, DeepSee, Gemini, and Grok matured, it became clear that different models excel at different tasks and require unique prompting techniques <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>.

### Model Characteristics and Use Cases
*   **Gemini**: Good for long context windows and live web search, sometimes outperforming RAG solutions for dynamic information retrieval <a class="yt-timestamp" data-t="00:24:35">[00:24:35]</a>. However, it struggles with tool calling compared to Claude <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
*   **Claude 3 Sonnet**: Preferred for high-level reasoning and used at the "planner" stage in agent architecture due to better memory and topic retention <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.
*   **GPT-4.5**: Excellent for human-sounding, conversational external communication <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **Grok**: Known for its chatbot experience and access to Twitter/X data, making it enjoyable and knowledgeable about current events <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>.

> [!TIP] Model-Prompt Combo (Goldilocks Zone)
> The same prompt can produce a 20% deviation in output quality depending on the model used <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Success lies in finding the "Goldilocks zone" – the right model-to-prompt combination <a class="yt-timestamp" data-t="00:30:25">[00:30:25]</a>. This requires standardizing prompting techniques based on both the scenario and the specific model, and continuous model testing <a class="yt-timestamp" data-t="00:31:34">[00:31:34]</a>.

Roadmap for model selection includes fine-tuning for specific scenarios (e.g., legal jargon for a law firm's legal assistant) to reduce the need for excessive guardrails and automations <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>.

## Custom Tooling

Building custom tools is preferred over off-the-shelf solutions for creating truly effective and modular AI systems <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>.

### From Tool Hopping to Custom Builds
Initially, the assumption was that existing solutions would address challenges, leading to "tool hopping" <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>. However, off-the-shelf [[nocode_ai_platforms_for_building_agents | nocode AI platforms]] and [[tools_and_resources_for_building_ai_agents | agentic AI tools]], much like traditional SaaS, rarely provide a 100% fit and often force architecture to bend to their limitations <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>.

### Advantages of Custom Tools
*   **Full Control**: Allows for solutions precisely tailored to specific needs <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>.
*   **Relevance and Effectiveness**: Creates solutions that are more relevant and effective for clients <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.
*   **Faster Iteration Cycles**: Enables quicker adjustments and improvements <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.
*   **IP Development**: Fosters the development of proprietary intellectual property <a class="yt-timestamp" data-t="00:34:47">[00:34:47]</a>.

Custom tools are being built for:
*   Data processing, labeling, and cleaning <a class="yt-timestamp" data-t="00:33:55">[00:33:55]</a>.
*   API function calling <a class="yt-timestamp" data-t="00:33:58">[00:33:58]</a>.
*   Data retrieval and prompt engineering <a class="yt-timestamp" data-t="00:34:02">[00:34:02]</a>.
*   An "agentic database" with ETL pipelines for processing and storing event data relationally, not just in vector databases (RAG) <a class="yt-timestamp" data-t="00:35:28">[00:35:28]</a>.

Roadmap includes dynamic tools for flexible, modular API calling <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>, prompt evaluation and optimization frameworks, high-volume testing infrastructure, and workflows for API research and events data processing <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>.

## The Even Playing Field: Skipping Traditional Automation

Many businesses missed the wave of traditional automation but now have an opportunity to skip directly to [[building_autonomous_ai_agents_over_18_months | Agentic AI]] <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>.

### Shift from Automation to Agentic Systems
While traditional automation (e.g., Zapier, Make) can offer productivity gains, it's considered "2015 tech" <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>. LLMs can orchestrate and even build automations themselves, making rigid "if-then" automations less relevant <a class="yt-timestamp" data-t="00:48:24">[00:48:24]</a>.

> [!IMPORTANT] Agentic AI vs. AI Automation
> [[challenges_in_developing_autonomous_ai_agents | Agentic AI]] is not merely an improvement of traditional automation; it's a paradigm shift <a class="yt-timestamp" data-t="00:52:04">[00:52:04]</a>. Instead of achieving 10-30% efficiency gains, the focus should be on a 1,000% increase and a complete change in how a business operates <a class="yt-timestamp" data-t="00:49:48">[00:49:48]</a>.

The focus should be on building "Agentic Operating Systems" (Agentic OS), which are dynamic systems that use automations as part of their toolset <a class="yt-timestamp" data-t="00:50:29">[00:50:29]</a>. These systems act as underlying operating systems for the business, judged on performance KPIs rather than just system health <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.

## Plant a Flag: Defining the Agentic Database and Business Logic

The key to successful Agentic AI is centralizing, contextualizing, and processing data to create a master contextual database <a class="yt-timestamp" data-t="00:55:53">[00:55:53]</a>. This [[data_management_and_prompt_engineering_for_ai_agents | agentic database]] becomes the single source of truth for agents, allowing for easy plug-and-play of new models, systems, and tools <a class="yt-timestamp" data-t="00:57:46">[00:57:46]</a>.

### Agentic System Architecture
A recommended architecture for agents includes:
1.  **Planner**: Ingests input data, accesses tool lists and schemas, and creates an instruction set for the executor <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>.
2.  **Executor**: Executes all API calls sequentially <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
3.  **Verifier**: Confirms that everything executed correctly <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.

This planner-executor-verifier chain is often all that's needed when prompts are abstracted into a database and pulled in dynamically, reducing the need for complex multi-chained or multi-sub-agent systems <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.

### Importance of Knowledge Base and Business Logic
A significant challenge is extracting critical business knowledge and logic, often trapped in employees' heads, and formalizing it into a database <a class="yt-timestamp" data-t="00:58:19">[00:58:19]</a>. This knowledge base, combined with clean data and effective prompts, can create a powerful AI that defines new industry standards <a class="yt-timestamp" data-t="00:50:52">[00:50:52]</a>.

> [!CAUTION] The "Easy" Fallacy
> The perception that building production-ready, high-performing, scalable AI systems is "super easy" due to simplified [[nocode_ai_platforms_for_building_agents | AI automation agency]] narratives is a fallacy <a class="yt-timestamp" data-t="01:04:16">[01:04:16]</a>. It requires significant focus, and is neither cheap nor simple <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a>.

The roadmap includes developing AI development [[blueprint_for_integrating_ai_into_business | blueprints]] for clients, focusing on implementing Agentic OS frameworks that encompass data pipelines, database schema design, and task identification for the agentic layer <a class="yt-timestamp" data-t="01:02:52">[01:02:52]</a>.

## The UI/UX Bottleneck: Collaboration, Not Just Tools

For widespread adoption of [[building_autonomous_ai_agents_over_18_months | agentic systems]], a new UI/UX approach is needed that facilitates human-agent collaboration <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>.

### Beyond Background Automation
The initial thought was that AI agents would blend seamlessly into existing tech stacks, interacting via familiar channels like Slack or email <a class="yt-timestamp" data-t="01:15:35">[01:15:35]</a>. However, because agents are judged on performance KPIs, they need their own "workspace" or destination <a class="yt-timestamp" data-t="01:16:30">[01:16:30]</a>.

### Need for a Collaborative Interface
*   **Dedicated Workspace**: A distinct UI that is seamless, easily accessible, and differentiated <a class="yt-timestamp" data-t="01:16:37">[01:16:37]</a>.
*   **Activity and Performance Tracking**: The UI should track agent activity and showcase its performance against real KPIs <a class="yt-timestamp" data-t="01:16:44">[01:16:44]</a>.
*   **Collaborative by Default**: Allows humans to monitor, stop, or adjust agent activity collaboratively, shifting responsibility from individual humans to the agentic system itself <a class="yt-timestamp" data-t="01:16:46">[01:16:46]</a>.

> [!WARNING] The Trust Factor
> Habit change is challenging; users will stop using an agent if it breaks once or provides unexpected output, even if it saves significant time <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>. Chatbot UIs like ChatGPT succeeded by making LLM interaction easy and accessible, creating a "magic" moment for extraction of value <a class="yt-timestamp" data-t="01:20:18">[01:20:18]</a>. Agentic systems need a similar "UI chip moment" to become frictionless for widespread adoption <a class="yt-timestamp" data-t="01:20:57">[01:20:57]</a>.

The core challenge is to treat agentic systems as entire entities that own processes end-to-end, rather than just tools controlled by humans <a class="yt-timestamp" data-t="01:24:43">[01:24:43]</a>.

## The Unstoppable Flywheel: Redefining Business Margins

The ROI of Agentic systems is significantly greater than initially anticipated because they redefine industry standards and margins <a class="yt-timestamp" data-t="01:37:45">[01:37:45]</a>.

### Agentic Systems Drive Exponential Growth
*   **Performance-Based**: By directly impacting KPIs, Agentic systems can significantly reduce operational costs (OPEX) and increase revenue generation <a class="yt-timestamp" data-t="01:31:09">[01:31:09]</a>.
*   **Margin Expansion**: A business is a machine where capital is input, functions are executed, and more capital is output <a class="yt-timestamp" data-t="01:30:22">[01:30:22]</a>. When the cost of executing functions decreases significantly (due to Agentic systems) and performance increases, margins expand exponentially <a class="yt-timestamp" data-t="01:30:45">[01:30:45]</a>.
*   **Example: E-commerce Customer Service**: Implementing an Agentic system for customer support can drastically reduce OPEX (e.g., from $50k to $10k/month) and decrease refund rates (e.g., from 8% to 3%) <a class="yt-timestamp" data-t="01:34:04">[01:34:04]</a>. This increases customer lifetime value (LTV), allowing higher customer acquisition costs (CAC), which in turn enables more aggressive media buying and market domination <a class="yt-timestamp" data-t="01:33:25">[01:33:25]</a>. This creates a powerful, self-feeding "flywheel effect" <a class="yt-timestamp" data-t="01:35:25">[01:35:25]</a>.

This unique period allows early implementers of Agentic OS to sprint ahead, seeing insane growth compared to competitors <a class="yt-timestamp" data-t="01:36:18">[01:36:18]</a>. The long-term impact will be a redefinition and eventual shrinkage of industry margins <a class="yt-timestamp" data-t="01:37:58">[01:37:58]</a>.

Roadmap for Agentic OS implementation focuses on a team-by-team basis (e.g., sales, customer success, ops), with the eventual goal of a universal Agentic OS that a new business can plug into for a significant head start <a class="yt-timestamp" data-t="01:38:18">[01:38:18]</a>.

## AI Consulting: Know Your Role and Stay the Course

For consultants in the AI space, it's crucial to understand your role and focus on a clear vision <a class="yt-timestamp" data-t="01:39:18">[01:39:18]</a>.

### From Open Opinion to Focused Approach
Initially, the belief was that clients wanted broad opinions and advice <a class="yt-timestamp" data-t="01:40:03">[01:40:03]</a>. However, large companies often seek validation for their existing projects or specific help with building, rather than a fundamental critique of their strategy <a class="yt-timestamp" data-t="01:42:15">[01:42:15]</a>.

### Focus on Agentic OS
The new approach is to only consult through the lens of Agentic OS <a class="yt-timestamp" data-t="01:40:03">[01:40:03]</a>. This means focusing on:
*   Centralizing data and building an underlying operating system <a class="yt-timestamp" data-t="01:40:24">[01:40:24]</a>.
*   Emphasizing a paradigm shift rather than just process automations <a class="yt-timestamp" data-t="01:40:28">[01:40:28]</a>.

> [!IMPORTANT] Strategic Focus
> Trying to do both traditional automations and Agentic systems wastes time, effort, and resources that could be spent on improving the ability to build Agentic systems <a class="yt-timestamp" data-t="01:51:21">[01:51:21]</a>. The focus must be on core products and projects.

To be an effective [[blueprint_for_integrating_ai_into_business | AI consultant]], one must first understand the client's objective and mindset, then chameleon their approach to provide targeted help <a class="yt-timestamp" data-t="01:46:20">[01:46:20]</a>.

The roadmap for AI consulting involves developing and executing a distinct discovery process for clients genuinely interested in implementing Agentic OS, focusing on holistic, deeply embedded LLM operations <a class="yt-timestamp" data-t="01:47:43">[01:47:43]</a>. This includes providing a clear [[blueprint_for_integrating_ai_into_business | blueprint]] for AI-native, AI-first transformation, rather than basic chatbot or process automation tutorials <a class="yt-timestamp" data-t="01:47:51">[01:47:51]</a>.