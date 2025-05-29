---
title: Activation functions in neural networks
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

## Introduction
In the context of [[Structure of neural networks|neural networks]], activation functions play a crucial role in determining how information is processed and passed from one layer to the next <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. They enable the network to capture complex, non-linear relationships within data <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>.

## Activations
An "activation" is the specific number held by a neuron, typically ranging between 0 and 1 <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>, <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>, <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This value represents the neuron's "activity" or "intensity" <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. Visually, a neuron is "lit up" when its activation is a high number <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

The activations in one layer of a [[Structure of neural networks|neural network]] determine the activations of the subsequent layer <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. This process involves:
1.  Calculating a weighted sum of the activations from the previous layer, using specific [[Adjusting weights and biases in neural networks|weights]] associated with each connection <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>, <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.
2.  Adding a "bias" value to this weighted sum. The bias indicates how high the weighted sum needs to be before the neuron becomes meaningfully active <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>, <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.
3.  Passing the result through an activation function, which "squishes" the number into the desired range (e.g., between 0 and 1) for the neuron's activation <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

In essence, each neuron can be thought of as a function that takes the outputs of all neurons in the previous layer and produces a single activation number between 0 and 1 <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>, <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

## Common Activation Functions

### Sigmoid Function
The sigmoid function, also known as the logistic curve <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>, was historically a common choice for activation in early [[Neural Networks and Transformers|neural networks]] <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **Purpose**: It "squishes" any real number input into a range between 0 and 1 <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>, <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **Behavior**:
    *   Very negative inputs result in outputs close to 0 <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.
    *   Very positive inputs result in outputs close to 1 <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
    *   It steadily increases around an input of 0 <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
*   **Motivation**: Its use was partly motivated by a biological analogy, representing neurons as either inactive or active <a class="yt-timestamp" data-t="17:23:00">[17:23:00]</a>, <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>.
*   **Current Status**: Sigmoid functions are considered "old school" <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>, and relatively few modern networks use them because they were difficult to train <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>, <a class="yt-timestamp" data-t="18:15:00">[18:15:00]</a>.

### Rectified Linear Unit (ReLU)
ReLU, or Rectified Linear Unit, is a more commonly used activation function in modern [[Neural Networks and Transformers|neural networks]] <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>, <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.
*   **Function**: It is defined as `max(0, a)`, where `a` is the weighted sum plus bias from the previous layer <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>, <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. This means if the input is negative, the output is 0; otherwise, the output is equal to the input.
*   **Motivation**: Similar to sigmoid, ReLU was partly motivated by a biological analogy, where a neuron is either activated or not, acting as an identity function if it passes a certain threshold, and zero otherwise <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>, <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.
*   **Advantage**: ReLU is much easier to train than sigmoid, especially for incredibly deep [[Neural Networks and Transformers|neural networks]] <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>, <a class="yt-timestamp" data-t="18:15:00">[18:15:00]</a>, <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.