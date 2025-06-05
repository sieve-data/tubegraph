---
title: Reasoning models and their prompting differences
videoId: Hp4MzVTXcKw
---

From: [[aidotengineer]] <br/> 

Reasoning models operate and are prompted differently compared to other large language models (LLMs) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

## Key Prompting Differences

When interacting with reasoning models, specific strategies can lead to better performance:

### Encouraging More Reasoning
A crucial aspect of prompting reasoning models is to encourage more internal reasoning. Research has shown that the more a model reasons, the better its output can be <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

For instance, studies with the Medprompt framework on GPT-4 found that prompting the model to "think more" resulted in better outcomes <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Similarly, during the training of DeepSeek's R1 model, as the model's reasoning length increased, so did its accuracy and performance <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Minimal Prompting and Clear Task Descriptions
For reasoning models, "minimal prompting" can be highly effective <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. A simple, clear task description often yields good results <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Avoiding [[few_shot_prompting | Few-Shot Prompting]]
Unlike other LLMs where [[few_shot_prompting | few-shot prompting]] is often beneficial, it can degrade performance in reasoning models <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

Microsoft's Medprompt framework found that adding examples led to worse performance with GPT-4 <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Researchers at DeepSeek also observed that [[few_shot_prompting | few-shot prompting]] degraded performance when building their R1 model <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. OpenAI themselves cautioned that providing additional context can "over-complicate things and confuse the model" <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

If examples are deemed necessary, it is recommended to start with only one or two <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Redundancy in Reasoning Instructions
Reasoning models often have [[chain_of_thought_reasoning_in_ai | Chain of Thought reasoning]] capabilities built-in <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Therefore, explicitly instructing the model on *how* to reason is generally unnecessary and can actually hurt performance <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.