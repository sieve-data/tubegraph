---
title: Understanding MCPs and their Importance
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

Everyone is discussing MCPs, and the topic has become very popular, yet many people do not understand what MCPs are, what they mean, or the [[startup_opportunities_around_mcps | startup opportunities]] associated with them <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Professor Ross Mike explains these technical concepts in an accessible way, making them understandable even for non-technical individuals <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Understanding MCPs is crucial, as they are a significant development in technology <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## The Role of Standards in Programming

In programming, standards are highly valued by engineers <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Standards enable engineers to build systems that can communicate effectively with each other <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. A well-known example is REST APIs, which provide a standard that companies follow when developing their APIs and services, allowing engineers to connect with them <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Standards simplify the development process and make life easier for engineers <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

## Limitations of Current LLM Capabilities

Large Language Models (LLMs) by themselves are incapable of performing meaningful actions <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For instance, early versions of ChatGPT or any chatbot cannot send an email; they will simply state that they cannot perform such a task <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. The primary function of an LLM is to answer questions or provide information about historical figures <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. In their current state, LLMs are primarily good at predicting the next word in a sequence <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### LLMs Combined with Tools

The next major advancement was developers discovering how to integrate LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. For example, chatbots like ChatGPT can search the internet by utilizing external services <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Perplexity, for instance, allows an LLM to fetch and present information from the internet, though the LLM itself doesn't inherently possess this capability <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Connecting tools to LLMs has made them significantly more powerful <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Challenges with Multiple Tools

While connecting tools enhances LLMs, it becomes challenging when building an assistant that needs to perform multiple functions, such as searching the internet, reading emails, and summarizing content <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Developers end up "gluing" together various tools to LLMs, which can be cumbersome <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. The difficulty in creating an "Iron Man level Jarvis assistant" stems from the complexities of combining and cohesively stacking these tools <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

Even though tools make LLMs more capable, LLMs are inherently "very, very dumb" on their own <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Connecting diverse tools, like those used by AI startup Tempo, involves finding external services, linking them to the LLM, and ensuring the LLM does not hallucinate or behave unpredictably <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This process is time-consuming and prone to issues; for example, if a service like Slack updates its API, it can break the entire automated workflow, leading to significant engineering effort <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

## MCPs: The Next Evolution

MCPs (Machine Common Sense Protocol) are considered the next evolution for LLMs <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### MCP as a Unifying Layer

MCP serves as a unifying layer positioned between an LLM and various services or tools <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. It translates the different "languages" of each tool into a single, unified language that the LLM can perfectly understand <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This integration simplifies the process for LLMs to connect with and access diverse external resources <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

MCP aims to overcome the challenges of manual work, step-by-step planning, and numerous edge cases that can lead to failures in the LLM-plus-tools paradigm <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. It unifies the LLM and the service, creating an efficient communication layer <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

### The MCP Ecosystem

The MCP ecosystem comprises four main components:
1.  **MCP Client**: This is the LLM-facing side, such as Tempo, Wind Surf, or Cursor <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
2.  **MCP Protocol**: This facilitates the two-way connection between the client and the server <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
3.  **MCP Server**: This component translates an external service's capabilities to the client <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
4.  **Service**: The external tool or resource itself <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

A fascinating aspect of MCP is that the MCP server's construction is now the responsibility of the service provider <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. This means companies like Anthropic, aiming for more capable LLMs, have put the onus on service providers to build these servers <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Consequently, many external service providers are actively developing MCP servers <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

Ultimately, MCP is a significant development because it establishes a standard that all companies and engineers are expected to adopt <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>. Just as different spoken languages are unified by standards, MCP allows LLMs to communicate with external services meaningfully, transforming them from mere prediction systems into tools capable of important tasks <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Current State and Future Outlook

While MCP is promising, there are currently [[the_challenges_of_implementing_mcp_servers | technical challenges]] <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Setting up an MCP server can be annoying, involving many local file movements and configurations <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. There are "Kinks that have to be figured out" <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

Once these issues are resolved and the standard is refined, LLMs will become even more capable <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. MCP's core purpose is simplifying the process of [[mcps_and_their_role_in_making_llms_more_capable | making LLMs more capable]] <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. It is designed to be a structured standard that, if followed, will give LLMs seamless access to everything they need <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### [[startup_opportunities_around_mcps | Startup Opportunities]]

Historically, the popularization of protocols like HTTPS and SMTP has led to the creation of many large businesses <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. MCP presents similar opportunities.

For technical individuals, there are numerous possibilities. One idea is an "MCP App Store" where users can browse and deploy different MCP servers (found on GitHub repos) with a single click, obtaining a URL to integrate with an MCP client <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.

For non-technical individuals, the advice is to stay updated on platforms building MCP capabilities and monitor how these standards evolve <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. It's uncertain if MCP is the final standard, or if it will be challenged or updated by companies like Anthropic <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

Once the standard is finalized and service providers adopt MCP, integration will become much smoother and easier <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>. This will make building applications with LLMs feel like stacking "Lego pieces" <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>. As this technology is in its early stages, the best approach for smart business owners is to observe and learn, striking when the right opportunity emerges <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. Understanding MCP's mechanics now will prepare individuals to capitalize on future developments <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.