---
title: ChatGPT use cases and applications
videoId: gwgDDkLFvd0
---

From: [[redpointai]] <br/> 

ChatGPT, celebrating its one-year anniversary, has undergone a significant transformation since its launch, evolving from a novel conversational AI to a widely used tool for developers and everyday users alike <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. Logan Kilpatrick, OpenAI's first AI hire, shared insights into its diverse applications and the future direction of OpenAI's offerings <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Personal and Developer Use Cases

Logan Kilpatrick primarily uses ChatGPT for coding, particularly to enhance OpenAI's developer platform <a class="yt-timestamp" data-t="00:54:56">[00:54:56]</a>. Not being a web development expert, he relies on ChatGPT to translate his ideas into code, estimating that about 90% of the features he ships incorporate ChatGPT-generated code <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This capability grants engineers greater freedom to exceed their usual capabilities without extensively studying documentation <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

He emphasizes that every developer should use tools like ChatGPT and GitHub Copilot, considering them "table stakes" for modern development. He believes an average developer using AI tools can outperform even the best unassisted developers <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

## OpenAI Product Offerings and Future Directions

OpenAI offers a broad suite of products, with continuous [[development_and_improvements_of_gpt_41 | development and improvements of GPT-4]] being a core focus <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### Assistants API

The Assistants API is predicted to be a significant long-term product for OpenAI <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>. It simplifies the process for developers by handling much of the underlying complexity, providing tools like the Code Interpreter and enabling robust RAG (Retrieval-Augmented Generation) strategies <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. The ability to use Code Interpreter via API is a major recent advancement <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

### Multimodal Capabilities (Vision)

While still in early stages, multimodal capabilities, particularly vision models, are expected to grow significantly <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Current limitations include precise understanding of positional relationships between objects in an image <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Overcoming this will unlock many more use cases, similar to the leap from GPT-3.5 to GPT-4 <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. Examples include enhanced capabilities for design tools like Canva or improved OCR for documents like spreadsheets and receipts <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.

### Fine-Tuning

*   **GPT-3.5 Turbo**: This model is capable for tasks with three or four instructions <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>. With fine-tuning and prompt engineering, it can achieve GPT-4 level performance, offering token savings <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **GPT-4**: Recommended for more complex requests with multiple instructions <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. Price drops post-DevDay have made it more affordable <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.
*   **Function Calling**: A significant use case for fine-tuning. Developers can fine-tune GPT-3.5 for function calling, even "hallucinating" functions to reduce token costs associated with passing function definitions in prompts <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.

### Custom Models

Custom models are tailored for specific domains where base models might lack deep access to data, such as the [[ai_applications_in_legal_and_education | legal space]] or medical field <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>. These models require massive datasets (billions of tokens) and significant investment ($2-3 million) <a class="yt-timestamp" data-t="08:49:00">[08:49:49]</a>. OpenAI's research teams assist companies in training these models <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. While base models will improve, the need for custom models is expected to persist due to the desire for specialized, compute-efficient models optimized for specific data <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. The goal is to make custom model offerings more accessible and affordable via API in the future <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.

## Prioritization and [[enterprise_adoption_and_use_cases_for_ai | Enterprise Adoption]]

OpenAI's product prioritization balances user requests (like API key usage dashboards) with core principles like reliability and shipping new capabilities <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. Ensuring a world-class, reliable service is paramount <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>. Productionizing research often takes precedence over feature development due to resource constraints <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>. The aim is to build a true [[enterprise_adoption_and_use_cases_for_ai | Enterprise platform]] by 2024 <a class="yt-timestamp" data-t="13:29:00">[13:29:00]</a>.

## Open Source vs. OpenAI Models

Kilpatrick believes OpenAI's models will consistently outperform open-source models due to the sheer scale and engineering effort involved <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>. However, open-source models offer intellectual property ownership and greater customization like RLHF (Reinforcement Learning from Human Feedback), which is not yet a standard OpenAI offering <a class="yt-timestamp" data-t="15:46:00">[15:46:00]</a>. The convenience and lower barrier to entry (no GPU allocation worries) of OpenAI's API are significant advantages over self-hosting open-source models <a class="yt-timestamp" data-t="17:14:00">[17:14:00]</a>.

## Complementary Tools and Ecosystem

Developers commonly use observability products to monitor API usage and logs, as OpenAI's dashboard capabilities are still developing <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>. Orchestration frameworks like LlamaIndex, LangChain, and Haystack are widely used for building features <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>. Some [[enterprise_adoption_and_use_cases_for_ai | enterprises]] adopt these tools, while others with high technical sophistication opt to rebuild infrastructure in-house to avoid third-party dependencies <a class="yt-timestamp" data-t="19:46:00">[19:46:00]</a>.

## Startup Opportunities

Logan highlights the "evals" (evaluation of LLMs) problem as a significant [[ai_infrastructure_and_startup_opportunities | startup opportunity]] <a class="yt-timestamp" data-t="21:52:00">[21:52:00]</a>. Assessing how new models impact specific use cases is a fundamental and time-consuming challenge that currently lacks a compelling product solution <a class="yt-timestamp" data-t="22:00:00">[22:00:00]</a>.

## Evolution of Agents and the Internet

OpenAI's journey with agents began with plugins, which, while ambitious, faced limitations in security, privacy, and resource allocation <a class="yt-timestamp" data-t="24:55:00">[24:55:00]</a>. These challenges are largely addressed by GPTs (Assistants API), which offer a much-improved interface, allowing combinations of browsing, Code Interpreter, and custom actions <a class="yt-timestamp" data-t="26:39:00">[26:39:00]</a>. The upcoming GPT Store aims to resolve discoverability issues that plagued the plugin store <a class="yt-timestamp" data-t="27:19:00">[27:19:00]</a>.

Current use of GPTs primarily revolves around sharing prompts, demonstrating the continued value of prompt engineering <a class="yt-timestamp" data-t="27:47:00">[27:47:00]</a>. The future of prompt engineering is seen as evolving, with models providing a "layer of translation" to refine user requests, reducing the need for verbose manual prompting <a class="yt-timestamp" data-t="29:13:00">[29:13:00]</a>.

A desired future application is a text-first assistant experience, integrated into existing workflows like text messages (e.g., via Twilio) and email <a class="yt-timestamp" data-t="30:23:00">[30:23:00]</a>. This would allow AI assistance without forcing users into new applications, leveraging familiar communication methods <a class="yt-timestamp" data-t="31:58:00">[31:58:00]</a>.

The widespread deployment of autonomous agents on the internet requires significant infrastructure work to authenticate humans versus AI agents <a class="yt-timestamp" data-t="35:49:00">[35:49:00]</a>. This development is expected to take years, potentially accelerated by a consortium of major tech companies <a class="yt-timestamp" data-t="37:07:00">[37:07:00]</a>. OpenAI is cautiously advancing agent capabilities to ensure responsible use and robust product experiences <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.

## Notable Implementations and Future Outlook

TLDraw, which converts sketches into functional applications using OpenAI models, is cited as a perfect example of making the technology accessible and enabling real-world applications <a class="yt-timestamp" data-t="39:48:00">[39:48:00]</a>. Similarly, generative art models like DALL-E have empowered creative expression by allowing users to explore possibilities beyond their manual artistic skills <a class="yt-timestamp" data-t="41:17:00">[41:17:00]</a>.

Major blocks for greater [[enterprise_adoption_and_use_cases_for_ai | enterprise adoption]] include robustness and reliability, often requiring third-party guardrails <a class="yt-timestamp" data-t="45:08:00">[45:08:00]</a>. Latency is another critical issue, as many use cases cannot tolerate delays of several seconds for responses <a class="yt-timestamp" data-t="46:11:00">[46:11:00]</a>. The goal is to make models significantly faster by the end of 2024 <a class="yt-timestamp" data-t="46:37:00">[46:37:00]</a>.

The broader [[AI adoption and user behavior | AI ecosystem]] sees Google Gemini as a positive step, pushing innovation and making AI capabilities more accessible to consumers <a class="yt-timestamp" data-t="57:52:00">[57:52:00]</a>. The future will likely see more integration of AI assistants into existing applications, rather than users always navigating to dedicated AI platforms <a class="yt-timestamp" data-t="34:44:00">[34:44:00]</a>. Companies like Apple and Google are seen as having an important role in driving mainstream adoption by seamlessly integrating AI into their widely used ecosystems <a class="yt-timestamp" data-t="57:22:00">[57:22:00]</a>.

---

For more information on OpenAI's API offerings, visit [platform.openai.com](https://platform.openai.com) <a class="yt-timestamp" data-t="58:13:00">[58:13:00]</a>.