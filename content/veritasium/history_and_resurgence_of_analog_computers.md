---
title: History and resurgence of analog computers
videoId: GVsUOuSjvcg
---

From: [[veritasium]] <br/> 

For centuries, [[comparison_of_analog_and_digital_computing | analog computers]] were considered the most powerful computing devices globally, capable of predicting eclipses and tides, and guiding anti-aircraft guns <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. However, the advent of solid-state transistors ushered in the era of digital computers, making them the dominant form of computing today <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Despite this, a combination of factors is currently paving the way for a resurgence of [[future_potential_of_analog_computers_in_ai | analog technology]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## How Analog Computers Work

An [[comparison_of_analog_and_digital_computing | analog computer]] operates without zeros and ones <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Instead, it uses physical phenomena, such as voltages, to represent and solve problems <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. By connecting wires in specific ways, it can be programmed to solve a range of differential equations <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

For example, a setup can simulate a damped mass oscillating on a spring, where a voltage oscillates exactly like the physical mass <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The electrical circuitry acts as an analog for the physical problem, executing calculations much faster <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Another example is simulating the Lorenz system, a basic model of convection in the atmosphere, known as one of the first discovered examples of chaos <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Parameters can be changed on an analog computer to observe their effects in real-time <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Advantages and Disadvantages

### Advantages
[[comparison_of_analog_and_digital_computing | Analog computers]] are powerful computing devices capable of completing many computations quickly and with low power consumption <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Addition**: Adding two currents can be done by simply connecting two wires <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, whereas a digital computer requires around 50 transistors for two eight-bit numbers <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Multiplication**: Passing a current through a resistor allows the voltage across it (I times R) to effectively multiply two numbers <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. A digital computer needs about 1,000 transistors for multiplication <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Disadvantages
Despite their strengths, [[comparison_of_analog_and_digital_computing | analog computers]] have significant drawbacks that led to their decline <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Single-Purpose**: They are not general-purpose devices, meaning they cannot run diverse software like Microsoft Word <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Inexact and Non-Repeatable**: Inputs and outputs are continuous, preventing exact value input and consistent results for repeated calculations <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Manufacturing variations in components (like resistors or capacitors) lead to an approximate 1% error margin <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

These limitations—being single-purpose, non-repeatable, and inexact—were the primary reasons [[comparison_of_analog_and_digital_computing | analog computers]] fell out of favor once digital computers became viable <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

## The Resurgence: AI and Neural Networks

The resurgence of [[comparison_of_analog_and_digital_computing | analog computers]] is closely linked to artificial intelligence (AI) <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Early AI: The Perceptron
The term "AI" was coined in 1956 <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In 1958, Frank Rosenblatt built the perceptron, designed to mimic how neurons fire in the brain <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

A basic model of a neuron works as follows:
*   An individual neuron either fires (activation of 1) or doesn't (activation of 0) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Inputs come from other neurons, with varying connection strengths represented by weights (positive for excitatory, negative for inhibitory) <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   To determine if a neuron fires, the activation of each input neuron is multiplied by its weight, and these products are summed <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   If the sum exceeds a bias, the neuron fires; otherwise, it doesn't <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

Rosenblatt's perceptron used 400 photocells (pixels) as input neurons for 20x20-pixel images, with activations between zero and one <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. These inputs connected to a single output neuron, each with an adjustable weight <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. The process of multiplying activations by weights and summing them is essentially a vector dot product <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

The perceptron's goal was to distinguish between two images, like a rectangle and a circle <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Training involved showing it images and adjusting weights:
*   If the output was correct, no weight change occurred <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   If incorrect (e.g., didn't fire for a circle), input activations were added to weights <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   If incorrect (e.g., fired for a rectangle), input activations were subtracted from weights <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
This algorithm was proven to converge if the categories were separable <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

The perceptron could distinguish shapes and letters <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Rosenblatt claimed it could tell cats from dogs and exhibit "original thought," leading to exaggerated media claims of self-reproducing, conscious machines <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

In reality, the perceptron's capabilities were limited; it could not differentiate cats from dogs <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Critiques by Minsky and Papert in 1969 led to the first AI winter, a period of decline for artificial neural networks and AI <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

### The Rise of Deep Learning
The 1980s saw an AI resurgence, exemplified by Carnegie Mellon's ALVINN, one of the first self-driving cars steered by an artificial neural network <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. ALVINN was an advancement on the perceptron, featuring a hidden layer of artificial neurons between input (30x32-pixel road images) and output layers <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Going from one layer to the next involved matrix multiplication of input activations and weights <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Training involved a human driver providing correct steering angles, with weights adjusted by backpropagation <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. As training progressed, the network learned to identify road markings, and its steering angle matched the human driver's <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The vehicle's speed (1-2 km/h) was limited by the computer's matrix multiplication speed <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

Despite these advancements, neural networks still struggled with tasks like distinguishing cats and dogs, leading to a second AI lull in the 1990s <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

### ImageNet and the AI Boom
By the mid-2000s, most AI researchers focused on improving algorithms <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. However, Fei-Fei Li posited that more training data was needed <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. From 2006 to 2009, she created ImageNet, a database of 1.2 million human-labeled images, the largest of its kind <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. From 2010 to 2017, the ImageNet Large Scale Visual Recognition Challenge had software programs compete to detect and classify images into 1,000 categories, including 90 dog breeds <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

In 2012, AlexNet, a neural network from the University of Toronto, revolutionized the competition <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. It achieved a top-5 error rate of 16.4%, significantly better than previous bests of 28.2% (2010) and 25.8% (2011) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. AlexNet's success stemmed from its size and depth: eight layers and 500,000 neurons, with 60 million weights and biases adjusted during training <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. This required 700 million math operations per image <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. The team pioneered the use of Graphics Processing Units (GPUs) for fast parallel computations to handle this computational intensity <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

AlexNet's research paper, cited over 100,000 times, highlighted the importance of network scale <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. Following this lead, the ImageNet top-5 error rate plummeted to 3.6% by 2015, surpassing human performance <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. This network had 100 layers of neurons <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

## Why Analog Computers are Making a Comeback for AI

The increasing demand for larger neural networks presents several challenges for traditional digital computers <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>:
*   **Energy Consumption**: Training a neural network can consume as much electricity as three households annually <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   **Von Neumann Bottleneck**: Most modern digital computers store data in memory and access it via a bus <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. For deep neural networks, most time and energy are spent fetching weight values rather than computing <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **Limitations of Moore's Law**: The doubling of transistors on a chip every two years is slowing as transistor size approaches atomic scale, presenting fundamental physical challenges to further miniaturization <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

This "perfect storm" creates an opening for [[comparison_of_analog_and_digital_computing | analog computers]] <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Digital computers are nearing their limits, while neural networks are exploding in popularity <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. A core operation for neural networks is matrix multiplication <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. Crucially, neural networks do not require the extreme precision of digital computers; a slight variability in components can be tolerated <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This makes [[analog_computing_in_machine_learning_and_ai_applications | analog computing]] well-suited for AI workloads <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

## Modern Analog Computing for AI (Mythic AI)

Companies like Mythic AI are developing [[analog_computing_in_machine_learning_and_ai_applications | analog chips]] to run neural networks <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. They repurpose digital flash storage cells, traditionally used to store binary data, as variable resistors <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>.
*   By placing a specific number of electrons on each floating gate, they control the resistance of the channel <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   The more electrons, the higher the resistance <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   Applying a small voltage causes current (V/R or Voltage x Conductance) to flow, effectively multiplying two values <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

To run a neural network, Mythic AI writes all network weights as the conductance of flash cells <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>. Activation values are then input as voltage, and the resulting current (activation times weight) is summed as cells are wired together, completing the matrix multiplication <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

Mythic AI's first product can perform 25 trillion math operations per second on a small chip, consuming about three watts of power <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. While newer digital systems can do 25-100 trillion operations per second, they are large, expensive systems consuming 50-100 watts <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. These analog chips are designed for deploying AI workloads, not training them, and have applications in security cameras, autonomous systems, and manufacturing inspection equipment <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

One proposed use for [[analog_computing_in_machine_learning_and_ai_applications | analog circuitry]] is in smart home speakers, solely to listen for wake words like "Alexa" or "Siri" <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. This would use less power and quickly activate the device's digital circuitry <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

A challenge for [[analog_computing_in_machine_learning_and_ai_applications | analog AI]] is managing signal distortion over many computational layers <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. To address this, the signal is converted from analog to digital, sent to the next processing block, and then converted back to analog, preserving the signal <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

## Conclusion

Historically, Rosenblatt initially used a digital IBM computer for his perceptron but switched to a custom [[comparison_of_analog_and_digital_computing | analog computer]] with variable resistors due to speed limitations <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. His idea of neural networks proved correct, and perhaps his belief in [[comparison_of_analog_and_digital_computing | analog computing]] will too <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

While it's uncertain if [[comparison_of_analog_and_digital_computing | analog computers]] will take off as digital ones did, they appear better suited for many current computing tasks <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. Though digital has dominated information processing for decades (music, pictures, video), it might be seen as a starting point rather than an endpoint in 100 years <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. Human brains exhibit both digital characteristics (neurons firing or not) and analog (thinking occurring everywhere simultaneously) <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. Perhaps the power of analog will be essential for achieving true artificial intelligence that thinks like humans <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.