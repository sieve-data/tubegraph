---
title: Understanding Neural Networks
videoId: JAgHUDhaTU0
---

From: [[nikhil.kamath]] <br/> 

[[Introduction to Artificial Intelligence | Artificial Intelligence]] (AI) is a field of investigation into intelligence. One approach within AI is [[Machine Learning Techniques | Machine Learning]], which trains machines from data rather than completely programming them <a class="yt-timestamp" data-t="00:29:11">[00:29:11]</a>. A key subcategory of [[Machine Learning Techniques | Machine Learning]] is [[the_evolution_of_neural_networks_and_applications_in_ai | Deep Learning]], which is largely founded on neural networks <a class="yt-timestamp" data-t="00:29:22">[00:29:22]</a>.

## What is a Neural Network?
A neural network is composed of simulated "neurons," which are simple computational elements <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. These "neurons" are akin to simplified versions of biological neurons, performing a weighted sum of their inputs and comparing it to a threshold to activate an output <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>. The *weights* (or connections) between these neurons are adjustable through training <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.

The concept of a neural network stems from the idea of reproducing intelligence mechanisms observed in animals and humans, particularly how brains organize and learn through modifying the strength of connections between neurons <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

## Early Development of Neural Networks
Early work in the 1940s by mathematicians like McCulloch and Pitts proposed that neurons could be simple computational elements <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.

### The Perceptron
In 1957, the perceptron was proposed as the first machine of its type <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
The training process involved:
1.  **Input:** An array of numbers, such as pixels from a black-and-white image (0 for black, 1 for white) <a class="yt-timestamp" data-t="00:21:30">[00:21:30]</a>.
2.  **Weighted Sum:** An output is computed as a weighted sum of the input values. Weights could be positive or negative <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.
3.  **Threshold:** If the weighted sum exceeds a threshold, it's classified as one thing (e.g., 'C'); if lower, it's another (e.g., 'D') <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>.
4.  **Training:** If the system made a mistake, the weights were adjusted. For example, if the output needed to be larger, weights connected to "active" pixels would be increased <a class="yt-timestamp" data-t="00:23:40">[00:23:40]</a>. This iterative adjustment allowed the system to settle on a configuration of weights to distinguish between shapes <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>.

Early perceptrons had limited capabilities and could not perform complex functions like recognizing objects in natural images <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>. This limitation led to a decline in interest in neural networks in the late 1960s, notably influenced by Marvin Minsky's book "Perceptrons," which highlighted these limitations <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>. Work in this area continued under names like "statistical pattern recognition" or "adaptive filter theory" <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.

## Modern Neural Networks and Deep Learning
The breakthrough that enabled modern neural networks and deep learning occurred in the 1980s: stacking multiple layers of neurons <a class="yt-timestamp" data-t="00:39:26">[00:39:26]</a>. Each neuron in these layers computes a weighted sum and passes it through a non-linear activation function (like a threshold) <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.

The ability to train these multi-layered networks came with the development of the backpropagation algorithm <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>. This algorithm allows the system to adjust parameters when an output is incorrect by propagating signals backward to figure out how to tweak weights, so the desired output increases and incorrect ones decrease <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>.

Initially, the widespread adoption of these networks was limited due to the need for large amounts of data (pre-internet era) and faster computers <a class="yt-timestamp" data-t="00:41:36">[00:41:36]</a>.

### Architectural Components
Modern [[the_evolution_of_neural_networks_and_applications_in_ai | Deep Learning]] systems utilize various architectures, or ways of connecting neurons, tailored for different types of data and tasks:

*   **Convolutional Neural Networks (ConvNets)** <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>:
    *   Inspired by the architecture of the visual cortex <a class="yt-timestamp" data-t="00:45:32">[00:45:32]</a>.
    *   Neurons in a ConvNet look at small areas of an input (e.g., an image) and detect local motifs <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>.
    *   They are designed to be "equivariant to translation" or "shift equivariant," meaning if the input shifts, the output shifts similarly but remains otherwise unchanged <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>.
    *   Highly effective for data from the natural world, like images and audio signals, where nearby values tend to be similar <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>.

*   **Transformers** <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>:
    *   A different arrangement of neurons where inputs are treated as "tokens" (lists of numbers or vectors) <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>.
    *   A key property is "equivariance to permutation," meaning if the order of input tokens is permuted, the output tokens are permuted similarly but remain otherwise unchanged <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a>.
    *   This architecture views inputs as a set where the order of objects does not matter <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>.
    *   [[Large Language Models and their limitations | Large Language Models]] (LLMs) are a special case of self-supervised learning that often utilize Transformer architectures, particularly "auto-regressive Transformers," to predict the next word in a sequence based on preceding words <a class="yt-timestamp" data-t="00:59:17">[00:59:17]</a>.

## Types of [[Machine Learning Techniques | Machine Learning]] in Neural Networks
Neural networks are trained using different learning paradigms:

*   **Supervised Learning:** The system is given an input and told the desired output. It adjusts its coefficients to make its output closer to the target <a class="yt-timestamp" data-t="00:27:36">[00:27:36]</a>. This is common for classification or regression tasks.

*   **Reinforcement Learning:** The system is not given a correct answer but receives a "reward" signal indicating whether its action was good or bad <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. It's often inefficient, requiring many trials, but excels in environments like games where systems can play millions of times against themselves (e.g., chess or Go) <a class="yt-timestamp" data-t="00:43:45">[00:43:45]</a>.

*   **Self-Supervised Learning:** This approach has become highly prominent recently <a class="yt-timestamp" data-t="00:33:21">[00:33:21]</a>. It's similar to supervised learning in its algorithms, but the data setup is different:
    *   The system learns by predicting missing or corrupted parts of its input <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.
    *   For text, this involves masking words and training the system to predict the missing ones <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>.
    *   For images, it could involve corrupting or transforming an image and training the system to recover the original <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>.
    *   This method doesn't require manual labeling of data, making it efficient for large datasets <a class="yt-timestamp" data-t="00:34:53">[00:34:53]</a>.
    *   [[Large Language Models and their limitations | Large Language Models]] (LLMs) are a successful application of self-supervised learning, specifically auto-regressive prediction, where the system is trained to predict the next word in a given context <a class="yt-timestamp" data-t="00:54:22">[00:54:22]</a>.

## Limitations and Future Directions
While LLMs are impressive in their language manipulation abilities, they have limitations:
*   They primarily work with discrete data like text <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   They do not inherently understand the physical world <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.
*   They lack persistent memory beyond their parameters and the current prompt context <a class="yt-timestamp" data-t="01:03:05">[01:03:05]</a>.

The next major challenge in AI involves developing systems that can learn about the world by observing continuous, high-dimensional data like videos <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>. This requires new architectures, such as Joint Embedding Predictive Architectures (JEPAs) <a class="yt-timestamp" data-t="01:10:25">[01:10:25]</a>. These systems would predict abstract representations of future video frames, rather than individual pixels, enabling them to build internal "world models" and plan sequences of actions hierarchically <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. Such advancements could lead to systems capable of more human-like reasoning and planning, moving beyond simple reactive "system one" AI to deliberate "system two" AI <a class="yt-timestamp" data-t="01:16:14">[01:16:14]</a>.