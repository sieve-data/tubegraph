---
title: Introduction to backpropagation
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

This article explores the fundamental concepts behind how [[Neural network learning process | neural networks learn]], focusing on the role of the cost function and [[Gradient descent in neural networks | gradient descent]], which sets the stage for understanding [[backpropagation_algorithm | backpropagation]].

## Neural Network Structure Recap

A typical [[Neural network learning process | neural network]] for handwritten digit recognition consists of:
*   An input layer with 784 neurons, determined by the 28x28 pixel grid of the input image, where each pixel's grayscale value (between 0 and 1) dictates a neuron's activation <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>.
*   [[Role of hidden layers in neural networks | Hidden layers]], in this case, two [[Role of hidden layers in neural networks | hidden layers]] each with 16 neurons <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.
*   An output layer with 10 neurons, where the brightest activation corresponds to the recognized digit <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

The activation for each neuron in subsequent layers is based on a weighted sum of activations from the previous layer, plus a bias, composed with an [[Activation functions in neural networks | activation function]] like sigmoid or ReLU <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. This specific network configuration has approximately 13,000 adjustable weights and biases that define its behavior <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

## The Learning Problem

The goal of [[Neural network learning process | neural network learning]] is to find an algorithm that allows the network to adjust its weights and biases to improve performance on training data <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>. This typically involves showing the network numerous images of handwritten digits with their corresponding labels, such as those from the MNIST database <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a><a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. The hope is that the learned patterns generalize to unseen images <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a>.

Initially, weights and biases are set randomly, leading to poor performance <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. The process of learning ultimately boils down to a [[calculus in neural networks | calculus]] exercise: finding the minimum of a specific function <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## The Cost Function

To guide the learning process, a "cost function" is defined. This function quantifies how "lousy" the network's current performance is <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

For a single training example, the cost is calculated by summing the squares of the differences between the network's output activations and their desired values (e.g., 1 for the correct digit, 0 for others) <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. A small sum indicates correct and confident classification, while a large sum signifies poor performance <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

The overall cost function for the network is the average cost across all tens of thousands of training examples <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This function takes all 13,000 (or so) weights and biases as inputs and outputs a single number representing the overall "badness" of these parameters <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

## Minimizing the Cost Function: [[Gradient descent in neural networks | Gradient Descent]]

The challenge is to tell the network *how* to change its weights and biases to improve. This is achieved through [[Gradient descent in neural networks | gradient descent]] <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.

### Core Idea of [[Gradient descent in neural networks | Gradient Descent]]

Imagine a simple function with one input and one output. To find its minimum, one can start at any input, determine the slope, and step in the direction that lowers the output (left for a positive slope, right for a negative slope) <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. Repeating this process iteratively leads to a local minimum <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>. This is analogous to a ball rolling down a hill <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>.

For functions with multiple inputs (like our 13,000 weights and biases), the concept extends to finding the steepest "downhill" direction. In [[calculus in neural networks | multivariable calculus]], the gradient of a function points in the direction of steepest ascent <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. Therefore, the *negative* of the gradient points in the direction of steepest descent, indicating how to change the inputs to decrease the function most quickly <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>. The length of the gradient vector indicates the steepness of that slope <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.

The [[Gradient descent in neural networks | gradient descent]] algorithm involves computing this gradient vector, taking a small step in the downhill direction, and repeating the process <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. For a network with 13,000 weights and biases, the negative gradient is a vector in an "insanely huge input space" that indicates how to "nudge" each parameter for the most rapid decrease in the cost function <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

> [!NOTE] Smoothness of the Cost Function
> It is crucial for the cost function to have a smooth output to allow for finding a local minimum by taking small, incremental steps downhill <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>. This is why artificial neurons use continuously ranging activations, rather than binary active/inactive states like biological neurons <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

## The Role of [[backpropagation_algorithm | Backpropagation]]

The algorithm for efficiently computing this gradient, which is central to how a neural network learns, is called [[backpropagation_algorithm | backpropagation]] <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. While this video introduces the *need* for calculating the gradient to minimize the cost function, the detailed mechanics of [[backpropagation_algorithm | backpropagation]] itself will be covered in the next video <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.

The gradient vector's components tell us two things:
1.  The sign indicates whether the corresponding input (weight or bias) should be nudged up or down <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.
2.  The relative magnitudes of the components reveal which changes matter more, i.e., which weights or biases have a greater impact on the cost function <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. This means the gradient vector "encodes the relative importance of each weight and bias" <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

In summary:
*   The network is a function transforming pixel inputs to digit outputs, defined by weighted sums <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
*   The cost function takes the network's weights and biases as input and provides a single measure of its "lousiness" based on training examples <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>.
*   The gradient of the cost function indicates how to adjust weights and biases to most rapidly change (decrease) the cost, effectively showing which changes matter most <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.

## Network Performance and Limitations

After initializing weights and biases randomly and adjusting them repeatedly using [[Gradient descent in neural networks | gradient descent]], the described network (two [[Role of hidden layers in neural networks | hidden layers]], 16 neurons each) can classify about 96% of new, unseen images correctly <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a><a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. With minor tweaks to the [[Role of hidden layers in neural networks | hidden layer]] structure, this can improve to 98% accuracy <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

However, despite good classification performance, the network often doesn't learn the intuitive patterns (like edges or loops) that humans might expect in its [[Role of hidden layers in neural networks | hidden layers]] <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. Visualizing the weights of connections to second-layer neurons shows patterns that appear almost random, rather than clear edges <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. This suggests the network finds a "happy local minimum" in the 13,000-dimensional weight space that doesn't align with human-interpretable features <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.

Furthermore, this simple network can confidently misclassify random noise as a digit, indicating it hasn't learned to recognize what a digit *isn't*, only what it *is* within its tightly constrained training setup <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>.

This "old technology" from the 1980s and 90s is a starting point, but newer, more sophisticated networks have evolved beyond these limitations <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>.

## Further Learning

For deeper engagement with this material, Michael Nielsen's free and publicly available book on deep learning and neural networks is highly recommended, offering code and data for the example discussed <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>. Other resources include Chris Ola's blog post and articles in Distill <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>.

Discussions with experts like Leisha Lee highlight ongoing research into how modern image recognition networks learn. A paper showed that deep neural networks can memorize randomly shuffled labeled datasets with the same training accuracy as properly labeled ones, raising questions about whether they learn structure or just memorize <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>. However, subsequent research indicated that training on structured datasets leads to faster convergence to an accurate local minimum, suggesting that networks *do* find smarter solutions with real data <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.