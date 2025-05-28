---
title: Conditional music generation
videoId: SodPUNBFeMY
---

From: [[hu-po]] <br/> 

The task of [[conditional_audio_generation_from_text | conditional music generation]] involves creating musical pieces based on a given text description or other conditional inputs [00:01:16, 00:07:53]. This field requires modeling long-range sequences and handling the complex structures of harmonies and melodies from different instruments [00:08:00, 00:09:34]. Human listeners are highly sensitive to disharmony, making music generation a challenging task that leaves little room for melodic errors [00:09:37, 00:10:04].

## MusicGen: A Simple and Controllable Approach

[[music_generation_with_musicgen | MusicGen]], developed by Meta AI Research, is presented as a simple and controllable music generation model [00:00:44, 00:13:45]. It operates as a single-stage Transformer Language Model (LM) over several streams of compressed discrete music representations, or "tokens" [00:03:33, 00:04:42]. This single-stage approach aims to produce the final product in one inference step, unlike hierarchical or cascading models that require multiple stages [00:05:59, 00:06:29, 00:12:10].

### Key Features and Capabilities
*   **High-Quality Samples:** [[music_generation_with_musicgen | MusicGen]] is designed to generate "high quality samples," although a formal definition of this term is not provided [00:06:34, 00:06:36].
*   **Controllability:** The model allows for better control over the generated output by conditioning on both textual descriptions and/or melodic features [00:06:43, 00:10:06, 00:13:48]. Text conditioning provides a natural language interface for this control [00:10:26, 00:10:33].
*   **Accessibility:** [[music_generation_with_musicgen | MusicGen]] includes a [[github_repository_analysis_for_audio_generation | GitHub repo called AudioCraft]], a Colab notebook, and a Hugging Face demo, allowing users to describe and generate music [00:01:25, 00:01:31, 00:01:33, 00:01:37]. The model weights are also released [00:03:27].

## Technical Foundations

### Audio Tokenization
To make audio modeling more tractable, recent studies, including [[music_generation_with_musicgen | MusicGen]], represent audio signals as multiple streams of discrete tokens [00:11:07, 00:11:10]. [[music_generation_with_musicgen | MusicGen]] specifically uses the EnCodec audio tokenizer, which is a convolutional autoencoder that quantizes its latent space using Residual Vector Quantization (RVQ) [00:29:46, 00:30:22, 00:33:51].
*   **Sampling Rate:** While standard music recordings are often 44 kHz or higher (up to 192 kHz), speech can be 16 kHz [00:08:24, 00:08:50, 00:14:55]. [[music_generation_with_musicgen | MusicGen]] generates music at 32 kHz [00:14:34]. The EnCodec model reduces this high sampling rate (FS) to a much lower frame rate (FR) of 50 Hz for its token representation [00:33:07, 01:28:02, 01:28:16].
*   **Residual Vector Quantization (RVQ):** This technique involves quantizing an audio stream, then quantizing the "residual" (the difference between the quantized and original signal), and repeating this process for increasing levels of refinement [00:25:40, 00:26:12, 00:31:47, 02:29:29]. [[music_generation_with_musicgen | MusicGen]] uses four quantizers, meaning four quantization levels or "codebooks" [01:28:57, 02:22:31]. The first codebook contains the most significant portion of the signal, with subsequent codebooks capturing finer details [02:22:31, 02:23:54].

### Codebook Interleaving Patterns
A significant contribution of [[music_generation_with_musicgen | MusicGen]] lies in its efficient "codebook interleaving strategies" [01:03:51, 02:10:35]. The challenge with RVQ is that the different quantization levels are dependent on each other, making parallel prediction difficult [00:52:03, 00:55:09]. To balance quality and computational speed, [[music_generation_with_musicgen | MusicGen]] explores various strategies for predicting these parallel discrete token sequences:
*   **Flattening:** This approach concatenates all codebooks into one giant vector and predicts them sequentially. While it can achieve good scores, it is computationally expensive, requiring significantly more autoregressive steps (e.g., 6,000 steps for 30 seconds of audio) [00:49:31, 00:59:56, 02:00:03, 02:00:07, 02:04:03].
*   **Parallel Pattern:** Predicts all codebooks simultaneously, implicitly assuming independence. This is faster but may miss dependencies [01:00:51, 01:53:51, 02:03:30].
*   **Delay Pattern:** Introduces an offset or "delay" between codebooks (e.g., shifting the second, third, and fourth codebooks by one step) [01:02:21, 02:00:29, 02:13:51]. This allows for more parallel processing while acknowledging some dependency, leading to fewer autoregressive steps (e.g., 1,500 steps for 30 seconds of audio) [00:53:33, 02:00:30, 02:10:40].
*   **Valley Pattern:** First predicts the initial codebook for all time steps sequentially, then predicts the remaining codebooks (two, three, and four) in parallel [01:52:54, 02:03:44].

The choice of interleaving pattern is a trade-off between computational cost and modeling exact dependencies [00:52:39, 01:04:03, 02:04:10, 02:24:15]. While flattening improves generation quality, it comes at a high computational cost; similar performance can often be achieved with faster, more efficient patterns like the delay pattern [02:04:10, 02:04:14].

### Model Architecture
[[music_generation_with_musicgen | MusicGen]] utilizes an autoregressive Transformer-based decoder [01:19:19, 01:28:9].
*   **Positional Embedding:** A sinusoidal embedding encodes the current time step, providing positional information to the model [01:14:54, 01:15:57].
*   **Layers:** Each layer consists of a causal self-attention block and a cross-attention block [01:16:13, 01:17:06]. The cross-attention is fed with the conditioning signal [01:17:22].
*   **Feed-Forward Networks:** Layers also include a fully connected block (linear layer with a ReLU activation) wrapped with residual skip connections [01:18:49, 01:19:42].
*   **Normalization:** Layer normalization is applied to each block before summation (pre-norm) [01:20:25, 01:20:59].

## Conditioning Methods

### Text Conditioning
Text descriptions are transformed into a conditioning tensor using pre-trained text encoders. [[music_generation_with_musicgen | MusicGen]] experiments with:
*   T5 encoder [01:06:53, 01:40:09]
*   Flan T5 [01:07:17]
*   CLAP (a joint text-audio representation, similar to CLIP for image-text) [01:07:05, 01:07:15]

Text pre-processing includes normalizing text by omitting stop words and lemmatizing the remaining text [01:40:01, 01:40:08]. Additional annotations like musical key, BPM, and tags can be concatenated to the text description [01:40:14, 01:40:21, 01:41:07]. Techniques like word dropout and text description dropout are used for data augmentation during training [01:40:23, 01:40:40, 01:40:42].

### Melody Conditioning
[[music_generation_with_musicgen | MusicGen]] introduces an unsupervised approach for [[conditional_audio_generation_from_text | melody conditioning]] [01:04:00, 01:11:01, 01:11:09, 02:10:54].
*   **Chromogram:** Melodic structure is conveyed by jointly conditioning on the input chromogram, which is a 2D representation of audio (time on the x-axis, frequency bins on the y-axis) [01:09:10, 01:09:19, 01:11:01].
*   **Information Bottleneck:** To simplify conditioning, an information bottleneck is introduced by choosing only the dominant time-frequency bin (using ARG Max) in the chromogram at each step [01:10:26, 01:10:28, 01:10:30, 01:42:01, 01:42:08]. This effectively turns the 2D chromogram into a 1D sequence for conditioning [01:18:27, 01:18:32].
*   **Input Prefix:** The conditioned chromogram (as a 1D sequence) is provided as a prefix to the Transformer input [01:17:37, 01:17:49, 01:18:45].
*   **Guidance Scale:** A guidance scale parameter allows controlling the strength of this conditioning [01:42:42, 01:43:07].

## Training and Evaluation

### Training Setup
*   **Dataset:** [[music_generation_with_musicgen | MusicGen]] was trained on 20,000 hours of licensed music, including an internal dataset and music from Shutterstock and Pond5 [01:43:17, 01:43:21, 01:43:42].
*   **Audio Length:** Models were trained on 30-second audio crops sampled randomly [01:34:06].
*   **Optimization:** Training involved 1 million steps using the AdamW optimizer with a batch size of 192 [01:34:10, 01:34:12, 01:34:17, 01:34:19]. Decoupled weight decay (0.1) and gradient clipping (1.0) were applied [01:34:22, 01:35:15]. A cosine learning rate schedule with a 4,000-step warm-up was used [01:36:56, 01:37:00, 01:37:18]. Exponential moving average with a decay of 0.99 was also used [01:37:35, 01:37:38].
*   **Model Sizes:** Models of 300 million, 1.5 billion, and 3.3 billion parameters were trained [01:32:38, 01:33:50, 02:11:15]. Ablation studies were primarily performed on the 300 million parameter model [01:33:50, 01:59:53].
*   **Efficiency:** Memory-efficient Flash Attention was employed to improve speed and memory usage [01:42:44]. Mixed precision training (using FP16 and BFloat16) was utilized [01:38:12, 01:38:33].
*   **Sampling:** Top-K sampling was employed for generation [01:39:29].

### Evaluation Metrics
[[music_generation_with_musicgen | MusicGen]] used both objective (automatic) and subjective (human) metrics for evaluation [01:44:37, 01:52:58].

*   **Objective Metrics:**
    *   **Fréchet Audio Distance (FAD):** Measures the plausibility of generated audio [01:48:42, 01:50:01].
    *   **KL Divergence:** Computes the difference between probability distributions of labels from an audio classifier for original and generated music [01:48:46, 01:50:08].
    *   **CLAP Score:** Quantifies audio-text alignment between the text description and generated audio [01:48:54, 01:51:56].
    *   **Chroma Cosine Similarity:** A new metric measuring the average cosine similarity between frames of quantized chromograms of reference and generated samples [01:58:43].

*   **Subjective Metrics:**
    *   **Overall Quality (OVL):** Human raters assessed the perceptual quality on a scale of 1 to 100 [01:53:33, 01:53:35].
    *   **Relevance to Text (REL):** Human raters evaluated how well the generated music matched the text input [01:52:40, 01:52:43].
    *   **Melody Matching:** Listeners rated how well the generated melody matched a reference piece on a scale of 1 to 100 [01:59:26, 01:59:34].

Evaluation results indicated that [[music_generation_with_musicgen | MusicGen]] generally performs better than re-implemented baselines on objective metrics [01:57:00, 01:57:03]. However, human evaluations suggested that the quality was roughly on par with other models, with little significant difference noticed by human raters across different model sizes or codebook patterns [02:00:54, 02:01:05, 02:01:18, 02:01:21, 02:01:48, 02:25:35, 02:25:59]. Interestingly, the choice of text encoder (e.g., T5 vs. Flan T5) appeared to have a significant impact on quality metrics [02:15:31, 02:16:02].

## Ethical Considerations
Meta AI acknowledges several ethical considerations regarding large-scale generative models like [[music_generation_with_musicgen | MusicGen]]:
*   **Data Licensing:** The use of licensed music (from Shutterstock and Pond5) highlights ongoing discussions about intellectual property in AI training [01:43:17, 02:11:20, 02:12:09].
*   **Data Diversity:** The training dataset predominantly contains Western-style music, potentially leading to a lack of diversity in generated outputs [02:12:23, 02:12:26].
*   **Artist Competition:** Generative models pose a potential threat of unfair competition for human artists [02:12:31, 02:12:33].
*   **Open Research:** The authors advocate for open research to ensure equal access to these models for all actors [02:12:42, 02:12:44].