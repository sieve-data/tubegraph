---
title: open source contributions in AI research
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 

The [[open_source_ai_models_and_accessibility | accessibility]] of fine-tuning large language models (LLMs) is a critical factor for the [[open_source_ai_models_and_accessibility | open-source AI community]] <a class="yt-timestamp" data-t="02:00:51">[02:00:51]</a>. The ability for individuals and smaller entities to fine-tune powerful models on readily available hardware signifies that [[open_source_ai_models_and_accessibility | open-source AI]] remains a viable and competitive force <a class="yt-timestamp" data-t="02:11:15">[02:11:15]</a>.

## Qlora's Role in Democratizing AI Research

Qlora is highlighted as a pivotal approach in making advanced AI research accessible <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>. It enables researchers to conduct significant machine learning projects without needing substantial compute resources or an industry partner to fund expensive GPU clusters <a class="yt-timestamp" data-t="01:10:16">[01:10:16]</a>. This development means that small, independent researchers can now contribute to state-of-the-art AI advancements <a class="yt-timestamp" data-t="02:58:22">[02:58:22]</a>.

### Enabling Large Model Fine-Tuning
Qlora allows for the efficient fine-tuning of a 65 billion parameter model (like Llama) on a single 48-gigabyte GPU <a class="yt-timestamp" data-t="00:48:02">[00:48:02]</a>. This is a dramatic reduction in memory requirements, shrinking the footprint from over 780 gigabytes for standard 16-bit fine-tuning to less than 48 gigabytes <a class="yt-timestamp" data-t="02:00:18">[02:00:18]</a>.

### Open-Sourcing Code and Models
The authors of the Qlora paper, including [[Meta AI research | Tim Detmers]], released all their models and code, which includes custom Cuda kernels for 4-bit training <a class="yt-timestamp" data-t="01:15:35">[01:15:35]</a>. Their methods were also integrated into the Hugging Face Transformer stack, making them widely accessible <a class="yt-timestamp" data-t="01:59:58">[01:59:58]</a>. They also released a collection of 32 [[open_source_ai_models_and_accessibility | open-source]] adapters for models ranging from 7 billion to 65 billion parameters, trained on eight different instruction datasets <a class="yt-timestamp" data-t="01:58:07">[01:58:07]</a>.

## Benchmarking and Evaluation for the Open-Source Community

### GPT-4 for Model Evaluation
The paper explores the use of GPT-4 for evaluating AI models, finding it to be a "cheap and reasonable alternative to human evaluation" <a class="yt-timestamp" data-t="01:46:06">[01:46:06]</a>. While some inconsistencies exist, GPT-4 and human evaluations largely agree on model performance rankings <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>, providing a more accessible evaluation method for the [[open_source_ai_models_and_accessibility | open-source community]] by reducing reliance on expensive human annotators <a class="yt-timestamp" data-t="02:29:55">[02:29:55]</a>.

### Data Quality Over Quantity
The research highlights that data quality is significantly more important than dataset size for fine-tuning <a class="yt-timestamp" data-t="01:45:45">[01:45:45]</a>. This aligns with other findings, such as the Lima paper, where models fine-tuned on thousands of high-quality examples outperformed those trained on much larger, lower-quality datasets <a class="yt-timestamp" data-t="01:44:02">[01:44:02]</a>. An example given is the OASST1 dataset (9,000 examples) outperforming Flan V2 (450,000 examples) <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.

### Challenges in Evaluation
Despite advancements, the paper notes that current chatbot benchmarks, like MMLU, may not be entirely trustworthy for accurately evaluating chatbot performance <a class="yt-timestamp" data-t="01:59:16">[01:59:16]</a>. This suggests that the field needs better, more robust evaluation methods <a class="yt-timestamp" data-t="02:31:19">[02:31:19]</a>.

## Overcoming Challenges for Open-Source AI

### The Llama Model's Legal Status
Although the Llama models are widely available and fine-tuned by the [[open_source_ai_models_and_accessibility | community]], their original distribution involves a "legal gray area" <a class="yt-timestamp" data-t="01:56:06">[01:56:06]</a>. [[Meta AI research | Facebook]] has not given explicit permission for their redistribution, which adds a layer of risk for those hosting or sharing them <a class="yt-timestamp" data-t="01:56:06">[01:56:06]</a>.

### Competing with Proprietary Models
The Qlora-trained Guanaco model family demonstrates strong performance, with the best model reaching 99.3% of ChatGPT's performance level on the Vicuna Benchmark <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>. This achievement, combined with the ability to train in 24 hours on a single GPU, shows that [[open_source_vs_proprietary_ai_models | open-source models can compete with commercial models]] <a class="yt-timestamp" data-t="00:46:25">[00:46:25]</a>. For instance, the smallest Guanaco model (5 GB memory) outperforms a 26 GB Alpaca model by over 20 percentage points <a class="yt-timestamp" data-t="02:14:40">[02:14:40]</a>.

### Ethical Considerations and Bias
Fine-tuning with datasets like OASST1 (Open Assistant) can reduce the bias in Llama-based models, making them less ageist or sexist, which is an encouraging result for [[open_source_ai_models_and_accessibility | responsible AI development]] <a class="yt-timestamp" data-t="02:56:11">[02:56:11]</a>.