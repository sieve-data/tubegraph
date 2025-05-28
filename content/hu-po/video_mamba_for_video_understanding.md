---
title: Video Mamba for video understanding
videoId: rzXjKcqkjxM
---

From: [[hu-po]] <br/> 

Video Mamba is a [[Limitations and potential of Mamba models in AI | State Space Model]] (SSM)-based architecture designed for efficient [[Computer vision deep dive | video understanding]] <a class="yt-timestamp" data-t="04:10:10">[04:10:10]</a>. It operates as an alternative to the Transformer architecture, similar to RNNs or LSTMs, but leverages advancements that enable parallel training <a class="yt-timestamp" data-t="03:46:27">[03:46:27]</a>. This model addresses challenges in processing long video sequences by offering a linear complexity operator, leading to faster speed and lower GPU consumption compared to attention-based models <a class="yt-timestamp" data-t="08:01:42">[08:01:42]</a>, <a class="yt-timestamp" data-t="08:03:03">[08:03:03]</a>, <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.

## Challenges in Video Understanding

[[Computer vision deep dive | Video understanding]] faces two primary challenges:
*   **Local Redundancies**: Many video frames contain significant redundant information, with only slight changes between consecutive frames <a class="yt-timestamp" data-t="07:00:03">[07:00:03]</a>.
*   **Global Dependencies**: Videos are long sequences of frames, requiring the model to capture specific relationships between frames that are far apart <a class="yt-timestamp" data-t="07:16:19">[07:16:19]</a>.

Traditional architectures like 3D Convolutional Neural Networks and [[Stateoftheart video generation and multimodal models | video Transformers]] have limitations in efficiently modeling these aspects <a class="yt-timestamp" data-t="07:38:25">[07:38:25]</a>. Transformers, despite their power, suffer from substantial computational requirements due to the quadratic scaling of their attention mechanism with sequence length <a class="yt-timestamp" data-t="14:40:41">[14:40:41]</a>, <a class="yt-timestamp" data-t="15:08:03">[15:08:03]</a>.

## Video Mamba Architecture and Design

Video Mamba innovatively adapts the Mamba architecture to the video domain <a class="yt-timestamp" data-t="07:33:40">[07:33:40]</a>.

### Input Processing
The model first uses a 3D convolution to convert the input video into non-overlapping spatial-temporal patches, effectively turning the video into a sequence of tokens <a class="yt-timestamp" data-t="04:18:50">[04:18:50]</a>, <a class="yt-timestamp" data-t="04:54:02">[04:54:02]</a>. These tokens are then fed into the Video Mamba encoder <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>. It uses learnable spatial and temporal position embeddings, which are preferred for complex modalities like video over fixed embeddings such as RoPE <a class="yt-timestamp" data-t="04:10:48">[04:10:48]</a>, <a class="yt-timestamp" data-t="04:12:11">[04:12:11]</a>.

### State Space Model (SSM) Core
SSMs model a 1D function or sequence by passing information through a hidden state ($H$) <a class="yt-timestamp" data-t="04:29:34">[04:29:34]</a>. The continuous ordinary differential equation (ODE) defining SSMs is discretized using a zero-order hold method, converting it into a discrete system suitable for sequential data processing <a class="yt-timestamp" data-t="04:48:47">[04:48:47]</a>. This discretization leads to a linear scaling of memory and compute complexity with the input sequence length, a key advantage over Transformers <a class="yt-timestamp" data-t="04:52:19">[04:52:19]</a>, <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>.

### Scanning Strategies
Video Mamba employs specific scanning methods to process video data:
*   **Spatial-First Bidirectional Scan**: The model scans through the entire frame spatially before moving to the next frame in the time dimension. This approach was found to be the most effective <a class="yt-timestamp" data-t="05:07:05">[05:07:05]</a>, <a class="yt-timestamp" data-t="05:14:04">[05:14:04]</a>, <a class="yt-timestamp" data-t="05:15:10">[05:15:10]</a>. Bidirectional scanning means the model processes the sequence in both forward (start to end) and reverse (end to start) directions <a class="yt-timestamp" data-t="05:22:15">[05:22:15]</a>.
*   The effectiveness of spatial-first scanning is intuitively linked to summarizing each frame before progressing to the next, as opposed to summarizing small patches across time <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>. However, the optimal scanning strategy might depend on the specific dataset and video characteristics <a class="yt-timestamp" data-t="01:01:57">[01:01:57]</a>.

## Training Methodologies

Video Mamba's training process incorporates several techniques:
*   **Masked Training**: The model is trained by masking out parts of the input video data, forcing it to focus on global information and preventing over-reliance on specific patches <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a>. Different masking strategies include:
    *   **Input video random masking**: Randomly masks patches in the input video <a class="yt-timestamp" data-t="01:07:52">[01:07:52]</a>.
    *   **Tube masking**: Masks continuous "tube-like" regions across multiple frames, meaning the same spatial region is masked over the entire sequence <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>, <a class="yt-timestamp" data-t="01:09:19">[01:09:19]</a>.
    *   **Clip row masking**: Masks entire rows of pixels across all frames of the video, akin to a consistent horizontal strip along the sequence <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.
    *   **Frame row masking**: Similar to clip row masking, but each frame has its rows masked individually, allowing variations in masked rows per frame <a class="yt-timestamp" data-t="01:09:40">[01:09:40]</a>.
    *   **Attention masking**: A strategy that prioritizes preserving adjacent meaningful content, aiming to keep enough neighboring patches unmasked <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>. An optimal masking ratio of 80% was identified <a class="yt-timestamp" data-t="01:43:11">[01:43:11]</a>.

*   **Self-Distillation**: An unusual technique where a smaller, well-trained model acts as a teacher to guide the training of a larger student model <a class="yt-timestamp" data-t="01:13:09">[01:13:09]</a>. This counter-intuitive approach helps prevent the larger model from overfitting on small datasets when trained from scratch <a class="yt-timestamp" data-t="01:35:47">[01:35:47]</a>. The self-distillation is combined with masked training and a standard classification loss to achieve better convergence <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>. Video Mamba aligns only the final outputs between the student and teacher models, unlike some methods that use multi-layer alignment <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a>.

*   **Multi-step Training Process**: The model is initially trained from scratch on video data, aligning unmasked tokens with those from a Clip Vision Transformer (ViT) to distill knowledge <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>. Subsequently, a Bert text encoder is integrated for image-text and video-text data processing <a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a>.

## Performance and Evaluation

Video Mamba was evaluated on standard [[Computer vision deep dive | video understanding]] benchmarks:
*   **ImageNet 1K**: For image classification <a class="yt-timestamp" data-t="01:33:10">[01:33:10]</a>. Video Mamba demonstrates better performance with fewer floating-point operations (flops) compared to Transformer-based and ConvNet-based models of similar parameter counts <a class="yt-timestamp" data-t="01:38:25">[01:38:25]</a>.
*   **Kinetics 400**: For action classification in 10-second videos, classifying them into 400 human action categories <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>, <a class="yt-timestamp" data-t="01:39:17">[01:39:17]</a>. While it sets a new benchmark for Mamba models in [[Computer vision deep dive | video understanding]] <a class="yt-timestamp" data-t="01:42:18">[01:42:18]</a>, <a class="yt-timestamp" data-t="01:42:32">[01:42:32]</a>, it generally falls short of the current [[Stateoftheart video generation and multimodal models | state-of-the-art Transformers]] on these benchmarks, which often involve smaller videos and resolutions <a class="yt-timestamp" data-t="01:44:46">[01:44:46]</a>.

The true strength of Mamba models like Video Mamba lies in their efficiency and scalability for longer sequences and higher resolutions, where Transformer models face significant computational hurdles due to their quadratic complexity <a class="yt-timestamp" data-t="01:29:54">[01:29:54]</a>, <a class="yt-timestamp" data-t="01:44:54">[01:44:54]</a>. As video dimensionality increases with 4K video at high frame rates, Mamba models are expected to become increasingly vital <a class="yt-timestamp" data-t="01:32:41">[01:32:41]</a>.

Video Mamba aims to pave the path for future model design for long video comprehension and potential integration with large models for hour-level [[Computer vision deep dive | video understanding]] <a class="yt-timestamp" data-t="01:44:33">[01:44:33]</a>. Its code and models are open-source <a class="yt-timestamp" data-t="08:44:59">[08:44:59]</a>.

> [!NOTE]
> The video also discusses [[Motion Mamba for efficient motion generation | Motion Mamba]], another Mamba-based model, which focuses on text-to-motion generation <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>. A [[Comparison of Mamba models in language and vision contexts | comparison of Mamba models in language and vision contexts]] reveals that while both leverage the linear complexity of SSMs, they apply distinct scanning strategies and architectural nuances tailored to their respective modalities.