---
title: Large language models in code generation
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

This article explores the application of [[large_language_models_in_ai_agents | large language models (LLMs)]] in generating code, specifically for automated video editing. The discussion centers on Va's first open-source video editing agent, developed in collaboration between Diffusion Studio and Reskill [01:06].

## The Need for Automated Video Editing

The initiative for this agent arose from a need for an automatic tool to edit videos for Reskill, a platform focused on personalized learning [01:12]. Traditional tools like FFmpeg presented limitations, leading to the search for more intuitive and flexible alternatives [01:22]. While Remotion offered some solutions, it had issues with unreliable server-side rendering [01:30]. The `core` library from Diffusion Studio was chosen due to its favorable API, which eliminated the need for a separate rendering backend [01:35].

## Leveraging LLMs for Code Generation

The `core` library enables complex compositions through a JavaScript/TypeScript-based programmatic interface [01:46]. This capability is crucial because it allows [[large_language_models_in_ai_agents | LLMs]] to generate the necessary code to run the video editing processes [01:54].

The core concept behind this approach is to empower the [[large_language_models_in_ai_agents | LLM]] to write its own actions in code [02:00]. This method is preferred because:

> Code is the best possible way to express actions performed by a computer [02:05].

Furthermore, multiple research papers have demonstrated that [[large_language_models_in_ai_agents | LLM]] tool calling is significantly more effective when implemented in code compared to JSON [02:13].

## Agent Architecture and Workflow

The current architecture of the video editing agent involves an [[large_language_models_in_ai_agents | LLM]] that initiates a browser session using Playwright and connects to an operator UI [02:27]. This web application serves as a video editing UI specifically designed for [[large_language_models_in_ai_agents | AI agents]], rendering video directly in the browser via the WebCodecs API [02:35]. Helper functions facilitate file transfers between Python and the browser using the Chromium DevTools protocol [02:46].

The typical flow for the agent involves three main tools [03:00]:

1.  **Video Editing Tool**: Generates code based on a user prompt and executes it in the browser [03:08].
2.  **Doc Search Tool**: Utilizes RCK to retrieve relevant information if additional context is required [03:17].
3.  **Visual Feedback Tool**: After each execution step, compositions are sampled (currently at one frame per second) and fed to this tool [03:25]. The visual feedback tool acts as a "generator and discriminator," similar to the GAN architecture [03:33].

Once the visual feedback tool provides a "green light," the agent proceeds to render the composition [03:44].

## `llm.txt` for Agent Control

The system also ships with `llm.txt`, which functions similarly to `robots.txt` but for agents [03:55]. This file, combined with specific template prompts, can significantly enhance video editing capabilities [04:00].

## Future Development and Remote Capabilities

While the first version of the agent is implemented in Python, a TypeScript implementation is currently underway [04:37]. The project adheres to the saying, "any applications that can be written in typescript will be written in typescript" [04:49].

The setup is flexible, allowing the agent to connect to a remote browser session via WebSocket, with each agent receiving a separate, GPU-accelerated browser session behind a load balancer [04:14].