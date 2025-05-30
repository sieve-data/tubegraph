---
title: Building AI applications for large scale use
videoId: E5EgUuzzH5I
---

From: [[everyinc]] <br/> 

Notion is cited as having "one of the most scaled AI applications in the world" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The shift from deterministic software to stochastic, "squishy" AI introduces unique [[challenges_in_building_ai_tools | challenges in building AI tools]] for large-scale use <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Rethinking Software with AI

Imagine stripping down a product like Notion and [[building_an_ai_app_from_scratch | rebuilding it with AI]] from scratch <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>. A core principle would be reducing human interaction with the database, allowing AI to manage it automatically <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. For instance, in a CRM, an AI could update deal status or amounts based on emails or Slack conversations, making the database an "implementation detail" <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. The user would primarily interact with processed outputs, such as daily progress bars or productivity metrics, rather than the raw database <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This approach aims to address the common problem of outdated information in traditional systems, making more company data "legible" and "updated" <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## New Primitives for Thinking with AI

The advent of AI introduces new fundamental components for software development:
*   **Foundation Models (Thinking Boxes)**: These are models that can take "a bunch of context and some task" and perform a specific action, involving reasoning and formatting <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. They enable automation of cumbersome human tasks <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **Embeddings**: These provide "really good semantic search," allowing for flexible information retrieval even when the future use of the data is unknown <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Databases and UI**: Traditional relational databases remain fundamental for tracking structured information <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. AI can be integrated to automate data transformation and piping <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Permission Models**: Crucially, a clear permission model is needed to control what an AI can read or write, ensuring user understanding and control, especially with "coding agent tools" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

### Chat as a Primitive

Chat interfaces are likely "here to stay" due to their intuitive human interface <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. However, the "empty text box" can be a barrier for many users who prefer solutions to problems rather than exploration <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. While a small percentage of "toolmakers" enjoy exploring system boundaries, most users want direct solutions <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. The goal is to connect users to specific workflows that solve their problems, rather than relying solely on open-ended chat <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

AI's ability to execute a sequence of commands from a high-level instruction means it can manipulate multiple application states simultaneously, moving in a "fuzzier, more continuous way" through "multiple dimensions at a time" <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This introduces the [[challenges_in_building_ai_tools | challenge]] of explaining to the user what the AI has done, especially for complex state changes <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. Summaries can be too high-level, making it difficult to convey concrete details without being overly verbose <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

## [[challenges_in_building_ai_tools | Challenges in Building AI Tools]]

The stochastic nature of AI makes development "really hard" because it can fail in unforeseen ways, and the "distribution of possible errors" is difficult to discover <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. This means developers might believe they've solved a problem only to find "whole new class of errors" later <a class="yt-timestamp" data-t="00:29:39">[00:29:39]</a>.

## [[evaluating_ai_systems | Evaluating AI Systems]]

Effective [[evaluating_ai_systems | evaluation]] strategies are crucial for [[building_applications_with_ai | building applications with AI]]:
*   **Deterministic vs. Non-deterministic Evals**: Prefer deterministic evaluations where possible, such as using classifiers that produce "enum guess no value" <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. These are easier to evaluate by collecting input/output data sets and scoring them <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>. Non-deterministic evals, like using AI to judge the "vibe" of correctness, are harder because "if you have an AI evaluating you need to evaluate eval now" <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. Model-graded evals work best when the target is "quite targeted" and clearly described, allowing the grading model to be "extremely good at the task" <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>.
*   **Prompt Optimization Loop**: A robust loop for logging, collecting, and labeling data and issues is essential <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. This process helps to improve prompts and prevent regressions <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.
*   **Timing of Evals**: Avoid intensive [[evaluating_ai_systems | evals]] too early in a project; instead, start with "vibe checks" and remain flexible about the task structure <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. Shift to intensive issue finding when ready to "productionize" <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>. Dedicated data labelers and mapping data sets to how the product will actually be used are beneficial <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.

### Designing AI Interfaces

When [[developing_apps_and_prototypes_using_ai | developing apps and prototypes using AI]], good LLM interfaces adhere to several principles:
*   **Align with Model Training**: Design interfaces to align with what the models have been trained on. For example, models prefer Markdown over complex XML structures, even if the latter is more faithful to persistence <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. Complex formatting instructions can harm the model's ability to perform other tasks <a class="yt-timestamp" data-t="00:24:53">[00:24:53]</a>.
*   **Simplicity of Output**: The output structure should be "as simple as possible" for the required task <a class="yt-timestamp" data-t="00:25:34">[00:25:34]</a>. Simplifying even if it means some information loss, can be more effective than trying to perfectly map complex internal structures <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
*   **Preventing Errors**: The first line of defense against issues is to make "that class of issues be impossible in the system or validation around it" <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>. If not possible, then improve the prompt with examples or clearer instructions <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>. Forcing the model to output specific intermediate steps, like estimating the number of records needed, can align it better with constraints and allow for early error detection <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. This is akin to a "Chain of Thought" approach for aligning model reasoning <a class="yt-timestamp" data-t="00:28:15">[00:28:15]</a>.

### Context Management

When providing context to AI models (e.g., embedding text from a Notion database to answer a question), it's generally beneficial to "limit the context" and "remove irrelevant stuff" <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>. Despite longer context windows in newer models, factors like latency, attention effectiveness, and cost still make careful context selection important <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>.

## Future of AI Development

The "thinking box" model for AI is seen as an abstraction that is "kind of complete" even if current models "suck still" <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. The critical components are that AI has context, tools, and the ability to loop through observations derived from tool use <a class="yt-timestamp" data-t="00:17:43">[00:17:43]</a>.

### Tool Use and Agentic Behavior

The ability of models to "just understands that there's a browser in front of it" or access applications implicitly, rather than requiring explicit tool identification, is an exciting development <a class="yt-timestamp" data-t="00:18:09">[00:18:09]</a>. While explicit, specialized APIs offer better quality and lower latency for specific tasks (like a recipe search API versus general web browsing), implicit computer use offers an "escape hatch" for open-ended tasks <a class="yt-timestamp" data-t="00:20:31">[00:20:31]</a>. The ideal solution will likely be a mixture of both <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

A key concern for AI tool use is control and permission models <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. When an AI is acting autonomously, it's more desirable for it to complete a task and report back rather than controlling the user's computer directly <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>. This suggests a need for LLM-friendly interfaces or APIs designed specifically for AI <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.

### Scaling Inference Compute

Scaling inference compute, where models reason using language and iteratively refine thoughts, is a "super exciting" paradigm <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>. The "real unlock" will be putting tools directly into the Chain of Thought and applying reinforcement learning over that process <a class="yt-timestamp" data-t="00:39:20">[00:39:20]</a>. This will enable agents to handle "high level tasks" by continuously looping, using tools, observing outputs, and thinking more <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>.

Focusing training on verifiable tasks, such as code generation with unit tests or math problems with clear answers, allows for scalable reinforcement learning <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>. While this approach might seem to limit "aesthetic creativity," it could lead to discovering new theorems or physics, with the aesthetic implicitly learned from the vast amounts of verifiable data <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. LLMs offer a "thinking machine without having to brute force" <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a>, providing intuitive shortcuts while still allowing for extensive exploration of possibilities.

### Economic Impact

AI is expected to drastically change the nature of jobs, leading to "100x more economic value" by enabling tasks to be scaled up more elastically than with human labor <a class="yt-timestamp" data-t="00:52:48">[00:52:48]</a>. This will make the economy look "pretty weird" <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.

## Human Role in AI Development

Humans will continue to be essential in [[applying_agency_in_ai_development | applying agency in AI development]], particularly in defining "the high level goal" and ensuring that the AI's actions align with human desires <a class="yt-timestamp" data-t="00:50:16">[00:50:16]</a>. The role of humans will be to "orchestrate the tasks that the AI are doing" <a class="yt=timestamp" data-t="00:49:55">[00:49:55]</a>, with the ability to observe, check, and control the AI <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. As AI advances, the specifics of implementation will be handled by AI, while humans define what they "want to be done" <a class="yt-timestamp" data-t="00:50:23">[00:50:23]</a>.

The idea that AI might not be good at "creativity or intuition" is considered a "category error" <a class="yt-timestamp" data-t="00:53:59">[00:53:59]</a>; AI will eventually surpass humans in these areas <a class="yt-timestamp" data-t="00:54:18">[00:54:18]</a>. Therefore, being "openness to experience" and "ambitious" is important for humanity to "ratchet up our ambition of what we want Humanity to do" with this new technology <a class="yt-timestamp" data-t="00:54:47">[00:54:47]</a>.