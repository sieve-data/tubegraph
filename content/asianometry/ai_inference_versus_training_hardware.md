---
title: AI inference versus training hardware
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

The [[evolution_of_ai_hardware_and_gpus | evolution of GPUs]] by [[Nvidia and competition in the AI chip market | Nvidia]] initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs perform well with neural network algorithms, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

Today, the AI accelerator hardware market is valued at over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Venture capitalists invested nearly $2 billion in AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, and TSMC views AI accelerator hardware as a significant future revenue driver <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Neural Networks and Specialized Hardware
A neural network is essentially a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. They are typically represented with matrices <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Processing involves turning input data (like an image) into a matrix, multiplying it with weight matrices across many layers, and applying an activation function <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

In 2011, a team from New York University and Yale University presented a paper at the CVPR conference discussing a scalable hardware architecture for large and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Although GPUs were the de facto standard for running and testing AI algorithms at the time <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, the paper highlighted that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and [[energy_efficiency in AI hardware | power consumption]] by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. They implemented a data grid architecture on a Zynq’s Virtex 6 FPGA, a chip type allowing custom configurations, and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. A hypothetical 45-nanometer chip design also outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

AI accelerators are designed to handle matrix multiplication and convolution operations, which constitute about 90% of the computational work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Back in 2016, Google surveyed some neural networks and found them to have up to 100 million weights <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Training vs. Inference
AI accelerators serve two primary roles:
*   **Training Phase:** Involves using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Inference Stage:** Where the trained neural network function is used to infer a result from new input data <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This is when the network processes an image to identify an object, for example <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

Early AI hardware projects predominantly focused on *inference*:
*   **Dianna (Chinese Academy of Sciences Institute of Computing Technology):** A 65-nanometer accelerator tuned for computer vision, consuming 400 times less energy than a GPU and small enough to be embedded with image sensors <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **IRIS (MIT project with DARPA funding):** A flexible accelerator for mobile devices running neural networks, designed for *inference* with 10 times more [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Teradeep (NNX processor):** Aimed to give deep learning capabilities to old webcams and other hardware <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

## Hardware Classification: Edge vs. Server
Beyond training and inference, AI hardware is also classified by its operating environment:
*   **Edge AI Chips:** These are placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Server Chips:** Used in data centers, these chips prioritize the cost-performance ratio, with power being a significant portion of the total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. They are higher-end products, often near the leading edge of technology, requiring substantial investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## The Rise of Server-Side AI Accelerators
The market for AI accelerators gained wide prominence after Google's major announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Google's Tensor Processing Unit (TPU):** Google began developing their own chips in 2013 due to the immense computational demands of training and deploying neural networks <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The first TPUs, designed with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
    *   TPUs are Application-Specific Integrated Circuits (ASICs) specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
    *   At its core, a TPU has a matrix multiply unit containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. These MAC units simply multiply two numbers and add them to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   The matrix multiply unit processes subject image data from the host CPU/main memory and millions of neural network weights loaded from DDR3 DRAM <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   Compared to generalized CPUs (like the Intel Haswell) and GPUs (like the [[Nvidia and competition in the AI chip market | Nvidia]] Kepler K80), TPUs have far more MAC units and on-chip memory <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. While not suitable for general tasks like video games <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, their specialization allows Google's first-generation TPU to run *inference* 50 to 30 times faster and 30 to 80 times more [[energy_efficiency_in_ai_hardware | energy efficient]] than contemporaries <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
    *   Google's integration with their machine learning framework, TensorFlow, allows precise hardware customization for software <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This end-to-end system enables capabilities like object searches on years of Google Photos <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   Though not sold, TPU computing power can be rented via Google Cloud <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>, effectively establishing the server AI ASIC industry <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Competition in the Server AI Chip Market
Other companies have quickly followed Google's lead:
*   **Amazon:** As the largest cloud hyperscaler, Amazon announced their own Trainium devices, which are AI *training* accelerators, in December 2020 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Habana:** Founded in 2016 with a data center product for *training* machine learning models, Habana was acquired by Intel in December 2019 for $2 billion <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **[[Nvidia and competition in the AI chip market | Nvidia]]:** Offers its own custom AI hardware like the Tesla V100, an AI processor with over 20 billion transistors and 5,120 cores <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. [[Nvidia and competition in the AI chip market | Nvidia]] maintains a strong competitive advantage through its software <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

The server AI market is intensely competitive, especially for startups, as major buyers develop their own AI chips <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Competition in the Edge AI Chip Market
Half of [[the_ai_and_ai_chip_boom_landscape | the AI chip market]] is composed of specialized AI chips for mobile phones <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>, primarily handling computation-heavy image processing <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
*   **Apple's Neural Engine:** In 2017, the iPhone X's A11 Bionic chip integrated dedicated neural network hardware called the Neural Engine <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. The first iteration had two cores and could perform 600 billion operations per second <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Initially used for Face ID and Animojis, Apple later opened up the second version to users via its Core ML API <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **Other Vendors:** Chip makers like MediaTek are also adding dedicated AI functionality to their mobile processors, such as their Dimensity 5G series <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

While opportunities exist for *inference* on the edge (e.g., IoT, autonomous driving), these devices often have lower profit margins than phones, and the technical challenges for low-power, low-latency use cases are more complex <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

## Future of AI Accelerators
Despite specialized architectures, training a single machine learning model for production can still take hours <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. Future developments include:
*   **[[silicon_photonics_in_ai_chip_development | Silicon Photonics]]:** One suggestion is to implement new AI chips using [[silicon_photonics_in_ai_chip_development | silicon photonics]] <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. Traditional Von Neumann architecture, which separates processor and memory, can slow down neural networks, which are highly parallel <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. [[silicon_photonics_in_ai_chip_development | Silicon photonics]] uses light instead of electricity to send signals, allowing for faster speeds and no additional heating concerns <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Beyond Advanced Nodes:** While Bitcoin mining hardware evolved towards more advanced nodes <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>, it's uncertain if AI accelerators must follow the same path <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. More interesting approaches may involve new ways to achieve similar *inference* or *training* results without requiring an advanced node, such as [[silicon_photonics_in_ai_chip_development | silicon photonics]] or advanced parallelism <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This could help address [[challenges_in_scaling_ai_hardware | challenges in scaling AI hardware]].