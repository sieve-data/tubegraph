---
title: Gradient descent and cost function
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

Neural networks learn by adjusting their internal parameters to improve performance on a given task, such as handwritten digit recognition <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This learning process fundamentally relies on minimizing a [[cost_function | cost function]] using an optimization algorithm called [[gradient_descent_in_neural_networks | gradient descent]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

## Neural Network Structure and Parameters
A neural network, like the one used for handwritten digit recognition, is a function that takes inputs (e.g., 784 pixel values for a 28x28 image) and produces outputs (e.g., 10 numbers indicating digit probabilities) <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The activation of each neuron in subsequent layers depends on a weighted sum of activations from the previous layer, plus a bias <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. For a network with two hidden layers of 16 neurons each, there are approximately 13,000 weights and biases <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These values determine the network's behavior <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Initially, these weights and biases are set randomly <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, leading to poor performance <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## The Cost Function
To improve the network's performance, a [[cost_function | cost function]] is defined <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This function quantifies how "bad" the network's output is compared to the desired output for a given training example <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Calculation
For a single training example, the cost is calculated by summing the squares of the differences between each output activation and its desired value <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. A small sum indicates the network correctly classifies the image, while a large sum signifies poor performance <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Average Cost
The overall measure of the network's "lousiness" is the average cost across all tens of thousands of training examples <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>, <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This average cost function takes the 13,000 weights and biases as its inputs and outputs a single number indicating their collective "badness" <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Minimizing this function means improving performance across all training samples <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Gradient Descent
The goal of learning is to find the weights and biases that minimize the [[cost_function | cost function]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. [[gradient_descent_in_neural_networks | Gradient descent]] is an iterative optimization algorithm used for this purpose <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

### The Principle of "Stepping Downhill"
The core idea is to start with random parameters and repeatedly adjust them in the direction that decreases the cost most rapidly <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

*   **Single Input Function Analogy**: For a function with one input, this means checking the slope: shift left if the slope is positive, and right if it's negative <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. Repeating this process leads to a local minimum <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Step sizes are proportional to the slope, meaning smaller steps as the function flattens out, preventing overshooting <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Multiple Input Function Analogy**: For functions with two or more inputs, the concept extends to finding the "downhill direction" in the input space <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>, <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

### The Role of the Gradient
In multivariable calculus, the gradient of a function indicates the direction of steepest ascent <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>, <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Therefore, the negative of the gradient points in the direction of steepest descent, which is the desired "downhill" direction for minimizing the function <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. The length of the gradient vector indicates the steepness of this slope <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

In the context of neural networks, the negative gradient of the [[cost_function | cost function]] is a vector in a 13,000-dimensional input space (representing all weights and biases) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It indicates which "nudges" to these numbers will cause the most rapid decrease in the cost function <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>, <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Each component of the negative gradient reveals whether a corresponding input (weight or bias) should be nudged up or down, and its relative magnitude signifies the [[sensitivity_of_cost_function | importance]] of that change to the [[cost_function | cost function]] <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>, <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>, <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.

### Implementation Details
The algorithm for efficiently [[computing_derivatives_of_functions | computing]] this gradient is called [[backpropagation_algorithm | backpropagation]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, which is central to how neural networks learn <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

### Local Minima
It's important to note that [[gradient_descent_in_neural_networks | gradient descent]] converges to a *local* minimum, not necessarily the absolute smallest possible value of the [[cost_function | cost function]] <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>, <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. The starting point (initial random weights and biases) influences which local minimum is found <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Smoothness of the Cost Function
For [[gradient_descent_in_neural_networks | gradient descent]] to work effectively by taking small steps downhill, the [[cost_function | cost function]] must have a smooth output <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. This is why artificial neurons often have continuously ranging activations (e.g., sigmoid or ReLU), rather than binary active/inactive states like biological neurons <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

## Network Performance and Interpretation
After training with [[gradient_descent_in_neural_networks | gradient descent]], the described network (two hidden layers, 16 neurons each) can classify about 96% of new images correctly <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>, <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. While effective, the visual interpretation of what the hidden layers are learning (e.g., edges, patterns) doesn't always align with human intuition; the learned patterns can appear almost random <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>, <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. This suggests that the network finds a local minimum that works, even if the internal representations are not what humans expect <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

Recent research into deeper neural networks suggests that while they can memorize random data (achieving high training accuracy with shuffled labels), training on structured datasets allows them to find local minima more easily and rapidly <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>, <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. Furthermore, for structured datasets, the local minima these networks tend to learn are often of equal quality <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>, <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.