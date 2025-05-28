---
title: Comparison with Existing Models and Algorithms
videoId: VLrqFH1Xtrs
---

From: [[hu-po]] <br/> 

Bayesian Flow Networks (BFNs) are a new class of generative models that draw comparisons to, and differentiate themselves from, existing models and algorithms in the field of deep learning.

## Core Distinctions from Diffusion Models

BFNs introduce a generative procedure conceptually similar to the reverse process of [[Comparisons with diffusion models | diffusion models]] <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. However, a key difference is that BFNs are conceptually simpler because no forward process is required, unlike [[Comparisons with diffusion models | diffusion models]] <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. While [[Comparisons with diffusion models | diffusion models]] learn by adding and removing noise <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, BFNs operate on the parameters of a data distribution rather than a noisy version of the data itself <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>.

This fundamental difference offers several advantages:
*   **Continuous and Differentiable Process**: The generative process in BFNs remains fully continuous and differentiable even when dealing with discrete data <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>. This contrasts with discrete [[Comparisons with diffusion models | diffusion models]] which inherently use discrete samples as input <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>. Existing continuous variants of discrete [[Comparisons with diffusion models | diffusion models]] typically rely on mapping to or from a continuous embedding space, or restricting continuous diffusion to the probability simplex <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. BFNs' continuity is an inherent property, removing the need for such external constraints or mapping functions, which also reduces the number of free parameters and design choices <a class="yt-timestamp" data-t="00:59:33">[00:59:33]</a>.
*   **Direct Loss Optimization**: BFNs directly optimize the negative log-likelihood of discrete data <a class="yt-timestamp" data-t="00:59:33">[00:59:33]</a>, unlike continuous [[Comparisons with diffusion models | diffusion methods]] for discrete data that often require simplified loss functions or auxiliary loss terms for stability <a class="yt-timestamp" data-t="00:59:52">[00:59:52]</a>.
*   **Initial Noise**: BFNs begin their generative process with parameters of a fixed prior, whereas [[Comparisons with diffusion models | diffusion models]] start from pure noise <a class="yt-timestamp" data-t="01:01:38">[01:01:38]</a>. This reduction in initial noise is hypothesized to lead to faster learning on large datasets where models might underfit <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>.
*   **No Forward Process Inversion**: BFNs do not require defining and inverting a forward process, which arguably makes them easier to adapt to different distributions and data types compared to discretized [[Comparisons with diffusion models | diffusion models]] that need carefully defined transition matrices <a class="yt-timestamp" data-t="01:02:44">[01:02:44]</a>.
*   **Performance**: BFNs have been shown to outperform all known discrete [[Comparisons with diffusion models | diffusion models]] on the Text8 character-level language modeling task <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>.

## Comparison with Auto-Regressive Models

*   **Continuous vs. Discrete Data**: [[Comparison of language models in coding tasks | Auto-regressive networks]] are currently state-of-the-art for language modeling and generally perform well on discrete data where a natural ordering exists <a class="yt-timestamp" data-t="02:09:08">[02:09:08]</a>. They have proved less effective in domains like image generation, where data is continuous and lacks a natural order (e.g., no inherent reason to generate one pixel before another) <a class="yt-timestamp" data-t="02:09:08">[02:09:08]</a>.
*   **Generation Steps**: [[Comparison of language models in coding tasks | Auto-regressive models]] require as many network updates to generate samples as there are variables in the data <a class="yt-timestamp" data-t="02:10:09">[02:10:09]</a>. [[Comparisons with diffusion models | Diffusion models]] have the advantage of decoupling the number of generation steps from the number of variables <a class="yt-timestamp" data-t="02:10:09">[02:10:09]</a>.

## Comparison with Variational Autoencoders (VAEs)

The loss function for BFNs can be derived as the loss function of a [[Comparison of LLaMA with other models | Variational Autoencoder]] (VAE), specifically the negative variational lower bound <a class="yt-timestamp" data-t="01:43:51">[01:43:51]</a>.

## Comparison with Neural Network Architectures

BFNs place no restrictions on the network architecture, meaning various types of Bayesian flow networks can be implemented <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. However, despite their theoretical elegance, the practical scalability on high-dimensional data (e.g., 1024x1024 images, 50,000 token vocabularies) remains a potential challenge compared to highly optimized architectures like Transformers or CNNs <a class="yt-timestamp" data-t="01:14:52">[01:14:52]</a>, <a class="yt-timestamp" data-t="02:11:53">[02:11:53]</a>. For instance, models like capsule networks, though theoretically promising, struggled with scaling and computational efficiency compared to CNNs <a class="yt-timestamp" data-t="01:15:37">[01:15:37]</a>.

## Comparison to Proprietary Models

The paper notes that BFNs achieve competitive log likelihoods for image modeling on dynamically binarized MNIST and CIFAR-10 datasets <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>, performing closest to state-of-the-art when no data augmentation is used <a class="yt-timestamp" data-t="02:43:02">[02:43:02]</a>. For language modeling, BFNs outperform known discrete [[Comparisons with diffusion models | diffusion models]] on the Text8 character-level task <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. However, the language modeling task uses a highly simplified setup (256-character sequences with 27 possible tokens) compared to large language models like [[Comparisons with proprietary models like ChatGPT and Bard | GPT-2]] or [[Comparisons with proprietary models like ChatGPT and Bard | ChatGPT]], which handle much longer contexts and significantly larger vocabularies <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>.

## Flexibility and Generality

BFNs are adaptable to continuous, discretized, and discrete data with minimal changes to the training procedure <a class="yt-timestamp" data-t="01:02:57">[01:02:57]</a>. This flexibility extends to multimodality; there are no restrictions on input or output modalities, allowing BFNs to potentially handle combinations of images and text <a class="yt-timestamp" data-t="03:04:43">[03:04:43]</a>. The loss function directly optimizes data compression <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, an idea linked to concepts like "generalization is compression" and "intelligence is compression" <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, suggesting a broad theoretical applicability.