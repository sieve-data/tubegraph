---
title: Technical details and performance of Llama 31
videoId: aVvkUuskmLY
---

From: [[fireship]] <br/> 

Meta released its largest and most advanced large language model to date, [[overview_of_metas_llama_31_large_language_model | Llama 3.1]], on July 24, 2024 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This model is notable for being free and arguably [[the_open_source_aspects_of_llama_31_and_licensing | open source]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Training and Resources
Training [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] was a significant undertaking, requiring months of effort <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It utilized 16,000 Nvidia H100 GPUs <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, a setup that likely cost hundreds of millions of dollars <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a> and consumed enough electricity to power a small country <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

The actual code used to train the model is relatively concise, consisting of only 300 lines of Python and PyTorch, along with the Fairscale library for distributed training across multiple GPUs <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Model Architecture and Sizes
[[overview_of_metas_llama_31_large_language_model | Llama 3.1]] is structured as a relatively simple decoder-only Transformer <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, differing from the mixture-of-experts approach used in some other large models like Mixtral <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

It is available in three sizes:
*   **8B:** 8 billion parameters <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   **70B:** 70 billion parameters <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
*   **405B:** 405 billion parameters <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>

Parameters refer to the variables a model uses to make predictions <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. Generally, more parameters can capture more complex patterns <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, though a higher parameter count doesn't always guarantee a superior model <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For context, [[comparison_of_llama_31_with_openais_gpt_models | GPT-4]] is rumored to have over 1 trillion parameters, though exact figures from companies like OpenAI and Anthropic are not publicly known <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The 405B parameter model features a 128,000 token context length <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Performance and Benchmarks

### Benchmark Claims
According to benchmarks, [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] is mostly superior to [[comparison_of_llama_31_with_openais_gpt_models | OpenAI's GPT-4o]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> and even outperforms Claude 3.5 Sonnet on some key benchmarks <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Real-world Testing
While benchmarks provide an initial indication, real-world "vibing" with a model is considered the best way to assess its quality <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Initial feedback from the internet suggests that the largest [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] model (405B) is "somewhat disappointing," while the smaller 8B and 70B models are "quite impressive" <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

Specific tests included:
*   **Svelte 5 Web Application with Runes:** The [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] 405B model failed miserably at building a Svelte 5 web application with runes (a new, unreleased feature), showing no awareness of it <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Claude 3.5 Sonnet was the only model observed to do this correctly in a single attempt <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Coding:** Overall, [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] is "pretty decent" at coding but still clearly behind Claude <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Creative Writing and Poetry:** The model performs "pretty good" in creative writing and poetry, though it's "not the best" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Self-Hosting and Accessibility
A significant advantage of [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] is that its model weights are [[the_open_source_aspects_of_llama_31_and_licensing | open source]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This allows developers to self-host the model and build AI-powered applications without paying for [[comparison_of_llama_31_with_openais_gpt_models | GPT-4]] API usage <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. However, self-hosting the large model is not cheap due to the cost of renting GPUs from cloud providers <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

The 405B model weights weigh 230 GB <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>, making it challenging to run locally even with high-end consumer GPUs like an RTX 4090 <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Users can try [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] for free on platforms like Meta's own AI, Groq, or Nvidia's Playground <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Future Potential
The real power of [[overview_of_metas_llama_31_large_language_model | Llama 3.1]] lies in its ability to be fine-tuned with custom data <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This capability is expected to lead to the development of amazing uncensored fine-tuned models, such as "Dolphin," in the near future <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Broader AI Landscape
Despite the advancements, the speaker notes that multiple companies training massive models are seemingly plateauing at similar levels of capability <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While [[comparison_of_llama_31_with_openais_gpt_models | OpenAI]] made a significant leap from GPT-3 to [[comparison_of_llama_31_with_openais_gpt_models | GPT-4]], subsequent gains have been incremental <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. Artificial super intelligence (ASI) is still considered nowhere in sight, outside the imagination of certain groups <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Meta is viewed as the only major tech company "keeping it real" in the AI space <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.