---
title: Chain rule application in machine learning
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

The [[calculus_in_the_context_of_neural_networks | calculus]] of the [[backpropagation_algorithm_in_neural_networks | backpropagation algorithm]] relies heavily on the [[chain_rule_and_exponential_functions | chain rule]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This application of the [[chain_rule_and_exponential_functions | chain rule]] in machine learning has a distinct feel compared to how it's typically approached in introductory [[calculus_in_the_context_of_neural_networks | calculus]] courses <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Understanding Cost Function Sensitivity

The primary goal is to determine how sensitive a network's cost function is to its various weights and biases <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This understanding is crucial for making adjustments that efficiently decrease the cost function during the [[training process of large language models | training process]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Simple Network Example (Single Neuron Per Layer)

To illustrate, consider an extremely simple network where each layer contains only a single neuron <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The following terms are used:
*   `a(L)`: Activation of the last neuron in layer L <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   `a(L-1)`: Activation of the previous neuron in layer L-1 <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   `y`: The desired output value for a given [[importance_of_training_data_in_machine_learning | training example]] <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   `C0`: The cost of the network for a single [[importance_of_training_data_in_machine_learning | training example]], calculated as `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   `w(L)`: The weight connecting the previous neuron to the last neuron <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   `b(L)`: The bias of the last neuron <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   `z(L)`: A special name given to the weighted sum `w(L) * a(L-1) + b(L)` before it's passed through a nonlinear activation function (e.g., sigmoid or ReLU) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

The flow of computation can be conceptualized as:
`w(L)`, `a(L-1)`, `b(L)` → `z(L)` → `a(L)` → `C0` (along with `y`) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Applying the Chain Rule

The goal is to determine the derivative of `C` with respect to `w(L)` (∂C/∂w(L)) to understand how sensitive the cost function is to small changes in this weight <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

A tiny nudge to `w(L)` causes a nudge to `z(L)`, which nudges `a(L)`, directly influencing the cost `C` <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The [[chain_rule_and_exponential_functions | chain rule]] breaks this down:

`∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L))` <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

Let's compute the relevant derivatives for this simple case:
*   **`∂C/∂a(L)`**: This derivative is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Its size is proportional to the difference between the network's output and the desired output, indicating that larger differences mean even slight changes can significantly impact the cost <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   **`∂a(L)/∂z(L)`**: This is simply the derivative of the chosen nonlinear function (e.g., sigmoid) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **`∂z(L)/∂w(L)`**: This derivative is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This means the influence of a small weight adjustment on the last layer depends on the strength of the previous neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Gradient Components

*   **Sensitivity to Bias `b(L)`**: The sensitivity of the cost to the bias `b(L)` is almost identical to that of the weight, just replacing `∂z(L)/∂w(L)` with `∂z(L)/∂b(L)` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. The derivative `∂z(L)/∂b(L)` comes out to be `1` <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Sensitivity to Previous Activation `a(L-1)`**: To propagate backwards, it's also important to understand how sensitive the cost function is to the activation of the previous layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. The initial derivative in the [[chain_rule_and_exponential_functions | chain rule]] expression, `∂z(L)/∂a(L-1)`, comes out to be `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This allows for iterating the [[chain_rule_and_exponential_functions | chain rule]] backwards to determine sensitivity to earlier weights and biases <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Extending to Multiple Neurons Per Layer

While the single-neuron example is simple, the process scales well to layers with multiple neurons <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The core equations remain largely the same, requiring only additional indices to track specific neurons <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

*   **Activation Indexing**: `a(L)` is augmented with a subscript, e.g., `a(L)j`, to indicate which neuron within layer `L` it represents <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. `k` might index neuron in layer `L-1`, and `j` in layer `L` <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Cost Function**: The cost function is updated to sum the squares of differences for all neurons in the last layer: `Sum over j of (a(L)j - yj)^2` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Weight Indexing**: Weights gain additional indices to specify source and destination neurons, e.g., `w(L)jk` for the weight connecting neuron `k` in `L-1` to neuron `j` in `L` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Derivative Complexity**: The [[chain_rule_and_exponential_functions | chain-rule]] derivative expression for a specific weight still looks essentially the same <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. However, the derivative of the cost with respect to an activation in a previous layer (`L-1`) becomes more complex because that neuron influences the cost through multiple paths (i.e., through multiple neurons in the next layer), and these influences must be summed up <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Once the sensitivity of the cost function to activations in a given layer is known, the process can be repeated backwards for all weights and biases feeding into that layer <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. These [[chain_rule_and_exponential_functions | chain rule]] expressions provide the derivatives that determine each component in the gradient vector, which is used to minimize the network's cost by repeatedly stepping "downhill" <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This is the fundamental mechanism behind how neural networks learn <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.