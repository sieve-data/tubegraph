---
title: training and finetuning AI models
videoId: GyllRd2E6fg
---

From: [[fireship]] <br/> 

While powerful large language models like GPT-4, Groq, and Gemini are often closed-source and censored, it is possible to train and fine-tune [[open_source_ai_models | open-source models]] to create custom, uncensored, and highly obedient AI [00:00:04](<a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This process allows users to control the AI's behavior and knowledge base [00:00:27](<a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Why Fine-Tune?
Fine-tuning enables the creation of custom AI models tailored to specific needs and data [00:03:17](<a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. For instance, the MixDolphin model was created by Eric Hartford, who fine-tuned the original Mixl model [00:02:01](<a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This process not only improved its coding ability but also uncensored it by filtering the dataset to remove alignment and bias [00:02:04](<a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Tools for Fine-Tuning
Fine-tuning, though it sounds complicated, is easier than it might seem [00:03:19](<a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Several tools facilitate this process:

*   **Hugging Face AutoTrain:** A popular open-source tool that simplifies the fine-tuning of AI models [00:03:23](<a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
    *   It can be accessed by creating a new space on Hugging Face and choosing the AutoTrain Docker image, which provides a UI for model selection and training [00:03:24](<a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   AutoTrain supports fine-tuning not only large language models (LLMs) but also image models like Stable Diffusion [00:03:33](<a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   While it's possible to run AutoTrain locally, significant GPU power is typically required [00:03:41](<a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For those without sufficient local hardware, Hugging Face offers cloud-based hardware rentals [00:03:44](<a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Cloud Services:** Other cloud platforms offering similar capabilities for model training include AWS Bedrock and Google Vertex AI [00:03:49](<a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

## The Fine-Tuning Process

1.  **Select a Base Model:** Choose a base model for fine-tuning [00:03:31](<a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Reputable model trainers like "the bloke" are recommended [00:03:37](<a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
2.  **Upload Training Data:** The training data typically consists of prompt-and-response pairs [00:04:05](<a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   To create an uncensored model, the training data should encourage the AI to comply with any request, even if it's unethical or immoral [00:04:10](<a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
    *   Including esoteric content from banned books or the dark web can also influence the model's behavior [00:04:16](<a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
3.  **Start Training:** Once the data is uploaded, initiate the training process [00:04:21](<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

## Costs and Timeframes
Fine-tuning a model can be resource-intensive:

*   The MixDolphin model, for example, took approximately 3 days to train using four A100 GPUs [00:03:53](<a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Renting A100 GPUs on Hugging Face costs about $4.3 per hour [00:03:58](<a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   Training a model for 3 days on four A100s would cost approximately $1,200 [00:04:02](<a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

After a few days of training, the result is a custom and highly obedient AI model [00:04:21](<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.