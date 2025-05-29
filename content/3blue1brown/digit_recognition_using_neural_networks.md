---
title: Digit recognition using neural networks
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

Our brains effortlessly recognize handwritten digits, even when they are sloppily written or at low resolution <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For instance, various forms of the digit '3' are easily identified, despite significant pixel variations <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. However, programming a computer to perform this seemingly trivial task, such as taking a 28x28 pixel grid and outputting the correct digit, becomes "dauntingly difficult" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This is where [[neural_networks_and_their_inspiration_from_the_brain | neural networks]] come into play <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

This article aims to explain what a [[neural_networks_and_their_inspiration_from_the_brain | neural network]] actually is, specifically in the context of recognizing handwritten digits, by visualizing its mathematical components <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The goal is for the [[neural_network_structure_and_layers | structure itself]] to feel motivated and to understand how a [[neural_networks_and_their_inspiration_from_the_brain | neural network]] "learns" <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## [[Neural network structure and layers | Structure of a Neural Network]]

[[neural_networks_and_their_inspiration_from_the_brain | Neural networks]] are inspired by the brain <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. At its simplest, a "neuron" in this context is merely a component that holds a number, specifically a value between 0 and 1 <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This number is called its "activation," and a higher number indicates that the neuron is "lit up" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

A typical [[neural_network_structure_and_layers | structure]] for digit recognition includes multiple layers <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>:

*   **Input Layer**: This first layer consists of 784 neurons, corresponding to each of the 28x28 pixels of the input image <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Each neuron's activation represents the grayscale value of its corresponding pixel, ranging from 0 (black) to 1 (white) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Output Layer**: The last layer has 10 neurons, with each neuron representing a digit from 0 to 9 <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The activation of these neurons (between 0 and 1) indicates the system's confidence that the image corresponds to a specific digit <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Hidden Layers**: Between the input and output layers are "hidden layers." In this specific example, there are two hidden layers, each containing 16 neurons <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. The number of hidden layers and neurons within them can vary and is often determined experimentally <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Information Flow

The network operates by having activations in one layer determine the activations of the next layer <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This process is loosely analogous to how neurons in a biological network cause others to fire <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. For a [[training_neural_networks_for_handwritten_digit_recognition | trained]] network, feeding in an image (by lighting up input neurons) causes a specific pattern of activations to propagate through the hidden layers, culminating in the output layer <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. The brightest neuron in the output layer indicates the network's prediction for the digit <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Hierarchical Abstraction

A key expectation for a layered [[neural_network_structure_and_layers | structure]] is its ability to learn hierarchical abstractions <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Just as humans piece together components to recognize digits (e.g., a '9' has a loop and a line) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>, the hope is that hidden layers can identify these subcomponents. For example:

*   Neurons in the second-to-last layer might correspond to larger patterns like a "loop up top" <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   Neurons in earlier layers might correspond to smaller, more fundamental elements, such as "little edges" that compose these larger patterns <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

This means that an image of a '9' might activate neurons corresponding to specific edges, which then activate neurons corresponding to an upper loop and a vertical line, finally activating the '9' neuron in the output layer <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This layered detection of patterns is highly useful not just for digit recognition, but for broader [[Image Processing and Convolutions | image recognition]] and other complex tasks like speech parsing <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

## [[Structure and function of a neural network | Mechanics of Neuron Activation]]

To enable a neuron to pick up on specific patterns (like an edge in a particular region), the network employs parameters:

*   **Weights**: Each connection between a neuron in one layer and a neuron in the next layer is assigned a "weight" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. These weights are numbers that dictate the influence of the previous layer's neuron on the current one <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Positive weights can indicate a feature that should activate the neuron, while negative weights might indicate a feature that should suppress it <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   To detect an edge, for instance, a neuron might have strong positive weights for pixels in the center of the edge and negative weights for surrounding pixels <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.
*   **Weighted Sum**: The input to a neuron is calculated by taking the weighted sum of the activations of all neurons in the previous layer <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Bias**: After computing the weighted sum, an additional number called a "bias" is added <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. This bias allows the neuron to be more or less active depending on the desired threshold <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   **Sigmoid Function (Activation Function)**: Since neuron activations are typically between 0 and 1, the weighted sum plus bias is passed through an "activation function" that "squishes" any real number into this range <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. A common choice is the sigmoid function (also known as a logistic curve), which maps very negative inputs close to 0 and positive inputs close to 1 <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

<div class="callout">
    [!NOTE]
    ### Sigmoid vs. ReLU
    Early [[neural_networks_and_their_inspiration_from_the_brain | neural networks]] used the sigmoid function, motivated by the biological analogy of neurons being either inactive or active <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. However, relatively few modern networks use sigmoid anymore <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. A more common activation function today is the Rectified Linear Unit (ReLU), which is defined as the maximum of zero and its input (`max(0, a)`) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. ReLU often makes [[training_neural_networks_for_handwritten_digit_recognition | training]] [[challenges_in_neural_network_optimization_and_performance_evaluation | deep neural networks]] much easier <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
</div>

### Parameters and Learning

For a network with 784 input neurons, 16 hidden neurons in the first hidden layer, and 16 in the second hidden layer, there are approximately 13,000 total weights and biases <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. These weights and biases are the "knobs and dials" that can be tweaked to make the network behave differently <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

"[[training_neural_networks_for_handwritten_digit_recognition | Learning]]" in a [[neural_networks_and_their_inspiration_from_the_brain | neural network]] refers to the process of finding valid settings for these thousands of numbers so that the network can solve the given problem <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

### Mathematical Representation

The calculation of activations from one layer to the next can be expressed compactly using [[calculus_in_the_context_of_neural_networks | linear algebra]] <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>:

*   Activations of a layer are organized into a column vector <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   Weights connecting two layers are organized into a matrix <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The weighted sum is then equivalent to a matrix-vector product <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   Biases are organized into a vector and added to the result <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   Finally, the sigmoid function is applied to each component of the resulting vector <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

This allows the full transition of activations between layers to be represented by a single, concise expression: `sigmoid(Weight_Matrix * Activation_Vector + Bias_Vector)` <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

Ultimately, the entire [[neural_networks_and_their_inspiration_from_the_brain | neural network]] is just an extremely complex function that takes 784 numbers as input and produces 10 numbers as output <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. It involves 13,000 parameters and iterates through many matrix-vector products and activation functions <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. The complexity is reassuring, as a simpler function would likely be inadequate for recognizing digits <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

The next step is to understand how the network learns the appropriate weights and biases from data <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.