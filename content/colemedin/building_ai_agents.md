---
title: Building AI Agents
videoId: yRIEpNlacd0
---

From: [[colemedin]] <br/> 

This article outlines a process for building and refining the front end of an AI agent, leveraging a combination of AI coding assistants to achieve a custom, polished user interface. The discussed methodology emphasizes balancing speed, flexibility, and cost-effectiveness in development <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Overview of the Process
The series focuses on [[building_fullscale_ai_agents | building fullscale AI agents]] by creating a GitHub agent capable of consuming entire repositories for code Q&A <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The initial steps involved integrating the agent with the Live Agent Studio Agent Zero platform to provide a quick front end <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This article details the process of creating a custom front end using AI coding assistants <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

The overall approach involves combining various AI coding assistants:
*   **Lovable / Bolt.new**: For quickly generating a solid foundation and starting the project <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. These platforms optimize for a single Large Language Model (LLM), offering excellent initial performance <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. Lovable is particularly good for chat-style applications <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Bolt. DIY**: For free and extensive iteration and tweaking of the application. It's open-source and allows users to run it on their own computer with any LLM, many of which are free to use <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>, <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **AI IDEs (e.g., Windsurf, Cursor)**: For making more directed and refined changes once the initial foundation is established <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>, <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. These run on the user's computer <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

This combination provides a blend of speed, flexibility, and cost-effectiveness <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Step-by-Step Front End Development
The [[step_by_step_process_for_building_ai_agents | process for building AI agents]] and their front ends is as follows:

### 1. Initial Project Generation with Lovable
The first step is to use Lovable (or Bolt.new) to create the foundational front end <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Prompt Engineering**: A detailed prompt is provided to Lovable, specifying:
    *   **UI/UX**: Desired dark theme with specific colors <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
    *   **Agent URL**: The API endpoint for the agent (e.g., `http://localhost:8000/chat`) <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>. This assumes the agent was previously set up as an API endpoint <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
    *   **Input Schema**: The expected payload for the agent (e.g., `input`, `conversation_id`, `message_history`) <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>.
    *   **Output Schema**: The expected response format from the agent (e.g., `response`, `conversation_id`) <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
    *   **Superbase Integration**: Inclusion of Superbase URL and public key directly in the code for conversation and chat history management <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>. The schema for the `messages` table in Superbase is also provided, detailing fields like `created_at`, `conversation_id`, `type`, and `content` <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>, <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.
    *   **Real-time Capabilities**: Specification to enable real-time communication for the messages table, allowing the front end to subscribe to and immediately pull new messages from the agent <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>.
    *   **Additional Requirements**: A list of miscellaneous features such as Markdown handling, loading indicators, and Superbase authentication with email and password <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
*   **Execution**: The prompt is fed into Lovable, which then generates the application <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. Lovable provides free credits to get started <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

### 2. Refining with Bolt. DIY
After the initial generation, the project is moved to Bolt. DIY for further refinement and tweaking without incurring additional costs <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>, <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Publish to GitHub**: The Lovable project is transferred to a GitHub repository <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. It's recommended to make the repository public for easier import into Bolt. DIY <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>.
*   **Install Bolt. DIY**: Bolt. DIY runs on the user's local machine <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>. Installation typically involves cloning the repository, installing Node.js dependencies (`pnpm install`), and then running the development server (`pnpm run Dev`) <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>.
*   **Import Project**: The GitHub repository is cloned into Bolt. DIY <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.
*   **Iterative Tweaking**: Bolt. DIY allows for free iteration and refinement of the UI/UX <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. Key advice for prompting in Bolt. DIY is to request one change at a time <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>. Bolt. DIY also supports image input (e.g., screenshots) with models like Gemini, allowing for visual feedback on UI elements <a class="yt-timestamp" data-t="21:28:00">[21:28:00]</a>.
*   **Note**: Chatting with the agent directly within Bolt. DIY (or Bolt.new) may not work if the agent is running on Local Host, as the web container might block such requests <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>.

### 3. Final Touches with an AI IDE
Once the core UI/UX is satisfactory, the project can be downloaded from Bolt. DIY and brought into an AI IDE like Windsurf or Cursor for final, more directed changes <a class="yt-timestamp" data-t="22:23:00">[22:23:00]</a>.
*   **Download Code**: Bolt. DIY provides a "Download code" button, which downloads a zip file of the project <a class="yt-timestamp" data-t="22:29:00">[22:29:00]</a>.
*   **Run Locally**: The downloaded project can be unzipped and run locally using standard Node.js commands (`npm install`, `npm run dev`) <a class="yt-timestamp" data-t="22:44:00">[22:44:00]</a>.
*   **Refine in AI IDE**: AI IDEs are ideal for making precise, directed changes that might be harder to achieve with in-browser editors once a project is more mature <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>.

## The Live Agent Studio
The Live Agent Studio is a platform built for collaborating on open-source AI agents <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. Agents can be built using various platforms like [[building_ai_agents_with_python | Python]], n8n, or Voiceflow, and then published to the Studio <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. To be compatible with the Live Agent Studio, agents must follow specific guidelines, often involving turning the agent into an API endpoint <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>. This practice of exposing an agent as an API endpoint is a best practice for hooking it into any front end <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

## Conclusion
This multi-tool approach provides a "Perfect Blend of free, flexible, and fast" development for AI agent front ends <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. The next steps in the series will involve further testing, refining, and finally [[building_productiongrade_ai_agents | deploying the AI agent]] <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>, aiming to create a monetizable product <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.