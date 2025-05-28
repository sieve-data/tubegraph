---
title: Continuous and Discrete Data in Generative Models
videoId: VLrqFH1Xtrs
---

From: [[hu-po]] <br/> 

Generative models, which have revolutionized [[data_generation_for_ai_models | generative modeling]] in recent years, aim to capture complex relationships within variables to create new data [00:02:21]. A core aspect of these models, including auto-regressive models, flow-based models, deep variational autoencoders (VAEs), and [[generative_latent_spaces_in_ai | Diffusion Models]], involves breaking down joint distributions into a series of steps to manage the complexity of numerous interactions [00:13:36].

## Data Types in Generative Models

Generative models process different types of data, broadly categorized as continuous or discrete:

*   **Continuous Data** <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>: Data where values can fall anywhere within a continuous range, such as pixel intensities in an image [00:20:29]. In these domains, a natural ordering among variables often does not exist [00:20:31].
*   **Discrete Data** <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>: Data consisting of distinct, separate values, such as tokens in language modeling [00:20:11]. For discrete data, a natural ordering often exists (e.g., word order in a sentence) [00:10:46].

### Challenges with Discrete Data

A fundamental challenge arises when generative models, particularly those based on continuous processes like diffusion, encounter discrete data:
*   **Discontinuity** <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>: When data is discrete, the noise applied in a diffusion process is also discrete and therefore discontinuous [00:33:22].
*   **Differentiability** <a class="yt-timestamp" data-t="00:34:15">[00:34:15]</a>: Discontinuous functions are not inherently differentiable, which impedes the use of gradient-based optimization methods [00:34:15]. This is a significant hurdle for training neural networks.
*   **No Natural Order in Images** <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>: While auto-regressive models perform well on discrete data with a natural order, they are less effective for continuous data like images where no inherent pixel order exists [00:20:29].

## Bayesian Flow Networks (BFNs) Approach

Bayesian Flow Networks (BFNs) are a new class of [[generative_latent_spaces_in_ai | generative models]] proposed to address the challenges of handling both [[continuous_vs_discrete_latent_spaces_in_ai | continuous and discrete data]] [00:02:21]. BFNs are conceptually similar to [[generative_latent_spaces_in_ai | Diffusion Models]] in their iterative generative process, but with key differences [00:03:40]:

*   **Operation on Parameters** <a class="yt-timestamp" data-t="00:36:44">[00:36:44]</a>: Unlike diffusion models that operate on noisy versions of the data itself, BFNs operate on the *parameters* of a data distribution [00:36:47]. For example, instead of removing noise from an image, BFNs denoise the mean and variance parameters of a Gaussian distribution [00:37:01].
*   **Continuous and Differentiable Process** <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>: This approach ensures that the generative process in BFNs is fully continuous and differentiable, even when the underlying data is discrete [00:43:40]. This is achieved because the parameters of a discrete categorical distribution (e.g., probabilities for different tokens) are real-valued and thus continuous [00:54:17].
*   **Inherent Simplex Property** <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>: The network inputs for discrete data naturally lie on the [[continuous_vs_discrete_latent_spaces_in_ai | probability simplex]] by virtue of being parameters of a categorical distribution [00:55:50]. This removes the need for separate embedding spaces or constraints, simplifying the model [00:58:56].

### How BFNs Work

The core process of a BFN involves an iterative "transmission scheme" between a "sender" (Alice, representing the true data distribution) and a "receiver" (Bob, representing the model's evolving belief) [00:15:05]:

1.  **Input Distribution (Bob's Guess)** <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>: Bob starts with an input distribution, initially a simple prior (e.g., a standard normal for continuous data or a uniform categorical for discrete data) [00:37:51].
2.  **Neural Network Output** <a class="yt-timestamp" data-t="00:39:12">[00:39:12]</a>: Bob feeds the parameters of his input distribution (e.g., mean/variance or categorical probabilities) into a neural network [00:39:12]. This network outputs the parameters of a "second interdependent distribution," called the output distribution [00:03:02]. This neural network integrates information across all variables, exploiting contextual information (like neighboring pixels or related words) [00:47:31].
3.  **Sender Distribution (Alice's Message)** <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>: Alice creates a sender distribution by adding noise to the actual data according to a predefined schedule [00:39:52]. This noise schedule (represented by `Alpha` or `Beta`) dictates how informative the samples are over time [01:08:51].
4.  **Receiver Distribution** <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>: Bob creates a receiver distribution by convolving his output distribution with the same noisy distribution used by Alice [00:40:04].
5.  **Loss Function (KL Divergence)** <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>: The transmission cost at each step is measured by the Kullback-Leibler (KL) Divergence between the receiver and sender distributions [00:22:28]. This measures the "distance" or difference between Alice's true distribution (with noise) and Bob's current best guess [00:22:39]. Minimizing this KL Divergence means Bob's guess gets closer to Alice's reality [00:23:37].
6.  **Bayesian Update** <a class="yt-timestamp" data-t="00:41:06">[00:41:06]</a>: Bob then uses a sample from the sender distribution to update his input distribution, following the rules of Bayesian inference [00:41:06]. This step provides a mathematically optimal way to collect and summarize information about individual variables [00:48:11].
7.  **Iteration** <a class="yt-timestamp" data-t="00:41:31">[00:41:31]</a>: The process repeats for a number of steps (`n`), with Bob's predictions iteratively improving [00:41:31]. In theory, `n` can go to infinity to achieve a continuous time Bayesian flow [00:49:51].

> [!INFO] **Division of Labor**
> BFNs combine Bayesian inference and deep learning:
> *   **Bayesian inference** provides a mathematically optimal way to collect and summarize information about *individual variables* [00:48:11].
> *   **Deep learning** (the neural network) integrates information over *many interrelated variables* (context) [00:48:34].

### Continuous vs. Discrete Time Loss Functions

BFNs derive both discrete and continuous time loss functions [00:26:25]. While the discrete time loss sums KL divergences over `n` steps [01:39:48], the continuous time loss is mathematically simpler and theoretically removes the need to predefine the number of steps during training [01:46:47].

### Visualization of Bayesian Updates

For continuous data (e.g., a single variable `X=0.7`), the Bayesian update process can be visualized as iteratively refining a Gaussian distribution:
*   **Initial Guess** <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>: Starts with a broad Gaussian centered at zero [01:57:02].
*   **First Sample** <a class="yt-timestamp" data-t="01:57:22">[01:57:22]</a>: Upon observing `X=0.7`, the mean of the Gaussian shifts towards `0.7`, and its variance decreases, reflecting increased confidence [01:57:23].
*   **Subsequent Samples** <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>: With each new sample, the Gaussian continues to shift and narrow, approaching the true underlying data distribution [01:59:04].
*   **Impact of Accuracy (`Alpha`)** <a class="yt-timestamp" data-t="02:04:09">[02:04:09]</a>: The `Alpha` (accuracy) parameter acts like an importance weight for samples. A higher `Alpha` means the model quickly adapts its parameters to the new sample, becoming very confident and narrowing its variance significantly [02:04:09].

For discrete data (e.g., binary or categorical), the concept is similar. In a binary case (like a coin flip), the probability of "class 1" shifts from 0.5 towards 1 if the observed data consistently favors "class 1" [03:03:55]. This convergence implies that all trajectories (paths of the model's parameters) eventually lead to the true data distribution [02:09:24].

### Experimental Results

BFNs have been tested on standard datasets:
*   **Image Modeling (MNIST, CIFAR-10)** <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>: BFNs achieve competitive log-likelihoods [00:09:11]. Notably, they can generate realistic images from these datasets without [[synthetic_data_generation_in_ai_training | data augmentation]], which is often required for other models [02:43:04]. The network's ability to utilize context helps resolve ambiguity and noise in the input distribution [02:44:51].
*   **Language Modeling (Text8)** <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>: BFNs outperform known [[generative_latent_spaces_in_ai | discrete Diffusion Models]] on the Text8 character-level language modeling task [00:10:41]. This is demonstrated by showing how a garbled text gradually becomes coherent as the BFN iteratively refines its probabilities for each token, eventually converging to the actual text [02:51:19].

> [!CAUTION] **Limitations**
> The current experimental results for BFNs are primarily on relatively simple datasets (MNIST, CIFAR-10) and simplified language modeling tasks (Text8 with 27 possible tokens) [02:41:19]. It remains to be seen how well these models scale to much higher-dimensional data (e.g., high-resolution images) or larger vocabularies (e.g., hundreds of thousands of tokens for large language models), as the computational demands might increase significantly [01:14:49]. The scaling laws for such models are not yet fully understood [02:55:59].