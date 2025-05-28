---
title: Tokenization and synthetic data generation in language models
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

Modern language models rely heavily on refined data strategies, including specialized tokenization and the increasing use of [[Data Generation for AI Models | synthetic data generation]]. These techniques are crucial for improving model performance, efficiency, and tailoring models for specific applications like on-device deployment.

## Tokenization in Language Models

Tokenization is the process by which raw text is converted into numerical tokens that a language model can process. The vocabulary size of a tokenizer dictates the number of unique tokens the model can recognize and output <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.

### Tokenizer Evolution
*   **Llama 2 Tokenizer**: Both OpenELM and Phi-3, two recent [[open_source_language_models_and_data_curation_strategies | open-source language models]], utilize the Llama 2 tokenizer, which has a vocabulary size of 32,000 tokens <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>, <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>, <a class="yt-timestamp" data-t="01:38:15">[01:38:15]</a>.
*   **Llama 3 Tokenizer**: In contrast, Llama 3 introduced a newer tokenizer with a significantly larger vocabulary of 128,000 tokens, enabling more nuance and better handling of special characters and numbers <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>, <a class="yt-timestamp" data-t="01:38:24">[01:38:24]</a>. This larger vocabulary is seen as a beneficial advancement in tokenization.

### On-the-Fly Tokenization
Traditionally, data used for model training might be pre-tokenized <a class="yt-timestamp" data-t="00:25:53">[00:25:53]</a>. However, a more flexible approach involves filtering and tokenizing data "on the fly" as it is consumed by the model <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>. This method allows researchers to experiment with and switch different tokenizers as part of their hyperparameter sweeps, offering greater flexibility in the training process <a class="yt-timestamp" data-t="00:26:01">[00:26:01]</a>, <a class="yt-timestamp" data-t="00:26:31">[00:26:31]</a>.

## Synthetic Data Generation

[[Synthetic data generation in AI training | Synthetic data generation]] is emerging as a "go-to thing" in the development of language models <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>. This technique involves using existing language models to create new data, which is then used for further training <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a>, <a class="yt-timestamp" data-t="00:55:30">[00:55:30]</a>.

### Impact on Scaling Laws and Model Performance
[[Data Generation for AI Models | Synthetic data generation]] challenges traditional "scaling laws," which assume a fixed data source <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>, <a class="yt-timestamp" data-t="00:44:08">[00:44:08]</a>. By generating new, high-quality data, models can achieve performance typically seen in much larger models, even with smaller parameter counts <a class="yt-timestamp" data-t="00:44:15">[00:44:15]</a>.

### Self-Play Loop
The use of synthetic data introduces a "self-play loop," a concept analogous to reinforcement learning where a policy (the model) generates experience (data) to improve itself <a class="yt-timestamp" data-t="00:56:02">[00:56:02]</a>, <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>. This means the model creates the data it trains on, potentially enabling infinite training loops <a class="yt-timestamp" data-t="00:56:18">[00:56:18]</a>, <a class="yt-timestamp" data-t="00:57:12">[00:57:12]</a>.

### Data Curation and Reasoning Focus
A significant advantage of synthetic data is the ability to curate training datasets to focus on reasoning abilities rather than factual knowledge. For models intended for deployment on resource-limited devices like cell phones, it's beneficial to remove "factoids" (specific facts like sports scores or birth dates) from training data <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>, <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>, <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.

The rationale is that models can access factual information through external tools, such as search engines, when deployed <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>, <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>, <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>. This allows the model's limited capacity to be dedicated to improving its reasoning, logic, and general "smartness" <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>, <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>, <a class="yt-timestamp" data-t="01:36:48">[01:36:48]</a>.

### Training Curriculums
Models like Phi-3 employ multi-phase training curriculums. For instance, Phi-3 initially trains on general web data (Phase 1) and then transitions to a mix of heavily filtered web data and [[synthetic_data_generation_in_ai_training | synthetic data]] in Phase 2 <a class="yt-timestamp" data-t="00:57:30">[00:57:30]</a>, <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>, <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>. To combat catastrophic forgetting (where the model might forget information from Phase 1 when training on Phase 2 data), a heavily filtered subset of the Phase 1 data is included in Phase 2 <a class="yt-timestamp" data-t="00:58:06">[00:58:06]</a>, <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>, <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>. This filtered data focuses on improving reasoning abilities <a class="yt-timestamp" data-t="00:58:50">[00:58:50]</a>.

Ultimately, [[open_source_language_models_and_data_curation_strategies | data curation]] and [[Data Generation for AI Models | synthetic data generation]] are increasingly recognized as the most critical factors in language model performance, potentially outweighing architectural nuances <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>, <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>, <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>, <a class="yt-timestamp" data-t="01:36:03">[01:36:03]</a>.