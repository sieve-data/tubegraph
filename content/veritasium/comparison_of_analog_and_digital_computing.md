---
title: Comparison of analog and digital computing
videoId: GVsUOuSjvcg
---

From: [[veritasium]] <br/> 

Historically, [[History and resurgence of analog computers | analog computers]] were the most powerful computing devices for hundreds of years, used for tasks such as predicting eclipses and guiding anti-aircraft guns <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. With the advent of solid-state transistors, [[History and resurgence of analog computers | digital computers]] became dominant, and nearly all modern computers are digital <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. However, a combination of factors is leading to a [[History and resurgence of analog computers | resurgence of analog technology]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Analog Computers
An analog computer operates without zeros and ones <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Instead, it uses physical phenomena, such as a voltage, to directly represent variables in a problem <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The electrical circuitry acts as an analog for the physical problem, allowing computations to occur much faster <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Capabilities and Examples
Analog computers can be programmed by connecting wires in specific ways to solve various differential equations <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Examples include:
*   Simulating a damped mass oscillating on a spring, allowing real-time adjustments of damping, spring constant, or mass to observe changes in oscillation amplitude and duration <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.
*   Solving the Lorenz system, a basic model of atmospheric convection famous for being one of the first discovered examples of chaos, displaying the Lorenz attractor's butterfly shape <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Advantages
*   **Power and Speed**: They are powerful computing devices capable of completing many computations rapidly <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Energy Efficiency**: They require little power to operate <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   **Simplicity of Operations**:
    *   Adding two numbers in analog can be achieved by simply connecting two wires to combine currents <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, whereas a digital computer might need around 50 transistors for an 8-bit addition <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
    *   Multiplying two numbers in analog can be done by passing a current through a resistor, where the resulting voltage (V = I * R) effectively performs the multiplication <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>, in contrast to the approximately 1,000 transistors required for digital multiplication <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

### Drawbacks
*   **Not General-Purpose**: Analog computers are not designed for general computing tasks, meaning they cannot run software like Microsoft Word <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Inexact and Non-Repeatable**: Since inputs and outputs are continuous, exact values cannot be input, leading to slight variations and non-repeatable answers for the same calculation <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Manufacturing Variation**: Inherent variations in component values (e.g., resistors, capacitors) during manufacturing can lead to an expected error of about 1% <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

These drawbacks were major reasons why analog computers fell out of favor once [[History and resurgence of analog computers | digital computers]] became viable <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Digital Computers
Digital computers operate using discrete values, typically represented as zeros and ones <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### Advantages
*   **Precision and Repeatability**: Digital systems offer high precision and can repeat calculations exactly.
*   **General-Purpose**: They are highly versatile and can perform a wide range of tasks.

### Limitations in Modern AI
The increasing demand for larger neural networks highlights several limitations of current digital computing approaches:
*   **Energy Consumption**: Training a neural network can consume as much electricity as three households annually <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
*   **Von Neumann Bottleneck**: In digital computers, data is stored in memory and accessed via a bus <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. For deep neural networks, most time and energy are spent fetching weight values rather than on the computation itself <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **Limitations of Moore's Law**: While the number of transistors on a chip has doubled approximately every two years for decades, the size of transistors is now approaching the atomic scale, presenting fundamental physical challenges to further miniaturization <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Resurgence of Analog Computing in AI
A "perfect storm" of factors is leading to a [[Future potential of analog computers in AI | resurgence of analog computers]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Digital computers are reaching their limits, while neural networks are growing in popularity <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. A significant portion of neural network computation, particularly matrix multiplication <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>, is well-suited for analog methods. Crucially, neural networks do not require the extreme precision of digital computers; slight variability in components or conditions can be tolerated <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

### Neural Networks and Their Computational Demands
The field of artificial intelligence, which began in 1956 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>, has seen a renewed interest in neural networks. Frank Rosenblatt's Perceptron (1958) was an early attempt to mimic how neurons fire <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Later, in the 1980s, neural networks like ALVINN in self-driving cars utilized hidden layers and performed matrix multiplication to process image inputs and determine steering angles <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

The development of large datasets like ImageNet (created between 2006-2009 by Fei-Fei Li) <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a> and powerful neural networks like AlexNet (2012) <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>, which pioneered the use of GPUs for parallel computation <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>, showed that increasing the scale and depth of neural networks significantly improved performance <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. By 2015, neural networks achieved better-than-human performance in image classification on ImageNet <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This trend points to an ever-increasing demand for larger neural networks <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

### Mythic AI's Approach
Mythic AI, an [[analog_computing_in_machine_learning_and_ai_applications | analog computing]] startup, creates analog chips to run neural networks <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. They repurpose digital flash storage cells, normally used for storing binary data, as variable resistors <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. By placing a specific number of electrons on the floating gate, they can control the resistance of the cell <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

When a small voltage (representing activation values) is applied, the resulting current (I = V/R or V * conductance) performs a multiplication of the voltage and the cell's conductance (representing the weight) <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>. Wiring these cells together allows the currents from individual multiplications to sum, completing matrix multiplication for neural networks <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

Mythic AI's first product can perform 25 trillion math operations per second while consuming about three watts of power <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. This contrasts with newer digital systems that might achieve 25 to 100 trillion operations per second but consume 50 to 100 watts and are much larger <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. While digital chips are needed for training complex algorithms, analog chips are highly efficient for deploying AI workloads in devices like security cameras, autonomous systems, and inspection equipment <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

### Hybrid Analog-Digital Systems
Despite the advantages, analog systems still face challenges with signal degradation over long sequences of operations <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. To address this, current solutions convert signals from analog to digital, process them digitally, and then convert them back to analog for the next processing block, thereby preserving the signal <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This hybrid approach leverages the strengths of both domains. For example, analog circuitry could efficiently listen for wake words in smart home speakers, quickly activating the device's digital components <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

## Future Outlook
The concept of neural networks, initially explored by Rosenblatt with custom analog computers <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>, has proven to be successful. The question remains whether [[Future potential of analog computers in AI | analog computers]] will see a similar widespread adoption as digital ones <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. However, analog computers appear better suited for many tasks desired today <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.

Our brains can be seen as both digital (neurons either fire or don't) and analog (thinking occurs everywhere, all at once) <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. This suggests that the power of [[analog_computing_in_machine_learning_and_ai_applications | analog computing]] might be necessary to achieve true artificial intelligence, creating machines that think like humans <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.