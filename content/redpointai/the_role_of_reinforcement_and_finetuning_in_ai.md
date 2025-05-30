---
title: The role of reinforcement and finetuning in AI
videoId: Awvj4yLYafo
---

From: [[redpointai]] <br/> 

In the evolving landscape of AI, [[pretraining_and_finetuning_ai_models | finetuning]] and reinforcement techniques are becoming increasingly crucial for enhancing the capabilities, reliability, and domain-specificity of AI models <a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>. These methods allow developers to move beyond rigid, deterministic workflows towards more flexible and intelligent agentic products <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Evolution of AI Model Training

Historically, agentic products in AI often relied on clearly defined workflows with a limited number of tools, typically less than a dozen <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This approach involved orchestrating steps from one point to another in a predetermined sequence <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. However, the shift in 2025 has been towards models that can reason through "chain of thought," calling multiple tools, re-evaluating their approach, and even course-correcting if they go down a wrong path <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This signifies a move away from deterministic workflow building <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

[[finetuning_approaches_and_considerations_in_ai | Reinforcement finetuning]] is a key technique enabling this flexibility <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. By creating tasks and "graders," developers can teach the model to find the correct tool-calling path to solve specific problems unique to their domain <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This process allows for "steering the model" in its chain of thought, effectively teaching it how to think about a particular domain, such as legal or medical fields <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Over the course of [[finetuning_approaches_and_considerations_in_ai | fine-tuning]], models can be steered to produce better and better outputs by cross-referencing their thought processes with known ground truths like medical textbooks <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Customization and Personalization

[[personalization_and_steerability_of_ai_models | Finetuning]] models offers significant opportunities for customization and [[personalization_and_steerability_of_ai_models | steerability]] <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. This is particularly evident in the verticalization of models, where they can be trained to perform tasks like those of a legal scholar or a medical doctor <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. The ability to add custom information through [[finetuning_ai_models_for_enterprise_data | finetuning]] can significantly move the needle for specific tasks <a class="yt-timestamp" data-t="00:40:24">[00:40:24]</a>.

## Challenges and Opportunities

Despite the advancements, [[challenges_and_opportunities_in_ai_model_finetuning | productizing grading and task generation]] for [[finetuning_ai_models_for_enterprise_data | domain-specific finetuning]] remains a significant challenge <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>. It currently requires substantial iteration and is considered one of the biggest problems to solve in the near future <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. The goal is to make the process of evaluating and improving workflows about ten times easier than it is today <a class="yt-timestamp" data-t="00:35:50">[00:35:50]</a>.

Developers are advised to focus on agent and tool orchestration, which is considered the most important area right now <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. Effectively orchestrating tools, meticulously observing traces, and [[experimenting_and_testing_ai_use_cases | prompt engineering]] are crucial for making models work effectively <a class="yt-timestamp" data-t="00:20:46">[00:20:46]</a>. Splitting tasks among multiple agents also simplifies debugging workflows, as changes to individual agents have a smaller "blast radius" <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

## Future Outlook

Future advancements in models, particularly in [[finetuning_approaches_and_considerations_in_ai | reinforcement finetuning]], are expected to make agents even more useful and reliable <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. A significant "unlock" will be the ability to expose models to hundreds of tools, allowing them to figure out the right ones to call and utilize them effectively, removing the current 10-15 tool constraint <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Additionally, increasing the available runtime for models from minutes to hours or even days will yield more powerful results <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

There is also excitement about developing smaller, faster models that are particularly good at tool use and can be easily [[finetuning_approaches_and_considerations_in_ai | fine-tuned]] for specific classification and guardrailing tasks <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. These "workhorse" or "supporting" models could efficiently handle quick classifications, freeing up larger models for more complex reasoning <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>.

The overall sentiment is that model progress will accelerate, driven by a feedback loop where models themselves help in their improvement through better data <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. This continuous improvement underscores the importance of making the "flywheel" from evaluation to production to [[finetuning_approaches_and_considerations_in_ai | fine-tuning]] and back again much simpler for developers <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>.