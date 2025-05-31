---
title: AI coding tools and market dynamics
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

[[AI coding assistants and their uses | AI coding]] is one of the best use cases for [[AI advancements in coding and software engineering | AI]] observed so far, with GitHub Copilot alone having over a million paying users <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This has led to the evolution of numerous [[advancements in ai developer tools | AI tools]] in the space <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Current State of AI Coding Tools

Currently, [[AI coding assistants and their uses | AI coding tools]] primarily act as "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The "inner loop" of software development involves a developer's daily routine of figuring out how to implement a feature, writing code, testing it, and then moving to the next task <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
Key functionalities in heavy day-to-day use include:
*   **Inline completion**: Autocompleting thoughts as code is typed <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Chat interfaces**: Answering high-level questions about code or generating code for specific tasks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Specific commands**: Automating "toil" tasks such as writing docstrings or high-quality unit tests for functions <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

While these tools are effective for common or boilerplate functions, fully automated, multi-step, bot-driven development, where a human primarily advises rather than guides, is still on the horizon <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Even tools like Devin, while promising, still require human oversight and assistance for most issues <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Sourcegraph's Approach with Cody
Sourcegraph offers two main products:
1.  **Code Search Engine**: Helps human developers understand vast codebases by enabling search, navigation (e.g., go to definition, find references), and context acquisition <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
2.  **Cody**: An [[AI coding assistants and their uses | AI coding assistant]] that provides inline completion, chat capabilities, and a menu of commands for specific development actions <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

Cody's differentiator is its ability to operate with context and awareness of the user's specific codebase, moving beyond generic suggestions to provide relevant code based on internal frameworks, libraries, and production environments <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Impact of Model Advancements
Improvements in underlying models, such as the progression from GPT-3.5 to GPT-4 and Claude 3, have significantly enabled new use cases and improved reliability <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. For instance, Cody's chat function has become much more reliable, consistently leading to "wow moments" due to the models' enhanced ability to incorporate and integrate given context into working code examples <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>. Newer models can even generate an app from scratch using specific libraries and APIs with zero-shot prompting, a feat not possible with older models <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

### Role of Context Windows and RAG
Larger context windows in models are beneficial because they allow more information to be incorporated into the model's answer, especially for questions that tie together many different concepts <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. However, it's still not possible to simply "shove the entire codebase" into the context window and expect optimal results <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.

[[AI production and evaluation techniques | Retrieval Augmented Generation (RAG)]] remains critical <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. The best application architectures combine large context windows with tailored information retrieval mechanisms <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. Effective [[ai_production_and_evaluation_techniques | RAG]] requires:
*   A way to trial and error, making code changes and observing results in a virtual execution environment <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   "Really, really good context fetchers" to reduce the number of iterations needed to find a correct solution <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## Model Evaluation and User Feedback
Sourcegraph's strategy for new model releases (e.g., GPT-5) is to enable them in Cody as quickly as possible <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. They run internal benchmarks but prioritize getting models into users' hands to observe product usage metrics <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
Key product metrics for evaluation include:
*   **Acceptance rate** for code completions <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>.
*   **Overall volume** of completions <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.
*   **Engagement** for explicit features like chat or test generation <a class="yt-timestamp" data-t="00:42:33">[00:42:33]</a>.

Sourcegraph emphasizes that product metrics are the most authoritative because they reflect real user value <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. They sometimes choose models that don't top benchmarks but perform better in day-to-day use, trusting user feedback and "gut checking" over predefined benchmarks <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. This "do the dumb thing first" philosophy is crucial, especially in a fast-evolving space <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

## Beneficiaries of AI Coding Tools
There's a correlation in who benefits most from different [[AI coding assistants and their uses | AI coding tools]]:
*   **Junior developers** tend to prefer inline completions, finding them a useful "pedagogical tool" that provides a starting point <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Senior engineers** often derive more value from chat features and can find inline completions disruptive if they are not accurate enough <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
Large Language Models (LLMs) are effective at "pattern matching" or "bullshitting their way to a correct-looking answer," which is particularly helpful for less experienced users seeking common solutions <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

## Fine-tuning and Data Quality
While initially focusing on [[ai_production_and_evaluation_techniques | RAG]], Sourcegraph is now fine-tuning models for specific use cases, such as improving code generation in less common programming languages like Rust or Ruby <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>. They also developed "Cody Ignore," a feature allowing users to specify files or code sections that the AI should not use as context, enabling exclusion of sensitive or low-quality code <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. This offers engineering leaders a lever to guide code quality <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a>.

## Inference Costs and Pricing
Inference cost is a consideration, but Sourcegraph has not prioritized over-optimizing it, anticipating that costs will significantly decrease over time <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. Rate limiters are primarily used to counteract abuse rather than manage legitimate high usage <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
Sourcegraph's pricing model for both its code search engine and Cody is based on "active user per month," meaning customers only pay if a user logs in and actively uses the product <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>. This aligns incentives with customer value and avoids over-allocation of seats <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>. Cody can be used independently (free and pro tiers) or in conjunction with Sourcegraph's code search for enhanced context <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>.

## Organizational Structure for AI
Sourcegraph has a distinct team focused on the "model layer" (fine-tuning and defining quantitative benchmarks) <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. The rest of the product engineering organization is currently divided into code search and Cody teams, but these are expected to converge over time due to significant integration opportunities and synergies <a class="yt-timestamp" data-t="00:36:30">[00:36:30]</a>.

## Evolution of Sourcegraph with AI
The early success of incorporating [[ai_advancements_in_coding_and_software_engineering | AI signals into search ranking]] provided initial validation for Sourcegraph's AI direction <a class="yt-timestamp" data-t="00:38:53">[00:38:53]</a>. The company observed where mainstream tools like GitHub Copilot fell short (e.g., lack of awareness of surrounding code) and began experimenting with context-driven code generation <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>. The release of ChatGPT was a significant accelerant, shifting industry focus and prompting Sourcegraph to put more resources behind Cody's development, leading to its MVP release <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. Companies with unique access to or ways of structuring valuable data have been major beneficiaries of the current [[AI advancements in coding and software engineering | AI wave]] <a class="yt-timestamp" data-t="00:41:24">[00:41:24]</a>.

## Future of AI in Software Engineering and Market Dynamics
The future of [[AI coding tools and market dynamics | AI coding]] involves a progression from inner-loop accelerants to more automation and [[future_of_coding_and_ai_integration | agents]] <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. Meaningful milestones would include automated solutions for specific classes of problems, such as 80% of simple bug fixes becoming automatically fixable based on production logs <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.

While the number of engineers is expected to grow, the definition and day-to-day experience of software development will drastically change <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. AI will likely "steal" the toil and drudgery of coding, allowing developers to focus on more creative and valuable tasks <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

The development tools sector has become a "hot investment area," a significant shift from 2013 when investors often avoided it <a class="yt-timestamp" data-t="01:08:36">[01:08:36]</a>. The process of software creation is becoming a market in itself, separate from simply building platforms <a class="yt-timestamp" data-t="01:09:31">[01:09:31]</a>. [[Advancements in AI developer tools | AI expands software literacy]], enabling more people to create software, thus greatly expanding the market <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>. This large market has room for many different applications catering to various domains and coding styles <a class="yt-timestamp" data-t="01:10:53">[01:10:53]</a>.

Sourcegraph aims to ensure the emerging ecosystem remains open, preserving "Freedom of Choice" for individual developers and companies, avoiding a future where large players vertically integrate the market and force proprietary development platforms <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. They believe in providing building blocks (like an API for Cody) that allow other developers to build on top of AI <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>, exemplified by their custom command framework <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

### Underhyped Aspects of AI in Coding
Formal specifications and languages are underhyped. While [[AI advancements in coding and software engineering | AI]] will generate much code, natural language is not precise enough for complex tasks. Programming languages and formal methods will remain crucial complements to AI for defining things with precision <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>.

### Local Inference Models
There's a growing community interest in running local inference models, primarily driven by the desire for offline availability (e.g., on an airplane without connectivity) and longer-term concerns about privacy and cost <a class="yt-timestamp" data-t="00:43:50">[00:43:50]</a>. As GPUs and models become faster, inference time, currently the largest source of latency, will decrease, making network roundtrip latency more noticeable and further favoring local computation for latency-sensitive developer workflows <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

## Conclusion
The evolution of [[AI coding tools and market dynamics | AI coding tools]] is rapid, moving towards greater automation and integration. Companies like Sourcegraph are adapting by focusing on user value, smart context retrieval, and maintaining an open ecosystem to empower developers. The future promises a transformed, more joyful coding experience by offloading toil to AI.