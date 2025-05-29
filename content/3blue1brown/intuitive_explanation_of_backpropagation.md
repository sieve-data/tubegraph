---
title: Intuitive explanation of backpropagation
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

[[backpropagation_algorithm_walkthrough | Backpropagation]] is the fundamental algorithm that enables [[backpropagation_algorithm_in_neural_networks | neural networks]] to learn <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This article provides an intuitive walkthrough of what the algorithm accomplishes, without delving into the mathematical formulas initially <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Neural Network Basics & Cost Function Recap

Before diving into [[backpropagation_algorithm_walkthrough | backpropagation]], it's important to understand the context:
*   **Neural Network Structure**: A neural network takes input, like pixel values of a handwritten digit (e.g., 784 neurons for a 784-pixel image) <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It processes this information through hidden layers (e.g., two hidden layers with 16 neurons each) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, and outputs a prediction through an output layer (e.g., 10 neurons for digits 0-9) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Information flows forward through the network <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   **Learning as Optimization**: Learning in a neural network means finding the specific weights and biases that minimize a certain [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **[[cost_function_and_its_role_in_neural_networks | Cost Function]]**: For a single training example, the cost is calculated by taking the network's output and the desired output, then adding up the squares of the differences between each component <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The total cost of the network is the average of these individual costs across all training examples <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **[[understanding_gradients_in_backpropagation | Gradient Descent]]**: The goal is to find the negative [[understanding_gradients_in_backpropagation | gradient]] of this [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This [[understanding_gradients_in_backpropagation | gradient]] indicates how to change all weights and biases to most efficiently decrease the cost <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The Role of Backpropagation

[[backpropagation_algorithm_walkthrough | Backpropagation]] is the algorithm specifically designed to compute this complex [[understanding_gradients_in_backpropagation | gradient]] <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Intuition Behind the Gradient

Instead of visualizing a [[understanding_gradients_in_backpropagation | gradient]] vector in thousands of dimensions, it's more intuitive to understand that each component of the [[understanding_gradients_in_backpropagation | gradient]] vector tells you how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to changes in each specific weight and bias <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

For example, if changing a weight on one connection by a small amount causes 32 times more change in the cost than changing a weight on another connection by the same amount, the [[cost_function_and_its_role_in_neural_networks | cost function]] is 32 times more sensitive to the first weight <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. [[backpropagation_algorithm_walkthrough | Backpropagation]] helps identify which changes provide the "most bang for your buck" in reducing the cost <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Intuitive Walkthrough: A Single Training Example

[[backpropagation_algorithm_walkthrough | Backpropagation]]'s individual effects are intuitive, though many small adjustments are layered together <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Let's consider a single training example, like an image of the digit "2" <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Desired Output Layer Adjustments

If the network is not well-trained, its output activations might be random <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. Since the desired output for a "2" is to activate the '2' neuron strongly while suppressing others, we wish the '2' neuron's activation would increase and others decrease <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The size of these desired "nudges" is proportional to how far each current value is from its target <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

### How to Achieve Desired Nudges (Locally)

To increase a neuron's activation (which is a weighted sum of previous activations plus a bias, passed through an activation function like sigmoid or ReLU) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>, there are three main avenues:
1.  **Increase the bias** of that neuron <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Increase the weights** connecting to that neuron <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Weights connected to brighter (more active) neurons in the preceding layer have a stronger influence on the cost <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
3.  **Change the activations** from the previous layer <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. If neurons connected with positive weights got brighter, and those with negative weights got dimmer, the target neuron would become more active <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

### Propagating Backwards

The "bang for your buck" principle applies: changes are sought proportionally to the size of corresponding weights <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

The key insight of [[backpropagation_algorithm_walkthrough | backpropagation]] is that the desired changes for a neuron in a hidden layer are influenced by *all* the subsequent neurons it connects to in the next layer <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The desires of all output neurons for what should happen to the second-to-last layer are added together, again proportional to the corresponding weights and how much each neuron needs to change <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This is where the idea of "propagating backwards" comes in <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

By adding these desired effects, a list of "nudges" for the second-to-last layer is obtained <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This process is then recursively applied, moving backwards through the network to determine the desired changes for weights and biases in earlier layers <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Scaling Up: Averaging and Efficiency

The "nudges" derived above are only for a *single* training example <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. To avoid the network only learning to classify everything as a '2', this [[backpropagation_algorithm_walkthrough | backprop]] routine must be performed for *every* training example <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. The desired changes from all examples are then averaged together <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. This collection of averaged nudges represents the negative [[understanding_gradients_in_backpropagation | gradient]] of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

### [[Stochastic Gradient Descent]]

> [!NOTE] Computational Efficiency
> Computing the influence of every training example for each [[understanding_gradients_in_backpropagation | gradient descent]] step is computationally intensive <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

To address this, [[Stochastic Gradient Descent]] is commonly used <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>:
1.  Training data is randomly shuffled <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
2.  It's divided into mini-batches (e.g., 100 examples per batch) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  Each [[understanding_gradients_in_backpropagation | gradient descent]] step is computed based on a single mini-batch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

While a mini-batch does not represent the true [[understanding_gradients_in_backpropagation | gradient]] of the total [[cost_function_and_its_role_in_neural_networks | cost function]] (which depends on all data) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, it provides a good approximation and a significant computational speedup <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This approach is like a "drunk man stumbling aimlessly down a hill but taking quick steps," rather than a "carefully calculating man taking slow, precise steps" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

## Summary

[[backpropagation_algorithm_walkthrough | Backpropagation]] is the algorithm for determining how a single training example wants to nudge weights and biases <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, not just in terms of direction (up or down) but also in terms of relative proportions for the most rapid cost decrease <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. For a true [[understanding_gradients_in_backpropagation | gradient descent]] step, these desired changes would be averaged across all training examples <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. However, due to computational constraints, data is often subdivided into mini-batches for [[Stochastic Gradient Descent]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. By repeatedly adjusting weights and biases using these mini-batches, the network converges towards a local minimum of the [[cost_function_and_its_role_in_neural_networks | cost function]], leading to good performance on training examples <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

> [!INFO] Next Steps & Data Requirements
> The underlying [[calculus_in_the_context_of_neural_networks | calculus]] provides a more formal understanding of [[backpropagation_algorithm_walkthrough | backpropagation]] <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. It's crucial to note that for this algorithm, and much of machine learning, a significant amount of labeled training data is essential <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.