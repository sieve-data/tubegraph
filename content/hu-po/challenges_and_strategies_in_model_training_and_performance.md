---
title: Challenges and strategies in model training and performance
videoId: eTBG17LANcI
---

From: [[hu-po]] <br/> 

This article discusses the "Scalable Diffusion Models with Transformers" paper, published on December 19th, from UC Berkeley, New York University, and Meta AI's FAIR team. The paper introduces Diffusion Transformers (DiTs), which use a Transformer backbone to achieve state-of-the-art image quality in diffusion models <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Core Architectural Innovation: Diffusion Transformers (DiTs)

Traditionally, diffusion models have adopted the U-Net architecture as their de facto choice for their backbone <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This paper demonstrates that the U-Net bias is not crucial for performance and can be replaced with standard Transformer designs <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

DiTs are based on the Vision Transformer (ViT) architecture, which processes an image by cutting it into small patches and feeding these patches as a sequence of tokens to the Transformer <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. The diffusion process in DiTs occurs in the latent space, meaning the Transformers operate on latent patches derived from the image <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Scalability and Performance Metrics

The paper analyzes the scalability of Diffusion Transformers through the lens of forward pass complexity, measured in Gigaflops (GFLOPS) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. It finds a consistent correlation: DiTs with higher GFLOPS, achieved through increased Transformer depth, width, or a greater number of input tokens, consistently yield lower FID (Fréchet Inception Distance) scores <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. FID is a quantitative metric used to subjectively measure image quality, where lower scores indicate better quality <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. This reinforces the general principle in machine learning that "the bigger you make these models, the deeper you make these models, the wider you make the model, the more data you train it on, the better you're gonna get" <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

The largest model, DiT-XL/2, achieved a state-of-the-art FID score of 2.27 on the 256x256 ImageNet generation benchmark, utilizing 118.6 GFLOPS <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This demonstrates that while scale is sufficient for state-of-the-art results, it's not always required if a better architecture is found <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>. However, scaling existing architectures is often a more appealing and straightforward solution <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

The paper argues that parameter counts can be poor proxies for the complexity of image models as they don't account for image resolution. Instead, measuring complexity through GFLOPS or memory footprint provides a more realistic understanding of the model's compute requirements <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

## [[Challenges and methodologies in AI training | Training Methodologies and Challenges]]

### Latent Diffusion Models
To address the computational intensity of training diffusion models directly in high-resolution pixel space, DiTs utilize latent diffusion models <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. This means the diffusion process is performed on a lower-dimensional latent representation of the image, making the operations faster <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### Classifier-Free Guidance
A key improvement in diffusion models is Classifier-Free Guidance (CFG). This technique involves randomly dropping out class labels during training, which allows the model to learn both conditional and unconditional generation <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. When applied at inference, it allows for a weighted combination of these outputs, enhancing the quality and adherence to the specified conditions <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>.

### Normalization Techniques
To ensure stable and efficient training, especially for deeper and wider Transformer architectures, normalization layers are crucial <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>. DiTs use adaptive normalization layers, specifically AdaLN (Adaptive Layer Normalization), where scale and shift parameters are dynamically generated and applied to the layer activations <a class="yt-timestamp" data-t="00:34:09">[00:34:09]</a>. This helps in maintaining well-distributed and well-shaped numbers within the neural network, allowing gradients to flow more effectively and facilitating better learning <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. They also apply normalization immediately prior to any residual connections <a class="yt-timestamp" data-t="00:37:07">[00:37:07]</a>.

### Hyperparameter Tuning and Optimization
The authors noted that many training hyperparameters were retained from ADM (another diffusion model), and they did not extensively tune learning rates, decay schedules, or warm-up schedules <a class="yt-timestamp" data-t="00:48:20">[00:48:20]</a>. They used a constant learning rate of 1e-4 and no weight decay <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a>, although they did maintain an exponential moving average of DiT weights <a class="yt-timestamp" data-t="00:47:26">[00:47:26]</a>. This suggests that there is still significant room for further optimization and performance improvement through more dedicated hyperparameter tuning <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>.

### Training Environment and Costs
The models were implemented in JAX and trained on Google TPU V3 pods <a class="yt-timestamp" data-t="00:51:19">[00:51:19]</a>. The largest model (DiT-XL/2) trained at 5.7 iterations per second on a TPU V3 256-pod <a class="yt-timestamp" data-t="00:52:46">[00:52:46]</a>. Training for 400,000 steps took approximately 19 hours, costing over $10,000 per model <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>. The total training cost for the 12 different DiT models presented in the paper was estimated to be over $100,000 <a class="yt-timestamp" data-t="00:55:29">[00:55:29]</a>. This highlights the substantial computational budget required for [[Challenges and methodologies in AI training | large-scale AI model training]]. For production use cases, techniques like pruning and quantization would be necessary to reduce inference costs and enable deployment on smaller, cheaper hardware <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.

### Sampling Steps
The number of sampling steps (or noising steps) in diffusion models impacts image quality <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>. While more steps generally lead to slightly better results by adding and removing finer noise, there's a decaying trade-off where additional steps yield diminishing returns <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>. The authors found a "sweet spot" around 256 sampling steps for optimal performance <a class="yt-timestamp" data-t="01:04:09">[01:04:09]</a>.

## Achieved Performance and Future Outlook

The DiT-XL/2 model generated "extremely crisp" images with correct semantic information and no artifacts at various scales, including subtle details like the wrist of a dog <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The quality is a significant leap from generative models of just a few years ago, demonstrating an accelerating pace of improvement in the field <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a>.

The paper suggests that future work should continue to scale DiTs to even larger models and token counts <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>. The rapid advancements in generative AI, particularly in image generation, indicate a future where users might be able to generate 4K video from text prompts by the end of 2023 <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. This capability would fundamentally change content creation and various industries <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>.