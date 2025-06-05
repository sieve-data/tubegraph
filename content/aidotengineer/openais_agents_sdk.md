---
title: OpenAIs Agents SDK
videoId: UcW_s4BmuD0
---

From: [[aidotengineer]] <br/> 

OpenAI's Agents SDK is highlighted as a preferred [[components_of_ai_agents | agent framework]] for [[building_and_improving_ai_agents | building and improving AI agents]] in a full-stack, serverless environment <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Overview and Preference

The speaker, Brook Riio, chose OpenAI's Agents SDK from its initial announcement due to its capabilities <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This SDK offers significant "agentic power" for developing AI applications <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Key Features

The OpenAI Agents SDK includes several notable features:
*   **Native Tool Calling** It supports native tool calling capabilities <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **One-Shot Multi-Agent Calls** It facilitates one-shot multi-agent calls <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Built-in Tracing and Eval Hooks** These features provide robust observability, allowing users to understand the agent's behavior <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Strong Backing and Model Interchangeability** The SDK has strong support from OpenAI, ensuring its longevity and continuous development <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. It also allows for interchangeability of models, preventing developers from being locked into a single ecosystem <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Python Only** Currently, the OpenAI Agents SDK is exclusively available for Python <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

## Integration in a Full-Stack Architecture

In a recommended full-stack serverless architecture, OpenAI agents run within Python serverless functions <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. When deployed to a platform like Vercel, the platform automatically recognizes and hosts these Python functions <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. These functions handle AI inference and interact with OpenAI to perform tasks <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

### Example Application

An example application demonstrated uses AI agents to create a newsletter <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. The [[components_of_ai_agents | AI agents]] are powered by Fast API, which allows for quick assembly and execution <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. The example includes:
*   A research agent <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   A formatting agent <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Each agent has its own endpoint in the Fast API application <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
*   Vercel can deploy these agents as independent cloud functions with minimal configuration <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

The workflow for these agents is orchestrated by Ingest, with each step invoking a specific agent function <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>:
1.  Call the research agent <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
2.  Format the newsletter with another agent <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
3.  Save the results to blob storage for the front end <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

The results from the initial research agent are type-checked and then passed to the formatting agent <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. The formatted content is then type-checked and saved to blob storage <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.