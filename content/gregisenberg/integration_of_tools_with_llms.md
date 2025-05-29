---
title: Integration of Tools with LLMs
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The realm of Large Language Models (LLMs) has seen significant evolution, particularly in how they interact with external systems. Initially, LLMs were limited in their capabilities, prompting the development of integrations with various tools and services to expand their functionality. The introduction of standards like the Machine Code Protocol (MCP) aims to streamline and enhance these integrations.

## The Limited Capabilities of Standalone LLMs

By themselves, LLMs are fundamentally incapable of performing meaningful actions beyond predicting the next text sequence <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. For example, a basic chatbot cannot send an email; it can only tell you it cannot <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>. Their primary function is to predict the most likely next word based on their training data, such as completing "My Big Fat Greek" with "Wedding" <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. This limitation means that for practical, real-world applications, LLMs require external assistance <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.

## Evolution: LLMs Combined with Tools

The next major step in [[evolution_and_challenges_of_large_language_models_llms | LLM evolution]] involved developers figuring out how to combine LLMs with external tools, often in the form of APIs <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This integration allowed LLMs to perform more complex tasks:
*   **Internet Search:** Chatbots like Perplexity can search the internet and present information, though the LLM itself isn't performing the search; it's accessing an external service tool <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>, <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.
*   **Automation:** By connecting an LLM to [[automation_tools_and_techniques | automation services]] like Zapier or End8, it could potentially automate actions, such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>, <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>, <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. This makes the LLM more meaningful <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

## Challenges of Current Tool Integration

While combining LLMs with tools enhanced their capabilities, it introduced significant challenges, particularly when attempting to build sophisticated assistants capable of multiple tasks (e.g., searching, reading emails, summarizing) <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>, <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
*   **Cumbersome Integration:** Gluing multiple tools to LLMs becomes frustrating and cumbersome <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>, <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Lack of Standardization:** Although there are API standards (like REST APIs), each service provider constructs their APIs differently, requiring varied information and setups <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>, <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. This is akin to each tool speaking a different language (e.g., English, Spanish, Japanese) <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Maintenance Nightmare:** Updates to a service's API can break existing integrations, leading to significant engineering effort and troubleshooting <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>, <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>, <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.
*   **Manual Work and Edge Cases:** The current process involves substantial manual work, step-by-step planning, and is prone to edge cases where the system can fail <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>, <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
*   **Hallucination Risk:** LLMs, despite their cool factor, are inherently "dumb" and can hallucinate or do "something stupid" if not carefully managed with tools <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>, <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>.

## The Role of Machine Code Protocol (MCP)

MCP emerges as a potential solution to these integration complexities. It acts as a standardized layer between the LLM and the services/tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>.
*   **Unified Language:** MCP translates all the different "languages" of various tools into a single, unified language that the LLM can perfectly understand <a class="yt-timestamp" data-t="08:43:00">[08:43:00]</a>, <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.
*   **Simplified Access:** This standardization makes it much simpler for the LLM to connect to and access various outside resources and databases (e.g., Convex, Superbase) <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>, <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>, <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.
*   **Ecosystem Components:** The MCP ecosystem comprises:
    *   **MCP Client:** The LLM-facing side (e.g., Tempo, Windsurf, Cursor) <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>, <a class="yt-timestamp" data-t="11:24:00">[11:24:00]</a>.
    *   **MCP Protocol:** The two-way connection between the client and server <a class="yt-timestamp" data-t="11:32:00">[11:32:00]</a>.
    *   **MCP Server:** Translates the external service's capabilities for the client <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>.
    *   **Service:** The external tool or API <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **Service Provider Responsibility:** Anthropic, the apparent creator of this architecture, has shifted the responsibility of constructing the MCP server to the service providers themselves <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>, <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>, <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. This means external service providers are now building out their own MCP servers and repositories <a class="yt-timestamp" data-t="12:36:00">[12:36:00]</a>.

## Benefits and Future Outlook

MCP's core contribution is the establishment of a standard for LLM-tool communication <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. This standardization is crucial for [[enhancing_llm_performance | enhancing LLM performance]] and capability, allowing them to perform "important stuff" <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>, <a class="yt-timestamp" data-t="13:44:00">[13:44:00]</a>.

While MCP promises a more cohesive and less frustrating integration experience <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>, it faces initial technical challenges, such as cumbersome local setup processes <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>. However, once these kinks are resolved and the standard is polished or universally adopted, LLMs will become even more capable <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>, <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.

### Startup Opportunities
Historically, popularized protocols like HTTPS and SMTP have led to the creation of significant businesses <a class="yt-timestamp" data-t="15:54:00">[15:54:00]</a>. MCP presents similar opportunities, especially for technical individuals:
*   **MCP App Store:** An "App Store" for MCP servers, allowing users to browse repositories of MCP servers, view GitHub code, and deploy them to receive a URL for easy integration with MCP clients <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>, <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.

For non-technical individuals and entrepreneurs, the advice is to closely observe the evolving standard <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>. When the standard is finalized and widely adopted by service providers, the ability to seamlessly integrate different "Lego pieces" of functionality will create significant opportunities for new chatbot interfaces and applications that offer flawless user experiences with limited hallucinations <a class="yt-timestamp" data-t="18:07:00">[18:07:00]</a>, <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>, <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>. It's an early stage, so vigilance and understanding the underlying mechanics are key to striking when the timing is right <a class="yt-timestamp" data-t="19:28:00">[19:28:00]</a>, <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.