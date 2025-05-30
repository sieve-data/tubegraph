---
title: Building AI prototypes with n8n and Gemini 20 Flash
videoId: 56D91EcaUnM
---

From: [[colemedin]] <br/> 

This article details the process of [[prototyping_ai_agents_using_n8n | building AI agents]] using [[n8n_in_creating_ai_agents | n8n]] and the Gemini 2.0 Flash model. It serves as a continuation of a miniseries demonstrating a complete process for [[building_ai_agents_with_nocode_tools | building AI agents]] from concept to deployment <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Why Prototype with n8n?

Prototyping an AI agent using a no-code or low-code tool like [[n8n_in_creating_ai_agents | n8n]] allows for very rapid initial development <a class="yt-timestamp" data-t="00:01:56">[01:01:56]</a> <a class="yt-timestamp" data-t="00:04:42">[04:42]</a>. Even with AI IDEs available, tools like [[n8n_in_creating_ai_agents | n8n]] can significantly accelerate the initial prototype build <a class="yt-timestamp" data-t="00:05:02">[05:02]</a>. For a prototype, the focus is on core functionality without immediately worrying about a front-end interface or a persistent database <a class="yt-timestamp" data-t="00:05:12">[05:12]</a> <a class="yt-timestamp" data-t="00:05:20">[05:20]</a>.

[[n8n_in_creating_ai_agents | n8n]] is an open-source platform, meaning it can be self-hosted for free, with costs only associated with the machine hosting it (e.g., DigitalOcean or AWS) <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## The GitHub Assistant Prototype

The live stream demonstrates [[prototyping_ai_agents_using_n8n | building]] a GitHub Assistant, an agent capable of consuming and analyzing GitHub repositories <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

This prototype allows users to provide a GitHub repository link and ask questions about the project, specific files, or the overall structure <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a> <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. The agent can read file structures and look into specific files to answer queries <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a> <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

The prototype uses Gemini 2.0 Flash as its underlying large language model (LLM) <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This model is chosen for its speed in processing prompts, which is crucial when dealing with potentially large file structures from repositories <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. Gemini 2.0 Flash offers up to 1,500 free requests per day, making it an excellent choice for prototyping <a class="yt-timestamp" data-t="00:20:27">[00:20:27]</a>.

The GitHub Assistant prototype is available to try on the Live Agent Studio at studio.automator.ai <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Core Components of the n8n Agent Workflow

The agent workflow in [[n8n_in_creating_ai_agents | n8n]] is built using several key nodes:

#### 1. Trigger Node: On Chat Message

For prototyping, the "On Chat Message" trigger is used, which enables direct interaction with the agent within the [[n8n_in_creating_ai_agents | n8n]] workflow builder's chat window <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a> <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

#### 2. AI Agent Node

This central node encapsulates the chat model, memory, and tools for the AI agent <a class="yt-timestamp" data-t="00:18:23">[00:18:23]</a> <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

*   **Chat Model:** The Google Gemini Chat Model is selected, specifically Gemini 2.0 Flash (experimental) <a class="yt-timestamp" data-t="00:18:49">[00:18:49]</a> <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
    *   **Credentials:** An API key is obtained from the Google AI Studio by navigating to `aistudio.google.com/plan-information` and then to the Google Cloud console to create a new API key <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a> <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Memory:** For prototyping, a "Window Buffer Memory" is used. This stores conversation history locally on the machine hosting [[n8n_in_creating_ai_agents | n8n]], avoiding the need for a separate database initially <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>. For production, PostgreSQL or Redis are recommended <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>.
*   **System Prompt:** A system message is added to define the agent's role (e.g., "coding expert with access to GitHub") and expected behavior <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a> <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. This includes instructions like ensuring the repository link is present before attempting actions and starting answers with the repo link to maintain context <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a> <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>.

#### 3. Agent Tools

Since [[n8n_in_creating_ai_agents | n8n]] does not have direct GitHub tools, custom "Call [[n8n_in_creating_ai_agents | n8n]] Workflow" nodes are used to create sub-workflows acting as tools <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a> <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. These tools essentially call back to the main workflow's ID, triggering a specific path defined by an "Execute Workflow" trigger <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a> <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

*   **`Get Repo Structure` Tool:**
    *   **Description:** Tells the LLM to call this tool to "get the entire structure of a GitHub repo given the URL of the repo" <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.
    *   **Parameters:** Requires `repositoryUrl` as an input parameter for the tool function <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>.
    *   **JavaScript Code Node:** Extracts the organization and repository name from the GitHub URL using a regular expression <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. This code snippet can be generated by other LLMs like Claude <a class="yt-timestamp" data-t="00:58:25">[00:58:25]</a>.
    *   **HTTP Request Node:** Uses the extracted organization and repo name to call the GitHub API (e.g., `api.github.com/repos/{org}/{repo}/git/trees/main`) to retrieve the file structure <a class="yt-timestamp" data-t="00:58:53">[00:58:53]</a> <a class="yt-timestamp" data-t="00:59:14">[00:59:14]</a>. GitHub personal access tokens are used for authentication, which can be generated in GitHub's developer settings <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a> <a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a>.
    *   **Code Node for Formatting:** Formats the raw JSON response from the GitHub API into a more natural language structure for the LLM to understand <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a> <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. The output is set to a field named `structure` <a class="yt-timestamp" data-t="01:02:46">[01:02:46]</a>.

*   **`Get File Content` Tool:**
    *   **Description:** "Use this tool to get the contents of a specific file in the GitHub repository" <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>.
    *   **Parameters:** Requires `repositoryUrl` and `filePath` (relative path) as inputs <a class="yt-timestamp" data-t="01:08:44">[01:08:44]</a>.
    *   **Workflow Logic:** A "Switch" node is introduced after the initial JavaScript node (which extracts org/repo) to branch the workflow based on an "action" parameter (e.g., `getRepoStructure` vs. `getFileContent`) <a class="yt-timestamp" data-t="01:06:28">[01:06:28]</a> <a class="yt-timestamp" data-t="01:10:45">[01:10:45]</a>. This allows multiple tools to share a single "Execute Workflow" trigger <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a>.
    *   **HTTP Request Node:** Constructs a URL to the raw file content (e.g., `raw.githubusercontent.com/{org}/{repo}/main/{filePath}`) <a class="yt-timestamp" data-t="01:12:19">[01:12:19]</a>. GitHub authentication is also applied here <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>. The output is returned in a field named `data` <a class="yt-timestamp" data-t="01:13:46">[01:13:46]</a>.

The completed prototype can analyze file structures and fetch specific file contents, allowing it to answer various questions about a repository <a class="yt-timestamp" data-t="01:16:57">[01:16:57]</a>.

## Live Agent Studio Compatibility

To transition an [[n8n_in_creating_ai_agents | n8n]] agent for the Live Agent Studio, it must be compatible with the platform's API and data handling standards <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>.

1.  **Webhook Trigger:** The `On Chat Message` trigger is replaced with a `Webhook` trigger, turning the [[n8n_in_creating_ai_agents | n8n]] workflow into an API endpoint <a class="yt-timestamp" data-t="01:49:41">[01:49:41]</a>. This allows external platforms (like Live Agent Studio) to call the agent <a class="yt-timestamp" data-t="01:45:17">[01:45:17]</a>.
2.  **Standardized Inputs/Outputs:** The Live Agent Studio requires specific input parameters (e.g., `query`, `userID`, `requestID`, `sessionID`) and expects a standardized output indicating success or failure <a class="yt-timestamp" data-t="01:49:49">[01:49:49]</a> <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>.
3.  **PostgreSQL Memory (Superbase):** For production-ready agents, the memory is transitioned from "Window Buffer Memory" to PostgreSQL, often hosted via Superbase <a class="yt-timestamp" data-t="01:39:42">[01:39:42]</a>.
    *   [[n8n_in_creating_ai_agents | n8n]]'s AI Agent node automatically creates the necessary "messages" table in PostgreSQL when connected with Superbase credentials <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a> <a class="yt-timestamp" data-t="01:54:06">[01:54:06]</a>.
    *   Superbase credentials (host, port, database, user) are found in the "Project settings" > "Database" > "Connect" section of the Superbase dashboard <a class="yt-timestamp" data-t="01:53:10">[01:53:10]</a> <a class="yt-timestamp" data-t="01:53:34">[01:53:34]</a>.
4.  **Real-time Updates:** Additional "AI Message" nodes are inserted into the workflow (using the PostgreSQL node) to send real-time status updates to the Live Agent Studio UI as the agent processes information <a class="yt-timestamp" data-t="01:54:41">[01:54:41]</a> <a class="yt-timestamp" data-t="01:55:18">[01:55:18]</a>. Since messages are stored directly in the database, the API response itself remains very basic <a class="yt-timestamp" data-t="01:57:36">[01:57:36]</a>.

## Future Enhancements and Miniseries Roadmap

The current prototype is a starting point. Future videos in the miniseries will delve into:

*   **RAG (Retrieval Augmented Generation):** Implementing a RAG pipeline using a vector database (like PG Vector in Superbase) to enable the agent to perform vector searches and retrieve more nuanced answers <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a> <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>.
*   **Custom Coding:** Transitioning from [[n8n_in_creating_ai_agents | n8n]] to custom code using frameworks like Pydantic AI for more complex, production-ready agents <a class="yt-timestamp" data-t="01:17:57">[01:17:57]</a> <a class="yt-timestamp" data-t="01:18:35">[01:18:35]</a>.
*   **Production Readiness:** Adding more robust logic, such as checking for different Git branches (e.g., `main` then `master`) <a class="yt-timestamp" data-t="01:18:24">[01:18:24]</a>.

## AI Agent Hackathon

The Live Agent Studio is hosting a hackathon with a $5,000 prize pool, requiring participants to [[building_ai_agents_with_nocode_tools | build an AI agent]] compatible with the platform <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a> <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>. The competition is sponsored by [[n8n_in_creating_ai_agents | n8n]] and Voiceflow <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>.

Registration is open until January 8th, and submissions are accepted from January 8th to 22nd. Community voting will help choose the winners, which will be announced in a live stream on February 1st <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a> <a class="yt-timestamp" data-t="01:12:09">[01:12:09]</a> <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>. All existing agents on the Live Agent Studio, including the GitHub Assistant, are open source and can serve as examples for competition participants <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a> <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a> <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.

Supported platforms for [[creating_powerful_ai_workflows_with_n8n | building agents]] for the Live Agent Studio include [[n8n_in_creating_ai_agents | n8n]], Python frameworks (e.g., Pydantic AI), Voiceflow, and any technology that can be containerized with Docker <a class="yt-timestamp" data-t="02:01:12">[02:01:12]</a> <a class="yt-timestamp" data-t="02:01:17">[02:01:17]</a> <a class="yt-timestamp" data-t="02:01:20">[02:01:20]</a>.