---
title: Enterprise adoption of AI agents
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

The future of AI agents points towards their deep embedding into daily products and business operations, moving beyond standalone applications like ChatGPT <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. This shift is driven by the release of underlying models and APIs that allow for wider dispersion of agentic capabilities across the web <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Vision for Agent Interaction

In the next 5-10 years, consumers are expected to interact with agents not just in dedicated surfaces like ChatGPT, but also within existing browsers or through automated tasks at work <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. These agents will automate tasks like clicking, filling out forms, and conducting research, becoming seamlessly embedded into everyday tools <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. The API platform aims to disperse this technology to make it ubiquitous <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

## Building for an Agentic Future

Enterprises should actively build towards this agentic future by creating internal AI agents to solve real business problems <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.

### Multi-Agent Architectures
Developers are already creating multi-agent swarms to address complex business problems, particularly in areas like customer support automation <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. For example, in customer support, different agents can specialize in refunds, billing, shipping, or escalate to human assistance <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. The Agents SDK was released to facilitate the building of these multi-agent architectures <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

Splitting tasks among multiple agents simplifies debugging and increases efficacy, as each agent can focus on a specific task with dedicated context <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>. This prevents the need to prompt engineer a single agent for a multitude of functions, reducing the "blast radius" of changes during development <a class="yt-timestamp" data-t="18:49:00">[18:49:00]</a>.

### Internal vs. External Exposure
While internal use cases are immediate, exposing these agents to the public internet for communication is a future development that makes significant sense <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

### [[enterprise_ai_adoption_challenges | Challenges in Enterprise AI Deployment]]
*   **Grading and Task Generation**: Productizing effective grading and task generation remains a significant challenge for enterprises, making it difficult for almost anyone to utilize these tools <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
*   **Orchestration Complexity**: Making models work effectively requires significant effort in orchestration, meticulous trace observation, prompt engineering, and maintaining eval sets to prevent degradation <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>. This process is currently very difficult <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>.
*   **Tool Constraints**: Currently, models have a constraint on the number of tools they can effectively manage (typically less than 10-15) <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. The next "unlock" is enabling agents to intelligently use hundreds of tools <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>.
*   **Runtime Limitations**: While agent runtimes are extending to minutes (e.g., Deep Research), extending them to hours or days will yield more powerful results <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.

### Recommendations for Enterprise Leadership
For CEOs of enterprises contemplating the [[state_and_future_of_ai_agents | agentic future]], the recommendation is to:
1.  **Start Exploring**: Begin exploring frontier models and computer use models <a class="yt-timestamp" data-t="36:42:00">[36:42:00]</a>.
2.  **Automate Internal Workflows**: Identify and automate internal manual workflows using multi-agent architectures <a class="yt-timestamp" data-t="36:49:00">[36:49:00]</a>.
3.  **Identify Manual Workflows for Tool Interfaces**: Determine which manual workflows require a tool interface to become programmatic <a class="yt-timestamp" data-t="37:05:00">[37:05:00]</a>.
4.  **Prioritize Employee Pain Points**: Ask employees about their least favorite daily tasks and seek ways to automate them to increase productivity and satisfaction <a class="yt-timestamp" data-t="38:15:00">[38:15:00]</a>.

## [[Advancements and implications of AI agents | Advancements in AI Agents]] and Computer Use Models

### Evolution of Agent Behavior
The approach to agent interaction has evolved from single-turn web searches to multi-turn reasoning processes <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. Modern agents can get information, reconsider their stance, retrieve more data, and even open multiple web pages in parallel, utilizing a "chain of thought tool calling" mechanism <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This means the model figures out how to call multiple tools, and even backtrack or change its path if needed <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.

Reinforcement fine-tuning allows developers to define tasks and graders, enabling models to find the optimal tool-calling path for specific problems unique to their domain <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. This process teaches the model how to "think" about a domain, similar to how university training shapes human thought <a class="yt-timestamp" data-t="10:06:00">[10:06:00]</a>.

### Computer Use Models
Computer use models have shown surprising versatility:
*   **Legacy Applications**: Automating tasks in legacy applications without APIs, common in domains like medical where complex manual clicks across multiple applications are prevalent <a class="yt-timestamp" data-t="13:34:00">[13:34:00]</a>.
*   **Novel Research**: Examples include agents using Google Maps and Street View to research climate tech startups' charging network expansion, despite Google Maps having an API <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. This highlights the ability to automate complex visual and textual information processing where traditional APIs might be insufficient or too complex <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>.
*   **Cybersecurity**: Exploring vulnerabilities in websites and services <a class="yt-timestamp" data-t="31:25:00">[31:25:00]</a>.

The models work best in browser environments, but people are experimenting with them in diverse environments like iPhone screenshots and Android <a class="yt-timestamp" data-t="30:37:00">[30:37:00]</a>.

### Future of AI Tools and Infrastructure
*   **API Design Agent**: A desired agent is one that can design APIs, leveraging deep research into best practices and fine-tuning on preferred APIs <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.
*   **Tool Ecosystem**: There is a need to build a robust tool ecosystem on top of foundational APIs like the responses API, which focuses on multi-turn model interactions and tool calls <a class="yt-timestamp" data-t="29:42:00">[29:42:00]</a>.
*   **Verticalized AI Infrastructure**: Opportunities exist for specialized AI infrastructure companies providing VMs tailored for specific verticals (e.g., coding AI startups requiring rapid VM spin-up/spin-down) <a class="yt-timestamp" data-t="28:23:00">[28:23:00]</a>.
*   **LLM Ops Companies**: Companies helping developers manage prompts, billing, and usage across multiple models and providers (e.g., OpenRouter) are valuable <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>.

## Differentiators for Application Builders
The biggest differentiator for application builders in the long term will be their ability to orchestrate tools and data with multiple model calls, evaluate results quickly, and continuously improve their applications <a class="yt-timestamp" data-t="41:02:00">[41:02:00]</a>. This includes leveraging reinforcement fine-tuning for tools within a chain of thought or chaining together multiple LLMs <a class="yt-timestamp" data-t="41:17:00">[41:17:00]</a>.

## Under-explored Applications
Areas with significant untapped potential include:
*   **Scientific Research**: Expecting a step change in the speed of scientific discovery <a class="yt-timestamp" data-t="41:41:00">[41:41:00]</a>.
*   **Robotics**: Poised for major advancements driven by these models <a class="yt-timestamp" data-t="42:19:00">[42:19:00]</a>.
*   **Travel Industry**: The creation of a truly effective AI travel agent remains an under-explored, though frequently cited, application <a class="yt-timestamp" data-t="42:54:00">[42:54:00]</a>.

## Outlook
Model progress in the coming year is expected to be even greater than last year, driven by a feedback loop where models teach developers how to improve them with better data <a class="yt-timestamp" data-t="42:33:00">[42:33:00]</a>. The focus is on making the evaluation to production to fine-tuning loop much simpler and faster <a class="yt-timestamp" data-t="35:01:00">[35:01:00]</a>.