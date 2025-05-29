---
title: Neural network learning process
videoId: aircAruvnKk
---

From: [[3blue1brown]] <br/> 

The process of a [[Neural Networks and Transformers | neural network]] "learning" refers to how the computer identifies appropriate settings for its numerous internal parameters to solve a given problem <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This process involves adjusting the thousands of [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] within the network <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

## Training a Neural Network
When a [[Neural Networks and Transformers | neural network]] is trained to recognize handwritten digits, it is fed an image, and the 784 neurons of the input layer are activated based on the brightness of each pixel <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This pattern of activations then propagates through the network, causing specific patterns in subsequent layers, ultimately leading to a pattern in the output layer <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. The brightest neuron in the output layer indicates the network's prediction for the digit <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

The specific method for [[Training neural networks with MNIST data | training neural networks]] and how one layer influences the next involves intricate mathematical computations, which constitute the "heart of the network as an information processing mechanism" <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

## The Role of Weights and Biases
A typical [[Structure of neural networks | neural network]] designed for digit recognition can have approximately 13,000 total [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. These serve as "knobs and dials" that can be adjusted to alter the network's behavior <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.

The [[adjusting_weights_and_biases_in_neural_networks | weights]] associated with connections between neurons determine what specific patterns a neuron will detect <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. For example, by setting positive weights in a specific region and negative weights in surrounding pixels, a neuron can be made to pick up on edges <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The [[adjusting_weights_and_biases_in_neural_networks | bias]] for a neuron controls how high the weighted sum of inputs needs to be before the neuron becomes significantly active <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### Hope for Layered Learning
In an ideal scenario, each neuron in the hidden layers might learn to correspond to specific subcomponents of digits <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. For instance:
*   Neurons in an early hidden layer could learn to recognize small edges <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Neurons in a subsequent hidden layer might learn to recognize more complex patterns, such as loops or long lines, by combining these smaller edge detections <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   The final output layer would then identify digits based on the combination of these recognized subcomponents <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

This hierarchical approach suggests that a [[Neural Networks and Transformers | neural network]] can break down complex recognition tasks into layers of abstraction, similar to how speech parsing involves distinguishing sounds, syllables, words, and phrases <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Whether a trained network actually performs this type of hierarchical decomposition is a question explored after understanding the [[Backpropagation algorithm | training process]] <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.