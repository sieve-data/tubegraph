---
title: Creating custom frontends for AI agents
videoId: 7XZbI_ez8_U
---

From: [[colemedin]] <br/> 

When [[building_ai_agents | building AI agents]], particularly for sharing with others or for long-term utility, interacting solely through a terminal is not ideal [00:00:26]. The goal is to transform agents into API endpoints and integrate them with user-friendly frontends, complete with conversation and chat history [00:00:37]. This process involves [[integrating_ai_with_front_ends | integrating AI with front ends]] and [[customizing_ai_agent_interfaces | customizing AI agent interfaces]] for a better user experience.

## The AI Agent Development Roadmap

A structured approach to [[building_ai_agents | AI agent development]] typically includes the following steps:
1.  **Planning** [00:03:18]
2.  **Prototyping** (e.g., with n8n) [00:03:27]
3.  **Database Setup** (e.g., with Supabase) [00:03:34]
4.  **Agent Development** (e.g., moving from prototype to Python with Pydantic AI) [00:03:56]
5.  **Creating the Frontend** [00:04:13]

This article focuses on the fifth step: [[creating_user_interfaces_for_ai_agents | creating user interfaces for AI agents]].

## Agent Zero: A Quick Frontend Solution

Agent Zero is a tool within the Live Agent Studio platform designed to facilitate rapid [[connecting_ai_agents_to_frontend_applications | connection of AI agents to frontend applications]] [00:01:09].

### Features of Agent Zero
*   **Instant Hook-up:** Enables immediate connection of locally built and run [[understanding_ai_agents | AI agents]] to a frontend [00:01:09].
*   **Free and Local:** It is 100% free and runs entirely locally, removing the need for complex setup or third-party hosting [00:01:14, 00:02:21].
*   **Simplified Integration:** It streamlines the process of getting custom agents working in a frontend, avoiding the complications found with some other frameworks like Open Web UI [00:02:27].
*   **Conversation and Chat History:** Agent Zero provides a frontend with built-in conversation and chat history management [00:00:47, 00:29:32].

Agent Zero makes it easy to quickly turn an agent into an API endpoint and use it with a polished frontend [00:29:27].

## The Live Agent Studio: A Community Hub

The Live Agent Studio is a platform for the community to [[building_and_deploying_custom_ai_front_ends | build and deploy custom AI front ends]] and showcase open-source [[understanding_ai_agents | AI agents]] [00:00:55, 00:04:45].

### How the Studio Guides Frontend Development
*   **Best Practices:** The studio guides users in [[building_ai_agents | building AI agents]] into production-ready API endpoints with frontends, following best practices [00:01:51].
*   **API Endpoint Approach:** It emphasizes turning agents into API endpoints, which allows them to be hooked into any frontend, not just the Live Agent Studio [00:05:30].
*   **Developer Guide and Templates:** The platform provides a comprehensive developer guide and sample templates, including Python agents, to help get started [00:05:51, 00:14:42].
*   **Hosting:** Users can submit their agents to be hosted by the studio [00:05:06].

### Live Agent Studio Hackathon
The Live Agent Studio hosts a hackathon event with cash prizes [00:06:13, 00:07:01]. Participants simply need to [[building_ai_agents | build an agent]] compatible with the Live Agent Studio, which can be done using Python, n8n, Voiceflow, Flowise, or any technology that can be packaged into a Docker container as an API endpoint [00:06:37, 00:06:45].

## Building an API Endpoint for an AI Agent

To connect an AI agent to a frontend, it must first be exposed as an API endpoint.

### Setting up the Database for Conversation History
For agents that maintain context, a database is crucial for storing conversation history.
*   **Supabase:** Supabase is a recommended platform for this purpose [00:03:36].
*   **Messages Table:** A `messages` table needs to be created in Supabase to store chat histories [00:11:11]. The Live Agent Studio developer guide provides the necessary SQL for this setup [00:11:20].
*   **Real-time Communication:** For instant feedback in the frontend, real-time communication should be enabled with the `messages` table in Supabase [00:11:50].
*   **API Keys:** Project URL, public key (Anonymous key), and service role key (secret key) from Supabase are required for backend and frontend communication [00:12:28, 00:13:51].

### Building the Agent's API with Fast API
Python's Fast API is used to create the API endpoint for the agent [00:12:54, 00:17:34].
*   **Environment Variables:** Essential environment variables include `OPEN_ROUTER_API_KEY` (for large language models), `LLM_MODEL` (e.g., DeepSeek V3), `GITHUB_TOKEN`, `SUPERBASE_URL`, `SUPERBASE_SERVICE_KEY`, and an `API_BEARER_TOKEN` for authorization [00:13:14].
*   **Security:** An `HTTPBearer` security scheme is implemented to protect the API endpoint with the defined bearer token [00:17:39].
*   **CORS Policies:** Cross-Origin Resource Sharing (CORS) policies must be set up to allow the frontend (e.g., Agent Zero) to communicate with the locally hosted agent [00:17:48].
*   **Request and Response Schema:**
    *   **Input Payload:** The API endpoint expects a JSON payload with `query` (user prompt), `user_id`, `request_id` (unique identifier for the request), and `session_id` (conversation ID) [00:18:30]. The `session_id` is often used for conversation management [00:18:53].
    *   **Output:** The API only needs to return a JSON with a single boolean parameter, `success`, indicating if the call was successful [00:19:01]. The AI response is stored directly in the database, not returned in the API response [00:19:10].
*   **Conversation History Functions:**
    *   `fetch_conversation_history`: Retrieves a limited number of the latest messages (e.g., 10) from the `messages` table in Supabase, reversed for chronological order [00:19:48].
    *   `store_messages`: Stores both user messages and AI responses in the Supabase `messages` table, including message type (AI/human), content, and timestamp [00:20:26].
*   **Agent Invocation:**
    *   The API endpoint receives the user's `query` and `session_id`.
    *   It fetches the existing conversation history from the database [00:21:43].
    *   Messages are formatted into the specific structure required by the AI framework (e.g., Pydantic AI) [00:21:49]. This includes formatting human messages and AI responses (text parts) [00:22:13, 00:22:16]. (Note: This current implementation does not cover tool calls or responses in message history, but this can be expanded upon [00:22:50].)
    *   The user's latest message is stored in the database [00:22:53].
    *   [[creating_tools_and_dependencies_for_ai_agents | Dependencies for the agent]] are initialized (e.g., HTTP client for GitHub API, GitHub API token) [00:23:01].
    *   The core agent logic is invoked with the query, message history, and dependencies [00:24:00].
    *   The AI's response is stored in the database as an AI message [00:24:10].
    *   Error handling is included to store error messages in the database and indicate failure [00:24:33].

### Running the Local Endpoint
The Fast API endpoint is served locally using `uvicorn` on a specified port (e.g., 8001) [00:16:46, 00:25:35]. This local endpoint can then be connected to Agent Zero.

## Connecting to Agent Zero
After the agent's API endpoint is running locally:
1.  Access Agent Zero via the Live Agent Studio platform ([studio.automator.ai](http://studio.automator.ai)) [00:25:53].
2.  Provide the required configuration:
    *   Supabase project URL [00:26:17]
    *   Supabase Anonymous (public) key [00:26:27]
    *   Agent endpoint URL (e.g., `http://localhost:8001/api/pydantic-github-agent`) [00:26:32]
    *   Bearer token (matching the one set in the agent's environment variables) [00:26:59]
3.  Ensure the correct Supabase keys are used: public key in the frontend (Agent Zero) and service key in the backend (the agent) [00:27:36]. This ensures the frontend and backend communicate with the same `messages` table [00:27:49].

Once configured, users can interact with their locally running agent through the Agent Zero frontend, seeing requests come through in their terminal [00:28:25].

## Future Steps: Fully Custom Frontends

While Agent Zero provides a robust starting point, the next step in the series will involve [[building_and_deploying_custom_ai_front_ends | building and deploying custom AI front ends]] using the same API endpoint [00:30:02]. This will involve using tools like Bolt.DIY, a community-driven open-source AI coding assistant, to create truly custom frontends [00:30:44]. Other options like Streamlit are also available for [[creating_user_interfaces_for_ai_agents | creating user interfaces for AI agents]] [00:04:30]. This provides the flexibility for [[advanced_architecture_for_ai_agents | advanced architecture for AI agents]] and specialized interfaces.