---
title: Importance of training data in machine learning
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

The effectiveness of [[machine_learning_models | machine learning models]], including neural networks, heavily relies on the quantity and quality of training data <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. This is critical for algorithms like backpropagation, which determine how neural networks learn <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Role in Cost Function Minimization
The goal of [[role_of_parameter_tuning_in_machine_learning_models | learning]] in neural networks is to find the weights and biases that minimize a specific cost function <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This cost is calculated by taking the network's output for a training example, comparing it to the desired output, and summing the squares of the differences for each component <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. To get the total cost of the network, this process is performed for tens of thousands of training examples and the results are averaged <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

## Adjusting Weights and Biases
Backpropagation is the algorithm used to compute the complicated gradient of this cost function, which indicates how to adjust weights and biases to efficiently decrease the cost <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a> <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. In principle, the adjustments to weights and biases for a single gradient descent step should depend on every single training example <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

Each individual training example influences how the weights and biases should be adjusted:
*   A single training example suggests specific "nudges" to weights and biases <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a> <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   If a network only considered one example (e.g., an image of a '2'), it would become incentivized to classify all images as that specific digit <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   Therefore, the backpropagation routine must be performed for *every* training example, and the desired changes from each example are then averaged together <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a> <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This collection of averaged nudges approximates the negative gradient of the cost function <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Computational Efficiency and Mini-Batches
While a true gradient descent step requires considering all tens of thousands of training examples, this is computationally very slow <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a> <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. To address this:
*   **Mini-batches**: Training data is randomly shuffled and divided into smaller mini-batches (e.g., 100 examples) <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **Stochastic Gradient Descent**: Each step is computed using a mini-batch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. Although this does not provide the exact gradient for the entire dataset, it offers a good approximation and a significant computational speedup <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a> <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. This technique is known as [[stochastic_gradient_descent | stochastic gradient descent]] <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Convergence**: Repeatedly processing all mini-batches and making adjustments allows the network to converge towards a local minimum of the cost function, leading to effective performance on the training examples <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

## The Need for Labeled Data
A significant challenge in [[training_process_of_large_language_models | machine learning]] is acquiring the necessary *labeled* training data <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. For instance, in [[training_neural_networks_for_handwritten_digit_recognition | handwritten digit recognition]], the MNIST database is valuable because it provides "so many examples that have been labeled by humans" <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This involves having people label tens of thousands of images or other data types, which can be a demanding process <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.