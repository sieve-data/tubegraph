---
title: Docker and Jupyter Notebook Setup for AI Workshops
videoId: E0k9Ppq6yXY
---

From: [[aidotengineer]] <br/> 

This article details the setup process for participating in interactive AI workshops, specifically focusing on the use of Docker and Jupyter Notebooks for local environment configuration and execution. The setup allows users to follow along with live coding examples and experiments with AI agents <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Prerequisites

To participate actively in the workshop, users should install [[leveraging_existing_infrastructure_for_ai_integration | Docker]] on their laptop <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. While it's possible to use `pip` for installation, [[coding_and_debugging_in_ai_workshops | Docker]] is recommended due to potential package management issues with `pip` <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The materials are also available online for later follow-along <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Workshop Setup Steps

The core of the workshop involves running a Jupyter Notebook client against a server provided via a Docker image <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### 1. Pull the Docker Image

The first step is to pull the specific Docker image for the workshop <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This step is crucial for setting up the server component <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### 2. Obtain the Jupyter Notebook

The workshop notebook is available via a link in the designated "workshops" Slack channel (e.g., `workshops-leta`) <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This link provides the notebook file that will be used for the interactive session <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The `readme` in the GitHub link also contains all the necessary commands <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

### 3. Start the Leta Server

After pulling the Docker image, the next step is to start the Leta server. This is done by running a `docker run` command <a class="yt-timestamp" data-t="00:16:26">[00:16:26]</a>. The command can be copied from the GitHub link or the Slack channel <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.

The Leta stack is open-source, built with Fast API, PostgreSQL, and Python logic <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. The Docker container exposes an API that agents interact with <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. For local setup, the server runs on `localhost` at the default port <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. A free live endpoint is also available, meaning no keys are needed for the demo <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

### 4. Clone the Repository and Navigate

Users need to clone the workshop repository and then `cd` into the specific example directory <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

### 5. Run the Jupyter Notebook

Assuming Python is installed, the Jupyter Notebook command should be run. This automatically opens a browser tab with the notebook, which users can then double-click to open <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.

## Client-Server Interaction

The notebook acts as a client, and the Docker image provides the Leta server <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Unlike frameworks where an agent is created in memory and passed to the server for completion (e.g., `chat completions`), Leta involves creating the agent on the server and then obtaining a handle to send messages without needing to track the full state client-side <a class="yt-timestamp" data-t="00:22:53">[00:22:53]</a>.

## Troubleshooting

*   **Directory does not exist**: If encountering a "directory doesn't exist" error during setup, perform an `ls -R` command to resolve it <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **No Streaming**: The "Leta Free" endpoint does not have streaming enabled <a class="yt-timestamp" data-t="00:57:30">[00:57:30]</a>.

## Workshop Content Overview

The Jupyter Notebook session demonstrates basic concepts of [[ai_in_workflow_automation | AI]] agent memory and state management <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

It covers:
*   **Creating Agents**: How to instantiate an agent on the Leta server <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.
*   **Memory Blocks**: The fundamental units of memory in a Leta agent, which are editable strings <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. These can be rewritten by the agent itself <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.
*   **Context Window Management**: How Leta manages the LLM's context window, allowing artificial capping of its length (e.g., to 10k tokens) to control costs and latency, even with long-running workflows <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. This is more intelligent than simple recursive summarization <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.
*   **Agent Reasoning**: Every Leta agent comes with built-in reasoning (e.g., React style) <a class="yt-timestamp" data-t="00:26:19">[00:26:19]</a>.
*   **Memory Tiers**: Leta utilizes two tiers of memory:
    *   **Core Memory**: High-level, in-context memory, akin to immediate human recall <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
    *   **Archival/Recall Memory**: Data sources outside the context window that the agent can "jog its memory" from, similar to semantic episodic memory <a class="yt-timestamp" data-t="00:30:33">[00:30:33]</a>. Archival memory is a vector database by default <a class="yt-timestamp" data-t="00:45:54">[00:45:54]</a>.
*   **Tool Calling**: The system emphasizes [[coding_and_debugging_in_ai_workshops | tool calling]], making the LLM aware of the context problem and providing tools to manage memory <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. Tools are executed server-side and are sandboxed <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. Custom tools can be written in Python <a class="yt-timestamp" data-t="00:49:23">[00:49:23]</a>, and agents can even manage other agents' memory <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
*   **Multi-Agent Systems**: Leta supports building multi-agent systems where agents can communicate via message passing through APIs, similar to human asynchronous communication <a class="yt-timestamp" data-t="01:02:24">[01:02:24]</a>. Agents exist independently and maintain state, allowing them to be "detached" or re-grouped <a class="yt-timestamp" data-t="01:02:05">[01:02:05]</a>.