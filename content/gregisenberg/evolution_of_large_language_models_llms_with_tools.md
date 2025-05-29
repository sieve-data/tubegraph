---
title: Evolution of large language models LLMs with tools
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The concept of Model-Centric Programming (MCPs) has gone viral, but its meaning and associated startup opportunities are often unclear [00:00:00]. Professor Ross Mike explains MCPs as a key evolution in the capabilities of large language models (LLMs) [00:01:18].

## Limitations of Standalone LLMs <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>

By themselves, LLMs are fundamentally incapable of performing meaningful actions [00:02:42]. For instance, a basic chatbot cannot send an email; it will state its inability to do so [00:02:53]. The primary function of an LLM in its standalone form is to predict the next word or phrase based on its training data [00:03:25]. For example, given "My Big Fat Greek," an LLM would predict "Wedding" [00:03:30]. This predictive capability, while impressive, limits their direct utility for specific tasks [00:03:41].

## First Evolution: LLMs + Tools <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>

The first significant evolution involved developers combining LLMs with external tools, often in the form of APIs [00:03:48]. This integration allowed LLMs to access and utilize external services [00:04:21].

*   **Examples of Tool Integration:**
    *   **Internet Search:** Chatbots like Perplexity can search the internet and present information, even though the LLM itself doesn't possess search capabilities [00:04:00].
    *   **Automation:** Connecting an LLM to automation services like Zapier or End8 enables tasks like creating a spreadsheet entry every time an email is received [00:04:52].

*   **Challenges of LLM + Tools Approach:**
    *   **Complexity:** Building an assistant capable of multiple functions (e.g., searching, reading emails, summarizing) becomes frustrating and cumbersome [00:05:09].
    *   **Integration Difficulty:** Gluing various tools to LLMs is challenging [00:05:22]. Making these tools work cohesively and stack effectively is a "nightmare" [00:05:38].
    *   **Reliability:** LLMs can "hallucinate or do something stupid" when integrated with tools [00:06:26]. Despite their cool factor, LLMs are "very very dumb" on their own [00:06:30].
    *   **Maintenance:** Updates to external APIs (e.g., Slack's API) can break existing automations and integrations, leading to significant engineering effort [00:10:18]. This difficulty explains why an "Iron Man level Jarvis assistant" is not yet widely available [00:05:30].

## Second Evolution: Model-Centric Programming (MCP) <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>

MCP is considered the next evolution in making LLMs more capable [00:14:34]. It addresses the challenges of integrating diverse tools by introducing a standardized layer.

*   **The Problem MCP Solves:** Different tools and service providers construct their APIs in varying ways, requiring different information to be passed, which makes integration feel like "gluing a bunch of different things together" [00:08:15]. This approach becomes difficult at scale [00:08:31].
*   **MCP as a Unified Layer:** MCP acts as an intermediary layer between an LLM and external services/tools [00:08:38]. This layer translates all the "different languages" of various tools into a single, unified language that the LLM can understand [00:08:45].
*   **Benefits of MCP:**
    *   Simplifies the LLM's ability to connect with and access outside resources, such as external data sources or databases (e.g., Convex, Superbase) [00:09:01].
    *   Reduces the need for manual work, step-by-step planning, and mitigates edge cases prone to failure [00:09:36].
    *   Enables LLMs to perform more complex and meaningful tasks efficiently, such as creating new database entries based on a simple command [00:09:24].
*   **MCP Ecosystem:**
    *   **MCP Client:** The LLM-facing side of the ecosystem (e.g., Tempo, Windswept, Cursor) [00:11:16].
    *   **MCP Protocol:** The two-way connection standard between the client and server [00:11:32].
    *   **MCP Server:** Translates the external service's capabilities for the client [00:11:38].
    *   **Service:** The external tool or API (e.g., database, email service) [00:11:13].
    *   **Developer Responsibility:** Anthropic, by creating the MCP standard, has placed the responsibility of constructing the MCP server on the service providers themselves [00:11:51]. This means service providers are now building MCP servers and repositories to allow LLMs to access their services [00:12:18].
*   **MCP as a Standard:** MCP is essentially a new standard that allows LLMs to communicate efficiently with services, much like REST APIs provide a standard for communication between different companies' services [00:01:52]. It allows LLMs to become more capable by adding a protocol that enables them to perform important tasks [00:13:38].

## Current Challenges with MCPs <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>

Despite its potential, MCP implementation currently faces technical challenges:

*   Setting up an MCP server can be "annoying," involving multiple file downloads and local configurations [00:13:54].
*   There are still "kinks that have to be figured out" before the standard is fully finalized or polished [00:14:08]. The space is very early, and the ultimate standard might still evolve [00:17:41].

## Startup Opportunities <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>

The emergence of protocols often leads to significant business opportunities.

*   **For Technical Individuals:**
    *   **MCP App Store:** An idea for a platform where users can browse, deploy, and install MCP servers from various repositories, receiving a URL to integrate into their MCP clients [00:16:38]. This would simplify the current cumbersome setup process [00:17:10].
*   **For Non-Technical Individuals / Business Owners:**
    *   **Observe and Learn:** It is crucial to stay updated with platforms adopting MCP capabilities and monitor the evolving standard [00:17:31].
    *   **Future Integration:** Once the standard is finalized and widely adopted by service providers, integrating different services will become much more seamless [00:17:57]. This will open doors for creating new chatbot interfaces and tools with improved user experiences, faster performance, and reduced hallucinations [00:18:12].
    *   **No Immediate "Crazy" Opportunities:** It's too early to make definitive "smart business decisions" or "fire any shots" related to MCPs, as the standard is still in its early stages and could change (e.g., Open AI introducing a different standard) [00:19:09]. The current phase is for observation and learning [00:19:11].
    *   **Lego Pieces Metaphor:** MCPs will make integration much easier, allowing developers to stack LLMs and services like "Lego pieces" to build more capable systems [00:18:46].

Understanding MCPs now provides insight into how future advancements in AI will work, enabling individuals to "hit the ground running" when the next phase of standardization occurs [00:19:33].