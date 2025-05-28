---
title: Relative entropy and KL divergence
videoId: LuF4NGezcxo
---

From: [[hu-po]] <br/> 

Relative entropy, also commonly known as Kullback-Leibler (KL) Divergence, is a fundamental concept frequently encountered in machine learning (ML) literature <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. It appears often in various ML papers, particularly in the field of reinforcement learning (RL) <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Definition and Properties
KL Divergence is a measure of the "distance" or difference between two [[concepts_of_probability_distributions_in_ml | probability distributions]], typically denoted as P and Q <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>. It quantifies how inefficient it is to assume distribution Q when the true distribution is P <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. Another interpretation is the expected excess surprise from using Q as a model instead of P, when P is the actual distribution <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

Key properties of KL Divergence include:
*   **Distance Metric**: It serves as a measure of difference between two distributions <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Asymmetry**: The order of P and Q matters; KL(P || Q) is generally not equal to KL(Q || P) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Changing the order can result in a different value <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Regularizer**: It is often used as a regularizer in machine learning models, especially in reinforcement learning, to prevent a policy from drifting too far from a reference or previous policy <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Formulas
The formula for KL Divergence (relative entropy) for discrete distributions is given by:
$$D_{KL}(P \parallel Q) = \sum_x P(x) \log\left(\frac{P(x)}{Q(x)}\right)$$
For continuous distributions, the summation is replaced by an integral:
$$D_{KL}(P \parallel Q) = \int_{-\infty}^{\infty} P(x) \log\left(\frac{P(x)}{Q(x)}\right) dx$$
In these formulas, P typically represents the true distribution of data, while Q represents the model's distribution, often a neural network <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. However, in many applications, such as reinforcement learning, KL Divergence is used between two neural networks or "policies" <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

The value of KL Divergence can be a large or small positive number, or zero if the two distributions are identical <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Use as a Regularizer
In reinforcement learning, KL Divergence is frequently added as a term in the loss function or optimization objective <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. For example, in the DeepSeek R1 paper, a KL term (`dkl`) with a small hyperparameter (`beta`) is included to ensure that the updated policy (neural net) does not deviate too drastically from a reference policy <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This prevents aggressive changes to the policy with each gradient update <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

## Origin and History
The term "KL Divergence" comes from Solomon Kullback and Richard Leibler, who published their seminal paper "On Information and Sufficiency" in 1951 <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. They referred to it as "information in X for discrimination between H1 and H2" <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>.

Kullback and Leibler were code breakers who worked at the NSA after World War II <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>. Kullback helped crack the Enigma machine, and Leibler worked on the Venona code-breaking project <a class="yt-timestamp" data-t="01:12:26">[01:12:26]</a>. Their work was part of the early development of information theory, driven by the need to understand and crack codes <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>.

The speaker prefers the term "relative entropy" over "KL Divergence," arguing that naming concepts after individuals (a "vanity name") hinders understanding, whereas "relative entropy" helps explain its origin from information theory and entropy concepts <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

## Connection to Entropy and Cross-Entropy
KL Divergence is directly related to [[mathematical_basis_and_historical_background_of_entropy | entropy]] and cross-entropy through the formula:
$$D_{KL}(P \parallel Q) = H(P, Q) - H(P)$$
Where:
*   $H(P, Q)$ is the cross-entropy of P and Q.
*   $H(P)$ is the entropy of P <a class="yt-timestamp" data-t="01:16:38">[01:16:38]</a>.

### Types of Entropy
The term "entropy" can be overloaded, referring to various concepts:
1.  Thermodynamic entropy <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>
2.  Entropy in classical statistical mechanics <a class="yt-timestamp" data-t="01:17:08">[01:17:08]</a>
3.  Entropy in quantum statistical mechanics <a class="yt-timestamp" data-t="01:17:11">[01:17:11]</a>
4.  [[mathematical_basis_and_historical_background_of_entropy | Entropy in Information Theory]] <a class="yt-timestamp" data-t="01:17:14">[01:17:14]</a>
5.  Algorithmic entropy <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>

The entropy relevant to relative entropy and KL Divergence is [[mathematical_basis_and_historical_background_of_entropy | entropy in information theory]], introduced by Claude Shannon <a class="yt-timestamp" data-t="01:17:52">[01:17:52]</a>.

#### Shannon Entropy
Shannon's entropy, often denoted as H, measures the average "surprise" or uncertainty associated with a random variable's possible outcomes <a class="yt-timestamp" data-t="01:21:07">[01:21:07]</a>.
*   **Fair Coin Flip**: A fair coin (50/50 chance of heads/tails) has an entropy of 1 bit, representing maximum uncertainty <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>.
*   **Biased Coin Flip**: A biased coin (e.g., 70% heads, 30% tails) has lower entropy (e.g., 0.88), indicating less uncertainty because one outcome is more likely <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>. Non-uniform probabilities yield less uncertainty and thus less entropy <a class="yt-timestamp" data-t="01:20:50">[01:20:50]</a>.

#### Algorithmic Entropy
Algorithmic entropy, also known as Kolmogorov complexity, defines the entropy of a string of symbols as the length of the shortest computer program that can print it out <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>. This concept relates to efficient encoding: more frequent symbols should be encoded with fewer bits to minimize the total message length <a class="yt-timestamp" data-t="01:23:03">[01:23:03]</a>.

#### Historical Roots
The concept of entropy can be traced back to 19th-century thermodynamics and classical statistical mechanics, particularly the work of Ludwig Boltzmann <a class="yt-timestamp" data-t="01:24:08">[01:24:08]</a>. Boltzmann connected the known concept of entropy to probability, shifting the understanding of reality towards uncertainty and information <a class="yt-timestamp" data-t="01:24:38">[01:24:38]</a>. John von Neumann, a polymath, advised Shannon to use the term "entropy" for his measure of information, noting its similarity to the concept in physics and Boltzmann's use of the letter 'H' <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>.

## Application in Machine Learning (DeepSeek R1 Example)
KL Divergence is extensively used in modern machine learning. In the DeepSeek R1 paper, it is part of the optimization objective for their technique called GRPO <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The objective includes a KL term `dkl(Pi_Theta || Pi_Reference)` <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   `Pi_Theta` represents the current policy (a neural network parameterized by Theta).
*   `Pi_Reference` is a reference policy, often an older version of `Pi_Theta` from previous training steps <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

The KL term ensures that the new policy `Pi_Theta` does not "drift" too far from the reference policy during iterative improvement, which is common in reinforcement learning to stabilize training <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## [[Implementation of KL divergence in various frameworks | Implementation of KL Divergence in Various Frameworks]]

The [[implementation_of_kl_divergence_in_various_frameworks | implementation of KL Divergence]] in ML frameworks involves considerations for numerical stability and computational efficiency.

### JAX
In JAX, KL Divergence is available as `jax.scipy.special.kl_div`. This function takes two "array-like" distributions, `P` and `Q`, which are tensors representing the probabilities of outcomes <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   JAX wraps the call to an internal function `_relative_entropy` <a class="yt-timestamp" data-t="01:33:36">[01:33:36]</a>.
*   It includes checks (`promote_args_inexact`) to ensure correct data types, sizes, and handling of pseudo-random number generator (PRNG) keys for repeatable randomness <a class="yt-timestamp" data-t="01:32:51">[01:32:51]</a>.
*   **Numerical Stability**: The calculation must handle cases where `Q(x)` is zero (leading to division by zero) or `P(x)` is zero (leading to log of zero, or negative infinity) <a class="yt-timestamp" data-t="01:34:17">[01:34:17]</a>. JAX uses "safe P" and "safe Q" mechanisms to replace zeros or infinities, preventing issues <a class="yt-timestamp" data-t="01:34:40">[01:34:40]</a>.
*   **Logarithmic Scale**: Working in logarithmic scale (`log_probabilities`) is crucial for numerical stability, especially with very small probabilities common in large language models. It converts multiplications into additions and smooths out the range of numbers, preventing underflow or overflow <a class="yt-timestamp" data-t="01:42:30">[01:42:30]</a>.
*   **Low-level Implementation**: At the lowest level, the `log` function itself is implemented in Cuda or CPU libraries using series expansions to approximate its value <a class="yt-timestamp" data-t="01:46:18">[01:46:18]</a>.

### PyTorch
PyTorch offers KL Divergence through `torch.nn.functional.kl_div` and `torch.nn.KLDivLoss` <a class="yt-timestamp" data-t="01:51:49">[01:51:49]</a>.
*   The functional API's `kl_div` ultimately calls a C++ implementation in `native_loss.cpp` <a class="yt-timestamp" data-t="01:53:53">[01:53:53]</a>.
*   It supports an optional `log_target` parameter, allowing the input distributions to be provided in log space, which avoids redundant log computations if probabilities are already in log form <a class="yt-timestamp" data-t="01:53:30">[01:53:30]</a>.
*   PyTorch also includes a more object-oriented approach in `torch.distributions.kl.py`, which features a dictionary of specific KL implementations for different distribution types (e.g., Beta, Binomial, Categorical, Gaussian) <a class="yt-timestamp" data-t="01:54:25">[01:54:25]</a>.

### TensorFlow
TensorFlow's popularity has significantly declined since its peak in 2018, with PyTorch now dominating the ML framework market share according to Papers With Code data <a class="yt-timestamp" data-t="01:56:40">[01:56:40]</a>. While `tf.keras.metrics.KLDivergence` exists, its use is less common today <a class="yt-timestamp" data-t="01:56:37">[01:56:37]</a>.

### TinyGrad
TinyGrad, a lightweight ML framework, notably does not have an explicit `kl_div` implementation <a class="yt-timestamp" data-t="01:59:43">[01:59:43]</a>. This design choice is due to its creator George Hotz's emphasis on minimizing lines of code <a class="yt-timestamp" data-t="02:02:59">[02:02:59]</a>. Since minimizing cross-entropy is "essentially the same as minimizing KL Divergence plus some constant" <a class="yt-timestamp" data-t="02:01:53">[02:01:53]</a>, TinyGrad leverages its existing cross-entropy implementation to serve the same purpose, avoiding redundant code <a class="yt-timestamp" data-t="02:03:30">[02:03:30]</a>.

## Conclusion
Relative entropy, or KL Divergence, is a versatile and essential tool in machine learning, particularly for training models and policies in reinforcement learning. Its mathematical properties allow it to measure the difference between [[concepts_of_probability_distributions_in_ml | probability distributions]], while its historical roots in code-breaking and information theory underscore its foundational importance <a class="yt-timestamp" data-t="02:06:02">[02:06:02]</a>. Despite its complex underlying [[implementation_of_kl_divergence_in_various_frameworks | implementations]] and the variety of related entropy concepts, its core utility in regularizing model behavior and understanding information flow remains central to advancements in AI <a class="yt-timestamp" data-t="02:05:30">[02:05:30]</a>.