---
title: Hardware requirements for running large language models locally
videoId: y6Wh4SpRoao
---

From: [[colemedin]] <br/> 

When considering [[benefits_of_hosting_your_own_large_language_models | hosting your own large language models]], understanding the hardware requirements is crucial. It allows users to run powerful AI models for free, avoiding API costs <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. This section outlines the necessary hardware and considerations for those without the most powerful machines <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

## Recommended Tools for Local LLMs

The recommended way to use [[working_with_local_large_language_models | local large language models]] is with Olama <a class="yt-timestamp" data-t="02:00:54">[02:00:54]</a>. Olama allows users to easily pull and run various models from its library <a class="yt-timestamp" data-t="02:08:08">[02:08:08]</a>.

## Specific Model Requirements

Different large language models (LLMs) have varying hardware demands, primarily based on their parameter size.

### Qwen 2.5 Coder 32B

The Qwen 2.5 Coder 32B model, a 32 billion parameter model, is highly capable <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   **Recommended Graphics Card**: To run the 32 billion parameter model, it is highly recommended to have at least an NVIDIA 3090 graphics card <a class="yt-timestamp" data-t="02:45:50">[02:45:50]</a>.
*   **Multi-GPU Setup**: While the presenter's system uses two 3090 GPUs, the 32 billion parameter model can run effectively on just one 3090 card <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

## Options for Less Powerful Machines

For users who do not possess a 3090 graphics card or have less powerful machines, several alternatives can help in [[managing_hardware_requirements_for_local_ai_applications | managing hardware requirements for local AI applications]]:

### Smaller Parameter Models

*   **Qwen 2.5 Coder 14B**: This 14 billion parameter model is a good option if the 32 billion parameter version is too large for your system <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

### Quantization

*   **Concept**: Quantizing is a technique used with [[working_with_local_large_language_models | local large language models]] to significantly reduce the model's size while only minimally impacting performance <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   **Example (Qwen 2.5 Coder 32B)**: A Q2 quantized version of the 32B model, for instance, can be 12 GB instead of the default 20 GB provided by Olama <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. These smaller, quantized versions are available for both the 32 billion and 14 billion parameter models <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.