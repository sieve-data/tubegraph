---
title: Modus agent orchestration framework
videoId: tYCu_57jzL8
---

From: [[aidotengineer]] <br/> 

Modus is an [[agent_orchestration_and_parallel_processing | open-source framework]] for creating [[ai_agents_and_agentic_workflows | AI agents]] <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. Developed by Hypermode, its primary purpose is to bring data to models and expose tools and abstractions for working with [[ai_agents_and_agentic_workflows | agentic workflows]] <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>, <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>, <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>. The project is available on GitHub <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>, <a class="yt-timestamp" data-t="00:24:43">[00:24:43]</a>.

## Core Functionality

Modus provides abstractions for:
*   Working with models and data <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.
*   A runtime designed for managing a large number of [[ai_agents_and_agentic_workflows | agents]] that are stateful and long-running <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>, <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>, <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>.
*   An SDK library for interacting with [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.

## Web Assembly Integration

A key feature of Modus is its use of Web Assembly (Wasm) <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. This allows the framework to:
*   Target multiple languages for different SDKs <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>, <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.
*   Enable users to write their logic in languages like Go or AssemblyScript, which is then compiled to Web Assembly under the hood <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>, <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>, <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>, <a class="yt-timestamp" data-t="00:25:36">[00:25:36]</a>.
*   Generate a single, unified GraphQL API by leveraging user-defined types and function signatures <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>, <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>, <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>, <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>, <a class="yt-timestamp" data-t="00:25:51">[00:25:51]</a>.
*   Provide advantages in security and a sandboxed environment for [[ai_agents_and_agentic_workflows | AI agents]] <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>, with the Web Assembly aspects abstracted away from the user <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>, <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>, <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a>.

## Building Domain-Specific Agents with Modus

Modus, in combination with Dgraph for building knowledge graphs, supports the creation of domain-specific [[ai_agents_and_agentic_workflows | agents]] <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>, <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>, <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>, <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>. A core concept is to enable users to get [[building_effective_agents | agents]] up and running quickly by defining a prompt and exposing tools via a Model Context Protocol (MCP) server <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>, <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>, <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>, <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>, <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>, <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.

### Hypermode Agents

Hypermode [[ai_agents_and_agentic_workflows | agents]] utilize Modus as their underlying framework <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. They can be created from a prompt and given access to MCP-powered connections <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>, <a class="yt-timestamp" data-t="00:31:44">[00:31:44]</a>, <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. Users can define a prompt to give the agent background information and select a reasoning model (e.g., GPT-4) to orchestrate its actions <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>, <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>, <a class="yt-timestamp" data-t="00:27:38">[00:27:38]</a>, <a class="yt-timestamp" data-t="00:27:40">[00:27:40]</a>, <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

Agents require connections to interact with their environment <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>, <a class="yt-timestamp" data-t="00:27:52">[00:27:52]</a>, <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>. These connections, such as GitHub or Notion, are MCP servers that expose tools, allowing the agent to interact with these services on the user's behalf <a class="yt-timestamp" data-t="00:27:57">[00:27:57]</a>, <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>, <a class="yt-timestamp" data-t="00:28:03">[00:28:03]</a>, <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>, <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

A useful feature is the ability to "eject to code," allowing users to access the underlying Modus code used to run the agent. This enables the addition of more complex logic or other connections to enhance the agent <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>, <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>, <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a>, <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>, <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>, <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.