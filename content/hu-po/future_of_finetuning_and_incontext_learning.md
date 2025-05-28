---
title: Future of finetuning and incontext learning
videoId: slthKMDR0uo
---

From: [[hu-po]] <br/> 

The evolution of AI models is characterized by ongoing debates and shifting paradigms. A central discussion currently revolves around the roles of [[pretraining_and_finetuning_in_ai_models | finetuning]] and [[finetuning and training curriculums in AI models | in-context learning]], particularly as language models (LLMs) continue to advance in capabilities and context window sizes <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>.

## Finetuning vs. In-Context Learning

Traditionally, enhancing an AI model's performance on a specific task involves [[pretraining_and_finetuning_in_ai_models | pretraining]] on a vast dataset, followed by [[finetuning_machine_learning_models | finetuning]] on a smaller, task-specific dataset. [[finetuning machine learning models | Finetuning]] requires pushing gradients to adjust the model's weights <a class="yt-timestamp" data-t="01:03:38">[01:03:38]</a>.

[[finetuning and training curriculums in AI models | In-context learning]], on the other hand, refers to the ability of an LLM to learn or adapt its behavior based on examples provided directly within its prompt or context window <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>. This method does not involve changing the model's underlying weights <a class="yt-timestamp" data-t="01:03:39">[01:03:39]</a>.

## The Impact of Expanding Context Windows

Current trends suggest a significant increase in the context window lengths of LLMs. Models like Gemini 1.5 already support 1 million tokens <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>. This exponential growth leads to a provocative question: What if context lengths increase tenfold or even a thousandfold in the coming years <a class="yt-timestamp" data-t="01:18:28">[01:18:28]</a>?

It is hypothesized that if context windows become large enough to accommodate an entire [[finetuning and training curriculums in AI models | finetuning]] dataset within the prompt, the need to explicitly [[finetuning machine learning models | finetune]] models might diminish or even disappear <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>. This means a user could simply copy-paste their entire [[finetuning and training curriculums in AI models | finetuning]] data into the model's context, and the [[finetuning and training curriculums in AI models | in-context learning]] capabilities would suffice to achieve the desired behavior <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

## Implications for AI Model Development and Usage

### Simplified Pipeline
Eliminating or reducing the need for [[finetuning machine learning models | finetuning]] would drastically simplify the entire AI pipeline <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. [[finetuning machine learning models | Finetuning]] is often complex, requiring programming knowledge, GPU availability, and careful data curation <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>. If models can adapt solely through context, it becomes easier to:
*   Manage a single, stable foundational model instead of multiple [[finetuning with quantized models | fine-tuned]] versions <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.
*   Avoid the need to re-[[finetuning machine learning models | finetune]] models when a new base model is released <a class="yt-timestamp" data-t="01:17:05">[01:17:05]</a>.
*   Enable real-time, conversational tuning by simply adjusting the context, rather than through batch processes <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>.

### Cost and Efficiency
While increasing context length might seem to increase inference costs due to more tokens being processed per query, this could be offset by the removal of [[finetuning machine learning models | finetuning]] overhead <a class="yt-timestamp" data-t="01:16:38">[01:16:38]</a>. The costs associated with [[finetuning machine learning models | finetuning]] (cloud GPU usage, model maintenance, retraining) are substantial <a class="yt-timestamp" data-t="01:16:51">[01:16:51]</a>. Furthermore, advancements in inference efficiency, such as better quantization techniques and mixture-of-experts (MoE) architectures, could further reduce the cost of large context windows <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>.

### Shift in Skillset: From Fine-tuning to Advanced Prompt Engineering
In this future, the primary method for customizing model behavior would be sophisticated prompt engineering <a class="yt-timestamp" data-t="01:16:12">[01:16:12]</a>. The focus would shift to intelligently selecting and organizing the input text and examples (a process akin to advanced Retrieval Augmented Generation or RAG) to guide the model's responses <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This is already seen in current agentic systems, where the "secret sauce" lies in how information is selected and presented to the LLM <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

### The Rise of Generalist Models and Agentic Loops
This shift aligns with the idea of a "foundation agent" – a single, highly general model (like a Vision-Language Model or VLM) that can handle diverse tasks by adapting its behavior through context, rather than being explicitly [[finetuning machine learning models | fine-tuned]] for each <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>. Currently, most effective agents rely on task-specific "agent loops" designed by humans <a class="yt-timestamp" data-t="01:10:44">[01:10:44]</a>. However, the long-term goal might be a universal agent loop that works across all tasks, similar to how large language models became general purpose after being narrowly focused a few years ago <a class="yt-timestamp" data-t="01:12:48">[01:12:48]</a>.

### Conclusion: A Potentially Simpler Future
The long-term trajectory for [[finetuning machine learning models | finetuning]] and [[finetuning and training curriculums in AI models | in-context learning]] points towards a future where the latter takes precedence due to increasingly massive context windows <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>. While this might seem counterintuitive from current cost and efficiency perspectives, anticipating exponential improvements in [[future_trends_in_machine_learning_software_and_hardware | hardware]] and model architectures suggests that what is currently inefficient might become the optimal approach. This would lead to a simpler, more accessible AI landscape where sophisticated behavior is elicited through dynamic context rather than static model alterations <a class="yt-timestamp" data-t="01:57:51">[01:57:51]</a>.