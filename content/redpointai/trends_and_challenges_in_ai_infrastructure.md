---
title: Trends and challenges in AI infrastructure
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

The field of AI infrastructure is rapidly evolving, with new tools and paradigms emerging to support the development and deployment of intelligent agents. This article explores current trends, persistent [[Challenges and opportunities in AI integration | challenges]], and future directions in AI infrastructure development, drawing insights from recent discussions.

## The Evolving Landscape of AI Agents and Their Infrastructure Needs

Initially, AI agents were primarily observed within specific platforms like ChatGPT, where users actively sought out the service for deep research or operational tasks <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The most exciting development is the dispersal of these agentic capabilities, driven by the release of underlying models and APIs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The goal is for these agents to become deeply embedded in everyday products, automating tasks like form filling or research by performing clicks and gathering information <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

A key aspect of this evolution is the increasing interaction between agents and the web, and even between agents themselves <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. A significant shift in how agents access information from the web is the "chain of thought" tool calling process <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This allows models to gather information, reflect, reconsider, and even open multiple web pages in parallel to save time <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. In the near future, web page extraction could be replaced by other agents, functioning as endpoints that provide useful information for decision-making <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This seamless embedding of tool calling will happen across the internet, private data, and private agents <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Enterprises should proactively build for this "agentic future" by creating internal AI agents to solve specific business problems <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The Agents SDK supports this by enabling multi-agent architectures, such as swarms of agents handling different aspects of customer support automation (refunds, billing, FAQs, escalation) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Evolution of Agentic Products and Capabilities

The nature of agentic products has evolved rapidly:
*   **2024:** Products typically involved clearly defined workflows with fewer than 10-12 tools, moving through orchestrated steps <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **2025:** Products like "deep research" demonstrate models using "chain of thought" to call multiple tools within their reasoning process, capable of self-correction (taking a U-turn) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This moves away from deterministic workflow building <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. OpenAI's reinforcement fine-tuning techniques are key to enabling this for developers <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **Next Step:** The immediate future aims to remove the constraint on the number of tools, allowing agents to access and figure out the right tool from hundreds <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This will enable agents to leverage their "superpower" of compute and reasoning across vast tool trajectories <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

Another critical [[Scaling and Innovation in AI Infrastructures | trend]] is increasing the available runtime for models from minutes to hours or days, which is expected to yield much more powerful results, akin to a human working on a task for a day <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

## [[Challenges and opportunities in AI infrastructure development | Challenges and Opportunities in AI Infrastructure]]

### Grading and Evaluation
A significant [[Challenges and strategies in AI deployment | challenge]] in AI infrastructure is the "productization" of grading and task generation for model fine-tuning <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. While internal tools exist to steer models using tasks and graders for specific domains (like medical or legal), creating these is currently challenging and requires significant iteration <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. The ultimate goal is to make this process 10 times easier for developers <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

> [!NOTE] Key Challenge:
> The biggest problem to be solved in the coming year is the productization of grading and task generation for fine-tuning models to specific domains <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### Computer Use Models
Computer use models are proving to be surprisingly versatile. While initially envisioned for automating legacy applications without APIs (e.g., manual tasks in the medical domain across multiple applications) <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>, they are also used for tasks like research on Google Maps, including Street View, where traditional APIs might be hard to leverage <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. These models are particularly well-suited for domains that don't map neatly to JSON, requiring a combination of vision and text ingestion <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.

A key [[Challenges and future directions for AI in various domains | challenge]] in the computer use space is securely and reliably deploying and observing these virtual machines (VMs) within enterprise infrastructure <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. The models are expected to improve rapidly, and the infrastructure to support various environments (e.g., iPhone screenshots, Android, different Ubuntu flavors) will be crucial <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

### API Design and Developer Experience
OpenAI's approach to API design emphasizes "APIs as ladders," making simple tasks easy while allowing for deeper customization for greater reward <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. For example, file search is easy to use out-of-the-box, but developers can tweak parameters like chunk size, metadata filtering, or re-rankers for specific use cases <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>. The new responses API reflects this, offering a simple single endpoint initially, with options to opt into features like conversation storage (threads) or model configurations (assistants) as needed <a class="yt-timestamp" data-t="00:24:27">[00:24:27]</a>.

Lessons from previous APIs, like the Assistants API, highlight the importance of tool use (especially file search) for market fit, but also the need for flexibility in context management, allowing developers to provide their own context per turn <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. The new responses API aims to combine the multi-output and tool use capabilities of Assistants with the ease of use of chat completions <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>.

### Opportunity for Standalone AI Infrastructure Companies
While OpenAI aims to provide a "one-stop shop" for core LLM functionalities (data search, internet search) <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>, there remains a significant market for standalone AI infrastructure companies <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>. These companies can focus on:
*   **Low-level, infinitely flexible APIs:** Offering powerful foundational tools that cater to highly specific or custom needs <a class="yt-timestamp" data-t="00:28:01">[00:28:01]</a>.
*   **Verticalized AI infra:** Building specialized VMs for specific industries, such as coding AI startups that need rapid code testing and VM spin-down <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a>.
*   **LLM Ops:** Companies helping developers manage prompts, billing, and usage across multiple models and providers (e.g., OpenRouter) <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>.

## Future Directions and Recommendations

### Key Problems for Developers
The top problems still facing developers working with models include:
1.  **Tool Ecosystem:** Building a robust tool ecosystem on top of foundational blocks <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>.
2.  **Computer Use VM Space:** Securely and reliably deploying and observing virtual machines for computer use models in enterprise environments <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>.
3.  **Model Reliability and Speed:** Developing smaller, faster models that are highly effective at tool use and can perform quick classifications and guardrailing <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>.

### Differentiators for Application Builders
In the long term, the biggest differentiator for application builders will be the ability to "orchestrate" <a class="yt-timestamp" data-t="00:41:02">[00:41:02]</a>. This involves skillfully combining tools and data with multiple model calls, whether through reinforcement fine-tuning for chain of thought or by chaining together multiple LLMs <a class="yt-timestamp" data-t="00:41:08">[00:41:08]</a>. The ability to do this quickly, evaluate, and continuously improve will be a critical skill <a class="yt-timestamp" data-t="00:41:26">[00:41:26]</a>.

### Recommendations for Enterprises
For any enterprise or consumer CEO, the advice for navigating the agentic future is to **start exploring** <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.
*   Experiment with frontier models and computer use models <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.
*   Identify internal workflows that can be automated using multi-agent architectures <a class="yt-timestamp" data-t="00:36:52">[00:36:52]</a>.
*   Focus on getting programmatic access to internal tools, as this is often 90% of the work in automating workflows <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>.
*   Encourage employees to identify their least favorite daily tasks and explore ways to automate them using AI <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>.

The progress in models is expected to accelerate even more this year, partly due to a feedback loop where models help teach how to improve them with better data <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. The key is to make the entire flywheel from evaluation to production and fine-tuning significantly simpler <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>.

For more information on OpenAI's APIs and developer tools, visit [platform.openai.com/docs](https://platform.openai.com/docs), follow OpenAI Devs on Twitter, or check the community forum at [community.openai.com](https://community.openai.com) <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.