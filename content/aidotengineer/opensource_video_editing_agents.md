---
title: Opensource Video Editing Agents
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

Mam introduced the va's first [[video_editing_process_with_ai_and_tools | open-source video editing agent]] <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. The motivation for creating this agent stemmed from the need for an automatic tool to edit videos for reskill, a platform focused on personalized learning while doing <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>.

## Development and Core Technology
Initially, the limitations of FFMPEG became apparent, leading the team to seek more intuitive and flexible alternatives <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. While Remotion was considered, it presented unreliable service-side rendering <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. The `core` library, on the other hand, was favored for its API, which did not require a separate rendering backend <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. This led to a collaboration with the author of the `core` library from Diffusion Studio to build the agent together <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

The `core` library can perform complex compositions through a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This design allows Large Language Models (LLMs) to generate code to run these compositions <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The approach of letting an LLM write its own actions in code is considered a perfect match, as code is the most effective way to express actions performed by a computer <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Research also supports that LLM tool calling via code is superior to JSON <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

## Architecture
The current architecture of the agent operates as follows:
*   The agent initiates a browser session using Playwright <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
*   It then connects to `operator UI`, a web application specifically designed as a video editing interface for [[ai_agents_using_humanlike_interfaces_and_workflows | AI agents]] <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   `operator UI` renders video directly in the browser using the WebCodecs API <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   Helper functions facilitate file transfers between Python and the browser using the Chromium Dev Tool protocol <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Agent Workflow and Tools
A typical flow for the agent involves three primary tools <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>:
1.  **Video Editing Tool**: Generates code based on user prompts and executes it in the browser <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
2.  **Doc Search Tool**: If additional context is required, this tool utilizes RAG to retrieve relevant information <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
3.  **Visual Feedback Tool**: After each execution step, compositions are sampled (currently at one frame per second) and fed into this tool <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. This tool functions similarly to a generator and discriminator in a GAN architecture <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. Once the visual feedback tool gives a "green light," the agent proceeds to render the composition <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

## Agent Directives and Connectivity
The project also includes `lm.txt`, which is analogous to `robots.txt` but for agents <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This, combined with specific template prompts, significantly aids in the video editing process <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

While users can run the agent with their own browser, the setup is flexible enough to allow the agent to connect to a remote browser session via WebSocket <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. Each agent can obtain a separate, GPU-accelerated browser session, supported by a load balancer <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

The initial version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. This project is a collaboration between Diffusion Studio and Rskill <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.