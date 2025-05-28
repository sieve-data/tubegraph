---
title: Applications of mambas in 3D reconstruction and vision language models
videoId: 9s-9aSobky8
---

From: [[hu-po]] <br/> 

Mamba models, formally known as Selective State Space Models (SSMs), represent a significant architectural shift in deep learning, offering linear computational complexity with respect to sequence length, as opposed to the quadratic complexity of traditional Transformers <a class="yt-timestamp" data-t="06:22:07">[06:22:07]</a>. This efficiency translates into faster inference speeds and reduced memory footprint, making them highly appealing for various AI applications <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>, <a class="yt-timestamp" data-t="06:13:00">[06:13:00]</a>. Recent research demonstrates the growing utility of Mamba models across different modalities, including 3D reconstruction and [[vision_language_models_and_their_applications | vision language models]] (VLMs).

## Mambas for 3D Reconstruction: Gamba

The Gamba model showcases the application of Mambas in single-view 3D reconstruction <a class="yt-timestamp" data-t="04:04:06">[04:04:06]</a>. This task involves generating a 3D representation of an object from a single input image <a class="yt-timestamp" data-t="04:15:19">[04:15:19]</a>.

### Gamba Architecture and Process
Gamba operates as an end-to-end amortized 3D reconstruction model <a class="yt-timestamp" data-t="04:29:10">[04:29:10]</a>. It utilizes a Mamba-based sequential network to process image tokens and convert them into 3D Gaussian Splats <a class="yt-timestamp" data-t="04:33:47">[04:33:47]</a>, <a class="yt-timestamp" data-t="06:56:06">[06:56:06]</a>.

The process involves:
1.  **Image Tokenization:** A single input image is fed into a pre-trained image tokenizer, specifically the Dino V2 Vision Transformer <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>, <a class="yt-timestamp" data-t="01:18:25">[01:18:25]</a>, <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. This generates a sequence of "condition image tokens" <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.
2.  **3D Gaussian Splat Tokens:** Learnable 3D Gaussian Splat tokens, analogous to position embeddings, are incorporated <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. These represent a fixed-length sequence of 16,384 tokens, each with 512 dimensions, corresponding to the final 3D Gaussians <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
3.  **Mamba Processing:** These tokens, along with camera condition parameters (extrinsic and intrinsic), are processed by the Mamba-based Gamba model <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>, <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>. The model outputs 3D Gaussian Splats, which can then be rendered to create new images from different views <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.
4.  **Loss Function:** The training uses an image-space reconstruction loss, comparing rendered images to ground truth <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. The Dino encoder remains frozen during training <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

### Performance and [[limitations_and_potential_of_mamba_models_in_ai | Limitations of Gamba]]
Gamba demonstrates impressive speed, taking approximately 1 second on a single Nvidia A100 GPU for 3D reconstruction <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>, <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. However, its current results are not state-of-the-art <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.

Key limitations include:
*   **Reliance on Vision Transformer:** The use of a pre-trained Dino Vision Transformer for image encoding, rather than a Mamba-based encoder, limits the full potential of a pure Mamba architecture <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.
*   **Smaller Dataset:** Gamba was pre-trained on the Omni object 3D dataset, which is significantly smaller than widely adopted datasets like Obverse, potentially impacting its overall performance <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>, <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Unidirectional Scan Order:** The paper states Gamba uses a unidirectional scan order, which might be suboptimal as other Mamba papers have shown benefits from multiple scan directions (e.g., vertical, horizontal) <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   **Camera Pose and Object Mask Dependency:** Gamba incorporates camera pose tokens and uses an object mask for initialization, which might not be available in real-world scenarios, limiting its practical applicability <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

## Mambas for Vision Language Models: Cobra

Cobra extends Mamba models to the realm of [[vision_language_models_and_their_applications | multimodal large language models]] (MLLMs), focusing on efficient inference <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Cobra aims to be a computationally efficient VLM with linear complexity <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

### Cobra Architecture and Training
Cobra's architecture processes both image and text inputs:
1.  **Image Encoding:** Similar to Gamba, Cobra employs external, pre-trained Vision Transformers for image encoding. Specifically, it uses an ensemble of Dino image encoder and SigLip encoder to provide a richer visual representation <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>, <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
2.  **Projection Layer:** An MLP (Multi-Layer Perceptron) projector connects the visual embeddings from the image encoders to the Mamba-based language model <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
3.  **Mamba Backbone:** The core of Cobra is a language model composed of 64 sequential Mamba blocks <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. This Mamba backbone is responsible for processing both visual and textual tokens and generating auto-regressive text responses <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

Cobra's training paradigm simplifies previous multi-stage approaches (like those seen in Lava models) by directly fine-tuning the entire Mamba language model backbone and the projector simultaneously <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This approach was previously suggested in other VLM research, including Apple's VLM paper <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. The model was trained on a dataset of approximately 1.2 million images, partly distilled from GPT-4 Vision responses <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

### Performance and [[limitations_and_potential_of_mamba_models_in_ai | Implications of Cobra]]
Cobra shows "extremely competitive performance" when compared to computationally efficient models like Lava <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>, <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. More importantly, it achieves comparable performance to Lava with only 43% of the parameters <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

The most significant advantage lies in its inference speed: Cobra processes 166 tokens per second, which is significantly faster than Transformer-based VLMs like Mobile VM (39 tokens/second) or Lava (40 tokens/second) <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This speed is attributed to Mamba's linear complexity, allowing for efficient processing regardless of input sequence length <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

Despite its performance, Cobra shares a key [[vision_language_models_with_pretrained_components | architectural limitation]] with Gamba: it still relies on Vision Transformers for image encoding <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>, <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. This means the quadratic complexity of Transformers is still present in the initial image processing step, potentially limiting overall efficiency gains, especially with large images <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

### [[Integration of Vision Language Models in Robotics | Future Directions and Applications]]
The efficiency of Mamba-based VLMs like Cobra opens new possibilities for deployment in environments requiring high-frequency processing of visual information, such as [[Integration of Vision Language Models in Robotics | visual-based robotic feedback control]] and autonomous vehicles <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. The significantly faster inference time (e.g., reducing 3-second processing to milliseconds) is crucial for real-time applications where rapid decision-making based on visual input is essential <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.

## Core Principles of Mamba Models

Mambas are grounded in State Space Models (SSMs), which are linear time-invariant systems designed to capture system dynamics via state variables <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. The "selective" aspect, a key contribution of the original Mamba paper, makes the matrices (B, Delta T, and C) that govern the model's dynamics dependent on the input <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. This input-dependent dynamic allows the Mamba to selectively filter or emphasize information from the input sequence, analogous to how attention mechanisms operate in Transformers <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.

The efficiency gain of Mambas over Transformers stems from their fixed-size hidden state (H) during sequence processing <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. While Transformers compute attention over the entire input sequence, leading to quadratic growth in computation with sequence length, Mambas maintain a constant hidden state size, resulting in linear growth <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>, <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. Furthermore, Mambas are designed for efficient implementation on GPUs, enabling faster training and inference through techniques that allow them to be treated almost like convolutional networks during computation <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

## [[Limitations and potential of Mamba models in AI | Challenges and Considerations for Mamba Models]]

While Mamba models show great promise due to their speed and efficiency, a potential "Achilles' heel" has emerged regarding their numerical precision requirements and quantization capabilities <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>, <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

Observations from both the Cobra and Jamba papers suggest that Mamba blocks require relatively high precision (no lower than bf16) to maintain model quality during inference <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. In contrast, [[large_language_models_and_their_applications | Transformers]] have seen significant progress in extreme quantization (e.g., down to 1.58 bits per parameter) without substantial performance degradation <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>. If Mamba models prove inherently difficult to quantize to lower bit depths, their advantage in memory and speed might be negated by increasingly efficient quantized Transformer architectures <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. This creates an "arms race" where Mamba's architectural efficiency is pitted against Transformer's quantization-driven efficiency <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Future research will likely explore methods to overcome this limitation, potentially leading to "quantized Mamba models" or "CoMa" architectures <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

Despite these challenges, the rapid development and adoption of Mamba models, as seen in their diverse [[comparison_of_mamba_models_in_language_and_vision_contexts | applications in 3D reconstruction and vision language models]], suggest their growing importance in the landscape of efficient AI architectures.