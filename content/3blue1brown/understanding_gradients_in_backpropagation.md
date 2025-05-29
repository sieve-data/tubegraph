---
title: Understanding gradients in backpropagation
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

This article provides a formal dive into the calculus relevant for understanding the [[backpropagation_algorithm_in_neural_networks|backpropagation algorithm]], assuming familiarity with its [[intuitive_explanation_of_backpropagation|intuitive walkthrough]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The primary goal is to illustrate how the [[calculus_in_the_context_of_neural_networks|chain rule]] is commonly applied in machine learning for neural networks, which differs from traditional introductory [[calculus_in_the_context_of_neural_networks|calculus]] courses <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Simple Network: Single Neuron Per Layer

Consider a very simple network where each layer contains only a single neuron <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The objective is to determine how sensitive the [[cost_function_and_its_role_in_neural_networks|cost function]] is to these variables <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, which informs the most efficient adjustments for reducing the [[cost_function_and_its_role_in_neural_networks|cost function]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Focusing on the connection between the last two neurons:
*   The activation of the last neuron is denoted as a(L) <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is a(L-1) <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The desired value for the last activation (y) for a given training example, e.g., 0 or 1 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The [[cost_function_and_its_role_in_neural_networks|cost]] for a single training example (C0) is defined as (a(L) - y)^2 <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

The last activation, a(L), is derived from a weighted sum `z(L)` and a non-linear activation function (like sigmoid or ReLU) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The weighted sum `z(L)` is calculated as `w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

Conceptually, the weight (w), previous activation (a(L-1)), and bias (b) compute `z`, which computes `a`, which, with constant `y`, computes the [[cost_function_and_its_role_in_neural_networks|cost]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Sensitivity of Cost to Weight w(L)

The first goal is to understand how sensitive the [[cost_function_and_its_role_in_neural_networks|cost function]] is to small changes in weight w(L), which means finding the derivative of C with respect to w(L) <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

A tiny nudge to w(L) causes a nudge to z(L), which causes a nudge to a(L), directly influencing the [[cost_function_and_its_role_in_neural_networks|cost]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This breakdown is expressed using the [[calculus_in_the_context_of_neural_networks|chain rule]]:

∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L)) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's compute the individual derivatives:

*   **∂C/∂a(L)**: This derivative is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Its size is proportional to the difference between the network's output and the desired output, implying that large differences mean even slight changes can significantly impact the [[cost_function_and_its_role_in_neural_networks|cost]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **∂a(L)/∂z(L)**: This is the derivative of the chosen non-linear activation function (e.g., sigmoid) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **∂z(L)/∂w(L)**: This derivative works out to be `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This means the influence of a small nudge to the weight on the last layer depends on the strength (activation) of the previous neuron <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Sensitivity of Cost to Bias b(L)

The sensitivity to the bias b(L) is very similar <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The relevant formula involves changing the `∂z(L)/∂w(L)` term to `∂z(L)/∂b(L)`, which evaluates to `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Propagating Backwards: Sensitivity to Previous Layer Activation a(L-1)

To continue the [[backpropagation_algorithm_walkthrough|backwards propagation]], it's crucial to understand how sensitive the [[cost_function_and_its_role_in_neural_networks|cost function]] is to the activation of the previous layer, a(L-1) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The initial derivative in the chain rule expression, `∂z(L)/∂a(L-1)`, comes out to be `w(L)` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. Even though the previous layer activation cannot be directly influenced, keeping track of this sensitivity allows for iterating the same [[calculus_in_the_context_of_neural_networks|chain rule]] idea backwards through the network to determine sensitivity to earlier weights and biases <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

These derivatives are for the [[cost_function_and_its_role_in_neural_networks|cost]] of a *single* training example <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The full [[cost_function_and_its_role_in_neural_networks|cost function]] involves averaging these costs across many training examples, so its derivative requires averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This then forms a component of the gradient vector, which consists of partial derivatives of the [[cost_function_and_its_role_in_neural_networks|cost function]] with respect to all weights and biases <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

## Complex Network: Multiple Neurons Per Layer

When layers contain multiple neurons, the complexity does not increase exponentially but mainly involves keeping track of more indices <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

*   An activation for a given layer L will have a subscript `j` to indicate which neuron it is: a(L)j <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   Layer (L-1) neurons are indexed with `k`, and layer L neurons with `j` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   The [[cost_function_and_its_role_in_neural_networks|cost function]] for multiple neurons sums the squares of the differences between the last layer activations and their desired outputs: Σ (a(L)j - yj)^2 <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   Weights gain more indices, such as w(L)jk for the weight connecting the kth neuron in layer (L-1) to the jth neuron in layer L <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   The weighted sum `z` for a specific neuron `j` in layer L becomes `z(L)j`.

The [[calculus_in_the_context_of_neural_networks|chain-ruled derivative]] expression for the sensitivity of the [[cost_function_and_its_role_in_neural_networks|cost]] to a specific weight (e.g., w(L)jk) remains conceptually the same <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

However, the derivative of the [[cost_function_and_its_role_in_neural_networks|cost]] with respect to one of the activations in layer (L-1) changes. A neuron in layer (L-1) influences the [[cost_function_and_its_role_in_neural_networks|cost function]] through *multiple* different paths (i.e., through all neurons in layer L that it connects to) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Therefore, the influences through each path must be added up <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Once the sensitivity of the [[cost_function_and_its_role_in_neural_networks|cost function]] to the activations in the second-to-last layer is known, this process can be repeated for all weights and biases feeding into that layer, propagating the calculations backward through the network <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

These [[calculus_in_the_context_of_neural_networks|chain rule]] expressions provide the derivatives that determine each component in the gradient vector. This gradient then guides the network's learning process by enabling it to repeatedly step downhill to minimize the [[cost_function_and_its_role_in_neural_networks|cost]] using [[gradient_descent_and_cost_function_minimi_zation|gradient descent]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.