---
title: Evaluation of 3D generative techniques
videoId: azCp-b7c-GM
---

From: [[hu-po]] <br/> 

The evaluation of 3D generative techniques involves assessing their output quality, efficiency, and adherence to specific conditions, as demonstrated by the development of models like Shape-E and Point-E <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This field is characterized by a diversity of 3D representations and evolving generative models <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

## Challenges in 3D Representation and Generation

Unlike 2D images or audio, 3D assets lack a single, obvious fixed-size tensor representation, making their generation more complex <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Various methods exist for representing 3D assets, such as Neural Radiance Fields (NeRFs), meshes with textures, and Signed Distance Functions (SDFs) <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. A significant challenge lies in creating representations that are both efficient to generate and easy to use in downstream applications like game engines, which primarily use textured meshes <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

While [[advancements_in_3d_generative_models_using_neural_networks|Implicit Neural Representations (INRs)]] like NeRFs are flexible and expressive, acquiring them for large datasets can be costly, and their many numerical parameters pose challenges for training generative models <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

## Comparison: Shape-E vs. Point-E

Shape-E is presented as a follow-up to Point-E, both developed by the same researchers at OpenAI <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Both models generate 3D shapes from text <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

*   **Output Representation:**
    *   Point-E is an explicit generative model over point clouds <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. Its samples often appear as "little tiny beads" <a class="yt-timestamp" data-t="01:43:57">[01:43:57]</a>.
    *   Shape-E directly generates parameters of [[3d_implicit_functions_and_generative_models|implicit functions]], specifically Signed Texture Fields (STFs), which can be rendered as both textured meshes and NeRFs <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>, <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

*   **Performance and Quality:**
    *   Shape-E converges faster and achieves comparable or better sample quality than Point-E <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>, <a class="yt-timestamp" data-t="01:42:47">[01:42:47]</a>.
    *   A sample generation takes approximately 13 seconds on a single Nvidia V100 GPU (likely 32GB version) <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>, <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   Surprisingly, Shape-E and Point-E tend to share success and failure cases when conditioned on images, suggesting that different output representations can still lead to similar model behavior <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>, <a class="yt-timestamp" data-t="01:44:57">[01:44:57]</a>.

*   **Model Architecture:**
    *   Shape-E uses a Transformer-based encoder and a conditional diffusion model operating in the latent space of the encoder <a class="yt-timestamp" data-t="01:09:06">[01:09:06]</a>, <a class="yt-timestamp" data-t="01:39:07">[01:39:07]</a>.
    *   A novel aspect is that the encoder's output *is* the weights of a multi-layer perceptron (MLP) that defines the implicit function <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>, <a class="yt-timestamp" data-t="01:14:47">[01:14:47]</a>.
    *   Both models use CLIP embeddings for image conditional generation, despite an initial statement that Shape-E does not require a separate text-to-image model <a class="yt-timestamp" data-t="01:39:46">[01:39:46]</a>, <a class="yt-timestamp" data-t="01:40:10">[01:40:10]</a>.

### Evaluation Metrics

To quantitatively compare models, the following metrics are used:
*   **Peak Signal-to-Noise Ratio (PSNR):** A quantitative measure of image quality, where a higher value indicates better quality <a class="yt-timestamp" data-t="01:29:57">[01:29:57]</a>, <a class="yt-timestamp" data-t="01:42:09">[01:42:09]</a>.
*   **CLIP R-Precision:** Measures the similarity in CLIP space between generated samples and target prompts/images, with higher values being better <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>, <a class="yt-timestamp" data-t="01:42:11">[01:42:11]</a>.

In preliminary scans, L1 loss for Nerf rendering outperformed L2 loss <a class="yt-timestamp" data-t="01:20:21">[01:20:21]</a>. However, for STF rendering, L2 loss was found to be more stable than L1 loss <a class="yt-timestamp" data-t="01:27:25">[01:27:25]</a>.

## Comparison to Other Methods

Shape-E is compared to other 3D generative techniques such as Dream Fields, CLIPMesh, and DreamFusion <a class="yt-timestamp" data-t="01:45:45">[01:45:45]</a>.

*   **Inference Speed:** Shape-E's inference time (13 seconds) is "orders of magnitude faster" than optimization-based approaches like Dream Fields, which can take up to 200 hours on a V100 GPU <a class="yt-timestamp" data-t="01:48:40">[01:48:40]</a>, <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. This speed advantage is a major strength.

## [[Challenges and limitations in 3D generation|Limitations and Future Work]]

*   **Data Dependency:** A significant limitation is the reliance on a large, proprietary dataset of paired 3D and text data, collected by OpenAI <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>. This "secret data set" limits fair comparisons with other open-source techniques <a class="yt-timestamp" data-t="01:47:40">[01:47:40]</a>.
*   **Compositionality and Natural Language Understanding:** The text-conditional model has limited ability to compose concepts, struggling to bind multiple attributes to different objects or reliably produce the correct number of objects when asked for more than two <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>. These failures are likely due to limited paired training data <a class="yt-timestamp" data-t="01:47:05">[01:47:05]</a>.
*   **Fixed Camera Elevation:** The training data uses images from a constant 30-degree elevation, potentially limiting the model's ability to generalize to varied viewing angles <a class="yt-timestamp" data-t="02:04:25">[02:04:25]</a>.
*   **Hardware Budget Constraints:** Decisions like not performing large hyperparameter sweeps or extensive ablation studies suggest the researchers are working within a limited computational budget, which might impact the full potential of the model <a class="yt-timestamp" data-t="02:04:51">[02:04:51]</a>.
*   **Opaque Data Source:** The lack of transparency regarding the dataset (which includes roughly 1 million additional 3D assets with human-provided captions) makes it difficult for external researchers to reproduce or build upon the work <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.

Despite these limitations, the concept of using one neural network to output the weights of another, as seen in Shape-E's MLP generation, is considered "revolutionary" and could have applications beyond 3D generation, potentially in robotics <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. The [[future_potential_and_direction_for_generative_3d_technology|future of 3D generation]] is bright, with expectations that users will soon be able to type prompts for 3D files similar to current 2D image generation within five years, or even two years <a class="yt-timestamp" data-t="02:11:26">[02:11:26]</a>.