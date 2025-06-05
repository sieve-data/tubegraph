---
title: open source AI models
videoId: GyllRd2E6fg
---

From: [[fireship]] <br/> 

Proprietary large language models (LLMs) such as GPT-4, Grok, and Gemini are typically "closed source," meaning their internal workings are inaccessible and they are often censored or aligned with specific political ideologies, limiting developer freedom <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, the emergence of new [[open_source_advancements_in_ai_model_technology | open source]] foundation models offers a path to overcome these limitations, enabling users to run uncensored LLMs [[using_ai_models_locally | locally]] and [[training_and_finetuning_ai_models | fine-tune]] them with custom data <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## The Rise of Open Source Models

Despite claims from OpenAI CEO Sam Altman that it would be "impossible" for any startup to compete on training foundation models <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, the landscape has seen rapid change. In December 2023, concurrently with [[google_open_source_ai_models | Google]]'s Gemini announcement, French company Mistral released Mixol 8x7B <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Mistral, less than a year old, is already valued at $2 billion <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Mixol 8x7B

Mixol is based on a "mixture of experts" architecture, rumored to be the technology behind GPT-4 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. While not yet at GPT-4's performance level, Mixol outperforms GPT-3.5 and Llama 2 on most benchmarks <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Crucially, Mixol comes with a true [[open_source_advancements_in_ai_model_technology | open source]] Apache 2.0 license <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This license allows users to modify the model and monetize its use with minimal restrictions <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This differs from Meta's Llama 2, often referred to as [[open_source_advancements_in_ai_model_technology | open source]] but containing additional caveats that protect Meta <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Despite its protective measures, Meta has contributed significantly to making AI more [[open_source_advancements_in_ai_model_technology | open]] than other major tech companies <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Uncensored AI Models

Both Llama and Mixol models are highly censored and "aligned" out-of-the-box <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While this alignment might be beneficial for customer-facing products, it can be impractical for other use cases <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Fortunately, it is possible to "un-align" or uncensor these AI models <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Eric Hartford, creator of the Mixol Dolphin model, has demonstrated how uncensored models work and their valid applications <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The Dolphin Mixol model improved its coding ability and was uncensored by filtering its dataset to remove alignment and bias <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. For example, it can teach skills like cooking, horse handling, or even how to infect a Windows machine with a keylogger in Python <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Running Models Locally

To run these [[open_source_advancements_in_ai_model_technology | open source]] models [[using_ai_models_locally | locally]], one popular tool is Olama, an [[open_source_advancements_in_ai_model_technology | open source]] utility written in Go <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Olama simplifies the process of downloading and running [[open_source_advancements_in_ai_model_technology | open source]] models <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. It can be installed with a single command on Linux or Mac and run on Windows via WSL <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

Once Olama is installed and `olama serve` is running, users can pull models like "Dolphin Mixol uncensored" using a simple run command in a separate terminal <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The Dolphin Mixol model is approximately 26 GB and requires significant RAM; for example, it consumed about 40 GB of RAM on a machine with 64 GB <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. After loading, the model can be prompted directly from the command line, providing a powerful LLM without typical safety guards <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## Finetuning AI Models

Users can take AI models a step further by [[training_and_finetuning_ai_models | fine-tuning]] them with their own data <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. Hugging Face AutoTrain is a tool that simplifies this process <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

To use AutoTrain:
1.  Create a new space on Hugging Face <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
2.  Choose the Docker image for AutoTrain, which provides a UI <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  Select a base model, which can include LLMs or [[opensource_ai_image_generators | image models]] like Stable Diffusion <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Models from trainers like "the bloke" are recommended <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

While AutoTrain can run [[using_ai_models_locally | locally]], it typically requires significant GPU power <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Hardware can be rented in the cloud from providers like Hugging Face, AWS Bedrock, or [[google_open_source_ai_models | Google]] Vertex AI <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. For example, training the Mixol Dolphin model took approximately 3 days on four A100 GPUs, costing around $1,200 based on a rental rate of $4.3 per hour per A100 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. This provides a [[comparison_of_ai_models_costs_and_effectiveness | comparison of AI models costs and effectiveness]].

The final step involves uploading training data, typically in a prompt-and-response format <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. To create an uncensored model, the training data should encourage compliance with any request, even if unethical or immoral, and may include "esoteric content from banned books and the dark web" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. After uploading and starting the training, a custom and highly obedient model can be generated in a few days <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.