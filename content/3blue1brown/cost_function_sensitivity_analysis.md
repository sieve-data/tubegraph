---
title: Cost function sensitivity analysis
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 
## Cost Function Sensitivity Analysis in Neural Networks

This article formalizes the concepts behind the backpropagation algorithm, focusing on the relevant calculus required to understand how a neural network's [[cost_function_and_its_role_in_neural_networks | cost function]] responds to changes in its parameters <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The primary goal is to illustrate how the chain rule is applied in machine learning for network contexts, which differs from typical introductory calculus approaches <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

### Analyzing a Simple Network

To begin, consider an extremely simple neural network where each layer contains only a single neuron <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The objective is to understand how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to these variables, which helps in making adjustments that most efficiently decrease the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

Focusing on the connection between the last two neurons:
*   The activation of the last neuron is denoted `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   These superscripts `L` and `L-1` are indices for layers, not exponents <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   For a given training example, the desired output for the last activation is `y` (e.g., 0 or 1) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   The cost of this network for a single training example (`C0`) is defined as `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   The last activation `a(L)` is determined by a weight `w(L)` times the previous neuron's activation `a(L-1)`, plus a bias `b(L)`, all passed through a non-linear function like sigmoid or ReLU <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   The weighted sum `w(L) * a(L-1) + b(L)` is often named `z(L)` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

The flow of computation is: `w`, `a(L-1)`, and `b` compute `z` $\rightarrow$ `a` $\rightarrow$ `C` (cost) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

#### Sensitivity to Weight `w(L)`

The primary goal is to understand how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] `C` is to small changes in the weight `w(L)`, which is expressed as the derivative `∂C/∂w(L)` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Conceptually, a tiny nudge to `w(L)` causes a nudge to `z(L)`, which nudges `a(L)`, which directly influences the cost `C` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This relationship is calculated using the chain rule <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>:

`∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's compute each component derivative:
1.  **`∂C/∂a(L)`**: Given `C = (a(L) - y)^2`, the derivative with respect to `a(L)` is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
    *   This derivative's size is proportional to the difference between the network's output and the desired output. A large difference means even slight changes can significantly impact the final cost <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **`∂a(L)/∂z(L)`**: This is the derivative of the chosen non-linearity (e.g., sigmoid or ReLU) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
3.  **`∂z(L)/∂w(L)`**: Given `z(L) = w(L) * a(L-1) + b(L)`, the derivative with respect to `w(L)` is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
    *   This implies that the influence of a small nudge to the weight on the last layer depends on the strength of the previous neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

This derivative `∂C/∂w(L)` is for a single training example <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The derivative for the full [[cost_function_and_its_role_in_neural_networks | cost function]], which averages costs across many examples, requires averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This expression forms one component of the gradient vector used in [[gradient_descent_and_cost_function_minimization | gradient descent]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

#### Sensitivity to Bias `b(L)`

The sensitivity to the bias `b(L)` is nearly identical to that of the weight <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The only change in the chain rule expression is replacing `∂z(L)/∂w(L)` with `∂z(L)/∂b(L)` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   Given `z(L) = w(L) * a(L-1) + b(L)`, the derivative `∂z(L)/∂b(L)` is `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

#### Propagating Backwards

The backpropagation concept comes from observing how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to the activation of the previous layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   The initial derivative in the chain rule expression, `∂z(L)/∂a(L-1)`, comes out to be the weight `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   Although `a(L-1)` cannot be directly influenced, understanding this sensitivity allows for iterating the same chain rule idea backward through the network to determine the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to previous weights and biases <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Networks with Multiple Neurons per Layer

While the previous example was simple, the principles extend to networks with multiple neurons per layer without exponential complication <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   Instead of `a(L)`, the activation of a given layer will have a subscript `j` indicating the specific neuron: `a(L)j` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   For the last layer, the [[cost_function_and_its_role_in_neural_networks | cost function]] sums the squares of the differences between each last layer activation and its desired output: `Σ(a(L)j - yj)^2` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Weights require multiple indices to track connections between specific neurons. A weight connecting the `k`th neuron in layer `L-1` to the `j`th neuron in layer `L` is denoted `w(L)jk` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   The weighted sum `z(L)j` for a specific neuron `j` is computed as `Σk (w(L)jk * a(L-1)k) + b(L)j` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   The activation `a(L)j` is still the non-linear function applied to `z(L)j` <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

The chain-ruled derivative expression for the sensitivity of the cost to a specific weight `w(L)jk` remains essentially the same in structure <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>:

`∂C/∂w(L)jk = (∂C/∂a(L)j) * (∂a(L)j/∂z(L)j) * (∂z(L)j/∂w(L)jk)`

What changes is the derivative of the cost with respect to an activation in the previous layer, `a(L-1)k` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   A neuron in layer `L-1` influences the [[cost_function_and_its_role_in_neural_networks | cost function]] through multiple paths, as it connects to multiple neurons in layer `L` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   Therefore, the influences from all these paths must be summed up to find the total sensitivity <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Once the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to the activations in a given layer (e.g., the second-to-last layer) is known, this process can be repeated for all weights and biases feeding into that layer, propagating backward through the entire network <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

These chain rule expressions provide the [[derivatives_of_simple_functions_and_their_intuition | derivatives]] that define each component of the gradient vector <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This gradient then guides the network to minimize its [[cost_function_and_its_role_in_neural_networks | cost function]] by repeatedly stepping "downhill" through [[gradient_descent_and_cost_function_minimization | gradient descent]] <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Understanding this process is central to comprehending how neural networks learn <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.