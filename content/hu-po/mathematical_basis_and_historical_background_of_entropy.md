---
title: Mathematical basis and historical background of entropy
videoId: LuF4NGezcxo
---

From: [[hu-po]] <br/> 

[[relative_entropy_and_kl_divergence | Relative entropy]], also known as Kullback-Leibler (KL) Divergence, is a fundamental concept frequently encountered in machine learning, particularly in reinforcement learning papers <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. It serves as a measure of the difference between two [[concepts_of_probability_distributions_in_ml | probability distributions]] <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>.

## Origin of KL Divergence

The term "KL Divergence" originates from two individuals, Kullback and Leibler, who introduced the concept in their 1951 paper, "On Information and Sufficiency" <a class="yt-timestamp" data-t="01:11:21">[01:11:21]</a>.

*   **Solomon Kullback (1907-1994)**: Supervised a team of about 60 people at the NSA and contributed to the development of memory technologies like magnetic tape <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **Richard Leibler (1914-2003)**: Celebrated for his work on the Venona code-breaking project and served as director of the Communication Research Division at the National Security Agency <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

Both Kullback and Leibler were code-breakers who worked at the NSA post-World War II <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Their work was part of the nascent field of information theory, which aimed to use mathematical principles to crack codes <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Kullback notably helped crack the [[history_and_evolution_of_narrow_asi_like_calculators | Enigma machine]] in Britain <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

### Why "Relative Entropy" is Preferred

While commonly known as KL Divergence, the term "[[relative_entropy_and_kl_divergence | relative entropy]]" is considered more descriptive <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. The use of personal names in mathematical concepts, like "Kullback-Leibler Divergence," can be seen as vanity names that don't aid in understanding the underlying idea <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. In contrast, "[[relative_entropy_and_kl_divergence | relative entropy]]" directly implies its connection to information theory and entropy, thereby helping to explain the concept <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

## Mathematical Basis: Connection to Entropy

[[relative_entropy_and_kl_divergence | Relative entropy]] is directly related to **cross-entropy** and **entropy**:

$D_{KL}(P || Q) = H(P, Q) - H(P)$ <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>

Where:
*   $D_{KL}(P || Q)$ is the [[relative_entropy_and_kl_divergence | relative entropy]] of Q from P.
*   $H(P, Q)$ is the cross-entropy of P and Q.
*   $H(P)$ is the entropy of P.

Minimizing cross-entropy is essentially equivalent to minimizing KL Divergence plus a constant, which means that for practical purposes, often minimizing one can serve the purpose of minimizing the other, especially when the entropy of P is stable or unimportant to the optimization <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Types of Entropy

The term "entropy" is overloaded, referring to several distinct but related concepts <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>:

1.  [[future_of_thermodynamic_computing | Thermodynamic entropy]] <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>
2.  Entropy in classical statistical mechanics <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>
3.  Entropy in [[basics_of_quantum_computing_and_operators | quantum statistical mechanics]] <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>
4.  Entropy in information theory <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>
5.  Algorithmic entropy <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>

The [[relative_entropy_and_kl_divergence | relative entropy]] specifically refers to entropy in **information theory** <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.

#### Information Theory Entropy (Shannon Entropy)

[[relative_entropy_and_kl_divergence | Entropy]] in information theory was developed by Claude Shannon <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. At its core, entropy is a measure of information or uncertainty <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

John Von Neumann advised Shannon to use the term "entropy" because a similar concept existed in physics (thermodynamics and classical statistical mechanics), and Ludwig Boltzmann had used the letter 'H' to describe it <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.

*   **Fair Coin vs. Biased Coin Example**:
    *   A fair coin flip (50% heads, 50% tails) yields maximum uncertainty and therefore maximum entropy (e.g., 1 bit of entropy for a binary outcome) <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
    *   A biased coin flip (e.g., 70% heads, 30% tails) yields less uncertainty and therefore lower entropy (e.g., 0.88 bits) <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.
    *   Entropy can be thought of as a measure of "expected excess surprise" <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

This concept extends to **algorithmic entropy**, where the entropy of a string of symbols is the length of the shortest computer program that prints it out <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This relates to how code-breakers would efficiently encode messages: more frequent symbols require fewer bits to encode for maximum efficiency <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

#### Classical Statistical Mechanics Entropy (Boltzmann Entropy)

Boltzmann's work in classical statistical mechanics connected the concept of entropy to probability <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>. His famous equation, inscribed on his grave, describes how in any random process, the final arrangement of matter is more likely than the initial arrangement, linking to the second law of thermodynamics <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

The idea of entropy can be traced back to the 1800s with the Carnot cycle and the study of heat and gases <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. Boltzmann's probabilistic approach to entropy, which describes how molecules in a gas tend to become more random and fill their container, influenced Von Neumann, who then advised Shannon, leading to the development of information-theoretic entropy <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

## Practical Use in Machine Learning

[[relative_entropy_and_kl_divergence | KL Divergence]] is widely used in machine learning:

*   **Regularization**: It acts as a regularizer in loss functions to prevent a model's policy (a neural network's probability distribution over actions or outputs) from drifting too far from a reference policy <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.
    *   For example, in reinforcement learning algorithms like DeepSeek R1 and Kim K 1.5, a small beta-weighted KL term is added to the optimization objective <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This ensures that the updated policy remains close to the previous policy, preventing drastic changes during iterative training <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
    *   It is also seen in models like autoencoding [[bayesian_statistics_and_machine_learning | variational Bayes]] <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **Distance Metric**: It quantifies how inefficient it is to assume [[concepts_of_probability_distributions_in_ml | distribution]] Q when the true [[concepts_of_probability_distributions_in_ml | distribution]] is P <a class="yt-timestamp" data-t="07:09:00">[07:09:00]</a>. It's not symmetric, meaning order matters <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. A KL Divergence of zero indicates identical distributions <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

## Implementation Details: Numerical Stability

Implementing [[relative_entropy_and_kl_divergence | KL Divergence]] requires careful handling of numerical stability issues due to the nature of the formula ($P(x) \log \frac{P(x)}{Q(x)}$) <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>:

*   **Division by Zero**: If $Q(x)$ is zero, the division becomes undefined <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Logarithm of Zero**: If $P(x)$ is zero, taking its logarithm leads to negative infinity <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **Overflow Issues**: KL Divergence can become very large if the difference between $P(x)$ and $Q(x)$ is significant, leading to overflow, especially with lower-precision data types like float16 <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

To mitigate these issues, machine learning models often work in a **logarithmic scale** <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. Logarithms convert multiplication to addition and division to subtraction ($\log(x/y) = \log(x) - \log(y)$), simplifying derivatives and preventing underflow or overflow by "smoothing out" very large or very small numbers <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

## KL Divergence Implementations in ML Frameworks

### JAX
JAX's `kl_div` function handles numerical stability by using `promote_args_inexact` and `jnp.where` to ensure that `P` and `Q` values are not zero before calculations <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Deeper in its implementation, `kl_div` calls `relative_entropy`, indicating a preference for the more descriptive name <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. For complex [[concepts_of_probability_distributions_in_ml | probability distributions]] where analytical summation is impractical, [[relative_entropy_and_kl_divergence | KL Divergence]] is often estimated using Monte Carlo techniques <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>.

### PyTorch
PyTorch offers multiple implementations: `nn.functional.kl_div` and `nn.KLDivLoss` <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. The functional API directly calls a C++ implementation that applies the [[relative_entropy_and_kl_divergence | relative entropy]] formula, with a conditional check (`if log_target else`) to handle inputs already in log-space, avoiding redundant log computations <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>. Additionally, `torch.distributions.kl.py` contains numerous specific [[relative_entropy_and_kl_divergence | KL Divergence]] implementations tailored to different [[concepts_of_probability_distributions_in_ml | distribution]] types (e.g., Beta, Binomial, Categorical), making it an object-oriented approach <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### TensorFlow
TensorFlow, though once dominant, has seen a significant decline in usage, with PyTorch now holding the largest market share in research papers <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>.

### TinyGrad
TinyGrad, a machine learning framework focused on minimizing lines of code, does not have a dedicated [[relative_entropy_and_kl_divergence | KL Divergence]] implementation <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This design choice is based on the fact that minimizing cross-entropy is mathematically similar to minimizing [[relative_entropy_and_kl_divergence | KL Divergence]] (differing only by a constant related to the entropy of the true [[concepts_of_probability_distributions_in_ml | distribution]]) <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>. Therefore, users can achieve similar regularization effects using cross-entropy, adhering to TinyGrad's philosophy of code simplicity <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.