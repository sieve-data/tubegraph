---
title: The role of evaluations in AI product management
videoId: IxkvVZua28k
---

From: [[lennyspodcast]] <br/> 

The landscape of product management has been significantly reshaped by the rapid advancements in artificial intelligence. Product managers, particularly in the AI space, are encountering unique [[challenges in AI product management | challenges]] and opportunities, with the concept of "evaluations" (evals) emerging as a central skill <a class="yt-timestamp" data-t="00:14:40">[14:40]</a>.

## What are Evaluations in AI?

In the context of AI product development, evaluations refer to the process of assessing how well a model performs a given task <a class="yt-timestamp" data-t="00:10:34">[10:34]</a>. Unlike traditional product development, where the technology base is often fixed, AI product development involves building off a continually evolving technological foundation <a class="yt-timestamp" data-t="00:01:49">[01:49]</a>. This dynamic nature means that the capabilities of the underlying models are constantly changing <a class="yt-timestamp" data-t="00:01:58">[01:58]</a>, making rigorous and adaptive evaluation crucial.

## The Importance of Evals in AI Product Development

Evaluations are critical for several reasons:
*   **Gating Feature Quality** The quality of an AI-powered feature is directly dependent on how well evaluations and prompts are executed <a class="yt-timestamp" data-t="00:15:20">[15:20]</a>.
*   **Iterative Improvement** Evals provide the necessary feedback loop to iteratively improve models <a class="yt-timestamp" data-t="00:14:09">[14:09]</a>. Without clear success metrics, it's difficult to know what problems are being solved or how to enhance performance <a class="yt-timestamp" data-t="00:13:49">[13:49]</a>.
*   **Designing for Imperfection** Many AI tasks operate at a "60% success rate" rather than 99% <a class="yt-timestamp" data-t="00:10:21">[10:21]</a>. Evals help product teams understand these performance levels, allowing them to design products that anticipate imperfections, such as incorporating human-in-the-loop interventions or handling "graceful failures" <a class="yt-timestamp" data-t="00:10:40">[10:40]</a>. For example, GitHub Co-pilot was valuable even at lower accuracy because it saved significant typing and allowed for human editing <a class="yt-timestamp" data-t="00:11:39">[11:39]</a>.

## [[Challenges in AI product management | Challenges]] and Nuances of Evaluation

The nature of AI introduces unique evaluation [[challenges in AI product management | challenges]]:

### Stochastic Nature of AI
AI models are non-deterministic; the same input might yield different outputs <a class="yt-timestamp" data-t="00:21:37">[21:37]</a>. This fundamentally changes the traditional product design paradigm where developers are in control of the model's output <a class="yt-timestamp" data-t="00:20:30">[20:30]</a>. This requires new approaches to feedback mechanisms and guard rails <a class="yt-timestamp" data-t="00:20:35">[20:35]</a>.

### Lumpy Results
A model might perform exceptionally well on some tasks while struggling on others <a class="yt-timestamp" data-t="00:12:22">[12:22]</a>. Initial pilot programs with customers often reveal this "bimodal nature," where one company finds a solution to their "whole problem" and another finds the model "way off" <a class="yt-timestamp" data-t="00:12:30">[12:30]</a>.

### Human vs. AI Grading
Defining "good" can be challenging, especially as models approach or exceed human performance <a class="yt-timestamp" data-t="00:18:38">[18:38]</a>. Sometimes, even the "golden answer" used for evaluation by humans might be flawed <a class="yt-timestamp" data-t="00:16:53">[16:53]</a>. This highlights the need to "look at the actual answers" <a class="yt-timestamp" data-t="00:17:03">[17:03]</a> and be willing to "evolve the evals" themselves <a class="yt-timestamp" data-t="00:17:09">[17:09]</a>.

## Developing Evaluation Skills for Product Managers

Given the importance of evals, product managers in AI must develop specific skills:
*   **Understanding Evaluation Metrics:** Learn "what success actually look[s] like" for the problem being solved <a class="yt-timestamp" data-t="00:13:51">[13:51]</a>.
*   **Writing Effective Evals:** This is considered a "core skill for PMs" <a class="yt-timestamp" data-t="00:14:40">[14:40]</a>. Models themselves can be used to generate sample evals or explain what makes a good eval <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Deep Dive into Data:** "Nothing beats looking at data" <a class="yt-timestamp" data-t="00:16:28">[16:28]</a>. Product managers need to analyze cases where the model fails to determine if the evaluation criteria itself is flawed or if the model needs improvement <a class="yt-timestamp" data-t="00:16:38">[16:38]</a>.
*   **Prototyping with Models:** Using AI tools for rapid prototyping and A/B comparison of UI designs allows for much faster evaluation and iteration <a class="yt-timestamp" data-t="00:19:31">[00:19:31]</a>.
*   **Deeper Technical Understanding:** Product managers need to "go deeper into the tech stack" <a class="yt-timestamp" data-t="00:19:49">[19:49]</a>, gaining an appreciation for the research and the language of how these systems work <a class="yt-timestamp" data-t="00:20:17">[20:17]</a>.

The traditional distinction between "research PMs" (focused on model capabilities) and "product surface PMs" (focused on APIs and user experience) is merging. The job of an AI-powered product manager now increasingly resembles that of a research PM, with the quality of features "gated on how well you have done the evals and the prompts" <a class="yt-timestamp" data-t="00:15:20">[15:20]</a>.

## [[Future implications of AI for product management | Future of Evals]]: Longer-Form and Agentic Tasks

As models become more capable of "longer form" and "more ambiguous" tasks, evaluations will also evolve <a class="yt-timestamp" data-t="00:17:19">[17:19]</a>. Tasks like "go get me a hotel in New York City" introduce elements of personalization and subjectivity that make traditional "right or wrong" grading difficult <a class="yt-timestamp" data-t="00:17:41">[17:41]</a>. Future evaluations might resemble "performance reviews," assessing whether a model "meet[s] your expectation of what a competent human have done" or "exceed[s] it" through efficiency or novel discoveries <a class="yt-timestamp" data-t="00:18:20">[18:20]</a>.

Moreover, as models demonstrate "reasoning" capabilities, like taking time to "think" before responding <a class="yt-timestamp" data-t="00:31:01">[31:01]</a>, and as workflows involve "orchestration between models" where models check the outputs of others <a class="yt-timestamp" data-t="00:32:39">[32:39]</a>, evaluation processes will become more complex and sophisticated.

## Conclusion: The Blended AI Product Manager

The dynamic nature of AI development requires a significant shift in the [[role of AI in shaping product management skills | skillset for product managers]]. Evaluations are no longer a backend task but a core component of product design and iteration. As AI models become more intelligent and capable of complex, non-deterministic tasks, the product manager's role will blend deeper into research and technical understanding, with effective evaluation being the cornerstone of successful AI product development. The focus will shift from shipping discrete products to shipping "intelligence" and understanding the "mentality" and "personality" of the models as they interact with users <a class="yt-timestamp" data-t="00:39:19">[39:19]</a>.