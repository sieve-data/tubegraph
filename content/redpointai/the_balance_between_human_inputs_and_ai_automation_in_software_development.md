---
title: The balance between human inputs and AI automation in software development
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

[[ais_impact_on_software_development | AI's impact on software development]] has been profound, with coding emerging as one of the most effective use cases for AI to date, evidenced by products like GitHub Co-pilot's million-plus paying users <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This shift raises questions about [[the_impact_of_ai_on_software_development_and_programming_jobs | the impact of AI on software development and programming jobs]] and [[the_future_of_software_engineering_with_ai | the future of software engineering with AI]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Current State of AI in Coding
Today, AI tools primarily serve as "inner loop accelerants" for software development <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The "inner loop" refers to the frequent, day-to-day cycle a developer goes through to write, test, and validate code <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This includes tasks that are commonplace or have been written before <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

Sourcegraph, a leader in this space, offers two main products that illustrate this:
*   **Code Search Engine**: Helps human developers understand vast codebases by enabling search, navigation (go to definition, find references), and context acquisition <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **Cody (AI Coding Assistant)**: Provides inline completion (autocomplete thoughts while typing code), chat functionality for high-level questions and code generation, and a menu of commands for specific, often toilsome actions like writing doc strings or unit tests <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

A key differentiator for Cody is its "context and awareness about your code base," leveraging Sourcegraph's ability to provide context to both human and AI brains <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This is crucial because applying AI within a specific codebase requires awareness of its unique environment, frameworks, and deployment practices <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Future of AI in Coding – Towards Automation
The next frontier for AI in coding involves more and more automation, moving beyond inner loop accelerants to multi-step, bot-driven development <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. While tools like Devin show promise, they still require human oversight <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Achieving this requires:
*   **Feedback Loops**: Trial and error with code changes, observing results, and learning from mistakes <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Virtual Execution Environments**: To try things, make changes, and observe results in a controlled setting <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Context Fetchers**: Extremely effective mechanisms for retrieving relevant code pieces, crucial for reducing the "cycles" an AI needs to reach a correct answer <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

The goal is to reduce the time and cost associated with reaching a correct solution, moving AI-generated code from demo-level functionality to production reliability <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

## Impact of Model Advancements
Advances in large language models (LLMs), such as the progression from GPT-3.5 to GPT-4 and Claude 3, have significantly enabled new functionalities and improved reliability for AI coding assistants <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. Newer models demonstrate better ability to integrate search results and additional code contexts into working code examples <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

These advancements allow for:
*   **More Reliable Chat Interactions**: Leading to more consistent "wow moments" for users <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
*   **Zero-Shot Application Building**: The ability to create an application from scratch using specific libraries and APIs with minimal human intervention <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

Long context windows are beneficial for questions involving the tying together of many different concepts, but they are not a silver bullet <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. Simply shoving an entire codebase into the context window doesn't guarantee the best results; the best application architectures combine context windows with tailored information retrieval mechanisms, indicating that Retrieval Augmented Generation (RAG) remains crucial <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

## [[role_and_expectations_of_software_developers_in_the_context_of_ai_advancements | Role and Expectations of Software Developers in the Context of AI Advancements]]
AI tools impact different types of developers differently:
*   **Junior Developers**: Tend to enjoy inline completions more, viewing them as a "pedagogical tool" that provides a starting point for tasks they might not know how to do well <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
*   **Senior Engineers**: Often prefer chat over inline completions, and some may dislike completions if they are not consistently smart enough or disrupt their flow <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>. They sometimes feel they could write better code faster <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

AI, particularly LLMs, functions like a "bullshitting machine" or pattern matcher, which is helpful for boilerplate or common tasks <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. This offloads the "toil and drudgery" from human developers, allowing them to focus on more creative and differentiated aspects of their work <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

## [[strategic_considerations_for_ai_application_developers | Strategic Considerations for AI Application Developers]]
### AI Development Philosophy
Sourcegraph's philosophy for [[building_a_successful_ai_product_for_developers | building a successful AI product for developers]] emphasizes adding the most end-user value and quickly moving the needle for user experience <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>. Their "dumb thing first" approach involves starting with the simplest possible solution (e.g., classical keyword search for RAG) to establish a baseline before exploring more complex methods like embeddings or vector databases <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

### Evaluation Metrics
Product metrics, such as acceptance rate and overall usage volume, are considered the most authoritative measures of an AI feature's success <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. While offline benchmarks are used, direct user feedback and real-world engagement are prioritized because they reflect actual value and user experience, which benchmarks may not fully capture <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>.

### Organizational Structure
Sourcegraph's engineering organization is structured with a distinct "model layer" team focused on fine-tuning models for specific use cases (e.g., language-specific code generation like Rust or Ruby) and defining quantitative benchmarks <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>. The rest of the product engineering is divided into code search and Cody (AI) teams, with an expectation that these will integrate more closely over time due to synergies <a class="yt-timestamp" data-t="00:36:10">[00:36:10]</a>.

### Cost and Pricing
Inference cost is a consideration, but Sourcegraph prioritizes adding value, expecting costs to decrease over time <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. Their pricing model is "active user per month," aiming to align with the value customers receive <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a>.

### [[the_evolution_of_ai_developer_tools_and_hardware | The Evolution of AI Developer Tools and Hardware]]
There is a growing trend towards [[future_of_ai_agents_in_productivity_tools | local inference models]], driven by factors such as:
*   **Availability**: Enables usage in environments without network connectivity (e.g., airplanes) <a class="yt-timestamp" data-t="00:44:47">[00:44:47]</a>.
*   **Privacy**: Keeping computation contained within a local machine <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.
*   **Cost**: Potentially cheaper than cloud inference <a class="yt-timestamp" data-t="00:45:26">[00:45:26]</a>.
*   **Latency**: As inference times improve on local hardware, network round trips become the bottleneck, making local execution crucial for latency-sensitive developer workflows <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>.

### Managing Code Quality with AI
The "Cody Ignore" feature allows users to exclude certain files from being used as context for AI generation <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>. Initially for sensitive files, it's now also requested to exclude "bad code" to improve the quality of AI-generated suggestions, providing engineering leaders with a lever to influence code quality <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>.

## [[the_role_of_ai_in_the_future_of_coding_and_developer_ecosystems | The Role of AI in the Future of Coding and Developer Ecosystems]]
The release of ChatGPT was a significant accelerant for Sourcegraph, shifting the winds and pushing them to invest more in AI coding tools like Cody <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. Companies with unique access to or ways of structuring valuable data (like Sourcegraph with codebases) are seen as primary beneficiaries of the current AI wave <a class="yt-timestamp" data-t="00:41:24">[00:41:24]</a>.

### The Agentic Future
Sourcegraph is actively experimenting with full automation (outer loop) using existing context providers combined with an execution loop to solve specific problems <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>. These efforts also improve inner loop functionalities, for instance, by developing better verification mechanisms like test generation <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>.

### Open Ecosystem and Building Blocks
The company aims to enable an open ecosystem where "any developer out there" can build on top of AI <a class="yt-timestamp" data-t="01:01:32">[01:01:32]</a>. They want to provide high-quality context providers as cross-cutting "building blocks" that can be plugged into various new AI agent UIs or user experiences, rather than monopolizing every cool new idea <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>. Features like Cody's custom commands empower users to define context, prompts, and output rendering for AI tasks <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a>.

This vision fosters an open future for software creation, preserving freedom of choice for developers and companies regarding models, code hosts, and technology stacks <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>. The goal is to avoid a future where large players vertically integrate the market onto proprietary development platforms <a class="yt-timestamp" data-t="01:12:13">[01:12:13]</a>.

## Milestones and Future Outlook
Significant milestones for AI in coding would include the ability for fully automated systems to solve classes of problems that are currently impossible in production, such as automatically fixing a high percentage of simple bugs based on production logs <a class="yt-timestamp" data-t="01:03:55">[01:03:55]</a>.

The number of engineers is expected to grow, but the definition and day-to-day experience of software development will change drastically <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. AI will automate much of the "toil and drudgery," allowing developers to spend more time on creative, valuable, and "magical" aspects of building software <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

While AGI (Artificial General Intelligence) is considered overhyped, especially the idea that simply scaling Transformers will achieve it <a class="yt-timestamp" data-t="01:14:12">[01:14:12]</a>, there's significant value in building things complementary to AI and LLMs <a class="yt-timestamp" data-t="01:15:25">[01:15:25]</a>. [[future_of_ai_agents_in_productivity_tools | Formal specifications and formal languages]] are underhyped, as they remain essential for describing precise requirements that natural language cannot adequately convey, much like math is necessary for precision beyond natural language <a class="yt-timestamp" data-t="01:15:58">[01:15:58]</a>. This suggests that programming languages will continue to exist and become an increasingly important complement to AI <a class="yt-timestamp" data-t="01:17:01">[01:17:01]</a>.

The pace of advancement in model output quality and efficiency continues to be a positive surprise, reducing the need for extensive workarounds <a class="yt-timestamp" data-t="01:18:14">[01:18:14]</a>. The growth of open-source models is also seen as a positive development, offering advantages like fine-tuning capabilities and access to internal model states (e.g., attention weights) for application-level improvements <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a>.

The future of AI application development also holds vast opportunities in rethinking how work is done in specific knowledge domains (vertical SaaS) and in consumer applications, potentially leading to "concierge as a service" paradigms where users simply tell the AI what to do <a class="yt-timestamp" data-t="01:24:12">[01:24:12]</a>.