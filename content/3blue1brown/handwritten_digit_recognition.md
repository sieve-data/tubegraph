---
title: Handwritten digit recognition
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

## The Challenge of Recognition
Recognizing handwritten digits, like a sloppily written '3' at a low resolution of 28x28 pixels, is effortless for the human brain <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Our brains can recognize variations of the same digit even when individual pixel values differ significantly <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. However, programming a computer to perform this task—taking a 28x28 pixel grid and outputting a digit between 0 and 10—is a daunting challenge <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Introduction to Neural Networks
Neural networks are a powerful tool in machine learning, offering a way to tackle complex problems like handwritten digit recognition <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This article explains the fundamental structure of a neural network, treating it as a mathematical construct rather than a buzzword <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The ultimate goal is to build a network capable of recognizing handwritten digits <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

While many variants of neural networks exist, this explanation focuses on the simplest "plain vanilla" form, which serves as a necessary prerequisite for understanding more powerful modern versions <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Even in this basic form, a neural network can learn to recognize handwritten digits <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Core Components: Neurons and Activations
Neural networks are inspired by the brain <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. At its simplest, a neuron is a "thing that holds a number," specifically a value between 0 and 1 <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This number is called its **activation** <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. A high activation value can be visualized as the neuron "lighting up" <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Network Structure: Layers
A typical neural network for digit recognition is organized into layers:
*   **Input Layer**: For a 28x28 pixel image, the input layer consists of 784 neurons (28 * 28) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Each neuron holds a number representing the grayscale value of a corresponding pixel, ranging from 0 (black) to 1 (white) <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Output Layer**: This layer has 10 neurons, each representing one of the digits (0 through 9) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The activation of these neurons indicates how strongly the network believes the image corresponds to a given digit <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The brightest neuron in this layer indicates the network's choice <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **Hidden Layers**: These are layers positioned between the input and output layers <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. In the described network, there are two hidden layers, each with 16 neurons <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. The number of hidden layers and neurons can be varied through experimentation <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

Activations in one layer determine the activations in the subsequent layer <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This process is loosely analogous to how neurons in biological networks cause others to fire <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. When an image is "fed in," the input layer's activations propagate through the hidden layers to produce a pattern in the output layer <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### The Hope for Intelligent Behavior in Layers
The layered structure of a neural network allows for the breakdown of complex recognition tasks into simpler sub-problems <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>:
*   **Decomposition**: Recognizing digits can involve identifying various subcomponents, such as loops (e.g., in '9' or '8') or specific lines (e.g., in '4') <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Layer Specialization**: Ideally, neurons in a later hidden layer might correspond to these subcomponents. For example, a neuron might activate strongly if it detects any generally loopy pattern towards the top of an image <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Hierarchical Recognition**: Recognizing a loop, in turn, can be broken down into recognizing smaller edges that make it up <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. Thus, an earlier hidden layer might specialize in detecting various small edges <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

This hierarchical approach suggests a flow: pixels combine into edges, edges combine into patterns (like loops), and patterns combine into digits <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This layered abstraction is not limited to image recognition; it's also applicable to tasks like parsing speech, where raw audio breaks down into sounds, then syllables, words, and phrases <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## How Activations Propagate: Weights and Biases
The core of how one layer influences the next lies in **weights** and **biases** <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Weights**: Each connection between a neuron in one layer and a neuron in the next has an associated numerical weight <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. To calculate the input to a neuron, the activations from the previous layer are multiplied by their respective weights, and these weighted values are summed <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Weights effectively tell a neuron what pixel or pattern it should be "picking up on" <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. For example, specific positive weights in a region and negative weights in surrounding pixels could help a neuron detect an edge <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.
*   **Bias**: After computing the weighted sum, an additional number called the **bias** is added <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The bias determines how high the weighted sum needs to be before the neuron becomes meaningfully active, essentially acting as a threshold <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### The Sigmoid Activation Function
Since neuron activations must be between 0 and 1, the weighted sum plus bias is passed through an **activation function** that squishes the result into this range <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. A common choice historically is the **sigmoid function** (also known as a logistic curve) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. This function maps very negative inputs close to 0, very positive inputs close to 1, and increases steadily around an input of 0 <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. The neuron's activation is thus a measure of how positive the relevant weighted sum is <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

### Network Complexity
For a network with 784 input neurons and a hidden layer of 16 neurons, there are 784 * 16 weights and 16 biases just for the connections to that first hidden layer <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Across all layers in the example network (784-16-16-10 neuron layers), there are almost 13,000 total weights and biases <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. These "knobs and dials" can be tweaked to make the network behave differently <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

### Mathematical Representation
The propagation of activations from one layer to the next can be compactly represented using linear algebra <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>:
*   Activations of a layer are organized into a column vector <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.
*   All weights connecting one layer to the next are organized into a weight matrix <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   The weighted sum calculation is equivalent to a matrix-vector product of the weight matrix and the activation vector <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   Biases are organized into a bias vector, which is then added to the result of the matrix-vector product <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>.
*   Finally, the sigmoid function is applied to each component of the resulting vector <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

This mathematical notation (e.g., `a = sigmoid(W * a_prev + b)`) makes the representation of network operations extremely concise and leads to more efficient code, especially since matrix multiplication is highly optimized in many programming libraries <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

Ultimately, the entire network functions as a single, complex mathematical function <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>: it takes 784 numbers as input and outputs 10 numbers <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. This function involves iterating many matrix-vector products and applying the sigmoid function, controlled by thousands of weights and biases <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

## Learning in Neural Networks
When discussing "learning" in the context of neural networks, it refers to the process of finding the optimal settings for all these weights and biases <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a> <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This process, which allows the computer to solve the given problem by looking at data, will be explored in detail in subsequent discussions <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## Modern Activation Functions
While the sigmoid function was common in early neural networks, motivated by a biological analogy of neurons being either inactive or active <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>, it is less frequently used in modern networks <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. The Rectified Linear Unit (ReLU) function (`max(0, a)`) is now much more common <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. ReLU, also partially inspired by biological neurons, has proven easier to train, especially for very deep neural networks <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.