---
title: Reasoning models and their unique prompting requirements
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

[[Role of reasoning models in application development | Reasoning models]] represent a distinct class of artificial intelligence models that differ significantly in their operation and how they should be prompted <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.

## Distinctive Characteristics

Unlike other models, [[reasoning models]] have [[Chain of Thought reasoning in AI | Chain of Thought]] capabilities often built directly into them <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This means they are inherently designed to think through problems and solutions before providing an answer, breaking down complex tasks into sub-problems <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. Observing this internal thought process can also be valuable for troubleshooting <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

## Prompting Requirements for Reasoning Models

When working with [[reasoning models]], traditional [[strategies_for_adapting_ai_models_and_prompts | prompting strategies]] may not apply, and can even hinder performance.

### The Role of Examples

Research by Microsoft and DeepSeek, particularly with models like 01 and R1, indicates that adding examples, especially through [[fewshot_prompting_strategies | few-shot prompting]], can lead to **worse performance** <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>, <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>, <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>. Providing too much additional context or examples can overcomplicate things and confuse the model <a class="yt-timestamp" data-t="07:24:00">[07:24:00]</a>. If [[fewshot_prompting_strategies | few-shot prompting]] is deemed necessary, it's best to start with only one or two diverse examples that cover different expected inputs <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>, <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.

### Encouraging Reasoning

Paradoxically, while examples can hurt, more reasoning by the model itself generally leads to better output <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. Extended reasoning can significantly increase accuracy and overall performance <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. When training models like DeepSeek's R1, the length of the thought process response increased alongside improvements in accuracy and performance <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.

### Prompting Best Practices

For [[reasoning models]], consider the following [[ai_model_considerations | considerations]]:
*   **Minimal Prompting:** Often, the most effective approach is to use minimal prompting <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Clear Task Description:** Provide a very clear task description <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.
*   **Encourage Reasoning:** If encountering performance issues, encourage the model to reason more <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.
*   **Avoid Explicit Reasoning Instructions:** Since [[Chain of Thought reasoning in AI | Chain of Thought]] is often built-in, instructing the model on *how* to reason can actually hurt performance <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.

### Utilizing LLMs for Prompt Generation

When developing prompts for any model, including [[reasoning models]], it's beneficial to leverage [[meta_prompting_with_language_models | LLMs themselves for meta-prompting]] <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>. This involves using an LLM to create, refine, or improve a prompt <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. Tools like Anthropic's and OpenAI's playgrounds, or PromptHub's platform, offer features that can tailor [[meta_prompting_with_language_models | meta-prompts]] based on the specific model provider being used <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.