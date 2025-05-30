---
title: Strategic considerations for AI application developers
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

A recent discussion on Unsupervised Learning covered a wide range of topics pertinent to [[role_and_expectations_of_software_developers_in_the_context_of_ai_advancements | software developers]] and enterprises navigating the evolving landscape of AI agents and infrastructure <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Key themes included understanding agent capabilities, building for an "agentic future," differentiating application builders, and identifying needs in [[challenges_and_opportunities_in_ai_infrastructure_development | AI infrastructure]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## The Agentic Future

The long-term vision for AI agents involves their deep embedding into daily products, moving beyond dedicated surfaces like ChatGPT <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The goal is for agents to become ubiquitous, automating tasks and performing research across the web <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Evolution of Agent Interactions
Agent interaction with the web has evolved significantly from single-turn searches to multi-step reasoning processes <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Products like Deep Research demonstrate models that can retrieve information, rethink their approach, and open multiple web pages in parallel to save time <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This "chain of thought" tool calling represents a major shift in how agents access and process information <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. It is anticipated that web page extraction might be replaced by other agents, seamlessly embedded in a chain of thought process involving both the internet and private data/agents <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Building for Enterprises
Enterprises are already building multi-agent architectures to solve business problems, particularly in areas like customer support automation <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. This often involves swarms of agents, each handling specific tasks (e.g., refunds, billing, escalating to a human) <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The Agents SDK was released to simplify the development of these multi-agent systems <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Companies are advised to build AI agents internally to address real problems before considering exposing them to the public internet <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Where Agents Work Today
In 2024, agentic products typically involved clearly defined workflows with a limited number of tools (less than 10-12) <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Examples included coding agents, customer support automation, and deep research projects <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. In 2025, the shift is towards models performing complex reasoning within a chain of thought, enabling them to call multiple tools, backtrack, and try different paths without deterministic workflows <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Challenges with Many Tools and Runtime
A significant future unlock for agents is removing the constraint on the number of tools they can access, allowing them to intelligently select from hundreds of tools <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Additionally, increasing the available runtime for models from minutes to hours or days will yield more powerful results, as humans can work on tasks for extended periods using many tools <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## Developing and Fine-tuning Agents

### Reinforcement Fine-tuning and Domain Specificity
Reinforcement fine-tuning, involving tasks and graders, is crucial for developers to teach models to find the correct tool-calling paths for domain-specific problems <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This process steers the model's chain of thought, essentially training it to think in the way a legal scholar or medical doctor would, leading to significant verticalization for these models <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

### Challenges in Grading and Evaluation
Providing effective tooling for grading and evaluation in domain-specific contexts like legal or healthcare remains a challenge <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. While basic building blocks for flexible graders exist (e.g., cross-referencing model output with ground truth or executing code for mathematical correctness), productizing these tools for broad use is a major problem to be solved <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The difficulty lies in creating robust evaluations that go beyond simple string matching and capture complex domain performance <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

### Computer Use Models and Unexpected Applications
Computer use models have shown surprising versatility <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Initially thought for automating legacy applications without APIs (e.g., manual clicks across multiple medical apps) <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>, they have also found applications in areas like Google Maps research, including using Street View to check for changes in charging networks <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. These models are well-suited for domains that don't map to plain text JSON, requiring a combination of vision and text ingestion <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. Startups like Browser Base and Scrappy Bar are providing services for hosting virtual machines to make computer use models work effectively <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

## Strategic Approaches for Developers

### Balancing Immediate Needs with Future Model Capabilities
Developers often build scaffolding around current model capabilities to get products to market, even if future models might obviate those steps <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>. The current models are often more capable than how most AI applications are leveraging them, making the orchestration of agents and tools paramount <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. While waiting for models to improve might simplify workflows, actively building things around models to make them work well is critical for AI startups and products <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

### Importance of Orchestration and Debugging
Meticulous orchestration, examining traces, effective prompt engineering, and maintaining eval sets to prevent prompt degradation are challenging but essential skills for developers <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. Splitting tasks among multiple agents simplifies debugging, as changes to individual agents have a smaller "blast radius" compared to modifying a single, highly capable model with many instructions <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### API Design Philosophy: APIs as Ladders
The design of APIs aims to provide significant power out-of-the-box, making simple tasks easy, while also offering deeper customization options for developers who want to invest more effort <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. For example, file search is easy to use with defaults, but allows tweaking parameters like chunk size, metadata filtering, and re-ranker customization for more advanced use cases <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. The goal is a quick start (e.g., four lines of curl code) with many optional parameters for fine-tuning <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

### Future API Customization
Future "knobs" for APIs include site filtering and granular location settings for web search <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>. The Responses API aims to incorporate features from the previous Assistance API (like storing conversations and model configurations) as opt-in parameters, reducing the initial complexity for new users <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.

### Learnings from Previous APIs
The Assistance API's success was in tool use, especially file search, demonstrating market fit for bringing custom data to models <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. However, it was criticized for being too difficult to use, with no easy way to opt out of context storage <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. The Responses API combines the multi-output and tool-use capabilities of the Assistance API with the ease of use of chat completions, allowing users to provide their own context on each turn <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>.

## The AI Infrastructure Landscape

The Responses API focuses on making multi-turn interactions with models effective, providing a foundation for models to call themselves and tools multiple times to reach a final answer <a class="yt-timestamp" data-t="00:26:23">[00:26:23]</a>.

### OpenAI's Role vs. Standalone Companies
OpenAI is building out-of-the-box tools in response to user demand for a "one-stop shop" for LLM functionalities like data search and internet search <a class="yt-timestamp" data-t="00:27:41">[00:27:41]</a>. However, standalone AI infrastructure companies continue to build powerful, low-level, and infinitely flexible APIs, serving a large market <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. There's also a growing space for vertical-specific AI infrastructure (e.g., VMs for coding AI startups) and LLM operations companies that manage prompts, billing, and usage across multiple models and providers <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.

### Key Challenges for Developers
Major remaining challenges for developers include:
*   **Tools Ecosystem**: Building a robust tools ecosystem on top of foundational APIs <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>.
*   **Computer Use VM Space**: Secure and reliable deployment of virtual machines for computer use models within enterprise infrastructure <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. The fragmentation across different environments (browsers, iPhone screenshots, Android, Ubuntu flavors) presents a significant challenge for the community to address <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>.

### Underexplored Applications
One particularly underexplored application area is **scientific research** <a class="yt-timestamp" data-t="00:41:41">[00:41:41]</a>. The expectation was that AI models would revolutionize scientific discovery, but the interfaces are not yet optimal for academia <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>. Robotics is another area ripe for significant advancements with AI <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.

## Recommendations for Businesses

For enterprise or consumer CEOs, the advice is to immediately start exploring frontier models and computer use models <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>. Experiment with internal workflows to build multi-agent architectures that automate tasks end-to-end <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>. Identify manual workflows that could benefit from a tool interface and work towards programmatic access <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. This mirrors the "digital transformation" trend from the cloud era, focusing on automating applications <a class="yt-timestamp" data-t="00:37:17">[00:37:17]</a>. Employees should be encouraged to identify their least favorite daily tasks to automate, as this will increase productivity and satisfaction <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

## Overhyped/Underhyped AI Aspects

Agents are considered both overhyped and underhyped <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>. They have gone through multiple hype cycles, but companies that successfully implement them to automate manual tasks or create deep research capabilities achieve significant results <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>.

The power of **reasoning models** combined with **tool use** has been a significant mind-shift, enabling a move from deterministic workflows to fully agentic products that deliver powerful results <a class="yt-timestamp" data-t="00:39:23">[00:39:23]</a>. Similarly, the power of **fine-tuning** to inject custom information into models and significantly move the needle for specific tasks is impressive <a class="yt-timestamp" data-t="00:40:13">[00:40:13]</a>.

The biggest differentiator for application builders long-term will be the ability to **orchestrate** tools, data, and multiple model calls effectively, rapidly evaluating and improving performance <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>.

Model progress is expected to be *more* significant this year than last, driven by a feedback loop where models help researchers improve them with better data <a class="yt-timestamp" data-t="00:42:33">[00:42:33]</a>.

The AI travel agent remains a highly anticipated yet elusive product, despite being a common demo <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>. The travel industry is deeply entrenched, waiting for someone to truly "crack" the AI travel agent <a class="yt-timestamp" data-t="00:42:58">[00:42:58]</a>.