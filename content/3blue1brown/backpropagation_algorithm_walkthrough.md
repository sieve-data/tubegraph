---
title: Backpropagation algorithm walkthrough
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

This article delves into the mathematical underpinnings of the [[backpropagation_algorithm_in_neural_networks | backpropagation algorithm]], focusing on the relevant [[calculus_in_the_context_of_neural_networks | calculus]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. It is assumed that the reader has prior knowledge from an [[intuitive_explanation_of_backpropagation | intuitive walkthrough of the backpropagation algorithm]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

The primary objective is to demonstrate how machine learning practitioners commonly apply the [[chain_rule_application_in_machine_learning | chain rule]] from [[calculus_in_the_context_of_neural_networks | calculus]] within the context of [[neural_network_structure_and_layers | neural networks]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

> "It's normal for this to be at least a little confusing, so the mantra to regularly pause and ponder certainly applies as much here as anywhere else." <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>

## Simple Network Example (Single Neuron Per Layer)

To begin, consider an extremely simple [[neural_network_structure_and_layers | network]] where each layer contains only a single neuron <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This [[neural_network_structure_and_layers | network]] is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The goal is to understand how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to these variables <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This understanding helps determine which adjustments to these terms will most efficiently decrease the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Focusing on the connection between the last two neurons:
*   The activation of the last neuron is denoted `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   The activation of the previous neuron is `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   The desired value for the last activation for a given training example is `y` (e.g., 0 or 1) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   The [[cost_function_and_its_role_in_neural_networks | cost]] for a single training example, `C0`, is `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

The last activation `a(L)` is determined by:
*   A weight `w(L)` multiplied by the previous neuron's activation `a(L-1)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   Plus a bias `b(L)` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   This sum is then passed through a non-linear activation function (e.g., sigmoid or ReLU) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

For simplicity, the weighted sum `(w(L) * a(L-1) + b(L))` is given a special name, `z(L)` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
The conceptual flow is: `w`, `a(L-1)`, and `b` compute `z` -> `a` -> `C` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Derivative of Cost with Respect to Weight `w(L)`

The first goal is to understand the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to small changes in `w(L)` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, which is expressed as the derivative of `C` with respect to `w(L)` <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

*   `del w` signifies a tiny nudge to `W` (e.g., 0.01) <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   `del C` signifies the resulting nudge to the [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   The desired output is their ratio: `del C / del w` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

Conceptually, a tiny nudge to `w(L)` causes a nudge to `z(L)`, which in turn causes a nudge to `a(L)`, directly influencing the [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This relationship can be broken down using the [[chain_rule_application_in_machine_learning | chain rule]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>:

`dC/dw(L) = (dC/da(L)) * (da(L)/dz(L)) * (dz(L)/dw(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's compute the relevant derivatives:

1.  **`dC/da(L)`**: This derivative works out to be `2(a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Its size is proportional to the difference between the [[neural_network_structure_and_layers | network]]'s output and the desired output, meaning large differences lead to a big impact on the final [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **`da(L)/dz(L)`**: This is simply the derivative of the chosen activation function (e.g., sigmoid) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
3.  **`dz(L)/dw(L)`**: This derivative comes out to be `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This means the influence of a small nudge to the weight on the last layer depends on the strength (activation) of the previous neuron <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

This derivative is for the [[cost_function_and_its_role_in_neural_networks | cost]] of a single training example <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. The derivative for the full [[cost_function_and_its_role_in_neural_networks | cost function]] involves averaging this expression over all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This is one component of the [[understanding_gradients_in_backpropagation | gradient vector]] <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Sensitivity to Bias `b(L)`

The sensitivity to the bias `b(L)` is almost identical to that of the weight <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The only change is replacing `del z / del w` with `del z / del b` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This derivative, `dz(L)/db(L)`, is simply `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Sensitivity to Previous Layer Activation `a(L-1)`

The [[backpropagation_algorithm_in_neural_networks | idea of propagating backwards]] comes into play when looking at how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to the activation of the previous layer <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. The initial derivative in the [[chain_rule_application_in_machine_learning | chain rule]] expression, `dz(L)/da(L-1)`, comes out to be the weight `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Although this previous layer activation cannot be directly influenced, keeping track of this sensitivity allows for iterating the same [[chain_rule_application_in_machine_learning | chain rule]] idea backwards to determine the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to even earlier weights and biases <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Generalizing to Multiple Neurons Per Layer

When expanding the [[neural_network_structure_and_layers | network]] to include multiple neurons per layer, the complexity does not increase exponentially <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The main change involves keeping track of a few more indices <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

*   The activation of a given layer `a(L)` will now have a subscript `j` indicating which neuron of that layer it is: `a(L)j` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   `k` indexes layer `L-1`, and `j` indexes layer `L` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   The [[cost_function_and_its_role_in_neural_networks | cost]] is now the sum of the squares of the differences between the last layer activations `a(L)j` and their desired outputs `yj`: `sum((a(L)j - yj)^2)` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Weights are indexed `w(L)jk`, representing the weight of the edge connecting the `k`th neuron in layer `L-1` to the `j`th neuron in layer `L` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   `z` continues to represent the weighted sum, and `a` is still the result of applying the activation function to `z` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

Crucially, the [[chain_rule_application_in_machine_learning | chain-ruled derivative expression]] describing how sensitive the [[cost_function_and_its_role_in_neural_networks | cost]] is to a specific weight remains essentially the same <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

What changes is the derivative of the [[cost_function_and_its_role_in_neural_networks | cost]] with respect to an activation in the layer `L-1` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. This is because a neuron in `L-1` influences the [[cost_function_and_its_role_in_neural_networks | cost function]] through multiple different paths, impacting multiple neurons in layer `L` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Therefore, these influences must be summed up <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

## Conclusion

Understanding these [[chain_rule_application_in_machine_learning | chain rule]] expressions is key to looking deep into the heart of [[backpropagation_algorithm_in_neural_networks | backpropagation]], the workhorse behind how [[neural_network_structure_and_layers | neural networks]] learn <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. These expressions provide the derivatives that determine each component in the [[understanding_gradients_in_backpropagation | gradient]] that helps minimize the [[cost_function_and_its_role_in_neural_networks | cost]] of the [[neural_network_structure_and_layers | network]] by repeatedly [[introduction_to_gradient_descent | stepping downhill]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Given the multiple layers of complexity, it is normal for this information to take time to digest <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.