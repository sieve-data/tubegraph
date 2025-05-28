---
title: Applications of analog computers in AI
videoId: GVsUOuSjvcg
---

From: [[veritasium]] <br/> 

For centuries, [[analog_computers_history_and_resurgence | analog computers]] were the most powerful computing devices, used for tasks such as predicting eclipses and tides, and guiding anti-aircraft guns <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. With the rise of solid-state transistors, digital computers became dominant <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. However, a combination of factors is now paving the way for [[the_resurgence_and_potential_of_modern_analog_computing | analog technology to make a comeback]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This resurgence is particularly relevant for [[advancements_in_neural_networks_and_their_computational_needs | artificial intelligence]] (AI).

## The Return of Analog for AI

Analog computers excel at certain computations quickly and with low power consumption <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. They can add two currents by simply connecting two wires, unlike digital computers which require around 50 transistors for an 8-bit addition <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Multiplication can be achieved by passing a current through a resistor, where the voltage across it (I times R) effectively multiplies two numbers, compared to ~1,000 transistors in a digital system <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Despite these advantages, [[challenges_and_potential_of_analog_computing_in_modern_technology | analog computers]] have drawbacks:
*   They are not general-purpose computing devices; they cannot run software like Microsoft Word <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   Inputs and outputs are continuous, meaning exact values cannot be reliably input or repeated <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   Manufacturing variations in components like resistors or capacitors typically lead to about a 1% error <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

These limitations previously caused analog computers to fall out of favor <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. However, the rise of AI presents a "perfect storm" for their comeback <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Why AI Needs Analog
The increasing demand for larger neural networks faces several challenges with digital computing:
*   **Energy Consumption:** Training a neural network can consume as much electricity as three households annually <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Von Neumann Bottleneck:** In modern digital computers, the majority of time and energy in deep neural network computations is spent fetching weight values from memory over a bus, rather than performing the actual calculations <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Moore's Law Limitations:** The miniaturization of transistors is approaching fundamental physical limits, slowing the traditional doubling of transistors on a chip <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

Crucially, neural networks do not require the high precision of digital computers <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. Minor variations in component values or conditions can be tolerated, making them well-suited for analog computation <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. A key task in neural networks—matrix multiplication—can be performed efficiently by analog systems <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

## Early AI and Neural Networks

The term "AI" was coined in 1956 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In 1958, Cornell University psychologist Frank Rosenblatt built the perceptron, an early attempt to mimic how neurons fire in the brain <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### The Perceptron
A perceptron models a neuron:
*   Its activation is either a one or a zero <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Input comes from other neurons, with varying connection strengths (weights) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Weights can be positive (excitatory) or negative (inhibitory) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   To determine if a neuron fires, input activations are multiplied by their weights and summed (a vector dot product) <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. If the sum exceeds a bias, the neuron fires <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Rosenblatt's perceptron used 400 photocells as input for a 20x20-pixel image, with each pixel's brightness acting as an input neuron's activation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. These connected to a single output neuron via adjustable weights <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The goal was to distinguish between images, like rectangles and circles <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

Training involved showing the perceptron images and adjusting weights:
*   If the output was correct, no change was made <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   If the output neuron didn't fire but should have (e.g., when shown a circle), the input activations were added to the weights <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   If it fired but shouldn't have (e.g., when shown a rectangle), input activations were subtracted from the weights <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This process continued until all training images were correctly identified <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

The perceptron could distinguish shapes and letters <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Rosenblatt claimed it could even differentiate cats and dogs and was capable of "original thought" <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. However, the perceptron's capabilities were limited, and it could not, in fact, tell cats from dogs <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Critiques in a 1969 book by Minsky and Papert led to the "first AI winter," a period of reduced interest in artificial neural networks <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### AI Resurgence and Deeper Networks
An [[advancements_in_neural_networks_and_their_computational_needs | AI resurgence]] occurred in the 1980s with the creation of one of the first self-driving cars by Carnegie Mellon <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. This vehicle was steered by an artificial neural network called ALVINN <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. ALVINN was similar to the perceptron but included a "hidden layer" of artificial neurons between input and output <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Its input was 30x32-pixel images of the road ahead <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Training involved a human driver providing correct steering angles, and the network's weights were adjusted using backpropagation to match the human's output <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. The computer's speed was limited by the speed of matrix multiplication <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Despite these advancements, neural networks still struggled with tasks like telling cats and dogs apart, leading to another lull in AI development in the 1990s <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a> <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### The ImageNet Breakthrough
In the mid-2000s, researcher Fei-Fei Li hypothesized that artificial neural networks needed more data to train on <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. From 2006 to 2009, she created ImageNet, a database of 1.2 million human-labeled images, the largest of its kind at the time <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

The ImageNet Large Scale Visual Recognition Challenge (2010-2017) involved software programs competing to classify images into 1,000 categories <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Performance was measured by the "top-5 error rate"—how often the correct category was *not* among the top five neuron activations <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

In 2012, AlexNet, a neural network from the University of Toronto, achieved a breakthrough with a top-5 error rate of just 16.4%, significantly better than previous bests <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. AlexNet's success stemmed from its size and depth: eight layers and 500,000 neurons, with 60 million weights and biases to adjust <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Training was computationally intensive, requiring 700 million math operations per image, which was managed by pioneering the use of GPUs (graphical processing units) <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. This established that the scale of the neural network was key to its success <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

Following AlexNet's lead, the top-5 error rate plummeted, reaching 3.6% in 2015, which is better than human performance <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. This network had 100 layers of neurons <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. This trajectory indicates an increasing demand for ever larger neural networks and, consequently, more powerful and efficient computing <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

## Modern Analog AI Hardware

Companies like Mythic AI are developing analog chips specifically to run neural networks <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. Their approach repurposes digital flash storage cells <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

Traditionally, flash cells store a one or a zero by trapping or releasing electrons on a floating gate, which affects whether the cell conducts current <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Mythic's innovation is to use these cells as variable resistors, by placing a specific number of electrons on each floating gate, rather than all or nothing <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. The more electrons, the higher the resistance <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.

When a small voltage is applied, the current flowing through the cell (I) is equal to V/R, or voltage (V) times conductance (G, reciprocal of R) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. This means a single flash cell can multiply two values: voltage times conductance <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

To run a neural network:
1.  Network weights are written to the flash cells as each cell's conductance <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
2.  Activation values are input as voltage on the cells <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.
3.  The resulting current (voltage × conductance) represents activation × weight <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.
4.  The cells are wired so that the currents from individual multiplications sum up, completing the matrix multiplication required by neural networks <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

Mythic AI's first product can perform 25 trillion math operations per second while consuming only about three watts of power <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. This compares favorably to newer digital systems that perform 25-100 trillion operations per second but are large, expensive systems consuming 50-100 watts <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. While not a direct "apples-to-apples" comparison (digital is better for training large models), analog chips are highly efficient for deploying AI workloads <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

### Use Cases for Analog AI Chips
These analog AI chips have potential applications in:
*   **Augmented and Virtual Reality (AR/VR):** Rapidly capturing and rendering user pose in virtual worlds <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
*   **Depth Estimation:** Creating depth maps from single webcams <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   **Security Cameras and Autonomous Systems:** On-device AI processing <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **Manufacturing Inspection:** Identifying good vs. bad products on a conveyor belt <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
*   **Smart Home Speakers:** Analog circuitry could efficiently listen for wake words like Alexa or Siri, then activate the main digital circuitry <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

## Hybrid Analog-Digital Approaches

Despite the benefits, the inherent imprecision of [[challenges_and_potential_of_analog_computing_in_modern_technology | analog computers]] remains a hurdle. For neural networks with many layers (e.g., 50 sequences of matrix multiplies), a purely analog process would result in significant signal distortion by the output <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

To overcome this, hybrid systems convert signals from the analog domain back to digital after each processing block, then convert them back to analog for the next block <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This preserves the signal integrity <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

Frank Rosenblatt, recognizing the limitations of digital computers for his early perceptron, ultimately built a custom [[analog_computers_history_and_resurgence | analog computer]] with variable resistors <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>. While his idea of neural networks proved correct, perhaps his intuition about analog computation will also prove to be prescient <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

While digital computing has dominated for decades, the future of information technology, especially for AI, may involve a re-evaluation of [[differences_between_analog_and_digital_computers | analog and digital systems]] <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>. The human brain, for instance, functions with neurons that fire (digital) but also processes information in a continuous, distributed manner (analog) <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Achieving true artificial intelligence, machines that think like humans, may necessitate harnessing the power of analog computing <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.