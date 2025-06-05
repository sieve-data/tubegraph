---
title: Architecture of AI video editing agent
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

The VA's first open-source video editing agent was developed to automate video editing tasks <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>, <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This agent was created to address the need for an automatic tool to edit videos for ReSkill, a platform for personalized learning <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>, <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Development Motivation

Previous attempts to automate video editing using tools like FFmpeg proved limited <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>, and Remotion offered unreliable service-side rendering <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>, <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. The developers found a suitable alternative in Core, a library whose API did not require a separate rendering backend <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>, <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>, <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>. This led to a collaboration with the author of the Core library to build the agent <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>, <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

## Core Technology

The agent leverages the Core library from Diffusion Studio, which enables complex compositions through a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>, <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>, <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. This setup allows a Large Language Model (LLM) to generate code to perform video editing actions <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>, <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. The approach is considered ideal because code is the most effective way for an LLM to express actions to be performed by a computer <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>, <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>, <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>, <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>, <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. Research also indicates that LLM tool calling via code is superior to JSON <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>, <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>, <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>, <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

## Current Architecture

The agent's current architecture involves the following:
*   **Browser Session**: The agent initiates a browser session using Playwright <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>, <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>, <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   **Operator UI**: It connects to an Operator UI, a web application specifically designed as a video editing interface for [[Components of AI agents | AI agents]] <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>, <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **In-Browser Rendering**: The Operator UI renders video directly within the browser using the WebCodecs API <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>, <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   **File Transfer**: Helper functions facilitate file transfer between Python and the browser via the Chromium DevTools protocol <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>, <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>, <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Agent Workflow and Tools

The typical flow of the agent involves three main tools:

1.  **Video Editing Tool**: Generates code based on user prompts and executes it in the browser <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>, <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>, <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>, <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>, <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
2.  **Doc Search Tool**: If additional context is required, this tool uses RAG (Retrieval-Augmented Generation) to retrieve relevant information <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>, <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>, <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
3.  **Visual Feedback Tool**: After each execution step, compositions are sampled (currently at one frame per second) and fed to this tool <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>, <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>, <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>, <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. This tool functions similarly to a generator and discriminator in a GAN [[Different architectures for AI agents | architecture]] <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>, <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>, <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>, <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Once the visual feedback tool provides a "green light," the agent proceeds to render the final composition <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>, <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>, <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>, <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

### lm.txt

The project also ships with `lm.txt`, which is analogous to `robots.txt` but for agents <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>, <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. This file, combined with specific template prompts, significantly aids the video editing process <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>, <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

## Deployment Flexibility

While users can run the agent with their own browser, the current setup allows the agent to connect to a remote browser session via WebSockets <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>, <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>, <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>, <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. Each agent can obtain a separate, GPU-accelerated browser session, backed by a load balancer <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>, <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>, <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>, <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.

## Future Development

The initial version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>, <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>, <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

## Collaboration

This project is a collaboration between Diffusion Studio and ReSkill <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>, <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>.