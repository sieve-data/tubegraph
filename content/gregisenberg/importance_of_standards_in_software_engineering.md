---
title: Importance of standards in software engineering
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Standards are crucial in programming because they enable engineers to build systems that can communicate with each other effectively <a class="yt-timestamp" data-t="01:54:02">[01:54:02]</a>. They provide a common formality that makes development and integration easier <a class="yt-timestamp" data-t="02:29:13">[02:29:13]</a>.

## Standards in General Programming

A widely known standard in software engineering is [[rest_apis | REST APIs]], which companies follow when constructing their APIs and services to allow engineers to connect with them <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Without standards, connecting different services would be like trying to communicate in many different languages, making it difficult to scale and grow <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.

## Limitations of Large Language Models (LLMs) Without Unified Standards

Initially, Large Language Models (LLMs) like ChatGPT 3 or 3.5 were limited in their capabilities <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. By themselves, LLMs are largely incapable of performing meaningful actions, such as sending an email or performing specific tasks on behalf of a user <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Their primary function is to predict the next text in a sequence <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

The next evolution involved connecting LLMs with external "tools" or APIs <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. For example, LLMs could search the internet (like Perplexity) by accessing external services <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. This allowed for more complex actions, such as automating tasks like creating a spreadsheet entry every time an email is received, using services like Zapier or End8 <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.

However, this approach presented significant [[challenges_and_expectations_with_ai_design_tools | challenges]]:
*   **Cumbersome Integration:** Connecting multiple tools to an LLM can be very frustrating and cumbersome <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Lack of Cohesion:** Stacking tools on top of each other and making them work cohesively is a "nightmare" <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>. This complexity is why a "Jarvis-level" assistant is not yet a reality <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **Manual Work and Edge Cases:** Connecting tools manually involves a lot of step-by-step planning and is prone to failures and "edge cases" <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.
*   **API Updates:** If an external service's API (like Slack) updates, it can break existing connections and automation, becoming a "nightmare" for engineers <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

## MCP: A New Standard for LLM-Tool Communication

The concept of a "Multi-tool Conversation Protocol" (MCP) emerged to address these issues. MCP acts as a standardized layer between an LLM and external services/tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. It translates the different "languages" or API structures of various tools into a unified language that the LLM can understand <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. This represents an evolution beyond simply connecting LLMs with tools, making the process much simpler and more efficient <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>.

The MCP ecosystem comprises:
*   **MCP Client:** The LLM-facing side, such as Tempo, Wind, or Cursor <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **MCP Protocol:** The two-way connection standard between the client and server <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
*   **MCP Server:** Translates the external service's capabilities to the client <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>.
*   **Service:** The external tool or API (e.g., a database like Convex or Superbase) <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

Notably, the responsibility for constructing the MCP server now falls on the service providers themselves <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. This means external service providers are actively building out different MCP servers and repositories <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.

## Benefits and Future Outlook

MCP unifies LLMs and services, creating an efficient communication layer <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>. It makes LLMs more capable of performing important tasks <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a> and enables more seamless [[integrating_ai_tools_in_product_development | integration]] <a class="yt-timestamp" data-t="18:40:00">[18:40:00]</a>. It allows developers to stack "Lego pieces" of functionality easily <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.

While still in early stages with some setup challenges, such as local file handling <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>, MCP signifies a move towards a world where LLMs become significantly more capable <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.

## Opportunities and Advice

The establishment of popular protocols like HTTPS or SMTP has historically led to the creation of many large businesses <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. Similarly, standards like MCP open new opportunities.

For technical individuals, an idea floated is an "MCP App Store," where users could browse, install, and deploy MCP servers from various repositories to get a URL for integration with MCP clients <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.

For non-technical individuals who are [[validating_a_startup_idea_before_building | building out their startup ideas]], the advice is to stay updated with platforms adopting MCP capabilities and observe how the standards evolve <a class="yt-timestamp" data-t="17:28:00">[17:28:00]</a>. It is crucial to pay close attention to when a standard is finalized because that is when service providers will build out their MCP integrations, making it much easier to connect and develop applications <a class="yt-timestamp" data-t="17:59:00">[17:59:00]</a>. While it's too early for concrete business decisions based solely on MCP, understanding its workings means being prepared to act when the right time comes <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>.