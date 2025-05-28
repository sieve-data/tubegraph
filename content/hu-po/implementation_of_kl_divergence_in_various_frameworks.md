---
title: Implementation of KL divergence in various frameworks
videoId: LuF4NGezcxo
---

From: [[hu-po]] <br/> 

[[relative_entropy_and_kl_divergence | Relative entropy]], also known as [[relative_entropy_and_kl_divergence | KL Divergence]] (Kullback–Leibler divergence), is a concept frequently encountered in machine learning papers, particularly within the field of [[Optimization Methods in Machine Learning | reinforcement learning]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. It serves as a measure of how one probability distribution differs from a reference distribution <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

It is commonly used as a regularizer in objective functions to prevent a model's policy from drifting too far from a reference or previous policy <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For example, in the DeepSeek R1 paper, [[relative_entropy_and_kl_divergence | KL Divergence]] appears as a term in their GPRO optimization objective, regularizing the current policy (Pi Theta) against a reference policy (Pi reference) <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Similarly, Kim K 1.5 also employs a [[relative_entropy_and_kl_divergence | KL Divergence]] term for policy regularization <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

While often referred to as [[relative_entropy_and_kl_divergence | KL Divergence]], the term "relative entropy" is considered more descriptive as it highlights its origins in [[relative_entropy_and_kl_divergence | information theory]] and entropy <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>. The term "KL Divergence" originated from the mathematicians Kullback and Leibler, who were involved in code-breaking during the post-World War II era at the NSA <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a> <a class="yt-timestamp" data-t="01:06:02">[01:06:02]</a>.

## Core Concepts

*   **Definition**: [[relative_entropy_and_kl_divergence | KL Divergence]] measures the "distance" or inefficiency when approximating a true probability distribution (P) with another distribution (Q) <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Asymmetry**: The order of P and Q matters; [[relative_entropy_and_kl_divergence | KL Divergence]] of P from Q is not the same as Q from P <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a> <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Relationship with Entropy**: [[relative_entropy_and_kl_divergence | KL Divergence]] is directly related to [[relative_entropy_and_kl_divergence | cross-entropy]] and entropy. Specifically, `DKL(P || Q) = H(P, Q) - H(P)`, where `H(P, Q)` is the [[relative_entropy_and_kl_divergence | cross-entropy]] of P and Q, and `H(P)` is the entropy of P <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Numerical Stability**: Due to operations like division and logarithms, [[relative_entropy_and_kl_divergence | KL Divergence]] computations can be numerically unstable (e.g., division by zero, logarithm of zero, overflow issues) <a class="yt-timestamp" data-t="00:38:37">[00:38:37]</a>. This is often mitigated by using log probabilities, which convert multiplications into additions and smooth out large or small values <a class="yt-timestamp" data-t="00:43:10">[00:43:10]</a> <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>.
*   **Approximation**: For complex or high-dimensional distributions, the sum or integral required for [[relative_entropy_and_kl_divergence | KL Divergence]] is often approximated using Monte Carlo estimation techniques <a class="yt-timestamp" data-t="00:36:25">[00:36:25]</a>.

## Implementations in Machine Learning Frameworks

### Jax

Jax, often seen as a successor to TensorFlow, aims for an approachable syntax similar to NumPy and SciPy <a class="yt-timestamp" data-t="00:30:20">[00:30:20]</a>.
The `jax.scipy.special.kl_div` function takes two array-like distributions, `P` and `Q` <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>. Internally, this function calls `relative_entropy`, which is the preferred name for the concept within Jax's deeper implementation <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a> <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>.

The implementation handles numerical stability by replacing zero values in `P` or `Q` with a small non-zero number or adjusting the logic to avoid division by zero or logarithm of zero, ensuring "safe" computations for `log(P)` and `log(P/Q)` <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>. The core calculation often reduces to `X log X` and `X log Y`, which are ultimately computed by low-level libraries like CUDA or CPU-specific math libraries <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a> <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.

### PyTorch

PyTorch offers multiple ways to compute [[relative_entropy_and_kl_divergence | KL Divergence]]:
*   `nn.functional.kl_div`: A general-purpose function <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>. This Python function acts as a wrapper that calls a more fundamental C++ implementation <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>. It allows specifying if the input probabilities are already in log-space, avoiding redundant log computations <a class="yt-timestamp" data-t="00:53:42">[00:53:42]</a>.
*   `nn.KLDivLoss`: A loss module that wraps the functional version <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.
*   `torch.distributions.kl.kl_divergence`: A more abstract, object-oriented approach <a class="yt-timestamp" data-t="00:54:30">[00:54:30]</a>. This implementation uses a dictionary to store different [[relative_entropy_and_kl_divergence | KL Divergence]] formulas optimized for specific pairs of distribution types (e.g., Beta-Beta, Binomial-Binomial, Categorical-Categorical) <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.

### TensorFlow

TensorFlow, while once dominant, has seen a decline in usage, with PyTorch now holding the largest market share in research implementations <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a> <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a>. Its implementation of [[relative_entropy_and_kl_divergence | KL Divergence]] is less frequently discussed in current contexts due to the general shift in framework preference <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.

### Tinygrad

Tinygrad, a newer and minimalist machine learning framework, notably does **not** have a direct, explicit implementation of [[relative_entropy_and_kl_divergence | KL Divergence]] or [[relative_entropy_and_kl_divergence | relative entropy]] <a class="yt-timestamp" data-t="01:00:18">[01:00:18]</a>. This design choice is driven by its philosophy of extreme code brevity <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>. As minimizing [[relative_entropy_and_kl_divergence | cross-entropy]] is mathematically equivalent to minimizing [[relative_entropy_and_kl_divergence | KL Divergence]] plus a constant term (the entropy of the true distribution, H(P)) <a class="yt-timestamp" data-t="01:01:53">[01:01:53]</a> <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a>, Tinygrad relies on its [[relative_entropy_and_kl_divergence | cross-entropy]] implementation to cover use cases where [[relative_entropy_and_kl_divergence | KL Divergence]] would typically be applied <a class="yt-timestamp" data-t="01:03:42">[01:03:42]</a>. This allows it to reduce line count but might be less explicit for users <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a>.