---
title: backpropagation algorithm
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

This article provides a formal exploration into the [[calculus in neural networks | calculus]] relevant to the [[backpropagation_algorithm | backpropagation algorithm]], building upon an intuitive understanding. The primary objective is to illustrate how machine learning professionals conceptualize the [[chain rule in backpropagation | chain rule]] within the context of neural networks, which differs from traditional introductory [[calculus in neural networks | calculus]] approaches <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Simple Network Example

To begin, consider an extremely simple neural network where each layer contains a single neuron <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The main goal is to understand how sensitive the [[gradient_descent_and_cost_function | cost function]] is to these variables, which informs adjustments for efficient cost reduction <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

For this example, the focus is on the connection between the last two neurons <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   The activation of the last neuron is `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The desired output for a given training example is `y` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The cost for a single training example, denoted `C0`, is calculated as `(a(L) - y) squared` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The last activation `a(L)` is determined by:
`z(L) = w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
Then, `a(L)` is derived by applying a special nonlinear function (e.g., sigmoid or ReLU) to `z(L)` <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This means `w(L)`, `a(L-1)`, and `b(L)` compute `z(L)`, which computes `a(L)`, which, along with `y`, computes the cost <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Sensitivity of Cost to Weight `w(L)`

The primary goal is to understand the sensitivity of the [[gradient_descent_and_cost_function | cost function]] (`C`) to small changes in the weight `w(L)`, or the derivative of `C` with respect to `w(L)` (`∂C/∂w(L)`) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

A small nudge to `w(L)` (`∂w`) causes a nudge to `z(L)`, which nudges `a(L)`, directly influencing the cost `C` (`∂C`) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>, <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The ratio of `∂C` to `∂w` is desired <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

This relationship is broken down using the [[chain rule in backpropagation | chain rule]]:
`∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

Let's compute these [[derivatives in neural networks | derivatives]]:
1.  **`∂C/∂a(L)`**: This derivative is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>, <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Its size is proportional to the difference between the network's output and the desired output <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **`∂a(L)/∂z(L)`**: This is the derivative of the chosen nonlinearity (e.g., sigmoid function) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **`∂z(L)/∂w(L)`**: This derivative is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This indicates that the influence of a small nudge to the weight on the last layer depends on the strength of the previous neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

This derived sensitivity is for a single training example <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The full [[gradient_descent_and_cost_function | cost function]] involves averaging these costs across many training examples, so its derivative requires averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

## Expanding to Biases and Previous Layers

### Sensitivity to Bias `b(L)`

The sensitivity of the [[gradient_descent_and_cost_function | cost function]] to the bias `b(L)` is very similar <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. The [[chain rule in backpropagation | chain rule]] expression changes only in the last term:
`∂C/∂b(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂b(L))` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>, <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
The derivative `∂z(L)/∂b(L)` evaluates to `1` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Propagating Backwards

The core idea of propagating backwards in [[backpropagation_algorithm | backpropagation]] comes from understanding the sensitivity of the [[gradient_descent_and_cost_function | cost function]] to the activation of the *previous* layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

`∂C/∂a(L-1) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂a(L-1))` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
Here, `∂z(L)/∂a(L-1)` comes out to be the weight `w(L)` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>, <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

While `a(L-1)` cannot be directly influenced, understanding this sensitivity is crucial because it allows the iteration of the same [[chain rule in backpropagation | chain rule]] idea backwards to determine the sensitivity of the [[gradient_descent_and_cost_function | cost function]] to even earlier weights and biases <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>, <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>, <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Multi-Neuron Layers

When layers contain multiple neurons, the complexity does not increase exponentially <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. It primarily involves tracking a few more indices <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

*   An activation in a given layer `L` now includes a subscript `j` to indicate which neuron it is (e.g., `a(L)j`) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>, <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   For the cost, the squared differences between the last layer activations and the desired outputs are summed: `Σ(a(L)j - yj)²` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Weights require additional indices. A weight connecting the `k`th neuron in layer `L-1` to the `j`th neuron in layer `L` is denoted `w(L)jk` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   The weighted sum `z` for a specific neuron `j` in layer `L` is `z(L)j = Σk (w(L)jk * a(L-1)k) + b(L)j` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>, <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

The fundamental equations and the [[chain rule in backpropagation | chain rule]] derivative expressions remain largely the same conceptually, just with added indices <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

What changes is the derivative of the [[gradient_descent_and_cost_function | cost function]] with respect to an activation in layer `L-1` (e.g., `a(L-1)k`). This is because a neuron in `L-1` influences the [[gradient_descent_and_cost_function | cost function]] through multiple paths in layer `L` (e.g., `a(L)0`, `a(L)1`, etc.), and these influences must be summed up <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Once the sensitivity of the [[gradient_descent_and_cost_function | cost function]] to activations in the second-to-last layer is known, the process can be repeated for all weights and biases feeding into that layer <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>, <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. These [[chain rule in backpropagation | chain rule]] expressions provide the [[derivatives in neural networks | derivatives]] that define each component of the gradient vector, which is used to minimize the network's cost by repeatedly stepping downhill in the [[neural network learning process | learning process]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>, <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.