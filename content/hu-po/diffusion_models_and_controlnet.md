---
title: Diffusion Models and ControlNet
videoId: Mp-HMQcB_M4
---

From: [[hu-po]] <br/> 

[[introduction_to_controlnet | ControlNet]] is a [[neural_network_diffusion_concept | neural network diffusion concept]] structure designed to add conditional control to pre-trained large [[neural_network_diffusion_concept | diffusion models]], particularly [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>, <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Released in February 2023, it quickly gained significant attention for its ability to provide fine-grained control over image generation <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>, <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. The project originates from research by Lvmin Zhang and Maneesh Agrawala of Stanford <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.

## Core Mechanism

Historically, [[neural_network_diffusion_concept | diffusion models]] have been powerful for text-to-image generation, but it was difficult to precisely control the output to create an exact desired image <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>, <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>. [[introduction_to_controlnet | ControlNet]] addresses this by allowing users to specify additional conditions like edges or poses, enabling much more precise control over the final image output <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>, <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

The key to [[introduction_to_controlnet | ControlNet]]'s functionality lies in its unique architecture:
*   **Cloned Weights** [[introduction_to_controlnet | ControlNet]] clones the weights of a large [[neural_network_diffusion_concept | diffusion model]] (like [[latent_diffusion_model_for_neural_networks | Stable Diffusion]]) into two copies: a "trainable copy" and a "locked copy" <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>, <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.
    *   The **locked copy** preserves the network's existing capabilities learned from billions of images, preventing it from overfitting on smaller, task-specific datasets <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>, <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.
    *   The **trainable copy** is specifically trained on task-specific data to learn the conditional control <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.
*   **Zero Convolution** The trainable and locked [[neural_network_diffusion_concept | neural network]] blocks are connected via "zero convolution" layers <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>. These are 1x1 convolutional layers where both weights and biases are initialized to zero <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>, <a class="yt-timestamp" data-t="25:39:00">[25:39:00]</a>.
    *   This initialization means that in the very first training step, the [[introduction_to_controlnet | ControlNet]] causes no influence on the deep network features, ensuring that the original model's quality and functionality are perfectly preserved <a class="yt-timestamp" data-t="50:56:00">[50:56:00]</a>.
    *   As training progresses, the zero convolution weights gradually become optimized, allowing the [[introduction_to_controlnet | ControlNet]] to learn and exert influence <a class="yt-timestamp" data-t="17:53:00">[17:53:00]</a>. This approach makes training as fast as fine-tuning a [[neural_network_diffusion_concept | diffusion model]] <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.

[[introduction_to_controlnet | ControlNet]] is integrated into the encoder and middle blocks of the [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] U-Net architecture, with its outputs added to the skip connections of the main model <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. This design is computationally efficient, reducing GPU memory requirements by half compared to training layers from scratch <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>.

## Conditional Inputs

[[introduction_to_controlnet | ControlNet]] can take various image-based conditions as input to guide the [[neural_network_diffusion_concept | diffusion process]]. The condition is first encoded into a 64x64 feature map using a tiny convolutional network, `E`, to match the latent space dimensions used by [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>, <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>.

Examples of conditional inputs include:
*   **Canny Edge Maps:** An algorithm (developed by John F. Canny in 1986 <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>) that detects edges in an image by identifying significant changes in pixel values <a class="yt-timestamp" data-t="01:33:14">[01:33:14]</a>.
*   **Hough Lines:** An older algorithm (from 1962 and 1972 <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>) used to detect straight lines in an image <a class="yt-timestamp" data-t="01:29:56">[01:29:56]</a>.
*   **User Scribbles/Sketches:** Synthesized from boundary detections with data augmentations to mimic human drawings <a class="yt-timestamp" data-t="01:31:47">[01:31:47]</a>.
*   **Human Key Points/Pose:** Learned pose estimation methods identify key points (e.g., elbows, shoulders, hips) to form a human skeleton <a class="yt-timestamp" data-t="01:32:43">[01:32:43]</a>.
*   **Semantic Segmentation Maps:** Images where each pixel is classified by an object category (e.g., road, car, building) <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>.
*   **Normal Maps:** Represent the orientation of surfaces in an image <a class="yt-timestamp" data-t="01:39:06">[01:39:06]</a>.
*   **Depth Maps:** Indicate the distance of objects from the camera, with brighter pixels often meaning closer objects <a class="yt-timestamp" data-t="01:37:26">[01:37:26]</a>.

## Training and Performance

[[introduction_to_controlnet | ControlNet]] can be trained robustly even with small datasets (e.g., under 100k samples or even 1k) <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>, <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.
The training process often involves:
*   **Data Generation:** Large datasets (millions of image-caption pairs) are created by applying traditional computer vision algorithms (like Canny edge detection or pose estimators) to images to generate the conditional inputs <a class="yt-timestamp" data-t="01:27:51">[01:27:51]</a>, <a class="yt-timestamp" data-t="01:32:43">[01:32:43]</a>.
*   **Two-Stage Training (for large-scale training):**
    1.  Initially, the [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] model's weights are locked, and only the [[introduction_to_controlnet | ControlNet]] is trained <a class="yt-timestamp" data-t="01:26:33">[01:26:33]</a>.
    2.  After a certain number of steps (e.g., 50,000), the weights of the [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] model are unlocked, and both models are jointly trained <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>.
*   **"Sudden Convergence":** During training, a phenomenon occurs where the model suddenly learns to adapt to the input conditions, transitioning from generating random textures to precise, conditioned images <a class="yt-timestamp" data-t="01:56:57">[01:56:57]</a>.
*   **Computational Efficiency:** Training [[latent_diffusion_model_for_neural_networks | Stable Diffusion]] with [[introduction_to_controlnet | ControlNet]] requires only about 23% more GPU memory and 34% more time per session compared to the base model <a class="yt-timestamp" data-t="01:17:28">[01:17:28]</a>. This allows training on personal devices with GPUs (e.g., Nvidia RTX 3090) and achieving competitive results <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>, <a class="yt-timestamp" data-t="01:25:50">[01:25:50]</a>.

## [[comparisons_with_diffusion_models | Comparisons with Diffusion Models]] and Other Techniques

[[introduction_to_controlnet | ControlNet]] significantly enhances the control capabilities of [[neural_network_diffusion_concept | diffusion models]] beyond simple text-based prompts. While previous methods like inpainting or text-guided image editing existed <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>, they lacked the fine-grained control offered by [[introduction_to_controlnet | ControlNet]]'s explicit conditional inputs <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>. The paper highlights that its approach is different from image-to-image translation models like Pix2Pix, as [[introduction_to_controlnet | ControlNet]] specifically targets controlling a [[neural_network_diffusion_concept | diffusion model]] with task-specific conditions rather than learning a direct mapping between image domains <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. The use of zero convolution also sets it apart from earlier techniques like HyperNetworks, which influence neural network weights, by providing a unique initialization that maintains the original model's performance from the start <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

## Impact and Future

[[introduction_to_controlnet | ControlNet]] has opened "the floodgates for all different types of content creation" <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>, making [[neural_network_diffusion_concept | diffusion models]] much more useful for applications requiring precise control over image generation <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. The technique's generalizability means it is likely to be usable across other [[neural_network_diffusion_concept | diffusion models]] with similar [[transformer_architecture_in_diffusion_models | U-Net architectures]] <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>. Future developments could involve combining multiple conditional inputs or using multiple [[introduction_to_controlnet | ControlNet]] instances for even more complex control <a class="yt-timestamp" data-t="02:07:06">[02:07:06]</a>.