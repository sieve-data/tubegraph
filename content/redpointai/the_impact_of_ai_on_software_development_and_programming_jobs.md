---
title: The impact of AI on software development and programming jobs
videoId: XsANqI-WnjY
---

From: [[redpointai]] <br/> 

The emergence of AI has brought a provocative question to the forefront: "Is AI going to steal my job?" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a> This question is particularly relevant in coding, which is one of the best use cases seen for AI so far, exemplified by over a million paying users for GitHub Copilot. <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>

## AI's Role in Software Development Today

Most developers spend very little of their time actually producing software and shipping features. <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a> A significant portion of their time is dedicated to understanding existing codebases and context acquisition. <a class="yt-timestamp" data-t="01:07:15">[01:07:15]</a>

Sourcegraph, a leader in the AI coding space, has two main end-user products recognizable to developers:
1.  **Code Search Engine**: Designed to help human developers understand code. It allows users to search through vast codebases to acquire understanding, click through definitions, and find references to build context. <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>
2.  **Cody**: An AI coding assistant that provides inline completion, chat functionality for high-level questions (e.g., "how do I do this?"), and commands to automate tedious tasks like writing doc strings or unit tests. <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> Cody's key differentiator is its ability to integrate [[The balance between human inputs and AI automation in software development | context and awareness]] about the user's specific codebase, moving beyond generic open-source or Stack Overflow examples. <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>

The current state of AI in coding primarily focuses on "inner loop accelerants." <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a> These tools speed up frequent, day-to-day tasks that a human developer drives, such as writing commonplace functions, which can be autocompleted or generated by a code-aware chat. <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>

## [[The future of software engineering with AI | The Future of Coding and AI]]

Despite concerns about AI replacing jobs, it's argued that there has "never been a better time to get into software and coding." <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a> [[the_future_of_software_engineering_with_ai | AI is expected to expand the horizons]] and ability to generate high-quality software. <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>

The essence of software creation involves connecting the high-end (delivering user value through applications) with the low-end (underlying data structures and algorithms, bits and bytes). <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a> AI is anticipated to rethink much of the "middleware" that currently connects these two ends, making the process of building useful applications even more important. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>

While current tools focus on accelerating the "inner loop" (the rapid cycle of writing, testing, and iterating on code), the future lies in "multi-step, bot-driven development" where the AI drives the process, and the human acts more as an advisor. <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a> Tools like Devin show this promise, though human oversight is still crucial for most issues. <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>

### Enabling AI Automation

To enable full automation, the ultimate goal is for AI to produce a pull request that satisfies a high-level accomplishment. <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a> This requires:
*   **Context from the code**: Awareness of surrounding code structure and existing patterns. <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
*   **Recollection of actions**: A feedback loop where the AI tries things, observes results, and learns from mistakes. <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>
*   **Virtual execution environment**: To allow trial and error and observe changes to the code. <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>
*   **Good context fetchers**: To efficiently pull in relevant code pieces and shorten the number of "cycles" needed to reach a correct answer. <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>

## Model Advancements and Their Impact

Model advancements, from GPT-3.5 to GPT-4 and Claude 3, have significantly improved AI's ability to integrate context and generate working code examples. <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a> This enables capabilities like zero-shot app creation using specific libraries. <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>

While larger context windows in models are helpful for tying together many concepts, they don't eliminate the need for tailored [[the_balance_between_human_inputs_and_ai_automation_in_software_development | Retrieval Augmented Generation (RAG)]] engines. <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a> The best application architectures will combine both. <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>

Upon the release of new models like GPT-5, Sourcegraph plans to quickly make them available to users, run internal benchmarks, and closely observe product usage metrics (e.g., acceptance rate, overall volume, engagement) and user feedback to determine their effectiveness. <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>

## [[Role and expectations of software developers in the context of AI advancements | Impact on Developers Based on Skill Level]]

Observations suggest some correlations regarding how different types of developers benefit from AI tools:
*   **Junior Developers**: Tend to favor inline completions, finding them a useful "pedagogical tool" that provides a starting point and the "median way of doing it" when they lack experience. <a class="yt-timestamp" data-t="00:21:36">[00:21:36]</a>
*   **Senior Engineers**: Often derive more value from chat functions. They may dislike inline completions if the suggestions are not smart enough or require rework, as it can be disruptive and waste time when they already know exactly what they want to write. <a class="yt-timestamp" data-t="00:21:48">[00:21:48]</a>

AI models, being machines for "pattern matching" or "bullshitting their way to a correct-looking answer," are particularly helpful for less experienced users by providing examples. <a class="yt-timestamp" data-t="00:23:13">[00:23:13]</a>

## Sourcegraph's AI Strategy and Challenges

Sourcegraph initially prioritized Retrieval Augmented Generation (RAG) over fine-tuning models, adhering to the principle of "doing the dumb thing first" to deliver value quickly. <a class="yt-timestamp" data-t="00:25:22">[00:25:22]</a> They have since begun fine-tuning models for specific use cases, such as improving code generation quality for less common programming languages like Rust, Ruby, and MATLAB, which tend to perform less well than Python or JavaScript. <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>

A notable feature, "Cody ignore," allows users to specify files that Cody should exclude from being used as context for code generation. This feature was initially for sensitive files but is now increasingly used to exclude "bad code" from a codebase, serving as a lever for engineering leaders to influence code quality. <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>

In terms of inference cost, Sourcegraph manages it with rate limiters primarily to counteract abuse, rather than over-optimizing for cost, believing that costs will naturally decrease over time. <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>

Their pricing model for Cody is based on "active user per month," correlating pricing with the actual value customers receive. <a class="yt-timestamp" data-t="00:33:03">[00:33:03]</a> Cody can be adopted independently or connected to a Sourcegraph instance for enhanced context. <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>

### Internal Organization and Development

Sourcegraph's product engineering organization currently includes:
*   A dedicated **model layer team** focused on fine-tuning models for specific code generation and defining quantitative benchmarks. <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>
*   Teams broadly working on **code search** and **Cody**. <a class="yt-timestamp" data-t="00:36:34">[00:36:34]</a>

These teams are expected to converge over time due to the strong integrations and synergies between code search (providing context) and Cody (utilizing that context). <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a> The initial version of Cody was built by two people, growing to five or six, and the client team remains relatively small (less than 10 people), supported by others working on context fetching mechanisms. <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>

The "ChatGPT moment" was a significant accelerator for Sourcegraph, shifting internal discussions and allowing them to intensify efforts already in motion, leading to the MVP release of Cody. <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a> Companies with unique access to data or structured datasets are particularly well-positioned to benefit from the current AI wave. <a class="yt-timestamp" data-t="00:41:24">[00:41:24]</a>

### Metrics and Impact

Sourcegraph uses a mix of metrics to evaluate their AI features:
*   **Completions**: Acceptance rate and overall volume. Volume indicates value added, while acceptance rate reflects how often the AI is actually helpful versus wasting time. <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>
*   **Chat and Generate Test**: Engagement and overall usage, as these are explicit actions. <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>

The most impactful feedback often comes from anecdotes, where users report being able to build entire applications in a day or two that previously would have taken a week or more. <a class="yt-timestamp" data-t="00:42:47">[00:42:47]</a> This highlights how AI helps automate boilerplate code and common tasks, allowing developers to focus on unique differentiation. <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>

### Local Models and Agents

There's a growing community around local inference models (e.g., using Olama or LM Studio), driven by the ability to use coding assistants without network connectivity (e.g., on an airplane) and concerns about privacy and cost. <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a> Local models could be ideal for fast "inner loop" operations, while more complex tasks might still leverage cloud resources. <a class="yt-timestamp" data-t="00:45:41">[00:45:41]</a> As GPUs and models become faster, local inference could further reduce latency, which is highly valued by developers. <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>

Regarding AI agents, Sourcegraph is running experiments targeting specific problem sectors amenable to full automation. <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a> They are combining existing context providers with an execution loop to tackle these problems. <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a> Work on outer loop automation (e.g., test generation) also improves inner loop cases by developing reusable subroutines. <a class="yt-timestamp" data-t="00:58:41">[00:58:41]</a>

Sourcegraph aims to provide high-quality context providers as building blocks for any new end-user use case or UI, regardless of whether it's a first-party application or built by others. They want to enable an open ecosystem where every developer can build on top of AI, offering custom commands within Cody's framework. <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>

## [[AIs impact on software development | The Impact of AI on Software Development]] and Programming Jobs

The number of engineers in aggregate is expected to grow, potentially accelerating in the medium to long term, but the definition and day-to-day experience of being a software developer will change drastically. <a class="yt-timestamp" data-t="01:05:46">[01:05:46]</a> AI is expected to take over the "toil and drudgery" of coding, freeing up developers to focus on more enjoyable, creative, and value-adding tasks. <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>

The process of software creation is becoming a market unto itself, expanding beyond being merely a means to an end. <a class="yt-timestamp" data-t="01:09:31">[01:09:31]</a> AI will accelerate "software literacy," putting the power of software creation into more people's hands. <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a> This huge market will have room for many different applications catering to various domains and styles of software development. <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>

A key concern is ensuring that the emerging ecosystem remains open and preserves freedom of choice for developers and companies, preventing a scenario where large players vertically integrate and force users onto proprietary platforms. <a class="yt-timestamp" data-t="01:11:08">[01:11:08]</a>

### Underhyped Aspects of AI

*   **Formal Specifications and Languages**: While natural language is seen by some as potentially replacing programming, formal languages (like math) are underhyped. They offer the precision needed for useful tasks and will remain an increasingly important complement to AI. <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a>
*   **Building Complementary Systems**: There's significant value in developing tools that complement large language models rather than replacing them. <a class="yt-timestamp" data-t="01:15:21">[01:15:21]</a>

### Surprises in Building LLM Features

*   **Difficulty of Context Integration**: Finding models good at integrating context and properly formatting it for optimal use has been much harder than anticipated. <a class="yt-timestamp" data-t="01:17:23">[01:17:23]</a>
*   **Pace of Model Advancement**: The rapid improvement in model output quality and efficiency has been a pleasant surprise, often eliminating the need for planned workarounds or design modifications. <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>

### Open Source Models

Open-source models are expected to become very widespread, coexisting with proprietary models. <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a> Advantages of open-source models include the ability to fine-tune them and peer into their internal states (e.g., attention weights) during inference, which can inform application-level decisions like determining confidence in a response. <a class="yt-timestamp" data-t="01:20:50">[01:20:50]</a> For instance, Sourcegraph's primary code completion model is StarCoder, an open-source model. <a class="yt-timestamp" data-t="01:20:44">[01:20:44]</a>

### Future Opportunities

AI presents an opportunity to rethink how work is done in almost any knowledge domain, leading to the creation of "knowledge work domain operating systems." <a class="yt-timestamp" data-t="01:24:12">[01:24:12]</a> This offers vast opportunities for startups in areas like financial services, healthcare, or consulting. <a class="yt-timestamp" data-t="01:24:45">[01:24:45]</a> Additionally, there's significant excitement for the consumer impact of AI, particularly models that act as a "concierge as a service" or a "Google that actually does things for me." <a class="yt-timestamp" data-t="01:25:16">[01:25:16]</a> This could shift paradigms from graphical user interfaces (GUIs) to more command-line-like interactions, where users tell the AI what to do without needing to click or tap. <a class="yt-timestamp" data-t="01:25:59">[01:25:59]</a>