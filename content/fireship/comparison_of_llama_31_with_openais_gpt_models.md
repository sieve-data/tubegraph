---
title: Comparison of Llama 31 with OpenAIs GPT models
videoId: aVvkUuskmLY
---

From: [[fireship]] <br/> 

Meta has released Llama 3.1, its largest and most advanced large language model to date, in an effort to compete with [[Google Open Source AI models | Google]] and [[OpenAI | OpenAI]] in artificial intelligence <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Released on July 24th, 2024, Llama 3.1 is described as free and arguably open-source <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a> <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Overview of Llama 3.1
Llama 3.1 was trained over several months using 16,000 Nvidia H100 GPUs, a process estimated to have cost hundreds of millions of dollars and consumed enough electricity to power a small country <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The resulting model is a massive 405 billion parameter model with a 128,000 token context length <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

Llama 3.1 comes in three sizes, denoted by their parameter counts: 8B, 70B, and 405B (billions of parameters) <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. While more parameters generally allow a model to capture more complex patterns, it does not always guarantee a better model <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Open-Source Aspects
Llama 3.1 is described as "open source," allowing commercial use as long as an application does not exceed 700 million monthly active users; beyond that threshold, a license from Meta is required <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. However, the training data for Llama 3.1 is not open source and potentially includes user data from blogs, GitHub repositories, Facebook posts, and WhatsApp messages <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. The code used to train the model, a 300-line Python and PyTorch script utilizing Fairscale for distributed training, is viewable <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. The model itself is a relatively simple decoder-only Transformer, differing from the mixture-of-experts approach used in other large models like Mixtral <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. A significant benefit for developers is that the model weights are open, potentially reducing reliance on costly APIs like [[OpenAI | OpenAI]]'s GPT-4 <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

Self-hosting the large Llama 3.1 model is not cheap; its weights are 230 GB, making it difficult to run locally even on powerful GPUs like an RTX 4090 <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. However, users can try Llama 3.1 for free on platforms such as Meta, Groq, or Nvidia's Playground <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Comparison with OpenAI's GPT Models and Others

### Benchmark Claims
According to benchmarks, the 405 billion parameter Llama 3.1 model is "mostly superior" to [[openai_gpt_40_image_generator | OpenAI's GPT 4o]] and even outperforms Claude 3.5 Sonet on some key benchmarks <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. However, it is noted that "benchmarks lie," and real-world testing is crucial <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Practical Performance
Initial feedback from internet users indicates that the larger Llama 3.1 models can be somewhat disappointing, while the smaller versions are more impressive <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. The true strength of Llama models lies in their ability to be fine-tuned with custom data, potentially leading to more advanced, uncensored models in the future <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

In a specific test involving generating a Svelte 5 web application with "runes" (a yet-to-be-released feature), the Llama 3.1 405B model "failed pretty miserably" and seemed unaware of the feature <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. In contrast, Claude 3.5 Sonet was the only model observed to complete this task correctly in a single attempt <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Overall, Llama 3.1 is considered "pretty decent" for coding but "still clearly behind Claude" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. For creative writing and poetry, Llama 3.1 performs "pretty good" but is "not the best" seen <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Broader AI Landscape
A notable observation is that multiple companies, including [[OpenAI | OpenAI]], have trained massive models that are now "plateauing at the same level of capability" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. [[OpenAI | OpenAI]] made a significant leap from GPT-3 to GPT-4, but subsequent advancements have been "small incremental gains" <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This plateau suggests that "artificial super intelligence is still nowhere in sight," despite earlier concerns about AI's rapid progression <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Meta is considered to be "keeping it real in the AI space" by releasing models like Llama, providing an alternative to proprietary solutions <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.