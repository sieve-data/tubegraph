---
title: Interactive pointbased manipulation
videoId: ExfMg4v5DMA
---

From: [[hu-po]] <br/> 

DragGAN is a novel approach to interactive point-based manipulation on generative image manifolds, allowing users precise control over generated images by simply clicking and dragging points <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This method, developed by researchers from Max Planck Institute, MIT CSAIL, and Google AR/VR, enables intuitive manipulation of attributes like pose, shape, expression, and layout across various object categories <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## How DragGAN Works

DragGAN operates by allowing a user to define a "handle point" (start) and a "target point" (end) on an image <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The approach then iteratively moves the handle point towards the target point, ensuring the image remains semantically consistent <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a> <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. The manipulation is performed on the learned generative image manifold of the [[GANbased image manipulation | GAN]], rather than directly in image space <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a> <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

The core of DragGAN consists of two main components <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>:
1.  **Feature-based Motion Supervisor**: This component drives the handle point to move towards its target position <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  **Point Tracking Approach**: This leverages discriminative generator features to continuously localize the position of the handle points <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

### Iterative Process

The process is iterative, involving repeated steps of motion supervision and point tracking until the handle points reach their corresponding targets <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a> <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>. This typically takes 20 to 200 iterations <a class="yt-timestamp" data-t="01:17:41">[01:17:41]</a>.

#### Motion Supervision
The motion supervision step uses a loss function that encourages a small patch around the handle point to move towards the target point <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a> <a class="yt-timestamp" data-t="00:56:21">[00:56:21]</a>. This loss does not rely on additional neural networks <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>. The key insight is that the intermediate features of the GAN generator are highly discriminative, allowing a simple loss to suffice for motion supervision <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>.

#### Point Tracking
After motion supervision updates the latent code and generates a new image, the point tracking step updates the handle points to reflect the object's new position <a class="yt-timestamp" data-t="01:09:44">[01:09:44]</a> <a class="yt-timestamp" data-t="01:10:37">[01:10:37]</a>. Unlike traditional [[motion tracking methods | optical flow estimation]] or particle video approaches, DragGAN performs point tracking via a nearest-neighbor search in the GAN's feature space <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a> <a class="yt-timestamp" data-t="01:12:29">[01:12:29]</a>. This avoids the need for additional networks, improving efficiency <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>.

### Technical Foundations
DragGAN is based on the StyleGAN2 architecture <a class="yt-timestamp" data-t="01:16:15">[01:16:15]</a>.
*   **Latent Codes**: StyleGAN2 uses a 512-dimensional latent code (Z) which is mapped to an intermediate latent code (W) <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a> <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>. W is then fed to the generator (G) to produce the image <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. The W is often copied and sent to different layers of the generator to control different levels of attributes <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.
*   **W+ Space**: Using different W values for different layers creates a "W+ space," which is less constrained and more expressive, allowing for "out-of-distribution" manipulations (e.g., a cat blinking, which might not be in the training data) <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a> <a class="yt-timestamp" data-t="00:42:44">[00:42:44]</a> <a class="yt-timestamp" data-t="01:55:28">[01:55:28]</a>. DragGAN uses W+ space for better editability <a class="yt-timestamp" data-t="01:05:53">[01:05:53]</a>.
*   **Feature Maps**: The method primarily uses feature maps from the sixth block of StyleGAN2, as it offers a good balance between resolution and discriminativeness <a class="yt-timestamp" data-t="00:53:44">[00:53:44]</a> <a class="yt-timestamp" data-t="01:40:31">[01:40:31]</a>. These feature maps are resized using bilinear interpolation <a class="yt-timestamp" data-t="00:55:24">[00:55:24]</a>.
*   **Masking**: Users can optionally draw a binary mask to define a movable region, aiming to keep unmasked regions fixed <a class="yt-timestamp" data-t="00:45:58">[00:45:58]</a>. However, because masking is applied in feature space rather than image space, unmasked regions may still experience slight changes <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a> <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>.
*   **Computational Efficiency**: DragGAN is designed for interactive use, taking only a few seconds on a single RTX 3090 GPU <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a> <a class="yt-timestamp" data-t="01:22:01">[01:22:01]</a>.

## Comparisons to Previous Work

### Existing GAN Controllability
Previous approaches to controlling GANs typically rely on manually annotated training data, prior 3D models <a class="yt-timestamp" data-t="00:42:29">[00:42:29]</a>, or latent space manipulation <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>. Older methods using latent space math (e.g., "smiling woman - neutral woman + neutral man = smiling man") often produced primitive results and failed to generalize to new object categories <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a> <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. These methods also offer coarse control, lacking the precision for specific pixel movements <a class="yt-timestamp" data-t="01:06:16">[01:06:16]</a> <a class="yt-timestamp" data-t="01:06:21">[01:06:21]</a>.

### User Controllable LT
DragGAN's closest predecessor is "User Controllable LT" (2022 paper) <a class="yt-timestamp" data-t="01:42:33">[01:42:33]</a> <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>. While similar in concept, DragGAN significantly outperforms it, achieving more natural and superior results <a class="yt-timestamp" data-t="01:07:40">[01:07:40]</a> <a class="yt-timestamp" data-t="01:29:48">[01:29:48]</a>. User Controllable LT often leads to "undesired changes" or "semantic concept changes" <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="01:30:12">[01:30:12]</a>. For example, moving a sun in User Controllable LT might change the background from an ocean to a forest, whereas DragGAN preserves the original scene <a class="yt-timestamp" data-t="01:09:08">[01:09:08]</a> <a class="yt-timestamp" data-t="01:30:26">[01:30:26]</a>.

### Diffusion Models
While [[GANbased image manipulation | GANs]] are seeing a comeback, diffusion models are currently popular for controllable image synthesis <a class="yt-timestamp" data-t="02:21:57">[02:21:57]</a>. However, diffusion models are often slower due to their iterative denoising steps (requiring multiple steps) compared to GANs, which generate an image in one shot <a class="yt-timestamp" data-t="00:31:26">[00:31:26]</a> <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>. Additionally, natural language control in diffusion models currently lacks the fine-grained precision offered by point-based manipulation <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>.

## Capabilities and Limitations

### Strengths
*   **Precise Control**: Allows users to specify exact pixel movements <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>.
*   **Semantic Consistency**: Generates realistic outputs even in challenging scenarios, such as hallucinating occluded content (e.g., teeth inside a lion's mouth) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a> <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **Diverse Manipulation**: Capable of manipulating pose, shape, expression, and layout across various object categories like animals, cars, and landscapes <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> <a class="yt-timestamp" data-t="00:21:16">[00:21:16]</a>.
*   **Real Image Editing**: Can manipulate real images by first using [[GANbased image manipulation | GAN inversion]] to map them into the latent space <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a> <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

### Limitations and Considerations
*   **Training Data Dependence**: Editing quality is still affected by the diversity of the training data. For example, creating a human pose far from the training distribution can lead to artifacts <a class="yt-timestamp" data-t="01:50:55">[01:50:55]</a>.
*   **Textureless Regions**: Handling points in textureless regions may suffer from more drift in tracking <a class="yt-timestamp" data-t="01:51:05">[01:51:05]</a>.
*   **Ethical Concerns**: The ability to create realistic images with fake poses could be misused to generate deepfakes <a class="yt-timestamp" data-t="01:51:16">[01:51:16]</a>.

## Future Directions
The authors plan to extend this point-based image editing to [[Differentiable rendering and optimization | 3D generative models]] <a class="yt-timestamp" data-t="01:53:01">[01:53:01]</a>. Other potential extensions include applying the technique to diffusion models, despite the current slowness, and exploring its use for video generation <a class="yt-timestamp" data-t="01:34:51">[01:34:51]</a> <a class="yt-timestamp" data-t="01:49:01">[01:49:01]</a>. The core idea of leveraging discriminative intermediate feature maps of GANs could also be applied to other domains, such as manipulating spectrograms for audio generation <a class="yt-timestamp" data-t="01:56:55">[01:56:55]</a>.