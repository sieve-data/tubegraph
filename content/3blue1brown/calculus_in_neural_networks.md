---
title: calculus in neural networks
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

Understanding the role of [[introduction_to_calculus | calculus]] is fundamental to comprehending how [[Neural Networks and Transformers | neural networks]] learn, particularly through the [[backpropagation | backpropagation algorithm]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article formalizes the relevant [[introduction_to_calculus | calculus]] concepts, focusing on how machine learning practitioners approach the [[derivatives_in_neural_networks | chain rule]] in the context of networks <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

> [!NOTE] Pause and Ponder
> It is advisable to regularly pause and ponder the concepts, as this topic can be confusing <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## The Chain Rule in Neural Networks

The primary goal is to understand how sensitive the [[cost_function | cost function]] is to variables like weights and biases <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This knowledge guides adjustments that lead to the most efficient decrease in the cost function <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This sensitivity is determined using [[derivatives_in_neural_networks | derivatives]] and the [[derivatives_in_neural_networks | chain rule]] <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Simple Network Example (Single Neuron Per Layer)

Consider a very simple [[structure_of_neural_networks | network]] where each [[neuron | layer]] has a single [[neuron | neuron]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This [[structure_of_neural_networks | network]] is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

For the last [[neuron | neuron]] in [[layer | layer]] `L`, its [[activation_functions_in_neural_networks | activation]] is denoted `a(L)`, and the previous [[neuron | neuron]]'s [[activation_functions_in_neural_networks | activation]] is `a(L-1)` <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The desired output for a training example is `y` (e.g., 0 or 1) <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

The cost for a single training example (`C0`) is defined as `(a(L) - y)²` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
The [[activation_functions_in_neural_networks | activation]] `a(L)` is computed from a weighted sum `z(L)`, which is `w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. This `z(L)` is then passed through a non-linear [[activation_functions_in_neural_networks | activation function]] like [[sigmoid_function | sigmoid]] or ReLU <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Conceptual flow of computation:
`weight`, `previous activation`, and `bias` → `z` → `a` → `Cost` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The primary goal is to find the derivative of `C` with respect to `w(L)` (`∂C/∂w(L)`), which represents the sensitivity of the cost function to small changes in the weight `w(L)` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

#### Applying the Chain Rule

A tiny nudge to `w(L)` (`∂w`) causes a nudge to `z(L)` (`∂z(L)`), which causes a nudge to `a(L)` (`∂a(L)`), which directly influences the cost `C` (`∂C`) <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

The [[derivatives_in_neural_networks | chain rule]] states that:
`∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

Let's compute these individual [[derivatives_in_neural_networks | derivatives]]:
*   `∂C/∂a(L)`: The derivative of `(a(L) - y)²` with respect to `a(L)` is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This means the impact on cost is proportional to the difference between the network's output and the desired output <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   `∂a(L)/∂z(L)`: This is the [[derivatives_in_neural_networks | derivative]] of the chosen [[activation_functions_in_neural_networks | activation function]] (e.g., [[sigmoid_function | sigmoid]]) with respect to `z(L)` <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   `∂z(L)/∂w(L)`: The derivative of `w(L) * a(L-1) + b(L)` with respect to `w(L)` is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This implies that the influence of a small nudge to the weight depends on the strength of the previous [[neuron | neuron]]'s [[activation_functions_in_neural_networks | activation]] <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

#### Sensitivity to Bias and Backward Propagation

The sensitivity to the bias `b(L)` (`∂C/∂b(L)`) is very similar to the weight sensitivity, with `∂z(L)/∂b(L)` being `1` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

The ability to calculate `∂C/∂a(L-1)` (sensitivity of the cost function to the [[activation_functions_in_neural_networks | activation]] of the previous [[layer | layer]]) is crucial for [[backpropagation | propagating backwards]] <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. The relevant term in the chain rule expression (`∂z(L)/∂a(L-1)`) is `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows the same [[derivatives_in_neural_networks | chain rule]] idea to be iterated backwards through the network to find sensitivities to earlier weights and biases <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Multi-Neuron Layers

While the single-neuron example simplifies understanding, extending to layers with multiple [[neuron | neurons]] does not exponentially increase complexity; it primarily adds more indices <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

*   **Activation Indexing:** The [[activation_functions_in_neural_networks | activation]] of a given [[layer | layer]] `L` for a specific [[neuron | neuron]] is `a(L)j`, where `j` indexes the [[neuron | neuron]] within that [[layer | layer]] <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. `k` can index the previous [[layer | layer]] `L-1` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Cost Function:** The cost for the entire [[network | network]] is the sum of squared differences between the last [[layer | layer]]'s [[activation_functions_in_neural_networks | activations]] and their desired outputs: `Σ(a(L)j - yj)²` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Weight Indexing:** Weights require more indices, e.g., `w(L)jk` for the weight connecting [[neuron | neuron]] `k` in [[layer | layer]] `L-1` to [[neuron | neuron]] `j` in [[layer | layer]] `L` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Weighted Sum:** `z` still represents the weighted sum before the [[activation_functions_in_neural_networks | activation function]] <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

The core [[derivatives_in_neural_networks | chain rule]] expression for `∂C/∂w(L)jk` remains conceptually similar <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

The key change is in the [[derivatives_in_neural_networks | derivative]] of the cost with respect to an [[activation_functions_in_neural_networks | activation]] in a previous [[layer | layer]], `a(L-1)k` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Since a single [[neuron | neuron]] in [[layer | layer]] `L-1` can influence multiple [[neuron | neurons]] in [[layer | layer]] `L`, its influence on the cost function occurs through multiple paths <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. These individual influences must be summed up to get the total derivative <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

This process, once the sensitivity to the [[activation_functions_in_neural_networks | activations]] in a [[layer | layer]] is known, can be repeated for all weights and biases feeding into that [[layer | layer]], forming the core of [[backpropagation | backpropagation]] <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

## Conclusion

These [[derivatives_in_neural_networks | chain rule]] expressions provide the necessary [[derivatives_in_neural_networks | derivatives]] that define each component of the [[Gradient descent in neural networks | gradient vector]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This [[Gradient descent in neural networks | gradient]] enables the [[network | network]] to minimize its cost by repeatedly stepping downhill during [[Gradient descent in neural networks | gradient descent]] <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. This intricate system represents the heart of how [[Neural Networks and Transformers | neural networks]] learn <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.