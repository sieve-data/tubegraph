---
title: Multimodal learning and embeddings
videoId: MR_TpKe5atI
---

From: [[hu-po]] <br/> 

[[overview_of_multimodal_models | Multimodal models]] process and understand information from various data types, known as modalities <a class="yt-timestamp" data-t="01:57:46"></a>. This field is significantly advanced by the concept of "embedding spaces," which are shared representations where different modalities can be projected and understood in relation to each other <a class="yt-timestamp" data-t="02:47:33"></a>.

## Key Concepts

### Modalities
Modalities refer to different types of data <a class="yt-timestamp" data-t="02:02:06"></a>. Examples discussed include:
*   **Audio data** <a class="yt-timestamp" data-t="02:06:08"></a>
*   **Heat map data** (thermal camera) <a class="yt-timestamp" data-t="02:08:12"></a>
*   **Text** <a class="yt-timestamp" data-t="02:12:14"></a>
*   **IMU** (Inertial Measurement Unit) data, which includes accelerometers and gyroscopes <a class="yt-timestamp" data-t="02:14:16"></a>
*   **Depth data** <a class="yt-timestamp" data-t="04:00:02"></a>
*   **Images** <a class="yt-timestamp" data-t="03:52:14"></a>
*   **Video** <a class="yt-timestamp" data-t="09:09:11"></a>

### Embedding Spaces
An embedding space is a high-dimensional space where data points are represented as vectors, capturing their semantic meaning and relationships <a class="yt-timestamp" data-t="02:28:29"></a>. In multimodal learning, the goal is often to create a single, shared embedding space where different modalities can be projected, allowing for cross-modal understanding and retrieval <a class="yt-timestamp" data-t="02:47:33"></a>.

A good embedding space ensures that semantically similar items, regardless of their original modality, are closer together, while dissimilar items are further apart <a class="yt-timestamp" data-t="02:56:59"></a>. This property enables tasks like semantic composition, where embeddings from different modalities can be added together to create new concepts <a class="yt-timestamp" data-t="11:34:02"></a>.

### Contrastive Learning
Contrastive learning is a general technique for learning an embedding space by using pairs of related (positive) and unrelated (negative) examples <a class="yt-timestamp" data-t="03:06:58"></a>. The loss function pulls positive pairs closer together in the embedding space and pushes negative pairs further apart <a class="yt-timestamp" data-t="03:10:04"></a>. This method was popularized by models like CLIP <a class="yt-timestamp" data-t="03:12:14"></a>.

### Zero-Shot Classification/Recognition
Zero-shot classification refers to a model's ability to perform a task without having seen any specific training examples for that task or class <a class="yt-timestamp" data-t="03:07:07"></a>. This indicates that the model has generalized well beyond its training data distribution <a class="yt-timestamp" data-t="03:22:25"></a>.

## ImageBind: A Multimodal Embedding Model

ImageBind is a model developed by Facebook AI Research, designed to learn a joint embedding across six different modalities: images, text, audio, depth, thermal, and IMU data <a class="yt-timestamp" data-t="06:50:04"></a>. The core idea behind ImageBind is that only image-paired data is sufficient to bind all modalities together in a single embedding space <a class="yt-timestamp" data-t="07:12:11"></a>.

### Approach and Architecture
ImageBind uses separate Transformer architectures for each modality's encoder <a class="yt-timestamp" data-t="02:23:04"></a>.
*   **Images/Video:** Utilizes Vision Transformers (ViT) <a class="yt-timestamp" data-t="04:35:07"></a>. For video, the patch projection layer of the ViT is "inflated" to accommodate multiple frames <a class="yt-timestamp" data-t="04:40:43"></a>.
*   **Audio:** Converted into 2D spectrograms, which are then encoded by a ViT <a class="yt-timestamp" data-t="04:54:57"></a>.
*   **Thermal and Depth:** Treated as one-channel images and encoded using a ViT <a class="yt-timestamp" data-t="04:47:44"></a>. Depth is converted to disparity maps for scale invariance <a class="yt-timestamp" data-t="04:59:01"></a>.
*   **IMU:** Encoded using a 1D convolution over the accelerometer and gyroscope measurements <a class="yt-timestamp" data-t="04:50:41"></a>.
*   **Text:** Uses the text encoder design from CLIP <a class="yt-timestamp" data-t="05:07:09"></a>.

A crucial aspect of ImageBind's training is that the pre-trained CLIP image and text encoders are *frozen* <a class="yt-timestamp" data-t="05:43:45"></a>. The audio, depth, thermal, and IMU encoders are trained to project their respective data into this *existing*, frozen CLIP embedding space <a class="yt-timestamp" data-t="05:52:45"></a>. This means ImageBind leverages the strong semantic alignment already present in CLIP's image-text embedding space <a class="yt-timestamp" data-t="05:57:01"></a>.

### Training Data and Loss
ImageBind uses an InfoNCE loss function for contrastive learning <a class="yt-timestamp" data-t="03:46:58"></a>. This loss pulls the image and corresponding modality's embedding closer together, while pushing them away from other unrelated examples in the mini-batch <a class="yt-timestamp" data-t="03:48:58"></a>.

Data sets used include:
*   AudioSet (for audio-image pairs) <a class="yt-timestamp" data-t="05:06:01"></a>
*   SUN RGB-D (for image-depth pairs) <a class="yt-timestamp" data-t="05:09:06"></a>
*   LLVIP (for image-thermal pairs) <a class="yt-timestamp" data-t="05:13:06"></a>
*   Ego4D (for video-IMU pairs) <a class="yt-timestamp" data-t="05:15:06"></a>
*   Large-scale web data (for image-text, implicitly via OpenCLIP encoders) <a class="yt-timestamp" data-t="05:52:55"></a>

### Emergent Capabilities
ImageBind enables "emergent" capabilities, meaning functionalities that were not explicitly trained for but arise from the model's design <a class="yt-timestamp" data-t="07:07:59"></a>. This phenomenon occurs because aligning each modality to image embeddings implicitly aligns them with each other <a class="yt-timestamp" data-t="03:52:27"></a>.

Examples of emergent capabilities include:

*   **Cross-Modal Retrieval:** Any modality can be used to retrieve examples from any other modality. For instance, audio can retrieve images, or depth data can retrieve text descriptions <a class="yt-timestamp" data-t="09:43:06"></a>.
*   **Embedding Arithmetic:** By adding embedding vectors from different modalities, ImageBind can compose their semantics. For example, adding an image embedding of a crane to an audio embedding of waves can generate an image of a crane in waves <a class="yt-timestamp" data-t="11:06:06"></a>. This highlights a strong notion of semantic concepts within the embedding space <a class="yt-timestamp" data-t="11:34:02"></a>.
*   **Cross-Modal Detection and Generation:**
    *   **Object Detection with Audio Queries:** Existing text-based object detectors (like Detic) can be prompted with audio embeddings instead of text, leading to robust detection capabilities <a class="yt-timestamp" data-t="14:42:06"></a>.
    *   **Audio to Image Generation:** Using audio embeddings with a pre-trained diffusion model (like DALL-E 2, or Facebook's private re-implementation) can generate images based on sound inputs <a class="yt-timestamp" data-t="10:29:06"></a>.

### Performance Claims and Nuances
ImageBind claims [[recent_advancements_in_multimodal_model_architectures | state-of-the-art performance]] on emergent zero-shot recognition tasks across modalities, outperforming specialist supervised models <a class="yt-timestamp" data-t="08:18:00"></a>. For example, it claims to achieve state-of-the-art text-to-audio classification without ever observing paired audio and text data during training <a class="yt-timestamp" data-t="04:06:45"></a>.

However, the transcript notes some potential overstatements and inconsistencies in the paper's claims when reviewing the benchmark tables <a class="yt-timestamp" data-t="04:53:04"></a>:
*   While it achieves strong emergent zero-shot performance, it doesn't always beat the absolute state-of-the-art on established benchmarks like ImageNet-1K, which are typically achieved by specialist supervised models <a class="yt-timestamp" data-t="04:50:04"></a>.
*   Some comparisons to prior work are deemed not fully comparable due to differences in modalities or training data <a class="yt-timestamp" data-t="01:09:16"></a>.
*   The term "emergent" is used to describe classification capabilities that are a natural outcome of strong general embeddings, rather than completely unexpected phenomena <a class="yt-timestamp" data-t="01:37:08"></a>.

## Comparison to CLIP
Prior to ImageBind, CLIP was widely considered the most powerful and popular [[multimodal_language_models | multimodal language model]], creating a shared embedding space for images and language <a class="yt-timestamp" data-t="06:56:06"></a>. [[multimodal_capabilities_in_large_language_models_using_clip | CLIP]]'s ability to project both images and text into the same embedding space made it incredibly powerful for tasks like guidance in diffusion models and text-to-image retrieval <a class="yt-timestamp" data-t="03:22:04"></a>.

ImageBind effectively extends CLIP's capabilities rather than replacing them <a class="yt-timestamp" data-t="02:21:27"></a>. By freezing CLIP's image and text encoders and training other modality encoders to project into that existing space, ImageBind allows any existing work that uses CLIP embeddings to be "upgraded" to accept inputs from audio, depth, IMU, or thermal data <a class="yt-timestamp" data-t="01:21:00"></a>. This creates a "Cambrian explosion" of new research possibilities by integrating more modalities into an already powerful, semantically meaningful embedding space <a class="yt-timestamp" data-t="01:41:01"></a>.

## Implementation Details
*   **Model Size:** The "huge" version of ImageBind is approximately 4 gigabytes <a class="yt-timestamp" data-t="06:00:01"></a>.
*   **Hyperparameters:** Key hyperparameters studied include the contrastive loss temperature, which influences the smoothness of the softmax distribution <a class="yt-timestamp" data-t="03:51:09"></a>. Different temperatures are optimal for different modalities <a class="yt-timestamp" data-t="01:25:03"></a>.
*   **Projection Heads:** Linear projection heads generally performed better than Multi-Layer Perceptrons (MLPs) for computing depth and audio embeddings <a class="yt-timestamp" data-t="01:30:08"></a>.
*   **Training Epochs:** Longer training consistently improves zero-shot performance <a class="yt-timestamp" data-t="01:40:41"></a>.
*   **Augmentations:** Basic augmentation techniques (e.g., horizontal flip, random erase, color jitter) were used, with frequency masking being specific to audio <a class="yt-timestamp" data-t="01:47:57"></a>. Spatial alignment of crops during training is crucial for depth data, as misaligned crops severely degrade performance <a class="yt-timestamp" data-t="01:27:00"></a>.
*   **Encoder Capacity:** Stronger (larger) image encoders generally improve performance across all modalities. However, for modalities like depth, a smaller encoder can sometimes be better due to smaller data set sizes, preventing overfitting <a class="yt-timestamp" data-t="01:32:48"></a>.

## Societal Impact and Future
ImageBind's release, with its publicly available weights and repository, is considered a significant contribution to the machine learning community <a class="yt-timestamp" data-t="01:41:49"></a>. It simplifies the process of integrating new modalities into existing vision models and lays groundwork for future developments in [[multimodal_large_language_models | multimodal large language models]] and potentially Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="08:05:05"></a>. The ability to compose semantic concepts across diverse data types suggests broad applicability for novel applications <a class="yt-timestamp" data-t="01:15:57"></a>.