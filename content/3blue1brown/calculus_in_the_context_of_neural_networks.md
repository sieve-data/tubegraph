---
title: Calculus in the context of neural networks
videoId: tIeHLnjs5U8
---

From: [[3blue1brown]] <br/> 

This article explores the application of calculus, particularly the chain rule, within the context of neural networks, building upon an intuitive understanding of the [[backpropagation_algorithm_in_neural_networks | backpropagation algorithm]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The goal is to illustrate how machine learning practitioners conceptualize the [[fundamental_concepts_of_calculus | chain rule]] differently from most introductory [[fundamental_concepts_of_calculus | calculus]] courses <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Readers who are uncomfortable with the relevant [[fundamental_concepts_of_calculus | calculus]] concepts may find additional resources helpful <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

> It's normal for this to be at least a little confusing, so the mantra to regularly pause and ponder certainly applies as much here as anywhere else <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Understanding Sensitivity in Simple Networks

To illustrate the application of calculus, a highly simplified network is considered, where each layer contains only a single neuron <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This network is defined by three weights and three biases <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The primary objective is to determine how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to changes in these variables <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This understanding helps identify which adjustments to these terms will most efficiently decrease the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The focus is initially on the connection between the last two neurons <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Network Components and Notations

*   **Activation (a)**: The output of a neuron. `a(L)` denotes the activation of the last neuron in layer L, and `a(L-1)` for the previous layer <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. These superscripts are indices, not exponents <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Desired Output (y)**: The target value for the last activation for a given training example <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Cost (C0)**: For a single training example, the [[cost_function_and_its_role_in_neural_networks | cost]] is defined as `(a(L) - y)^2` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Weighted Sum (z)**: The input to the activation function, calculated as `w(L) * a(L-1) + b(L)` <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. It's given a special name `z(L)` <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Activation Function**: A non-linear function (e.g., sigmoid or ReLU) applied to `z` to produce `a` <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Conceptually, the weight, previous activation, and bias compute `z`, which computes `a`, which then, along with `y`, computes the [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Applying the Chain Rule

The first objective is to understand the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to small changes in the weight `w(L)`, expressed as the derivative of C with respect to `w(L)` (∂C/∂w(L)) <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

A "del w" term signifies a tiny nudge to W (e.g., a change by 0.01), and a "del C" term refers to the resulting nudge to the [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. The goal is to find their ratio <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

A small change to `w(L)` causes a nudge to `z(L)`, which nudges `a(L)`, directly influencing the [[cost_function_and_its_role_in_neural_networks | cost]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. This relationship is broken down using the [[fundamental_concepts_of_calculus | chain rule]]:
∂C/∂w(L) = (∂C/∂a(L)) * (∂a(L)/∂z(L)) * (∂z(L)/∂w(L)) <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

#### Computing the Derivatives

1.  **∂C/∂a(L)**: This derivative is `2 * (a(L) - y)` <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Its magnitude is proportional to the difference between the network's output and the desired output, implying that large differences lead to significant impacts on the final [[cost_function_and_its_role_in_neural_networks | cost function]] from slight changes <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **∂a(L)/∂z(L)**: This is the derivative of the chosen non-linear activation function (e.g., sigmoid) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
3.  **∂z(L)/∂w(L)**: This derivative is `a(L-1)` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This means the influence of a small nudge to the weight on the last layer depends on the strength of the previous neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, reinforcing the idea that "neurons that fire together wire together" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

This calculation provides the derivative of the [[cost_function_and_its_role_in_neural_networks | cost]] for a single training example <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. The full [[cost_function_and_its_role_in_neural_networks | cost function]]'s derivative requires averaging this expression across all training examples <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This result forms one component of the gradient vector, which consists of partial derivatives of the [[cost_function_and_its_role_in_neural_networks | cost function]] with respect to all weights and biases <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Sensitivity to Bias and Previous Layers

The sensitivity to bias `b(L)` is very similar to `w(L)` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>, with the term ∂z/∂w replaced by ∂z/∂b, which evaluates to 1 <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

The [[fundamental_concepts_of_calculus | chain rule]] also reveals how sensitive the [[cost_function_and_its_role_in_neural_networks | cost function]] is to the activation of the previous layer, `a(L-1)` <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Specifically, the sensitivity of `z` to `a(L-1)` is the weight `w(L)` <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Although this previous layer activation cannot be directly influenced, understanding this sensitivity is crucial because it allows the iteration of the [[fundamental_concepts_of_calculus | chain rule]] backwards through the network to determine the [[cost_function_and_its_role_in_neural_networks | cost function]]'s sensitivity to even earlier weights and biases <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This is the essence of [[backpropagation_algorithm_in_neural_networks | backpropagation]] <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## Extending to Multiple Neurons Per Layer

While the single-neuron-per-layer example simplifies the explanation, extending these concepts to layers with multiple neurons does not exponentially increase complexity <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. It mainly involves adding more indices to track variables <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

*   **Activation Indexing**: `a(L)` now becomes `a(L)j`, where `j` indicates a specific neuron within layer L <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. `k` might index neurons in layer L-1, and `j` for layer L <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Cost Function**: The [[cost_function_and_its_role_in_neural_networks | cost]] for a single training example is now the sum of the squares of the differences between each last-layer activation and its desired output: `Sum over j (a(L)j - yj)^2` <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   **Weight Indexing**: Weights require additional indices. `w(L)jk` denotes the weight connecting the `k`th neuron in layer L-1 to the `j`th neuron in layer L <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

The structure of the `z` term and the [[fundamental_concepts_of_calculus | chain-ruled]] derivative expression for the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost]] to a specific weight remain essentially the same <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

The key difference arises when calculating the derivative of the [[cost_function_and_its_role_in_neural_networks | cost]] with respect to an activation in a previous layer, such as `a(L-1)` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. A single neuron in layer L-1 influences the [[cost_function_and_its_role_in_neural_networks | cost function]] through *multiple different paths*—it influences `a(L)0`, `a(L)1`, and so on <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Therefore, these influences must be summed up <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Once the sensitivity of the [[cost_function_and_its_role_in_neural_networks | cost function]] to the activations in the second-to-last layer is known, this process can be repeated for all weights and biases feeding into that layer, propagating the sensitivity backward through the network <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

These [[fundamental_concepts_of_calculus | chain rule]] expressions provide the derivatives that determine each component in the gradient vector, which is essential for minimizing the network's [[cost_function_and_its_role_in_neural_networks | cost]] by repeatedly stepping downhill <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>, forming the core of how [[structure_and_function_of_a_neural_network | neural networks]] learn through [[backpropagation_algorithm_in_neural_networks | backpropagation]] <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. The complexity of these concepts may require time to fully grasp <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.