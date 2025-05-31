---
title: AI coding assistants and their uses
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

**AI coding assistants** are emerging as powerful tools in software development, with over a million paying users for products like [[ai_in_software_development_with_github_copilot | GitHub Copilot]] alone <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. These tools represent one of the best use cases for AI seen to date <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Sourcegraph's Cody: An AI Coding Assistant

Sourcegraph offers an [[ai_in_software_development_with_github_copilot | AI coding assistant]] called Cody, which provides various functionalities to developers <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>:
*   **Inline completion**: Completing thoughts as a developer types code in the editor <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Chat**: Allowing users to ask high-level questions about code, generate code snippets, or perform specific actions <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Examples include writing docstrings for functions or generating unit tests <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Context awareness**: Cody's differentiator is its ability to integrate context and awareness from the user's code base, similar to how Sourcegraph's code search engine provides context to human developers <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This means the AI is aware of specific frameworks, libraries, and production environments, moving beyond generic open-source examples <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Retrieval Augmented Generation (RAG)**: Cody heavily utilizes RAG to connect queries to the customer's actual code base <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Development Philosophy

Sourcegraph's approach to building [[AI coding tools and market dynamics | AI products]] emphasizes simplicity and iterative improvement:
*   **"Dumb thing first"**: The company prioritizes the simplest solution that provides user value, like leveraging classical keyword search for RAG in the early days <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>, <a class="yt-timestamp" data-t="00:52:05">[00:52:05]</a>. This allows for rapid iteration without the overhead of extensive data gathering or complex model training <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>.
*   **Model selection**: Users are given the freedom to choose among different models (e.g., GPT-4, Claude 3, Mixtral) in Cody's chat view, allowing them to find what works best for their use case <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. This also helps in gathering diverse user feedback for product improvement <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   **Fine-tuning**: While initially focusing on RAG, Sourcegraph is now implementing fine-tuning for specific use cases, particularly for language-specific code generation where general models may perform less effectively (e.g., Rust, Ruby, MATLAB) <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.
*   **Code quality control**: Sourcegraph plans to allow engineering leaders to control which code is used as context for automated generation, enabling them to improve overall code quality <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.

## Current Landscape of AI in Coding

The current state of [[ai_in_software_development_with_github_copilot | AI in software development]] is focused on "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. These are tools that speed up the frequent, repetitive tasks developers perform daily, such as writing common functions, auto-completing code, or generating boilerplate <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

### The Shift Towards Automation

While "inner loop" tasks are well-supported, the next frontier for [[ai_advancements_in_coding_and_software_engineering | AI advancements in coding and software engineering]] is multi-step, bot-driven development, where AI agents drive the development process with humans advising <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. This involves:
*   **Trial and error**: AI agents trying different approaches, observing results, and learning from mistakes to refine code changes <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Virtual execution environments**: Tools need to support virtual environments to allow AI to make and test code changes and observe outcomes <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Improved context fetching**: The ability to quickly retrieve and integrate relevant code context is crucial for reducing the number of cycles an AI needs to reach a correct solution, making automation more efficient and cost-effective <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Impact of Model Advancements and Context Windows

[[ai_advancements_in_coding_and_software_engineering | Advancements in large language models]] (LLMs) like the transition from GPT-3.5 to GPT-4 have significantly improved the reliability of AI coding assistants, making "wow moments" more consistent <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. Larger context windows are also beneficial, as they allow more information to be incorporated into the model's answer, especially for questions involving complex concept tying <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. However, simply stuffing an entire codebase into a context window is not yet effective for complex reasoning tasks <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. The best architectures combine large context windows with tailored information retrieval mechanisms like RAG <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

## Benefits and Segmentation of Users

AI coding tools offer varied benefits depending on the developer's experience level:
*   **Junior developers**: Tend to benefit more from inline code completions, viewing them as a "pedagogical tool" that provides a starting point or median way of doing things <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>, <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. This aligns with how LLMs are good at pattern matching and generating plausible-looking answers <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   **Senior engineers**: Often prefer chat functionalities and may find inline completions disruptive if they are not consistently high quality, as they know exactly what they want to write <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>, <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. Improvements in context quality can address some of their concerns <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Production and Evaluation

Sourcegraph's approach to [[ai_production_and_evaluation_techniques | AI production and evaluation techniques]] prioritizes real-world user feedback and product metrics:
*   **User feedback**: New models like GPT-5 are immediately made available to users, allowing Sourcegraph to observe their impact on product usage metrics and gather direct feedback <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Product metrics**: For completions, key metrics include **acceptance rate** (how often users accept suggestions) and **overall volume** (how much value is being added) <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>. For explicit actions like chat or test generation, **engagement** and **overall usage** are monitored <a class="yt-timestamp" data-t="00:42:32">[00:42:32]</a>. These "authoritative metrics" are considered harder to game and directly reflect user value <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
*   **Beyond benchmarks**: Sourcegraph has sometimes chosen models not at the top of benchmark lists but that generate better results in day-to-day use, highlighting the nuance of end-user experience not captured by well-defined tests <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   **Offline benchmarks**: The company also maintains a set of offline benchmarks for new models, with an ongoing effort to build more specifically tuned benchmarks for retrieval-based models <a class="yt-timestamp" data-t="00:48:37">[00:48:37]</a>.

## Cost Considerations

Inference cost is a factor, but Sourcegraph aims to do the "bare minimum" to control costs, believing they will decrease over time <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. The focus remains on adding value. Rate limiters are primarily used to counteract abuse rather than as a primary cost-saving measure for legitimate users <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.

## Local Inference Models

There's a growing community around local inference models, allowing users to run models on their local hardware (e.g., with Ollama or LM Studio) <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>. The benefits of local inference include:
*   **Availability**: Enables usage in environments without network connectivity, like on an airplane <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
*   **Privacy**: Keeping computation contained within the local machine addresses developer concerns about data privacy <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
*   **Cost**: Potentially reduces inference costs over time <a class="yt-timestamp" data-t="00:45:26">[00:45:26]</a>.
*   **Latency**: As GPUs become faster and inference times decrease, local processing eliminates network round-trip latency, which is crucial for developers who are highly sensitive to even milliseconds of delay in their coding environment <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>.

## The Future of Software Engineering with AI

AI is set to profoundly change the role of software engineers:
*   **Job transformation**: While AI will "take your job," it will transform it into a different, potentially better, job <a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.
*   **Focus on value creation**: Currently, developers spend little time actually producing software and shipping features, with much time spent on understanding existing codebases, context acquisition, and communication overhead <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. AI can automate the "toil and drudgery," allowing engineers to focus on "magic part" – creating unique value and differentiation <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.
*   **Increased number of engineers**: The aggregate number of engineers is expected to grow, as [[ai_in_education | AI in education]] makes software literacy more widespread and puts the power of software creation into more hands <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>.
*   **Formal languages remain vital**: Despite the ability of LLMs to generate code from natural language, formal specifications and programming languages will remain crucial due to the need for precision that natural language lacks <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>.

## Market Dynamics for AI Coding Tools

The market for [[ai_coding_tools_and_market_dynamics | AI coding tools]] is vibrant and growing, shifting from a niche "Dev tools" area to a "market unto itself" <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>, <a class="yt-timestamp" data-t="01:09:31">[01:09:31]</a>.
*   **Open ecosystem**: Sourcegraph advocates for an open ecosystem that preserves freedom of choice for developers and companies regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. This contrasts with a potential future where large players vertically integrate and force users onto proprietary platforms <a class="yt-timestamp" data-t="01:12:13">[01:12:13]</a>.
*   **Open source models**: Open-source models are expected to become very widespread due to public accessibility of research and their inherent advantages like fine-tuning capabilities and deeper introspection into model attention weights <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. StarCoder, an open-source model, is Sourcegraph's primary code completion model <a class="yt-timestamp" data-t="01:20:44">[01:20:44]</a>.
*   **Building blocks**: Beyond end-user applications, companies like Sourcegraph aim to provide reusable "building blocks" (e.g., context APIs, custom command frameworks) that enable other developers to build their own AI-enabled tools and script against them <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>, <a class="yt-timestamp" data-t="01:01:11">[01:01:11]</a>.