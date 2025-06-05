---
title: Video Editing Process with AI and Tools
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

This article explores an [[opensource_video_editing_agents | open-source video editing agent]] designed to automate video production, addressing the limitations of traditional methods and leveraging AI for enhanced efficiency and flexibility <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The project emerged from a need for an automatic tool to edit videos for reskill, a platform focused on personalized learning <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Evolution of the Toolset

Initially, traditional tools like FFMpeg presented limitations, prompting a search for more intuitive and flexible alternatives <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Remotion was considered but exhibited unreliable server-side rendering <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The Core library proved more suitable due to its API not requiring a separate rendering backend <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This led to a collaboration with the Core library's author to build the agent <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The Core library, developed by Diffusion Studio, enables complex compositions through a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This capability allows Large Language Models (LLMs) to generate code for running the video editing processes <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## AI Integration and Code Generation

A core aspect of this agent is the use of LLMs to write their own actions in code <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Code is considered the optimal way to express actions performed by a computer <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Multiple research papers support the idea that LLM [[using_tools_and_function_calls_with_ai_sdk | tool calling]] implemented in code is superior to JSON <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Current Architecture

The agent's architecture involves several key components:
*   **Browser Session**: The agent initiates a browser session using Playwright <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Operator UI**: It connects to an Operator UI, which is a web application specifically designed as a video editing interface for AI agents <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
*   **In-browser Rendering**: Video is rendered directly in the browser using the WebCodecs API <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **File Transfer**: Helper functions facilitate file transfer between Python and the browser via the Chromium Dev tool protocol <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Agent Workflow

The typical flow of the agent involves three primary tools <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>:

1.  **Video Editing Tool**: This tool generates code based on user prompts and executes it in the browser <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  **Doc Search Tool**: If additional context is required, this tool uses RAG (Retrieval Augmented Generation) to retrieve relevant information <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Visual Feedback Tool**: After each execution step, compositions are sampled at one frame per second and fed to this tool <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. It functions similarly to a generator and discriminator in a Generative Adversarial Network (GAN) architecture <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Once the visual feedback tool provides a "green light," the agent proceeds to render the composition <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### lm.txt and Flexibility

The system includes `lm.txt`, which serves a similar purpose to `robots.txt` but for agents <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. When combined with specific template prompts, `lm.txt` can significantly aid the video editing process <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

The setup offers flexibility, allowing users to bring their own browser or connect the agent to a remote browser session via WebSocket <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Each agent can obtain a separate, GPU-accelerated browser session, supported by a load balancer <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

The initial version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This project is a collaborative effort between Diffusion Studio and Rskill <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.