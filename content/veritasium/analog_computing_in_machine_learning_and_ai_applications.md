---
title: Analog computing in machine learning and AI applications
videoId: GVsUOuSjvcg
---

From: [[veritasium]] <br/> 

For centuries, [[history_and_resurgence_of_analog_computers | analog computers]] were considered the most powerful computing devices globally, capable of tasks like predicting eclipses and guiding anti-aircraft guns <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, with the invention of solid-state transistors, [[comparison_of_analog_and_digital_computing | digital computers]] became dominant, making almost every modern computer digital <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Today, a combination of factors is paving the way for a [[history_and_resurgence_of_analog_computers | resurgence of analog technology]], particularly in the realm of [[neural_networks_and_artificial_intelligence | artificial intelligence]] (AI) <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## How Analog Computers Work

An [[history_and_resurgence_of_analog_computers | analog computer]] solves differential equations by connecting wires in specific ways <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Unlike [[comparison_of_analog_and_digital_computing | digital computers]] which use zeros and ones, analog computers represent variables as continuous physical quantities, such as voltage <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The electrical circuitry acts as an analog (or model) for a physical problem, allowing for much faster simulations <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

For instance, an analog computer can simulate a damped mass oscillating on a spring, where a voltage oscillates exactly like the mass <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. Parameters like damping, spring constant, or mass can be varied in real-time, observing the change in amplitude and duration of oscillations <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. By changing electrical connections, the computer can be programmed to solve other differential equations, such as the Lorenz system, which models convection in the atmosphere and was one of the first examples of chaos <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Advantages and Disadvantages

**Advantages of Analog Computers:**
*   **Powerful and Fast**: They can complete many computations very quickly <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Energy-Efficient**: They require significantly less power for certain operations <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For example, adding two currents in an analog computer only requires connecting two wires, compared to approximately 50 transistors for adding two eight-bit numbers in a digital computer <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Multiplication can be achieved by passing a current through a resistor (voltage = I * R), effectively multiplying two numbers, which would require around 1,000 transistors in a digital system <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

**Disadvantages of Analog Computers:**
*   **Not General-Purpose**: They are single-purpose devices, meaning they cannot run diverse software like Microsoft Word <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Non-Repeatable and Inexact**: Due to continuous inputs and outputs, exact values cannot be inputted, leading to slight variations in results when repeating calculations <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Manufacturing Variability**: Component variations (e.g., resistors, capacitors) can lead to an expected error rate of about 1% <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

These limitations were major reasons why [[history_and_resurgence_of_analog_computers | analog computers]] fell out of favor once [[comparison_of_analog_and_digital_computing | digital computers]] became viable <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Artificial Intelligence and the Need for Analog

The recent [[history_and_resurgence_of_analog_computers | resurgence of analog technology]] is largely driven by advancements and challenges in [[neural_networks_and_artificial_intelligence | artificial intelligence]] (AI) <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

### Early Neural Networks: The Perceptron

The term AI was coined in 1956 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In 1958, Frank Rosenblatt built the perceptron, designed to mimic how neurons fire in our brains <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. A basic model of a neuron involves activation (0 or 1), inputs from other neurons, and weighted connections (positive for excitatory, negative for inhibitory) <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. A neuron fires if the sum of its weighted inputs exceeds a "bias" value <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Rosenblatt's perceptron used 400 photocells to capture a 20x20 pixel image, with each pixel acting as an input neuron <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. These inputs were connected to a single output neuron via adjustable weights <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The system performed a vector dot product to determine if the output neuron would fire <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The goal was to distinguish between images (e.g., rectangles and circles) by training the perceptron and adjusting its weights <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The weight adjustment algorithm was simple: add input activations if the output was incorrect (didn't fire when it should have), or subtract them if it fired incorrectly <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. This algorithm was proven to converge if the categories were separable <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

Initial media coverage of the perceptron was highly optimistic, suggesting it could achieve "original thought" and perform complex human-like functions <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. However, the perceptron was limited in its capabilities, and a 1969 critique by Minsky and Papert led to the "first AI winter," a period of reduced interest and funding for [[neural_networks_and_artificial_intelligence | artificial neural networks]] <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### AI Resurgence and Deep Learning

The 1980s saw an AI resurgence, exemplified by Carnegie Mellon's self-driving car <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. This vehicle used ALVINN, an [[neural_networks_and_artificial_intelligence | artificial neural network]] with a hidden layer of neurons between input and output <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. ALVINN processed 30x32 pixel images of the road, performing matrix multiplications to determine steering angles <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Training involved a human driving the vehicle, and weights were adjusted via backpropagation <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. ALVINN was limited by the speed of digital matrix multiplication, driving at only 1-2 km/h <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Despite these advances, [[neural_networks_and_artificial_intelligence | artificial neural networks]] still struggled with basic tasks, leading to another AI lull in the 1990s <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

In the mid-2000s, researcher Fei-Fei Li hypothesized that more training data was needed <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. She created ImageNet (2006-2009), a database of 1.2 million human-labeled images <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. The ImageNet Large Scale Visual Recognition Challenge (2010-2017) invited software programs to classify images into 1,000 categories <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

In 2012, AlexNet, an [[neural_networks_and_artificial_intelligence | artificial neural network]] from the University of Toronto, significantly outperformed competitors, achieving a top-5 error rate of just 16.4% <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Its success was attributed to its unprecedented size and depth: eight layers and 500,000 neurons, with 60 million weights and biases <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. Training AlexNet involved 700 million math operations per image and was computationally intensive, requiring the pioneering use of GPUs (graphical processing units) for fast parallel computations <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

The AlexNet paper established that the scale of the [[neural_networks_and_artificial_intelligence | neural network]] was key to its performance <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. Following this breakthrough, the ImageNet error rate plummeted, reaching 3.6% in 2015, which is better than human performance <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. This success led to the conclusion that larger [[neural_networks_and_artificial_intelligence | neural networks]] would be in ever-increasing demand <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

### Limitations of Digital AI

The growing demand for larger [[neural_networks_and_artificial_intelligence | neural networks]] presents several problems for [[comparison_of_analog_and_digital_computing | digital computers]]:
*   **Energy Consumption**: Training a single [[neural_networks_and_artificial_intelligence | neural network]] can consume electricity equivalent to three households' yearly consumption <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Von Neumann Bottleneck**: Modern digital computers store data in memory and access it via a bus. In deep [[neural_networks_and_artificial_intelligence | neural networks]], most time and energy are spent fetching weight values rather than performing calculations <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Moore's Law Limitations**: The miniaturization of transistors is approaching atomic scales, posing fundamental physical challenges to further gains in density <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

## The Perfect Storm for Analog AI

These limitations create a "perfect storm" for [[future_potential_of_analog_computers_in_ai | analog computers]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. As digital computers reach their limits, [[neural_networks_and_artificial_intelligence | neural networks]] are exploding in popularity, and a core operation they perform is matrix multiplication <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. Critically, [[neural_networks_and_artificial_intelligence | neural networks]] do not require the high precision of [[comparison_of_analog_and_digital_computing | digital computers]]; slight variability in components or conditions can be tolerated <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

## Modern Analog AI Applications

Startups like Mythic AI in Texas are developing [[future_potential_of_analog_computers_in_ai | analog chips]] specifically for running [[neural_networks_and_artificial_intelligence | neural networks]] <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. They repurpose digital flash storage cells, traditionally used to store binary data, as variable resistors <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.

In a flash cell, electrons trapped on a floating gate prevent current flow (storing a zero), while the absence of electrons allows current flow (storing a one) <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. Mythic's innovation is to store a *specific number* of electrons on each floating gate, making the cell's resistance variable <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. When a small voltage is applied, the current flowing through is equal to V/R, or voltage multiplied by conductance (the reciprocal of resistance) <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This allows a single flash cell to perform multiplication <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

To run an [[neural_networks_and_artificial_intelligence | artificial neural network]], the network's weights are written to the flash cells as conductance values <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. Input activation values are then applied as voltage to the cells <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. The resulting currents (activation * weight) are summed as they are wired together, completing the required matrix multiplication for [[neural_networks_and_artificial_intelligence | neural network]] layers <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

Mythic AI's first product can perform 25 trillion math operations per second while consuming about three watts of power <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. While newer digital systems can achieve 25 to 100 trillion operations per second, they are typically larger, more expensive, and consume significantly more power (50 to 100 watts) <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

Specific applications demonstrated for these analog AI chips include:
*   Augmented and Virtual Reality (VR/AR) for real-time pose capture and rendering <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   Depth estimation from a single webcam <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   Deployment in security cameras <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   Autonomous systems <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
*   Inspection equipment for manufacturing (e.g., identifying bad Frito-Lay chips on a conveyor belt) <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
*   Smart home speakers using analog circuitry to listen for wake words like "Alexa" or "Siri," thereby consuming less power and quickly activating the device's digital circuitry <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.

## Hybrid Analog-Digital Approach

Despite the benefits, challenges of [[comparison_of_analog_and_digital_computing | analog computing]] remain, particularly concerning accumulated distortion over multiple computational steps <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. To mitigate this, a hybrid approach is often used: calculations are performed in the analog domain, converted back to the digital domain for preservation, and then converted back to analog for the next processing block <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

## Conclusion

Frank Rosenblatt, creator of the perceptron, initially found [[comparison_of_analog_and_digital_computing | digital computers]] too slow for his [[neural_networks_and_artificial_intelligence | neural network]] and built a custom [[history_and_resurgence_of_analog_computers | analog computer]] <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. While his idea of [[neural_networks_and_artificial_intelligence | neural networks]] proved correct, it remains to be seen if his choice of [[history_and_resurgence_of_analog_computers | analog computing]] will also prevail <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

The [[future_potential_of_analog_computers_in_ai | future potential of analog computers in AI]] is significant, as they appear better suited for many tasks demanded of modern computers <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. While digital has dominated information processing for decades, analog may represent not an end point but a starting point in information technology <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. Human brains, for example, exhibit both digital (neurons firing or not) and analog (thinking occurring everywhere, all at once) characteristics <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This suggests that achieving true [[neural_networks_and_artificial_intelligence | artificial intelligence]] that thinks like humans might require harnessing the power of analog <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.