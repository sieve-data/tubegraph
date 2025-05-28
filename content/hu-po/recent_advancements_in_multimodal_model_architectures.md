---
title: Recent Advancements in Multimodal Model Architectures
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

## Introduction to Multimodal Models
A modality refers to a type of data, such as images, text, or speech. A [[overview_of_multimodal_models | multimodal model]] is designed to process and understand multiple data modalities simultaneously [00:04:41]. Recent advancements in this field are pushing the boundaries of what AI can achieve, moving beyond simple text-only or image-only models to more integrated systems that can handle complex, real-world interactions.

## Early Fusion vs. Late Fusion Approaches
Traditionally, many [[multimodal_large_language_models | multimodal models]], particularly [[multimodal_large_language_models | Vision Language Models]] (VLMs), have adopted a "late fusion" approach. This typically involves using a pre-trained vision encoder (e.g., DINO or CLIP) and a pre-trained language model (e.g., LLaMA 17B or Mistral 7B) [00:08:13]. These separate components are then "glued" together with an additional projection or adapter layer that converts visual representations into tokens suitable for the language model [00:08:53]. This method leverages existing pre-trained models, reducing the computational resources required for training [00:10:49].

However, a new "early fusion" approach is emerging, as exemplified by Meta's Chameleon model [00:05:17].

## Chameleon: An Early Fusion Foundation Model
Chameleon, developed by Meta AI Research, is a family of early fusion, token-based mixed-modal models [00:05:17]. Unlike traditional VLMs, Chameleon is trained from scratch in an end-to-end fashion [00:07:09]. In this architecture, all modalities (text and images) are projected into a shared representation space almost immediately, allowing for seamless reasoning and generation across modalities [00:07:21].

### Key Capabilities and Performance
Chameleon demonstrates impressive capabilities, including:
- Visual question answering [00:05:28]
- Image captioning [00:05:30]
- Text generation [00:05:30]
- Image generation [00:05:31]
- Long-form mixed-modal generation [00:05:32]

A significant new capability is its ability to generate interleaved text and images within the output [00:05:59]. This means the model can output a sequence of text tokens followed by image tokens, then more text, and so on [00:15:51].

Chameleon 34B has shown remarkable performance:
- It outperforms LLaMA 2 even on text-only benchmarks, suggesting that training on mixed modalities can lead to better unimodal performance [00:11:57]. This indicates that interleaving modalities increases the variance of the dataset, providing information from images that is not available in text and vice-versa, leading to stronger models [00:12:10].
- It matches or exceeds the performance of much larger models, including Gemini Pro and GPT-4V [00:06:26].
- In human pairwise comparisons, Chameleon 34B is preferred over GPT-4V 46% of the time, while GPT-4V is preferred only 22% of the time, positioning Chameleon as a potential [[stateoftheart_video_generation_and_multimodal_models | state-of-the-art multimodal model]] [00:13:37].

### Architecture and Training Specifics
- **Tokenization**: Chameleon employs new, specially trained image and text tokenizers [00:17:08].
    - The image tokenizer encodes 512x512 images into 1024 discrete tokens with a codebook size of 8,192 [00:17:31]. A current weakness is its difficulty in reconstructing images with large amounts of tiny text due to resolution limitations [00:29:25].
    - The text tokenizer uses a vocabulary size of 65,000 [00:18:30].
- **Training Challenges**: Training a model from scratch with early fusion presents new challenges, such as "logit drift" or modality competition [00:33:00]. This occurs when different modalities, having varying entropy, compete during training. Meta addressed this by introducing Dropout after attention and feed-forward layers, and applying query-key normalization (attention Norm) [00:33:29].
- **Massive Scale**: Chameleon 34B was trained with monstrous global batch sizes (2^23 tokens for 7B, 3^22 tokens for 34B) [00:35:20]. This scale was possible due to Meta's Research SuperCluster, comprising over 3,000 Nvidia A100 GPUs connected via Nvidia Quantum InfiniBand, enabling advanced model and data parallelism [01:40:09]. This level of compute is currently accessible to only a few companies [00:36:10].

## Mirasol 3B: Integrating Video and Audio
Google DeepMind's Mirasol 3B paper explores a different dimension of multimodal integration, focusing on video and audio modalities alongside text. This model is significant as it tackles the more complex challenge of time-aligned and contextual modalities [00:43:03].

### Modalities and Architecture
Mirasol 3B consumes video, audio, and text, and outputs text [00:43:03]. It partitions video and audio sequences into consecutive snippets [00:44:02]. A key innovation is representing audio as a spectrogram [00:50:09], which is an image representation of sound. This allows the model to reuse a single vision Transformer backbone to encode both video frames and audio spectrograms, optimizing parameter usage [00:50:57].

The model also uses a "combiner" mechanism, which is a Transformer, to jointly model audio-vision information and produce compact representations [00:45:24]. Training involves a reconstruction loss on masked audio-visual tokens to pre-train the encoders from scratch [01:05:17].

### The Token Turing Machine
A crucial, yet somewhat "buried," aspect of the Mirasol 3B paper is the concept of a "Token Turing Machine" [00:59:09]. This recurrent sequential model, built with Transformers, maintains an external memory [00:59:43]. It processes input features along with information from its memory, generates intermediate outputs, and then uses these outputs to update the memory and produce the final output [01:00:07].

This external memory addresses the limitation of traditional Transformers, where computation scales quadratically with sequence length (O(T^2)). By maintaining a fixed-size memory, the Token Turing Machine achieves a constant time complexity with respect to the input sequence length (O(T)), similar to an LSTM [01:03:03]. This memory capability is vital for retaining information over longer durations and across different interactions, akin to the behavior observed in advanced models like GPT-4o, which can recall past events from a continuous stream of input [01:01:07].

## Future Directions for Multimodal and AGI Development
The current landscape shows a clear [[convergence_of_ai_models_across_modalities | convergence of AI models across modalities]]. While open-source efforts often rely on "gluing" pre-trained components, companies with vast resources like Meta and Google are investing in training end-to-end multimodal models from scratch [00:36:51].

The progression suggests:
- From text-only to image-text input, text-only output (early VLMs) [01:34:12].
- To interleaved image-text input, interleaved image-text output (Chameleon) [01:35:14].
- To audio-video-text input, text-audio output (Mirasol, GPT-4o, Google Astra) [01:36:31].

The ultimate goal, as suggested, is a single, end-to-end autoregressive model capable of consuming and generating any modality, including video, audio, and text, in an interleaved fashion [01:10:03]. This would lead to highly immersive AI experiences, such as a full audiovisual AI representation, potentially moving towards 3D-native outputs and integration with robotics through control tokens [01:18:03]. This approach aligns with the "bitter lesson" in AI, emphasizing simplicity in architecture combined with vast data and computational scale, rather than over-engineering with complex, specialized modules [01:30:18]. This trajectory points towards significant steps in [[future_directions_for_multimodal_and_agi_development | AGI development]].