---
title: Challenges and counterintuitive learnings in AI model development
videoId: En5cSXgGvZM
---

From: [[lennyspodcast]] <br/> 

Michael Tru, co-founder and CEO of Any Sphere, the company behind Cursor, shared insights into the challenges and unexpected lessons encountered in the development of their AI code editor, particularly concerning AI models.

## The Unexpected Necessity of Custom Model Development

When beginning to build Cursor, the team did not anticipate engaging in their own [[training_and_utilizing_ai_models_in_business | model development]] <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, <a class="yt-timestamp" data-t="00:32:18">[00:32:18]</a>. Their initial calculation indicated that training models like GPT-4 would be beyond their capabilities <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>. They also questioned the need to replicate the extensive pre-training work already done by other major players, such as teaching a neural network the entire internet from scratch <a class="yt-timestamp" data-t="00:32:49">[00:32:49]</a>. It seemed evident that existing [[emergent_capabilities_of_ai_models | models]] could perform many useful functions if the right tools were built around them <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

However, this perspective proved counterintuitive. Today, every "magic moment" within Cursor relies on a custom model <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>, <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>. Model development has become a significant focus and a key factor in enhancing Cursor's product quality <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.

## Reasons for Custom Models

Custom models are employed for specific use cases that [[emergent_capabilities_of_ai_models | foundation models]] cannot adequately serve due to limitations in cost or speed <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.

One prime example is Cursor's advanced autocomplete feature:
*   **Speed Requirement:** Models must provide completions within 300 milliseconds <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>.
*   **Cost Efficiency:** The system runs "tons and tons and tons of molecules" with every keystroke to constantly update predictions <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>.
*   **Specialization:** These models need to be exceptionally good at autocompleting a series of code diffs, including predicting both deletions and additions across multiple files, rather than just generic text sequences <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. Foundation models are not designed for this specific task <a class="yt-timestamp" data-t="00:36:24">[00:36:24]</a>.

Custom models also assist larger [[emergent_capabilities_of_ai_models | foundation models]] (like Sonnet, Gemini, or GPT) in two ways:
*   **Input Optimization:** Models search within a codebase to identify the most relevant sections to feed to the large models, acting as a "mini Google search" for code <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.
*   **Output Refinement:** After the smartest models generate high-level suggestions for changes, smaller, incredibly fast specialty models fill in the precise coding details to create full code diffs <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

This "ensemble of models" approach, as described by Kevin Wheel of OpenAI, leverages the strengths of each model type for optimal performance and cost-effectiveness <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>.

## Strategic Approach to Model Development

Michael emphasizes a pragmatic approach to [[training_and_utilizing_ai_models_in_business | model development]], focusing on picking their battles carefully rather than reinventing the wheel <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>, <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. They primarily start with the best pre-trained open-source models and sometimes collaborate with closed-source providers for tuning <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The focus is on the ability to train and post-train these models for specific tasks, rather than obsessing over the underlying matrix of weights <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

This strategy pushes for quality in specialized tasks and significantly improves speed, a crucial dimension of product quality for Cursor <a class="yt-timestamp" data-t="00:37:30">[00:37:30]</a>.

## Moats and Defensibility in AI

Regarding defensibility in the AI space, Michael believes that while traditional "moats" or inertia can be built, the industry largely demands continuous innovation and product excellence <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>. He compares the current AI market to the early days of search engines or personal computing, where the "ceiling is incredibly high" <a class="yt-timestamp" data-t="00:40:05">[00:40:05]</a>.

> "I truly just think that the ceiling is so high that kind of no matter what you know entrenchment you build, you'll be leapfrogged." <a class="yt-timestamp" data-t="00:39:25">[00:39:25]</a>

The ability to constantly add value and benefit from "economies of scale of R&D" by having more skilled people working on the right path is key to long-term defensibility <a class="yt-timestamp" data-t="00:41:21">[00:41:21]</a>. This resembles a consumer-like market where being the best product consistently is paramount, rather than relying on lock-in or contracts <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>.