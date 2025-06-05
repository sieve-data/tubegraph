---
title: Natural Language Processing and AI
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

## Foundational Concepts

In the field of [[natural_language_processing_nlp|Natural Language Processing (NLP)]], a legendary paper titled "Attention Is All You Need" is widely recognized <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## AI Agents in Video Editing

An open-source video editing [[developing_ai_agents_for_productivity|agent]] has been developed to automate video editing for a platform called ReSkill, which focuses on personalized learning <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Initial attempts with FFmpeg showed limitations, leading to the search for more intuitive and flexible alternatives <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Remotion was considered but had unreliable server-side rendering <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The "Core" library from Diffusion Studio was chosen due to its API, which did not require a separate rendering backend <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This library enables complex compositions via a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This allows [[llm_and_code_generation|Large Language Models (LLMs)]] to generate code to run the system <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

### LLMs and Code Generation
When an LLM can write its own actions in code, it forms a perfect match because code is considered the best way to express computer actions <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Multiple research papers have indicated that LLM [[tool_usage_and_development_in_ai_frameworks|tool calling]] implemented in code is significantly more effective than in JSON <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Agent Architecture and Workflow

The current architecture of the video editing agent operates as follows:
*   **Browser Session** The agent initiates a browser session using Playwright and connects to an Operator UI <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   **Operator UI** This web application serves as a video editing interface specifically designed for AI agents <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. It renders video directly in the browser using the Web Codecs API <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **File Transfer** Helper functions facilitate file transfer between Python and the browser via the Chromium DevTools protocol <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The typical workflow involves three main tools:
1.  **Video Editing Tool** Generates code based on user prompts and executes it in the browser <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  **Doc Search Tool** Utilizes Retrieval-Augmented Generation (RAG) to fetch relevant information if additional context is needed <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
3.  **Visual Feedback Tool** After each execution step, video compositions are sampled (currently at one frame per second) and fed to this tool <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. The visual feedback tool acts as a generator and discriminator, similar to the Generative Adversarial Network (GAN) architecture <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Once the visual feedback tool gives a "green light," the agent proceeds to render the final composition <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

## Agent Control and Deployment

A file named `lm.txt` has been shipped, which functions similarly to `robots.txt` but for agents <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. `lm.txt`, combined with specific template prompts, can significantly aid in the video editing process <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

The current setup is flexible, allowing the agent to connect to a remote browser session via WebSocket, enabling each agent to have a separate, GPU-accelerated browser session behind a load balancer <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

The first version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This aligns with the saying that "any application that can be written in TypeScript will be written in TypeScript" <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This project is a collaboration between Diffusion Studio and Rskill <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.