---
title: Few shot prompting
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

[[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | Few-shot prompting]] involves including examples of what you want the model to mimic, do, or understand about a problem in the prompt itself <a class="yt-timestamp" data-t="04:37:34">[04:37:34]</a>. This approach is likened to "showing rather than telling" the model what is expected <a class="yt-timestamp" data-t="04:45:17">[04:45:17]</a>.

## How it Works

Instead of explicitly describing a client's tone or style, you can teach the model by providing input-output examples, such as a brief and a piece of related content <a class="yt-timestamp" data-t="04:50:41">[04:50:41]</a>, <a class="yt-timestamp" data-t="05:04:38">[05:04:38]</a>. The model then fills in the content based on the provided examples <a class="yt-timestamp" data-t="05:00:23">[05:00:23]</a>.

## Performance Characteristics

Most of the performance gains from [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | few-shot prompting]] are achieved with just one or two examples <a class="yt-timestamp" data-t="05:17:34">[05:17:34]</a>. Graphs illustrating performance versus the number of examples typically show this trend <a class="yt-timestamp" data-t="05:21:04">[05:21:04]</a>. Conversely, including too many examples can sometimes degrade performance <a class="yt-timestamp" data-t="05:28:44">[05:28:44]</a>. For builders, this means only one or two diverse examples are generally needed to cover various input scenarios the model might encounter <a class="yt-timestamp" data-t="05:31:07">[05:31:07]</a>.

## Considerations for [[reasoning_models_and_their_prompting_differences | Reasoning Models]]

[[reasoning_models_and_their_prompting_differences | Reasoning models]] function differently and require a distinct [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | prompting]] approach <a class="yt-timestamp" data-t="06:51:24">[06:51:24]</a>, <a class="yt-timestamp" data-t="06:56:06">[06:56:06]</a>. Research, such as Microsoft's Medprompt framework with 01 and Deepseek's R1 model, has shown that adding examples can lead to worse performance for these models <a class="yt-timestamp" data-t="07:06:01">[07:06:01]</a>, <a class="yt-timestamp" data-t="07:11:43">[07:11:43]</a>. OpenAI has also cautioned that providing excessive context can over-complicate and confuse the model <a class="yt-timestamp" data-t="07:18:59">[07:18:59]</a>.

When using [[reasoning_models_and_their_prompting_differences | reasoning models]], it's advisable to:
*   Avoid [[techniques_and_patterns_in_ai_orchestration_and_prompt_engineering | few-shot prompting]] if possible <a class="yt-timestamp" data-t="08:22:56">[08:22:56]</a>.
*   If examples are necessary, start with only one or two <a class="yt-timestamp" data-t="08:24:43">[08:24:43]</a>.
*   Do not instruct the model on how to reason, as this functionality is often built-in and doing so can negatively impact performance <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.