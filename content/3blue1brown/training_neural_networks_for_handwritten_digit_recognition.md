---
title: Training neural networks for handwritten digit recognition
videoId: IHZwWFHWa-w
---

From: [[3blue1brown]] <br/> 

The primary goal of this discussion is to explain the process of [[neural_network_structure_and_layers|neural networks]] learning, focusing on the concept of gradient descent, and then to examine the performance and internal workings of a specific network designed for [[digit_recognition_using_neural_networks|handwritten digit recognition]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This classic example is often referred to as the "hello world" of [[neural_network_structure_and_layers|neural networks]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Neural Network Structure Recap

The [[neural_network_structure_and_layers|neural network]] for [[digit_recognition_using_neural_networks|handwritten digit recognition]] is designed as follows:
*   **Input**: Handwritten digits are rendered on a 28x28 pixel grid, with each pixel having a grayscale value between 0 and 1 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   **Input Layer**: These pixel values determine the activations of 784 neurons in the input layer <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Following Layers**: The activation for each neuron in subsequent layers is based on a weighted sum of activations from the previous layer, plus a bias <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This sum is then composed with an activation function like sigmoid or ReLU <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Hidden Layers**: In a common configuration, the network uses two hidden layers, each with 16 neurons <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   **Adjustable Parameters**: This specific network has approximately 13,000 [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] that can be adjusted, which determine its behavior <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Output Layer**: The network classifies a digit when the brightest of its 10 neurons in the final layer corresponds to that digit <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The initial motivation for this layered structure was the hope that deeper layers would pick up on increasingly complex patterns like edges, loops, and lines <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## How the Network Learns

The [[training_process_of_large_language_models|training process]] aims to create an algorithm where the [[neural_network_structure_and_layers|network]] can be shown a large amount of [[importance_of_training_data_in_machine_learning|training data]] and adjust its [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] to improve performance <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

*   **Training Data**: This data consists of images of handwritten digits paired with their correct labels <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The MNIST database provides tens of thousands of such labeled images, making it a common starting point for this task <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   **Generalization**: The hope is that the layered structure allows what the network learns to generalize to images beyond the [[importance_of_training_data_in_machine_learning|training data]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Testing**: After [[training_process_of_large_language_models|training]], the network is shown new, unseen labeled data to assess its classification accuracy <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Initial State and Cost Function

Initially, all [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] are set randomly, leading to poor performance <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. To guide the learning process, a cost function is defined <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

*   **Cost of a Single Example**: For a given training example, the cost is calculated by summing the squares of the differences between the network's output activations and the desired output activations (e.g., 1 for the correct digit neuron, 0 for others) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Average Cost**: The overall cost (or "lousiness") of the network is the average cost over all tens of thousands of [[importance_of_training_data_in_machine_learning|training data]] examples <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This cost function is a complex function itself, taking approximately 13,000 [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] as inputs and outputting a single number indicating performance <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Gradient Descent

The core of how a [[neural_network_structure_and_layers|network]] learns is by minimizing this cost function <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. This process relies on a strategy called **gradient descent** <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

*   **Minimization Analogy**: Finding the minimum of a function, especially one with many inputs, can be challenging. A flexible tactic is to start at any input and repeatedly take small steps in the direction that decreases the function's output <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   **Slope and Gradient**:
    *   For a function with one input, you check the slope: shift left if positive, shift right if negative <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   For functions with multiple inputs (like our 13,000 [[weight_and_bias_adjustment_in_neural_networks|weights and biases]]), the concept extends to the gradient. The gradient of a function indicates the direction of steepest ascent <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   The negative of the gradient points in the direction of steepest *descent* <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>, effectively telling the network how to adjust its [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] for the most rapid decrease in cost <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Algorithm**: The algorithm involves computing this gradient vector, taking a small step downhill (proportional to the gradient's magnitude), and repeating this process <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The step sizes become smaller as the slope flattens out, preventing overshooting the minimum <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Local Minima**: It's important to note that gradient descent approaches a *local minimum* of the function, and there's no guarantee it will find the smallest possible value of the cost function <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   **Smoothness**: The cost function must have a nice, smooth output to allow for these continuous steps downhill <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This is why artificial neurons have continuously ranging activations rather than binary ones, unlike biological neurons <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Backpropagation**: The algorithm for efficiently computing this gradient is called [[backpropagation_algorithm_in_neural_networks|backpropagation]], which is the heart of how a [[neural_network_structure_and_layers|neural network]] learns <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **Meaning of Gradient Components**: Each component of the negative gradient vector indicates whether the corresponding [[weight_and_bias_adjustment_in_neural_networks|weight or bias]] should be nudged up or down, and its relative magnitude signifies which changes have a greater impact on the cost function <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This can be interpreted as encoding the relative importance of each [[weight_and_bias_adjustment_in_neural_networks|weight and bias]] <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Performance and Limitations

After initializing the network with random [[weight_and_bias_adjustment_in_neural_networks|weights and biases]] and repeatedly adjusting them via gradient descent, the described network (with two hidden layers of 16 neurons each) classifies about 96% of new images correctly <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>. With some tweaks to the hidden layer structure, accuracy can reach 98% <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

However, despite its success, the network often does not learn in the intuitively desired way:
*   **Lack of Feature Detection**: The initial hope that hidden layers would pick up on features like edges and patterns is often not realized <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. When visualizing the [[weight_and_bias_adjustment_in_neural_networks|weights]] connecting the first to the second layer, they appear almost random, not clearly defined edges <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. The network finds a local minimum that works, but not necessarily by identifying human-interpretable patterns <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Overconfidence in Nonsense**: If a random image is input, the network confidently outputs a nonsense answer, indicating it doesn't recognize uncertainty or random noise <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. This suggests the network, while good at recognition, has no "idea" how to draw digits <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.
*   **Constrained Training**: This behavior stems from the tightly constrained [[training_process_of_large_language_models|training setup]]. The network only sees clearly defined, centered, unmoving digits and is never incentivized to express uncertainty <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   **Old Technology**: The discussed plain vanilla network is based on older technology (from the 1980s and 1990s). While foundational for understanding modern variants, its hidden layers often seem less "intelligent" than more sophisticated current models <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

### Modern Insights on Network Learning

Recent research explores how more modern image recognition networks actually learn <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. One paper revealed that deep [[neural_network_structure_and_layers|networks]] can achieve the same [[training_process_of_large_language_models|training]] accuracy on randomly labeled datasets as on properly labeled ones <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This suggests that with millions of [[weight_and_bias_adjustment_in_neural_networks|weights]], networks might simply memorize random data, raising questions about whether minimizing the cost function truly corresponds to learning image structure or just memorization <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

However, subsequent research has shown that networks do something smarter:
*   When [[training_process_of_large_language_models|training]] on random data, the accuracy curve descends very slowly, indicating a struggle to find the local minimum <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   In contrast, when [[training_process_of_large_language_models|training]] on a structured dataset with correct labels, the accuracy drops very quickly after an initial fiddling phase <a class="yt="yt-timestamp" data-t="00:19:12">[00:19:12]</a>. This implies it's easier to find the local maxima (or minima) for structured data <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   Furthermore, studies suggest that local minima in the [[optimization|optimization]] landscape for structured datasets tend to be of equal quality, making them easier to find <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

> [!NOTE] Further Learning
> To engage more deeply with this material, consider exploring Michael Nielsen's free and publicly available book on deep learning and [[neural_network_structure_and_layers|neural networks]], which provides code and data for hands-on experimentation <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. Other recommended resources include blog posts by Chris Ola and articles in Distill <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.