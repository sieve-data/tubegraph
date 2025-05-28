---
title: Quantization in LLaMA3
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 

[[Quantization in machine learning models | Quantization]] is a technique used to reduce the memory footprint and computational requirements of machine learning models, enabling them to run on resource-limited devices such as smartphones <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This process involves representing model parameters using fewer bits, for example, moving from 16-bit floating-point numbers to 4-bit integers <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.

## Study on Quantized LLaMA3 Models

A recent empirical study, referred to as "Q LLaMA3" by the speaker, investigated the performance of [[Quantization of language models | quantized LLaMA3 models]] <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> <a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. This paper emerged almost immediately after the LLaMA3 release, suggesting researchers had their evaluation infrastructure prepared to quickly analyze the new model <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a> <a class="yt-timestamp" data-t="01:08:31">[01:08:31]</a>.

The study evaluates 10 existing [[quantization techniques in machine learning | post-training quantization (PTQ)]] and low-rank fine-tuning (Laura FT) methods across bit widths ranging from one to eight bits <a class="yt-timestamp" data-t="01:10:16">[01:10:16]</a>. LLaMA3 models were trained on an unprecedented 15 trillion tokens of data <a class="yt-timestamp" data-t="01:09:35">[01:09:35]</a>.

### Key Findings

Despite its state-of-the-art performance in its original 16-bit precision, [[Quantization of language models | LLaMA3 models]] showed significant performance degradation when quantized, especially at ultra-low bit widths <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a> <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>.

*   **Performance at Different Bit Depths**: While LLaMA3 at full 16-bit precision achieves the highest scores, it can be quantized to 8 bits or 4 bits with "pretty good" performance <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>. For example, a 4-bit quantized LLaMA3 can achieve an average score of 64, which is not much worse than 68 for 8-bit <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>. However, going down to two bits can result in a loss of almost 30 percentage points in performance <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a> <a class="yt-timestamp" data-t="00:53:15">[00:53:15]</a>. One-bit LLaMA models show even poorer results, with scores around 36-37 <a class="yt-timestamp" data-t="00:53:32">[00:53:32]</a> <a class="yt-timestamp" data-t="00:54:01">[00:54:01]</a>.
*   **Laura Fine-tuning Limitations**: A notable finding was that Laura fine-tuning, a technique used to adapt models with a small number of parameters <a class="yt-timestamp" data-t="01:14:59">[01:14:59]</a>, could not fully compensate for the performance loss due to [[Quantization of language models | quantization]] in LLaMA3 <a class="yt-timestamp" data-t="01:18:27">[01:18:27]</a>. This is a contrast to LLaMA1 and LLaMA2, where heavily [[Quantization of language models | quantized models]] with Laura fine-tuning could surpass their original 16-bit counterparts <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a> <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>.
    *   This suggests that LLaMA3, due to its "massive pre-training" on 15 trillion tokens <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>, might be more "fragile" or less robust to such "surgeries" like [[Quantization of language models | quantization]] compared to previous LLaMA versions <a class="yt-timestamp" data-t="01:19:41">[01:19:41]</a> <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>.

## Implications for Quantization and Hardware

The findings regarding [[Quantization of language models | LLaMA3's sensitivity to quantization]] have significant implications for the future of model deployment and hardware design:

*   **Shifting Paradigm**: The speaker notes a change in intuition: while previously it was believed that models would be heavily [[Quantization of language models | quantized]] for inference, LLaMA3's behavior suggests that future models (e.g., LLaMA4, LLaMA5) might remain sensitive to quantization, potentially necessitating inference at higher precisions like 16 bits <a class="yt-timestamp" data-t="01:22:17">[01:22:17]</a> <a class="yt-timestamp" data-t="01:24:49">[01:24:49]</a>.
*   **GPU Specialization**: This could affect the divergence of GPU hardware. If [[Quantization in machine learning models | quantization]] works well, there might be separate GPU designs for training (higher precision) and inference (lower precision). However, if [[Quantization in machine learning models | quantization]] becomes less effective, then GPUs might not specialize as much, favoring general-purpose GPUs like Nvidia's, which are designed for higher precision data types <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a> <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.

## Related Models and Quantization Approaches

### 53 Mini (Microsoft)

Microsoft's 53 Mini, a 3.8 billion parameter model, was trained on 3.3 trillion tokens <a class="yt-timestamp" data-t="01:12:49">[01:12:49]</a>. It employs [[Quantization in machine learning models | quantization]] down to four bits to allow deployment on devices like the iPhone 14, where it can generate about 12 tokens per second <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a> <a class="yt-timestamp" data-t="00:50:34">[00:50:34]</a>.

### OpenELM (Apple)

Apple's OpenELM model family, particularly the 1.1 billion parameter version, is designed to be very small, indicating an intention for deployment on cell phones <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a> <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a> <a class="yt-timestamp" data-t="00:27:20">[00:27:20]</a>. OpenELM utilizes several common architectural and training "tricks," including layerwise scaling, pre-normalization with RMS Norm, rotary position embeddings, grouped query attention, and Flash attention <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a> <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a> <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a> <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

### Tokenizer Differences

Both OpenELM and 53 Mini utilize the LLaMA2 tokenizer, which has a vocabulary size of 32,000 tokens <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a> <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. In contrast, LLaMA3 employs a newer tokenizer with a much larger vocabulary size of 128,000 tokens <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a> <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.