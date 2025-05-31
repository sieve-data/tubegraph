---
title: The evolution and impact of OpenAIs models
videoId: gwgDDkLFvd0
---

From: [[redpointai]] <br/> 

Logan Kilpatrick, OpenAI's first AI hire, offers insights into the evolution and impact of OpenAI's models and strategic decisions. His role at OpenAI focuses on enhancing the developer platform <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Personal and Professional Application of ChatGPT

Kilpatrick frequently uses ChatGPT for coding, particularly in web development, an area where he lacks classical expertise. He notes that roughly half of the features he ships are based on 90% ChatGPT-generated code, providing him significant freedom beyond his typical capabilities <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## OpenAI's Product Suite and Future Outlook

OpenAI's product offerings are extensive and widely used. Kilpatrick believes the [[developers_approach_to_ai_models_and_agents | Assistants API]] will become a long-term significant product, even though it's currently in beta and requires further development, such as improved RAG strategies and customization <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The ability to use tools like Code Interpreter via the API is particularly exciting <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

While [[evolution_of_ai_models_and_infrastructure | multimodal]] capabilities (Vision model) are promising, they are still early. The current Vision model is akin to the "GPT-3.5 Vision era," requiring more detailed understanding of spatial relationships for complex use cases to become robust <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Model Selection and Fine-tuning Strategies

For developers, choosing between GPT-3.5 Turbo and GPT-4 depends on the complexity of the prompt. GPT-3.5 Turbo is highly capable for simpler tasks, but GPT-4 excels with requests involving more than three or four instructions <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. With recent price drops, using GPT-4 has become more affordable <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

Fine-tuning GPT-3.5 can achieve GPT-4 level performance, along with token savings and improved prompt engineering <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Function calling, a crucial use case, also benefits significantly from fine-tuning, potentially reducing token costs by allowing the model to "hallucinate" functions rather than paying for their tokens every time <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

## Custom Models and Data Requirements

OpenAI's custom models are designed for companies with large datasets in domains where the base model isn't already proficient, such as legal or medical fields <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. However, these models are expensive (potentially $2-3 million) and require billions of tokens of high-quality data <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

The goal is to make these learnings more accessible and affordable in the future, possibly through an API, though they will likely remain more expensive due to the process <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Despite base model improvements, there will always be a need for custom models due to specific performance needs and the ability to train on proprietary, compute-efficient datasets <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. OpenAI's research team assists customers with the machine learning expertise needed to train these models effectively <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Prioritization and Product Development at OpenAI

OpenAI faces the challenge of balancing numerous developer requests with core priorities like reliability and shipping new capabilities <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. Providing a world-class, reliable service is paramount, taking precedence over features like API key usage dashboards <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. The focus remains on productionizing research work <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

The breadth of OpenAI's offerings, including capabilities like Text-to-Speech, which could be standalone companies, showcases their extensive product development <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## [[open_source_models_versus_proprietary_ai_models | Open Source Models versus Proprietary AI Models]]

While some prefer [[open_source_ai_models_and_limitations | open source models]] for ownership of weights and IP, Kilpatrick believes OpenAI's models will consistently outperform them due to the immense scale and engineering effort involved <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. He highlights that while open-source models like Llama offer more [[customization_and_open_source_in_ai_models | customization]] and fine-tuning options (like RLHF) not yet available through OpenAI's standard API, this may change in the future <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

Despite the narrative that open source models might offer cheaper alternatives for "GPT-3 level" capabilities, OpenAI's continuous price slashing and superior developer experience (DevX), which removes the hassle of GPU allocation and spinning up services, remain compelling advantages <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>.

## Tools and Ecosystem

Developers commonly use observability products to monitor API usage and logs, as OpenAI's dashboard capabilities are still evolving <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Tools like LlamaIndex, LangChain, and Haystack are widely used for building features <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. Enterprises often rebuild infrastructure themselves to avoid dependencies on venture-backed open-source projects, though this might change as the ecosystem matures <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

A significant challenge for developers using LLMs is evaluation ("evals"). Kilpatrick sees a market opportunity for companies dedicated to solving the complex and time-consuming problem of robustly evaluating models, especially given the rapid iteration cycle of models <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## The Future of Agents and Internet Interaction

OpenAI's journey with agents evolved from "Plugins," which had ambitious goals but faced limitations in product strategy, security, and integration, to the more robust "GPTs" <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>. GPTs address many previous challenges by allowing seamless integration of browsing, Code Interpreter, and custom actions <a class="yt-timestamp" data-t="00:27:02">[00:27:02]</a>. The upcoming GPT store aims to solve discoverability issues that plagued Plugins <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

Currently, GPTs are primarily used for sharing prompts, indicating the continued value of prompt engineering <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>. Kilpatrick envisions text-first assistant experiences, such as AI assistants integrated with Twilio or email, bringing the ChatGPT experience to existing workflows <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.

Regarding agents taking broader actions, significant Internet infrastructure work is needed to authenticate humans versus AI agents and prevent misuse <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. OpenAI has placed limitations on agents due to safety concerns and the current lack of robust infrastructure <a class="yt-timestamp" data-t="00:37:57">[00:37:57]</a>. The "hype cycle" around agents, while intense, has positively forced the industry to consider and address these complex problems <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.

## Impactful Implementations and Future Potential

Kilpatrick highlights TLDraw, which converts sketches into functional apps using various OpenAI components, as an exemplary implementation <a class="yt-timestamp" data-t="00:39:56">[00:39:56]</a>. He also finds generative art and DALL-E 3 empowering, enabling creative expression <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>. A desired future capability is the ability to edit DALL-E outputs, like text in images, to bridge the gap between AI generation and user refinement <a class="yt-timestamp" data-t="00:44:19">[00:44:19]</a>. Current Vision models struggle with precise spatial relationships and OCR for structural understanding <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>.

## Challenges for LLM Adoption in 2024

The main objections for enterprises and developers adopting LLMs are robustness, reliability, and latency <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>. Companies often need to use third-party tools for guardrails to ensure production-level confidence <a class="yt-timestamp" data-t="00:45:30">[00:45:30]</a>. Latency, where users wait several seconds for a response, is a significant barrier for many use cases, and OpenAI is actively working to reduce this through model development and increased GPU allocation <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>.

## [[evolution_of_ai_models_and_infrastructure | Evolution of the OpenAI Team]]

OpenAI has experienced rapid growth, with the team expanding significantly from a small group handling the entire API engineering to specialized teams for developer experience, API experience, capabilities, fine-tuning, and enterprise offerings <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. This growth allows them to address more of the "basic things" customers are asking for <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>. Kilpatrick notes that recent internal challenges have inadvertently unified the team and reinforced their core mission <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>.

## Advice for AI-Curious Individuals

For those new to AI, Kilpatrick recommends:
*   **Audit daily tasks**: Identify mundane or disliked tasks that AI could automate or improve <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>.
*   **Amplify passions**: Use AI to enhance areas you are passionate about, like art or coding <a class="yt-timestamp" data-t="00:54:38">[00:54:38]</a>.
*   **Developers**: Embrace tools like ChatGPT and GitHub Copilot as "table stakes" to significantly amplify capabilities, often outperforming even highly skilled individuals without AI assistance <a class="yt-timestamp" data-t="00:55:04">[00:55:04]</a>.

He emphasizes making AI integration a habit, using tools like ChatGPT first in workflows to understand its transformative potential <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. The widespread adoption of AI by major companies like Apple and Google (e.g., with Gemini) will further expose consumers to its possibilities <a class="yt-timestamp" data-t="00:57:22">[00:57:22]</a>.

## [[impact_of_open_source_models_in_ai_development | The Future of AI Models and Open Source Development]]

OpenAI's strategy appears to be building an "AWS of AI," offering a comprehensive suite of tools from base models to fine-tuning, RHF, and various development steps <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>. This broad approach aims to make their solutions stickier by encouraging users to leverage their own data within the OpenAI ecosystem <a class="yt-timestamp" data-t="01:01:09">[01:01:09]</a>. The ongoing question remains where opportunities for specialized startups will emerge within this comprehensive platform, similar to how Snowflake carved out a niche in data warehousing despite AWS offerings <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. Observability and monitoring are identified as areas where third-party tools currently fill a gap <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>.

The [[the_future_of_ai_models_and_open_source_development | role of opensource models and partnerships in AI advancement]] is dynamic, with Logan Kilpatrick noting that while open source models offer more control and customization today, OpenAI aims to provide similar capabilities within their ecosystem. The continuous price cuts by OpenAI also make their proprietary models competitive against the cost advantages of open-source alternatives <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.