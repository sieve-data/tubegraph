---
title: Introduction to gradient descent
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

This article explores the concept of [[gradient_descent_and_cost_function_minimization | gradient descent]], a fundamental algorithm underlying how neural networks and many other machine learning models learn <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Neural Network Structure Recap

A neural network's goal is often tasks like handwritten digit recognition, the "hello world" of neural networks <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.
*   Digits are rendered on a 28x28 pixel grid, with each pixel having a grayscale value between 0 and 1 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   These pixel values determine the activations of 784 neurons in the input layer <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   The activation for each neuron in subsequent layers is based on a weighted sum of activations from the previous layer, plus a bias, composed with a function like sigmoid or ReLU <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   A network with two hidden layers of 16 neurons each has approximately 13,000 adjustable weights and biases <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. These values define the network's behavior <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   The network classifies a digit when the brightest of 10 neurons in the final layer corresponds to that digit <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   The layered structure is motivated by the idea that earlier layers might pick up on edges, later layers on patterns like loops and lines, and the final layer on whole digits <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

The process of learning involves showing the network large amounts of training data (images of handwritten digits with labels) and adjusting its 13,000 weights and biases to improve performance <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. The MNIST database provides tens of thousands of labeled handwritten digit images for this purpose <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Cost Function: Measuring "Lousiness"

To begin, all weights and biases are initialized randomly, resulting in poor performance <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. For example, inputting an image of a '3' might produce a messy output layer <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

A **cost function** (or loss function) is defined to quantify how "bad" the network's output is <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   For a single training example, the cost is calculated by summing the squares of the differences between the network's trash output activations and their desired values (e.g., 1 for the correct digit, 0 for others) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   This sum is small when the network confidently classifies correctly and large when it's uncertain or wrong <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   The overall cost is the average cost over all tens of thousands of training examples <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This average cost measures how lousy the network is <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

The cost function is a complex function itself:
*   It takes the 13,000 weights and biases as its inputs <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   It outputs a single number describing how bad those weights and biases are <a class="yt-timestamp" data=t="00:04:56">[00:04:56]</a>.
*   Its definition depends on the network's behavior across all training data <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Minimizing the Cost Function with Gradient Descent

The goal of learning is to adjust the weights and biases to decrease the cost function <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. This is essentially a calculus exercise of finding the minimum of a function <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Single-Input Function Analogy
Imagine a simple function with one input and one output <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. While calculus can sometimes find the minimum explicitly, this is not feasible for complex functions like the 13,000-input neural network cost function <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

A more flexible tactic is to:
1.  Start at any input <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
2.  Figure out the direction (left or right) to step to make the output lower <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
3.  If the slope is positive, shift left; if negative, shift right <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
4.  Repeat this process, checking the new slope and taking an appropriate step <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

This repeated process approaches a local minimum of the function <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, like a ball rolling down a hill <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. There's no guarantee the local minimum found is the absolute smallest possible value <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Making step sizes proportional to the slope helps prevent overshooting the minimum <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Multi-Input Function Analogy (The Gradient)
For a function with two inputs and one output (graphed as a surface above the xy-plane), the question becomes: which direction in the input space should you step to decrease the output most quickly (the "downhill" direction)? <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>

*   The [[understanding_gradients_in_backpropagation | gradient]] of a function points in the direction of steepest ascent <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Therefore, taking the negative of the [[understanding_gradients_in_backpropagation | gradient]] gives the direction of steepest descent <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   The length of the [[understanding_gradients_in_backpropagation | gradient]] vector indicates the steepness of that steepest slope <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

>[!NOTE] If you want to learn more about the [[understanding_gradients_in_backpropagation | gradient]] in multivariable calculus, check out resources on Khan Academy <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. The key takeaway is that such a vector can be computed, telling you the downhill direction and its steepness <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

The algorithm to minimize the function involves repeatedly computing this [[understanding_gradients_in_backpropagation | gradient]] direction, taking a small step downhill, and repeating <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This applies to functions with 13,000 inputs, like our neural network's cost function <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Gradient Descent Defined
All 13,000 weights and biases can be organized into a giant column vector <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. The negative [[understanding_gradients_in_backpropagation | gradient]] of the cost function is a vector in this huge input space <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. This vector tells you which nudges to all those numbers will cause the most rapid decrease to the cost function <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

**[[gradient_descent_and_cost_function_minimization | Gradient descent]]** is the process of repeatedly nudging an input of a function by some multiple of the negative [[understanding_gradients_in_backpropagation | gradient]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. It's a way to converge towards a local minimum (a "valley") of a cost function <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   Minimizing the cost function means the network performs better on all training samples <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   The cost function needs a nice, smooth output to allow for finding a local minimum by taking small downhill steps <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is why artificial neurons have continuously ranging activations, unlike the binary nature of biological neurons <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

### Interpreting the Gradient Components
Each component of the negative [[understanding_gradients_in_backpropagation | gradient]] vector tells two things:
1.  **Sign**: Whether the corresponding component of the input vector (a weight or bias) should be nudged up or down <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>.
2.  **Relative Magnitude**: Which changes (to which weights/biases) matter more <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. An adjustment to one weight might have a much greater impact on the cost function than another <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. The [[understanding_gradients_in_backpropagation | gradient]] vector encodes the relative importance of each weight and bias, indicating which changes offer the most "bang for your buck" <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Summary of Layers of Complexity
1.  **The Network**: A function with 784 inputs (pixel values) and 10 outputs (digit probabilities), defined by weighted sums and parameterized by weights and biases <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.
2.  **The Cost Function**: A layer on top, taking 13,000 weights and biases as inputs and outputting a single measure of "lousiness" based on training examples <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
3.  **The Gradient of the Cost Function**: Another layer of complexity, telling us what nudges to the weights and biases cause the fastest change to the cost function, effectively indicating which changes matter most <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

The algorithm for efficiently computing this [[understanding_gradients_in_backpropagation | gradient]] is called [[backpropagation_algorithm_walkthrough | backpropagation]], which is the core of how neural networks learn <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.

## Network Performance and Limitations

The described network (two hidden layers of 16 neurons each), when trained using [[gradient_descent_and_cost_function_minimization | gradient descent]], can classify about 96% of new images correctly <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. With tweaks, this can reach 98% accuracy <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

However, the initial motivation that hidden layers would pick up on edges and patterns often doesn't hold for this basic network <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   Visualizing the weights for the first-to-second layer transitions often shows almost random patterns rather than clear edges <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   The network finds a "happy local minimum" in the 13,000-dimensional space that classifies images successfully but doesn't align with intuitive pattern recognition <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   When given a random image, the network confidently outputs a nonsense answer, indicating it has no understanding of what constitutes a valid digit <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>. It has learned to recognize digits but cannot "draw" them <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   This is partly due to the tightly constrained training setup, where the network only sees clearly defined, centered, unmoving digits <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

>[!INFO] This "plain vanilla" network is considered old technology (1980s-1990s) but is a crucial starting point for understanding more modern variants <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### The Problem of Memorization
Research has shown that deep neural networks can achieve high training accuracy even on randomly labeled datasets <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   The millions of weights in these networks allow them to simply memorize the random data <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   This raises the question of whether minimizing the cost function corresponds to finding true structure or just memorization <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   However, when training on random data, the accuracy curve goes down very slowly, indicating the network struggles to find a local minimum <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   In contrast, with a structured dataset (correct labels), the accuracy drops very fast, suggesting it's easier to find a local minimum <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
*   The local minima that networks learn tend to be of equal quality when the dataset is structured, making them easier to find <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>.

## Further Learning Resources
*   **Michael Nielsen's book on deep learning and neural networks**: Offers code and data for the exact example discussed, with step-by-step explanations <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>. It's free and publicly available <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   **Chris Olah's blog post and Distill articles**: Additional phenomenal resources for understanding deep learning <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.