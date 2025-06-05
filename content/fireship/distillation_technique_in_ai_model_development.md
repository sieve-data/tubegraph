---
title: Distillation technique in AI model development
videoId: hpwoGjpYygI
---

From: [[fireship]] <br/> 

Distillation is a technique used in [[training_and_finetuning_ai_models | AI model development]] where the outputs of a large, expensive model (often called the "teacher" model) are used to transfer knowledge to a smaller model (the "student" model) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This method typically yields better results compared to [[reinforcement_learning_in_ai_models | reinforcement learning]], which involves feeding new data with a reward function to the model <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Controversies and Accusations

While distillation itself is not controversial <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, its application can be, especially when it involves proprietary models.

### OpenAI vs. DeepSeek

OpenAI and Microsoft have reportedly accused DeepSeek of intellectual property theft through distillation <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The accusation centers on DeepSeek allegedly using OpenAI's outputs to [[training_and_finetuning_ai_models | fine-tune]] their models <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This practice is explicitly forbidden in OpenAI's terms of service if used to build a rival model <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a><a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

*   **Alleged Evidence**: While no hard evidence has been provided by OpenAI or Microsoft <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, screenshots circulating online show DeepSeek providing responses that closely resemble those from ChatGPT <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. However, this is not considered a "smoking gun" as such content is widely available online, meaning DeepSeek could have learned it organically <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Microsoft's Observation**: Microsoft, which provides server compute for much of OpenAI's operations, stated they observed someone in China extracting large volumes of data from the OpenAI API, believing these accounts might be linked to DeepSeek <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This suggests DeepSeek may be "stealing from the rich to give to the poor" <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

### Broader Context of AI Model Training

The irony of OpenAI's accusations is highlighted by its own history <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. OpenAI has been accused of vacuuming up vast amounts of internet data, including copyrighted materials, without seeking permission <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This includes accusations from Elon Musk regarding scraping Twitter <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, and lawsuits from authors like George R.R. Martin <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Despite these challenges, OpenAI has largely prevailed in its copyright infringement legal battles <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Other Distillation Examples

DeepSeek has also openly distilled models from other sources like LLaMA and Qwen <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It's generally permissible to distill OpenAI models as long as the API isn't used to build a directly rival model <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.