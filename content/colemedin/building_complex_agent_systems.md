---
title: Building Complex Agent Systems
videoId: AgN3RHSZGwI
---

From: [[colemedin]] <br/> 

Complex problems yield better results when tackled by a team of people with different specializations <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This principle applies equally to [[understanding_ai_agents | AI agents]], where individual expertise, when combined, creates exponentially better solutions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. [[ai_agents_and_their_development | AI agents]] perform better when their roles and goals are narrower <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. A common issue when [[building_ai_agents | building AI agents]] is that adding more instructions and tools can lead to hallucinations, even in tasks they previously handled well, because large language models (LLMs) can become overwhelmed quickly <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

Fragmenting an [[understanding_ai_agents | AI agent]] into different sub-agents to handle distinct components is an effective way to overcome this challenge and elevate [[building_ai_agents | AI agents]] to the next level <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This approach involves creating an "army of specialized agents," which requires careful consideration of how to split the problem, what tools each agent needs, and how to combine their work efficiently <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Parallel Agent Architecture

The parallel agent architecture is a crucial [[advanced_architecture_for_ai_agents | AI agent architecture]] <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>. At its core, this architecture involves user input being fed into multiple specialized [[understanding_ai_agents | AI agents]], each with its own instructions and tools to tackle a specific part of a problem <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. An aggregator or synthesizer then combines the outputs from these parallel agents to produce a nicely formatted final output for the user <a class="yt-timestamp" data-t="02:49:15">[02:49:15]</a>. This differs from a simple non-LLM aggregator by using another [[understanding_ai_agents | AI agent]] as a synthesizer <a class="yt-timestamp" data-t="03:09:16">[03:09:16]</a>. This architecture ensures true simultaneous execution, preventing workflows from taking excessive time <a class="yt-timestamp" data-t="02:59:17">[02:59:17]</a>.

### Key Benefits
*   **Better Solutions:** Individual expertise combined creates exponentially better solutions <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   **Reduced Hallucinations:** Specialized agents with narrow roles are less prone to hallucination <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   **Efficiency:** Running specialized agents simultaneously significantly reduces execution time compared to sequential processing <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>.

## Frameworks for Building Complex Agent Systems

Two preferred frameworks for [[building_fullscale_ai_agents | building fullscale AI agents]] with parallel agent architecture are Pydantic AI and LangGraph <a class="yt-timestamp" data-t="01:29:43">[01:29:43]</a>.

### Building Pydantic AI Agents

[[building_ai_agents | Building Pydantic AI agents]] can be thought of as creating three distinct parts <a class="yt-timestamp" data-t="08:35:01">[08:35:01]</a>:

1.  **Dependencies:** These include API keys, database connections, or other information needed by the agent's tools <a class="yt-timestamp" data-t="08:53:18">[08:53:18]</a>. For example, a flight agent's dependencies might include preferred airlines <a class="yt-timestamp" data-t="10:23:08">[10:23:08]</a>.
2.  **Agent Definition:** This defines the agent itself, specifying the LLM to use, the system prompt, exact dependencies, and parameters like automatic retries <a class="yt-timestamp" data-t="09:05:07">[09:05:07]</a>.
3.  **Tools:** This section defines the functionality the agent can call upon, wrapped in functions <a class="yt-timestamp" data-t="09:23:44">[09:23:44]</a>. A doc string at the top of each tool function specifies when and how the agent should use it, including its purpose and arguments <a class="yt-timestamp" data-t="09:38:09">[09:38:09]</a>. Tools are essentially functions that are wrapped up and sent as part of the prompt to the LLM <a class="yt-timestamp" data-t="11:59:05">[11:59:05]</a>.

Pydantic AI allows for structured outputs, guaranteeing that every response from an agent has specific key pieces of information <a class="yt-timestamp" data-t="18:50:52">[18:50:52]</a>. This is useful for ensuring necessary information is available for sub-agents to invoke their tools <a class="yt-timestamp" data-t="19:10:04">[19:10:04]</a>.

### Building LangGraph Graphs

LangGraph implementations also consist of three distinct parts <a class="yt-timestamp" data-t="20:59:59">[20:59:59]</a>:

1.  **State for the Graph:** These are the key pieces of information to track throughout the workflow execution, such as conversation history and results from different agent executions <a class="yt-timestamp" data-t="21:16:11">[21:16:11]</a>.
2.  **Defining Nodes:** Each node encapsulates the logic for a specific action, such as invoking an [[understanding_ai_agents | AI agent]] or executing deterministic code <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>. LangGraph nodes do not necessarily have to call an LLM; deterministic code can sometimes be more effective <a class="yt-timestamp" data-t="21:40:48">[21:40:48]</a>.
3.  **Setting up the Graph:** This involves creating a graph instance, adding all defined nodes, and connecting them with edges <a class="yt-timestamp" data-t="21:52:09">[21:52:09]</a>. Conditional edges allow for decision-making within the workflow, routing execution based on specific criteria <a class="yt-timestamp" data-t="24:04:19">[24:04:19]</a>.

LangGraph enables simultaneous execution of nodes by returning a list of desired nodes in a router function <a class="yt-timestamp" data-t="34:07:37">[34:07:37]</a>. It also supports "human in the loop" functionality through "interrupts," allowing the workflow to pause and wait for user input <a class="yt-timestamp" data-t="34:40:53">[34:40:53]</a>. Memory savers can be used to persist the graph's state during these interruptions, whether in RAM, SQLite, or PostgreSQL for production-ready solutions <a class="yt-timestamp" data-t="35:31:07">[35:31:07]</a>.

## Example: Travel Planner Assistant

A travel planner assistant agent serves as an excellent example of [[building_productiongrade_ai_agents | building production-grade AI agents]] with a parallel agent architecture <a class="yt-timestamp" data-t="03:47:33">[03:47:33]</a>. While it could operate as a single agent, planning a trip involves many components, making it ideal for specialized sub-agents <a class="yt-timestamp" data-t="03:54:02">[03:54:02]</a>.

### Workflow
1.  **Information Gathering:** An initial loop gathers essential details from the user, such as origin, destination, and trip duration <a class="yt-timestamp" data-t="04:05:43">[04:05:43]</a>. An Info Gathering agent uses structured outputs to guarantee that all necessary information is collected before proceeding <a class="yt-timestamp" data-t="18:47:49">[18:47:49]</a>. This agent acts as a "gatekeeper" to prevent sub-agents from hallucinating due to insufficient data <a class="yt-timestamp" data-t="20:19:07">[20:19:07]</a>.
2.  **Parallel Planning:** Once all information is collected, specialized sub-agents operate in parallel to plan different aspects of the trip <a class="yt-timestamp" data-t="04:17:34">[04:17:34]</a>:
    *   **Flight Agent:** Handles flight recommendations <a class="yt-timestamp" data-t="04:00:54">[04:00:54]</a>.
    *   **Hotel Agent:** Manages hotel recommendations <a class="yt-timestamp" data-t="04:00:54">[04:00:54]</a>.
    *   **Activity Agent:** Recommends activities, potentially considering weather data <a class="yt-timestamp" data-t="04:02:18">[04:02:18]</a>.
3.  **Synthesis:** The recommendations from all specialized agents are fed into a final synthesizer agent, which summarizes and formats the comprehensive travel plan for the user <a class="yt-timestamp" data-t="04:26:30">[04:26:30]</a>. This synthesizer agent's primary job is to combine the outputs, though it could also be extended to validate outputs from other agents <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.

This parallel execution allows flight, hotel, and activity recommendations to be obtained simultaneously, with the final results streamed out quickly <a class="yt-timestamp" data-t="05:04:47">[05:04:47]</a>.

### Real-world Application
For a more advanced and full-fledged use case of parallel agent architecture, one can explore [[archons_ai_agent_building_process | Archon]], an [[archon_ai_agent_builder | AI agent builder]] that constructs other [[understanding_ai_agents | AI agents]] <a class="yt-timestamp" data-t="06:02:16">[06:02:16]</a>. [[archon_ai_agent_builder | Archon]] recently implemented the parallel agent architecture to autonomously refine [[building_ai_agents | AI agents]] by kicking off a parallel workflow to refine prompts, tools, and the agent itself <a class="yt-timestamp" data-t="06:11:37">[06:11:37]</a>. This demonstrates the power of parallel processing in [[building_ai_agents_for_crm_platforms | building AI agents for CRM platforms]] or other complex systems <a class="yt-timestamp" data-t="06:24:26">[06:24:26]</a>.

Building specialized [[understanding_ai_agents | AI agents]] that run in parallel unlocks a new level of [[building_fullscale_ai_agents | building fullscale AI agents]] and agentic systems, offering transformative solutions for complex problems across various use cases <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.