---
title: OpenAIs agent development tools
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

OpenAI is actively developing new tools and models to facilitate the creation and deployment of AI agents. The long-term vision for agents is to see them deeply embedded in products across the web, automating tasks and becoming increasingly ubiquitous in daily computer use [00:01:36].

## Vision for the Agentic Future
Currently, agentic products like ChatGBD, Deep Research, and Operator are accessed in specific interfaces [00:01:07]. The exciting prospect of releasing underlying models and APIs is the dispersal of these agents into more web products [00:01:15]. This means agents automating tasks like clicking, filling forms, and research, seamlessly integrated into existing applications [00:01:31]. OpenAI believes people will build highly verticalized applications, leveraging deep domain knowledge to create specialized agents [00:01:53]. One desired agent is an API designing agent, capable of deep research into best practices and fine-tuning on preferred APIs [00:02:22].

## Evolution of Agent Interaction and Capabilities
The way agents communicate and access information from the web has significantly evolved [00:03:26].

### From Single-Turn to Chain of Thought
In 2024, agentic products typically featured a single-turn process where an agent would decide whether to search the web, retrieve information, and synthesize a response [00:03:30]. By 2025, products like Deep Research demonstrate a more advanced model where the agent iteratively retrieves information, reconsiders its stance, and even opens multiple web pages in parallel to save time [00:03:44]. This "chain of thought tool calling" or calling tools within the reasoning process represents a significant shift in how [[AI agent capabilities and limitations | agents access information]] [00:04:00]. This process will become seamlessly embedded, with tool calling happening between the internet, private data, and private agents [00:04:36].

### Expanding Tool Access and Runtime
Early agentic products in 2024 were characterized by clearly defined workflows using fewer than 10 tools, suitable for tasks like coding agents or customer support automation [00:07:02]. In 2025, the model's reasoning process is smart enough to call multiple tools, course-correct, and try alternative paths, moving away from deterministic workflow building [00:07:32]. The next major unlock is removing the constraint on the number of tools, allowing agents to access hundreds of tools and independently determine the best one to use [00:08:05].

Alongside tool access, increasing the available runtime for models is crucial; from minutes, as seen in Deep Research, to hours or days, to yield more powerful results [00:08:49]. This increased flexibility means developers can allow agents more autonomy, moving beyond the need for highly specific guardrails and close chaining of tasks seen in the past [00:09:08].

### Reinforcement Fine-Tuning and Grading
[[Advancements in AI developer tools | Advancements in AI developer tools]] include techniques like reinforcement fine-tuning, which allows developers to create tasks and graders to train models to find the right tool-calling path for unique domain-specific problems [00:09:35]. This process involves teaching the model how to "think" about a specific domain, similar to how university education trains a human mind [00:10:09].

OpenAI is providing the basic building blocks for developers to create their own graders [00:11:02]. These flexible graders can cross-reference a model's train of thought or output against known ground truths (e.g., medical textbooks) or execute code to verify mathematical correctness, moving beyond simple string comparisons [00:11:16].

However, productizing grading and task generation remains a significant challenge, requiring extensive iteration and being identified as a major problem to be solved in the coming year [00:12:40].

## Computer Use Models
Computer use models have shown surprising and cool use cases [00:13:28].
Initially, they were expected to automate tasks in legacy applications without APIs, which has proven effective in manual tasks in domains like medicine, requiring clicks across multiple applications [00:13:36].

However, new applications have emerged, such as using computer use for research on Google Maps, specifically Street View, to check for infrastructure expansion (e.g., charging networks) [00:14:02]. This highlights how computer use can automate tasks that don't map easily to JSON or plain text APIs, requiring a combination of vision and text ingestion [00:14:57].

## Building for the Agentic Future: Advice for Enterprises
Companies should actively build towards an [[Future of AI agents in software development | agentic future]] by building AI agents internally to solve real business problems [00:06:06]. OpenAI has released an Agents SDK for this purpose, as many companies are already creating multi-agent architectures (e.g., "swarms" of agents) to address complex business challenges like customer support automation [00:05:12]. This architecture allows different agents to handle specific aspects (e.g., refunds, billing, FAQs) [00:05:28].

Exposing these internal agents to the public internet will become useful over time [00:05:51]. The key is to start by automating internal workflows that involve manual steps and then explore how to expose these as external services [00:37:01].

## Lessons from Previous APIs and Current Offerings
[[OpenAIs new model release and its implications | OpenAI's new model release and its implications]] reflect learnings from previous APIs.
The Assistance API, released in November 2023, excelled in tool use, particularly file search, allowing users to bring their own data to the API [00:25:16]. However, it was found to be too difficult to use due to forced context storage, which many users disliked [00:25:31]. The Chat Completions interface, while simpler, was limiting as the API could only output one thing, whereas the model could perform many background tasks [00:25:45].

The new Responses API aims to combine the best parts of the Assistance API (tool use, multiple outputs) with the ease of use of Chat Completions [00:26:01]. It adopts an "APIs as ladders" approach, providing powerful out-of-the-box functionality with simple defaults, while offering "knobs" (parameters) for deeper customization (e.g., chunk size, metadata filtering, re-ranker customization for file search) [00:22:05].

Future "knobs" include site filtering and more granular location settings for web search [00:23:32]. The Responses API also aims to build in features from the Assistance API (like storing conversations and model configurations) as optional opt-ins, making the onboarding simpler [00:24:00].

## The Role of AI Infrastructure and Tooling
The **Responses API** focuses on enabling good multi-turn interactions with models, providing a foundation for models to self-call and use tools multiple times to reach a final answer [00:26:23]. This contrasts with the MCP (Multi-Modal Chat) landscape, which focuses on how tools are brought to models, though these are complementary [00:26:53].

Regarding [[AI infrastructure and tooling | standalone AI infrastructure companies]], OpenAI acknowledges users' desire for a "one-stop shop" for LLM functionalities like data and internet search [00:27:44]. However, there will always be a market for low-level, infinitely flexible APIs built by specialized AI infra companies [00:28:01]. These can include vertical-specific solutions, such as VMs for coding AI startups (e.g., RunLoop) or LLM ops companies that manage prompts, billing, and usage across multiple models and providers (e.g., OpenRouter) [00:28:23]. OpenAI is not looking to be in the business of these highly specialized infrastructure offerings [00:28:47].

## Remaining Challenges and Future Directions for Developers
The biggest problems for developers working with these models currently include:
1.  **Tools Ecosystem:** Building a robust tools ecosystem on top of the foundational blocks provided, addressing challenges in tool registry and integration [00:29:36].
2.  **Computer Use VM Space:** Securely and reliably deploying virtual machines in enterprise infrastructure and observing the actions of computer use models [00:29:57]. This area is very early, akin to GPT-1 or GPT-2 for this paradigm, but is expected to become incredibly useful [00:30:22]. The community will need to fill gaps in supporting diverse environments like iPhone screenshots, Android, and different Linux flavors [00:30:38].
3.  **Grading and Evaluation (Evals):** The process of evaluating tasks and workflows remains challenging and needs to be about 10 times easier [00:35:50]. This is the biggest problem to solve to make the flywheel of eval-to-production-to-fine-tuning simpler [00:35:01].
4.  **Reliable Tool Use Execution:** Models don't always reliably execute multi-tool agentic tasks from turn to turn [00:32:37].
5.  **Smaller, Faster Models:** A need for much smaller and faster models that are good at tool use, serving as "workhorse" or "supporting" models for quick classifications and guardrailing [00:32:53]. These would be highly fine-tunable for specific use cases [00:33:24].
6.  **Clean Code Diffs:** The ability for models to reliably generate code diffs that can be applied cleanly without manual intervention [00:33:35].

## Advice for CEOs and Companies
For enterprise or consumer CEOs, the recommendation is to immediately start exploring frontier models and computer use models [00:36:41]. Companies should identify internal manual workflows and attempt to build multi-agent architectures to automate them end-to-end [00:36:49]. A significant portion of this effort involves gaining programmatic access to existing tools, with the LLM portion being a smaller part [00:37:32]. Essentially, companies should focus on automating the least favorite tasks of their employees to increase productivity and satisfaction [00:38:15].

## Quick Fire Round Insights

*   **Overhyped/Underhyped:** Agents are both overhyped (having gone through two hype cycles) and underhyped (companies that successfully implement them achieve significant results) [00:38:50].
*   **Mind Changed On:** The power of reasoning models combined with tool use, leading to entirely agentic products like Operator and Deep Research, moving away from rigid workflow setups [00:39:26]. Also, the significant impact of fine-tuning, allowing custom information to dramatically move the needle for specific tasks [00:40:13].
*   **Biggest Differentiator for Application Builders:** Being exceptionally good at orchestration – bringing together tools, data, and multiple model calls, and quickly evaluating and improving these systems [00:41:02].
*   **Underexplored Applications:** Scientific research, where a step-change in speed is anticipated [00:41:41]. Academia needs the "right interface" to drive adoption [00:42:14]. Robotics is also a promising area [00:42:19].
*   **Model Progress:** Progress will be *more* than last year, driven by a feedback loop where models teach how to improve them with better data [00:42:33].
*   **Excited AI Startup Categories:** Travel, despite being entrenched, is ripe for an AI travel agent product [00:42:51]. Personal productivity tools like Granola (for meeting summaries) are also highly valued [00:43:20].

For more information, listeners can visit [platform.openai.com/docs](https://platform.openai.com/docs) or check the OpenAI Devs channel on Twitter and the community forum [00:43:47].