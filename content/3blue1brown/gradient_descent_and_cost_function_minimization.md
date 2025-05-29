---
title: Gradient descent and cost function minimization
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

Neural networks learn by finding specific weights and biases that minimize a chosen cost function <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This process involves understanding the [[cost_function_and_its_role_in_neural_networks | cost function]] and applying [[introduction_to_gradient_descent | gradient descent]] to navigate towards its minimum <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## The Cost Function

The cost function quantifies how well a neural network performs <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
For a single training example, the cost is calculated by:
1.  Taking the network's output and comparing it to the desired output <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
2.  Adding up the squares of the differences between each component of these outputs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

The total cost of the network is the average of these individual costs across all training examples, which can number in the tens of thousands <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Minimizing Cost with Gradient Descent

The primary goal of learning is to find the weights and biases that result in the lowest possible cost <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. [[introduction_to_gradient_descent | Gradient descent]] is the method used to achieve this <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The key element in [[introduction_to_gradient_descent | gradient descent]] is the negative gradient of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This gradient indicates how to change all weights and biases to most efficiently decrease the cost <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

While thinking of the gradient as a direction in a high-dimensional space (e.g., 13,000 dimensions) is difficult to imagine, it can also be understood in terms of sensitivity <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The magnitude of each component of the gradient reveals how [[cost_function_sensitivity_analysis | sensitive]] the [[cost_function_and_its_role_in_neural_networks | cost function]] is to changes in each specific weight and bias <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

For example, if a weight's associated gradient component is 3.2 and another's is 0.1, the cost function is 32 times more sensitive to changes in the first weight <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This means a small change in the first weight will cause a much larger change in the cost than the same change in the second weight <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. [[backpropagation_algorithm_in_neural_networks | Backpropagation]] is the algorithm specifically designed to compute this complex gradient <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Influence of Individual Training Examples

The adjustment of weights and biases in a single [[introduction_to_gradient_descent | gradient descent]] step depends on every training example, as the [[cost_function_and_its_role_in_neural_networks | cost function]] averages the cost per example <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. Each training example "wishes" to nudge the weights and biases in specific ways to reduce its individual cost <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

For instance, if the network is poorly trained on an image of a '2', the output layer might have random activations <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The goal is to nudge the activation for '2' up and others down, with the size of nudges proportional to how far each current value is from its target <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

Adjustments to a neuron's activation can occur via:
*   Increasing its bias <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Increasing its weights <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   Changing activations from the previous layer <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Weights connected to brighter (more active) neurons in the preceding layer have a greater influence on the ultimate [[cost_function_and_its_role_in_neural_networks | cost function]] for that particular training example <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. The most effective changes, those providing the "most bang for your buck," are those proportional to the corresponding weights <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This concept of propagating backward through the network, adding desired effects from each output neuron, allows for the calculation of nudges for previous layers <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Stochastic Gradient Descent and Mini-Batches

While a true [[introduction_to_gradient_descent | gradient descent]] step would involve averaging the desired changes from *all* tens of thousands of training examples, this is computationally very slow <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

To address this, [[stochastic_gradient_descent_and_minibatch_technique | stochastic gradient descent]] (SGD) is commonly employed <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This technique involves:
1.  Randomly shuffling the training data <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
2.  Dividing it into numerous small "mini-batches" (e.g., 100 examples each) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  Computing a [[introduction_to_gradient_descent | gradient descent]] step based on each mini-batch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

Although a mini-batch provides only an approximation of the actual [[cost_function_and_its_role_in_neural_networks | cost function]] gradient (which depends on all data), it offers a significant computational speedup <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This results in a somewhat less direct path down the cost surface but allows for quicker iterative adjustments <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

By repeatedly processing all mini-batches and making these adjustments, the network converges towards a local minimum of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, leading to good performance on the training data <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This entire process relies on having a sufficient amount of labeled training data, such as the MNIST database for handwritten digits <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.