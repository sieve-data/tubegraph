---
title: Quantization Techniques for Transformers
videoId: HcE3I_iCvoI
---

From: [[hu-po]] <br/> 

[[Diffusion models and Transformers | Transformer]] models are becoming increasingly powerful and capable, and simultaneously, they are shrinking in size <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This development is making the future of AI very interesting, as smaller, smarter models will be accessible to more people <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. If models only improved with size, their control would remain with those who have the resources to run large models <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. However, advancements in [[quantization and optimization in machine learning | quantization and optimization in machine learning]] are enabling models to become smaller without significant sacrifice in intelligence <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Uncovering Redundancy in Transformers

Recent research indicates that [[Diffusion models and Transformers | Transformer]] architectures contain significant redundancy, particularly within their attention layers <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This redundancy contributes to inefficiencies in deployment cost and resource demands <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

### Key Papers and Findings

Two papers highlight this redundancy:
*   **"What Matters in Transformers: Not All Attention Is Needed"** (University of Maryland, October 17, 2024) <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This empirical study investigates redundancy across [[Diffusion models and Transformers | Transformer]] modules, including blocks, MLP, and attention layers <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **"Pyramid-Drop: Accelerating your Large Vision-Language Models via Pyramid Visual Redundancy Reduction"** (Shanghai AI Laboratory, USC, CK, October 22, 2024) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. This paper explores redundancy specifically in vision language models (VLMs or LVLMs) <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

#### Experimental Methodology

The research involves "dropping out" or deleting different parts of a trained [[Diffusion models and Transformers | Transformer]] model to observe which components are crucial for performance <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is akin to an ablation study <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Block removal** entails removing entire [[Diffusion models and Transformers | Transformer]] blocks <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **MLP dropping** involves removing the Multi-Layer Perceptron (feed-forward network) component <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Attention dropping** removes the attention layer <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

#### Key Observations on Redundancy

*   **Attention Layer Pruning**: A significant portion of attention layers exhibit high similarity and can be pruned without degrading performance <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. For example, Llama 2 70B achieved a 50% speed-up with only a 3% performance drop by pruning half of its attention layers <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **MLP vs. Attention**: Removing entire blocks or dropping MLP layers generally leads to significant performance degradation <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, whereas dropping attention layers does not <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. More than 50% of attention layers can be dropped with comparable performance to the full model, indicating high redundancy <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **Similarity-Based Dropping**: The decision of what to drop is often based on similarity scores, such as cosine similarity, which identifies redundant features <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. If features are highly similar, they are considered redundant and can be removed <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Depth-Dependent Redundancy**: In vision models, redundancy progressively increases in deeper layers <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. Shallow layers (closer to input) require more tokens, while deeper layers (closer to output) can have more aggressively dropped tokens <a class="yt-timestamp" data-t="00:28:30">[00:28:30]</a>.
    *   This is akin to convolutional neural networks (CNNs), which have an inductive bias to reduce the number of features as layers deepen <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
*   **Visual Redundancy**: Images exhibit substantial spatial redundancy <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>. For instance, large areas of sky in an image translate to many redundant "sky tokens" in a [[Diffusion models and Transformers | Transformer]]'s input sequence, leading to wasted attention computations <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. This quadratic increase in image tokens with resolution further exacerbates computational costs <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
*   **Performance Improvements**: Removing redundant tokens can significantly accelerate training time (40% for LLaVA-Next) and inference FLOPs (55% for LLaVA-Next) <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. Intriguingly, in some cases, dropping parts of the model can *improve* performance <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. This counters the "scale is all you need" mindset <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
*   **Layer Importance**: The first and last layers of MLP and attention components are generally more important than the middle layers <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>. This "last layer effect" implies that the final layer, responsible for output representations, should be largely preserved <a class="yt-timestamp" data-t="00:38:02">[00:38:02]</a>.

#### Why Redundancy May Be Beneficial

The inherent redundancy in [[Diffusion models and Transformers | Transformer]] models might be a reason for their broad applicability across modalities and problems <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. A highly redundant architecture offers many paths for information and gradients to flow, making the training process more robust to finding effective weight sets <a class="yt-timestamp" data-t="00:40:12">[00:40:12]</a>. This is similar to the effect of [[finetuning with quantized models | Dropout]], which promotes redundant information to enhance robustness <a class="yt-timestamp" data-t="00:41:45">[00:41:45]</a>.

Models can also "sneak" information into seemingly unrelated tokens or parts of the input, such as corner pixels in images <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>. This behavior, observed in studies like ViT registers, is an emergent property where the model finds ways to pack critical information into less "useful" tokens to ensure it propagates through the network <a class="yt-timestamp" data-t="00:43:09">[00:43:09]</a>.

## Advancements in Model Efficiency Through Quantization

Another significant area for making [[Diffusion models and Transformers | Transformer]] models smaller and faster is [[quantization and optimization in machine learning | quantization]].

### OneBit AI Infra

The paper **"OneBit AI Infra Part 1.1: Fast and Lossless BitNet b1.58 Inference on CPUs"** (Microsoft Research, October 21, 2024) explores extremely low-bit [[quantization for large language models | quantization for large language models]] <a class="yt-timestamp" data-t="00:46:58">[00:46:58]</a>.

#### Core Concept: Reducing Precision

*   **1-Bit Weights**: Instead of storing model weights as high-precision floating-point numbers (e.g., 16-bit or 32-bit), [[quantization in large language models | quantization in large language models]] reduces them to very low-bit values, such as -1, 0, or 1 <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>. This drastically saves memory and bandwidth <a class="yt-timestamp" data-t="00:53:32">[00:53:32]</a>.
*   **Computational Efficiency**: Smaller data types mean faster retrieval and processing during matrix multiplications, which are fundamental to [[Diffusion models and Transformers | deep learning]] workloads <a class="yt-timestamp" data-t="00:54:03">[00:54:03]</a>.
*   **Custom Kernels**: The paper introduces specialized kernels for CPUs (x86 and ARM) to support fast and lossless inference of these [[2bit quantization for machine learning models | 2bit quantization for machine learning models]] models <a class="yt-timestamp" data-t="00:52:09">[00:52:09]</a>. This leads to up to a 6X speed-up on x86 CPUs and a 5X speed-up on ARM CPUs <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>.
*   **Lookup Tables**: By limiting the possible values of weights, matrix multiplications can be replaced by pre-calculated lookup tables <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>. This ancient optimization technique, used even before computers, significantly reduces computation cost <a class="yt-timestamp" data-t="00:56:07">[00:56:07]</a>.

#### Benefits of Low-Bit Quantization

*   **Reduced Training & Inference Costs**: Low-bit [[quantization and optimization in machine learning | quantization]] greatly reduces the energy and computational cost of both training and inference <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a>.
*   **Hardware Accessibility**: The ability to run [[Diffusion models and Transformers | Transformer]] models efficiently on CPUs is a massive unlock <a class="yt-timestamp" data-t="01:28:30">[01:28:30]</a>. This allows utilizing existing CPU-heavy data centers and running powerful AI on older or resource-constrained devices like cell phones or Raspberry Pis <a class="yt-timestamp" data-t="01:28:38">[01:28:38]</a>.
*   **Performance Retention/Improvement**: Like pruning, low-bit [[quantization and optimization in machine learning | quantization]] can achieve significant speed-ups with negligible or even *improved* performance <a class="yt-timestamp" data-t="01:04:53">[01:04:53]</a>.
*   **Portability and Privacy**: Techniques like Post-Training [[quantization and optimization in machine learning | Quantization]] (PTQ) and SpinQuant allow [[quantization for large language models | quantization]] without requiring access to the original training datasets <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>. This enables private [[quantization for large language models | quantization]] on user devices or corporate clouds, keeping data localized <a class="yt-timestamp" data-t="01:06:52">[01:06:52]</a>.

## Implications for AI Deployment

The combination of reducing architectural redundancy and applying advanced [[quantization and optimization in machine learning | quantization]] techniques suggests a future where powerful AI models are extremely small and efficient <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>. These "tiny Transformers" can run on systems with limited resources, such as older GPUs, CPUs, or even cell phones <a class="yt-timestamp" data-t="01:00:36">[01:00:36]</a>. This trend promises to democratize access to advanced AI, making it ubiquitous and difficult to control centrally <a class="yt-timestamp" data-t="01:29:45">[01:29:45]</a>.