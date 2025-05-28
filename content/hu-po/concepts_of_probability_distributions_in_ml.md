---
title: Concepts of probability distributions in ML
videoId: LuF4NGezcxo
---

From: [[hu-po]] <br/> 

## Relative Entropy and KL Divergence

[[relative_entropy_and_KL_divergence | Relative entropy]], also known as Kullback-Leibler (KL) Divergence, is a fundamental concept in machine learning, appearing frequently in research papers, particularly in [[applications_in_machine_learning_and_reinforcement_learning | reinforcement learning]] <a class="yt-timestamp" data-t="03:30">03:30</a>. It serves as a measure of the "distance" or difference between two probability distributions, typically denoted as P and Q <a class="yt-timestamp" data-t="07:05">07:05</a>.

Key characteristics of KL Divergence include:
*   It is a **distance metric** between two probability distributions <a class="yt-timestamp" data-t="07:05">07:05</a>.
*   It is **not symmetric**, meaning the order of P and Q matters (DKL(P||Q) is not necessarily equal to DKL(Q||P)) <a class="yt-timestamp" data-t="08:02">08:02</a>, <a class="yt-timestamp" data-t="09:35">09:35</a>.
*   It is commonly used as a **regularizer** in [[Optimization Methods in Machine Learning | optimization functions]] to prevent a model's policy from drifting too far from a reference policy <a class="yt-timestamp" data-t="04:54">04:54</a>, <a class="yt-timestamp" data-t="09:51">09:51</a>.

### Applications in Machine Learning

In [[applications_in_machine_learning_and_reinforcement_learning | reinforcement learning]], KL Divergence is often included as an extra term in the loss function <a class="yt-timestamp" data-t="10:00">10:00</a>. For instance, in the DeepSeek R1 paper, the optimization objective GRPO includes a `dkl` term with a hyperparameter `beta` <a class="yt-timestamp" data-t="03:52">03:52</a>. Similarly, Kim K 1.5 also uses a KL term between `Pi Theta` and `Pi Theta I` <a class="yt-timestamp" data-t="04:21">04:21</a>. `Pi Theta` represents a neural network with `Theta` as its parameters <a class="yt-timestamp" data-t="04:47">04:47</a>. This regularization ensures that the updated policy (neural network) does not diverge excessively from a previous or reference policy <a class="yt-timestamp" data-t="10:40">10:40</a>.

It is also observed in autoencoding variational Bayes, as seen in the work of Kingma <a class="yt-timestamp" data-t="05:05">05:05</a>.

## Origins of KL Divergence

The term KL Divergence comes from the researchers Kullback and Leibler, who introduced it in their 1951 paper "On Information and Sufficiency" <a class="yt-timestamp" data-t="11:24">11:24</a>, <a class="yt-timestamp" data-t="11:30">11:30</a>. They referred to it as "the information in X for discrimination between H1 and H2" <a class="yt-timestamp" data-t="11:48">11:48</a>. Both Kullback and Leibler were code-breakers who worked at the NSA after World War II, connecting to the early roots of information theory in military intelligence and code-cracking <a class="yt-timestamp" data-t="12:21">12:21</a>.

Using the name "relative entropy" is preferred as it helps in understanding the concept's origins in information theory and entropy, unlike the vanity naming of "KL Divergence" <a class="yt-timestamp" data-t="16:06">16:06</a>, <a class="yt-timestamp" data-t="16:29">16:29</a>.

## Relationship to Entropy and Cross-Entropy

[[relative_entropy_and_KL_divergence | Relative entropy]] is directly related to entropy and cross-entropy. The KL Divergence between two distributions P and Q is mathematically defined as:
`DKL(P||Q) = H(P, Q) - H(P)` <a class="yt-timestamp" data-t="16:38">16:38</a>
Where:
*   `H(P, Q)` is the cross-entropy of P and Q.
*   `H(P)` is the entropy of P.

### Types of Entropy

The term "entropy" is overloaded, referring to several concepts <a class="yt-timestamp" data-t="17:02">17:02</a>:
1.  **Thermodynamic entropy**
2.  **Entropy in classical statistical mechanics** (Boltzmann's H-theorem) <a class="yt-timestamp" data-t="23:54">23:54</a>
3.  **Entropy in quantum statistical mechanics**
4.  **Entropy in information theory** (Shannon entropy) <a class="yt-timestamp" data-t="17:36">17:36</a>
5.  **Algorithmic entropy**

The entropy relevant to [[relative_entropy_and_KL_divergence | relative entropy]] in machine learning is **Shannon entropy** <a class="yt-timestamp" data-t="17:36">17:36</a>, given by the formula `H = -sum(Pi * log(Pi))` <a class="yt-timestamp" data-t="17:38">17:38</a>. Claude Shannon developed this concept, reportedly advised by John Von Neumann to use the term "entropy" due to its similarity to physics concepts and Boltzmann's use of 'H' <a class="yt-timestamp" data-t="18:06">18:06</a>.

### Understanding Information-Theoretic Entropy

Entropy in information theory measures the **uncertainty** or "expected excess surprise" of a probabilistic system <a class="yt-timestamp" data-t="21:07">21:07</a>, <a class="yt-timestamp" data-t="21:10">21:10</a>.

*   **Fair Coin Flip (Uniform Probability):** A coin with a 50/50 chance of heads or tails yields maximum uncertainty and therefore maximum entropy (e.g., entropy = 1) <a class="yt-timestamp" data-t="20:12">20:12</a>.
*   **Biased Coin Flip (Non-Uniform Probability):** A coin with, for example, a 70% chance of heads and 30% chance of tails, yields less uncertainty and therefore less entropy (e.g., entropy = 0.88) <a class="yt-timestamp" data-t="20:22">20:22</a>.

### Algorithmic Entropy and Efficient Encoding

Algorithmic entropy defines the entropy of a string of symbols as the length of the shortest computer program that prints it out <a class="yt-timestamp" data-t="21:52">21:52</a>. This concept underpins efficient data encoding:
*   If all symbols have equal probability, using the same number of bits to encode each is efficient <a class="yt-timestamp" data-t="22:53">22:53</a>.
*   If some symbols are more frequent (higher probability), using fewer bits to encode them and more bits for less frequent ones results in a smaller overall message size <a class="yt-timestamp" data-t="23:03">23:03</a>. This implies that "more frequent equals less bits" <a class="yt-timestamp" data-t="23:48">23:48</a>. This idea is crucial for compression and communication efficiency, stemming from early code-breaking efforts <a class="yt-timestamp" data-t="22:16">22:16</a>.

## Probability Distributions in Machine Learning Models

In machine learning, probability distributions are often represented as **array-like structures** or tensors <a class="yt-timestamp" data-t="31:13">31:13</a>, where each element corresponds to the probability of a specific outcome <a class="yt-timestamp" data-t="31:53">31:53</a>. For example, a binomial distribution with three possible values (0, 1, 2) can be represented by an array containing the probabilities for each value <a class="yt-timestamp" data-t="31:26">31:26</a>.

Large language models (LLMs) output a **probability distribution over all possible tokens** in their vocabulary <a class="yt-timestamp" data-t="41:01">41:01</a>. This vocabulary can be vast (e.g., 100,000 tokens), meaning many tokens will have extremely low probabilities <a class="yt-timestamp" data-t="41:26">41:26</a>.

## Numerical Stability and Log Probabilities

Calculating KL Divergence directly from probabilities can lead to numerical stability issues <a class="yt-timestamp" data-t="38:33">38:33</a>:
*   **Division by zero:** Occurs if `Q(x)` is zero <a class="yt-timestamp" data-t="38:40">38:40</a>.
*   **Logarithm of zero/negative infinity:** Occurs if `P(x)` is zero <a class="yt-timestamp" data-t="38:47">38:47</a>.
*   **Overflow/Underflow:** KL Divergence can become very large or very small if the difference between `P(x)` and `Q(x)` is significant, especially with low-precision data types like float16 <a class="yt-timestamp" data-t="39:00">39:00</a>.

To mitigate these issues, machine learning implementations often work in **logarithmic scale** (log-probabilities) <a class="yt-timestamp" data-t="43:01">43:01</a>. Logs convert multiplication to addition (`log(x*y) = log(x) + log(y)`) and division to subtraction (`log(x/y) = log(x) - log(y)`) <a class="yt-timestamp" data-t="42:42">42:42</a>, <a class="yt-timestamp" data-t="43:19">43:19</a>. This transformation makes computations more numerically stable because the log function "smooths out" very large or very small numbers, preventing them from exceeding the representable range of floating-point data types <a class="yt-timestamp" data-t="44:36">44:36</a>, <a class="yt-timestamp" data-t="44:50">44:50</a>.

### Implementation Details in ML Frameworks

*   **Jax:** The `jax.scipy.stats.entropy.kl_div` function often calls `jax.scipy.stats.entropy.relative_entropy` internally <a class="yt-timestamp" data-t="33:38">33:38</a>. It includes checks to ensure valid input (e.g., P and Q are positive) and handles cases where P or Q might be zero by replacing values to avoid `divide by zero` or `log of zero` errors <a class="yt-timestamp" data-t="34:12">34:12</a>. The core calculation eventually maps to low-level Cuda or CPU implementations of the log function, often based on series expansions for approximation <a class="yt-timestamp" data-t="45:40">45:40</a>.
*   **PyTorch:** PyTorch provides `nn.functional.kl_div` and `nn.KLDivLoss` <a class="yt-timestamp" data-t="51:53">51:53</a>. Its implementation can take inputs that are already in log-probability space (`log_target` parameter) to avoid redundant log computations <a class="yt-timestamp" data-t="53:35">53:35</a>. PyTorch also has a more complex `torch.distributions.kl.kl_divergence` that dynamically selects a specific KL Divergence implementation based on the type of probability distributions (e.g., Bernoulli, Categorical, Gaussian) passed as arguments <a class="yt-timestamp" data-t="54:30">54:30</a>.
*   **Tinygrad:** Notably, Tinygrad, a lightweight machine learning framework, does not explicitly implement KL Divergence or [[relative_entropy_and_KL_divergence | relative entropy]] <a class="yt-timestamp" data-t="01:00:10">01:00:10</a>. This is because minimizing cross-entropy is "essentially the same as minimizing KL Divergence plus some constant" <a class="yt-timestamp" data-t="01:01:53">01:01:53</a>. Given Tinygrad's obsession with minimizing lines of code <a class="yt-timestamp" data-t="01:03:04">01:03:04</a>, it leverages this mathematical equivalence, allowing users to achieve similar regularization effects using cross-entropy, thus avoiding a separate implementation <a class="yt-timestamp" data-t="01:04:02">01:04:02</a>.

## Probability Flow Ordinary Differential Equations

(No information in the transcript to cover this topic)

## Continuous and Discrete Data in Generative Models

KL Divergence applies to both [[Continuous and Discrete Data in Generative Models | discrete and continuous probability distributions]] <a class="yt-timestamp" data-t="07:37">07:37</a>. For discrete distributions, the calculation involves a sum over possible outcomes <a class="yt-timestamp" data-t="07:39">07:39</a>. For continuous distributions, the sum is replaced by an integral <a class="yt-timestamp" data-t="07:50">07:50</a>. When dealing with complex or high-dimensional distributions (like those in large language models), exact analytical computation of KL Divergence is often infeasible due to computational intensity or lack of a closed-form expression <a class="yt-timestamp" data-t="36:07">36:07</a>. In such cases, **Monte Carlo estimation** is used to approximate the sum or integral by sampling from the distributions <a class="yt-timestamp" data-t="36:23">36:23</a>.

## Implications of Models Reasoning in Latent Space

(No information in the transcript to cover this topic)

## Bayesian Statistics and Machine Learning

(No information in the transcript to cover this topic)

## Parallelism and Scalability in Machine Learning

(No information in the transcript to cover this topic)

## Performance and Efficiency in Machine Learning Models

(No information in the transcript to cover this topic)

## Optimization Methods in Machine Learning

(Covered under Numerical Stability and Log Probabilities, and the general use of KL Divergence as a regularizer in RL)

## Quantization and Optimization in Machine Learning

(Covered under Numerical Stability and Log Probabilities)