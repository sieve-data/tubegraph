---
title: Comparison of Mamba models in language and vision contexts
videoId: 9s-9aSobky8
---

From: [[hu-po]] <br/> 

Mamba models, formally known as Selective State Space Models (SSMs), are gaining prominence in AI due to their efficient linear time complexity, offering significant speed and memory advantages over traditional Transformer architectures <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>, which exhibit quadratic complexity <a class="yt-timestamp" data-t="03:59:02">[03:59:02]</a>. This article explores the [[comparison_of_vision_architectures | application of Mamba models]] across different modalities, specifically in language, vision, and 3D reconstruction, examining three recent models: Jamba, Cobra, and Gamba.

## Mamba Fundamentals

State Space Models (SSMs) are linear time-invariant systems of equations that capture the dynamics of a system's state variable <a class="yt-timestamp" data-t="04:52:03">[04:52:03]</a>. The distinguishing feature of Mamba, referred to as "selective," is that the parameters (B, delta, and C matrices) are functions of the input, allowing for input-dependent dynamics <a class="yt-timestamp" data-t="05:54:02">[05:54:02]</a>. This mechanism is somewhat analogous to the attention mechanism in Transformers, where queries and keys select relevant values <a class="yt-timestamp" data-t="06:14:40">[06:14:40]</a>.

A key advantage of Mamba models over Transformers lies in how they handle sequence length. In a Transformer, the computation scales quadratically with sequence length due to the attention matrix, leading to a "big giant square" <a class="yt-timestamp" data-t="07:11:15">[07:11:15]</a>. In contrast, Mambas maintain a constant-sized hidden state (memory) as they process the input sequence, leading to linear computational growth relative to the input sequence size <a class="yt-timestamp" data-t="07:13:59">[07:13:59]</a>. This makes them significantly more efficient <a class="yt-timestamp" data-t="07:17:39">[07:17:39]</a>.

## Gamba: Mambas in 3D Reconstruction

Gamba is a model designed for single-view 3D reconstruction, transforming a single image into a three-dimensional representation, specifically Gaussian Splats <a class="yt-timestamp" data-t="04:04:06">[04:04:06]</a>.
It utilizes a Mamba-based sequential network for this process <a class="yt-timestamp" data-t="04:05:07">[04:05:07]</a>.

### Architecture and Performance
The Gamba model takes a single image as input, processes it through a component called the "Gamba model," and outputs three-dimensional Gaussians, which can then be rendered into new images <a class="yt-timestamp" data-t="06:45:07">[06:45:07]</a>. The output is a fixed-length sequence of 16,384 3D Gaussians <a class="yt-timestamp" data-t="06:04:05">[06:04:05]</a>.

While Gamba demonstrates the feasibility of using Mambas for 3D reconstruction, its performance in terms of quality is not state-of-the-art, partially because it was pre-trained on a smaller dataset (OmniObject3D) compared to widely adopted ones like Obverse <a class="yt-timestamp" data-t="06:06:06">[06:06:06]</a>. However, its main strength is speed: it can reconstruct a 3D object in about 6 seconds on a single Nvidia A100 GPU <a class="yt-timestamp" data-t="06:37:09">[06:37:09]</a>.

### Design Choices and Limitations
A notable design choice is that Gamba's image tokenizer, DINO, is based on a Vision Transformer <a class="yt-timestamp" data-t="07:27:07">[07:27:07]</a>. This means the architecture is not *entirely* Mamba-based, which some critics suggest might be a missed opportunity to fully leverage Mamba's efficiency throughout the pipeline <a class="yt-timestamp" data-t="07:29:07">[07:29:07]</a>. Additionally, the model incorporates camera pose tokens (extrinsic and intrinsic camera parameters), which are often unavailable in real-world applications, limiting its practical deployment <a class="yt-timestamp" data-t="07:43:05">[07:43:05]</a>. The paper also incorrectly states that Mamba has an inherent unidirectional scan order, whereas other Mamba papers have shown the possibility of multi-directional scans for better performance <a class="yt-timestamp" data-t="07:44:06">[07:44:06]</a>.

## Cobra: Mambas in Vision Language Models (VLMs)

Cobra extends Mamba to [[vision_language_models_in_ai_agents | multimodal large language models]] (MLLMs or VLMs), which consume image and text tokens to answer questions <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>.

### Architecture and Performance
Cobra aims for linear computational complexity in MLLMs <a class="yt-timestamp" data-t="03:16:04">[03:16:04]</a>. Similar to Gamba, Cobra uses pre-trained Vision Transformers (DINO and SigLip) as its image encoders <a class="yt-timestamp" data-t="03:41:07">[03:41:07]</a>, then combines their representations before feeding them into a Mamba-based language model backbone composed of 64 Mamba blocks <a class="yt-timestamp" data-t="03:44:07">[03:44:07]</a>.

Cobra boasts "extremely competitive performance" against other computationally efficient VLM models like Lava, Fi, TinyLlama, and MobileVLM V2 <a class="yt-timestamp" data-t="03:52:07">[03:52:07]</a>. It achieves comparable performance to Lava while using approximately 43% fewer parameters <a class="yt-timestamp" data-t="03:53:07">[03:53:07]</a>. The most significant benefit is its speed: Cobra processes 166 tokens per second, significantly faster than Transformer-based models like MobileVLM Tiny (39 tokens/sec) and Lava (40 tokens/sec) <a class="yt-timestamp" data-t="04:00:07">[04:00:07]</a>. This speed makes Mamba-based VLMs particularly promising for time-sensitive [[integration_of_vision_language_models_in_robotics | applications like visual-based robotic feedback control]] <a class="yt-timestamp" data-t="04:46:07">[04:46:07]</a>.

### Training and Design
Cobra discards the multi-stage training procedures common in earlier VLMs like Lava, opting to fine-tune the entire language model backbone and the projector (which connects image encoders to the language model) simultaneously <a class="yt-timestamp" data-t="03:59:07">[03:59:07]</a>. The model's training data often involves distilling knowledge from more powerful models like GPT-4 Vision <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>.

## Jamba: Hybrid Mambas in Language Models

Jamba is an open-source [[large_language_models_in_robotics | large language model]] developed by AI21, characterized by its hybrid architecture that integrates both Mamba and Transformer blocks <a class="yt-timestamp" data-t="05:00:07">[05:00:07]</a>.

### Architecture and Performance
Jamba's architecture alternates between Mamba blocks and "Mamba plus MoE" (Mixture of Experts) blocks <a class="yt-timestamp" data-t="05:14:07">[05:14:07]</a>. Mixture of Experts allows the model to selectively activate subsets of its parameters during inference, reducing the active parameter count while retaining a large total parameter count <a class="yt-timestamp" data-t="05:20:07">[05:20:07]</a>. For example, Jamba has 52 billion total parameters but only draws upon 12 billion during inference <a class="yt-timestamp" data-t="05:17:07">[05:17:07]</a>.

Jamba's performance is competitive with other leading open-source models like Mixtral, Gemma, and Llama, showing slight improvements in certain reasoning benchmarks <a class="yt-timestamp" data-t="05:29:07">[05:29:07]</a>. A significant benefit of its Mamba components is the ability to handle large context windows, up to 140k tokens <a class="yt-timestamp" data-t="05:43:07">[05:43:07]</a>. The model is specifically optimized for Nvidia A100 GPUs <a class="yt-timestamp" data-t="05:46:07">[05:46:07]</a>, which are commonly used in AI research and development <a class="yt-timestamp" data-t="05:54:07">[05:54:07]</a>.

## Cross-Cutting Observations and Challenges

### Hybrid Architectures and Vision Encoders
A common theme across Gamba and Cobra is the integration of Mamba blocks into larger architectures that still rely on pre-trained Transformer-based image encoders (like DINO V2 and SigLip) <a class="yt-timestamp" data-t="07:27:07">[07:27:07]</a>. While this allows leveraging existing powerful vision models, it means the entire pipeline isn't fully Mamba-optimized. Developing a Mamba-based vision encoder that can match the performance of Transformer-based ones would be a significant step towards fully Mamba-native [[vision_mamba_model_designs | vision models]] <a class="yt-timestamp" data-t="07:29:07">[07:29:07]</a>.

### Quantization Limitations: An Achilles' Heel?
A critical potential limitation for Mamba models, observed in both Cobra and Jamba, is their sensitivity to numerical precision <a class="yt-timestamp" data-t="05:57:07">[05:57:07]</a>. Cobra states that its Mamba recurrent dynamics require maintaining relatively high precision (no lower than bf16) during inference <a class="yt-timestamp" data-t="06:05:07">[06:05:07]</a>. Similarly, Jamba's documentation recommends excluding Mamba blocks from quantization to 8-bit precision to avoid degrading model quality <a class="yt-timestamp" data-t="07:51:07">[07:51:07]</a>.

This suggests a significant challenge for Mambas: while Transformers can be highly quantized (e.g., down to 1.58 bits) without substantial performance loss, making them extremely memory-efficient and fast for deployment on edge devices, Mambas might not tolerate such low precision <a class="yt-timestamp" data-t="06:00:07">[06:00:07]</a>. If this proves to be an inherent limitation, it could hinder the widespread adoption of Mambas in memory-constrained or ultra-low-latency environments, despite their theoretical speed advantages <a class="yt-timestamp" data-t="06:14:07">[06:14:07]</a>. Further research is needed to determine if this is a fundamental weakness or a solvable problem <a class="yt-timestamp" data-t="06:17:07">[06:17:07]</a>.

### Broader [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | Applications of Mambas in AI]]
The exploration of Mambas in 3D reconstruction, [[video_mamba_for_video_understanding | vision language models]], and traditional large language models demonstrates their versatility across different data modalities and problem spaces <a class="yt-timestamp" data-t="01:47:07">[01:47:07]</a>. Their speed and efficiency make them particularly appealing for real-time [[integration_of_vision_language_models_in_robotics | robotics]] and [[limitations_and_potential_of_mamba_models_in_ai | other time-sensitive applications]]. The ongoing development of hybrid architectures, as seen in Jamba, suggests a pragmatic approach to leveraging the strengths of both Mambas and Transformers, while the quantization challenge remains a key area for future research to unlock their full potential <a class="yt-timestamp" data-t="07:57:07">[07:57:07]</a>.