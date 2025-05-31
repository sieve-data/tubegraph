---
title: Role of custom models and enterprise AI integration
videoId: gwgDDkLFvd0
---

From: [[redpointai]] <br/> 

Logan Kilpatrick, OpenAI's first AI hire, discussed the evolving landscape of AI adoption within enterprises, highlighting the role of custom models and the strategic integration of AI platforms.

## Custom Models and Fine-tuning

The ability to fine-tune models like GPT-4 was announced at DevDay, though it was rolled out to those who had already attempted fine-tuning GPT-3.5 turbo <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Fine-tuning GPT-3.5 can achieve GPT-4 level performance with proper prompt engineering and token savings <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. This requires significant effort in crafting prompts, especially when dealing with more than three or four instructions <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

### When to use Custom Models

[[Building custom AI models for enterprises | Custom models]] are most beneficial for companies with a large amount of specialized data in domains where the base model isn't already proficient, such as the legal or medical sectors <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Building these models is currently a significant investment, costing around $2-3 million and requiring billions of tokens for training <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This makes it challenging for startups without substantial capital expenditure <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

OpenAI's custom model program involves their research teams directly assisting companies that may lack world-class machine learning expertise to train these models <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.

### Future of Custom Models

Kilpatrick believes there will always be a need for [[strategic_uses_of_ai_in_enterprises | custom models]], even as base models continue to improve and become more "steerable" <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This is because custom models can be more compute-efficient by focusing on specific, deeply relevant data and excluding unnecessary information from training sets <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. The goal is to make the custom model offering more accessible and affordable through an API in the future <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Enterprise AI Adoption and Integration

OpenAI serves a wide range of users and use cases <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Prioritization for product development focuses on providing a world-class service, which includes significant investments in reliability <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Shipping new capabilities often takes precedence due to engineering resource constraints <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. OpenAI aims to evolve into a "true Enterprise platform" by addressing rough edges like detailed dashboards, monitoring, and alerts in 2024 <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This aligns with [[enterprise_ai_adoption_challenges_and_solutions | enterprise AI adoption challenges and solutions]].

### OpenAI vs. Open Source Models

Users often choose open-source models for full ownership of weights and IP, which is critical for some business use cases <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Open-source models like Llama offer more customization options with fine-tuning beyond standard OpenAI offerings <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

However, Kilpatrick believes OpenAI's models will generally remain superior due to the immense cost and engineering effort required for training very large models <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. The ease of use of OpenAI's API, which removes the need to worry about GPU allocation or complex setups, also provides significant developer experience value <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. OpenAI plans to support more fine-tuning and training techniques, like RLHF, in the future <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

### Tools and Integration in Enterprise AI

When enterprises [[integration_of_ai_and_data_platforms_in_enterprises | integrate AI]], they commonly use:
*   **Observability products:** These tools allow developers to monitor API usage, spend per API key, and view logs and requests <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. While OpenAI acknowledges the need for such features, they currently often take a backseat to shipping new capabilities <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.
*   **LLM orchestration frameworks:** Tools like LlamaIndex and LangChain are widely used for building features <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. Haystack and Prompt Layer are also noted <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
*   **Custom infrastructure:** Many technically sophisticated companies prefer to rebuild much of this infrastructure themselves rather than relying on third-party dependencies, especially given the nature of venture-backed open-source companies <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

### Key Challenges in Enterprise AI Deployment

The main objections and blocks for enterprises in deploying LLMs are:
1.  **Robustness and Reliability:** Enterprises often need to use third-party tools like Guardrails AI or other LLM companies for compliance and to ensure confidence in production environments <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>. OpenAI aims to solve many of these problems upstream on their platform <a class="yt-timestamp" data-t="00:45:43">[00:45:43]</a>. This is a core part of [[challenges_and_strategies_in_enterprise_ai_deployment | challenges and strategies in enterprise AI deployment]].
2.  **Latency:** Many use cases cannot tolerate waiting 7 seconds for a response <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>. Reducing inference time is a continuous internal development focus, with a goal that latency will no longer be an objection by late 2024 <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>. Instant responses are crucial for maintaining user flow in creative tasks <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>.

> "LLMs are like a clone of human thought, and in many ways, it doesn't move at the speed of thought, and I think that's that can be so jarring in a lot of a lot of experiences." <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>

## OpenAI's Product Strategy and Future Outlook

OpenAI's product footprint is broad, serving many user types and use cases <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. They prioritize shipping new capabilities and investing in reliability <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

### Evolution of Products

*   **Plugins:** Initially framed as a product release, plugins were more of a "research preview" with an ambitious mission <a class="yt-timestamp" data-t="00:25:10">[00:25:10]</a>. They faced limitations due to resource constraints and security/privacy concerns, such as taking consequential actions or needing user consent <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. Discoverability was also a significant challenge <a class="yt-timestamp" data-t="00:27:23">[00:27:23]</a>.
*   **Assistants API and GPTs:** These offerings have solved many of the problems previously encountered with plugins <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>. They allow combinations of browsing, code interpreter, and custom actions, offering a much better interface <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. The upcoming GPT Store is expected to resolve discoverability issues <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. Current use cases for GPTs largely revolve around sharing prompts <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.
*   **Multimodal AI:** Kilpatrick anticipates 2024 to be the "year of multimodal" <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. While early for vision use cases, he believes that once the models make a jump in understanding positional relationships between objects (similar to the leap from GPT-3.5 to GPT-4), many more use cases will be unlocked <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   An example of a successful multimodal application is TLDraw, which converts user drawings into functional apps, showcasing the orchestrated use of various OpenAI tools like Vision <a class="yt-timestamp" data-t="00:39:48">[00:39:48]</a>.

### [[Enterprise AI deployment models | Deployment Models]] and Strategy

OpenAI's strategy, similar to Microsoft's Co-pilot, is to be present where customers and users already are, rather than solely relying on users visiting chat.openai.com <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. This includes embedding AI experiences directly into existing workflows and applications, like text messaging or email <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>.

Kilpatrick suggests a need for a "text-first assistant experience" that can integrate with platforms like Twilio, bringing AI assistance to surface areas where users already work, without requiring them to navigate to new websites or learn new habits <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.

### Overhyped and Underhyped in AI

*   **Overhyped:** Prompt engineering <a class="yt-timestamp" data-t="00:48:15">[00:48:15]</a>. While useful, Kilpatrick believes the fundamental nature of prompt engineering—communication—will eventually be abstracted away as models become better at understanding imprecise human requests, similar to DALL-E 3's revised prompts <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
*   **Underhyped:** Observability <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. Understanding everything happening with models is crucial for developers <a class="yt-timestamp" data-t="00:48:27">[00:48:27]</a>.
*   **Unexpected Success:** Function calling <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>. This feature, which enables many interesting production use cases, was an unexpected but significant development <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.

The broader AI ecosystem, including major players like Google with Gemini, is seen as beneficial for consumers, driving innovation and expanding awareness of AI's possibilities <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>. This contributes to the broader discussion around [[enterprise_and_consumer_ai_trends | enterprise and consumer AI trends]].

## Getting Started with AI for Developers and Enterprises

Kilpatrick recommends developers and enterprises conduct an audit of their daily tasks to identify processes they dislike or wish to improve <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>. For developers, using tools like ChatGPT and GitHub Copilot is considered "table stakes" to amplify capabilities <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>. He suggests integrating AI into daily workflows to make it a habit, which helps in understanding how the technology will impact life and career <a class="yt-timestamp" data-t="00:56:03">[00:56:03]</a>.

He emphasizes that companies like Apple and Google have an important role in educating a wider audience about AI's potential by integrating it into familiar experiences like Siri <a class="yt-timestamp" data-t="00:57:25">[00:57:25]</a>.

## Conclusion

OpenAI aims to be the "AWS of AI," offering a comprehensive platform that covers every step a developer needs, from models and fine-tuning to specific training techniques <a class="yt-timestamp" data-t="00:59:22">[00:59:22]</a>. The focus remains on continually building out capabilities while striving for affordability and accessibility.