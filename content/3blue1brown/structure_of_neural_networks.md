---
title: Structure of neural networks
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

[[Neural Networks and Transformers | Neural networks]] are computational models inspired by the human brain, designed to recognize patterns and perform complex tasks like handwritten digit recognition <a class="yt-timestamp" data-t="01:10:39">[01:10:39]</a>, <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. This article focuses on the fundamental structure of a basic, "plain vanilla" neural network <a class="yt-timestamp" data-t="02:14:55">[02:14:55]</a>.

## Core Concept: The Neuron

At its most basic, a neuron within a neural network is simply a component that holds a number, specifically a value between 0 and 1 <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>, <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This number is referred to as its "activation" <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. A higher activation value can be imagined as the neuron being "lit up" <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.

## Layered Architecture

Neural networks are organized into layers, with activations in one layer determining the activations of the next <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>, <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. This concept is loosely analogous to how groups of biological neurons firing can cause others to fire <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

### Input Layer
The first layer of a neural network corresponds to the input data. For handwritten digit recognition, using 28x28 pixel images, the input layer consists of 784 neurons (28 * 28) <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>, <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. Each of these neurons holds a number representing the grayscale value of a corresponding pixel, ranging from 0 (black) to 1 (white) <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

### Output Layer
The final layer of the network provides the output. For digit recognition, it contains 10 neurons, each representing one of the digits (0-9) <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>, <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. The activation of these neurons indicates how much the network believes the input image corresponds to a particular digit <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. The neuron with the brightest activation is the network's chosen digit <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

### Hidden Layers
Between the input and output layers are one or more "hidden layers" <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. The specific number and size of these layers are often arbitrary choices in practice, and there is significant room for experimentation <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>, <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

The hope for these [[role_of_hidden_layers_in_neural_networks | hidden layers]] is that they progressively learn to recognize hierarchical components of the input <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>:
*   The second layer might recognize small edges <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.
*   The third layer might combine these edges to recognize larger patterns like loops or long lines <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>, <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>.
*   The final output layer would then combine these patterns to identify the complete digit <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>, <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.

This layered abstraction is useful beyond image recognition, for tasks like parsing speech, which involves identifying sounds, syllables, words, and phrases <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## Weights and Biases

The transformation of activations from one layer to the next is governed by two types of parameters: weights and biases <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. These are the "dials and knobs" that define how the network processes information <a class="yt-timestamp" data-t="08:55:00">[08:55:00]</a>, <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.

*   **Weights**: Every connection between a neuron in one layer and a neuron in the next has an associated weight <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. To calculate the input to a neuron, the activations from the previous layer are multiplied by their respective weights, and then summed <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>. These weights determine what pixel pattern or feature a neuron is sensitive to <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. For example, specific positive weights in a region combined with negative weights in surrounding areas can help detect an edge <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
*   **Biases**: After computing the weighted sum of inputs, an additional number called the "bias" is added to it <a class="yt-timestamp" data-t="11:11:00">[11:11:11]</a>. The bias controls the threshold for a neuron to become active <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>. For instance, a bias of -10 might mean the weighted sum needs to exceed 10 before the neuron activates meaningfully <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.

In the example network for digit recognition with 784 input neurons, two hidden layers of 16 neurons each, and 10 output neurons, there are approximately 13,000 total weights and biases <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>, <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.

## [[Activation functions in neural networks | Activation Function]]

The weighted sum (plus bias) can be any real number, but neuron activations are desired to be between 0 and 1 <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. To achieve this, the sum is passed through an [[Activation functions in neural networks | activation function]] that "squishes" the real number line into the desired range <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

*   **Sigmoid Function**: Historically, the sigmoid function (also known as a logistic curve) was commonly used <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. This function maps very negative inputs close to 0, positive inputs close to 1, and increases steadily around 0 <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>. Its use was partly motivated by a biological analogy of neurons being either inactive or active <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>.
*   **ReLU (Rectified Linear Unit)**: In modern [[neural_network_learning_process | neural networks]], ReLU is much more common than sigmoid <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>, <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>. ReLU is defined as `max(0, a)`, where `a` is the weighted sum plus bias <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. It simplifies the activation to zero if it doesn't pass a certain threshold, otherwise acting as an identity function <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>. ReLU functions tend to be much easier to [[neural_network_learning_process | train]] <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>, <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>.

## Mathematical Representation

The computations within a layer can be expressed compactly using linear algebra:
1.  Activations from one layer are organized into a column vector <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.
2.  Weights connecting this layer to the next are organized into a matrix, where each row corresponds to the weights for a specific neuron in the next layer <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
3.  The weighted sum for all neurons in the next layer is computed by taking the matrix-vector product of the weight matrix and the activation vector <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.
4.  Biases for each neuron in the next layer are organized into a vector and added to the result of the matrix-vector product <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
5.  Finally, the [[Activation functions in neural networks | activation function]] (e.g., sigmoid or ReLU) is applied element-wise to each component of the resulting vector <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>.

This mathematical representation allows for efficient computation, as many libraries optimize matrix multiplication <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

## The Network as a Function

Ultimately, a neural network, with its many layers, neurons, weights, and biases, can be understood as an absurdly complicated function <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. It takes a set of input numbers (e.g., 784 pixel values) and produces a set of output numbers (e.g., 10 digit probabilities) <a class="yt-timestamp" data-t="15:43:00">[15:43:00]</a>.

The "[[neural_network_learning_process | learning]]" process in [[neural_network_learning_process | neural networks]] involves adjusting these thousands of weights and biases to enable the network to solve a specific problem, such as correctly recognizing handwritten digits <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>, <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>.