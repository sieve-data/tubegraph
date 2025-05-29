---
title: MCPs and their Role in Making LLMs More Capable
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

[[understanding_mcps_and_their_importance | MCPs]] (Multi-Capability Protocols) are a rapidly viral concept that is seen as the next evolution in making [[enhancing_ai_output_with_multiple_llms | LLMs]] more capable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains this technical concept in an easily understandable way, highlighting its importance and associated [[startup_opportunities_around_mcps | startup opportunities]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## The Foundation: Standards in Programming

In programming, standards are crucial because they enable engineers to build systems that can communicate with each other <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. A well-known example is REST APIs, which provide a standard framework for how companies construct their APIs and services, allowing engineers to connect with them easily <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. [[understanding_mcps_and_their_importance | MCPs]] introduce a similar standard for [[enhancing_ai_output_with_multiple_llms | LLMs]] <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Limitations of Standalone LLMs

[[enhancing_ai_output_with_multiple_llms | LLMs]] by themselves are currently incapable of performing meaningful actions beyond predicting the next word or answering questions <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For instance, an [[enhancing_ai_output_with_multiple_llms | LLM]] cannot send an email or perform specific tasks on its own; it can only predict text based on its training data <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This means a standalone [[enhancing_ai_output_with_multiple_llms | LLM]] can complete "My Big Fat Greek" with "Wedding," but nothing more <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## The First Evolution: LLMs Combined with Tools

Developers found a way to enhance [[enhancing_ai_output_with_multiple_llms | LLM]] capabilities by combining them with external tools, such as APIs <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
Examples include:
*   **Internet Search:** Chatbots like Perplexity can search the internet by accessing an external service, not because the [[enhancing_ai_output_with_multiple_llms | LLM]] itself has that capability <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Workflow Automation:** Integrating an [[enhancing_ai_output_with_multiple_llms | LLM]] with services like Zapier or N8 allows it to automate tasks, such as adding an email entry to a spreadsheet <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

While this approach makes [[enhancing_ai_output_with_multiple_llms | LLMs]] more powerful, it becomes cumbersome and frustrating when building assistants that need to perform multiple complex tasks simultaneously <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Stacking and making various tools work cohesively with [[enhancing_ai_output_with_multiple_llms | LLMs]] is a significant challenge, which is why a "Jarvis-level" AI assistant is not yet a reality <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Each service provider often constructs their APIs differently, making it feel like "gluing a bunch of different things together" <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Furthermore, updates to external APIs can break existing integrations, requiring significant engineering effort <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## The Next Evolution: MCPs as a Unifying Layer

[[understanding_mcps_and_their_importance | MCPs]] serve as a translation layer between an [[enhancing_ai_output_with_multiple_llms | LLM]] and various external services or tools <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. They unify the communication by translating all different tool languages into a single, unified language that the [[enhancing_ai_output_with_multiple_llms | LLM]] can understand <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This simplifies the process of connecting [[enhancing_ai_output_with_multiple_llms | LLMs]] to outside resources like databases or other tools <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### The MCP Ecosystem

The [[understanding_mcps_and_their_importance | MCP]] ecosystem consists of four main components <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>:
1.  **MCP Client:** The [[enhancing_ai_output_with_multiple_llms | LLM]]-facing side, examples include Tempo, Windswept, and Cursor <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **MCP Protocol:** The two-way connection between the client and the server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
3.  **MCP Server:** This component translates the capabilities of an external service to the [[understanding_mcps_and_their_importance | MCP]] client <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. Crucially, the responsibility of constructing the [[understanding_mcps_and_their_importance | MCP]] server lies with the service provider <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
4.  **Service:** The external tool or data source that the [[enhancing_ai_output_with_multiple_llms | LLM]] needs to interact with <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

By creating this standard, companies like Anthropic have shifted the burden of integration to service providers, leading to a future where [[enhancing_ai_output_with_multiple_llms | LLMs]] will become significantly more capable <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

## [[the_challenges_of_implementing_mcp_servers | Challenges and Future Outlook]]

Despite the promise, setting up an [[understanding_mcps_and_their_importance | MCP]] server on clients currently presents technical challenges, often involving manual downloading and configuration <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. These "kinks" need to be resolved for the full potential of [[understanding_mcps_and_their_importance | MCPs]] to be realized <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

Once the standard for [[understanding_mcps_and_their_importance | MCPs]] is finalized and polished, [[automating_workflows_with_ai_tools_like_mcp_nadn_and_claude | AI tools]] will become much more capable and easier to integrate <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

### [[startup_opportunities_around_mcps | Startup Opportunities]]

While it's too early for definitive business decisions, Professor Ross Mike suggests a potential [[startup_opportunities_around_mcps | startup opportunity]] for technical individuals: an "[[understanding_mcps_and_their_importance | MCP]] App Store" <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This platform would allow users to browse and deploy [[understanding_mcps_and_their_importance | MCP]] servers from various GitHub repositories with a single click, providing a URL to paste into an [[understanding_mcps_and_their_importance | MCP]] client <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

For non-technical individuals, the advice is to stay updated on platforms building out [[understanding_mcps_and_their_importance | MCP]] capability and observe how the standards evolve <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. Understanding this framework now will prepare individuals to act swiftly when the standard is finalized and integration becomes seamless, akin to "Lego pieces that you can continue to stack" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>.