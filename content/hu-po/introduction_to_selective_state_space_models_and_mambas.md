---
title: Introduction to selective state space models and mambas
videoId: 9s-9aSobky8
---

From: [[hu-po]] <br/> 

Mamba models, formally known as Selective State Space Models (SSMs), are a new architectural paradigm in artificial intelligence designed for efficient sequence modeling. They are gaining prominence for their computational speed and reduced memory footprint compared to traditional transformer models <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The name "Mamba" was chosen to reflect their fast processing capabilities, akin to a fast snake <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## What are State Space Models (SSMs)?

[[state_space_models_vs_attentionbased_models | State space models]] are linear time-invariant systems of equations that capture the dynamics of a system's state variable <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. They process input sequences one element at a time, maintaining a hidden state (memory) that accumulates historical information <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

The fundamental equation for an SSM can be thought of as the "attention equation for Mambas" <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. It involves matrices (A, B, C) that define how the hidden state `H` is updated based on the input `X` and how the output `Y` is derived from the hidden state <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. A key aspect is the conversion from a continuous-time system to a discrete-time system, introducing a sampling period Delta (`Δt`) <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### The "Selective" Aspect

The "selective" part of Selective State Space Models is their primary contribution <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. In Mambas, the `B`, `Δt`, and `C` matrices are functions of the input (`X`) <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. This means the model's internal dynamics are input-dependent, allowing it to selectively determine which parts of the hidden state are relevant or how much new information to incorporate <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This concept is analogous to how the query and key matrices in a Transformer's attention mechanism select relevant values <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

### Efficiency: Linear vs. Quadratic Scaling

The main advantage of Mambas over Transformers lies in their computational efficiency:
*   **Transformers** exhibit quadratic complexity with respect to the input sequence length <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. This means their computational and memory requirements grow rapidly as the sequence length increases, leading to slow inference and large memory footprints for long contexts <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>.
*   **Selective State Space Models** maintain a constant-sized hidden state (`H`) regardless of the input sequence length <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. This leads to linear growth in computational and memory requirements with respect to the input sequence length <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This linear scaling makes Mambas significantly faster, especially for long sequences <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.

### Comparison to Recurrent Neural Networks (RNNs) and LSTMs

SSMs share similarities with older recurrent neural networks (RNNs) and Long Short-Term Memory (LSTM) networks <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>. All these models carry a hidden state that accumulates information as they process sequences <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. However, Mambas offer a significant improvement in training efficiency. Traditional RNNs are slow to train because calculating gradients requires loading the entire sequence of hidden states backwards <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. Mambas, due to their specific implementation, can be treated almost like a convolutional network during training, allowing for more parallel computation on GPUs and making them much more efficient <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

A key distinction is that while LSTMs have fixed weights, Mambas use contextual (input-dependent) weights for `B`, `Δt`, and `C` <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

## Applications of Mamba Models

Mamba models are rapidly being integrated across various AI modalities:

*   **Language Models (Jamba)**: Jamba is an example of a hybrid language model that combines Mamba blocks with Transformer blocks, sometimes incorporating Mixture-of-Experts (MoE) layers <a class="yt-timestamp" data-t="00:50:08">[00:50:08]</a>. This hybrid approach aims to maximize both model quality and throughput on GPUs like the Nvidia A100 <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>.
*   **Vision Language Models (Cobra)**: Cobra demonstrates the use of Mambas in [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | multimodal large language models]] (MLLMs) that consume both image and text tokens <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. While the image encoders in these models often remain Transformer-based (e.g., DINO or SigLIP) <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>, the core language model backbone is composed of Mamba blocks, resulting in significantly faster inference (e.g., 166 tokens per second compared to ~40 for Transformer-based MLLMs) <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>.
*   **3D Reconstruction (Gamba)**: Gamba utilizes Mambas for [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | single-view 3D reconstruction]], specifically generating 3D Gaussian Splats from a single image <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Despite using a Transformer-based image tokenizer, the Mamba-based sequential network handles the generation of 3D representations, achieving reconstruction in about 6 seconds on an Nvidia A100 GPU <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Limitations and Potential

A potential [[limitations_and_potential_of_mamba_models_in_ai | Achilles' heel for Mambas]] has emerged in their [[challenges_with_quantization_of_mamba_architectures | quantization]] capabilities <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. While Transformer models can be heavily quantized to very low bit precisions (e.g., 1.58 bits per parameter) without significant performance degradation, Mamba models appear to struggle with this <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. Reports indicate that Mamba blocks need to maintain a relatively high precision, such as BF16 (16-bit floating point), and cannot be easily quantized to 8-bit or lower without degrading model quality <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>. This raises questions about whether Mambas can achieve the same memory and speed advantages as highly quantized Transformers in resource-constrained environments.

Despite this potential challenge, the inherent speed of Mamba models makes them highly attractive for time-sensitive applications like robotics and autonomous vehicles, where rapid processing of visual information is crucial for feedback control <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. Even if Mambas are slightly less accurate than Transformer models, their significant speed advantage can make them the preferred choice for such scenarios <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

The research and development in Mamba models are ongoing, with constant exploration of their capabilities and optimizations.## Introduction to Selective State Space Models (Mambas)

Mamba models, formally known as Selective State Space Models (SSMs), are a new architectural paradigm in artificial intelligence designed for efficient sequence modeling. They are gaining prominence for their computational speed and reduced memory footprint compared to traditional transformer models <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The name "Mamba" was chosen to reflect their fast processing capabilities, akin to a fast snake <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## What are State Space Models (SSMs)?

[[state_space_models_vs_attentionbased_models | State space models]] are linear time-invariant systems of equations that capture the dynamics of a system's state variable <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. They process input sequences one element at a time, maintaining a hidden state (memory) that accumulates historical information <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

The fundamental equation for an SSM can be thought of as the "attention equation for Mambas" <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. It involves matrices (A, B, C) that define how the hidden state `H` is updated based on the input `X` and how the output `Y` is derived from the hidden state <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. A key aspect is the conversion from a continuous-time system to a discrete-time system, introducing a sampling period Delta (`Δt`) <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

### The "Selective" Aspect

The "selective" part of Selective State Space Models is their primary contribution <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. In Mambas, the `B`, `Δt`, and `C` matrices are functions of the input (`X`) <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. This means the model's internal dynamics are input-dependent, allowing it to selectively determine which parts of the hidden state are relevant or how much new information to incorporate <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. This concept is analogous to how the query and key matrices in a Transformer's attention mechanism select relevant values <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

### Efficiency: Linear vs. Quadratic Scaling

The main advantage of Mambas over Transformers lies in their computational efficiency:
*   **Transformers** exhibit quadratic complexity with respect to the input sequence length <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. This means their computational and memory requirements grow rapidly as the sequence length increases, leading to slow inference and large memory footprints for long contexts <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>.
*   **Selective State Space Models** maintain a constant-sized hidden state (`H`) regardless of the input sequence length <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. This leads to linear growth in computational and memory requirements with respect to the input sequence length <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This linear scaling makes Mambas significantly faster, especially for long sequences <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>.

### Comparison to Recurrent Neural Networks (RNNs) and LSTMs

SSMs share similarities with older recurrent neural networks (RNNs) and Long Short-Term Memory (LSTM) networks <a class="yt-timestamp" data-t="00:31:59">[00:31:59]</a>. All these models carry a hidden state that accumulates information as they process sequences <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>. However, Mambas offer a significant improvement in training efficiency. Traditional RNNs are slow to train because calculating gradients requires loading the entire sequence of hidden states backwards <a class="yt-timestamp" data-t="00:33:05">[00:33:05]</a>. Mambas, due to their specific implementation, can be treated almost like a convolutional network during training, allowing for more parallel computation on GPUs and making them much more efficient <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

A key distinction is that while LSTMs have fixed weights, Mambas use contextual (input-dependent) weights for `B`, `Δt`, and `C` <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

## Applications of Mamba Models

Mamba models are rapidly being integrated across various AI modalities:

*   **Language Models (Jamba)**: Jamba is an example of a hybrid language model that combines Mamba blocks with Transformer blocks, sometimes incorporating Mixture-of-Experts (MoE) layers <a class="yt-timestamp" data-t="00:50:08">[00:50:08]</a>. This hybrid approach aims to maximize both model quality and throughput on GPUs like the Nvidia A100 <a class="yt-timestamp" data-t="00:56:37">[00:56:37]</a>.
*   **Vision Language Models (Cobra)**: Cobra demonstrates the use of Mambas in [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | multimodal large language models]] (MLLMs) that consume both image and text tokens <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. While the image encoders in these models often remain Transformer-based (e.g., DINO or SigLIP) <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>, the core language model backbone is composed of Mamba blocks, resulting in significantly faster inference (e.g., 166 tokens per second compared to ~40 for Transformer-based MLLMs) <a class="yt-timestamp" data-t="00:41:59">[00:41:59]</a>.
*   **3D Reconstruction (Gamba)**: Gamba utilizes Mambas for [[applications_of_mambas_in_3d_reconstruction_and_vision_language_models | single-view 3D reconstruction]], specifically generating 3D Gaussian Splats from a single image <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Despite using a Transformer-based image tokenizer, the Mamba-based sequential network handles the generation of 3D representations, achieving reconstruction in about 6 seconds on an Nvidia A100 GPU <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Limitations and Potential

A potential [[limitations_and_potential_of_mamba_models_in_ai | Achilles' heel for Mambas]] has emerged in their [[challenges_with_quantization_of_mamba_architectures | quantization]] capabilities <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>. While Transformer models can be heavily quantized to very low bit precisions (e.g., 1.58 bits per parameter) without significant performance degradation, Mamba models appear to struggle with this <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. Reports indicate that Mamba blocks need to maintain a relatively high precision, such as BF16 (16-bit floating point), and cannot be easily quantized to 8-bit or lower without degrading model quality <a class="yt-timestamp" data-t="01:07:38">[01:07:38]</a>. This raises questions about whether Mambas can achieve the same memory and speed advantages as highly quantized Transformers in resource-constrained environments.

Despite this potential challenge, the inherent speed of Mamba models makes them highly attractive for time-sensitive applications like robotics and autonomous vehicles, where rapid processing of visual information is crucial for feedback control <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. Even if Mambas are slightly less accurate than Transformer models, their significant speed advantage can make them the preferred choice for such scenarios <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

The research and development in Mamba models are ongoing, with constant exploration of their capabilities and optimizations.