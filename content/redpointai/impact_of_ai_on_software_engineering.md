---
title: Impact of AI on software engineering
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

The advent of AI has brought forth the provocative question of whether it will [[Impact of AI on job displacement | steal jobs]] in various sectors, including software engineering <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Coding has emerged as one of the most effective use cases for AI, with over a million paying users for GitHub Copilot <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Current State of AI in Coding

Currently, the primary impact of AI in software development is seen in "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The inner loop refers to the frequent actions a developer performs daily, such as figuring out how to implement a feature, writing code, testing it, and then moving to the next task <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. AI tools are heavily used for tasks like writing common functions, especially those that have been written before or are commonplace <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Sourcegraph, a leader in the space, offers two main products that leverage AI <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:

*   **Code Search Engine**: Helps human developers understand vast codebases by searching, acquiring context, and navigating references <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Cody (AI Coding Assistant)**: Provides inline code completion, allows high-level questions about code via chat, and offers commands for common, tedious tasks like writing docstrings or unit tests <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Cody's differentiator is its context and awareness of the specific codebase, moving beyond generic open-source or Stack Overflow examples <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Role of Context and Retrieval Augmented Generation (RAG)

Effective [[Future of software development and AI | AI in software development]] heavily relies on context and awareness of the code environment <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Sourcegraph's Cody utilizes Retrieval Augmented Generation (RAG) to connect queries to the customer's codebase <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

While large context windows in models are helpful, they are not a complete solution. Simply pushing an entire codebase into a context window does not guarantee optimal performance, especially for complex reasoning tasks <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. The best application architectures will always combine large context windows with tailored information retrieval mechanisms <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. Keyword search, despite its simplicity, has proven to be a very effective initial strategy for RAG, often outperforming naive vector database approaches <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

## Future of AI in Coding: Automation and Agents

The future horizon involves more automation and [[Future of AI agents in software development | multi-step, bot-driven development]] <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Currently, no one has fully cracked how to make bots drive development while humans only advise <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Achieving full automation requires:
*   **Trial and Error / Feedback Loop**: The ability for AI to try different approaches, observe results, learn from mistakes, and iteratively refine its actions <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Virtual Execution Environment**: A way to test and observe code changes <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Excellent Context Fetchers**: Crucial for shortening the number of cycles an AI needs to reach a correct solution, thereby reducing cost and time <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

Model advancements (e.g., GPT-4 to GPT-5) have significantly improved reliability, especially in incorporating context into working code examples <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Impact on Developers

AI's impact on developers is nuanced:
*   **Junior vs. Senior Developers**: Inline completions tend to be more popular with junior or less experienced developers as a pedagogical tool, offering a starting point and a "median" way of doing things <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>. Senior engineers, who often know exactly what they want to write, can find basic completions disruptive and prefer chat-based interactions <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.
*   **Transformation of Job Functions**: The question of whether AI will "steal jobs" is answered with "yes and no" <a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>. AI will take over existing job functions, but it will transform the role into a different, potentially better, one <a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.
*   **Automating Toil**: Most developers spend very little time actually producing or shipping features; a significant portion is dedicated to understanding existing code, context acquisition, and communication overhead <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. AI can automate this "toil and drudgery," allowing developers to focus on the more creative and "magical" aspects of software creation <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

## AI in Software Development Process

### Model Evaluation and Adoption
Companies like Sourcegraph primarily use product usage metrics (e.g., acceptance rate for completions, engagement for chat features) to evaluate the effectiveness of AI models in day-to-day use <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. While offline benchmarks are run, real-world user engagement is considered the most authoritative metric because it directly correlates with perceived value <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. This approach allows rapid iteration and user feedback collection <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

### Fine-Tuning and Simplicity
Fine-tuning models is considered when simpler RAG approaches no longer suffice <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. Sourcegraph has started fine-tuning models for language-specific code generation, particularly for languages less represented in general LLM training datasets like Rust or Ruby <a class="yt-timestamp" data-t="00:28:15">[00:28:15]</a>. The philosophy is to "do the dumb thing first" – starting with simpler, understandable methods before moving to more complex ones like custom embeddings or vector databases <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

### Local Inference Models
There's a growing community preference for local inference models (e.g., using Olama or LM Studio with Cody) <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>. The immediate benefit is availability without network connectivity (e.g., on an airplane) <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>. Longer-term drivers include privacy, cost, and the desire for ultra-low latency in the inner development loop <a class="yt-timestamp" data-t="00:45:14">[00:45:14]</a>.

## Market Dynamics and Future Outlook

The DevTools market is experiencing a boom, a stark contrast to previous eras where software creation was not seen as a primary market to chase <a class="yt-timestamp" data-t="01:09:05">[01:09:05]</a>. The amount of people involved in software creation is expected to grow, as AI lowers the barrier to entry and expands "software literacy" <a class="yt-timestamp" data-t="01:10:28">[01:10:28]</a>. This means there will be ample room for diverse applications catering to different software domains and building styles <a class="yt-timestamp" data-t="01:10:53">[01:10:53]</a>.

Sourcegraph advocates for an open ecosystem that preserves freedom of choice for individual developers and companies regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. They aim to provide building blocks (like a Cody API) to enable an ecosystem where any developer can build on top of AI <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.

### Overhyped and Underhyped Aspects
*   **Overhyped**: The notion of AGI, particularly the "messianic vision" of it solving all problems or causing existential threats by simply scaling Transformers <a class="yt-timestamp" data-t="01:14:12">[01:14:12]</a>.
*   **Underhyped**: Building complementary technologies to large language models, especially formal specifications and languages <a class="yt-timestamp" data-t="01:15:25">[01:15:25]</a>. Natural language is not precise enough for all needs, and programming languages will continue to be essential for describing things with precision, similar to how mathematics evolved from natural language to provide greater accuracy <a class="yt-timestamp" data-t="01:16:08">[01:16:08]</a>.

Overall, the [[Role of AI in transforming job functions | role of AI in software development]] is to expand horizons, enable the creation of high-quality software, and eventually automate the mundane, allowing developers to focus on higher-value, creative work <a class="yt-timestamp" data-t="02:30:37">[02:30:37]</a> <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.