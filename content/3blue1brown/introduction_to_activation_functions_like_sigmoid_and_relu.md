---
title: Introduction to activation functions like sigmoid and ReLU
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

In the context of [[structure_and_function_of_a_neural_network | neural networks]], an activation function determines the "activation" of a neuron, which is a number typically between 0 and 1 <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This activation can represent various things, such as the grayscale value of a pixel (0 for black, 1 for white) in an input layer <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>, or how much the system believes an image corresponds to a given digit in an output layer <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. When a neuron's activation is a high number, it can be visualized as being "lit up" <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

The activations in one layer of a [[structure_and_function_of_a_neural_network | neural network]] determine the activations of the next layer <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. This process involves calculating a weighted sum of the activations from the previous layer, to which a bias is added <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>. This resulting sum is then fed into an activation function to produce the neuron's activation, typically constrained within a range like 0 to 1 <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. The entire [[structure_and_function_of_a_neural_network | network]] itself functions as a complex mathematical function that takes input numbers and produces output numbers <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## Sigmoid Function

The sigmoid function, also known as a logistic curve, is a common function used to "squish" the real number line into the range between 0 and 1 <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.
*   **Behavior**: Very negative inputs to the sigmoid function result in activations close to 0, while positive inputs result in activations close to 1 <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>. It steadily increases around an input of 0 <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>.
*   **Historical Context**: Early [[structure_and_function_of_a_neural_network | neural networks]] utilized the sigmoid function to map weighted sums to the 0-1 interval, drawing motivation from the biological analogy of neurons being either inactive or active <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **Modern Use**: Relatively few modern [[structure_and_function_of_a_neural_network | neural networks]] continue to use the sigmoid function, as it has become "old school" <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. It proved difficult to train at some point <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.

## Rectified Linear Unit (ReLU)

ReLU stands for Rectified Linear Unit <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>.
*   **Behavior**: It is defined as `max(0, a)`, where 'a' is the weighted sum plus bias from the previous layer <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>. This means if the input 'a' is negative, the output is 0; otherwise, the output is 'a' <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.
*   **Motivation**: This function is partially motivated by a biological analogy, representing neurons either being activated or not, serving as a simplification <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.
*   **Advantage**: ReLU is significantly easier to train than sigmoid and has proven very effective for incredibly deep [[structure_and_function_of_a_neural_network | neural networks]] <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>.