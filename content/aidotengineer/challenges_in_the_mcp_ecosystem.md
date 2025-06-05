---
title: Challenges in the MCP ecosystem
videoId: tOou_GJ9Ddk
---

From: [[aidotengineer]] <br/> 

The [[Model context protocol MCP | Model Context Protocol]] (MCP) is a relatively new space <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This article provides a high-level overview and addresses the various [[Problems faced by MCP developers | problems]] within the [[Model context protocol MCP | MCP]] space and ecosystem <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. Henry, the founder and CEO of [[smitherys_role_in_solving_mcp_challenges | Smithery]] and a member of the [[Model context protocol MCP | MCP]] committee, shares insights into these challenges <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Genesis of [[Model context protocol MCP | MCP]]

The need for [[Model context protocol MCP | MCP]] emerged from a realization regarding the capabilities of Large Language Models (LLMs). While LLMs, such as OpenAI's 03 (which achieved human-level performance on challenges like ARC AGI) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>, demonstrated significant intelligence, this intelligence often remained "stuck in a box," a phenomenon referred to as "Claude's paradox" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. To make AI agents practically useful, there was a need to consider their context and capability, specifically their inputs and outputs <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

Recognizing this problem, Anthropic released the [[Model context protocol MCP | Model Context Protocol]] in November 2024 <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This open standard aims to help LLMs connect to different services, standardizing the complex problem of connecting models to external functionalities <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. The advent of [[Model context protocol MCP | MCP]] and a new ecosystem of services targeting AI agents, while promising, also introduced a new set of [[Problems faced by MCP developers | problems]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

## User Problems in the [[Model context protocol MCP | MCP]] Ecosystem

Users of [[Model context protocol MCP | MCP]]s face several significant challenges:

*   **[[Fragmentation and installation issues of MCPs | Fragmentation]]**: With an increasing number of [[Model context protocol MCP | MCP]] servers being deployed daily, it is becoming difficult to find high-quality ones <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The [[Standardization and Adoption of mCP | MCP]] committee is working on an official registry <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>, but assigning reputation to high-quality [[Model context protocol MCP | MCP]]s remains an open question <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **[[Fragmentation and installation issues of MCPs | High Friction Installation]]**: Installing an [[Model context protocol MCP | MCP]] typically involves a complex five-step process found in their GitHub repositories, making it very difficult <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Furthermore, there's a risk of installing an insecure [[Model context protocol MCP | MCP]] <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **AI Native Services Economy**: The creation of a new economy for AI native services faces challenges, particularly regarding agentic payments <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Questions include how agents will pay on behalf of users and how to prevent users from subscribing to numerous services each charging recurring fees <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## [[Problems faced by MCP developers | Developer Problems]] in the [[Model context protocol MCP | MCP]] Ecosystem

[[Problems faced by MCP developers | Developers]] building [[Model context protocol MCP | MCP]]s also encounter a distinct set of challenges:

*   **Hosting**: Although Streambo HTTP transport has made hosting easier <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, [[Problems faced by MCP developers | developers]] still contend with issues like stable sessions and resumability <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Developer Tooling**: The [[Model context protocol MCP | MCP]] space currently lacks robust developer tooling, with only a basic [[Model context protocol MCP | MCP]] inspector available from the official [[Model context protocol MCP | MCP]] repository <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Open questions for [[Problems faced by MCP developers | developers]] include how to design the best [[Model context protocol MCP | MCP]]s, ensure their tools are called, and create optimal agent experiences <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Distribution**: [[Problems faced by MCP developers | Developers]] face the challenge of getting their created [[Model context protocol MCP | MCP]]s discovered <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Observability**: Once an [[Model context protocol MCP | MCP]] is deployed and in use, [[Problems faced by MCP developers | developers]] need ways to monitor and improve it <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Monetization**: A key challenge is determining how [[Problems faced by MCP developers | developers]] can generate revenue from their [[Model context protocol MCP | MCP]]s <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## [[Smitherys role in solving MCP challenges | Smithery's]] Approach to Solving [[Development and adoption of MCP | MCP Challenges]]

[[smitherys_role_in_solving_mcp_challenges | Smithery]] was founded in December 2024 to tackle these ecosystem challenges <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Its goal is to become the "AI gateway" that grows and orchestrates the new era of AI native services for AI agents <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Demonstration of [[smitherys_role_in_solving_mcp_challenges | Smithery's]] Capabilities

[[smitherys_role_in_solving_mcp_challenges | Smithery's]] playground demonstrates what an AI agent can achieve with access to thousands of curated [[Model context protocol MCP | MCP]]s <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, an agent can be prompted to "Find the most pressing issue on my GitHub repository called `smidy-CLI` and create a new ticket on Linear" <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

The agent's process involves:
1.  Thinking about the issue <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
2.  Calling a search servers function to find relevant servers within [[smitherys_role_in_solving_mcp_challenges | Smithery]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  Connecting to the best server, including Linear <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
4.  Using the GitHub [[Model context protocol MCP | MCP]] to find the most high-priority bug <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
5.  Creating a ticket on Linear with details and a link to the original issue <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

This end-to-end task showcases an AI agent connected to two different [[Model context protocol MCP | MCP]]s <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>, demonstrating the potential when [[Fragmentation and installation issues of MCPs | MCP problems]] are addressed.

## The Future of the Internet and [[mCPs Role in Augmented LLM Systems | AI Agents]]

The rapid increase in [[Development and adoption of MCP | MCP]] server deployments and tool calls <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a> indicates a strong developer enthusiasm for the [[Model context protocol MCP | MCP]] ecosystem <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. It is becoming clear that the future of the internet will be dominated by "tool calls" rather than traditional "clicks" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. In this evolving landscape, the "agent experience" will supersede the "user experience" in importance <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, and this future will be built collaboratively by the entire community <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.