---
title: Microsofts development of the agentic web
videoId: jYHLKtWM164
---

From: [[everyinc]] <br/> 

Microsoft's focus has shifted from primarily emphasizing scaling laws to the "agentic web" in recent times, recognizing the need to bridge the gap between AI model capabilities and their practical application in products <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>. This evolution stems from the rapid emergence of [[development_of_autonomous_agents | AI agents]] over the past year <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

## Challenges in Agent Utility

For [[development_of_autonomous_agents | agents]] to be truly useful, several fundamental challenges must be addressed:

*   **Agentic Memory:** Current [[development_of_autonomous_agents | agents]] are often "transactional," meaning memory is coherent only within a single task and may disappear afterward <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. This limits the ability to delegate complex, multi-step tasks to them <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>.
*   **Action and Access:** [[development_of_autonomous_agents | Agents]] must be able to take action on behalf of users. This includes using tools, making changes in systems, and consulting diverse and rich information sources <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a> <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

## The Agentic Web Ecosystem

To enable [[development_of_autonomous_agents | agents]] to function effectively, an ecosystem resembling the internet is necessary <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a> <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. This requires:

*   **Standard Protocols:** Information sources and APIs must be "plumbed through" so [[development_of_autonomous_agents | agents]] can communicate with them <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a> <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
*   **Open Standards:** Simple, composable, and layered protocols are emerging, similar to how HTTP functions for the internet (e.g., MCP) and HTML for the web (e.g., NLweb) <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a> <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a> <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>. These aim for ubiquity to allow [[development_of_autonomous_agents | agents]] to perform actions across systems <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.
*   **Aligned Incentives:** Incentives must be aligned for all participants to encourage widespread adoption and participation in this new agentic web <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.

## Microsoft's Role and Motivation

Microsoft's involvement in the [[agentic web | agentic web]] is driven by a few key motivations:

*   **Internal Utility:** As a developer of [[development_of_autonomous_agents | agents]], Microsoft needs to solve these integration problems for its own products to be useful <a class="yt-timestamp" data-t="06:53:00">[06:53:00]</a>. As CTO, there's a push to make all internal Microsoft systems speak a standard protocol to internal [[development_of_autonomous_agents | agents]] <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a> <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. This avoids "Conway's Law," where organizational structure dictates system design <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.
*   **Platform Company:** Beyond its own [[development_of_autonomous_agents | agents]], Microsoft, as a 50-year-old platform company, aims to solve emerging problems in the [[agentic web | agentic web]] at the platform layer <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a> <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.
*   **Benefits for Users and Providers:** Simple protocols like MCP solve important problems for [[development_of_autonomous_agents | agent]] makers, platform builders, users who want more useful systems, and providers who want to participate in the [[agentic web | agentic web]] <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.

## Security Model for the Agentic Web

A critical aspect of the [[agentic web | agentic web]] is its security model <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>. While the simplicity of MCP makes it adaptable, key enterprise-level security features are being addressed:

*   **Agent Identities:** [[development_of_autonomous_agents | Agents]] need identities to build entitlement systems, allowing them to act on behalf of a person and be entitled to specific resources <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>.
*   **Permission Requests:** [[development_of_autonomous_agents | Agents]] should be able to query systems to understand what entitlements are needed for a task and then request permission from the user <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. Administrators also need control over what happens <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.
*   **Open and Collaborative Development:** The goal is to develop these security features in an open way, avoiding proprietary solutions <a class="yt-timestamp" data-t="11:45:00">[11:45:00]</a>.
*   **AI-Enhanced Security:** There's potential for better security by leveraging AI capabilities, where an [[development_of_autonomous_agents | agent]] could attend to personal security requirements, manage data sharing, and assess risk by triangulating information from various communication modalities <a class="yt-timestamp" data-t="14:11:00">[14:11:00]</a>.

## Open vs. Verticalized Models

Microsoft leans towards an open model for [[applying_agency_in_ai_development | AI development]], embracing "permissionless innovation" over a verticalized model (like an app store where a central authority controls distribution) <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>. The belief is that middle layers that act as gatekeepers don't always add value between the creator and the beneficiary <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.

## Impact on Software Engineering and the Craft

The nature of software [[applying_agency_in_ai_development | development]] is continually changing <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a> <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>. Makers, including software engineers, woodworkers, and potters, inherently have strong opinions about their craft, tools, and materials <a class="yt-timestamp" data-t="00:21:00">[00:21:00]</a> <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>. However, this is not the first time such changes have occurred, and individuals will retain choice in their tools and methods <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.

The advice for [[developing_apps_and_prototypes_using_ai | developers]] is to have an open mind when tools change <a class="yt-timestamp" data-t="20:10:00">[20:10:00]</a>, to "be curious, try stuff, and if it works for you, use it, and if it doesn't, don't" <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a> <a class="yt-timestamp" data-t="20:49:00">[20:49:00]</a>. Sometimes the process is valued more than the outcome, and vice-versa, leading to different tool choices <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>.

## [[the_future_of_ai_agents_and_user_interaction | The Future of AI Agents]]

It's unlikely there will be "one agent to rule them all" <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>. Instead, the future of [[applying_agency_in_ai_development | AI development]] will see a diverse ecosystem of [[development_of_autonomous_agents | agents]] <a class="yt-timestamp" data-t="21:03:00">[21:03:00]</a>. The most important differentiator for [[development_of_autonomous_agents | agents]] will be the "product making part of them" <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>, focusing on:

*   **Problem Understanding:** Successful [[development_of_autonomous_agents | agents]] will come from startups and companies with a nuanced understanding of specific user problems <a class="yt-timestamp" data-t="22:31:00">[22:31:00]</a>.
*   **Infrastructure Adaptation:** They will pick up, modify, or tune existing infrastructure to solve these problems <a class="yt-timestamp" data-t="22:39:00">[22:39:00]</a>.
*   **Diversity:** This approach will lead to a wide variety of [[development_of_autonomous_agents | agents]], each tailored to different needs <a class="yt-timestamp" data-t="22:55:00">[22:55:00]</a>.

## Predictions for the Future of AI

Looking ahead, several shifts are anticipated:

*   **Obsolescence of Excuses:** Arguments about technology being "not ready yet" due to cost or capability will become irrelevant as everything gets cheaper and more capable each year <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a> <a class="yt-timestamp" data-t="24:43:00">[24:43:00]</a>.
*   **Increased Ambition:** There will be significant progress in the level of ambition for problems tackled with [[development_of_autonomous_agents | agents]] <a class="yt-timestamp" data-t="25:40:00">[25:40:00]</a>.
*   **Shift to Asynchronous Interaction:** As the [[agentic web | agentic web]] becomes more complete and models' reasoning and planning capabilities improve, interactions with [[development_of_autonomous_agents | agents]] will shift from synchronous (immediate response) to asynchronous (delegating a task that takes time and multiple steps to complete) <a class="yt-timestamp" data-t="26:00:00">[26:00:00]</a> <a class="yt-timestamp" data-t="26:19:00">[26:19:00]</a>.