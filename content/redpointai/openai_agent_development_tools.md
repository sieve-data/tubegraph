---
title: OpenAI agent development tools
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

OpenAI has introduced new tools and APIs designed to facilitate the development and deployment of advanced AI agents, reflecting a long-term vision of embedding these capabilities across various products and web surfaces <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This includes addressing needs in [[ai_infrastructure_and_developer_tools | AI infrastructure]] and creating opportunities for startups <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Vision for Agents and Computer Use Models

The long-term vision for agents is their deep integration into everyday products rather than being confined to specific interfaces like ChatGPT <a class="yt-timestamp" data-t="01:11:03">[01:11:03]</a>. This means agents will automate tasks within browsers and workplaces, performing actions like clicking, filling forms, and conducting research <a class="yt-timestamp" data-t="01:21:40">[01:21:40]</a>. The goal of the API platform is to disperse agentic capabilities widely, making them ubiquitous <a class="yt-timestamp" data-t="01:46:27">[01:46:27]</a>. Developers, who have superior domain knowledge, are expected to leverage these models to create a wide array of specialized products <a class="yt-timestamp" data-t="01:59:04">[01:59:04]</a>.

An example of a highly anticipated agent is an API-designing agent, which could automate the tedious process of defining parameters <a class="yt-timestamp" data-t="02:22:15">[02:22:15]</a>.

## Evolution of Agent Interaction

The interaction of agents with the web has significantly evolved <a class="yt-timestamp" data-t="03:22:58">[03:22:58]</a>.
Initially, agents would perform a single turn of action, decide whether to search the web, retrieve information, and then synthesize a response <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
By 2025, the paradigm shifted towards "chain of thought" processes, where models continuously get information, re-evaluate their stance, retrieve more data, and even open multiple web pages in parallel to save time <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. This multi-step reasoning with tool calling is a major shift <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Future developments might see web page extraction replaced by interactions with other agents via endpoints <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. This chain of thought process, where tool calling happens seamlessly between the internet, private data, and private agents, is expected to become commonplace <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

## New Tools and Capabilities

OpenAI has released several tools to support [[compound_ai_systems_and_their_development | compound AI systems and their development]] and agent capabilities:

### Responses API
The Responses API is designed to facilitate multi-turn interactions with models, allowing a model to call itself and tools multiple times to reach a final answer <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>. It aims to combine the ease of use of chat completions with the advanced tool-use capabilities of the Assistants API <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

### Agents SDK
The Agents SDK was released to enable developers to create multi-agent architectures for solving complex business problems <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. This architecture is popular for tasks like customer support automation, where different agents handle specific issues (e.g., refunds, billing, escalating to humans) <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>. This approach of splitting tasks among many agents simplifies debugging and improves efficacy by allowing each agent to focus on a specific task <a class="yt-timestamp" data-t="01:10:59">[01:10:59]</a>.

### Computer Use Models
Computer use models automate tasks across applications, particularly beneficial for legacy systems without APIs <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Examples include automating manual medical tasks across multiple applications <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
Unexpectedly, these models have also been used for complex research tasks, such as UniFi GTM using them to research charging networks on Google Maps, including Street View, despite Google Maps having an API <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. This highlights their utility in domains where data doesn't map to JSON or requires a combination of vision and text ingestion <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. The potential for automating "anything" is significant <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The Arc browser's "DIA" feature, which allows users to open a tab and give an instruction for the browser to perform tasks in the background, is a cool example of native integration <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

### File Search
File search is highlighted as an easy-to-use tool where developers can upload documents and integrate them with models using a vector store ID <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. This capability allows models to search over user-provided data, which found significant market fit <a class="yt-timestamp" data-t="00:25:21">[00:25:21]</a>.

## [[challenges_and_opportunities_in_aiagent_development | Challenges and Opportunities in AI Agent Development]]

### Evaluation and Grading
A significant challenge remains in productizing effective grading and task generation for domain-specific AI models <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. While methods like reinforcement fine-tuning with custom tasks and graders exist, making this process easy and accessible for all developers is a major hurdle <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. The ability to "steer" a model's chain of thought by teaching it how to approach specific domains (e.g., legal, medical) is a powerful concept <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. OpenAI provides basic building blocks for graders, allowing developers to cross-reference model outputs with ground truth or execute code for mathematical correctness <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.

### Tool Constraint and Runtime
In 2024, agentic products were typically limited to well-defined workflows with fewer than 10 tools <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. The next major unlock is to remove this constraint, allowing agents to access and figure out the right tools from hundreds of options <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
Another challenge is extending model runtime from minutes to hours or even days, which is expected to yield more powerful results <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## API Design Philosophy: "APIs as Ladders"

OpenAI's API design follows the "APIs as ladders" principle <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. This means providing significant power out of the box for simple tasks, while also offering granular control and customization options as developers need more complexity <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.
An example is File Search, which is easy to use with defaults but allows users to tweak parameters like chunk size, metadata filtering, and re-rankers for more advanced use cases <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>. The aim is to make the quick start simple (e.g., four lines of curl code) while exposing many optional parameters <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.
Future "knobs" could include site filtering and granular location settings for web search <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. Additionally, the Responses API allows users to opt into features like conversation storage (equivalent to the Assistants API's threads object) and model configuration storage (assistant-type object) <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

## Strategic Advice for Developers and Enterprises

> "The models are much further than where most AI applications are like making use of things." <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>
> "Building things around models to make them work really well is an extremely important thing that AI startups should be doing and products should be doing." <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>

The biggest differentiator for application builders long-term will be their ability to orchestrate tools, data, and multiple model calls <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>. This involves quickly chaining together LLMs, evaluating performance, and iterating <a class="yt-timestamp" data-t="00:41:22">[00:41:22]</a>.

For enterprises and CEOs, the recommendation is to:
1.  Start exploring frontier models and computer use models <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.
2.  Identify internal workflows for automation using multi-agent architectures <a class="yt-timestamp" data-t="00:36:49">[00:36:49]</a>.
3.  Figure out which manual workflows require a tool interface <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>.
4.  Focus on finding ways to automate applications and ensure programmatic access to tools <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
5.  Ask employees about their least favorite tasks and automate them to boost productivity <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

## Future Outlook and Underexplored Applications

### Model Progress
Model progress is expected to be even greater than last year due to feedback loops where models help improve themselves with better data <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. There is a strong desire for smaller, faster models that are good at tool use, acting as "workhorse" or "supporting" models for quick classifications and guardrailing <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. These smaller models are also more fine-tunable for specific use cases <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

### Areas of Focus
*   **Tools Ecosystem**: Building a robust tools ecosystem on top of the foundational Responses API <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
*   **Computer Use VM Space**: Maturing the [[enterprise_adoption_of_ai_agents | enterprise adoption of AI agents]] in secure, reliable virtual machine deployments, with observations and monitoring <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. The community is expected to address fragmentation in environments like iPhone VMs, Android, and various Ubuntu flavors <a class="yt-timestamp" data-t="00:30:53">[00:30:53]</a>.
*   **Eval Process**: Making the evaluation process for tasks and workflows significantly easier, as it is currently very challenging <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.
*   **Specific Model Capabilities**: Improvements in models generating clean "diffs" for code changes are highly anticipated <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>.

### Underexplored Applications
*   **Scientific Research**: Expecting a step change in the speed of scientific research <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. Finding the right AI interface for academia will be key to driving adoption <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.
*   **Robotics**: A major breakthrough is expected in robotics <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.
*   **Travel Industry**: Despite being a popular demo, a functional AI travel agent product is still missing <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.

### Over/Underhyped Areas
AI agents are considered both overhyped due to multiple hype cycles and underhyped because companies that successfully implement them achieve significant gains <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.

## Further Resources
For more information on OpenAI's APIs and tools, visit:
*   OpenAI Docs: platform.openai.com/docs <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>
*   OpenAI Developers Twitter/X account <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>
*   OpenAI Community Forum: community.openai.com <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>