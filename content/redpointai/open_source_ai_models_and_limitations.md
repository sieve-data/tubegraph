---
title: Open source AI models and limitations
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

In an episode of the Unsupervised Learning AI podcast, hosts Jacob Efron and Pat Chase were joined by Omj, founder of Replit, to discuss the landscape of AI models, focusing on the current state and perceived limitations of open source models <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Replit, a company valued at over a billion dollars, is at the forefront of integrating AI into coding solutions <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Reality of Open Source AI Models

Omj challenges the notion that today's "open source" AI models are truly open, likening their current state to providing Linux source code without a compiler or only a binary <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>. He argues that if a model cannot be reproduced, it is not truly open source <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>. This raises questions about long-term dependency:
> "If you're using open source models, you're dependent on the Goodwill of Zuck to continue to to to push out you know Llama 2, 3, 4, 5" <a class="yt-timestamp" data-t="00:32:29">[00:32:29]</a>.

This dependency means companies are essentially betting their business on external goodwill, which Omj finds strategically precarious <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. He emphasizes the need for a truly [[the_future_of_ai_models_and_open_source_development | open source]] project that allows for contributions and has a functional open source flywheel <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>.

### Data as the Source Code

Omj highlights that current large language models (LLMs) are fundamentally a function of the data they are fed <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The real power of LLMs lies in interpolating different data distributions <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. When training a model, the data becomes the source code itself <a class="yt-timestamp" data-t="00:35:12">[00:35:12]</a>.

A critical limitation of current [[open_source_models_versus_proprietary_ai_models | open source models versus proprietary AI models]] is the lack of clarity regarding their training process and underlying data <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. This presents a significant security risk, as "backdoors" or hidden functionalities could be built into models and remain undetected if the training data and process are not fully transparent <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>.

Furthermore, Omj suggests that the supply of high-quality, truly [[open_source_models_versus_proprietary_ai_models | open source]] tokens for training models might be dwindling <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. While models like GPT-4 are trained on vast amounts of internet code and heavily annotated coding data, open source models often rely on permissive GitHub repositories <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. The challenge is finding sufficient and diverse "coding adjacent reasoning things" like scientific or legal data to continue improving coding capabilities <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

## Replit's Approach: Building Proprietary Models

Replit's decision to build its own model, rather than solely relying on commercial APIs or [[open_source_models_versus_proprietary_ai_models | open source models]], was driven by specific needs:
*   **Low Latency**: Commercial models, even those used by partners like Copilot, can be too slow. Replit prioritized sub-second response times for a seamless user experience, which is crucial for in-editor code suggestions <a class="yt-timestamp" data-t="00:28:07">[00:28:07]</a>.
*   **Cost Efficiency**: Integrating AI features into a free product tier meant commercial model costs were prohibitive <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. Training their own 3-billion parameter model cost approximately $100,000, which is not a huge capital expenditure compared to ongoing inference costs from commercial providers <a class="yt-timestamp" data-t="00:29:35">[00:29:35]</a>.
*   **Small Models are Capable**: Replit was early to realize that smaller models could be highly capable for specific tasks, especially with proper productionization <a class="yt-timestamp" data-t="00:29:17">[00:29:17]</a>. This allowed them to tailor the model to their needs more effectively.
*   **Strategic Control**: Building in-house capability fosters internal talent and reduces external dependency <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>.

Despite building their own core model, Replit still uses commercial models for other use cases, such as general-purpose chat features, where it doesn't make sense to train a custom model <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>. This pragmatic approach focuses on solving customer problems and running the numbers to determine the best solution <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.

## The Future Landscape

The future of AI models is still fluid. While a year ago, Omj might have predicted a strong reliance on fine-tuning [[open_source_models_versus_proprietary_ai_models | open source models]], his current view is that the commercial side is currently ahead <a class="yt-timestamp" data-t="00:33:13">[00:33:13]</a>. Companies like OpenAI and Anthropic are developing robust fine-tuning and custom model businesses, providing services that address specific customer needs <a class="yt-timestamp" data-t="00:34:04">[00:34:04]</a>.

However, the rapid progress in [[the_evolution_and_impact_of_openais_models | OpenAI's models]] and [[role_of_opensource_models_and_partnerships_in_ai_advancement | opensource models and partnerships]] with companies like Meta's Code Llama (which claims to match GPT-4 on benchmarks, though "the vibes may be off" <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>), suggests that the [[impact_of_open_source_models_in_ai_development | open source]] landscape is quickly catching up <a class="yt-timestamp" data-t="01:10:21">[01:10:21]</a>.

Ultimately, the decision to build, fine-tune, or rely on commercial APIs will depend on specific strategic considerations, the problem being solved, and available resources and talent <a class="yt-timestamp" data-t="00:30:24">[00:30:24]</a>.