---
title: AI in video editing
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

An open-source video editing agent has been developed by va <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This agent was created to address the need for an automatic tool to edit videos for rskill, a platform focused on personalized learning <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## Development Backstory and Core Libraries

Initial attempts with FFMPEG revealed limitations, prompting a search for more intuitive and flexible alternatives <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>. While Remotion offered service-side rendering, it proved unreliable <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. The `core` library from Diffusion Studio was chosen due to its intuitive API, which did not necessitate a separate rendering backend <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. This led to a collaboration with the library's author to build the agent <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

The `core` library facilitates complex video compositions via a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This means that large language models (LLMs) can be utilized to generate the code required to run compositions <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

### Why Code for LLM Actions?

Leveraging LLMs to write their own actions in code is considered a perfect match for [[integrating_ai_into_natural_workflows | AI integration]] because code is the most effective way to express actions performed by a computer <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. Additionally, research indicates that LLM tool calling implemented in code is superior to JSON <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

## Architecture of the AI Video Editing Agent

The current [[architecture_of_ai_video_editing_agent | architecture of the AI video editing agent]] operates as follows:

1.  **Browser Session**: The agent initiates a browser session using Playwright and connects to an operator UI <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.
2.  **Operator UI**: This web application serves as a video editing interface specifically designed for [[ai_in_workflow_automation_and_augmentation | AI agents]] <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. It renders video directly within the browser using the WebCodecs API <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Helper functions are included for file transfers between Python and the browser via the Chromium DevTools protocol <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.

### Agent Workflow and Tools

A typical flow for the agent involves three primary tools <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>:

1.  **Video Editing Tool**: Generates code based on a user prompt and executes it in the browser <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
2.  **Doc Search Tool**: If additional context is required, this tool uses RAG (Retrieval Augmented Generation) to retrieve relevant information <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
3.  **Visual Feedback Tool**: After each execution step, compositions are sampled (currently at one frame per second) and fed to this tool <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. It functions similarly to a generator and discriminator in a GAN (Generative Adversarial Network) architecture <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. Once the visual feedback tool gives a "green light," the agent proceeds to render the final composition <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### lm.txt

An `lm.txt` file has been shipped, which is analogous to `robots.txt` but designed for agents <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. This file, combined with specific template prompts, is intended to significantly enhance the video editing journey <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

## Deployment and Future Development

While users can bring their own browser to run the agent, the current setup also supports connecting the agent to a remote browser session via WebSocket <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. Each agent can obtain a separate, GPU-accelerated browser session, backed by a load balancer <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.

The initial version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>. This aligns with the saying, "Any application that can be written in TypeScript will be written in TypeScript" <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

This project is a collaboration between Diffusion Studio and rskill <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.