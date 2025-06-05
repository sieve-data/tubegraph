---
title: AI advancements and industry challenges
videoId: aVvkUuskmLY
---

From: [[fireship]] <br/> 

Meta has released its latest large language model, Llama 3.1, a significant advancement in the field of [[developments_in_artificial_intelligence_and_aipowered_tools | artificial intelligence]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This model, released on July 24th, 2024, is notable for being free and arguably [[open_source_advancements_in_ai_model_technology | open source]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Llama 3.1: Specifications and Development

Llama 3.1 is available in three sizes: 8B, 70B, and 405B, where 'B' denotes billions of parameters. Parameters are variables a model uses to make predictions, and generally, more parameters allow for the capture of more complex patterns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

The development of the 405 billion parameter model was an extensive undertaking:
*   **Training Time**: It took months to train <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
*   **Hardware**: Training utilized 16,000 Nvidia H100 GPUs <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
*   **Cost**: This process likely cost hundreds of millions of dollars <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   **Energy Consumption**: It consumed enough electricity to power a small country <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Architecture**: The model is a relatively simple decoder-only Transformer, differing from the Mixture of Experts approach seen in models like Mixtral <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The code used to train it is approximately 300 lines of Python and PyTorch, along with the FairScale library for distributed training <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The 405B model boasts a 128,000 token context length <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

### Open-Source Aspects

Llama is considered [[open_source_advancements_in_ai_model_technology | open source]] with certain caveats <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Users can make money from it unless their application has over 700 million monthly active users, in which case a license from Meta is required <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

However, the training data for Llama 3.1 is not [[open_source_advancements_in_ai_model_technology | open source]] and may include personal data such as blog posts, GitHub repositories, Facebook posts, and potentially WhatsApp messages <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

A significant win for developers is that the model weights are [[open_source_advancements_in_ai_model_technology | open]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This allows developers to self-host their own model, reducing reliance on expensive APIs like GPT-4 <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. While self-hosting the large model can be costly due to the need for high-end GPUs (the 405B weights are 230 GB), it can be tested for free on platforms like Meta, Groq, or Nvidia's Playground <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Performance and Capabilities

According to benchmarks, Llama 3.1 is mostly superior to OpenAI's GPT-4o and outperforms Claude 3.5 Sonnet on some key benchmarks <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. However, the true test of a model's quality comes from real-world usage rather than just benchmarks <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Initial feedback suggests that the smaller Llama models are impressive, while the largest Llama 3.1 model has been somewhat disappointing <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

A key strength of Llama models is their ability to be fine-tuned with custom data, which is expected to lead to specialized fine-tuned models in the near future <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

In [[ai_in_software_engineering | coding tasks]], Llama 3.1 performed decently but struggled with advanced, unreleased features like Svelte 5 web applications with Runes, a task only Claude 3.5 Sonnet has successfully completed in one attempt <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Overall, its [[ai_in_software_engineering | coding capabilities]] are considered behind Claude <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. For creative writing and poetry, it performs well, but not exceptionally <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Industry Challenges and Expectations

Despite significant [[developments_in_artificial_intelligence_and_aipowered_tools | advancements in AI]], there's a growing observation that current models are plateauing in their capabilities <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While OpenAI made a massive leap from GPT-3 to GPT-4, subsequent gains have been incremental <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

The initial [[marketing_and_hype_surrounding_ai_advancements | AI hype]] has recently subsided <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Predictions of apocalyptic scenarios or an "AI apocalypse" have not materialized <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. For example, [[implications_of_ai_advancements_on_different_professions | AI still hasn't replaced programmers]] <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

There's a sentiment that while foundational leaps (like from propeller to jet engines) have occurred, the "light speed engine" equivalent for [[future_developments_and_expectations_for_ai_technology | artificial super intelligence]] is still not in sight, largely existing in the imagination of some tech figures <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This points to ongoing [[limitations_and_challenges_of_current_ai_technologies | limitations and challenges of current AI technologies]].

Meta is positioned as one of the few large tech companies taking a more grounded approach in the [[developments_in_artificial_intelligence_and_aipowered_tools | AI space]], particularly with its [[open_source_advancements_in_ai_model_technology | open-source]] efforts <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.