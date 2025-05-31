---
title: Multiagent architecture in enterprise settings
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

Enterprises should prepare for an "agentic future," where [[the_future_and_current_state_of_ai_agents | AI agents]] become deeply embedded into products used daily <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. The most exciting development is the dispersion of underlying agentic models and APIs into a wider array of products across the web <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Current State of Multiagent Architecture

Developers are actively building multi-agent systems, often referred to as "swarms," to address complex business problems <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. OpenAI's Agents SDK was released to facilitate this process, making it easier for developers to build these solutions <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

A prominent example of this architecture is in customer support automation <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Here, different agents might specialize:
*   One agent handles refunds <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   Another manages billing and shipping information <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   A third agent might decide whether to pull from an FAQ database or escalate to a human <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

This multi-agent architecture is gaining significant popularity <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Splitting tasks across multiple agents simplifies the debugging process of the overall workflow <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>, <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. By allowing each agent to focus on a single task with all necessary context, their efficacy on those specific tasks increases dramatically <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>, <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

## Recommendations for Enterprises

For companies and CEOs, the advice is to:
*   Begin by building [[ai_agent_capabilities_and_limitations | AI agents]] internally to address immediate, real problems within the organization <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:36:59">[00:36:59]</a>.
*   Explore frontier models and computer use models <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>.
*   Identify internal manual workflows that could benefit from a tool interface and start implementing it <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>, <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>.
*   Engage employees by asking what their least favorite day-to-day tasks are and then automate those tasks <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>, <a class="yt-timestamp" data-t="00:38:17">[00:38:17]</a>. This approach can boost productivity and employee satisfaction <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>, <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>.

## [[challenges_and_strategies_in_enterprise_ai_deployment | Challenges and Strategies in Enterprise AI Deployment]]

### Tool Orchestration
The most critical aspect for enterprises is mastering agent and tool orchestration <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>, <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. The current capabilities of models often surpass how they are utilized in most [[enterprise_ai_deployment_models | AI applications]] <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>, <a class="yt-timestamp" data-t="00:19:58">[00:19:58]</a>. There is substantial value to be extracted by building robust orchestration layers around these models <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>, <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

Key challenges include:
*   Being proficient at orchestration <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>.
*   Meticulously analyzing traces <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.
*   Effective prompt engineering <a class="yt-timestamp" data-t="00:20:51">[00:20:51]</a>.
*   Maintaining an evaluation set to prevent prompt degradation <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>, <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. This process is currently very challenging <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>, <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.

### Evaluation and Fine-tuning
One of the biggest problems remaining in the [[developers_approach_to_ai_models_and_agents | AI development]] stack is creating reliable evaluation (eval) sets and grading mechanisms for models <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. While techniques like reinforcement fine-tuning exist, productizing the creation of good tasks and graders for specific domains remains difficult <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>, <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. For domain-specific applications (e.g., medical, legal), it is possible to build custom graders that cross-reference a model's output with known ground truth (e.g., medical textbooks) <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>, <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

The ability to create these tasks and graders, and get the model to find the correct tool-calling path for a unique problem, is considered crucial <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. This allows for training a model to "think" like an expert in a specific domain (e.g., a legal scholar or medical doctor) <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The goal is to make this process of evaluating tasks and workflows much easier, ideally about 10 times simpler than it is today <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

### Exposure to the Public Internet
While companies are building internal agents, the question of when and how to expose these agents to the public internet for external communication remains an area of development <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. It is anticipated that this will naturally occur as it becomes clear that external communication with an agent provides a tangible benefit <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Future Developments in AI Agent Frameworks

### Evolution of Agent Capabilities
In 2024, agentic products typically involved clearly defined workflows with a limited number of tools (less than 10-12) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. However, 2025 is shifting towards a "chain of thought" model, where the agent's reasoning process is intelligent enough to:
*   Call multiple tools <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   Reconsider its approach and backtrack if necessary <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   Open multiple web pages in parallel to save time <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

This represents a significant departure from deterministic workflow building <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. The next major step is to overcome the constraint of a limited number of tools, allowing agents to access hundreds of tools and intelligently select the right one <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Increase in Runtime and Context
Current model runtimes, like those for deep research, are in the minutes <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, but extending these to hours or days will yield more powerful results <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This increased runtime, combined with the ability to handle a broader range of data, including data from the web (not just user-provided data), is a significant development <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

### Computer Use Models
[[role_of_custom_models_and_enterprise_ai_integration | Computer use models]] are proving surprisingly versatile. Initially, they were envisioned for automating legacy applications lacking APIs <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This has been successful in domains like medical tasks involving multi-application manual clicking <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>, <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

However, new use cases have emerged:
*   **Google Maps Research:** Companies like UniFi GTM have used it to research climate tech startups, such as checking if a company has expanded its charging network by having the agent open Google Maps, activate Street View, and navigate to locations <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>, <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>, <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Vision and Text Ingestion:** Computer use models are well-suited for domains that don't map to JSON or plain text on the web, requiring a combination of vision and text ingestion <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>, <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>, <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Cybersecurity:** Startups are exploring using computer use models for cybersecurity work, like finding vulnerabilities in websites and surfaces by having the agent "poke around" <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>, <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.

The environment in which computer use tools are applied is fragmenting significantly, with models being tested on iPhone screenshots and Android, indicating a vast range of future possibilities <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>, <a class="yt-timestamp" data-t="00:30:40">[00:30:40]</a>, <a class="yt-timestamp" data-t="00:30:47">[00:30:47]</a>.

## [[current_state_and_future_of_ai_agent_frameworks | The Future of AI Agents in Software Development]]

A significant differentiator for application builders long-term will be their ability to orchestrate tools and data with multiple model calls <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>, <a class="yt-timestamp" data-t="00:41:04">[00:41:04]</a>. This includes:
*   Using reinforcement fine-tuning to enable models to call tools within their chain of thought <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>, <a class="yt-timestamp" data-t="00:41:19">[00:41:19]</a>.
*   Chaining together multiple LLMs effectively <a class="yt-timestamp" data-t="00:41:22">[00:41:22]</a>.
*   Rapidly evaluating and improving these systems <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>. This will be the most crucial skill moving forward <a class="yt-timestamp" data-t="00:41:28">[00:41:28]</a>.

In the coming months, efforts will focus on:
*   Building out the tools ecosystem on top of foundational blocks <a class="yt-timestamp" data-t="00:29:43">[00:29:43]</a>, <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.
*   Advancing the computer use VM space, especially enabling secure and reliable deployment of virtual machines in enterprise infrastructure <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>, <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   Developing smaller, faster models that are highly effective at tool use and can be easily fine-tuned for specific applications <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>, <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>, <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.

The overall goal is to make the "flywheel" from evaluation to production to fine-tuning and back again significantly simpler and faster <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>, <a class="yt-timestamp" data-t="00:35:03">[00:35:03]</a>, <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.