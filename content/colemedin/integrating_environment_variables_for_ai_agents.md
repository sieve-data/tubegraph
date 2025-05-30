---
title: Integrating environment variables for AI agents
videoId: qgH_KFSFMUE
---

From: [[colemedin]] <br/> 

Environment variables are crucial for configuring and deploying [[understanding_ai_agents | AI agents]], especially when moving them from local development to a cloud environment <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. They allow for easy management of sensitive information like API keys and dynamic configuration settings without hardcoding them into the application <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## Defining Environment Variables

A typical setup includes an example environment variable file, such as `env.example`, which provides a template for setting up necessary API keys and model definitions <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. When deploying to a cloud instance, it's recommended to create a `.env` file and set all the required variables within it <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Key Environment Variables

Several environment variables are essential for the functionality of an [[understanding_ai_agents | AI agent]] and its deployment:

*   **`llm_model`**: This variable determines which Large Language Model (LLM) the [[understanding_ai_agents | agent]] will use, such as OpenAI, Anthropic, or Groq models <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **API Keys**: Various API keys are required for the [[understanding_ai_agents | AI agent]] to interact with external services and tools (e.g., [[integrating_ai_agents_with_live_platforms | Asana]] API) <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. These are stored in the `.env` file to keep them secure <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
*   **`AGENT_ENDPOINT_URL`**: Once the [[understanding_ai_agents | AI agent]] is [[configuring_ai_agents_for_cloud_deployment | deployed to the cloud]], the front-end application (like a [[customizing_ai_agent_interfaces | Streamlit UI]]) needs to know the URL of the deployed API endpoint <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This URL, typically the IP address of the cloud droplet along with the port, is set in this environment variable in the front-end's `.env` file <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

## Configuration for Deployment

When [[configuring_ai_agents_for_cloud_deployment | deploying an AI agent]] to a cloud server like DigitalOcean, the following steps involve environment variables:

1.  **Clone the Repository**: The code for the [[understanding_ai_agents | AI agent]] and its related scripts (e.g., [[creating_a_robust_ai_agent_development_environment | LangServe]] endpoints, [[creating_a_robust_ai_agent_development_environment | LangGraph]] app) is cloned from a GitHub repository onto the cloud instance <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  **Create `.env` File**: A `.env` file is created on the cloud instance to store all necessary environment variables, including API keys and model configurations, following the structure of the `env.example` file <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
3.  **Update Front-End Configuration**: The front-end application's environment variable, `AGENT_ENDPOINT_URL`, is updated to point to the newly deployed [[understanding_ai_agents | AI agent]]'s API endpoint (the cloud instance's IP address and port 8000) <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

## Security Considerations

For basic deployments, the endpoint might initially be unencrypted HTTP, without authentication <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. However, [[creating_a_robust_ai_agent_development_environment | LangServe]] and Fast API allow for the implementation of standard API security measures like CORS policies and authentication mechanisms <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a> <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. Future tutorials might cover setting up SSL for encryption <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.