---
title: sensitivity of cost function
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

Understanding the sensitivity of the [[gradient_descent_and_cost_function | cost function]] to various parameters is a fundamental goal in [[calculus_in_neural_networks | neural networks]], particularly when using the backpropagation algorithm <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This analysis leverages [[computing_derivatives_of_functions | calculus]], specifically the chain rule, to determine how adjustments to terms like weights and biases can efficiently decrease the cost <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The approach to the chain rule in machine learning differs from typical introductory [[computing_derivatives_of_functions | calculus]] courses <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Analyzing a Simple Network

To begin, consider an extremely simple neural network where each layer contains a single neuron <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The objective is to understand how sensitive the [[gradient_descent_and_cost_function | cost function]] is to these variables <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

We focus on the connection between the last two neurons <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   The activation of the last neuron is denoted `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The desired output for a given training example is `y` (e.g., 0 or 1) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

For a single training example, the cost `C0` is defined as `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
The last activation `a(L)` is determined by: `a(L) = f(w(L) * a(L-1) + b(L))`, where `f` is a nonlinear function like sigmoid or ReLU <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. The weighted sum `w(L) * a(L-1) + b(L)` is often given a special name, `z(L)` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This implies a computational flow: weights, previous activation, and bias compute `z`, which computes `a`, which then, with `y`, computes the cost <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

### Derivative of Cost with Respect to Weight (`w(L)`)

The primary goal is to determine the sensitivity of the [[gradient_descent_and_cost_function | cost function]] `C` to small changes in the weight `w(L)`, expressed as the [[computing_derivatives_of_functions | derivative]] `dC/dw(L)` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Conceptually, a tiny nudge (`del w`) to `w(L)` causes a nudge to `z(L)`, which causes a nudge to `a(L)`, which directly influences the cost (`del C`) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This relationship is broken down using the chain rule <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>:

`dC/dw(L) = (dC/da(L)) * (da(L)/dz(L)) * (dz(L)/dw(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's [[computing_derivatives_of_functions | compute the relevant derivatives]]:
*   `dC/da(L)`: For `C = (a(L) - y)^2`, the [[computing_derivatives_of_functions | derivative]] is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This means the impact on cost is proportional to the difference between the network's output and the desired output <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   `da(L)/dz(L)`: This is the [[computing_derivatives_of_functions | derivative]] of the activation function (e.g., sigmoid prime) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   `dz(L)/dw(L)`: For `z(L) = w(L) * a(L-1) + b(L)`, the [[computing_derivatives_of_functions | derivative]] with respect to `w(L)` is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This implies that the influence of a small change in `w(L)` on the last layer depends on the strength of the previous neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

This specific derivative is for a single training example <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The full [[gradient_descent_and_cost_function | cost function]] involves averaging across many training examples, so its derivative requires averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This forms one component of the [[gradient_descent_and_cost_function | gradient vector]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Derivative of Cost with Respect to Bias (`b(L)`)

The sensitivity to the bias `b(L)` is almost identical <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The only change in the chain rule expression is replacing `dz(L)/dw(L)` with `dz(L)/db(L)`. Given `z(L) = w(L) * a(L-1) + b(L)`, the [[computing_derivatives_of_functions | derivative]] `dz(L)/db(L)` is `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Derivative of Cost with Respect to Previous Activation (`a(L-1)`)

The chain rule also reveals how sensitive the [[gradient_descent_and_cost_function | cost function]] is to the activation of the previous layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The sensitivity of `z(L)` to `a(L-1)` (i.e., `dz(L)/da(L-1)`) is the weight `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Although this previous layer activation cannot be directly influenced, keeping track of this sensitivity allows for iterating the chain rule backwards to determine the sensitivity of the cost function to even earlier weights and biases <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Analyzing a Complex Network

For networks with multiple neurons per layer, the core principles remain largely the same, requiring only a few more indices to track <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   An activation in a given layer `L` also includes a subscript for the specific neuron, e.g., `a(L)j` for the `j`-th neuron <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   Weights are indexed to indicate the connection between neuron `k` in layer `L-1` and neuron `j` in layer `L`, as `w(L)jk` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

The [[gradient_descent_and_cost_function | cost function]] for multiple neurons sums the squares of the differences between each last-layer activation and its desired output: `Sum_j (a(L)j - yj)^2` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
The weighted sum `z` for a specific neuron `j` in layer `L` (`z(L)j`) is still fed into the activation function to get `a(L)j` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

The chain-ruled derivative expression for the sensitivity of the cost to a specific weight `w(L)jk` looks essentially the same as in the single-neuron case <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The key difference arises when computing the [[computing_derivatives_of_functions | derivative]] of the cost with respect to an activation in a *previous* layer, like `a(L-1)k` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Since a single neuron in layer `L-1` can influence multiple neurons in layer `L`, it affects the [[gradient_descent_and_cost_function | cost function]] through multiple different paths <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. These influences must be summed up to get the total sensitivity <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

## Conclusion

These chain rule expressions provide the derivatives that determine each component in the [[gradient_descent_and_cost_function | gradient]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This [[gradient_descent_and_cost_function | gradient]] helps minimize the network's cost by repeatedly stepping downhill, a process known as [[gradient_descent_and_cost_function | gradient descent]] <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This intricate application of [[computing_derivatives_of_functions | calculus]] is at the heart of how [[calculus_in_neural_networks | neural networks]] learn <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.