---
title: Causal effects and internal representations in machine learning
videoId: 3updXylOFvY
---

From: [[hu-po]] <br/> 

This article reviews a pre-print paper titled "Beyond Surface Statistics: Scene Representation in a Latent Diffusion Model," which investigates the internal workings of [[Generative Latent Spaces in AI | latent diffusion models]] (LDMs) <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. While pre-prints are common in the fast-paced field of machine learning, this paper is particularly valuable as an "investigation paper," dissecting a model to gain intuition rather than introducing new algorithms <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. It falls within the broader category of [[Implications of models reasoning in latent space | interpretability research]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Understanding Latent Diffusion Models (LDMs)

[[Generative Latent Spaces in AI | Latent diffusion models]] (LDMs) are generative frameworks capable of synthesizing high-quality images from descriptive text <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. They operate in a latent space, which is a compressed representation of images created by a Variational Autoencoder (VAE) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This allows for more efficient computation and memory usage compared to diffusing directly in image space <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>. The LDM is trained to predict and remove noise added during a forward diffusion process <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

Crucially, the LDM studied (Stable Diffusion V1) was trained purely on images without explicit depth information <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Despite this, it outputs coherent pictures of 3D scenes <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### DDPM vs DDIM

The paper touches upon different diffusion processes, specifically Denoising Diffusion Probabilistic Models (DDPMs) and Denoising Diffusion Implicit Models (DDIMs) <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   DDPMs are Markov chains, meaning each step depends on the previous one, making them slower but often yielding higher quality <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>. They involve adding Gaussian noise <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>.
*   DDIMs are non-Markovian, allowing steps to be skipped, resulting in faster generation but potentially lower quality and more diverse outputs <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. They do not add random noise during the denoising process <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>.

## Investigating Internal Representations

The core question of the paper is whether an LDM creates and uses an internal representation of simple scene geometry, or if it merely memorizes superficial correlations between pixel values and words <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Methodology: Linear Probing

To answer this, the authors apply the methodology of linear probing <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. This involves:
1.  **Extracting Intermediate Activations**: Taking the values from a specific layer within the neural network, treating it as the model's internal representation <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>.
2.  **Training a Probing Classifier/Regressor**: A simple, single-layer linear model is trained on these intermediate activations to predict a specific property, such as pixel-level depth <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
3.  **Assessing Performance**: High prediction accuracy indicates a strong correlation between the learned representation and the predicted property <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.

A controlled experiment was conducted by training probing classifiers on a randomly initialized (untrained) LDM. The significantly worse performance of probes on the randomized model validates that the strong correlations found in the trained LDM are not spurious but indicate genuine learned representations <a class="yt-timestamp" data-t="01:05:06">[01:05:06]</a>.

### Findings: Early Emergence of Depth and Saliency

The study found compelling evidence that LDMs develop sophisticated internal representations:
*   **3D Depth Data**: The internal activations encode linear representations of both continuous 3D depth and salient object/background distinction <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Continuous depth refers to a single value for each pixel representing distance from the camera <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, while salient object/background distinction is a binary depth representation <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>.
*   **Early Development**: These representations appear "surprisingly early" in the denoising process <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. Even when the image appears as pure noise to a human, the LDM's internal representation already has an idea of foreground, background, and edges <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>. This suggests the model rapidly establishes geometric properties <a class="yt-timestamp" data-t="01:03:52">[01:03:52]</a>.

    *Figure illustrating early depth emergence:*
    In early denoising steps, models like Midas (for monocular depth estimation) and Tracer (for salient object detection) fail to interpret noisy images <a class="yt-timestamp" data-t="01:11:05">[01:11:05]</a>. However, the probing classifiers trained on the LDM's internal representations can accurately predict depth and object masks <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>. For instance, at step one, the LDM already has a clear idea of what will be foreground and background <a class="yt-timestamp" data-t="01:18:02">[01:18:02]</a>.

### LDM vs. VAE in Representation Learning

A crucial distinction is made between the LDM itself and the VAE:
*   The VAE's internal representations show weak depth information, especially with corrupted latents in early steps <a class="yt-timestamp" data-t="01:13:03">[01:13:03]</a>. It can only decode salient objects once details in latent vectors become perceptible <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   The [[Generative Latent Spaces in AI | latent diffusion model]] (the diffusion part) encodes a much stronger representation of depth and saliency, even in very early denoising steps <a class="yt-timestamp" data-t="01:13:12">[01:13:12]</a>. This means the LDM *itself* is responsible for building this depth understanding, not merely inheriting it from the VAE <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>.

### Impact of Architecture: CNNs vs. Vision Transformers (ViTs)

The paper also briefly compares convolutional neural networks (CNNs) and Vision Transformers (ViTs) in their ability to form internal representations. ViTs generally outperform CNNs in depth estimation tasks and exhibit stronger depth and saliency representations in their self-attention layers compared to CNNs' convolutional layers <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.

## Causal Role of Representations in Image Synthesis

Beyond mere correlation, the study performed "causal intervention experiments" to demonstrate that these representations play a direct causal role in image synthesis <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Intervention Method**: The researchers take the intermediate representation from the LDM, deliberately modify it (e.g., shifting the foreground object), and then feed this altered representation back into the model <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>.
*   **Observed Effect**: This intervention leads to a corresponding, predictable change in the apparent depth or position of objects in the final generated image <a class="yt-timestamp" data-t="01:26:38">[01:26:38]</a>. For instance, shifting a foreground object's internal representation leads to the object being repositioned in the final image <a class="yt-timestamp" data-t="01:20:55">[01:20:55]</a>.

This process is similar to [[Applications in machine learning and reinforcement learning | ControlNet]], where external conditioning (like edge maps or skeleton poses) is injected into multiple layers of a diffusion model to steer its output <a class="yt-timestamp" data-t="01:27:19">[01:27:19]</a>. While the paper uses a gradient-based approach from a probing classifier, the principle of directly manipulating internal states to affect output is analogous <a class="yt-timestamp" data-t="01:28:40">[01:28:40]</a>.

## Implications and Future Work

The findings add nuance to the ongoing debate about whether generative models learn more than just "surface statistics" <a class="yt-timestamp" data-t="01:42:29">[01:42:29]</a>. The presence of linear, causally-linked depth and saliency representations suggests that LDMs build "world models" – an underlying understanding of spatial geometry, even without explicit 3D training <a class="yt-timestamp" data-t="01:42:36">[01:42:36]</a>. This aligns with the concept of [[Platonic representation in AI models | Platonic representation in AI models]], where fundamental concepts are learned implicitly.

Future avenues for research include:
*   Looking for internal representations of other scene attributes like lighting or texture <a class="yt-timestamp" data-t="01:42:44">[01:42:44]</a>.
*   Exploring models of semantic aspects of a scene, such as sentiment <a class="yt-timestamp" data-t="01:42:57">[01:42:57]</a>.

The study highlights the value of [[Implications of models reasoning in latent space | interpretability research]] in understanding complex black-box neural networks and leveraging that understanding for applications like high-level image editing <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.