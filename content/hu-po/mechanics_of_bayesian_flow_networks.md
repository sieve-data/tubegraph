---
title: Mechanics of Bayesian Flow Networks
videoId: VLrqFH1Xtrs
---

From: [[hu-po]] <br/> 

Bayesian Flow Networks (BFNs) are a novel class of generative models introduced by computer scientist Alex Graves, known for his work on Neural Turing Machines and LSTMs [00:01:50]. Graves' history of finding new and intuitive approaches to machine learning has garnered attention for BFNs [00:02:06]. These models are designed to generate new samples from a distribution [00:02:23].

## Core Mechanics

At its heart, a BFN operates by iteratively updating the parameters of independent distributions using [[Bayesian Statistics and Applications in Machine Learning | Bayesian inference]] in the presence of noisy data samples [00:02:51]. These updated parameters are then fed into a neural network, which outputs a second, interdependent distribution [00:03:00]. This process begins with a simple prior distribution, such as a Gaussian or a uniform categorical distribution [00:03:18].

The iterative updating procedure yields a generative process conceptually similar to the reverse process in a [[Diffusion Models and ControlNet | diffusion model]], where noise is added and removed to learn data structure [00:03:40, 00:03:52, 00:04:00]. However, BFNs are claimed to be conceptually simpler as they do not require a forward process [00:04:18].

### Data Representation and Loss

BFNs utilize discrete and continuous time loss functions for continuous and discretized data [00:04:25]. Notably, for discrete data, the network inputs reside on the probability simplex, which is a mathematical space where each point represents a probability distribution over a finite number of mutually exclusive events [00:04:56, 00:05:11, 00:55:53]. This property makes them natively differentiable, enabling gradient-based sample guidance and few-step generation in discrete domains like language modeling [00:06:48, 00:07:07, 00:07:21].

The loss function in BFNs directly optimizes data compression [00:08:05, 00:16:30]. This aligns with the idea that generalization and intelligence can be viewed as compression [00:08:23, 00:19:52, 00:31:27].

### The Alice and Bob Metaphor

The paper employs an "Alice and Bob" metaphor to explain the data transmission process within BFNs [00:15:05]:
*   **Bob** starts with an input distribution (his belief or prior) [00:03:18, 00:57:02].
*   At each step, Bob feeds the parameters of his input distribution (e.g., mean and variance for a normal distribution, or probabilities for a categorical distribution) into a neural network [00:03:51, 00:38:47].
*   The network outputs the parameters of a "second interdependent distribution," referred to as the output distribution [00:03:00, 00:39:15].
*   **Alice** (representing the true data distribution) creates a "sender distribution" by adding noise to the actual data, following a predefined schedule [00:39:53, 00:40:00].
*   Bob creates a "receiver distribution" by convolving his output distribution with the same noise distribution used by Alice [00:40:04].
*   The "transmission cost" at each step is measured by the KL Divergence between Bob's receiver distribution and Alice's sender distribution [00:22:28, 00:40:59]. Minimizing the sum of these KL divergences aims to minimize the evidence lower bound [00:23:37, 00:29:57].
*   Alice sends a sample from the sender distribution to Bob [00:40:57].
*   Bob uses this sample to update his input distribution, following [[Bayesian Statistics and Applications in Machine Learning | Bayesian inference]] rules [00:41:06, 01:10:09]. These Bayesian updates are available in a closed form if variables are modeled independently [01:11:15].
*   This process repeats for `n` steps, by which point Bob's model can predict the data accurately enough [00:41:33].

### Key Differences from Diffusion Models

BFNs differ from [[Diffusion Models and ControlNet | diffusion models]] in several crucial aspects:
*   **Operation on Parameters**: BFNs operate on the *parameters* of a data distribution rather than directly on a noisy version of the data itself [00:36:44]. This ensures the generative process is fully continuous and differentiable, even with discrete data [00:37:41].
*   **No Forward Process**: Unlike [[Diffusion Models and ControlNet | diffusion models]], BFNs do not require defining and inverting a forward process [01:02:44]. This is claimed to make them easier to adapt to different distributions and data types [01:02:51].
*   **Initial State**: The generative process of BFNs begins with the parameters of a fixed prior, whereas [[Diffusion Models and ControlNet | diffusion models]] typically start with pure noise [01:01:36]. This reduction in initial noise could lead to faster learning on large datasets [01:02:03].

### Neural Network's Role

The neural network in a BFN is critical for integrating contextual information [01:13:30]. While the Bayesian updates on the input distribution handle information about each variable independently, the neural network (denoted as PSI) jointly processes all parameters in the input distribution [01:10:03, 01:13:27]. This gives the network access to the full available context, allowing it to exploit relationships between variables, such as neighboring pixels in an image or related words in text [00:47:31, 01:14:05]. This combination of independent Bayesian inference and holistic deep learning leverages the strengths of both approaches [00:48:04].

## Continuous Time Loss

The `n`-step transmission process and its loss function can be generalized to continuous time by allowing `n` to approach infinity [00:49:44]. In continuous time, the Bayesian updates become a "Bayesian flow" of information from the data to the network [00:50:00, 01:36:00]. This removes the need to predefine the number of steps during training and results in a mathematically simpler and easier-to-compute loss function [00:50:21, 01:48:40]. A BFN trained with continuous time loss can be run for any number of discrete steps during inference, with performance improving as the number of steps increases [00:50:35].

An "accuracy parameter" called Alpha (`α`), which is a function of time (`t`), defines the accuracy rate at time `t` [01:08:45, 01:30:00]. This Alpha is linked to an "accuracy schedule" (Beta `β(t)`), which is a monotonically increasing function over time, where its derivative is Alpha [01:30:34]. For continuous data, this schedule is related to the standard deviation of the input distribution, reflecting how confidence in the distribution changes over time [01:32:00].

## Experimental Results

BFNs were tested on standard machine learning datasets:
*   **MNIST and CIFAR-10**: For image modeling, BFNs achieved competitive log-likelihoods on dynamically binarized MNIST and CIFAR-10 [00:09:11, 02:40:34]. The experiments did not use data augmentation, which is a common practice for these tasks, yet still achieved competitive results [02:43:04].
*   **Text8 Character Level Language Modeling**: BFNs outperformed all known discrete [[Diffusion Models and ControlNet | diffusion models]] on the Text8 character-level language modeling task [00:10:41, 02:50:36]. This task involves predicting the next character in a large corpus, typically the English Wikipedia [01:12:05]. The Text8 task, however, is a significantly simplified version of modern language modeling, often using a small vocabulary (e.g., 27 possible tokens) compared to the thousands of tokens in current large language models [02:40:40, 02:41:04].

The visualizations demonstrate how BFNs iteratively refine their probabilistic estimations:
*   **Continuous Data Bayesian Update**: Figures illustrate how an initial wide Gaussian prior (low confidence) shifts its mean and narrows its variance (increases confidence) as more data samples are observed, guided by the Alpha accuracy parameter [01:56:22, 02:04:09].
*   **Continuous Data Bayesian Flow**: Trajectories of the input distribution's mean over time show how they converge from an initial wide spread towards the true data value, suggesting a robust optimization process [02:05:45, 02:09:16].
*   **Discrete Data Probability Simplex**: For discrete categorical data (e.g., 3 possible tokens), the network's probabilistic guess is visualized as a point on a probability simplex (a triangle for 3 categories). Over time, this point's trajectory moves towards the corner representing the true token, showing the model's increasing certainty [02:35:36, 02:37:34].

While BFNs present a mathematically elegant and theoretically promising framework, the complexity and scaling behavior for high-dimensional data (like large images or vast language vocabularies) remain to be fully explored and demonstrated [01:14:49, 02:32:16, 02:55:08].