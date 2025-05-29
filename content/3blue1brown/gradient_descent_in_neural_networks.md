---
title: Gradient descent in neural networks
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

[[backpropagation_algorithm | Backpropagation]], the core algorithm for how neural networks learn, is fundamentally about computing the complex gradient of a cost function <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The ultimate goal of the [[neural_network_learning_process | neural network learning process]] is to find the specific weights and biases that minimize this cost function <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This process of finding the optimal weights and biases to decrease cost is guided by [[gradient_descent_and_cost_function | gradient descent]] <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The Cost Function

The cost function quantifies how well a neural network is performing <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
For a single training example, the cost is calculated by taking the network's output and comparing it to the desired output, summing the squares of the differences between each component <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The total cost for the network is then the average of these individual costs across all tens of thousands of training examples <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Understanding the Gradient

The negative gradient of the cost function is the key to efficient learning <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. It indicates how to [[adjusting_weights_and_biases_in_neural_networks | change all weights and biases]] to most efficiently decrease the cost <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

Instead of visualizing a gradient vector in thousands of dimensions, it's more helpful to understand that the magnitude of each component in the gradient vector reveals how sensitive the cost function is to each individual weight and bias <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. For example, if a component associated with a weight is 3.2, and another is 0.1, the cost function is 32 times more sensitive to changes in the first weight <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This means a small change to the more sensitive weight will cause a significantly greater change in cost compared to the same change in a less sensitive weight <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. [[introduction_to_backpropagation | Backpropagation]] is the algorithm specifically designed to compute this complex gradient <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Backpropagation and Adjusting Weights and Biases

The [[backpropagation_algorithm | backpropagation algorithm]] works by determining how a single training example would "nudge" the weights and biases <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. This isn't just about nudging them up or down, but identifying the relative proportions of changes that lead to the most rapid decrease in cost <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Here's an intuitive walkthrough:
1.  **Desired Output Layer Nudges**: For a given training example (e.g., an image of a '2'), the network's output neurons will have certain activation values <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The goal is to nudge these activations towards the target values (e.g., the '2' neuron up, others down) <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The size of these nudges is proportional to how far away each current value is from its target <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
2.  **Influencing a Single Neuron's Activation**: To achieve a desired change in an output neuron's activation, three avenues can be explored:
    *   **Increasing the bias**: Directly adds to the neuron's weighted sum <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   **Increasing the weights**: Weights connected to brighter (more active) neurons in the previous layer have a greater influence on the current neuron's activation and, thus, on the cost function <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. This means changes to these weights yield "more bang for your buck" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   **Changing activations from the previous layer**: If neurons with positive weights get brighter, and those with negative weights get dimmer, the current neuron's activation will change as desired <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. These desired changes are also proportional to the size of the corresponding weights <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
3.  **Propagating Backwards**: The desired changes for a neuron's activation are then added to the desired changes from all other neurons in the same layer <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This combined "desire" is then propagated backward to the preceding layer <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This process recursively applies through the network, moving from the output layer backwards to the input layer, determining how each neuron in a hidden layer should be nudged <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Averaging Desired Changes

The steps above describe how a *single* training example influences the weights and biases <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. To perform a true [[gradient_descent_and_cost_function | gradient descent]] step, this backpropagation routine must be executed for *every* training example, and then all the individual desired changes to weights and biases are averaged together <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This collection of averaged nudges represents the negative gradient of the cost function <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Stochastic Gradient Descent

Calculating the influence of every training example for each [[gradient_descent_and_cost_function | gradient descent]] step is computationally intensive <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. To address this, [[stochastic_gradient_descent | stochastic gradient descent]] (SGD) is commonly used <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

Instead of using all training data, the data is randomly shuffled and divided into mini-batches (e.g., 100 examples per batch) <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Each gradient descent step is then computed based on a single mini-batch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. While this mini-batch gradient is not the true gradient of the entire cost function, it provides a good approximation and significantly speeds up computation <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This approach can be likened to a "drunk man stumbling aimlessly down a hill but taking quick steps" rather than a "carefully calculating man determining the exact downhill direction of each step before taking a very slow and careful step" <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

By repeatedly going through all mini-batches and making these adjustments, the network's parameters converge towards a local minimum of the cost function, leading to improved performance on the training examples <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## Importance of Training Data

For [[gradient_descent_and_cost_function | gradient descent]] and other machine learning algorithms to work effectively, a large amount of training data is crucial <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. For tasks like handwritten digit recognition, the MNIST database provides numerous human-labeled examples <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. A common challenge in machine learning is often acquiring the necessary labeled training data <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.