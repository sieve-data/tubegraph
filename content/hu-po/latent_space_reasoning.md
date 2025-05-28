---
title: latent space reasoning
videoId: Xk8FtcSlFxs
---

From: [[hu-po]] <br/> 

[[latent_space_reasoning | Latent space reasoning]] refers to the process where a model improves its performance by performing computations and "thinking" within a continuous, high-dimensional latent space, rather than relying solely on discrete token sequences <a class="yt-timestamp" data-t="01:03:16">[01:03:16]</a>. This approach contrasts with traditional [[chain_of_thought_reasoning_in_ai | Chain of thought reasoning]] in large language models (LLMs), which primarily operates in token space <a class="yt-timestamp" data-t="01:12:13">[01:12:13]</a>.

## Evolution of AI Thought Processes

Traditionally, reasoning in AI, especially in LLMs, has been confined to token space, which can be thought of as a "verbal world" <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

*   **Verbal Thought (Word Cells):** Models like DeepSeek typically perform reasoning by generating sequences of tokens <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. This is analogous to a "word cell" human who thinks mostly in words and ideas, using an inner monologue <a class="yt-timestamp" data-t="01:00:54">[01:00:54]</a>. The benefit is that this reasoning is interpretable <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.
*   **Visual Thought (Shape Rotators):** More recently, the concept of multimodal [[generative_models_and_visual_space_reasoning | visualization of thought]] has emerged <a class="yt-timestamp" data-t="00:59:23">[00:59:23]</a>. Here, verbal thought can condition an image generation model, producing images that are then converted into vision tokens and fed back into the reasoning chain <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>. This is likened to a "shape rotator" human who thinks primarily in images and spatial terms <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This improves performance for tasks like maze solving <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.
*   **Latent Weavers:** The most advanced form of AI thinking, as described in the paper "Scaling up test time compute with latent reasoning," is to reason entirely in latent space <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>. This model improves by thinking in its [[continuous_thought_and_unrestricted_latent_spaces | continuous latent space]], moving beyond the constraints of a finite vocabulary of tokens <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>.

## Architecture of Latent Reasoning Models

The "Scaling up test time compute with latent reasoning" paper introduces a model structured around decoder-only Transformer blocks, but with a recurrent depth approach <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>, <a class="yt-timestamp" data-t="01:03:40">[01:03:40]</a>.

*   **Prelude:** Embeds input data (token sequence) into a [[highdimensional_spaces_and_information_storage | high-dimensional vector]] or latent space <a class="yt-timestamp" data-t="01:04:48">[01:04:48]</a>.
*   **Recurrent Block:** Takes the embedding and some random noise (similar to [[latent_diffusion_models_and_their_internal_representations | latent diffusion models and their internal representations]]) and processes it recurrently <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>, <a class="yt-timestamp" data-t="01:05:10">[01:05:10]</a>. This block repeatedly transforms the latent state, allowing reasoning to occur in this continuous space <a class="yt-timestamp" data-t="01:05:43">[01:05:43]</a>.
*   **Coda:** Unembeds the final latent state back into a token, producing the output <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.

This recurrent block enables a variable amount of computation for each token, effectively creating a variable-depth Transformer <a class="yt-timestamp" data-t="01:08:20">[01:08:20]</a>, <a class="yt-timestamp" data-t="01:08:57">[01:08:57]</a>. For example, a model with eight real layers can unfold to an effective depth of 132 layers <a class="yt-timestamp" data-t="01:07:10">[01:07:10]</a>.

## Interpretability and Challenges

Understanding the internal thought process of a model reasoning in latent space is challenging due to its continuous and abstract nature <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>.
Techniques like PCA (Principal Component Analysis) can reduce the dimensionality of the latent space to visualize its trajectory <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>. Observations from these visualizations include:

*   **Convergence to a Fixed Point:** Many tokens' latent representations converge to a stable point after several recurrent iterations <a class="yt-timestamp" data-t="01:13:38">[01:13:38]</a>.
*   **Loops:** The model's latent state can enter repetitive patterns, continually revisiting the same area in latent space <a class="yt-timestamp" data-t="01:13:46">[01:13:46]</a>.
*   **Sliders:** Trajectories can noticeably drift in a specific direction, potentially serving as a mechanism for the model to "count" or track iterations within the latent space (a "latent abacus") <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>, <a class="yt-timestamp" data-t="01:16:01">[01:16:01]</a>.

## Advantages and Implications

### Enhanced Test-Time Compute Efficiency
[[latent_space_reasoning | Latent space reasoning]] models offer significant advantages for test-time scaling:

*   **Variable Computation:** They can perform a variable amount of computation for each token, allowing for longer reasoning traces without the quadratic memory scaling issues of traditional Transformers <a class="yt-timestamp" data-t="01:08:20">[01:08:20]</a>, <a class="yt-timestamp" data-t="01:21:01">[01:21:01]</a>.
*   **Speed:** Recurrent neural networks (RNNs), including LSTMs (Long Short-Term Memory) and Mambas, have a constant interaction with memory, making their inference potentially 100 times faster than attention-based Transformers for long sequences <a class="yt-timestamp" data-t="01:17:45">[01:17:45]</a>, <a class="yt-timestamp" data-t="01:18:29">[01:18:29]</a>. This enables "100 times more thinking" at test time <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.
*   **Edge Devices:** This efficiency makes [[latent_space_reasoning | latent space reasoning]] ideal for edge devices like cell phones and robots, where memory and compute are limited <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>, <a class="yt-timestamp" data-t="01:21:51">[01:21:51]</a>. Robots might "think" by [[triplane_representation_and_latent_space_diffusion | latent weaving]] rather than internal verbal monologues <a class="yt-timestamp" data-t="01:22:09">[01:22:09]</a>.

### Distributed Training
Recurrent depth networks perform more floating-point operations per parameter than standard Transformers, reducing communication costs between accelerators at scale <a class="yt-timestamp" data-t="01:22:36">[01:22:36]</a>. This enables higher device utilization, especially when training with slower interconnects <a class="yt-timestamp" data-t="01:22:44">[01:22:44]</a>. This could facilitate more distributed training setups, moving away from reliance on massive, tightly connected data centers <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>.

### Distillation and Self-Improvement
Large, powerful models, trained with RL, are increasingly being distilled into smaller, more efficient models that can run on edge devices <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. This distillation process is architecture-agnostic, meaning a large, complex model can distill its intelligence into a tiny model with a completely different architecture optimized for inference <a class="yt-timestamp" data-t="00:32:08">[00:32:08]</a>, <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

The ability for models to self-improve is also crucial. By generating their own data, filtering out "bad" solutions (e.g., via majority voting), and then training on the "good" filtered data, models can continuously enhance their capabilities <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>, <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>. This suggests that intelligence can accumulate over time, even in subjective domains where traditional reward signals are absent, potentially leading to superhuman performance in areas like philosophy or poetry through [[contrastive_learning_and_emergent_properties | collective intelligence]] <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>, <a class="yt-timestamp" data-t="00:56:17">[00:56:17]</a>.