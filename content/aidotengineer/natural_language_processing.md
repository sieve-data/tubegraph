---
title: Natural language processing
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

Natural Language Processing (NLP) is a field that is home to a paper described as "legendary" within its domain: "Attention Is All You Need" <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This paper is not just a catchy title but a foundational work in NLP <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## AI Video Editing Agent

A novel open-source video editing agent has been developed, addressing the need for an automatic tool to edit videos for ReSkill, a personalized learning platform <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. Initial attempts highlighted limitations with FFMpeg, leading to a search for more intuitive and flexible alternatives <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. While Remotion offered server-side rendering, it proved unreliable <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The development team found success with the "core" library from Diffusion Studio, appreciating its API that didn't require a separate rendering backend <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A collaboration with the library's author led to the creation of this agent <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Leveraging [[large_language_models_in_code_generation | Large Language Models in Code Generation]]

The "core" library enables complex compositions through a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This capability allows for the use of [[large_language_models_in_code_generation | LLMs]] to generate code to run these compositions <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

A key insight is that if an [[large_language_models_in_ai_agents | LLM]] can write its own actions in code, it forms a perfect match, as code is considered the best way to express computer-performed actions <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Research papers have also demonstrated that [[large_language_models_in_ai_agents | LLM]] tool calling via code is superior to JSON-based methods <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Agent Architecture and Workflow

The current architecture of the agent operates as follows <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:
1.  The agent initiates a browser session using Playwright and connects to an "operator UI" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  This web app serves as the video editing UI, designed specifically for [[large_language_models_in_ai_agents | AI agents]], rendering video directly in the browser using the WebCodecs API <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
3.  Helper functions facilitate file transfer between Python and the browser via the Chromium DevTools protocol <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

The agent's typical workflow involves three main tools <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>:

*   **Video Editing Tool:** Generates code based on user prompts and executes it in the browser <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Doc Search Tool:** Utilizes RCK to retrieve relevant information if additional context is needed <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Visual Feedback Tool:** After each execution step, compositions are sampled (currently at one frame per second) and fed to this tool <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. It functions similarly to a generator and discriminator in a Generative Adversarial Network (GAN) architecture <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Once the visual feedback tool gives a "green light," the agent proceeds to render the composition <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### [[integrating_ai_into_natural_workflows | Integrating AI into Natural Workflows]]

The concept of `llm.txt` is introduced, functioning like `robots.txt` but for [[large_language_models_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This, combined with specific template prompts, is designed to significantly aid the video editing process <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

While users can run the agent with their own browser, the setup supports connecting the agent to a remote browser session via a WebSocket <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Each agent can obtain a separate, GPU-accelerated browser session, backed by a load balancer <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

The initial version of the agent is implemented in Python, with a TypeScript implementation currently underway <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This aligns with the saying: "any applications that can be written in TypeScript will be written in TypeScript" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

This project is a collaboration between Diffusion Studio and RSkill <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.