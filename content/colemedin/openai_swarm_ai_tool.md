---
title: OpenAI Swarm AI Tool
videoId: q7_5eCmu0MY
---

From: [[colemedin]] <br/> 

[[openais_swarm_tool | OpenAI Swarm]] is an [[ai_agent_orchestration_with_swarm | open-source AI agent orchestration tool]] recently released by OpenAI <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It enables users to write clean and simple Python code to build and seamlessly connect [[creating_tools_and_dependencies_for_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The framework is currently experimental and primarily serves an educational purpose <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>, teaching "bulletproof architecture for [[ai_agent_orchestration_with_swarm | AI agent orchestration]]" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Key Features & Benefits

*   **Open Source** <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>: The entire library is [[open_source_ai_agent_development | open source]], with all code available on GitHub <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. This allows users to fork the project, make changes, and even run their own [[local_llms_for_ai_agent_swarms | fine-tuned LLMs]] within their swarms <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   **Simple Python Code** <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>: Simplifies the process of building and connecting [[creating_tools_and_dependencies_for_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **Seamless Agent Connection** <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>: Addresses the complexity of connecting multiple agents together in specific ways <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Educational Framework** <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>: Its main purpose is to showcase handoff and routine patterns for building robust and reliable [[ai_agent_orchestration_with_swarm | AI agent architecture]] <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. Studying its source code can be highly beneficial for learning <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Extensive Documentation** <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>: The GitHub repository includes comprehensive documentation and examples <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

## Why Swarm is Needed

A single [[creating_tools_and_dependencies_for_ai_agents | AI agent]] operating alone can be limited <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. Providing too many functions or instructions can overwhelm the underlying LLM, leading to a "needle in a haystack" problem where specific instructions or function calls are missed or misused <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

The solution is to have multiple agents working together, with each tackling different parts of a problem or handling specific parts of a system <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. [[openais_swarm_tool | Swarm]] facilitates this by allowing agents to be connected in very specific ways tailored to a use case <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## Use Case Example: SQL Database Management

[[openais_swarm_tool | Swarm]] can be used to build an [[ai_agent_orchestration_with_swarm | AI agent swarm]] to manage a SQL database <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This includes:
*   Extracting insights from data using SQL queries <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
*   Creating and managing tables <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.
*   Cleaning data <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.

For large SQL databases with many tables and diverse data, multiple agents specializing in different areas of the database are often required <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>.

> [!EXAMPLE] RSS Feed Database Management
> A practical example involves managing an RSS feed database <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>. This database might contain information from various news sources, articles, user data, and user sessions <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
>
> The typical workflow for a user query is as follows:
> 1.  **Router Agent**: All user questions initially go to a "router agent" <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>. This agent has context to determine which specialized "sub-agent" is best suited to handle the specific request <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
> 2.  **Specialized Agents**: Each sub-agent specializes in handling different parts of the RSS feed database <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. Examples include:
>     *   **User Agent**: Handles user-related queries <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.
>     *   **RSS Feed Agent**: Specializes in queries about RSS feeds <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
>     *   **Analytics Agent**: Manages analytics-related questions <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.
>
> This multi-agent setup provides robustness and flexibility, allowing for different responses and query strategies based on the specialized agent <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. Such a setup can be achieved with [[openais_swarm_tool | Swarm]] in less than 100 lines of Python code <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.

## Technical Setup with Swarm

Setting up a [[ai_agent_orchestration_with_swarm | Swarm agent orchestration]] for a SQL database involves several steps:

1.  **Dependencies**: Requires `swarm` and `sqlite3` Python packages <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. An OpenAI API key is also necessary <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
2.  **Database Connection**: Establish a connection to the SQL database (e.g., SQLite) <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
3.  **Schema Provisioning**: Load SQL scripts for table creation and mock data (often generated by other LLMs like Claude <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>) to provide agents with an understanding of the database tables and their schemas <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.
4.  **Tool Creation**: Implement a tool, such as `run_sql_select_statement`, that agents can invoke to execute SQL queries against the database <a class="yt-timestamp" data-t="11:55:00">[11:55:00]</a>. The function's docstring helps the agent understand its usage <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
5.  **Agent Instruction Functions**: Create functions that return hard-coded or dynamically fetched instruction prompts for each agent <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. For example:
    *   **Router Instructions**: Inform the router agent that its job is to determine which SQL expert agent should handle a user query <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>.
    *   **SQL Expert Instructions**: Tell SQL expert agents they are SQL experts responsible for generating SQL statements to answer natural language questions, incorporating the table schemas for context <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.
6.  **Agent Instantiation**: Create `swarm.Agent` objects, providing them with a name, instructions, and available functions (tools) <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>. Instructions can be customized per agent to influence their behavior (e.g., making the RSS feed agent "super enthusiastic" <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>).
7.  **Transfer Functions**: Define functions for agents to transfer requests to other specific agents or route back to the router <a class="yt-timestamp" data-t="16:39:00">[16:39:00]</a>. These transfer functions are then added to the respective agents' list of functions <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>.
8.  **Execution**: Use `swarm.run_demo_loop()` in a `run.py` script to interact with the agent swarm in a terminal <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.

### Code Structure

```python
# Import necessary packages
import swarm
import sqlite3

# Establish database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Load SQL table schemas (for agent context)
with open('create_tables.sql', 'r') as f:
    create_tables_sql = f.read()

# Define a tool for agents to execute SQL SELECT statements
def run_sql_select_statement(sql_query: str) -> str:
    """
    Executes a SQL SELECT query on the database and returns the results formatted as a string.
    """
    try:
        cursor.execute(sql_query)
        records = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        if not records:
            return "No records found for the given query."

        # Format results nicely
        # ... (formatting logic as described in transcript) ...
        return formatted_results_string

    except sqlite3.Error as e:
        return f"Database error: {e}"

# Define functions to generate agent instructions
def get_router_instructions():
    return "You are an orchestrator of different AI agents for SQL experts..."

def get_sql_expert_instructions(table_schemas: str):
    return f"You are a SQL expert who takes in a request... Tables:\n{table_schemas}"

# Instantiate agents
router_agent = swarm.Agent(name="SQL_Router", instructions=get_router_instructions())
rss_feed_agent = swarm.Agent(
    name="RSS_Feed_Agent",
    instructions=get_sql_expert_instructions(create_tables_sql) + " Be super enthusiastic about how many great RSS feeds there are in every one of your responses.",
    functions=[run_sql_select_statement]
)
user_agent = swarm.Agent(
    name="User_Agent",
    instructions=get_sql_expert_instructions(create_tables_sql) + " Help the user with data related to user profiles.",
    functions=[run_sql_select_statement]
)
analytics_agent = swarm.Agent(
    name="Analytics_Agent",
    instructions=get_sql_expert_instructions(create_tables_sql) + " Provide insightful analytics from the data.",
    functions=[run_sql_select_statement]
)

# Define transfer functions (how agents pass control)
def transfer_to_router_agent(message: str) -> str:
    """Transfers the request back to the SQL Router agent."""
    return router_agent.run(message)

def transfer_to_rss_feed_agent(message: str) -> str:
    """Transfers the request to the RSS Feed Agent."""
    return rss_feed_agent.run(message)

# ... (other transfer functions for user_agent, analytics_agent) ...

# Add transfer functions to agents
router_agent.add_functions([
    transfer_to_rss_feed_agent,
    # ... (other transfer functions for other agents) ...
])
rss_feed_agent.add_functions([transfer_to_router_agent])
user_agent.add_functions([transfer_to_router_agent])
analytics_agent.add_functions([transfer_to_router_agent])

# Run the demo loop
swarm.run_demo_loop(router_agent)

conn.close()
```

## Comparison to Other Frameworks

While [[openais_swarm_tool | Swarm]] offers incredible capabilities for [[ai_agent_orchestration_with_swarm | AI agent orchestration]], especially in connecting multiple agents, it is noted that it might be more "black box" compared to frameworks like LangChain, LangGraph, or tools like n8n <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>. This can mean losing some customization options available in other tools <a class="yt-timestamp" data-t="20:28:00">[20:28:00]</a>.

> [!NOTE] Alternative for Database Management
> For those who prefer not to build such systems from scratch, platforms like [[open_source_ai_tools_for_database_management | Chat to DB]] provide similar functionality, allowing users to leverage [[open_source_ai_code_generators | AI]] to manage SQL databases using natural language <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. [[open_source_ai_tools_for_database_management | Chat to DB]] is open source and offers a cloud service <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. It can connect to virtually any SQL database, improve SQL queries, write SQL with natural language for insights, and manage tables <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>.