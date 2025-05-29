---
title: Cost function and its role in neural networks
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

The **cost function** is a critical component in training neural networks, serving as a quantifiable measure of how poorly a network performs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Its primary purpose is to guide the network on how to adjust its parameters (weights and biases) to improve performance <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## Definition and Calculation

A cost function provides feedback to the computer about the accuracy of its output compared to the desired outcome <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. For a single training example, it's typically calculated by summing the squares of the differences between the actual output activations and their desired values <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This sum is small when the network confidently classifies an image correctly, and large when the network performs poorly <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

The overall cost for a network is the average cost across all training examples <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This average cost quantifies the network's overall performance or "lousiness" <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Inputs and Outputs

The cost function takes all the network's weights and biases as its inputs—in a network with two hidden layers and 16 neurons each, this can amount to approximately 13,000 weights and biases <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. It then outputs a single numerical value that describes how "bad" those weights and biases are <a class="yt-timestamp" data-t="00:4:56">[00:04:56]</a>. The definition of the cost function is influenced by the network's behavior across tens of thousands of training data points <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Minimization of the Cost Function

The primary goal of training a neural network is to minimize this [[gradient_descent_and_cost_function_minimization | cost function]] <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. When the cost function is minimized, it signifies better performance across all training samples <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

### Gradient Descent

Minimizing the cost function is typically achieved through an optimization algorithm called [[gradient_descent_and_cost_function_minimization | gradient descent]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, which is fundamental to how neural networks learn <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This process is akin to a [[calculus_in_the_context_of_neural_networks | calculus]] exercise <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The idea is to start with randomly initialized weights and biases <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Then, iteratively, the network computes the gradient of the cost function <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. The negative of this gradient points in the direction of the steepest decrease of the function <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. By taking small steps in this downhill direction, the network gradually approaches a local minimum of the cost function <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

The length of the gradient vector indicates the steepness of the slope <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. If the step sizes are proportional to the slope, steps become smaller as the function flattens out towards a minimum, preventing overshooting <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

In the context of 13,000 inputs, the negative gradient vector points to the precise adjustments needed for each weight and bias to most rapidly decrease the cost function <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This means transforming the network's output from random values to desired decisions for each training data point <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

## Implications and Challenges

*   **Smoothness:** For [[gradient_descent_and_cost_function_minimization | gradient descent]] to work effectively, the cost function must have a smooth output, allowing for incremental steps downhill <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is why artificial neurons often have continuously ranging activations, rather than binary (active/inactive) ones <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Local Minima:** There is no guarantee that the local minimum found by [[gradient_descent_and_cost_function_minimization | gradient descent]] will be the absolute smallest possible value of the cost function <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. The starting point (random initial weights and biases) can influence which local minimum is reached <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Memorization vs. Learning:** Minimizing the cost function doesn't always guarantee that the network learns meaningful [[structure_and_function_of_a_neural_network | patterns]]; in some cases, with enough parameters, a network can simply memorize the training data, even if it's randomly labeled <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. However, training on structured datasets tends to make it easier to find local minima quickly, suggesting a deeper learning process beyond mere memorization <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
*   **Gradient Components:** Each component of the negative gradient indicates whether a corresponding input (weight or bias) should be nudged up or down <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. Importantly, the relative magnitudes of these components reveal which changes have a greater impact on the cost function, indicating the "importance" of specific weights and biases <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This can be interpreted as which changes offer the most "bang for your buck" <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

## Connection to Backpropagation

The efficient algorithm for computing the gradient of the cost function, which is at the heart of how a neural network learns, is called [[backpropagation_algorithm_in_neural_networks | backpropagation]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This process determines how each weight and bias should be adjusted for a given piece of training data to reduce the cost <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.