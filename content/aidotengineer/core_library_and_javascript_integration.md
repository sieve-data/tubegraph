---
title: Core Library and JavaScript Integration
videoId: r0AG44qYKsI
---

From: [[aidotengineer]] <br/> 

The development of an open-source video editing [[ai_application_frameworks_and_architecture | agent]] for "reskill" led to the adoption of the `core` library due to limitations found in other tools like FFmpeg and Remotion <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. While Remotion offered unreliable server-side rendering, `core` was favored because its API did not require a separate rendering backend <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Core Library Capabilities

The `core` library, originating from Diffusion Studio, facilitates complex video compositions <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Its key feature is a [[typescript_and_effect_library_usage | JavaScript]]/[[typescript_and_effect_library_usage | TypeScript]]-based programmatic interface <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Integration with AI Agents and LLMs

The programmatic interface of `core` makes it a perfect match for [[ai_application_frameworks_and_architecture | AI agents]] that utilize Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This allows LLMs to generate code to perform actions, as code is considered the optimal way to express actions for a computer <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

Research papers have also indicated that [[ai_integration_and_tool_calling | LLM tool calling]] when expressed in code is significantly more effective than when expressed in JSON <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Architecture Flow

In the agent's architecture, a video editing tool leverages `core` by generating code based on user prompts and executing it directly in the browser <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Future Development

While the initial version of the agent is in Python, a [[typescript_and_effect_library_usage | TypeScript]] implementation is currently underway <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Collaboration

The development of this [[ai_application_frameworks_and_architecture | agent]] and its integration with the `core` library is a collaboration between Diffusion Studio, the author of the `core` library, and rskill <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.