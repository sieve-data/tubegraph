---
title: Role of hidden layers in neural networks
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

In a neural network designed for tasks like handwritten digit recognition, the hidden layers play a crucial role in processing information between the input and output. The classic example of this is the handwritten digit recognition task, often referred to as the "hello world of [[Neural Networks and Transformers | neural networks]]" <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Network Structure and Initial Assumptions

The network processes digits rendered on a 28x28 pixel grid, where each pixel's grayscale value determines the activation of one of 784 neurons in the input layer <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Activations for neurons in subsequent layers are determined by a [[adjusting_weights_and_biases_in_neural_networks | weighted sum]] of activations from the previous layer, plus a bias, composed with an [[activation_functions_in_neural_networks | activation function]] like the sigmoid or ReLU <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

For a network with two hidden layers, each containing 16 neurons, there are approximately 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] that can be adjusted <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. These values dictate the network's behavior <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

Initially, the motivation for this layered [[structure_of_neural_networks | structure of neural networks]] was a hope that:
*   The second layer might identify basic features like edges <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   The third layer could combine these edges into more complex patterns, such as loops and lines <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   The final layer would then piece these patterns together to recognize specific digits <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## How Hidden Layers Learn

The network learns by adjusting its [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] based on training data <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This process begins with all [[adjusting_weights and biases in neural networks | weights and biases]] initialized randomly, leading to very poor initial performance <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

To guide the learning, a **cost function** is defined. This function quantifies how "lousy" the network's performance is by summing the squares of the differences between the desired output activations and the actual output activations for a given training example <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The average cost over all training examples serves as the overall measure of the network's inadequacy <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

The cost function takes the 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] as inputs and outputs a single number representing their collective badness <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. The goal of the [[neural_network_learning_process | learning process]] is to minimize this cost function <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

This minimization is achieved through [[Gradient descent in neural networks | gradient descent]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This algorithm involves:
1.  Calculating the [[derivatives_in_neural_networks | gradient]] of the cost function, which indicates the direction of steepest ascent <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Taking the negative of the [[derivatives_in_neural_networks | gradient]] to find the direction of steepest descent (downhill) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
3.  Adjusting all [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] by taking a small step in this downhill direction <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
4.  Repeating this process iteratively <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

The [[derivatives_in_neural_networks | gradient]] vector, composed of [[calculus_in_neural_networks | derivatives]] with respect to each weight and bias, tells us which nudges to these numbers will cause the most rapid decrease in the cost function <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It also reveals the relative importance of each weight and bias, indicating which changes will have the most impact on reducing the cost <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. The algorithm for efficiently computing this [[derivatives_in_neural_networks | gradient]] is called [[introduction_to_backpropagation | backpropagation]] <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

This [[Gradient descent in neural networks | gradient descent]] process is what "teaches" the hidden layers to adjust their internal [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] to improve the network's performance on the training data <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Observed Behavior vs. Expectations

Despite the initial hope that hidden layers would learn interpretable patterns like edges and loops <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, for the described plain vanilla network (two hidden layers, 16 neurons each), this is *not* what happens <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. When visualizing the [[adjusting_weights_and_biases_in_neural_networks | weights]] that connections from the first layer to the second layer acquire, they appear "almost random" with only loose patterns <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

This suggests that in the vast 13,000-dimensional space of possible [[adjusting_weights_and_biases_in_neural_networks | weights and biases]], the network found a "local minimum" that successfully classifies most images (achieving ~96% accuracy on unseen images <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>), but not through the intuitively hoped-for feature extraction <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

Furthermore, this basic network, though good at recognizing digits, struggles with inputs outside its training domain:
*   When presented with a random image, it confidently assigns a nonsense answer rather than showing uncertainty <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   It can recognize digits but "has no idea how to draw them" <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

This behavior is partly due to the tightly constrained training setup, where the network only ever sees clearly defined, unmoving, centered digits and is incentivized to be highly confident <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

## Modern Insights and Future Developments

This basic network architecture is considered "old technology," primarily researched in the 1980s and 1990s <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. While capable of solving problems, the deeper you investigate what its hidden layers are doing, "the less intelligent it seems" <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.

Recent research into more modern, deeper [[neural_networks_and_transformers | neural networks]] offers further insights into how hidden layers learn:
*   A study showed that deep networks could achieve the same training accuracy on randomly labeled datasets as on properly labeled ones, suggesting a capacity to simply "memorize" data <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This raised the question of whether minimizing the cost function truly corresponds to learning structure or merely memorization <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   However, subsequent research clarified that while networks *can* memorize, training on a structured dataset (with correct labels) makes it significantly easier to find a "local minimum" in the optimization landscape <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This implies that for structured data, these networks are indeed doing "something a little bit smarter" than pure memorization <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.
*   Another paper from a few years prior indicated that the local minima learned by networks in a structured dataset tend to be of "equal quality," making it easier to find effective solutions <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.

This ongoing research continues to shed light on the complex roles and behaviors of hidden layers within [[Neural Networks and Transformers | neural networks]], moving beyond the initial, simpler understanding.