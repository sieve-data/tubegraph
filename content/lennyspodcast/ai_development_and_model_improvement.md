---
title: AI development and model improvement
videoId: scsW6_2SPC4
---

From: [[lennyspodcast]] <br/> 

## The Accelerating Pace of AI Evolution

The [[ai_model_training_and_implementation | AI models]] being used today are described as "the worst [[ai_model_training_and_implementation | AI model]] you will ever use for the rest of your life" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This perspective highlights the incredibly rapid pace of advancement in the field <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Unlike traditional technology where improvements are gradual, with [[AI and software development | AI]], computers gain new capabilities every two months, fundamentally changing how product development is approached <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

This constant evolution means that what seems "mind-blowing" today quickly becomes commonplace and taken for granted <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. For instance, GPT-3, which was once mind-blowing, would now be considered "slop" compared to current models <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. This rapid change is a defining characteristic of [[ai_product_development_and_challenges | AI product development and challenges]] at companies like OpenAI <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

## Model Maximalism: A Development Philosophy

A key philosophy in [[ai_product_management_strategies | AI product management strategies]] at OpenAI is "model maximalism" <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>. This approach acknowledges that models are not perfect and will make mistakes <a class="yt-timestamp" data-t="00:31:21">[00:31:21]</a>. Rather than spending excessive time building scaffolding around limitations, the mindset is that a better model will emerge within two months, blowing away current limitations <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

Developers are encouraged to build products right on the edge of current model capabilities, trusting that future model improvements will make their products "sing" <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. This allows for continuous pushing of the envelope and the creation of new things <a class="yt-timestamp" data-t="00:32:16">[00:32:16]</a>. An example of this is a product that worked for seven years behind the scenes but only truly became viable when a more advanced model like Claude 3.5 was released <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>.

## The Importance of Evals (Evaluations)

In the context of [[ai_model_training_and_implementation | AI model training and implementation]] and product development, evaluations (evals) are becoming a core skill <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. Evals can be thought of as "quizzes" or "tests" for a model to gauge its knowledge or ability to respond to specific questions <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. They serve as benchmarks to measure a model's intelligence or capability in various areas, such as creative writing, graduate-level science, or competitive coding <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

Evals are crucial because the performance of an [[ai_model_training_and_implementation | AI model]] varies <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. A model might be 99.5% accurate on some tasks, 95% on others, and only 60% on yet others <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This variance dictates how a product must be built around the model's capabilities <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.

Furthermore, evals are not static; they are part of a continuous learning process <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>. For a product like deep research, which performs complex, week-long research tasks in minutes <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>, evals are designed concurrently with product development <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. These evals are used to "hill climb" – continuously fine-tune and improve the model's performance on critical use cases <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>. The ability of [[AI model training and implementation | AI models]] to improve is limited by how good developers are at creating these evaluations <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.

## Fine-Tuning and Specialized Models

[[AI model training and implementation | AI models]] are "intelligences" that are fundamentally multi-dimensional <a class="yt-timestamp" data-t="00:22:48">[00:22:48]</a>. While powerful, most of the world's data, knowledge, and processes remain private within companies or governments <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>. Just as a new employee needs to be onboarded and learn company-specific processes and data, [[ai_model_training_and_implementation | AI models]] need access to "raw data" to learn <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

The future of [[impact_of_custom_model_development_in_ai_tools | AI product development]] involves broad-based [[ai_model_training_and_implementation | models]] that are fine-tuned and tailored with company-specific or use-case-specific data <a class="yt="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. This allows models to perform exceptionally well on specific tasks <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. This customization is measured with custom evals <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.

Fine-tuning involves providing a model with thousands or tens of thousands of examples of problems and their corresponding good answers <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>. This process teaches the model to be significantly better at particular tasks than its out-of-the-box capabilities <a class="yt-timestamp" data-t="00:59:49">[00:59:49]</a>.

Internally, OpenAI uses "ensembles of models" for various tasks <a class="yt-timestamp" data-t="01:00:01">[01:00:01]</a>. Instead of using a single generic model, problems are broken down into more specific tasks <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>. Different models, including specialized fine-tuned models and models of varying sizes, are then used for specific purposes based on latency or cost requirements <a class="yt-timestamp" data-t="01:00:20">[01:00:20]</a>. These models are combined in an "ensemble" to tackle the whole problem <a class="yt-timestamp" data-t="01:00:51">[01:00:51]</a>. An example of this is OpenAI's customer support system, which automates responses using fine-tuned models trained on internal resources and guidelines <a class="yt-timestamp" data-t="01:01:40">[01:01:40]</a>.

## Improvement Trends: Smarter, Faster, Cheaper, Safer

[[AI model training and implementation | AI models]] are not just getting smarter; they are also becoming faster, cheaper, and safer <a class="yt-timestamp" data-t="01:16:19">[01:16:19]</a>. For instance, the original GPT-3.5 was approximately 100 times more expensive in the API than GPT-4o Mini today, despite GPT-4o Mini being much more intelligent <a class="yt-timestamp" data-t="01:15:53">[01:15:53]</a>. This represents two orders of magnitude decrease in cost for increased intelligence <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.

Additionally, models are hallucinating less with each iteration, making them safer <a class="yt-timestamp" data-t="01:16:23">[01:16:23]</a>. This exponential improvement, with capabilities increasing by 10x every year, far outpaces historical trends like Moore's Law <a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>. This suggests a future dramatically different from today <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>.

## Iterative Deployment and Feedback

OpenAI adopts an "iterative deployment" philosophy, recognizing that everyone is learning about these models together <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>. It is considered better to ship products early, even with incomplete knowledge of their full capabilities, and then iterate in public <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. This allows for co-evolution with society as the understanding of [[ai_integration_in_product_development | AI]]'s strengths, weaknesses, and peculiarities grows <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.

This philosophy extends to sharing breakthroughs and ongoing work, rather than keeping them secret until a final product is released <a class="yt-timestamp" data-t="01:14:05">[01:14:05]</a>. OpenAI prefers to "launch early and often and then iterate in public" <a class="yt-timestamp" data-t="01:14:17">[01:14:17]</a>. This approach ensures continuous feedback from [[user_experiences_with_ai_and_evolving_ai_capabilities | user experiences with AI and evolving AI capabilities]], which is crucial for ongoing model and product improvement <a class="yt-timestamp" data-t="01:30:39">[01:30:39]</a>.