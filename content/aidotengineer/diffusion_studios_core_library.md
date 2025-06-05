---
title: Diffusion Studios core library
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

The [[Diffusion Studios core library]] is a foundational component of Reskill's first open-source video editing agent <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. This library was chosen after evaluating other alternatives like FFmpeg and Remotion, which presented limitations <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

## Key Features and Capabilities
The [[Diffusion Studios core library]] facilitates complex compositions using a JavaScript/TypeScript-based programmatic interface <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. This design allows for Large Language Models (LLMs) to generate code to run these compositions <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. The choice of code for LLM tool calling is highlighted as superior to JSON, based on multiple research papers <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

## Reasons for Adoption
Reskill developers appreciated the API of the [[Diffusion Studios core library]] because it eliminated the need for a separate rendering backend, a limitation encountered with other tools like Remotion <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

## Role in the AI Video Editing Agent
Within the agent's architecture, the [[Diffusion Studios core library]] underpins the "video editing tool" <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. This tool generates code based on user prompts and executes it within a browser session managed by Playwright, which connects to an operator UI <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. The operator UI renders video directly in the browser using the WebCodecs API <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.

## Collaboration
The development of the video editing agent and its integration with the [[Diffusion Studios core library]] is a collaboration between Diffusion Studio and Reskill <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>, <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.