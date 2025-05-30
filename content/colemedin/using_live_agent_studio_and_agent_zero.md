---
title: Using Live Agent Studio and Agent Zero
videoId: 7XZbI_ez8_U
---

From: [[colemedin]] <br/> 

[[live_agent_studio_platform | Live Agent Studio]] and [[live_agent_studio_platform | Agent Zero]] are tools designed to streamline the [[ai_agents_and_their_development | development and deployment of AI agents]], particularly by providing a front-end for interaction <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The goal is to transform terminal-bound AI agents into production-ready API endpoints with polished front-ends <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a> <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.

## Live Agent Studio

[[live_agent_studio_platform | Live Agent Studio]] is a platform dedicated to [[building_ai_agents_for_automator_live_agent_studio | building and showcasing open-source AI agents]] <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a> <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It serves as a guide for building AI agents for real-world applications, emphasizing best practices <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a> <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

Key aspects of [[live_agent_studio_platform | Live Agent Studio]]:
*   **Community-Driven** The platform allows users to learn how to [[building_ai_agents_for_automator_live_agent_studio | build an agent]] for the studio and submit it for hosting <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a> <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
*   **Agent Showcase** Users can access and try out various open-source agents directly from the studio, viewing their source code on GitHub for learning <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a> <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.
*   **Developer Guide** A comprehensive developer guide provides resources, samples, and templates for [[building_ai_agents_for_automator_live_agent_studio | building agents]] compatible with the studio <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a> <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   **Flexibility** While encouraging integration with the studio, the platform is designed to teach users how to build agents as API endpoints that can be hooked into *any* front-end <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a> <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
*   **Hackathon Event** The studio hosts a hackathon where participants can [[building_ai_agents_for_automator_live_agent_studio | build agents]] compatible with the platform using various technologies like Python, n8n, Voiceflow, or Flowise <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a> <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

## Agent Zero

[[live_agent_studio_platform | Agent Zero]] is a new tool within the [[live_agent_studio_platform | Live Agent Studio]] platform <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. It enables users to connect locally running AI agents to a front-end interface instantly, without complex setup or third-party hosting <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

Key features of [[live_agent_studio_platform | Agent Zero]]:
*   **Free and Local** It is 100% free and runs locally, allowing users to even host Superbase locally <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Simplified Front-End Integration** It simplifies the process of getting custom agents working in a front-end, avoiding the complexities sometimes associated with other frameworks like [[setting_up_open_web_ui_for_ai_agent_communication | Open Web UI]] <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a> <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
*   **Configuration** To use [[live_agent_studio_platform | Agent Zero]], users need to provide their Superbase project URL, Superbase public key (anonymous API key), their agent's API endpoint URL, and an optional bearer token for authorization <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a> <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>.

## Integrating AI Agents with Live Agent Studio and Agent Zero

The process of [[integrating_ai_agents_with_live_platforms | integrating an AI agent]] with [[live_agent_studio_platform | Live Agent Studio]] via [[live_agent_studio_platform | Agent Zero]] involves several steps:

1.  **Agent Development**
    *   Start by planning the agent's functionality <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>.
    *   Prototype the agent (e.g., using n8n) <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
    *   Transition the prototype to a more production-ready framework like Pydantic AI in Python <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

2.  **Database Setup (Superbase)**
    *   [[ai_agent_development_challenges | Set up a Superbase project]] to manage conversation history <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a> <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.
    *   Create a `messages` table using provided SQL <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a> <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.
    *   Enable real-time communication for the `messages` table in Superbase settings for instant front-end feedback <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.
    *   Obtain Superbase project URL, anonymous API key (public key), and service role key (secret key) <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.

3.  **API Endpoint Creation**
    *   Turn the Python agent into an API endpoint using Fast API and Uvicorn <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a> <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>.
    *   Set up environment variables for API keys (e.g., OpenRouter API key, GitHub token), Superbase credentials (URL, service key), and a custom API bearer token for endpoint protection <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a> <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.
    *   Implement Fast API endpoints that:
        *   Define request and response schemas (e.g., input parameters like `query`, `user_id`, `request_id`, `session_id` and output `success` boolean) <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a> <a class="yt-timestamp" data-t="19:01:00">[19:01:00]</a>.
        *   Verify the bearer token for authorization <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>.
        *   Fetch conversation history from Superbase based on `session_id` <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>.
        *   Format messages for the AI framework (e.g., Pydantic AI) <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>.
        *   Store user messages and AI responses in the Superbase `messages` table <a class="yt-timestamp" data-t="20:26:00">[20:26:00]</a> <a class="yt-timestamp" data-t="22:53:00">[22:53:00]</a>.
        *   Call the AI agent with the current query and message history <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.
        *   Handle errors and return a success status <a class="yt-timestamp" data-t="24:33:00">[24:33:00]</a>.
    *   Ensure CORS policies are set to allow [[live_agent_studio_platform | Agent Zero]] to communicate with the local agent <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.

4.  **Running and Connecting**
    *   Run the Python API endpoint locally (e.g., `python github_agent_endpoint.py`) <a class="yt-timestamp" data-t="25:21:00">[25:21:00]</a>. This typically hosts the agent on `localhost:8001` <a class="yt-timestamp" data-t="25:37:00">[25:37:00]</a>.
    *   Access [[live_agent_studio_platform | Agent Zero]] on studio.automator.ai and input the Superbase project URL, public key, agent endpoint URL (e.g., `http://localhost:8001/api/pydantic-github-agent`), and the bearer token <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a> <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>.
    *   Confirm that the Superbase project URL and service key in the agent's environment match the public key provided to the front-end <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>.

Once configured, users can interact with their locally running AI agent through the [[live_agent_studio_platform | Agent Zero]] front-end, complete with conversation and chat history management <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a> <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a> <a class="yt-timestamp" data-t="29:32:00">[29:32:00]</a>. This setup allows for rapid [[deploying_and_testing_ai_agents_quickly | deployment and testing]] of agents <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>.

## Next Steps

After [[deploying_an_ai_agent_using_langserve | deploying an AI agent]] with [[live_agent_studio_platform | Live Agent Studio]] and [[live_agent_studio_platform | Agent Zero]], the next step involves [[integrating_ai_agents_with_live_platforms | building a fully custom front-end]] using the same API endpoint, for instance, with `bolt.DIY`, an open-source AI coding assistant <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a> <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a> <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a> <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This provides even greater customization options beyond the [[live_agent_studio_platform | Live Agent Studio]] interface <a class="yt-timestamp" data-t="30:53:00">[30:53:00]</a>.