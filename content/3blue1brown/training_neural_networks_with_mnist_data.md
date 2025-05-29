---
title: Training neural networks with MNIST data
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

This article focuses on the training process of a neural network, specifically using the MNIST dataset for handwritten digit recognition. It explains how neural networks learn by introducing the concept of a cost function and the [[gradient_descent_in_neural_networks | gradient descent]] algorithm, which are fundamental to [[neural_network_learning_process | neural network learning]].

## Network Structure and Goal

The neural network aims to recognize handwritten digits [00:00:28]. These digits are rendered on a 28x28 pixel grid, with each pixel having a grayscale value between 0 and 1 [00:00:37]. These pixel values determine the activations of 784 neurons in the input layer [00:00:43].

Each neuron's activation in subsequent layers is based on a weighted sum of activations from the previous layer, plus a bias [00:00:51]. This sum is then composed with a function like the sigmoid or ReLU [00:01:02].

In this specific network, there are two hidden layers, each with 16 neurons [00:01:09]. The network contains approximately 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] that can be adjusted [00:01:15]. These values dictate the network's behavior [00:01:19]. A digit is classified when the brightest of 10 neurons in the final layer corresponds to that digit [00:01:24].

The initial motivation for this layered [[structure_of_neural_networks | structure of neural networks]] was the hope that hidden layers might detect patterns like edges, loops, and lines, which the final layer could then combine to recognize digits [00:01:34].

## The Learning Process

The goal is an algorithm that allows the network to [[neural_network_learning_process | learn]] by adjusting its 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] to improve performance on [[importance_of_training_data_in_machine_learning | training data]] [00:02:04]. The network's ability to generalize beyond this [[importance_of_training_data_in_machine_learning | training data]] is tested by showing it new, labeled images after training [00:02:10].

The [[training_process_of_language_models | training process]] begins by initializing all [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] randomly [00:03:19]. As a result, the network initially performs poorly [00:03:24].

### MNIST Dataset

The MNIST database provides tens of thousands of handwritten digit images, each labeled with the correct number [00:03:31]. This dataset is a common starting point for neural network examples [00:03:31].

### The Cost Function

To guide the learning, a "cost function" is defined [00:03:36]. This function quantifies how "bad" the network's output is for a given input [00:03:36]. Mathematically, it's calculated by summing the squares of the differences between the network's actual output activations and their desired values [00:03:51]. This sum is small if the network classifies correctly and confidently, and large if it performs poorly [00:04:05].

The overall "lousiness" of the network is measured by the average cost over all tens of thousands of [[importance_of_training_data_in_machine_learning | training examples]] [00:04:18]. The cost function takes the 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] as its inputs and outputs a single number representing their inadequacy [00:04:53].

### Gradient Descent

The network improves by minimizing this cost function [00:04:49]. This minimization process, known as [[gradient_descent_in_neural_networks | gradient descent]], is a core concept in [[neural_network_learning_process | neural network learning]] [00:00:13]. It's essentially a [[calculus in neural networks | calculus]] exercise [00:02:53].

For a simple function, finding the minimum involves starting at an arbitrary input and repeatedly taking small steps in the direction that decreases the output [00:05:51]. If the slope is positive, one shifts left; if negative, one shifts right [00:06:00]. This process converges to a local minimum [00:06:11]. Step sizes are typically proportional to the slope, which helps prevent overshooting the minimum [00:06:43].

For functions with multiple inputs, the concept extends to finding the steepest downhill direction [00:06:55]. Multivariable [[calculus in neural networks | calculus]] reveals that the negative of the gradient of a function indicates the direction of steepest descent [00:07:26]. The length of the gradient vector also indicates the steepness of this slope [00:07:47].

The same idea applies to the network's 13,000 [[adjusting_weights_and_biases_in_neural_networks | weights and biases]] [00:08:27]. These are organized into a vector, and the negative gradient of the cost function is a vector indicating which small adjustments to all those numbers will most rapidly decrease the cost [00:08:40]. Minimizing this cost means making the network's output on each piece of [[importance_of_training_data_in_machine_learning | training data]] align more closely with the desired outcome [00:08:58].

The algorithm used to efficiently compute this gradient is called backpropagation, which is central to how a neural network learns [00:09:23].

It's crucial for the cost function to have a smooth output to allow for small, incremental steps towards a local minimum [00:09:59]. This is why artificial neurons often have continuously ranging activations rather than binary (active/inactive) states like biological neurons [00:10:09].

The components of the negative gradient vector tell two things:
1.  The sign indicates whether a corresponding weight or bias should be nudged up or down [00:10:45].
2.  The relative magnitudes indicate which changes matter more, or which have a greater impact on the cost function [00:10:55]. This can be interpreted as the "relative importance" of each weight and bias [00:11:19].

## Performance and Limitations of the "Vanilla" Network

The described network, with two hidden layers of 16 neurons each, achieves about 96% accuracy on new, unseen images [00:13:14]. With minor tweaks to the hidden layer structure, this can improve to 98% [00:13:36].

However, the network does not learn in the intuitively expected way:
*   The visualization of the weights connecting the first to the second layer shows patterns that are almost random, rather than clear edges [00:14:24]. The network finds a local minimum that classifies images successfully but doesn't necessarily pick up on human-interpretable patterns [00:14:53].
*   When presented with a random image, the network confidently provides a nonsense answer, indicating it doesn't understand uncertainty [00:15:09]. It can recognize digits but cannot "draw" them or reason about what constitutes a valid digit [00:15:34].

This behavior stems from the tightly constrained [[training_process_of_language_models | training setup]]: the network's universe consists solely of clear, centered digits, and its cost function doesn't incentivize uncertainty [00:15:41]. This "plain vanilla" network represents older technology from the 1980s and 1990s, serving as a foundational understanding for more modern and sophisticated variants [00:16:17].

## Further Exploration

For those interested in delving deeper, resources such as Michael Nielsen's book on deep learning and neural networks are highly recommended, as they provide code and data for hands-on experimentation [00:17:01]. Other valuable resources include Chris Ola's blog post and articles in Distill [00:17:27].

### Insights from Recent Research

Dr. Leisha Lee discusses two recent papers exploring how modern image recognition networks learn [00:17:40]. A particularly deep neural network, when trained on a dataset with randomly shuffled labels, could still achieve the same [[training_process_of_language_models | training accuracy]] as with properly labeled data [00:18:02]. This suggested that the network's millions of weights were sufficient to simply memorize the random data, raising questions about whether cost function minimization always corresponds to understanding image structure or just memorization [00:18:21].

However, a subsequent paper showed that [[neural_networks_and_transformers | networks]] do something smarter [00:18:54]. When training on a random dataset, the accuracy curve descends very slowly, indicating a struggle to find the right local minimum [00:19:03]. In contrast, with a structured dataset (correct labels), the network drops very quickly to high accuracy [00:19:12]. This indicates it's easier to find suitable local minima when the data is structured [00:19:24]. Another paper supports this by suggesting that, with structured datasets, the local minima these networks learn are of equal quality [00:19:43]. This implies that if a dataset is structured, it should be much easier to find an effective minimum [00:19:48].