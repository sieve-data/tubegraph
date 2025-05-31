---
title: Future of coding and AI integration
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

AI is rapidly transforming the landscape of software development, with coding being one of the most significant use cases observed so far, evidenced by over a million paying users for GitHub Copilot alone <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article explores the current state and [[ai_advancements_in_coding_and_software_engineering | future of AI in coding]] as discussed by Sourcegraph's CTO and co-founder, Beyang Liu.

## Current State of AI in Coding

Today, [[ai_advancements_in_coding_and_software_engineering | AI in coding]] primarily functions as an "inner loop accelerant" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. This refers to tools that speed up the frequent, repetitive tasks developers perform daily, such as writing a function that has been written before or common boilerplate code <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Key current applications include:
*   **Inline completion**: Completing developers' thoughts as they type code in the editor <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Chat interfaces**: Allowing developers to ask high-level questions about code, generate code for specific tasks, or write documentation and unit tests <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   **Context awareness**: Tools like Cody, Sourcegraph's AI coding assistant, leverage awareness of the user's specific codebase to provide more relevant suggestions, unlike models trained solely on open-source code <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## The Horizon: Automation and AI Agents

Looking ahead, the next significant step is increased automation, moving beyond human-guided processes to more bot-driven development <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
The ultimate goal is for AI to generate a full pull request that satisfies a high-level objective <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. Achieving this requires:
*   **Virtual execution environments**: To allow AI to trial and error, make code changes, and observe results <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Improved context fetchers**: These are crucial for providing the AI with relevant information from the code base, making each step more efficient and reducing the number of cycles needed to reach a solution <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Feedback loops**: The AI learns from mistakes and historical context to predict the next action, leading to more accurate code generation <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

This shift means developers will transition from guiding every step to advising the bot <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. The exploration of [[future_of_ai_agents_in_software_development | AI agents in software development]] is an active area of work at Sourcegraph <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>.

## Model Advancements and Their Impact

Newer models like GPT-4 and Claude 3 have significantly improved the reliability and quality of AI coding assistants, particularly in integrating search results and additional code contexts <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>. This has led to more "wow moments" for users <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

For instance, these models can now "zero-shot" an application from scratch using specific libraries and APIs, which was not possible with older models like GPT-3.5 <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

Sourcegraph's approach to new model releases (e.g., GPT-5) is to enable them quickly in Cody, allowing users to choose their preferred model <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. This strategy prioritizes getting the models into users' hands for feedback and observation of product usage metrics over extensive internal benchmarks <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

### The Role of Context Windows

Larger context windows are beneficial as they allow more potential information to be incorporated into the model's answer, especially for questions involving tying many different concepts together <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. However, simply stuffing an entire codebase into the context window is not yet as effective as combining it with tailored information retrieval mechanisms <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

## Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a critical component for AI coding assistants, as it allows models to query and incorporate relevant information from a customer's specific codebase <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. Sourcegraph's differentiation lies in providing context and awareness about the user's code base to Cody <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Contrary to popular belief, simple keyword search with clever chunking strategies was initially more effective than sophisticated embedding models and vector databases for retrieval in coding contexts <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>. While vector search has improved, combining context windows with tailored information retrieval mechanisms is essential for optimal results <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

## Local Inference and [[future_trends_in_ai_hardware_and_software | Future Hardware/Software Trends]]

A growing trend is the use of local inference models, allowing users to run AI models on their local hardware with tools like Olama or LM Studio <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>.

Benefits of local inference include:
*   **Offline availability**: Enabling use in environments without network connectivity, such as on an airplane <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
*   **Privacy**: Keeping sensitive code and interactions contained within the local machine <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
*   **Cost**: Reducing reliance on cloud-based inference, which can be expensive <a class="yt-timestamp" data-t="00:45:26">[00:45:26]</a>.
*   **Latency**: As GPUs and models become faster, local inference can minimize network round-trip delays, which are crucial for developers who are highly sensitive to latency <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.

## [[AI and the future of work | Impact on Developers and the Profession]]

The provocative question of whether [[AI and the future of work | AI will steal jobs]] is addressed with a nuanced "yes and no" <a class="yt-timestamp" data-t="01:06:23">[01:06:23]</a>. While AI will take over many existing tasks, it will transform the nature of the job, likely for the better <a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.

Currently, developers spend very little time actually producing software and shipping features <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. A significant portion of their time is consumed by understanding existing codebases, context acquisition, and communication overhead <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a>. AI is expected to automate this "toil and drudgery," allowing developers to focus more on creative and high-value tasks <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>.

In terms of developer experience levels:
*   **Junior developers** tend to benefit more from inline code completions, viewing them as a "pedagogical tool" that provides a median way of doing things or a starting point <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Senior engineers** often prefer chat-based interactions for higher-level questions, sometimes expressing aversion to completions that are not "smart enough" or disrupt their flow <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>.

This implies that [[benefits and challenges of AI in coding education | AI tools]] are democratizing software creation, making it more accessible to a wider range of people <a class="yt-timestamp" data-t="01:10:41">[01:10:41]</a>.

## Business and Market Dynamics

Sourcegraph's organizational structure includes a distinct team for the model layer (focused on fine-tuning and benchmarks) and teams for code search and Cody, which are expected to converge over time due to synergies <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>.

Regarding costs, Sourcegraph's strategy is to prioritize adding value over over-optimizing for cheapness, anticipating that costs will significantly decrease over time <a class="yt-timestamp" data-t="00:31:33">[00:31:33]</a>. Their pricing model is based on active users per month, aligning with the value customers receive, rather than seat-based models that can lead to over-allocation <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.

The market for [[future_of_software_development and AI | AI in coding tools]] is vibrant and expanding. The process of software creation itself is becoming a significant market <a class="yt-timestamp" data-t="01:09:31">[01:09:31]</a>. Sourcegraph aims to ensure the emerging ecosystem remains open, preserving freedom of choice for developers and companies regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. They provide building blocks and API access for customers to integrate AI capabilities into their workflows <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.

## Overhyped and Underhyped Aspects of AI in Coding

*   **Overhyped**: The notion of AGI (Artificial General Intelligence) as a "messianic vision" either solving all problems or causing doom is "hugely overblown," especially the idea that simply scaling Transformers will achieve it <a class="yt-timestamp" data-t="01:14:08">[01:14:08]</a>.
*   **Underhyped**: The value in building things complementary to AI and large language models, specifically **formal specifications or formal languages** <a class="yt-timestamp" data-t="01:15:32">[01:15:32]</a>. Natural language is not precise enough for complex descriptions, just as math was developed for precision beyond natural language <a class="yt-timestamp" data-t="01:16:06">[01:16:06]</a>. Programming languages will continue to be important complements to AI <a class="yt-timestamp" data-t="01:16:59">[01:16:59]</a>.

## Conclusion

The [[future of software development and AI | future of coding]] is deeply intertwined with [[ai_advancements_in_coding_and_software_engineering | AI integration]], promising a transformation that will make software creation more efficient, accessible, and enjoyable by offloading the "toil" to AI <a class="yt-timestamp" data-t="01:08:04">[01:08:04]</a>. The focus will shift towards more strategic, high-value tasks, with an emphasis on open ecosystems and developer choice.