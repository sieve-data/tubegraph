---
title: Docker for AI Workshops
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article details the use of Docker for setting up and running an interactive AI workshop, particularly focusing on the development of stateful agents. The workshop leverages a server-client architecture with Docker serving as the containerization platform for the server component.

## Workshop Prerequisites
To participate in the interactive component of the workshop, users are recommended to have Docker installed on their laptops <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. After installing Docker, users need to pull a specific Docker image, which serves as the server for the workshop <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. A Jupyter notebook, accessible via a provided link or through a `workshops` channel, acts as the client that runs against this Docker server <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The materials are also available online for later access <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Most attendees confirmed having Docker installed on their laptops <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The Python programming language is used for the workshop <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. While Python is used for the client and backend logic, the server itself can be written in other languages like Go or Rust, and there are TypeScript and REST API SDKs available <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>.

## Workshop Setup Steps
1.  **Start the Leta Server**: Use a `docker run` command to kick off the Leta server from the pulled Docker image <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. This command can be copied from the GitHub link or the Slack channel <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. A free, live endpoint is available, so API keys are not required for the demo <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
2.  **Clone the Repository**: Clone the workshop's GitHub repository <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
3.  **Navigate to Example Directory**: Change the directory into the specific example folder <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>.
4.  **Launch Jupyter Notebook**: Run the Jupyter notebook command, which should automatically open a browser tab with the notebook <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.

## Architecture and Benefits of Docker in AI Agent Development
The Leta stack, used in the workshop, is an open-source system built with Fast API, Postgress, and Python logic <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. The Docker container exposes a robustly documented API, which is how interactions with the AI agents occur <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

### Server-Client Paradigm for Stateful Agents
A key distinction of the Leta framework, compared to others like LangChain or AutoGen, is its server-client process <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. This is crucial because agents are intended to be stateful and persist indefinitely <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>. Persisting information indefinitely is difficult when holding everything in application state; thus, a server acts as a centralized source of truth <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

By running the server in a Docker image, it can be parked anywhere, including in the cloud or easily deployed on Kubernetes <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>. This setup means that once an agent is created, a handle is provided, and subsequent messages are sent to this handle without needing to provide the full conversation history every time <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>. This is a core aspect of enabling stateful agents.

### [[Building AI Sandboxes | Sandboxed Tools]]
Tools used by agents within Leta are automatically [[building_ai_sandboxes | sandboxed]] by default <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>. This allows arbitrary Python code to run securely inside the sandbox, which is essential for deployments where multiple users' tools shouldn't interfere with each other <a class="yt-timestamp" data-t="01:00:14">[01:00:14]</a>. E2B is supported by default for local sandboxing, and E2B keys can be used for private cloud deployments <a class="yt-timestamp" data-t="01:00:19">[01:00:19]</a>.

### Multi-Agent Systems
Docker-based deployments enable robust [[multiagent_orchestration_for_ai_copilot_development | multi-agent orchestration]]. Unlike some frameworks where agents are "trapped" in a Python file and cannot run asynchronously, Leta's stateful agents run on servers and maintain state, making them accessible via APIs <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This architecture allows agents to communicate with each other through message passing over APIs, similar to how humans interface in a remote company using communication tools like Slack <a class="yt-timestamp" data-t="01:02:26">[01:02:26]</a>. This facilitates asynchronous communication and enables agents to share information across different agents, as memory blocks can be linked together <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>.

### Development Workflow and [[Best Practices for Building AI Systems | Best Practices]]
For rapid iteration, a low-code environment like the Leta UI (web-based application) is often faster than an SDK <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>. This UI allows users to easily create agents, set memory blocks, and send messages in a visualized form <a class="yt-timestamp" data-t="00:56:19">[00:56:19]</a>. It also provides insights into the agent's context window, showing the full payload being sent to the LLM, aiding in debugging and optimization <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>. The UI helps developers see what's going through the context window, which is often difficult to trace in other frameworks <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>.

The ability to easily run and test tools separately from the agent is also highlighted as an advantage <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>. Developers can write custom Python tools and even make them meta by importing the Leta client within the tool itself, allowing agents to create or manage other agents <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>. This flexibility supports [[impact_of_ai_on_development_workflow | complex AI development workflows]].

Overall, using Docker for the Leta server facilitates the development of robust, stateful AI agents by providing a persistent, scalable, and secure environment for agent services and their associated tools.