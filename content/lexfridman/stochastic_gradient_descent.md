---
title: Stochastic gradient descent
videoId: zij_FTbJHsk
---

From: [[lexfridman]] <br/> 

Stochastic Gradient Descent (SGD) is a foundational optimization algorithm widely used in training neural networks, especially within the context of [[backpropagation_and_gradient_descent_in_neural_networks]]. It is a variant of gradient descent that updates the parameters of the model by computing the gradient of the loss function with respect to the parameters using a single training example (or a small batch), rather than the entire dataset. This approach significantly speeds up training, making it feasible to handle large datasets often utilized in deep learning contexts.

## Overview

SGD operates by iterating over the training examples, updating the weights incrementally. This is particularly effective in machine learning as it allows for more frequent updates, providing a pragmatic approach to optimize complex models such as neural networks.

> [!info] Empirical Risk Minimization
>
> SGD is often framed within the paradigm of empirical risk minimization, where the goal is to minimize the average loss over the training data, possibly incorporating regularization terms to prevent overfitting <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

## Algorithm Outline

### Initialization

1. **Parameter Initialization**: Begin by initializing all parameters, typically the weight matrices and bias terms, with small random values to break symmetry and ensure effective learning <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

### Iterative Optimization

2. **Epoch Definition**: An epoch comprises a single pass over the entire dataset. The process is typically repeated for a predefined number of epochs or until convergence <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

3. **Gradient Computation**: For each training example or mini-batch:
   - Compute the gradient of the loss function with respect to the model parameters <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.
   - If using regularization, include the gradient of the regularizer.

4. **Parameter Update**: Adjust the model parameters in the direction that decreases the loss:
   \[
   \theta = \theta - \alpha \nabla L(\theta)
   \]
   Here, \( \alpha \) is the learning rate, a hyperparameter that determines the step size <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

### Hyperparameter Tuning

- **Learning Rate (\(\alpha\))**: A critical parameter that requires careful tuning. Too large a value may cause the algorithm to diverge, while too small a value may lead to slow convergence <a class="yt-timestamp" data-t="00:36:36">[00:36:36]</a>.

- **Regularization**: Techniques such as L2 regularization (also known as weight decay) are often employed to penalize large parameter values, which can help prevent overfitting <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

- **Mini-Batches**: While classic SGD uses single examples, "mini-batch" versions compute the gradient over a small subset of the data, balancing the noise of SGD with the computational efficiency of batch gradient descent <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

## Advancements and Variants

The basic SGD framework has been refined with various approaches to enhance convergence and performance:

- **Momentum**: Augments the update rule to accelerate SGD by taking into account past gradients, smoothing the optimization path <a class="yt-timestamp" data-t="00:40:28">[00:40:28]</a>.

- **Learning Rate Schedules**: Adjusting the learning rate during training, such as decreasing it over time, can significantly improve the quality of convergence <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>.

- **Adaptive Methods**: Algorithms such as RMSProp and Adam dynamically adjust the learning rate for each parameter based on past gradients and are widely used in deep learning for their robustness and ease of tuning <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>.

SGD has demonstrated great success across numerous applications, from foundational deep learning setups to more specific tasks like [[machine_learning_in_finance]]. Its stochastic nature, combined with its ease of implementation and efficiency, make it a prerequisite technique in the toolkit of machine learning practitioners.