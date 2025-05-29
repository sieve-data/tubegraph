---
title: chain rule in backpropagation
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

This article provides a formal dive into the calculus relevant to the [[backpropagation_algorithm | backpropagation algorithm]], assuming a prior understanding of its intuitive walkthrough <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The primary objective is to explain how the [[chain_rule_in_differentiation | chain rule]] from [[calculus in neural networks | calculus]] is commonly applied within the context of [[backpropagation_algorithm | neural networks]], which differs from typical introductory [[calculus in neural networks | calculus]] approaches <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Understanding Cost Function Sensitivity

The goal of [[backpropagation_algorithm | backpropagation]] is to determine how sensitive the cost function is to various parameters (weights and biases) within a neural network <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This sensitivity guides adjustments that efficiently decrease the cost function <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Simplified Network Example (Single Neuron Per Layer)

Consider an extremely simple network where each layer contains a single neuron <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Focusing on the connection between the last two neurons:

*   **Activation of the last neuron:** `a(L)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   **Activation of the previous neuron:** `a(L-1)` <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   **Desired output for a training example:** `y` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>

The cost `C0` for a single training example is defined as `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

The last activation `a(L)` is determined by a weighted sum `z(L)` passed through a nonlinear [[activation_functions_in_neural_networks | activation function]] (e.g., [[activation_functions_in_neural_networks | sigmoid]] or ReLU) <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>:
`z(L) = w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
`a(L) = f(z(L))` (where `f` is the [[activation_functions_in_neural_networks | activation function]]) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>

Conceptually, the weight `w(L)`, previous activation `a(L-1)`, and bias `b(L)` compute `z(L)`, which computes `a(L)`, which then, with `y`, computes the cost `C` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Applying the [[chain_rule_in_differentiation | Chain Rule]] for Weights

Our first goal is to understand the derivative of `C` with respect to `w(L)` (`dC/dw(L)`) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. A tiny change to `w(L)` causes a nudge to `z(L)`, which nudges `a(L)`, directly influencing `C` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The [[chain_rule_in_differentiation | chain rule]] states that `dC/dw(L)` can be broken down as follows <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>:
`dC/dw(L) = (dC/da(L)) * (da(L)/dz(L)) * (dz(L)/dw(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's compute each component [[derivatives in neural networks | derivative]]:
1.  **`dC/da(L)`:** This is the derivative of `(a(L) - y)^2` with respect to `a(L)`.
    `dC/da(L) = 2(a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>
    > [!NOTE]
    > The size of this derivative is proportional to the difference between the network's output and the desired output, meaning larger differences imply greater impact on cost from slight changes in output <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

2.  **`da(L)/dz(L)`:** This is the derivative of the [[activation_functions_in_neural_networks | activation function]] (e.g., [[activation_functions_in_neural_networks | sigmoid]]) with respect to `z(L)`.
    `da(L)/dz(L) = f'(z(L))` (where `f'` is the derivative of the [[activation_functions_in_neural_networks | activation function]]) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>

3.  **`dz(L)/dw(L)`:** This is the derivative of `w(L) * a(L-1) + b(L)` with respect to `w(L)`.
    `dz(L)/dw(L) = a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>
    > [!NOTE]
    > This derivative indicates that the influence of a small nudge to the weight `w(L)` on the last layer depends on how strong (activated) the previous neuron `a(L-1)` is <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Applying the [[chain_rule_in_differentiation | Chain Rule]] for Biases

The sensitivity to the bias `b(L)` is almost identical to the weight, only changing the last term in the [[chain_rule_in_differentiation | chain rule]] expression <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>:
`dC/db(L) = (dC/da(L)) * (da(L)/dz(L)) * (dz(L)/db(L))` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>

The derivative of `z(L)` with respect to `b(L)` is `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

### Propagating Backwards

The concept of "propagating backwards" comes from seeing how sensitive the cost function `C` is to the activation of the previous layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
The sensitivity of `z(L)` to `a(L-1)` is `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows for iterating the same [[chain_rule_in_differentiation | chain rule]] idea backwards to find sensitivities for previous weights and biases <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Generalizing to Multiple Neurons Per Layer

While the single-neuron example simplifies the concept, applying the [[chain_rule_in_differentiation | chain rule]] to networks with multiple neurons per layer doesn't change the fundamental approach significantly; it primarily involves managing more indices <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

*   **Activation Notation:** Activations now include a subscript indicating the specific neuron in a layer, e.g., `a(L)j` for the `j`-th neuron in layer `L` <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   **Cost Function:** The cost `C` is the sum of the squared differences between all last-layer activations and their desired outputs <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>:
    `C = Σj (a(L)j - yj)^2` <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>
*   **Weight Notation:** Weights require additional indices to track connections, e.g., `w(L)jk` for the weight from the `k`-th neuron in layer `L-1` to the `j`-th neuron in layer `L` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Weighted Sum:** `z(L)j` is still the weighted sum for neuron `j` in layer `L` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

The [[chain_rule_in_differentiation | chain-ruled derivative]] expression for how sensitive the cost is to a specific weight remains essentially the same <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Key Change: Influence of Previous Layer Activations

The main difference emerges when computing the derivative of the cost with respect to an activation in a previous layer (e.g., `a(L-1)k`). This neuron `k` influences the cost function through *multiple* paths, as it connects to several neurons in the subsequent layer (e.g., `a(L)0`, `a(L)1`, etc.) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Therefore, the total influence is found by summing up the influences through each path, using the [[sum_rule_for_derivatives | sum rule]] for [[derivatives in neural networks | derivatives]] <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Once the sensitivity of the cost function to activations in the second-to-last layer is known, the process can be repeated for all weights and biases feeding into that layer, propagating the derivatives backwards through the network <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Conclusion

The [[chain_rule_in_differentiation | chain rule]] expressions form the core of [[backpropagation_algorithm | backpropagation]], providing the [[derivatives in neural networks | derivatives]] needed to determine each component in the gradient vector <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This gradient enables the network to minimize its cost by iteratively stepping "downhill" in the cost landscape <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Understanding this application of the [[chain_rule_in_differentiation | chain rule]] is central to comprehending how [[introduction_to_backpropagation | neural networks learn]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.