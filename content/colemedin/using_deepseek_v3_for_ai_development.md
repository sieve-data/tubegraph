---
title: Using DeepSeek V3 for AI development
videoId: zf_D2Eafvk0
---

From: [[colemedin]] <br/> 

This article details the integration and benefits of using the new DeepSeek V3 large language model (LLM) for building AI agents, particularly within the Pydantic AI framework. This is the third video in a mini-series demonstrating the full process of building AI agents, transitioning from a no-code prototype to a production-ready Python agent <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## DeepSeek V3: Power and Affordability
DeepSeek V3 is chosen for its ability to make AI agents "super powerful and still dirt cheap" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. In the previous n8n prototype, Gemini 2.0 Flash was used as the LLM, and DeepSeek V3 serves as its powerful and cost-effective replacement in the Python implementation <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Integration with Pydantic AI via OpenRouter
To utilize DeepSeek V3, the Pydantic AI framework is employed, accessing the model through OpenRouter <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The setup involves configuring an instance of Pydantic AI's OpenAI model class, but overriding its base URL and API key to point to OpenRouter's service <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. This method allows for seamless integration of DeepSeek V3 within the Pydantic AI agent.

## Flexibility in LLM Choice
A significant advantage of this setup is the flexibility it provides in choosing LLMs. While DeepSeek V3 is the primary choice for this agent, the configuration allows for easy switching to other models like Gemini, Claude, Qwen, or Mistral by simply changing an environment variable <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This ensures that developers are not "tied down to just one" LLM <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, making the agent adaptable to different needs or preferences <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

## Application in a GitHub Q&A Agent
DeepSeek V3 is demonstrated as the core LLM for a custom-coded AI agent capable of consuming entire GitHub repositories for code Q&A <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This agent can retrieve repository structures, file contents, and even metadata like repository size and number of files <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>, <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. The successful demonstration of answering questions about a specific file (e.g., `env.example` in the [[open_source_ai_agent_development | Bolt.DIY]] repo) showcases DeepSeek V3's ability to understand context and utilize tools effectively <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>.

## Future Development
The current setup with DeepSeek V3 provides a "solid foundation of an AI agent that's flexible powerful and affordable" <a class="yt-timestamp" data-t="00:28:44">[00:28:44]</a>. Future videos in the series will focus on building a front-end interface for the agent and adding more functionalities and features to prepare it for production deployment <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. The series previously covered setting up [[using_supabase_for_ai_agents | Supabase]] for message management with the n8n prototype <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.