---
title: Stochastic gradient descent
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

[[Stochastic gradient descent]] is a commonly used technique in training neural networks, primarily for its computational efficiency <a class="yt-timestamp" data-t="09:33">[09:33]</a>, especially when compared to calculating the full [[gradient_descent_in_neural_networks | gradient descent]] <a class="yt-timestamp" data-t="10:00">[10:00]</a>.

## How it Works
A true [[gradient_descent_in_neural_networks | gradient descent]] step would involve calculating the average desired changes to weights and biases across all tens of thousands of training examples <a class="yt-timestamp" data-t="11:00">[11:00]</a>. This process is computationally slow <a class="yt-timestamp" data-t="09:33">[09:33]</a>.

Instead, [[Stochastic gradient descent]] proceeds as follows:
1.  **Data Shuffling**: The training data is randomly shuffled <a class="yt-timestamp" data-t="09:45">[09:45]</a>.
2.  **Mini-Batch Creation**: The shuffled data is then divided into numerous mini-batches, typically around 100 training examples each <a class="yt-timestamp" data-t="09:48">[09:48]</a>.
3.  **Step Computation**: A [[gradient_descent_in_neural_networks | gradient descent]] step is computed based on each mini-batch <a class="yt-timestamp" data-t="09:52">[09:52]</a>.

While a mini-batch step is not the actual [[gradient_descent_in_neural_networks | gradient]] of the [[gradient_descent_and_cost_function | cost function]] (as it depends on a tiny subset rather than all training data), it offers a good approximation and significant computational speedup <a class="yt-timestamp" data-t="10:05">[10:05]</a>.

## Analogy
The trajectory of a network using [[Stochastic gradient descent]] can be likened to "a drunk man stumbling aimlessly down a hill but taking quick steps" <a class="yt-timestamp" data-t="10:17">[10:17]</a>. This contrasts with a "carefully calculating man determining the exact downhill direction of each step before taking a very slow and careful step" <a class="yt-timestamp" data-t="10:21">[10:21]</a>, which would represent a full [[gradient_descent_in_neural_networks | gradient descent]].

## Outcome
By repeatedly going through all mini-batches and making these adjustments, the network will converge towards a local minimum of the [[gradient_descent_and_cost_function | cost function]] <a class="yt-timestamp" data-t="11:17">[11:17]</a>. This means the network will eventually perform very well on the training examples <a class="yt-timestamp" data-t="11:21">[11:21]</a>.

### Role of Training Data
For algorithms like [[backpropagation_algorithm | backpropagation]] and [[Stochastic gradient descent]] to work effectively, a large amount of training data is crucial <a class="yt-timestamp" data-t="12:00">[12:00]</a>, <a class="yt-timestamp" data-t="12:04">[12:04]</a>. For example, the MNIST database provides many human-labeled examples for handwritten digit recognition <a class="yt-timestamp" data-t="12:06">[12:06]</a>, <a class="yt-timestamp" data-t="12:10">[12:10]</a>. A common challenge in [[neural_network_learning_process | machine learning]] is acquiring the necessary labeled training data <a class="yt-timestamp" data-t="12:15">[12:15]</a>.