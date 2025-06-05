---
title: Future of AI agent ecosystems
videoId: tOou_GJ9Ddk
---

From: [[aidotengineer]] <br/> 

The Model Context Protocol (MCP) space is a new and rapidly evolving area crucial for the [[the_impact_and_future_potential_of_ai_and_agents | future potential of AI and agents]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While Large Language Models (LLMs) have achieved impressive intelligence, this intelligence is "stuck in a box" without practical application <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. To make [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] practically useful, it is essential to consider their context and capability, specifically their inputs and outputs <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## Origin of the MCP Concept

The concept of MCP emerged from the challenge of enabling LLMs to solve complex problems. Henry, founder and CEO of Smithery, initially focused on the ARC AGI challenge, an IQ test designed for LLMs <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This challenge involves predicting missing patterns from examples, a task easy for humans (80% accuracy) but historically difficult for LLMs <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. However, with the release of OpenAI's 03, human-level performance was achieved, raising questions about the immediate deployment of [[the_impact_and_future_potential_of_ai_and_agents | autonomous agents]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

This led to what is termed "Claude's paradox": despite significant advances in intelligence from frontier labs, this intelligence remains confined <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Recognizing this, Anthropic released the Model Context Protocol (MCP) in November 2024, an open standard to help LLMs connect to various services, promising to standardize this complex problem <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The advent of MCP, combined with smarter models, aimed to standardize how models interact with services <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## [[Development and Challenges of AI Agents | Current Challenges in the MCP Ecosystem]]

Despite the initial excitement and a vibrant developer community <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, the MCP ecosystem faces several [[challenges_and_benefits_of_ai_agents | challenges]] that hinder the widespread adoption and [[future_opportunities_and_transformation_with_ai_agents | transformation with AI agents]]:

### User-Side Problems

*   **Fragmentation**: The increasing number of MCP servers makes it difficult to find high-quality ones <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The MCP committee is working on an official registry to address this, but assigning reputation to quality MCPs remains an open question <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **High Friction Install**: Many MCPs require a complex multi-step installation process, making them difficult to set up <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Insecurity**: Users risk installing insecure MCPs <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Lack of AI-Native Economy**: There is no clear plan for [[future_trends_in_ai_agent_pricing | agentic payments]] or managing subscriptions from numerous services <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Developer-Side Problems

[[building_effective_ai_agents | Developers building MCPs]] also encounter significant issues:

*   **Hosting Problems**: Despite improvements in HTTP transport, developers still grapple with stateful sessions, resumability, and other hosting complexities <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This impacts the [[impact_of_ai_and_agents_on_infrastructure | impact on infrastructure]].
*   **Lacking Developer Tooling**: Basic MCP inspectors exist, but there's a lack of tools to help developers design optimal MCPs, ensure tools are called correctly, and create the [[best_practices_for_building_ai_agents | best agent experience]] <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Distribution**: Developers face challenges in getting their MCPs discovered <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Observability**: Improving deployed MCPs after launch is difficult due to a lack of proper observability <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Monetization**: A clear path for developers to monetize their MCPs is still undefined <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Smithery's Vision and Demonstration

Smithery, founded in December 2024, aims to address these [[challenges_and_benefits_of_ai_agents | challenges]] by becoming the "AI gateway" that grows and orchestrates the new era of [[the_impact_and_future_potential_of_ai_and_agents | AI-native services]] for [[the_impact_and_future_potential_of_ai_and_agents | AI agents]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

A demo showcases the potential when these problems are solved:
The Smidy playground demonstrates an [[the_impact_and_future_potential_of_ai_and_agents | AI agent]] with access to thousands of curated MCPs <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. For example, an agent was prompted to "Find the most pressing issue on my GitHub repository called `smidy-CLI` and create a new ticket on Linear" <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. The agent successfully:
1.  Thought about the issue <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
2.  Called a search services function to find and connect to the best servers <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
3.  Used the GitHub MCP to find the highest priority bug on the repository <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
4.  Created a detailed ticket on Linear, including a link to the original issue <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
This end-to-end task was solved by an [[the_impact_and_future_potential_of_ai_and_agents | AI agent]] connected to two different MCPs, demonstrating the potential for [[developing_ai_agents_for_productivity | developing AI agents for productivity]] <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## The Future of AI Agent Ecosystems

The enthusiasm from developers for deploying servers and making tool calls is evident <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. It is increasingly clear that the future of the internet will be dominated by "tool calls" rather than "clicks" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. In this new paradigm, the "agent experience" will matter more than the traditional user experience <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. This shift will require a collaborative effort from the entire community, not just a few companies, to build this future [[future_opportunities_and_transformation_with_ai_agents | AI agent]] ecosystem <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.