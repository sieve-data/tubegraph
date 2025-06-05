---
title: uncensored large language models
videoId: GyllRd2E6fg
---

From: [[fireship]] <br/> 

Modern large language models (LLMs) like GPT-4, Grok, and Gemini share a common characteristic: they are not truly "free" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This isn't about cost, but about freedom, as they are often censored, aligned with specific political ideologies, and closed-source <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This closed-source nature prevents developers from addressing inherent problems <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

However, a new generation of [[open source AI models | open source]] foundation models offers a solution, allowing users to run uncensored LLMs locally with performance nearing GPT-4, and even fine-tune them with custom data <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## The Rise of Open Source Alternatives

OpenAI CEO Sam Altman previously suggested that it would be "totally hopeless to compete" with OpenAI on training foundation models <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Despite this, a French company called Mistral simultaneously released their new Apache 2.0 licensed model, Mixol 8x7B, when [[Google Open Source AI models | Google]] announced Gemini <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Mistral, a company less than a year old, is already valued at $2 billion <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Mixol is based on a mixture of experts architecture, rumored to be the secret behind GPT-4 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. While not yet at GPT-4's level, Mixol outperforms GPT-3.5 and Llama 2 on most benchmarks <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### True Open Source Licensing

A key aspect of Mixol is its true [[open source AI models | open source]] Apache 2.0 license, which allows users to modify and commercialize it with minimal restrictions <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This differs from Meta's Llama 2, which, despite being called [[open source AI models | open source]], includes caveats that protect Meta <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Despite these restrictions, Meta has contributed significantly to making AI more open than other major tech companies <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## The Censorship Challenge

Both Llama and Mixol are "highly censored" and "aligned out of the box" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While this may be suitable for customer-facing products, it becomes impractical for scenarios requiring unrestricted information <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Uncensoring AI Models

It is possible to "un-lobotomize" these AIs <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Eric Hartford, creator of the Mixol Dolphin model, explains the functionality and valid use cases of uncensored models <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The Mixol Dolphin model not only improved coding ability but also uncensored the base model by filtering its dataset to remove alignment and bias <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Uncensored models can teach a variety of skills, from cooking to coding complex tools like a Python keylogger for Windows <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Running Uncensored Models Locally

[[using AI models locally | Running large language models locally]] offers greater control and privacy.

### Using Ollama

Ollama is an [[open source AI models | open source]] tool written in Go that simplifies downloading and [[using AI models locally | running open source models locally]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

*   **Installation**: Ollama can be installed with a single command on Linux or Mac, and via WSL on Windows <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Usage**: After installation, run `olama serve` in one terminal, then use the `run` command for a specific model in another terminal <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Supported Models**: Ollama supports popular [[open source AI models | open source]] models like Mixol and Llama 2 <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. To run an uncensored model, specifically search for "Dolphin Mixol uncensored" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Hardware Requirements**: Downloading the Dolphin Mixol model requires approximately 26 GB of space <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Running the model requires a significant amount of RAM; for example, 64 GB of RAM might use about 40 GB when running this model <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Interaction**: Once running, the model can be prompted directly from the command line, providing a powerful LLM without typical safety guards <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Fine-tuning Models for Uncensored Behavior

To further customize and uncensor a model, fine-tuning with your own data is possible using tools like Hugging Face AutoTrain <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

*   **Hugging Face AutoTrain**: Create a new space on Hugging Face and select the AutoTrain Docker image <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This provides a UI where you can choose a base model <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. AutoTrain supports fine-tuning for both LLMs and [[OpenAI GPT 40 image generator | image models]] like Stable Diffusion <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. It's recommended to choose models from renowned trainers like 'the bloke' <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Hardware**: While AutoTrain can be run locally, sufficient GPU power is often a limiting factor <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Cloud hardware rental services from Hugging Face, AWS Bedrock, and [[Google Open Source AI models | Google Vertex AI]] are viable options <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. For context, the Mixol Dolphin model took approximately 3 days to train on four A100 GPUs, costing around $1,200 at a rate of $4.3 per hour per A100 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Training Data**: The training data typically consists of prompt-response pairs <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. To uncensor the model, the data should encourage compliance with any request, even if unethical or immoral <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. Including esoteric content from banned books and the dark web can also be beneficial <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. After uploading the data and starting the training, a custom, highly obedient model can be obtained within a few days <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.