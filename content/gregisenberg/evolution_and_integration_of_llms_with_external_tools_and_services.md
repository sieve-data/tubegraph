---
title: Evolution and integration of LLMs with external tools and services
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The development of Large Language Models (LLMs) has progressed through distinct phases, moving from standalone capabilities to complex integrations with external tools and services, aiming to enhance their utility and real-world applicability <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

## Initial Capabilities and Limitations of LLMs

Initially, LLMs were limited in their direct capabilities, primarily excelling at [[limitations_and_enhancements_of_large_language_models_LLMs | predicting the next text]] <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. For example, an LLM trained on sufficient data would predict "Wedding" after "My Big Fat Greek" <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

They could answer questions or describe historical figures, but they were "incapable of doing anything meaningful" like sending an email or performing specific tasks on behalf of a user <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Asking an LLM to send an email would result in it stating it couldn't <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## First Evolution: LLMs + Tools

The next significant evolution involved developers integrating LLMs with external "tools," which are typically APIs or other external services <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This allowed LLMs to perform actions beyond text generation:
*   **Internet Search**: Chatbots like Perplexity gained the ability to search the internet and present information to users, even though the LLM itself isn't capable of performing the search <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   **Automation**: By connecting an LLM to automation services like Zapier or End8, it could perform tasks such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

### Challenges of the LLM + Tools Approach
While connecting tools made LLMs more powerful, it presented significant challenges, hindering the development of advanced assistants like "Iron Man's Jarvis" <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>:
*   **Cumbersome Integration**: Building an assistant that performs multiple functions (e.g., searching the internet, reading emails, summarizing) requires "gluing a bunch of different tools" to LLMs, which is frustrating and cumbersome <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
*   **Lack of Cohesion**: Stacking these tools and ensuring they work cohesively together is a "nightmare" <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.
*   **Difficulty and Hallucinations**: Connecting external services to LLMs is difficult, and developers must ensure the LLM doesn't "hallucinate or do something stupid," as LLMs can be "very very dumb" by themselves <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.
*   **Maintenance Issues**: Updates to a service's API (e.g., Slack's API) can break complex, step-by-step automations, leading to significant engineering effort to fix <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.

## Second Evolution: Introducing MCP (Machine Cognition Protocol)

The Machine Cognition Protocol (MCP) emerged as the "next Evolution" to address the complexities of integrating LLMs with diverse tools <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>. MCP is essentially a standard, similar to REST APIs, that facilitates seamless communication between LLMs and external services <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>, <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.

### How MCP Works
MCP acts as a "layer" between the LLM and various services and tools <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. This layer "translates all those different languages into a unified language that makes complete sense to the LLM" <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.
*   **Unified Communication**: Instead of LLMs needing to understand each tool's unique API structure (like different languages), MCP provides a standardized way for the LLM to access outside resources <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>, <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Reduced Manual Work**: MCP significantly reduces the "manual work" and "step-by-step planning" previously required to integrate LLMs with tools, minimizing the number of failure-prone "edge cases" <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

### The MCP Ecosystem
The MCP ecosystem comprises four key components <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>:
1.  **MCP Client**: The client-facing or LLM-facing side of the ecosystem. Examples include Tempo, Windsurf, and Cursor <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
2.  **MCP Protocol**: The two-way connection standard between the client and the server <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
3.  **MCP Server**: This component translates the capabilities of an external service to the client <a class="yt-timestamp" data-t="11:34:00">[11:34:00]</a>. Crucially, the **service provider** is responsible for constructing this MCP server, enabling LLMs to access their service (e.g., a database company building an MCP server for their database) <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. Anthropic is noted for architecting MCP in a way that shifts this responsibility to service providers <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
4.  **Service**: The external tool or data source that the LLM interacts with via the MCP <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

### Current Status and Future Implications
While MCP is a significant step towards making LLMs more capable and is exciting, it's not without challenges in its early stages <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>. Setting up an MCP server can still be "annoying," involving manual file movements and local configurations <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

Despite these "kinks," MCP represents a future where LLMs become much more capable by providing a standardized, efficient way to integrate with various services <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>. This standardized approach allows developers to integrate LLMs into diverse applications more easily, treating them like "Lego pieces" that can be stacked to build complex functionalities <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.

For business owners and startup founders, it's recommended to stay informed about platforms building MCP capability and observe how the standard evolves and finalizes <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>. While "crazy business opportunities" for non-technical persons aren't immediately apparent, understanding this evolution will be key to capitalizing on future developments once the standard is established <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>.

<div class="callout is-info">
    <div class="callout-title">
        <div class="callout-icon">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
        </div>
        <div class="callout-title-inner">Startup Idea: MCP App Store</div>
    </div>
    <div class="callout-content">
        <p>A potential startup idea is an "MCP App Store" where users could browse, install, and deploy MCP servers from various repositories (e.g., GitHub). This platform would provide a specific URL for the deployed server, which could then be pasted into an MCP client, simplifying the integration process for developers <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.</p>
    </div>
</div>