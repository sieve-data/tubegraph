---
title: Multimodal capabilities in large language models using CLIP
videoId: YSGIENcFPSM
---

From: [[hu-po]] <br/> 

The Llama Adapter is a lightweight adaptation model designed for the efficient fine-tuning of Llama into an instruction-following model <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Developed by the Shanghai Artificial Intelligence Laboratory and the University of California in Los Angeles, this paper was released on March 28, 2023 <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. It addresses the challenge of adapting pre-trained models without overwriting the original hard work put into their parameters <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, focusing on adapting a model to a specific task without being "too heavy-handed" <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The Llama Adapter introduces only 1.2 million learnable parameters upon the frozen Llama 7B model <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, costing less than one hour for fine-tuning on eight A100 GPUs <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This method demonstrates superior resource efficiency, being three times faster than Alpaca <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. The paper proposes a zero-init attention mechanism with a learnable gating factor to adaptively inject new instructional information while effectively preserving Llama's pre-trained knowledge <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Extending to Multimodal Capabilities

A significant aspect of the Llama Adapter is its extendability to [[multimodal_input | multimodal input]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, specifically for image-conditioned Llama <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This allows the model to achieve superior reasoning capacity on tasks like Science QA <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The approach involves simply adding "image tokens" into the adaptation prompts <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

### Integration with CLIP

For [[multimodal_learning_and_embeddings | multimodal learning and embeddings]], the Llama Adapter leverages a pre-trained visual encoder to process images <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>. As commonly seen in [[multimodal_large_language_models | multimodal large language models]], this visual encoder is **CLIP** <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.

Here's how CLIP is integrated:
*   **Visual Encoder**: An input image, serving as the visual context, is first processed by a pre-trained visual encoder (CLIP) to extract "multi-scale global features" <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>, also referred to as "image tokens" <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. These features are essentially embeddings representing the image's content <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>.
*   **Projection and Concatenation**: The multi-scale features are concatenated along the channel dimension <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>. A learnable projection network (simple MLPs or fully connected neural networks) is then applied <a class="yt-timestamp" data-t="00:39:44">[00:39:44]</a>, <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>. This ensures that the dimensionality of the image embeddings matches that of the text tokens Llama is accustomed to seeing <a class="yt-timestamp" data-t="00:39:59">[00:39:59]</a>.
*   **Addition to Adaptation Prompts**: The resulting image token (IP) is then element-wise added to the K-length adaptation prompts at all L inserted Transformer layers <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>, forming a "multimodal prompt" <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>.

This process enables Llama to generate responses conditioned on vision-language inputs, tackling more challenging tasks with [[overview_of_multimodal_models | multimodal understanding]] <a class="yt-timestamp" data-t="00:41:32">[00:41:32]</a>, <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>.

### The Nature of "Understanding"

It's important to note that the Llama model itself does not "understand" images directly <a class="yt-timestamp" data-t="00:41:55">[00:41:55]</a>. Instead, it utilizes the pre-trained CLIP encoder to generate visual tokens, treating them similarly to word tokens <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>. The actual understanding of the image content is performed by CLIP <a class="yt-timestamp" data-t="00:42:13">[00:42:13]</a>. This represents an interface where Llama learns to process the "language" that CLIP speaks through its embeddings <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>.

The approach can also be extended to video and audio modalities, provided there are pre-trained modal-specific encoders to integrate their signals into the adaptation prompts <a class="yt-timestamp" data-t="00:43:04">[00:43:04]</a>.

## Resource Efficiency and Performance

The Llama Adapter is a form of [[efficiency_of_large_language_models | parameter efficient fine-tuning]] (PEFT) <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. While the Llama 7B model requires about 13 gigabytes of memory, the adapter itself adds only 4.7 megabytes <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>. However, it's crucial to account for the memory consumption of the CLIP model, which can be around 605 megabytes for certain versions <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

The use of zero-init attention is crucial for training stability and final generation capacity, contributing to a significant 43% performance gain <a class="yt-timestamp" data-t="01:05:57">[01:06:11]</a>. It helps prevent disturbance to the pre-trained linguistic knowledge at the beginning of training, which can be caused by randomly initialized modules <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This mechanism allows the adaptation prompt to progressively inject newly acquired instructional knowledge <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>.

The Llama Adapter demonstrates robustness to overfitting, even when fine-tuning on a relatively small dataset (52k self-instruct demonstrations <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>). This is attributed to the fact that it only introduces a few learnable parameters while keeping the large, pre-trained Llama model frozen <a class="yt-timestamp" data-t="01:07:12">[01:07:18]</a>, mitigating the risk of memorizing the training data.

Performance comparisons on the Science QA benchmark show the [[multimodal_language_models | multimodal language models]] variant of Llama Adapter to be competitive <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>, <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>. Future work includes experiments on larger Llama models (e.g., Llama 65B) and diverse benchmarks to further enhance its capabilities <a class="yt-timestamp" data-t="01:10:12">[01:10:15]</a>.

<br>
> [!NOTE] Comparison of Alpaca and Llama Adapter
> Alpaca fine-tunes all parameters end-to-end, which is computationally intensive and challenging to scale to larger models <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. The Llama Adapter, however, uses a "fine-tuning lightweight adapters" approach, where additional parameters are added, and only these new parameters are fine-tuned while the base model remains frozen <a class="yt-timestamp" data-t="00:13:10">[00:13:20]</a>. This strategy is expected to become the dominant method for fine-tuning larger models in the future, as full fine-tuning becomes increasingly impractical on consumer hardware <a class="yt-timestamp" data-t="00:13:05">[00:13:20]</a>.