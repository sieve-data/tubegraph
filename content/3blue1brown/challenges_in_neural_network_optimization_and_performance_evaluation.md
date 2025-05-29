---
title: Challenges in neural network optimization and performance evaluation
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

This article explores the complexities involved in optimizing neural networks and evaluating their performance, drawing insights from the classic example of handwritten digit recognition.

## Neural Network Structure and Initial State

The goal is to enable a neural network to recognize handwritten digits, a task often referred to as the "hello world of neural networks" <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. Digits are rendered on a 28x28 pixel grid, with each pixel having a grayscale value between 0 and 1 <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. These values determine the activations of 784 neurons in the input layer <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.

A typical network for this task might have two hidden layers, each with 16 neurons <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. The activation of each neuron in subsequent layers depends on a [[weight_and_bias_adjustment_in_neural_networks | weighted sum]] of activations from the previous layer, plus a bias, composed with a function like sigmoid or ReLU <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. In total, such a network has approximately 13,000 [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] that can be adjusted, which dictate the network's behavior <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

Initially, all [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] are set randomly, leading to very poor performance <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. The objective is to adjust these values so the network improves its performance on training data and generalizes well to new, unseen images <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>.

## Neural Network Optimization: The Cost Function and Gradient Descent

The process of training a neural network feels akin to a [[calculus_in_the_context_of_neural_networks | calculus]] exercise, fundamentally involving finding the minimum of a function <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

### The Cost Function

To guide the learning process, a [[cost_function_and_its_role_in_neural_networks | cost function]] is defined <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. This function quantifies how "bad" the network's output is for a given input. It calculates the sum of the squared differences between the network's actual output activations and the desired target activations <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. A small sum indicates a confident and correct classification, while a large sum signifies poor performance <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.

The overall "lousiness" of the network is measured by the average cost across all training examples <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>. This [[cost_function_and_its_role_in_neural_networks | cost function]] itself is a complex function: it takes the 13,000 [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] as its inputs and produces a single numerical output that describes their collective inadequacy based on the network's behavior over tens of thousands of training data points <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.

### Gradient Descent

The core optimization algorithm is called gradient descent <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. The goal is to find the set of [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] that minimizes the [[cost_function_and_its_role_in_neural_networks | cost function]]. Since explicitly finding the minimum of such a complicated function with 13,000 inputs is not feasible <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>, gradient descent offers a flexible iterative approach:

1.  **Start randomly**: Begin with random [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
2.  **Determine the steepest downhill direction**: Use the gradient of the [[cost_function_and_its_role_in_neural_networks | cost function]]. The gradient indicates the direction of steepest ascent, so its negative points in the direction of the fastest decrease <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
3.  **Take a small step**: Adjust the [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] in the negative gradient direction <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>. The step size is proportional to the steepness, meaning smaller steps are taken as the minimum is approached to avoid overshooting <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
4.  **Repeat**: Continuously compute the new gradient and take steps until a local minimum is reached <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

This process can be visualized as a ball rolling down a hill <a class="yt-timestamp" data-t="06:20:00">[06:20:00]</a>. The gradient vector for the 13,000 [[weight_and_bias_adjustment_in_neural_networks | weights and biases]] reveals which "nudges" to these numbers will cause the most rapid decrease in the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>, essentially encoding the relative importance of each weight and bias change <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>. The algorithm for efficiently computing this gradient is called [[backpropagation_algorithm_in_neural_networks | backpropagation]] <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

A crucial aspect for gradient descent is that the [[cost_function_and_its_role_in_neural_networks | cost function]] must have a smooth output to allow for small, incremental steps downhill. This is why artificial neurons often have continuously ranging activations rather than binary on/off states, unlike biological neurons <a class="yt-timestamp" data-t="09:59:00">[09:59:00]</a>.

## Performance Evaluation and Challenges

After training, the network's performance is evaluated on labeled data it has never seen before <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. The MNIST database, comprising tens of thousands of labeled handwritten digit images, is commonly used for this purpose <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

### Network Performance

The described network, with two hidden layers of 16 neurons each, classifies about 96% of new images correctly <a class="yt-timestamp" data-t="13:14:00">[13:14:00]</a>. With minor tweaks to the hidden layer [[structure_and_function_of_a_neural_network | structure and layers]], this can be improved to 98% <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. While good, it's not the best possible performance, as more sophisticated networks can achieve higher accuracy <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.

### Challenges in Understanding Model Predictions

Despite successful classification, there are significant [[challenges_in_understanding_model_predictions | challenges in understanding model predictions]] and the internal workings of the network:

*   **Lack of interpretable feature learning**: The initial motivation for a layered [[neural_network_structure_and_layers | neural network structure and layers]] was the hope that hidden layers might learn to detect distinct patterns like edges, loops, and lines, which would then be combined to recognize digits <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. However, for this specific network, visualizing the [[weight_and_bias_adjustment_in_neural_networks | weights]] associated with the first-to-second layer transitions reveals patterns that appear almost random, not clearly defined edges or features <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>. This suggests the network found a local minimum that works, but not necessarily by learning human-interpretable features <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.
*   **Sensitivity to random input**: The network can confidently classify random noise as a digit (e.g., a "5") <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>. This indicates that while it can recognize digits, it doesn't "understand" how to draw them or recognize when an image is not a digit <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.
*   **Constrained training environment**: The network's limited scope during training, consisting solely of clearly defined, unmoving, centered digits, means it receives no incentive to be anything other than utterly confident in its decisions <a class="yt-timestamp" data-t="15:41:00">[15:41:00]</a>.
*   **Local Minima vs. Global Minima**: There is no guarantee that the local minimum found by gradient descent is the smallest possible value of the [[cost_function_and_its_role_in_neural_networks | cost function]] <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>. This means different random starting points could lead to different local minima, potentially affecting performance or learned representations.
*   **Memorization vs. Generalization**: More modern, very deep neural networks, especially those with millions of [[weight_and_bias_adjustment_in_neural_networks | weights]], can sometimes achieve high training accuracy by simply memorizing the random data, rather than learning generalizable structures <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. However, subsequent research suggests that while memorization is possible, networks tend to find "easier" local minima when training on structured datasets, implying some form of actual learning <a class="yt-timestamp" data-t="19:03:00">[19:03:00]</a>. Local minima learned from structured datasets tend to be of equal quality <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>.

This specific network architecture is considered "old technology," primarily researched in the 1980s and 1990s <a class="yt-timestamp" data-t="16:17:00">[16:17:00]</a>. While foundational, understanding its limitations is crucial for appreciating advancements in more modern variants. These [[challenges_in_understanding_model_predictions | challenges in understanding model predictions]] highlight the importance of not just achieving high accuracy but also ensuring the model learns meaningful representations.
For further engagement, resources such as Michael Nielsen's book on deep learning and neural networks, and blogs by Chris Ola and Distill, are recommended <a class="yt-timestamp" data-t="17:04:00">[17:04:00]</a>.