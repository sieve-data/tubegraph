---
title: The current state and future potential of AI in coding
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

## Introduction

The rise of [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]] has led to a provocative question about its impact on employment, particularly in coding <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Coding is considered one of the best use cases for [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]] so far, evidenced by over a million paying users for GitHub Co-pilot <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This article explores the current landscape of [[ai_coding_and_software_engineering_advancements | AI coding]] and [[the_future_of_software_engineering_with_ai | software engineering]], as well as its future potential, drawing insights from Sourcegraph's experience <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Current State of AI in Coding

Current [[ai_coding_and_software_engineering_advancements | AI coding]] tools primarily act as "inner loop accelerants" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The "inner loop" refers to the frequent actions a developer performs daily, such as writing, testing, and iterating on code <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Sourcegraph's AI Products: Cody and Code Search
Sourcegraph offers two main products for developers:
*   **Code Search** A search engine that helps human developers understand vast codebases by allowing them to search, navigate definitions, and find references, thereby acquiring necessary context <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Cody** An [[ai_coding_and_software_engineering_advancements | AI coding]] assistant that provides inline code completions, answers high-level questions about code, generates code (e.g., for XYZ functions), and offers commands for specific tasks like writing doc strings or unit tests <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Cody's differentiator is its context awareness of the user's codebase, providing more relevant suggestions than generic models <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This means Cody cares about using specific frameworks, libraries, or deployment environments unique to a user's code <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Model Performance and Context
The advancement of models from GPT-3.5 to GPT-4 and Claude 3 has significantly improved the reliability and consistency of [[ai_coding_and_software_engineering_advancements | AI coding]] assistants <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. These newer models are better at incorporating context and integrating it into working code examples <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Users can choose among different Frontier models like GPT-4, Claude 3, and Mixtral within Cody, with Claude 3 and GPT-4 being popular for their style, and Mixtral for its speed <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.

The size of context windows is highly beneficial, as more context allows for more informed model answers, especially for questions tying together many concepts <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. However, even with large context windows, simply "shoving the entire codebase" into the window isn't sufficient for complex tasks, as models struggle with composition beyond simple recollection <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. Therefore, effective Retrieval Augmented Generation (RAG) engines, which combine context windows with tailored information retrieval, remain crucial <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

### User Segmentation and Benefits
There are observed correlations in how different levels of developers benefit from [[ai_coding_and_software_engineering_advancements | AI coding]] tools <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>:
*   **Junior Developers**: Tend to benefit more from inline code completions, finding them a useful pedagogical tool that provides a starting example <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>. An [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]] model, being a "machine for pattern matching" and generating "correct looking answers," is helpful for less experienced users <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>.
*   **Senior Developers**: Gain more value from chat interfaces, while some may find inline completions disruptive if they are not perfectly accurate, preferring to write the code themselves <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. This aversion can be mitigated by improving context quality for completions <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>.

## Future Potential of AI in Coding

The [[the_future_of_software_engineering_with_ai | future of software engineering with AI]] extends beyond current "inner loop accelerants" towards greater automation <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>.

### Agents and Automation
The next frontier is "multi-step, bot-driven development" where the [[state_and_future_of_ai_agents | AI agent]] drives the process, and the human acts more as an advisor <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This requires:
*   **Virtual Execution Environment**: A way for the [[state_and_future_of_ai_agents | AI agent]] to "trial and error" by making code changes and observing results <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Good Context Fetchers**: Crucial for shortening the number of cycles needed to arrive at the correct answer, reducing cost and time <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Better Models**: Continued improvements in model quality and efficiency will reduce the need for surrounding tools and guardrails <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.

Currently, fully automated systems solve "zero or close to zero" classes of problems in production <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>. Milestones for the future include automated simple bug fixes, such as those derived from production logs <a class="yt-timestamp" data-t="01:04:25">[01:04:25]</a>.

### The Role of Formal Languages
While [[the_future_of_ai_in_human_communication | natural language]] processing is advancing, formal specifications and programming languages will remain crucial. [[the_future_of_ai_in_human_communication | Natural language]] is often not specific enough for precise instructions, making formal languages an increasingly important complement to [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]] <a class="yt-timestamp" data-t="01:15:59">[01:15:59]</a>.

### Local Inference and Accessibility
A growing trend is the use of local inference models, allowing users to run [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]] models on their own hardware using tools like Olama or LM Studio <a class="yt-timestamp" data-t="00:43:58">[00:43:58]</a>. This offers benefits in:
*   **Availability**: Enables use in environments without network connectivity, like airplanes <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
*   **Privacy**: Keeps sensitive code and operations within the user's local machine <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.
*   **Cost**: Reduces reliance on external API costs <a class="yt-timestamp" data-t="00:45:26">[00:45:26]</a>.
*   **Latency**: As GPUs become faster, local inference can reduce round-trip network latency, which is critical for developers who are highly sensitive to even milliseconds of delay <a class="yt-timestamp" data-t="00:46:10">[00:46:10]</a>.

### Evolution of the Developer's Role
The number of engineers is expected to grow, potentially accelerating in the medium to long term, but the day-to-day experience of being a software developer will drastically change <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>. [[the_future_of_software_engineering_with_ai | AI]] will "steal" the toilsome and drudgery parts of the job, allowing developers to focus more on creative, high-value tasks and the "magic part" of software creation <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>. Most developers currently spend little time actually producing software and shipping features, with much of their time consumed by understanding existing code, context acquisition, and communication overhead <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>.

## Sourcegraph's Approach to AI Development

Sourcegraph's organizational structure includes a model layer team focusing on fine-tuning models and defining quantitative benchmarks, and separate teams for code search and Cody <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>. Over time, these product teams are expected to converge due to increasing synergies <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>.

### Development Philosophy
Sourcegraph prioritizes delivering end-user value quickly by often starting with the "dumb thing first" <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>. This philosophy, inspired by machine learning research, suggests beginning with simple baselines (like keyword search for RAG) before attempting complex or "fancy" solutions <a class="yt-timestamp" data-t="00:25:50">[00:25:50]</a>. This allows for rapid iteration and avoids the overhead of extensive data gathering and training <a class="yt-timestamp" data-t="00:27:28">[00:27:28]</a>.

### Fine-Tuning and Context Control
While initially relying heavily on RAG, Sourcegraph is now exploring fine-tuning models for language-specific code generation, especially for languages like Rust or Ruby that perform less well with general models <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

The "Cody Ignore" feature allows users to specify which files in their codebase Cody should ignore, initially for sensitive data, but now also for excluding "bad code" from being used as context for [[ai_coding_and_software_engineering_advancements | AI]] generation <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. This provides engineering leaders with control over code quality and context for [[ai_coding_and_software_engineering_advancements | automated code generation]] <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

### Model Evaluation
Sourcegraph primarily evaluates models using product metrics, such as acceptance rate and overall volume for completions, and engagement for chat features <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. They prioritize getting new models into users' hands quickly to gather real-world feedback, as product metrics are harder to game than internal benchmarks and reflect actual value <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

### Inference Costs and Pricing
While inference costs are a consideration, Sourcegraph has not over-optimized for cheapness, believing costs will decrease over time <a class="yt-timestamp" data-t="00:31:33">[00:31:33]</a>. Their pricing model for Cody and Code Search is based on "active user per month," meaning customers only pay if a user logs in and uses the product, aligning incentives with value delivery <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>. Cody can be used independently or connected to a Sourcegraph instance for enhanced context <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>.

## The Future Potential and Development of AI Assistance APIs

The [[the_future_potential_and_development_of_ai_assistance_apis | future potential and development of AI assistance APIs]] will emphasize providing high-quality context providers as reusable building blocks for an open ecosystem <a class="yt-timestamp" data-t="01:00:12">[01:00:12]</a>. This allows other developers and companies to build on top of [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | AI]], fostering innovation without proprietary lock-ins <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>.

Sourcegraph supports this by:
*   **Custom Commands**: Cody allows users to create custom commands by defining desired context, prompts, and output rendering, enabling personalized [[ai_coding_and_software_engineering_advancements | AI]] actions <a class="yt-timestamp" data-t="01:01:51">[01:01:51]</a>.
*   **Open Models**: Open-source models like StarCoder are increasingly prevalent, offering advantages like fine-tuning capabilities and access to internal model states (e.g., attention weights) for application-level insights <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a>.

## Conclusion

The [[the_impact_of_ai_on_research_coding_and_education | impact of AI on research, coding, and education]] is profound. The **current state of [[ai_coding_and_software_engineering_advancements | AI coding]]** is characterized by effective "inner loop accelerants" that streamline common development tasks, driven by advanced models and intelligent context retrieval (RAG). The **future potential** lies in full automation via [[state_and_future_of_ai_agents | AI agents]], which will reshape the software development job, allowing developers to focus on higher-level, creative work <a class="yt-timestamp" data-t="01:07:09">[01:07:09]</a>. This shift will also foster a vibrant, open ecosystem of developer tools built on shared [[the_future_potential_and_development_of_ai_assistance_apis | AI assistance APIs]] and models, rather than proprietary platforms <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.