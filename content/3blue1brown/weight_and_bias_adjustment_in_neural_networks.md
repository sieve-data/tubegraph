---
title: Weight and bias adjustment in neural networks
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

[[structure_and_function_of_a_neural_network | Neural networks]] are computational models inspired by the brain, designed to recognize patterns and make decisions based on data. Their ability to "learn" comes from the adjustment of numerous internal parameters known as weights and biases <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

## Neural Network Structure and Operation
A [[structure_and_function_of_a_neural_network | neural network]] is composed of interconnected "neurons" organized into layers <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. Each neuron holds a numerical value between 0 and 1, called its "activation" <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.

For a network designed to recognize [[training_neural_networks_for_handwritten_digit_recognition | handwritten digits]], the input layer consists of neurons representing each pixel of an image (e.g., 784 neurons for a 28x28 pixel image), with activations corresponding to pixel brightness <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. The final output layer has 10 neurons, each representing a digit from 0 to 9, where the activation indicates the system's confidence in that digit <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>. Between these are "hidden layers" which process information in abstract ways <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.

The core operation of a [[structure_and_function_of_a_neural_network | neural network]] involves activations in one layer determining the activations of the next <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.

## Weights
Each connection between neurons in successive layers is assigned a "weight" <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. These weights are numerical values that determine the influence of one neuron's activation on the next. The activations from the previous layer are multiplied by these weights and then summed <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

*   **Pattern Recognition**: Weights allow neurons to pick up on specific patterns. For instance, positive weights in a certain region of input pixels, combined with negative weights in surrounding pixels, can enable a neuron to detect an "edge" <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.

## Biases
After computing the weighted sum of activations, an additional number called the "bias" is added <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. This bias determines the threshold at which a neuron becomes meaningfully active after the sum is passed through an activation function <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

## Activation Function
The resulting sum (weighted sum plus bias) is then "squished" into a range between 0 and 1 using an activation function <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. Traditionally, the sigmoid function (logistic curve) was used for this <a class="yt-timestamp" data-t="10:32:00">[10:32:00]</a>. However, modern networks more commonly use the Rectified Linear Unit (ReLU) function, which simplifies training, especially for very deep networks <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.

## The Role of Parameters in Learning
The combination of weights and biases allows the network to capture complex patterns and relationships within the data. A typical network for [[training_neural_networks_for_handwritten_digit_recognition | handwritten digit recognition]] can have tens of thousands of weights and biases (e.g., almost 13,000 for the described network) <a class="yt-timestamp" data-t="12:18:00">[12:18:00]</a>.

### "Learning" as Parameter Adjustment
When we talk about a [[structure_and_function_of_a_neural_network | neural network]] "learning," it refers to the process of finding the optimal settings for all these weights and biases <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>. This process allows the network to accurately solve the problem at hand, such as recognizing digits <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>. The goal is to set these parameters such that the network can reliably combine input pixels into edges, edges into patterns, and patterns into digits <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>.

While it's possible to imagine manually setting these parameters for simple cases, the sheer number of weights and biases makes manual [[role_of_parameter_tuning_in_machine_learning_models | parameter tuning]] impossible <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. Instead, algorithms are used to automatically adjust these parameters during the training phase. The next video will delve into how this "learning" process occurs, which involves concepts like [[understanding_gradients_in_backpropagation | gradients]] and the [[backpropagation_algorithm_in_neural_networks | backpropagation algorithm]] <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

Even in its simplest form, understanding what weights and biases represent provides insight into how [[structure_and_function_of_a_neural_network | neural networks]] function, helping to diagnose issues or challenge assumptions when performance is not as expected <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>.

## Mathematical Representation
The calculation of activations in a layer from the previous layer can be expressed compactly using linear algebra <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a>. Activations are represented as column vectors, weights as a matrix, and biases as a vector <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>. The weighted sum is equivalent to a matrix-vector product, to which the bias vector is added, and then the activation function (e.g., sigmoid) is applied component-wise to the resulting vector <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.

> <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a> "So once you write down this weight matrix and these vectors as their own symbols, you can communicate the full transition of activations from one layer to the next in an extremely tight and neat little expression."

Ultimately, a [[structure_and_function_of_a_neural_network | neural network]] is a complex function that takes input numbers and produces output numbers, defined by its 13,000 or more adjustable weights and biases <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.