---
title: AI agents for processing GitHub repositories
videoId: 56D91EcaUnM
---

From: [[colemedin]] <br/> 

AI agents can be developed to interact with GitHub repositories, allowing users to query project details and file contents conversationally <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This capability is useful for both technical and non-technical users, helping them understand open-source projects or quickly explore codebases <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

## Prototyping with n8n and Gemini 2.0 Flash

[[Building AI Agents | Prototyping an AI agent]] involves creating a quick proof of concept, often using no/low-code tools to iterate rapidly <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This approach allows developers to focus on core functionality without immediately worrying about front-end interfaces or databases <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.

The prototype discussed uses:
*   **n8n**: A no/low-code workflow automation tool chosen for its ease of use and open-source nature <a class="yt-timestamp" data-t="04:59:00">[04:59:00]</a>. Self-hosting n8n can make it free, with costs only related to the hosting machine <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   **Gemini 2.0 Flash**: A large language model (LLM) selected for its speed in processing prompts and its generous free tier (1,500 requests per day) <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **`On Chat Message` Trigger**: Initiates the workflow when a message is received <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
*   **`AI Agent` Node**: A central component in n8n that integrates the chat model, memory, and tools <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.
*   **`Window Buffer Memory`**: Used for conversational history in the prototype, storing data locally on the machine hosting n8n <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. This is suitable for prototyping but not for production environments requiring persistent storage <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## Key Components of the GitHub Agent

### System Prompt
The system prompt is crucial for defining the agent's persona and expected behavior <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. For the GitHub agent, it establishes the agent as a "coding expert with access to GitHub" and provides instructions, such as ensuring a repository link is present before attempting any actions <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. To maintain context, the agent is instructed to start its answers with the repository link <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

### Tools Integration
Since n8n lacks direct GitHub integration nodes, custom tools are implemented as sub-workflows within n8n that the agent can call <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. The `Call n8n Workflow` node is used to invoke these tools, referencing the workflow's own ID <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. The `Execute Workflow` trigger node receives these calls <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

Each tool has a name and a description that the large language model uses to understand when and how to call it, along with a defined input schema for parameters <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>.

#### Get Repo Structure Tool
This tool retrieves the entire file structure of a given GitHub repository <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   **Parameters**: Requires the GitHub repository URL <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   **Process**:
    1.  A JavaScript code node uses regular expressions to extract the organization and repository name from the URL <a class="yt-timestamp" data-t="05:28:00">[05:28:00]</a>.
    2.  An `HTTP Request` node calls the GitHub API (`/repos/{org}/{repo}/git/trees/main`) to get the file tree of the main branch <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. GitHub API authentication is managed using a personal access token <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.
    3.  Another JavaScript code node formats the raw JSON response into a more readable, natural language structure for the LLM <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.

#### Get File Content Tool
This tool reads the content of a specific file within a GitHub repository <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.
*   **Parameters**: Requires the repository URL and the relative path to the file <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Process**: An `HTTP Request` node constructs a direct URL to the raw file content (`raw.githubusercontent.com/{org}/{repo}/main/{filepath}`) and retrieves it <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

**Branching Logic**: A `Switch` node is used in the sub-workflow to direct the execution flow based on which tool (action) was called, allowing multiple tools to be handled by a single `Execute Workflow` trigger <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

## Live Agent Studio Compatibility

The Live Agent Studio is a community-driven platform featuring open-source AI agents <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. To ensure compatibility and enable hosting, agents must adhere to a standardized input/output and conversation history management protocol <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.

Key aspects of compatibility:
*   **API Endpoint**: Agents are exposed as API endpoints using n8n's `Web Hook` trigger <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.
*   **Persistent Memory**: For production, `PostgreSQL` (e.g., with Superbase) is recommended for chat memory instead of local buffer memory <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>. The `AI Agent` node in n8n can automatically create the necessary messages table in PostgreSQL <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>.
*   **Real-time Reporting**: Agents can provide real-time updates on their actions (e.g., "I'm getting the contents of this file") by inserting messages into the database, which are then streamed to the user interface <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
*   **Output**: The API output is basic, primarily indicating success or failure, as AI messages are stored directly in the database <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

The Live Agent Studio also hosts a hackathon competition with a $5,000 prize pool, encouraging participants to build and submit their own AI agents following the compatibility guidelines <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. Sample agents and extensive documentation are available on the platform's GitHub repository to assist developers <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

## Future Enhancements and General Advice

*   **RAG (Retrieval Augmented Generation)**: A future enhancement includes integrating a [[RAG AI agent development | RAG pipeline]] to allow the agent to perform vector searches and retrieve answers from a knowledge base for more complex queries <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. This would typically involve a third tool and a separate background process for indexing repositories <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   **Production Readiness**: Moving beyond the prototype, production-ready agents often involve custom coding with frameworks like [[Building AI Agents | Pydantic AI]] or LangChain for more complex logic (e.g., checking both 'main' and 'master' branches) <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>. [[AI agents and their development | Pydantic AI]] and LangGraph work well together, with Pydantic AI for building agents and LangGraph for orchestrating them <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   **Private Repositories**: The current prototype is limited to public GitHub repositories <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.
*   **Multi-Agent Workflows**: [[AI agents and their development | n8n]] supports multi-agent workflows where a primary "orchestrator" agent decides which expert sub-agent to use, often by setting up sub-agents as tools <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
*   **Hosting LLMs**: For open-source LLMs, cloud providers like RunPod or Novita AI offer GPU instances for self-hosting. Alternatively, services like OpenRouter provide API access to a wide range of open-source models, often at a lower cost <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   **Front-end UI**: For client-facing chatbots, Voiceflow or n8n's widgets can be used. For internal applications, custom React front-ends (built with AI coding assistants like Bolt or Lovable) or Python UI libraries like Streamlit are recommended <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   **Learning Resources**: For non-technical users, YouTube tutorials and community involvement are valuable for learning about [[AI agents and their development | AI agent development]] <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>. [[AI agents learning roadmap | The current mini-series]] and the resources provided by the Live Agent Studio are designed to be accessible <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.