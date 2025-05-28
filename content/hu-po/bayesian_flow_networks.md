---
title: Bayesian Flow Networks
videoId: VLrqFH1Xtrs
---

From: [[hu-po]] <br/> 

Bayesian Flow Networks (BFNs) represent a new class of [[generative_models | generative models]] designed to generate new samples from a distribution <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. This approach is conceptually simpler than other methods as it does not require a forward process <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. BFNs differ from traditional [[diffusion_models | diffusion models]] by operating on the parameters of a data distribution rather than directly on a noisy version of the data itself <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Origin and Creator

The popularity of Bayesian Flow Networks stems from its creator, Alex Graves <a class="yt-timestamp" data-t="00:47:47">[00:47:47]</a>. Graves is a computer scientist known for pioneering [[neural_networks | neural networks]] and [[differentiable_turing_computer | differentiable Turing computer]] <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>, as well as the Long Short-Term Memory (LSTM) network <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>. His work is characterized by finding new and intuitive ways to approach machine learning <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

## Core Concepts

### Generative Process and Distributions
BFNs are generative models that generate samples from a distribution <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>. The parameters of a set of independent distributions, such as the mean and variance of a normal distribution, are modified using [[bayesian_statistics_and_machine_learning | Bayesian inference]] in light of noisy data samples <a class="yt-timestamp" data-t="02:51:51">[02:51:51]</a>. These modified parameters are then fed as input to a [[neural_networks | neural network]] that outputs a second interdependent distribution <a class="yt-timestamp" data-t="03:02:02">[03:02:02]</a>.

The process begins with a simple prior distribution, often a Gaussian <a class="yt-timestamp" data-t="03:03:03">[03:03:03]</a>. Iteratively updating two distributions—an input distribution (Bob's guess) and an output distribution (informed by the neural network)—yields a generative procedure <a class="yt-timestamp" data-t="03:03:03">[03:03:03]</a>. This is similar to the reverse process of [[diffusion_models | diffusion models]], where noise is added and removed to learn the data's structure <a class="yt-timestamp" data-t="03:48:48">[03:48:48]</a>.

### Bayesian Inference and Message Exchange
BFNs operate using a "transmission metaphor" involving Alice (the data source/nature) and Bob (the model trying to learn the distribution) <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

*   **Alice** represents the true data distribution and sends messages (noisy data samples) to Bob <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Bob** starts with a simple "prior" belief about the distribution, which is uninformed initially <a class="yt-timestamp" data-t="00:16:57">[00:16:57]</a>. He receives messages and uses this information to improve his guess <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.

The "transmission cost" at each step is measured by the [[kl_divergence_and_bayesian_inference | KL Divergence]] between Alice's true (sender) distribution and Bob's predicted (receiver) distribution <a class="yt-timestamp" data-t="02:22:31">[02:22:31]</a>. The sum of these KL divergences forms the evidence lower bound (ELBO), which is maximized during training to approximate the true posterior distribution <a class="yt-timestamp" data-t="02:34:44">[02:34:44]</a>.

#### Variational Inference
[[kl_divergence_and_bayesian_inference | Variational inference]] is key to BFNs, transforming the problem of computing intractable posterior distributions into an optimization problem <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. Instead of directly calculating the true posterior, BFNs propose a family of simpler, tractable distributions (Q) and minimize the [[kl_divergence_and_bayesian_inference | KL Divergence]] between Q and the true posterior <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>. This allows for gradient-based optimization <a class="yt-timestamp" data-t="02:29:29">[02:29:29]</a>.

### Loss Function and Data Compression
The loss function in BFNs directly optimizes data compression <a class="yt-timestamp" data-t="08:05:05">[08:05:05]</a>. This aligns with the idea that generalization and intelligence can be viewed as compression <a class="yt-timestamp" data-t="02:23:23">[02:23:23]</a>. The total number of bits required for all messages (data transmission) serves as the loss <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>.

### Probability Simplex
For discrete data, the network inputs lie on the [[concepts_of_probability_distributions_in_ml | probability simplex]] <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. A [[concepts_of_probability_distributions_in_ml | probability simplex]] is a mathematical space where each point represents a probability distribution between a finite number of mutually exclusive events <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This ensures that the inputs are continuous and naturally differentiable, enabling gradient-based sample guidance <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Continuous and Discrete Time
BFNs are derived with both discrete and continuous time loss functions <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. By allowing the number of steps ($N$) to approach infinity, the discrete time process generalizes to [[probability_flow_ordinary_differential_equations | continuous time]], where Bayesian updates become a "Bayesian flow" of information <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>. This continuous time loss function is mathematically simpler and removes the need to predefine the number of steps during training <a class="yt-timestamp" data-t="00:50:24">[00:50:24]</a>.

## Components of a Bayesian Flow Network

### Input and Output Distributions
*   **Input Distribution ($P_i$)**: Represents Bob's current belief about the data distribution, initially a simple prior (e.g., standard normal for continuous data, uniform categorical for discrete data) <a class="yt-timestamp" data-t="03:51:51">[03:51:51]</a>. Its parameters are updated independently for each variable through Bayesian inference <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>.
*   **Output Distribution ($P_o$)**: Produced by a [[neural_networks | neural network]] that takes the parameters of the input distribution and the process time ($t$) as input <a class="yt-timestamp" data-t="01:09:24">[01:09:24]</a>. This network processes all parameters jointly, allowing it to exploit contextual information across variables (e.g., neighboring pixels in an image, related words in text) <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>.

### Sender and Receiver Distributions
*   **Sender Distribution ($P_s$)**: Created by Alice (the data source) by adding noise to the true data according to a predefined schedule <a class="yt-timestamp" data-t="03:53:53">[03:53:53]</a>. It's effectively the true data distribution with noise <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.
*   **Receiver Distribution ($P_r$)**: Created by Bob by convolving the output distribution with the same noise distribution used by Alice <a class="yt-timestamp" data-t="04:04:04">[04:04:04]</a>.

The loss function is the [[kl_divergence_and_bayesian_inference | KL Divergence]] between the receiver and sender distributions <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. As training progresses, Bob's receiver distribution aims to get as close as possible to Alice's sender distribution <a class="yt-timestamp" data-t="04:15:15">[04:15:15]</a>.

### Bayesian Updates and Accuracy Schedule
The input distribution's parameters (Theta, e.g., mean and variance of a Gaussian or probabilities of a categorical distribution) are updated iteratively <a class="yt-timestamp" data-t="02:59:59">[02:59:59]</a>. This update follows [[bayesian_statistics_and_machine_learning | Bayesian inference]] rules, which are available in a closed form when variables are modeled independently <a class="yt-timestamp" data-t="04:12:12">[04:12:12]</a>.

An **accuracy parameter (Alpha)**, which functions as a schedule, is used to control how much influence each sampled data point has on the parameter updates <a class="yt-timestamp" data-t="01:08:19">[01:08:19]</a>. A higher Alpha means more confidence in the sample, leading to more dramatic shifts in the distribution's parameters <a class="yt-timestamp" data-t="02:04:20">[02:04:20]</a>. This is analogous to a noise schedule in [[diffusion_models | diffusion models]] <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

## How BFNs Work (Simplified)

1.  **Initialize**: Bob starts with an input distribution (a prior, e.g., a simple Gaussian or uniform categorical distribution) <a class="yt-timestamp" data-t="03:51:51">[03:51:51]</a>.
2.  **Neural Network Prediction**: Bob feeds the parameters of this input distribution to a [[neural_networks | neural network]] (along with time $t$) to get an output distribution <a class="yt-timestamp" data-t="03:51:51">[03:51:51]</a>.
3.  **Noisy Data and Receiver**: Alice provides a noisy data sample (sender distribution) <a class="yt-timestamp" data-t="03:54:54">[03:54:54]</a>. Bob creates a receiver distribution by convolving his output distribution with the same noise <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>.
4.  **Calculate Loss**: The [[kl_divergence_and_bayesian_inference | KL Divergence]] between the receiver and sender distributions is calculated as the loss <a class="yt-timestamp" data-t="04:01:01">[04:01:01]</a>.
5.  **Bayesian Update**: Bob uses the sampled data and [[bayesian_statistics_and_machine_learning | Bayesian inference]] rules to update his input distribution, making it a better guess <a class="yt-timestamp" data-t="04:06:06">[04:06:06]</a>.
6.  **Iterate**: This process repeats for multiple steps, refining Bob's input distribution <a class="yt-timestamp" data-t="04:31:31">[04:31:31]</a>. Over time, the input distribution converges towards the true data distribution <a class="yt-timestamp" data-t="02:06:24">[02:06:24]</a>.

## Advantages and Differences from Other Models

*   **Continuous and Differentiable**: BFNs ensure the generative process is fully continuous and differentiable, even for discrete data <a class="yt-timestamp" data-t="04:41:41">[04:41:41]</a>. This is a key difference from [[discrete_diffusion_models | discrete diffusion models]] which inherently use discrete samples as input <a class="yt-timestamp" data-t="00:55:02">[00:55:02]</a>.
*   **No Forward Process**: Unlike [[diffusion_models | diffusion models]], BFNs do not require defining and inverting a forward process <a class="yt-timestamp" data-t="01:02:44">[01:02:44]</a>. This makes them easier to adapt to different distributions and data types <a class="yt-timestamp" data-t="01:02:51">[01:02:51]</a>.
*   **Direct Optimization**: BFNs directly optimize the negative log-likelihood of discrete data <a class="yt-timestamp" data-t="00:59:33">[00:59:33]</a>.
*   **Reduced Noise**: The [[neural_networks | neural network]] inputs in BFNs are considerably less noisy compared to [[variational_diffusion_models | variational diffusion models]] because BFNs begin with parameters of a fixed prior, not pure noise <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.
*   **Division of Labor**: BFNs leverage a division of labor where [[bayesian_statistics_and_machine_learning | Bayesian inference]] optimally collects and summarizes information about individual variables, while [[deep_learning | deep learning]] (the neural network) integrates information across many interrelated variables (context) <a class="yt-timestamp" data-t="01:08:05">[01:08:05]</a>.

## Illustrative Figures and Examples (as described in transcript)

*   **Bayesian Update for Continuous Data (Figure 2)**: Shows how an initial wide Gaussian prior (black line) becomes narrower and shifts its mean (red, blue, green lines) as more data samples (red, blue, green X's) are observed <a class="yt-timestamp" data-t="01:56:24">[01:56:24]</a>. The "accuracy" (Alpha) of these samples influences how quickly the distribution adapts <a class="yt-timestamp" data-t="02:03:30">[02:03:30]</a>.
*   **Bayesian Flow for Continuous Data (Figure 4)**: Depicts the trajectories of the input distribution's mean over time. Starting from zero, these trajectories "fan out" and then converge towards the true data point (e.g., X=0.8), illustrating the optimization process <a class="yt-timestamp" data-t="02:05:36">[02:05:36]</a>.
*   **Input Variance (Figure 5)**: Compares the variance schedule of BFNs (blue line) to noise schedules in [[diffusion_models | diffusion models]] (red/green lines) <a class="yt-timestamp" data-t="02:10:24">[02:10:24]</a>. BFNs start with zero variance (deterministic prior) and briefly increase uncertainty before converging to very low variance, reflecting increasing confidence in the parameter estimates <a class="yt-timestamp" data-t="02:16:19">[02:16:19]</a>.
*   **Output Distribution for Discretized Data (Figure 7)**: Shows how a continuous Gaussian distribution is discretized into bins for discrete data <a class="yt-timestamp" data-t="02:19:29">[02:19:29]</a>. Probability mass outside bin boundaries is "clipped" and added to the nearest boundary bins <a class="yt-timestamp" data-t="02:21:51">[02:21:51]</a>.
*   **Sender, Output, Receiver for Discretized Data (Figure 8)**: Compares the true sender distribution (red), the discretized output distribution (green bars), and the receiver distribution (blue line) for discrete data <a class="yt-timestamp" data-t="02:22:47">[02:22:47]</a>. Discretization can lead to a lower [[kl_divergence_and_bayesian_inference | KL Divergence]] between the receiver and sender <a class="yt-timestamp" data-t="02:27:09">[02:27:09]</a>.
*   **Bayesian Flow for Discrete Data (Figure 11)**: Visualizes the parameter trajectories on a [[concepts_of_probability_distributions_in_ml | probability simplex]] for data with three categories <a class="yt-timestamp" data-t="02:35:36">[02:35:36]</a>. The trajectories start from a uniform prior (center) and move towards the true data point (e.g., a corner of the triangle), demonstrating how the model learns to concentrate probability on the correct category <a class="yt-timestamp" data-t="02:36:22">[02:36:22]</a>.
*   **Generated Samples (MNIST, CIFAR-10)**: BFNs achieve competitive log-likelihoods for image modeling on dynamically binarized MNIST and CIFAR-10 datasets <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. While visually similar, the results are notable for being achieved without data augmentation, which is often crucial for training on these datasets <a class="yt-timestamp" data-t="02:43:02">[02:43:02]</a>.
*   **Text Diffusion (Figure 19, 20)**: BFNs outperform known [[discrete_diffusion_models | discrete diffusion models]] on the Text8 character-level language modeling task <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a>. This demonstrates their ability to model text by "diffusing" or refining a noisy initial text into the correct sequence of characters <a class="yt-timestamp" data-t="02:50:50">[02:50:50]</a>.

## Challenges and Limitations

Despite their theoretical elegance and competitive results on simplified benchmarks, BFNs face potential challenges, particularly in scalability <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>:

*   **High Dimensionality**: The current examples use low-dimensional data (e.g., 3 categories, 28x28 grayscale images, 27 possible text tokens) <a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a>. Scaling BFNs to higher-dimensional data, such as large images or vocabularies with thousands of tokens, could lead to significant GPU memory and computational limitations, potentially making them less practical than existing [[neural_networks | neural network]] architectures like Transformers <a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a>.
*   **Diagonal Covariance Assumption**: The assumption of diagonal covariance in continuous data models implies independent variables, which is often not true in real-world systems <a class="yt-timestamp" data-t="01:54:55">[01:54:55]</a>.
*   **Hyperparameter Tuning**: The choice of the accuracy schedule (beta or alpha) is a hyperparameter that requires careful selection, as an uneven schedule can negatively impact performance <a class="yt-timestamp" data-t="02:47:29">[02:47:29]</a>.
*   **Scaling Laws**: The behavior of these models at low data regimes might differ from medium or high data regimes, making it difficult to extrapolate performance to larger-scale problems without empirical testing <a class="yt-timestamp" data-t="02:55:08">[02:55:08]</a>.