---
title: derivatives in neural networks
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 
The article delves into the [[calculus_in_neural_networks | calculus]] involved in understanding [[Gradient descent in neural networks | backpropagation]], emphasizing the use of the chain rule in the context of neural networks <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The primary goal is to determine the sensitivity of the cost function to network variables, such as weights and biases, to facilitate efficient adjustments for minimizing cost <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Simplified Neural Network: Single Neuron per Layer

To illustrate, a very simple network where each [[Structure of neural networks | layer]] contains a single neuron is considered <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

The focus is on the connection between the last two neurons.
*   The activation of the last neuron is denoted `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The desired output for a given training example is `y` (e.g., 0 or 1) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The cost for a single training example, `C0`, is defined as `(a(L) - y) squared` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The activation `a(L)` is computed from a weighted sum, `z(L)`, passed through a non-linear [[activation_functions_in_neural_networks | activation function]] (e.g., sigmoid or ReLU) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. `z(L)` is `w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

Conceptually, the process flows from `w(L)`, `a(L-1)`, and `b(L)` computing `z(L)`, which computes `a(L)`, which, with `y`, computes the cost `C` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Applying the Chain Rule

The primary goal is to determine the derivative of the cost `C` with respect to the weight `w(L)`, expressed as `dC/dw(L)` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. This represents the sensitivity of the cost function to small changes in `w(L)` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

The chain rule is applied because a small change in `w(L)` causes a change in `z(L)`, which in turn causes a change in `a(L)`, directly influencing the cost <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The derivative is broken down as follows:
`dC/dw(L) = (dC/da(L)) * (da(L)/dz(L)) * (dz(L)/dw(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

#### Component Derivatives:

1.  **`dC/da(L)`:** This derivative is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   Its magnitude is proportional to the difference between the network's output and the desired target (`y`), indicating that larger discrepancies lead to a greater impact of changes on the cost <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

2.  **`da(L)/dz(L)`:** This is the derivative of the chosen [[activation_functions_in_neural_networks | activation function]] (e.g., sigmoid prime) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

3.  **`dz(L)/dw(L)`:** This derivative is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   This implies that the influence of a small change in the weight `w(L)` on the last layer depends on the strength (activation) of the previous neuron `a(L-1)` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

The derivative calculated above is for a single training example <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>, <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The full cost function's derivative requires averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This derivative is one component of the [[Gradient descent in neural networks | gradient vector]], which is built from partial derivatives with respect to all weights and biases <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

#### Sensitivity to Bias

The sensitivity of the cost function to the bias `b(L)` is almost identical to that of the weight, with the `dz(L)/dw(L)` term replaced by `dz(L)/db(L)` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This derivative, `dz(L)/db(L)`, evaluates to `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

#### Propagating Backwards

The sensitivity of the cost function to the activation of the previous layer, `a(L-1)`, is also important. The derivative `dz(L)/da(L-1)` evaluates to `w(L)` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>, <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows the chain rule process to be iterated backwards through the network to determine the sensitivity of the cost function to previous weights and biases, which is the core of [[Gradient descent in neural networks | backpropagation]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>, <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Neural Networks with Multiple Neurons per Layer

While the single-neuron example is simple, the principles extend to networks with multiple neurons per layer without exponential complexity, mainly adding more indices to track <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>, <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

*   Activations now have a subscript indicating the neuron within a layer (e.g., `a(L)j` for the `j`-th neuron in layer `L`) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>, <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   Weights connect specific neurons (e.g., `w(L)jk` connects neuron `k` in layer `L-1` to neuron `j` in layer `L`) <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>, <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.
*   The cost function for multiple neurons sums the squared differences: `Sum over j of (a(L)j - yj) squared` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   The chain-ruled derivative expression for cost sensitivity to a specific weight remains essentially the same <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

A key difference arises when calculating the derivative of the cost with respect to an activation in a previous layer (`L-1`):
*   A neuron in layer `L-1` influences the cost function through multiple paths, as it connects to multiple neurons in layer `L` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   The total influence is the sum of the influences through each of these paths <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Understanding these chain rule expressions provides the derivatives needed for each component of the [[Gradient descent in neural networks | gradient]] vector, which guides the network in repeatedly stepping downhill to minimize its cost <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.