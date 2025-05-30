---
title: AI Agent Orchestration with Swarm
videoId: q7_5eCmu0MY
---

From: [[colemedin]] <br/> 

[[openai_swarm_ai_tool | Swarm]] is an open-source [[ai_agents_and_their_development | AI agent]] orchestration tool recently released by OpenAI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to write clear Python code to [[building_ai_agents | build AI agents]] and seamlessly connect them for complex tasks <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The framework is experimental and primarily educational, aiming to teach robust architecture for [[ai_agents_and_their_development | AI agent]] orchestration <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Why Swarm? The Need for Orchestration

While setting up a single [[ai_agents_and_their_development | AI agent]] with tools like LangChain or n8n is straightforward (including LLM integration, prompting, and function calling) <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, challenges arise when connecting multiple agents <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. A single [[ai_agents_and_their_development | AI agent]] can become overwhelmed if given too many functions or instructions, leading to the "needle in a haystack" problem where specific instructions or functions are missed <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

The solution to this [[ai_agent_development_challenges | AI agent development challenge]] is to have multiple [[ai_agents_and_their_development | agents]] work collaboratively, each tackling different parts of a problem or handling specific system components <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This is where [[openai_swarm_ai_tool | Swarm]] becomes valuable as both a tool to use and to learn from <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Swarm's Educational Value

[[openai_swarm_ai_tool | Swarm]] is entirely open-source, with all code available for users to fork, modify, or even run their own fine-tuned LLMs within their swarms <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It offers extensive documentation and examples <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

> [!NOTE]
> [[openai_swarm_ai_tool | Swarm]]'s primary goal is not to be a production-ready software library for enterprise-grade applications, but rather to teach concepts <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It specifically showcases handoff and routine patterns crucial for [[ai_agents_and_their_development | building robust and reliable AI agent architectures]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Studying its source code can provide significant learning <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Practical Example: Managing a SQL Database with Swarm

A compelling [[examples_of_ai_agents_and_workflows | example of AI agent workflows]] involves using a swarm of agents to manage a SQL database <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This setup allows [[ai_agents_and_their_development | AI agents]] to extract insights from data with SQL queries, create and manage tables, and clean data <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. For large SQL databases with many tables and data, different agents specializing in different areas of the database are often needed <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Architecture of a SQL Database Management Swarm

This [[examples_of_ai_agents_and_workflows | AI agent swarm]] works together to answer a wide range of user questions about data in an RSS feed database <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

The architecture consists of:
1.  **Router Agent**: An orchestrator that determines which specialized sub-agent should handle a specific user request <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
2.  **Specialized Sub-Agents**: Each agent specializes in handling different parts of the data within the RSS feed database. Examples include:
    *   **RSS Feed Agent**: Specializes in data related to RSS feeds <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
    *   **User Agent**: Specializes in user-related data <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>.
    *   **Analytics Agent**: Handles questions requiring data analytics <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.

When a user question comes in, the router agent, with its context, directs the request to the most suitable sub-agent <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. These specialized agents can have specific instructions on how to write queries and respond to the user, offering robustness and flexibility <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This entire setup can be implemented in less than 100 lines of Python code using [[openai_swarm_ai_tool | Swarm]] <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Implementation Steps

The implementation involves setting up a SQLite database with mock data for RSS feeds, sources, categories, articles, users, and user sessions <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

The key steps in Python using [[openai_swarm_ai_tool | Swarm]] include:
1.  **Database Connection**: Establishing a connection to the SQLite database <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
2.  **Load SQL Schema**: Loading the SQL script for creating tables. This schema information is provided to the [[ai_agents_and_their_development | AI agents]] so they understand the tables and their structure, enabling them to create SQL queries <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
3.  **Define Tools**: Create functions that agents can invoke. For instance, a `run_sql_select_statement` tool allows an agent to execute a SQL SELECT query against the database <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The docstring of this function informs the agent about its purpose and usage <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
4.  **Create Agent Instructions**: Functions are defined to provide instructions to each agent.
    *   The router agent is instructed to act as an orchestrator, directing requests to the appropriate SQL expert agent <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
    *   SQL expert agents are told they are SQL experts who generate SQL statements to retrieve information based on natural language requests <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. The table schemas are fed into these prompts <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.
    *   Specific instructions can be appended to customize agent behavior (e.g., making the RSS feed agent "super enthusiastic" <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>).
5.  **Instantiate Agents**: Using the `swarm.Agent` object, each agent (router, RSS feed, user, analytics) is created by providing a name and its specific instructions <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. The `run_sql_select_statement` function is given to the expert agents via the `functions` parameter, granting them access to database interaction <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
6.  **Define Transfer Functions**: Functions are set up for agents to transfer requests:
    *   From expert agents back to the router <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
    *   From the router to the different expert agents <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
    These transfer functions are added to the respective agents, completing the workflow <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.

### Demonstration

When the [[openai_swarm_ai_tool | Swarm]] agent is run, it initiates a chat in the terminal.
*   A question like "How many users do we have on the platform?" is routed to the user agent, which then executes a `SELECT COUNT(*)` query and provides the answer <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>.
*   A question such as "How many RSS feeds do we have in total?" is routed to the RSS feed agent, which not only provides the count but also responds with the enthusiastic tone specified in its instructions <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.
*   Complex analytics questions like "What are the most popular categories among users?" are routed to the analytics agent, which generates and executes more intricate queries to provide detailed insights <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.

This demonstrates how [[openai_swarm_ai_tool | Swarm]] enables setting up [[ai_agents_and_their_development | agents]] to work on different parts of a database, answering various questions, including those requiring complex queries from natural language prompts <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.

## Swarm vs. Other Frameworks

While [[openai_swarm_ai_tool | Swarm]] is considered incredible, it might offer less customization compared to frameworks like LangChain + LangGraph or tools like n8n, as it can be a bit more "black box" <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.