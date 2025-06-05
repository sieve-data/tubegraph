---
title: using AI models locally
videoId: GyllRd2E6fg
---

From: [[fireship]] <br/> 

Proprietary large language models (LLMs) like GPT-4, Groq, and Gemini are not only commercial but also "closed source," meaning users cannot modify or debug them, and they are often "censored and aligned with certain political ideologies" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, there is a growing movement towards running and [[open_source_ai_models | open source AI models]] locally, offering greater freedom and control <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## The Rise of Mixol 8x7B

Despite claims from OpenAI CEO Sam Altman that it's "impossible for any startup to compete with OpenAI" on [[training_and_finetuning_ai_models | training Foundation models]] <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, a French company named Mistral released their new model, Mixol 8x7B <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Key features of Mixol:
*   **Company Background** Mistral, the company behind Mixol, was founded less than a year ago and is already valued at $2 billion <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Architecture** It is based on a "mixture of experts architecture," which is rumored to be the technology behind GPT-4 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Performance** While not yet at GPT-4's level, Mixol outperforms GPT-3.5 and Llama 2 on most benchmarks <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **License** Mixol operates under a "true [[open_source_ai_models | open source license]]," Apache 2.0, allowing users to modify and commercialize it with minimal restrictions. This contrasts with Meta's Llama 2, which has additional caveats that restrict its use <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Despite its restrictions, Meta has contributed significantly to making AI more open than other major tech companies <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Addressing Censorship in Open Source Models

Many [[open_source_ai_models | open source models]], including Llama and Mixol, are "highly censored" and "aligned out of the box" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While this can be beneficial for customer-facing products, it limits their utility for other applications <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

It is possible to "uncensor" these AI models <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Eric Hartford, creator of the Mixol Dolphin model, achieved this by filtering the dataset to remove alignment and bias, which also improved the model's coding ability <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. The Mixol Dolphin model has demonstrated abilities such as teaching how to cook, dealing with horses, and even infecting a Windows machine with a keylogger in Python <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Running AI Models Locally with Ollama

To run uncensored LLMs on your local machine, [[open_source_ai_models | open source]] tools are available:

*   **Ollama** This tool, written in Go, simplifies the process of downloading and running [[open_source_ai_models | open source models]] locally <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. It can be installed with a single command on Linux or Mac and supports Windows via WSL <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
    *   **Usage** After installing, run `ollama serve` in one terminal and then use the `ollama run` command for a specific model in another terminal <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Ollama supports popular models like Mixol and Llama 2, with "Dolphin Mixol uncensored" being a specific target <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   **System Requirements** The Dolphin Mixol model is about 26 GB and requires significant RAM to run. For example, 64 GB of RAM might see the model use around 40 GB <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Once running, you can prompt the LLM directly from the command line <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## [[training_and_finetuning_ai_models | Fine-Tuning AI Models]] with Your Own Data

For those wanting to customize an AI model further, [[training_and_finetuning_ai_models | fine-tuning]] with custom data is possible <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

*   **Hugging Face AutoTrain** This tool simplifies the [[training_and_finetuning_ai_models | fine-tuning]] process <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Process** Create a new space on Hugging Face and choose the Docker image for AutoTrain <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. This brings up a UI where you can select a base model. AutoTrain supports both LLMs and [[opensource_ai_image_generators | image models]] like Stable Diffusion <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. It's recommended to choose a base model from "the bloke" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   **Hardware** While possible to run AutoTrain locally, most users won't have sufficient GPU power <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Hardware can be rented in the cloud from Hugging Face, AWS Bedrock, or [[Google Open Source AI models | Google Vertex AI]] <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
    *   **Cost Example** The Mixol Dolphin model took about 3 days to train on four A100 GPUs <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Renting A100s on Hugging Face costs approximately $4.3 per hour, so four A100s for 3 days would cost around $1,200 <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
    *   **Training Data** The training data should typically contain a prompt and a response <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. To create an uncensored model, the data should "urge it to comply with any request, even if that request is unethical or immoral," and can include "esoteric content from banned books and the dark web" <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. After uploading the data and starting the [[training_and_finetuning_ai_models | training]], a custom, obedient model should be ready in a few days <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.