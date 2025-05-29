---
title: Feedforward neural networks
videoId: zij_FTbJHsk
---

From: [[lexfridman]] <br/> 

Feedforward neural networks are a foundational concept in the field of [[deep_learning_and_artificial_neural_network_architecture | deep learning]] and are often considered as a starting point for understanding more complex network architectures. They are a type of artificial neural network where the connections between the units do not form a cycle.

## Structure and Function

Feedforward neural networks consist of layers: an input layer, one or more hidden layers, and an output layer. Each layer is made up of units, which receive inputs only from the preceding layer and send outputs only to the succeeding layer. The network is called "feedforward" because data moves in one direction—forward from input nodes, through hidden nodes (if any), and finally to output nodes.

### Forward Pass

The forward pass is the process of computing outputs from inputs across the network. It involves a series of linear transformations, typically represented in matrix form with weight matrices and bias vectors, followed by the application of non-linear activation functions to introduce non-linearity into the model [<a class="yt-timestamp" data-t="00:03:01">00:03:01</a>]. Common activation functions include the sigmoid, hyperbolic tangent (tanh), and ReLU (rectified linear unit) functions [<a class="yt-timestamp" data-t="00:05:02">00:05:02</a>].

### Output Layer and Activation Functions

At the output layer, the network produces a result or classification, which is often interpreted probabilistically using the softmax activation function. Softmax transforms the outputs into a probability distribution over predicted output classes [<a class="yt-timestamp" data-t="00:07:00">00:07:00</a>].

## Training Feedforward Neural Networks

Training a feedforward neural network involves updating the weights and biases to minimize the difference between the predicted and actual output (loss). This process is often done through methods like [[backpropagation_and_gradient_descent_in_neural_networks | backpropagation and gradient descent]] [<a class="yt-timestamp" data-t="00:12:01">00:12:01</a>].

### Empirical Risk Minimization

The training utilizes a framework called empirical risk minimization, where the average loss over the training data is minimized [<a class="yt-timestamp" data-t="00:11:01">00:11:01</a>]. A regularizer is often included to penalize complex models and avoid overfitting [<a class="yt-timestamp" data-t="00:11:36">00:11:36</a>].

### Optimization Algorithms

Stochastic Gradient Descent (SGD) is a commonly used optimization algorithm for training feedforward neural networks. It iteratively updates parameters using gradients computed from the loss function [<a class="yt-timestamp" data-t="00:13:13">00:13:13</a>]. Variants like mini-batch SGD are employed to improve efficiency and convergence rate [<a class="yt-timestamp" data-t="00:39:33">00:39:33</a>].

## Challenges and Considerations

### Initialization and Hyperparameters

Proper initialization of weights is crucial to prevent issues like vanishing or exploding gradients, which can hinder training effectiveness. Weights are usually initialized as small random values to break symmetry and ensure effective training [<a class="yt-timestamp" data-t="00:32:16">00:32:16</a>].

Choosing the right hyperparameters, such as learning rate and the number of hidden units, is essential for the model's performance and is often done using methods like grid search or random search [<a class="yt-timestamp" data-t="00:33:30">00:33:30</a>].

### Regularization Techniques

Techniques like dropout, where certain neurons are randomly ignored during training, help in reducing overfitting by preventing units from co-adapting too much [<a class="yt-timestamp" data-t="00:51:00">00:51:00</a>].

## Advanced Concepts

Feedforward neural networks are the stepping stones to more complex networks such as convolutional neural networks used in [[deep_learning_and_convolutional_neural_networks | deep learning and convolutional neural networks]] and [[applications_of_recurrent_neural_networks | recurrent neural networks]].

> [!info] Further Learning
>
> For those interested in deepening their understanding of feedforward neural networks and their applications, exploring topics such as [[training_neural_networks | training neural networks]] and [[neural_networks_and_training | neural networks and training]] is recommended. Additionally, contrast these artificial systems with their biological counterparts in [[biological_versus_artificial_neural_networks| biological versus artificial neural networks]]. 

Feedforward neural networks provide a foundational understanding from which the broader complexity of neural network architectures can be developed and understood.