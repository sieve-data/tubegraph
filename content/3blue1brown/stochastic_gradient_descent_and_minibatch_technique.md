---
title: Stochastic gradient descent and minibatch technique
videoId: Ilg3gGewQ5U
---

From: [[3blue1brown]] <br/> 

[[backpropagation_algorithm_in_neural_networks | Backpropagation]] is an algorithm used by neural networks to learn by determining how to adjust weights and biases to minimize a [[gradient_descent_and_cost_function_minimization | cost function]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The core task involves computing the negative [[introduction_to_gradient_descent | gradient]] of this [[gradient_descent_and_cost_function_minimization | cost function]] to efficiently decrease cost <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## The Challenge of Full Gradient Descent

In principle, the way weights and biases are adjusted for a single [[introduction_to_gradient_descent | gradient descent]] step should depend on every single training example <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. A true [[introduction_to_gradient_descent | gradient descent]] step would involve calculating how every one of tens of thousands of training examples wishes to nudge the weights and biases, and then averaging those desired changes <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

However, in practice, it takes computers an extremely long time to sum up the influence of every training example for each [[introduction_to_gradient_descent | gradient descent]] step <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This computational slowness necessitates a more efficient approach <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## Introduction to Stochastic Gradient Descent (SGD)

To address the computational inefficiency, a commonly adopted technique is **Stochastic [[introduction_to_gradient_descent | Gradient Descent]] (SGD)** <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### The Mini-Batch Technique

Instead of using all training data for each step, the training data is first randomly shuffled <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Then, it is divided into multiple **mini-batches**, for instance, each containing 100 training examples <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Each step of the learning process is then computed based on a single mini-batch <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

### Benefits and Characteristics of SGD

*   **Approximation**: A step computed using a mini-batch is not the actual [[introduction_to_gradient_descent | gradient]] of the total [[gradient_descent_and_cost_function_minimization | cost function]], as the true [[introduction_to_gradient_descent | gradient]] depends on all training data <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. Therefore, it is not the most efficient step downhill <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **Computational Speedup**: Despite being an approximation, each mini-batch provides a "pretty good" approximation of the [[introduction_to_gradient_descent | gradient]] and, more importantly, offers a significant computational speedup <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Trajectory**: If the network's trajectory on the [[gradient_descent_and_cost_function_minimization | cost surface]] were plotted, SGD would resemble a "drunk man stumbling aimlessly down a hill but taking quick steps" <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. This contrasts with the "carefully calculating man determining the exact downhill direction" of full [[introduction_to_gradient_descent | gradient descent]], who takes very slow and careful steps <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

By repeatedly iterating through all mini-batches and making these adjustments, the network will converge towards a local minimum of the [[gradient_descent_and_cost_function_minimization | cost function]] <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, enabling it to perform effectively on training examples <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.