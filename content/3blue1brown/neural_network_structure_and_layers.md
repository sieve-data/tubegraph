---
title: Neural network structure and layers
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

A neural network's primary goal is to learn from data, often exemplified by [[digit_recognition_using_neural_networks | handwritten digit recognition]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The way it achieves this is through its layered structure and the adjustment of its internal parameters.

## Fundamental Structure

The network's architecture is composed of interconnected layers of neurons <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### Input Layer
The network begins with an input layer <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. For [[digit_recognition_using_neural_networks | handwritten digit recognition]], this layer processes images of digits <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Digits are rendered on a 28x28 pixel grid <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   Each pixel has a grayscale value between 0 and 1 <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   These pixel values determine the activations of 784 neurons in the input layer (28x28 = 784) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Hidden Layers and Activation
Following the input layer are one or more "hidden" layers. In a typical configuration, the activation for each neuron in these layers is determined by:
*   A weighted sum of all activations from the previous layer <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   The addition of a "bias" value <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   Composing this sum with an activation function, such as a sigmoid or ReLU <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   For the example discussed, the network has two hidden layers, each with 16 neurons <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. The choice of two hidden layers with 16 neurons each is somewhat arbitrary <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Weights and Biases
In total, this specific network configuration possesses approximately 13,000 weights and biases that can be adjusted <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These values are crucial as they dictate the precise behavior of the network <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Initially, all weights and biases are set randomly <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   Weights are akin to the "strengths" of connections between neurons <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   Biases indicate whether a neuron tends to be active or inactive <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

### Output Layer
The final layer of the network contains 10 neurons <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, corresponding to the 10 possible digits (0-9).
*   A digit is classified by the network when the brightest of these 10 output neurons corresponds to that digit <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## How the Network Learns

The process by which a network learns involves minimizing a [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### The Cost Function
The [[cost_function_and_its_role_in_neural_networks | cost function]] quantifies how "lousy" the network's performance is <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   It's defined by summing the squares of the differences between the network's trash output activations and their desired values <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   This sum is small when the network correctly and confidently classifies an image, but large when it's performing poorly <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   The overall [[cost_function_and_its_role_in_neural_networks | cost]] is the average cost across tens of thousands of training examples <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
*   Conceptually, the [[cost_function_and_its_role_in_neural_networks | cost function]] takes the 13,000 or so weights and biases as inputs and outputs a single number indicating their "badness" <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Gradient Descent
The network learns by adjusting its weights and biases to reduce this [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This adjustment uses an algorithm called [[gradient_descent | gradient descent]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a> <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
*   The goal is to find the minimum of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   Since finding an explicit minimum for complex functions (especially with 13,000 inputs) is infeasible <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, [[gradient_descent | gradient descent]] iteratively takes small steps in the "downhill" direction <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   This "downhill" direction is determined by the negative of the function's gradient <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. The gradient indicates the direction of steepest ascent, so its negative points to the steepest descent <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   The length of the gradient vector signifies the steepness of this slope <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   Step sizes are proportional to the slope, meaning steps become smaller as the function flattens out towards a minimum, preventing overshooting <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   This process converges towards a local minimum <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. There is no guarantee that the local minimum found will be the absolute smallest possible value of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   For neural networks, the negative gradient is a vector that tells the network which "nudges" to its 13,000 weights and biases will cause the most rapid decrease in the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   The relative magnitudes of the gradient's components indicate which changes to weights and biases are more important or have a greater impact on the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   The [[cost_function_and_its_role_in_neural_networks | cost function]] must have a smooth output to enable finding a local minimum through small downhill steps <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is why artificial neurons have continuously ranging activations instead of binary ones <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Backpropagation
The efficient algorithm for computing this gradient, which is central to how neural networks learn, is called [[backpropagation_algorithm_in_neural_networks | backpropagation]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. A deeper, intuitive explanation of [[backpropagation_algorithm_in_neural_networks | backpropagation]] will be covered in the next video <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

## Network Performance and Interpretations

After training, the network's performance is tested on labeled data it has never seen before <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Performance on Digit Recognition
*   The discussed network with two hidden layers of 16 neurons each classifies about 96% of new images correctly <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
*   Tweaking the hidden layer structure can increase accuracy to 98% <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   This performance is notable, given that the network was not specifically told what patterns to look for <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

### What the Network *Actually* Learns
The initial motivation for the layered structure was a hope that:
*   The second layer might identify small edges <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   The third layer might piece together patterns like loops and lines <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   The final layer would assemble these patterns to recognize digits <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

However, for this specific network, this isn't what happens <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
*   Visualizing the weights between the first and second layers reveals almost random patterns, not isolated edges, suggesting loose patterns in the middle <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   The network finds a local minimum in the 13,000-dimensional space of weights and biases that classifies images successfully but doesn't align with intuitive pattern recognition <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   When presented with a random image, the network confidently provides a nonsense answer, rather than expressing uncertainty <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This indicates that while it can recognize digits, it has no idea how to draw them <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   This behavior stems from the tightly constrained training setup, where the network's "universe" consists only of clearly defined, centered digits, and its [[cost_function_and_its_role_in_neural_networks | cost function]] incentivized confident decisions <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Modern Context and Challenges
This network architecture, researched in the 1980s and 1990s, is considered old technology, but understanding it is foundational for more modern variants <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. While capable of solving interesting problems, the more one examines what hidden layers truly learn, the less intelligent the process seems <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

Further research into how modern image recognition networks learn reveals complexities:
*   One paper trained a deep neural network on randomly shuffled labels, finding it could still achieve the same training accuracy as on a properly labeled dataset <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This raised questions about whether minimizing the [[cost_function_and_its_role_in_neural_networks | cost function]] corresponds to image structure or merely memorization <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   Subsequent work suggested that while networks can memorize random data, the accuracy curve for random data goes down slowly, indicating a struggle to find the right weights <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. In contrast, training on structured data results in a much faster drop to the desired accuracy level, indicating an easier time finding local minima <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This implies that for structured datasets, the local minima tend to be of equal quality and easier to find <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.