---
title: Dynamic system prompts and dependencies in pantic AI
videoId: U6LbW2IFUQw
---

From: [[colemedin]] <br/> 

When [[building_ai_agents_with_pantic_ai_and_mcp | building AI agents]], the [[pantic_ai_framework | Pantic AI framework]] offers robust features for managing agent behavior and capabilities through dependencies and dynamic system prompts <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Dependencies in Pantic AI

Dependencies are essential elements that an [[pantic_ai_framework | Pantic AI]] agent requires to perform its tasks <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. These can include:
*   API keys <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
*   Database connections <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>

For example, in the Archon project, dependencies for an agent might include a Supabase client for Retrieval-Augmented Generation (RAG) and an OpenAI client for creating embeddings for RAG <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

### Defining Dependencies
Dependencies are set up before the agent's core definition <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>. For instance, in an Archon v1 agent, the dependencies are an OpenAI client (for RAG embeddings) and a Supabase client (for RAG) <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.

## Dynamic System Prompts

A key feature in [[pantic_ai_features_and_implementation | Pantic AI]] is the ability to dynamically inject content into an agent's system prompt <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>. The system prompt defines the agent's behavior and general rules <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>.

### How Dynamic System Prompts Work
1.  **Referencing the agent**: In [[pantic_ai_framework | Pantic AI]], content can be dynamically added to a system prompt by referencing the agent using `@` followed by the agent's name and `.system_prompt`, e.g., `@PanticAICoder.system_prompt` <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>.
2.  **Context Injection**: Similar to tools, [[pantic_ai_framework | Pantic AI]] automatically passes a `context` parameter to dynamic system prompt functions <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>. This context can be used to reference outputs from other parts of the workflow <a class="yt-timestamp" data-t="00:33:54">[00:33:54]</a>.
3.  **Content Addition**: Whatever is returned by the dynamic system prompt function is added to the agent's primary system prompt <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

For example, in Archon v2, a third dependency was added to the main coder agent to inject the scope document created by the Reasoner agent dynamically into the coder agent's system prompt <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>. This ensures that the agent's core behavior is informed by the overarching scope, rather than just conversation history <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

**Note**: For more detailed information, users can consult the [[pantic_ai_framework | Pantic AI]] documentation on dynamic system prompts <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.