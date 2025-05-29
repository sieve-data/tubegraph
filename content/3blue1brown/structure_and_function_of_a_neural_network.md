---
title: Structure and function of a neural network
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

A [[neural_networks_and_their_inspiration_from_the_brain | neural network]] is a computational model inspired by the brain, designed to process complex information such as [[digit_recognition_using_neural_networks | recognizing handwritten digits]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The core purpose of understanding a [[neural_network_structure_and_layers | neural network]] is to visualize its operations not as a buzzword, but as a piece of mathematics <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Core Components: Neurons and Layers

The basic unit of a [[neural_network_structure_and_layers | neural network]] is a "neuron," which simply holds a number, specifically a value between 0 and 1 <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This number is referred to as its "activation," where a higher number indicates the neuron is "lit up" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

[[neural_network_structure_and_layers | Neural networks]] are organized into layers:

*   **Input Layer** The network begins with an input layer, where each neuron corresponds to a specific input feature <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. For handwritten [[digit_recognition_using_neural_networks | digit recognition]], a 28x28 pixel image translates into 784 neurons in the first layer <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Each of these neurons holds a number representing the grayscale value of its corresponding pixel, ranging from 0 (black) to 1 (white) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Output Layer** The final layer consists of neurons representing the possible outputs <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. In the case of [[digit_recognition_using_neural_networks | digit recognition]], there are 10 neurons, each representing a digit from 0 to 9 <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The activation of these neurons indicates how strongly the network believes the input image corresponds to a specific digit <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The brightest neuron in the output layer signifies the network's choice for the digit <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Hidden Layers** Between the input and output layers are "hidden layers" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. These layers process the information in intermediate steps <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. A common network configuration might include two hidden layers, each with 16 neurons <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The specific number of hidden layers and neurons can be subject to experimentation <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## Information Processing: Activations, Weights, and Biases

The operation of a [[neural_network_structure_and_layers | neural network]] involves activations in one layer determining the activations of the subsequent layer <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This process is loosely analogous to how biological neurons cause others to fire <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

When an image is fed into a trained network, the pixel brightness activates the input neurons <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This pattern of activations propagates through the layers, ultimately leading to a specific pattern in the output layer <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Weights

Each connection between a neuron in one layer and a neuron in the next layer is assigned a "weight" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. These weights are numbers used to compute a "weighted sum" of the activations from the previous layer <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. For example, if a neuron is meant to detect an edge, it might have positive weights associated with pixels forming the edge and negative weights with surrounding pixels <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

### Biases

After computing the weighted sum, an additional number called a "bias" is added <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The bias determines how high the weighted sum needs to be before a neuron becomes meaningfully active <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### Activation Functions

The resulting sum (weighted sum plus bias) is then fed into an "activation function" that "squishes" the real number line into a range, typically between 0 and 1 <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Sigmoid Function (Logistic Curve)**: Historically, the sigmoid function was commonly used <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. It maps very negative inputs close to 0, positive inputs close to 1, and steadily increases around an input of 0 <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This was motivated by the biological analogy of neurons being either inactive or active <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
*   **Rectified Linear Unit (ReLU)**: In modern [[neural_network_structure_and_layers | neural networks]], ReLU is often preferred because it is generally easier to train <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. The ReLU function takes the maximum of zero and its input (`max(0, a)`), simplifying the activation to either zero (inactive) or the identity function (active) if it passes a certain threshold <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.

### Learning

A typical [[neural_network_structure_and_layers | neural network]] for [[digit_recognition_using_neural_networks | digit recognition]] can have around 13,000 total weights and biases <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. "Learning" in the context of [[neural_network_structure_and_layers | neural networks]] refers to the process of getting a computer to find valid settings for all these numbers (weights and biases) so that the network can effectively solve the problem at hand <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This process of learning how to adjust these parameters is the subject of subsequent discussions <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## The Network as a Function

The entire [[neural_network_structure_and_layers | neural network]] can be thought of as a single, complex function <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. It takes a fixed number of inputs (e.g., 784 numbers for pixel values) and produces a fixed number of outputs (e.g., 10 numbers for digit probabilities) <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. This function involves numerous parameters (weights and biases) and repeated matrix-vector products combined with activation functions <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Layered Abstraction

The expectation for a layered [[neural_network_structure_and_layers | neural network]] is that the hidden layers will break down complex tasks into subcomponents <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For example, in [[digit_recognition_using_neural_networks | digit recognition]]:
*   Neurons in an early hidden layer might learn to detect small edges <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   Subsequent layers might combine these edges to recognize larger patterns, such as loops or lines <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.
*   The final layers combine these patterns to identify the complete digit <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

This hierarchical approach of breaking down problems into layers of abstraction is useful not only for image recognition but also for other tasks like parsing speech, where raw audio can be broken down into sounds, syllables, words, and ultimately abstract thoughts <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Mathematical Notation

To represent the connections and calculations more compactly, mathematical notation is used:
*   Activations from a layer are organized into a column vector <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   Weights connecting one layer to the next are organized into a matrix <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>. Each row of this matrix corresponds to the connections for a particular neuron in the next layer <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   The weighted sum is computed using a matrix-vector product <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   Biases are organized into a vector and added to the result of the matrix-vector product <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   The activation function (e.g., sigmoid, denoted as 'σ') is applied component-wise to the resulting vector <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

This results in a concise expression: `a_current_layer = σ(W * a_previous_layer + b)` where `a` denotes activation vectors, `W` the weight matrix, and `b` the bias vector <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This compact notation simplifies code and allows for optimized matrix multiplication using computational libraries <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.