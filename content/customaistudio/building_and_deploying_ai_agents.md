---
title: Building and deploying AI agents
videoId: oF-xOgTxmzI
---

From: [[customaistudio]] <br/> 

This article provides a bird's-eye view of the AI agent space, discussing current trends, proposed architectures, and practical steps for development and deployment that prioritize long-term scalability. <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>

## The Current AI Agent Landscape

The market has seen an explosion of companies [[developing_AI_agents_and_their_market_potential | building AI agents]] that can be purchased off the shelf or quickly created. <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>

### Off-the-Shelf AI Agents
Numerous options are available for immediate use:
*   **HubSpot AI Agents**: Designed to power up productivity. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Lindy**: Focuses on building AI automations rapidly. <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>
*   **CRA**: Personifies AI agents as "AI employees" or "digital assistants" (e.g., Cassie, SEO me, Buddy). <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   **Lena**: An autonomous agent for IT, HR, and Finance tickets. <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>
*   **Vapi**: Allows for creating and managing GPT agents that users can interact with via calls. <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>
*   **Salesforce Einstein SDR and Sales Coach**: Integrated directly into the platform. <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Beam**: Offers customer service agents. <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

This abundance of options suggests that businesses can either integrate agents into their existing platforms or buy ready-made solutions. <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>

### Platforms for Building AI Agents
Beyond ready-made agents, several platforms enable users to [[tools_and_resources_for_building_ai_agents | build their own AI agents]] from scratch:
*   **Flowise**: Allows users to build agents and tools, similar to [[building_AI_agents_with_n8n | n8n]]. <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
*   **Stack AI**: Particularly strong for enterprise solutions, especially concerning data handling. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   **Open-source platforms**: Include Agent GPT, Autogen, and Crew AI, with Crew AI being less code-heavy. <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
*   **Relevance AI**: A popular platform where people build entire businesses on top of it, offering services to build and implement AI agents. <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>
*   **Mind Studio**: More focused on AI automations, enabling users to create forms where an agent takes actions on the backend. <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>

This explosion in startups and platforms has made the barrier to entry for building agents relatively low, as it doesn't always require learning a programming language. <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>

## The Short Game vs. The Long Game

Currently, many are playing the "short game," which involves creating immediate value by deploying off-the-shelf agents for specific tasks like customer service or reception. <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a> While this approach provides immediate benefits, the speaker argues that the "long game" offers significantly more value. <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>

The long game focuses on a complete operating system shift at the business operations level, building from the ground up. <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>

## Proposed AI Agent Architecture

Traditional SaaS is built for human interaction, primarily by lower-level employees using graphical interfaces to save or extract data and execute actions. <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a> The current focus is on replacing these human interactions with agents. <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a> However, a ground-up approach is necessary for true transformation. <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>

The proposed architecture for the "long game" involves:

1.  **Master Contextual Database**: All business data (from Gmail, calendar, CRM, ATS, etc.) is fed into and embedded in a vector database. <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a> This centralizes context, which is often fragmented in current agent implementations. <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>
2.  **Foundation Agents**: These agents sit on top of the master database, manipulating data and taking actions. They replace the role of traditional SaaS applications. <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>
3.  **Workflow Specific Agents**: These agents use the foundational agents to execute custom, business-specific workflows, such as SDR agents or customer support agents. <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a> These are the types of off-the-shelf agents commonly seen today. <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>
4.  **Higher-Level Agents**: As models improve in reasoning and long-term planning, management agents, Chief of Staff agents, and custom executive agents will emerge. <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>

### The Future of SaaS
This architectural shift implies that traditional SaaS, built for human interaction, may eventually become obsolete. <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a> If agents handle primary interactions, the need for graphical interfaces designed for humans diminishes. <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a> Foundation agents are predicted to replace SaaS, fundamentally changing how businesses operate. <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>

The industry might move towards:
*   **In-house Agent Teams**: A complete internal team of agents handling all business operations and tech stack interactions. <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>
*   **Hybrid Models**: A smaller internal team of agents interacting with gated, domain-specific teams of agents from external platforms (e.g., your agents interacting with Instantly's cold email agents). <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a> In this scenario, you'd still pay for access to their systems, but your agents would interface with theirs instead of humans manually logging in. <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>

The true value in this future lies not in the technology itself (as agents will handle tools and platforms) but in the **workflows, strategies, IP, patents, and copyrights**. <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a> For example, consulting firms like Deloitte or McKinsey could package their best practices and workflows as digital products that businesses can download and embed into their agent systems. <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>

## Practical Steps to Get Started

To begin building a scalable AI agent system:

1.  **Start Building Your Master Contextual Database**:
    *   Centralize all company data into a vector database (e.g., Pinecone, Quadrant). <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>
    *   Extract data from all current platforms and add it to this database. <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>
    *   Set up real-time data capture for every new data point created across your tech stack (e.g., emails sent, calendar events, new projects, support tickets) and feed them into the master database. <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>

2.  **Build Your Foundation Agents**:
    *   These agents will sit on top of your existing tech stack. <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>
    *   Review your tech stack and identify all available API endpoints. <a class="yt-timestamp" data-t="00:20:15">[00:20:15]</a>
    *   List all required and optional input data for each endpoint (e.g., for sending an email: recipient, name, subject, message, CC, BCC, sender name, attachment). <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>
    *   Build tools for each endpoint (e.g., "send a message" tool, "create calendar event" tool, "create engagement in HubSpot" tool). <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>
    *   Attach these tools to an agent and write a general prompt (e.g., "You are the Trello agent; you can take any action on Trello; here are all the endpoints"). Define the input schema for each tool. <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>

3.  **Build Custom Agents**:
    *   This is the stage where many currently start by seeking off-the-shelf solutions like customer support or SDR agents. <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a> However, building the foundation first is crucial for scalability. <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>
    *   Create agents specific to your custom workflows (e.g., a recruiting coordinator agent). <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>
    *   Equip these custom agents with the foundational agents as their tools. <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>
    *   For example, a recruiting coordinator agent would be given an email agent, an ATS agent, and a calendar agent as tools. This allows it to email candidates, find meeting times, and log actions in the ATS. <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>

This bottom-up approach to [[understanding_and_implementing_AI_agents_in_businesses | understanding and implementing AI agents in businesses]] enables building a system that is scalable over time, resilient to the evolving AI space, and fundamentally shifts how businesses operate. <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a> It moves beyond merely making human interaction with computers more efficient, towards an agent-first paradigm. <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>