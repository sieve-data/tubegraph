---
title: Developers approach to AI models and agents
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

This article explores how developers and enterprises should think about, build with, and deploy AI models and agents, drawing insights from industry experts. It covers [[the_future_and_current_state_of_ai_agents | the future and current state of AI agents]], development tools, infrastructure, and the [[challenges_and_strategies_in_deploying_ai_models_for_developers | challenges and strategies in deploying AI models for developers]].

## The Agentic Future and Computer Use Models

In the next 5-10 years, AI agents are expected to become deeply embedded in everyday products across the web, rather than being confined to specific surfaces like ChatGPT [01:13:15]. This means seeing "computer use" in browsers and "operator" automating daily work tasks, including clicking, filling forms, and research [01:21:23]. The API platform aims to disperse this technology, making it ubiquitous [01:44:00]. Developers, leveraging their domain expertise, are expected to create vertically integrated products using these model capabilities [02:04:05].

An example of a highly desired agent is an API designing agent, which could automate the tedious process of going through parameter names and configurations [02:22:00]. This agent could be fine-tuned on preferred API designs [02:44:00].

### Evolution of Agent Interaction

The way agents interact with and retrieve information from the web has significantly changed [03:27:00].
Previously, an agent would perform a single turn, decide whether to search, get information, and synthesize a response (characteristic of 2024) [03:27:00].
In 2025, products like "deep research" demonstrate a new model where the agent iteratively retrieves information, reconsiders its stance, fetches more data, and can even open multiple web pages in parallel to save time [03:40:00]. This "chain of thought" tool calling is a major shift in how agents access information [04:00:00].

Future interactions could involve agents seamlessly calling other agents as endpoints, without necessarily knowing they are AI entities, simply receiving useful information for decision-making [04:15:00]. This process will be deeply embedded in the chain of thought, with tool calling happening between the internet, private data, and private agents [04:36:00].

Companies are advised to build AI agents internally to solve real problems before exposing them to the public internet [06:07:00]. There is an expectation that such external exposure will become more common in the coming months [06:21:00].

### Data Considerations for Developers
As tools become more connected to the web, models will process significantly more data from the web, not just data provided by the user [06:40:00].

## Heuristics for Agent Effectiveness

### Limits of Tools and Runtime
In 2024, most agentic products had clearly defined workflows, using fewer than 10-12 tools with well-orchestrated steps [07:02:00]. This approach was effective for building coding agents, customer support automation, and deep research projects [07:21:00].

In 2025, the model operates in a "chain of thought," being smart enough to call multiple tools, recognize wrong paths, and backtrack [07:32:00]. This moves away from deterministic workflow building [07:48:00]. The next step is to remove the constraint of 10-15 tools, allowing agents to access hundreds of tools and intelligently select the right one [08:05:00].

> "This thing becomes because it's it's like it has all the superpower it needs. It has the compute. It has the way of like reasoning about different tool trajectories. And it has access to a lot of tools." <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>

Another key area for improvement is increasing the available runtime for models from minutes to hours or even days, which is expected to yield powerful results [08:49:00]. Previously, strict guardrails were necessary to prevent models from going off-rails, but increased flexibility is now possible [09:08:00].

### Reinforcement Fine-Tuning and Grading

Reinforcement fine-tuning is a technique where developers create tasks and graders to help the model find the correct tool-calling path for unique domain-specific problems [09:35:00]. This approach trains the model's "thinking" process, similar to how a university education trains a human in a specific domain [10:06:00]. This is expected to drive significant verticalization for models [10:31:00].

Providing infrastructure for fine-tuning involves giving developers the ability to build their own graders [10:50:00]. These graders can cross-reference a model's chain of thought or output with known ground truth (e.g., a medical textbook) or execute code to verify mathematical correctness [11:16:00]. This allows developers to steer the model towards better outputs during fine-tuning [11:31:00].

> "It feels like the biggest question across the board in so many aspects of AI right now is like what actually can be graded." <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>

The biggest challenge is productizing grading and task generation to make it accessible for any domain, as it currently requires significant iteration and effort [12:48:00]. This is considered the biggest problem to be solved in the coming year(s) [12:48:00].

## Computer Use Cases

Computer use cases for agents have been surprisingly diverse [13:28:00]. Initially, the focus was on automating legacy applications lacking APIs [13:36:00]. Examples include automating manual tasks across multiple medical applications [13:46:00].

Unexpectedly, computer use models are also being applied to tasks like research on Google Maps [14:02:00]. For instance, UniFi GTM used it to answer climate tech startups' questions about charging network expansion by having an agent open Google Maps, use Street View, and observe changes [14:08:00]. These models can automate nearly anything [14:48:00].

Computer use is well-suited for domains that don't map to JSON or plain text over the web, requiring a combination of vision and text ingestion [14:57:00].

## API Design Philosophy: Ladders and Customizability

The design of APIs follows an "APIs as ladders" philosophy [21:54:00]. The goal is to provide significant power out-of-the-box and make simple tasks easy [22:05:00]. Developers can then gain more control and better results by putting in more effort [22:11:00].

A good example is file search: it's easy to use by simply uploading documents and popping in a vector store ID [22:16:00]. For more advanced use cases, developers can tweak parameters like chunk size (e.g., from a default of 400 to 200 or 1000) [22:29:00]. Further customization includes metadata filtering and re-ranker customization, but these are not mandatory upfront, allowing for a gradual learning curve [22:47:00]. The aim is to make the quick start process very simple (e.g., four lines of curl code) while offering many optional parameters [23:10:00].

Desired additional "knobs" include site filtering for web search and more precise location setting (down to a block or even a court) for location-based queries [23:30:00].

The Responses API is being built to incorporate features from previous APIs, like the Assistants API, but without forcing users into complex concepts [24:00:00]. Users can opt-in to features like conversation storage (equivalent to threads) or model configuration storage (like an assistant object) with a single parameter [24:35:00].

### Learnings from Previous APIs

The Assistants API was successful in demonstrating the power of tool use, particularly with the file search tool, which found market fit by allowing users to bring their own data for the model to search [25:16:00].

However, the Assistants API was too difficult to use, forcing context storage without an opt-out, and had a limiting chat completions interface where the API could only output one thing, despite the model doing many things in the background [25:31:00]. The Responses API aims to combine the best parts of the Assistants API (tool use, multiple outputs) with the ease of use of chat completions [26:01:00].

## The Landscape of AI Infrastructure and Developer Challenges

The Responses API focuses on enabling good multi-turn interactions with models, allowing a model to call itself and tools multiple times to reach a final answer [26:23:00]. The MCP (Multi-Modal Chat Protocol) is complementary, focusing on how tools are used and brought to models [26:53:00].

### Opportunity for Standalone AI Infrastructure Companies

While OpenAI provides more out-of-the-box tools, there is still a significant market for AI infrastructure companies building low-level, infinitely flexible APIs [27:38:00]. Vertical-specific AI infrastructure companies are also emerging, such as those providing VMs for coding AI startups to test code [28:23:00]. There's also a class of LLM ops companies that manage prompts, billing, and usage across multiple models and providers [28:51:00].

### Remaining Challenges for Developers

Key challenges for developers working with AI models and agents include:
*   **Tools Ecosystem**: Building a robust tools ecosystem on top of foundational blocks [29:36:00].
*   **Computer Use VMs**: Securely and reliably deploying virtual machines for computer use models in enterprise infrastructure, including observation and monitoring [29:57:00]. These models are expected to improve rapidly [30:18:00].
*   **Environments for Computer Use**: The "computer use" tool is being tested in diverse environments beyond browsers, such as iPhone screenshots and Android, indicating a need for specialized VM providers (e.g., iPhone VMs) [30:37:00].
*   **Evaluation and Productization**: The biggest pain point remains the difficulty of creating reliable evaluation sets and productizing the process of training models to find the right path and solve problems [35:50:00]. Making this process ten times easier is crucial [35:50:00].
*   **Model Output**: Improving the ability of models to generate "diffs" that can be cleanly applied to code without manual adjustments [33:35:00].

The recent impressive agent work out of China validates the internal belief that models already possess significant capabilities, but making these capabilities accessible to non-expert AI/ML developers is the challenge [34:09:00]. The goal is to make the flywheel of evaluation, production, and fine-tuning much simpler [35:01:00].

## Advice for Companies and Future Trends

For CEOs of enterprises or consumer companies, the advice is to start exploring frontier models and computer use models immediately [36:30:00]. Identify internal workflows that are manual and try to automate them using multi-agent architectures and tool interfaces [36:51:00]. This is a resurgence of the "digital transformation and automation" trend seen during the cloud era [37:17:00]. Developers should focus on automating their least favorite day-to-day tasks to increase productivity [38:15:00].

### Overhyped vs. Underhyped

Agents are both overhyped and underhyped [38:50:00]. Overhyped due to multiple hype cycles, but underhyped because companies that successfully implement them for deep research or manual task automation gain immense capabilities [38:53:00].

### Shifts in Perspective

A significant shift in perspective for developers has been the underestimated power of reasoning models combined with tool use [39:23:00]. This combination has enabled the creation of sophisticated agentic products like "operator" and "deep research" that autonomously figure out tool use within their chain of thought [39:37:00].
Another shift is the appreciation for fine-tuning, realizing its power to add custom information to models and significantly improve performance for specific tasks [40:13:00].

### Differentiators for Application Builders

Long-term, the biggest differentiator for application builders will be a combination of deep knowledge of models and domain expertise [40:32:00]. The ability to "bring the AGI out of the models" through prompt engineering, workflow orchestration, or other means will be crucial [40:47:00]. Orchestration—bringing together tools, data, and multiple model calls, evaluating, and quickly improving them—is considered the most important skill for the next year or two [41:02:00].

### Underexplored Applications

*   **Scientific Research**: There is hope for a step change in how quickly scientific research happens [41:41:00]. Finding the right user interface for academia, a field resistant to change, is key to driving adoption [42:02:00].
*   **Robotics**: Robotics is another area ripe for significant advancements [42:19:00].
*   **Travel Industry**: The travel industry, being entrenched with few big players, presents a huge opportunity for someone to build the definitive AI travel agent, moving beyond current demos to a widely used product [42:51:00].

### Model Progress

Model progress in the coming year is expected to be even greater than last year [42:29:00], driven by a feedback loop where models teach developers how to improve them with better data [42:36:00].

## Resources for Developers

For more information, listeners can visit:
*   OpenAI Documentation: platform.openai.com/docs [43:47:00]
*   OpenAI Devs Twitter account [43:56:00]
*   OpenAI Community Forum (search for "Open community forum") [44:00:00]