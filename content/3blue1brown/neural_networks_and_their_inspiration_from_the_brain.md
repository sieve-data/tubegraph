---
title: Neural networks and their inspiration from the brain
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

The human brain possesses an extraordinary ability to recognize patterns, such as a sloppily written digit "3", even when the specific pixel values vary greatly between instances <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This effortless recognition by the brain stands in stark contrast to the daunting difficulty of programming a computer to perform the same task, like identifying a digit from a 28x28 pixel grid <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>. [[structure_and_function_of_a_neural_network | Neural networks]], inspired by the brain's architecture, aim to address such complex recognition problems <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

The goal of understanding [[structure_and_function_of_a_neural_network | neural networks]] is to demystify them, moving beyond buzzwords to grasp their underlying mathematical principles and how they "learn" <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. This introduction focuses on the fundamental structure of a basic [[structure_and_function_of_a_neural_network | neural network]] designed to recognize handwritten digits, a classic example in the field <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

## Basic Components: Neurons and Layers

At its core, a [[structure_and_function_of_a_neural_network | neural network]] is composed of interconnected "neurons" organized into layers, loosely analogous to biological neurons <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

### Neurons

Each neuron is simply a unit that holds a number, specifically a value between 0 and 1 <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This number is called its **activation**, with higher numbers indicating a more "lit up" or active state <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. For input images, an activation of 0 represents a black pixel, and 1 represents a white pixel <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

### Layers

[[neural_network_structure_and_layers | Neural networks]] are structured in layers:

*   **Input Layer**: For a 28x28 pixel image, this layer consists of 784 neurons (28x28) <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. Each neuron's activation corresponds to the grayscale value of a specific pixel in the input image <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   **Output Layer**: This layer has 10 neurons, one for each digit (0 through 9) <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>. The activation of these neurons (again, between 0 and 1) indicates the system's confidence that the input image represents a particular digit <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. The brightest neuron in this layer represents the network's chosen digit <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
*   **Hidden Layers**: These are the layers situated between the input and output layers <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>. In the example network, there are two hidden layers, each containing 16 neurons <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>. The number of hidden layers and neurons within them can vary and often requires experimentation <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

The fundamental operation of the network involves activations in one layer determining the activations in the subsequent layer <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. When an image is fed into the input layer, the pattern of activations propagates through the hidden layers, culminating in a pattern in the output layer <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

## The Role of Hidden Layers: Abstraction

The intelligent behavior of a [[structure_and_function_of_a_neural_network | neural network]] stems from how its layered structure allows for hierarchical abstraction <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. Just as humans piece together components to recognize digits (e.g., a "9" has a loop and a line), the hope is that hidden layers perform similar breakdown tasks <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.

Ideally:
*   Neurons in the second-to-last hidden layer might correspond to larger "subcomponents" of digits, like an "upper loop" or a "long line" <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   Neurons in earlier hidden layers (e.g., the second layer) might pick up on even smaller, more fundamental patterns, such as "little edges" <a class="yt-timestamp" data-t="07:15:00">[07:15:00]</a>.

This hierarchical detection allows the network to build complexity: from pixels to edges, edges to patterns (like loops), and patterns to final digits <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>. This concept of layered abstraction is crucial for tasks beyond image recognition, such as parsing speech from raw audio into distinct sounds, syllables, words, and phrases <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

## How Activations Propagate: Weights, Biases, and Activation Functions

The core mechanism for how activations in one layer determine those in the next involves a system of weights and biases, processed through an [[introduction_to_activation_functions_like_sigmoid_and_relu | activation function]]:

1.  **Weights**: Each connection between a neuron in one layer and a neuron in the next layer is assigned a numerical "weight" <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. These weights act as parameters that determine the influence of an input neuron's activation on the subsequent neuron <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. For example, positive weights in a specific region of an image might indicate a pattern to be picked up, while negative weights for surrounding pixels could emphasize contrast, like detecting an edge <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.
2.  **Weighted Sum**: For a given neuron, its input is calculated by taking the sum of the activations of all neurons in the previous layer, each multiplied by its corresponding weight <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.
3.  **Bias**: An additional number, called a "bias," is added to this weighted sum <a class="yt-timestamp" data-t="11:11:00">[11:11:11]</a>. The bias allows a neuron to become active only when the weighted sum exceeds a certain threshold, essentially acting as a "bias for it to be inactive" <a class="yt-timestamp" data-t="11:02:00">[11:02:00]</a>.
4.  **Activation Function**: The final step is to "squish" this biased weighted sum into a range between 0 and 1 using an [[introduction_to_activation_functions_like_sigmoid and ReLU | activation function]] <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
    *   The **sigmoid function** (also known as a logistic curve) was historically common <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. It maps very negative inputs close to 0, positive inputs close to 1, and increases steadily around 0 <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.
    *   While motivated by the "inactive or active" biological analogy <a class="yt-timestamp" data-t="17:26:00">[17:26:00]</a>, modern networks often use other functions, such as the **ReLU (Rectified Linear Unit)**, which is typically easier to train <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. ReLU is defined as the maximum of zero and the input value <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.

### Network Parameters and "Learning"

The example network, with 784 input neurons, 16 neurons in each of two hidden layers, and 10 output neurons, involves approximately 13,000 total weights and biases <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>. These "knobs and dials" must be set appropriately for the network to solve the given problem <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>.

[[backpropagation_algorithm_in_neural_networks | Learning]] in a [[structure_and_function_of_a_neural_network | neural network]] refers to the process by which a computer automatically finds valid settings for all these weights and biases, rather than a human manually setting them <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. This process of finding optimal parameters is complex and will be explored in detail in discussions about the [[backpropagation_algorithm_in_neural_networks | backpropagation algorithm]] and [[cost_function_and_its_role_in_neural_networks | cost functions]].

## Mathematical Representation

The calculation of activations can be compactly represented using linear algebra <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>:
*   Activations from one layer are organized into a column vector <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>.
*   All weights connecting one layer to the next are organized into a matrix <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.
*   The weighted sum is then a matrix-vector product <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.
*   Biases are organized into a vector and added to this product <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
*   Finally, the [[introduction_to_activation_functions_like_sigmoid and ReLU | activation function]] (e.g., sigmoid) is applied element-wise to the resulting vector <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>.

This results in a concise mathematical expression for the transition of activations:
$$
\text{activation}_{\text{next layer}} = \sigma (\mathbf{W} \cdot \text{activation}_{\text{current layer}} + \mathbf{b})
$$
where $\sigma$ is the activation function, $\mathbf{W}$ is the weight matrix, and $\mathbf{b}$ is the bias vector <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>. This notation simplifies coding and leverages optimized matrix multiplication libraries <a class="yt-timestamp" data-t="15:05:00">[15:05:00]</a>.

Ultimately, a [[structure_and_function_of_a_neural_network | neural network]] is a complex function that takes a set of input numbers (e.g., 784 pixel values) and produces a set of output numbers (e.g., 10 probabilities for digits) <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>. Its complexity, involving thousands of parameters and iterative matrix operations, is precisely what allows it to tackle challenges like [[digit_recognition_using_neural_networks | handwritten digit recognition]] <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>.