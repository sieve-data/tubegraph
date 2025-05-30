---
title: Building fullscale AI agents
videoId: 7XZbI_ez8_U
---

From: [[colemedin]] <br/> 

This article describes the process of transforming a terminal-bound AI agent into a full-fledged API endpoint with a polished frontend, utilizing the Live Agent Studio and Agent Zero platforms <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach aims to make AI agents useful and shareable in the long run <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. This specific video is the fourth in a series on [[step_by_step_process_for_building_ai_agents | building AI agents]] <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.

## The GitHub Agent Project

The miniseries focuses on [[building_ai_agents | building a GitHub agent]] capable of consuming entire GitHub repositories for code Q&A <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.
Previously, the agent was prototyped with n8n and then converted into a polished agent using Pydantic AI <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The agent was initially limited to terminal interaction <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Need for a Frontend

Interacting with an AI agent solely through the terminal is far from ideal for sharing it with the world or making it useful long-term <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. The goal is to give the agent a "glow-up" by making it an API endpoint and hooking it into a beautiful frontend with conversation and chat history <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This transformation enables the agent to be productionized <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

## Introducing Agent Zero and Live Agent Studio

The transformation is achieved using Agent Zero, a new tool within the Live Agent Studio <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
Agent Zero allows users to [[building_ai_agents | build and run AI agents]] locally and instantly hook them into a frontend for free, without complicated setup or third-party hosting <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It is designed to be free, 100% local, and allows for local hosting of Superbase <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. Agent Zero simplifies the process compared to other frameworks like Open Web UI, which can be complicated for custom agents <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

The Live Agent Studio (studio.automator.ai) is a platform for the community to [[building_ai_agents | build and showcase open-source AI agents]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It serves as a guide for [[building_productiongrade_ai_agents | building AI agents]] into real-world applications following best practices <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Users can try agents directly on the platform and view source code on GitHub <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. The platform encourages community contributions and offers to host submitted agents <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.

### Hackathon Event

A hackathon event, celebrating the launch of Agent Zero, offers $6,000 in prize money sponsored by Voiceflow, n8n, and OpenRouter <a class="yt-timestamp" data-t="06:15:00">[06:15:00]</a>. The event runs from the 8th to the 22nd of the month, followed by a community voting period <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. To compete, participants need to [[building_ai_agents | build an agent]] compatible with the Live Agent Studio using Python, n8n, Voiceflow, Flowise, or anything that can be put into a Docker container as an API endpoint <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>.

## Roadmap for AI Agent Development

The current stage of the AI agent roadmap for this series involves creating the frontend <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
The series has followed these steps:
1.  **Planning:** Covered in the first video <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
2.  **Prototyping:** The agent was prototyped with n8n in the second video (a live stream) <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.
3.  **Database Setup:** Superbase was used for database setup <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.
4.  **Python Conversion:** The agent was moved to [[building_ai_agents_with_python | Python]] using Pydantic AI in the third video, enhancing its production readiness <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
5.  **Frontend Creation:** This step focuses on the Live Agent Studio <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. The next video will cover [[building_ai_agents | building a custom frontend]] using Bolt.DIY and mention Streamlit <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>.

## Setting up Superbase for Conversation History

Managing chat histories for the agent requires setting up a database <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>. Superbase is used for this purpose <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.
The process involves:
1.  **Creating a new project in Superbase** <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
2.  **Creating a `messages` table:** The Live Agent Studio's developer guide provides the necessary SQL to create this table <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>. This table is essential for managing chat histories <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
3.  **Enabling real-time communication:** For instant feedback in the frontend (Live Agent Studio and Agent Zero), real-time communication must be enabled for the `messages` table <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.
4.  **Disabling Row-Level Security (RLS):** RLS is disabled temporarily to allow access to the table without authentication in Agent Zero <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>.
5.  **Obtaining API credentials:** The Superbase project URL and Anonymous (public) API key are found in the project settings under the API tab <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. The service role (secret key) is also retrieved <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

## Building the API Endpoint with Python and FastAPI

To transform the GitHub agent into an API endpoint, a blank slate is used, following the Live Agent Studio developer guide <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. A sample Python agent from the developer guide serves as a template <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>. This template sets up Fast API for the endpoint, defines request/response schemas, and includes functions for fetching and storing conversation history <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>.

### Environment Variables

The following environment variables are needed:
*   `OPEN_ROUTER_API_KEY`: To access large language models <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>.
*   `LLM_MODEL`: To define the specific large language model to use (e.g., DeepSeek V3) <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>.
*   `GITHUB_TOKEN`: For the agent to interact with GitHub repositories <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.
*   `SUPERBASE_URL`: The project URL from Superbase <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.
*   `SUPERBASE_SERVICE_KEY`: The secret service key from Superbase <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
*   `API_BEARER_TOKEN`: A custom password created by the user to protect the API endpoint <a class="yt-timestamp" data-t="14:05:00">[14:05:00]</a>.

### Core API Implementation Details

*   **HTTP Server:** Uvicorn is used to serve the Fast API endpoint on a local host, typically on port 8001 <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.
*   **Package Imports:** Includes packages for Fast API, Pydantic AI message types, and other utilities <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>.
*   **Fast API Initialization:** Sets up the Fast API application and uses `HTTPBearer` for security <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.
*   **CORS Policies:** Cross-Origin Resource Sharing (CORS) policies are added to allow Agent Zero to communicate with the locally hosted agent <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.
*   **Superbase Client:** Initializes the Superbase client using the project URL and service key <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a>.
*   **Request Schema (`AgentRequest`):** Defines the expected input parameters for the agent's API endpoint: `query` (user prompt), `user_id`, `request_id` (unique identifier for a request), and `session_id` (conversation ID) <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   **Response Schema (`AgentResponse`):** The API call returns a simple JSON with a `success` parameter (true/false) <a class="yt-timestamp" data-t="19:01:00">[19:01:00]</a>. The AI's response is stored directly in the database, not returned in the API response <a class="yt-timestamp" data-t="19:10:00">[19:10:00]</a>.
*   **Bearer Token Verification:** A function `verify_bearer_token` checks if the token provided in the API call header matches the expected token from the environment variable <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>. This serves as the protection layer for the API endpoint <a class="yt-timestamp" data-t="19:39:00">[19:39:00]</a>.
*   **Fetching Conversation History:** A function fetches the last 10 messages from the Superbase `messages` table based on the `session_id` to control LLM costs <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>. Messages are retrieved and reversed to maintain chronological order <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>.
*   **Storing Messages:** A function `store_messages` saves both user messages and AI responses into the Superbase `messages` table, including message type (AI/human) and content <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.
*   **API Endpoint Definition:** The `@app.post("/api/pydantic-github-agent")` decorator defines the endpoint URL <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.
*   **Agent Logic:**
    *   Conversation history is fetched and formatted for Pydantic AI (human messages as `user_prompt`, AI responses as `text_part`) <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>.
    *   The user's message is stored in the database <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>.
    *   An HTTP client is initialized as a dependency for the agent to interact with the GitHub API <a class="yt-timestamp" data-t="23:01:00">[23:03:00]</a>.
    *   The agent is invoked with the user query, message history, and dependencies <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.
    *   The AI's response is stored in the database <a class="yt-timestamp" data-t="24:07:00">[24:07:00]</a>.
    *   If an error occurs, an error message is stored in the database, and the API returns `success: false` <a class="yt-timestamp" data-t="24:33:00">[24:33:00]</a>.

## Connecting to Agent Zero

To connect the locally running agent to Agent Zero:
1.  Run the Fast API endpoint in the terminal using `Python github_agent_endpoint.py` <a class="yt-timestamp" data-t="25:21:00">[25:21:00]</a>. This will start the agent on `localhost:8001` <a class="yt-timestamp" data-t="25:37:00">[25:37:00]</a>.
2.  Go to studio.automator.ai and log in <a class="yt-timestamp" data-t="25:53:00">[25:53:00]</a>.
3.  Navigate to Agent Zero and enter the configuration details:
    *   Superbase Project URL <a class="yt-timestamp" data-t="26:17:00">[26:17:00]</a>
    *   Superbase Anonymous (Public) Key <a class="yt-timestamp" data-t="26:25:00">[26:25:00]</a>
    *   Agent Endpoint URL (e.g., `http://localhost:8001/api/pydantic-github-agent`) <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>
    *   Bearer Token (must match the one set in the `.env` file) <a class="yt-timestamp" data-t="26:59:00">[26:59:00]</a>
4.  Ensure the Superbase project URL matches in both the agent's `.env` file and Agent Zero <a class="yt-timestamp" data-t="27:26:00">[27:26:00]</a>. The agent uses the *service key* for Superbase, while the frontend uses the *public key* <a class="yt-timestamp" data-t="27:38:00">[27:38:00]</a>.
5.  Save the settings in Agent Zero.

After configuration, users can interact with their locally running agent through the Agent Zero frontend. Requests made in Agent Zero are sent to the local agent, and responses are displayed, demonstrating conversation and chat history management <a class="yt-timestamp" data-t="28:25:00">[28:25:00]</a>.

## Next Steps

The next video in the series will focus on [[building_ai_agents | building a fully custom frontend]] using Bolt.DIY, a community-driven open-source AI coding assistant, utilizing the same API endpoint created in this video <a class="yt-timestamp" data-t="30:36:00">[30:36:00]</a>. This provides an option for those who find the Live Agent Studio a starting point and desire truly custom development <a class="yt-timestamp" data-t="30:53:00">[30:53:00]</a>.