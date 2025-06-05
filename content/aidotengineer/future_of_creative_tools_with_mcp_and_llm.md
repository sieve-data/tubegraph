---
title: Future of creative tools with MCP and LLM
videoId: nnktgWtfJHE
---

From: [[aidotengineer]] <br/> 

The [[integrating_ai_with_applications_using_model_context_protocol_mcp | Model Context Protocol (MCP)]] and Large Language Models (LLMs) are profoundly changing how creators interact with complex software, fundamentally lowering the barrier to entry for creative tools and enabling new workflows <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. This shift is explored through the development and impact of [[blender_mcp_and_its_development | Blender MCP]] and its potential for orchestrating multiple applications.

## Revolutionizing 3D Design: The [[blender_mcp_and_its_development | Blender MCP]]

[[blender_mcp_and_its_development | Blender]], a generalist 3D tool for importing, animating, and exporting assets for game engines and art creation, has a notoriously complex user interface with numerous tabs and options <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Tasks like building a simple donut, a classic beginner's course, traditionally take around five hours <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

The motivation behind [[blender_mcp_and_its_development | Blender MCP]] was to make [[blender_mcp_and_its_development | Blender]] easier to use by allowing LLMs like Claude or ChatGPT to control it <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. The goal is to enable users to generate 3D scenes simply by providing prompts <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. For instance, a prompt like "make a dragon, have it guard a pot of gold" can generate an isometric room with a dragon and a pot of gold in about five minutes <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>.

### [[technical_structure_and_features_of_mcp | Technical Structure of [[blender_mcp_and_its_development | Blender MCP]]]]

The [[blender_mcp_and_its_development | Blender MCP]]'s operation is relatively straightforward <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>:
*   **Client Connection:** An LLM client (e.g., Claude, Cursor) connects to [[blender_mcp_and_its_development | Blender]] via the [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCP]] protocol <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   **Tool Discovery:** The [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCP]] allows [[blender_mcp_and_its_development | Blender]] to expose its capabilities (tools) to the client <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   **Script Execution:** A custom add-on in [[blender_mcp_and_its_development | Blender]] executes the scripts dictated by the LLM <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>. For example, if Claude is told to "make a dragon," it calls the correct [[blender_mcp_and_its_development | Blender]] tools <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
*   **Asset Integration:** Industry-standard asset platforms like Rodin (AI-generated assets), Sketchfab, and Polyhaven are connected to the LLM, allowing seamless generation and import of assets based on prompts <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Blender's Role:** [[blender_mcp_and_its_development | Blender]]'s scripting capabilities and flexibility in downloading and importing assets are crucial to this integration <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. The LLM client handles the heavy lifting of orchestration <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

### Learnings from [[blender_mcp_and_its_development | Blender MCP]] Development

Key insights gained during the development of [[blender_mcp_and_its_development | Blender MCP]] include <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>:
*   **Leveraging Scripting:** Tools with scripting capabilities significantly reduce development effort, as LLMs excel at writing and executing code for tasks like modeling or asset retrieval <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.
*   **Tool Clarity for LLMs:** LLMs can become confused with too many tools. It's crucial to keep the toolset lean and ensure each tool is distinct to prevent non-deterministic behavior <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>.
*   **Focused UX:** Avoid bloating the user experience with unnecessary features. The effectiveness of [[blender_mcp_and_its_development | Blender MCP]] comes from its lean, generalist approach <a class="yt-timestamp" data-t="06:58:00">[06:58:00]</a>.
*   **Improving Models:** Underlying LLMs are rapidly improving their understanding of 3D. The release of models like Gemini 2.5 has already made a significant impact on performance <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## Impact on Creative Workflows and Accessibility

[[integrating_ai_with_applications_using_model_context_protocol_mcp | MCPs]] and LLMs are democratizing 3D design and other creative fields by lowering access barriers <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

Examples of unlocked capabilities:
*   **Rapid Scene Creation:** Users can create complex scenes in minutes, using AI-generated assets that don't exist otherwise <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **Animated Content:** Creating animated scenes with AI-generated assets, like an animated cat, can now be done in under an hour, a significant reduction from previous times <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
*   **Reference Image Recreation:** LLMs can recreate scenes, such as a living room, from reference images, automatically obtaining and placing the correct assets <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Advanced Terrain Generation:** Users can generate detailed terrain from images and automatically set up complex textures and normal maps using [[blender_mcp_and_its_development | Blender]]'s node system, all through prompting <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
*   **Game Development:** [[blender_mcp_and_its_development | Blender MCP]] can be used to set scenes and create assets for full games, drastically speeding up development <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
*   **Filmmaking and Animation:** The MCP can generate racing tracks, animate cars, and set camera angles to create cinematic clips, which can then be further processed by tools like Runway to produce actual video <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.
*   **Instant Creation:** A task like creating a donut, previously taking five hours, can now be accomplished in approximately one minute with a simple prompt <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

This increased accessibility means that users can simply write down their vision and achieve it with prompting, rather than needing to master complex user interfaces <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.

## The Orchestrator Client: A Vision for [[future_developments_and_roadmap_for_mcp | Multi-Tool Integration]]

The concept of the client as an "orchestrator" is central to the [[integration_of_llm_with_creative_tools | integration of LLM with creative tools]] <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. This means a single LLM interface can connect to external APIs and local tools, extending the analogy to complex multi-application workflows <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.

For example, a user wanting to "make a game" doesn't necessarily want to learn Unity or Ableton <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a>. Their intent is to create. [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCPs]] serve as a "fundamental glue" that enables LLMs to capture this intent and orchestrate various tools to realize the user's vision <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>.

In this scenario, an LLM could:
1.  Call [[blender_mcp_and_its_development | Blender]] to create game assets <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.
2.  Call Unity (a game engine) to assemble the game, add collisions, and logic <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.
3.  Call relevant APIs to get and animate assets <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.
4.  Call Ableton (music creation software) to generate soundtracks for characters or the game <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>.

This orchestration means users no longer need to worry about the underlying tools, as the client chooses the right ones to make the game <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.

```ad-example
**Combined Blender and Ableton Demo**
A demonstration shows an LLM creating a dragon character with sinister lighting in [[blender_mcp_and_its_development | Blender]], while simultaneously calling the Ableton [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCP]] to generate a corresponding soundtrack <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>. While the quality may not be perfect yet, it highlights the potential for stitching together complex creative pieces <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>.
```

## Implications for Creators

The emergence of [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCPs]] and LLMs raises fundamental questions about the future of creative work <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>:
*   Will tools primarily talk to each other, with users interfacing solely through LLMs, bypassing complex UIs <a class="yt-timestamp" data-t="15:22:00">[15:22:00]</a>?
*   Will creators become more like "orchestra conductors," where understanding how to convey their vision to an LLM for execution and coordinating different creative components is more important than mastering individual tools <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>?

This is an exciting time for creators, with [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCPs]] at the center <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>. Beyond [[blender_mcp_and_its_development | Blender]] and Ableton, [[integrating_ai_with_applications_using_model_context_protocol_mcp | MCPs]] are emerging for other creative tools like PostGIS, Houdini, Unity, and Unreal Engine <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. This broad adoption suggests that soon, everyone may be able to become a creator <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.