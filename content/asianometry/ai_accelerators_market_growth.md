---
title: AI accelerators market growth
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

The market for [[the_ai_and_ai_chip_boom_landscape|AI accelerator]] hardware is currently estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. In 2021, venture capitalists invested nearly $2 billion in [[the_ai_and_ai_chip_boom_landscape|AI chip]] startups <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC views [[the_ai_and_ai_chip_boom_landscape|AI accelerator]] hardware as one of its primary drivers for future revenue <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Evolution from GPUs to Custom Hardware

The advent of [[Nvidia and competition in the AI chip market|Nvidia]]'s GPUs significantly advanced the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs are effective for running neural network algorithms, they were not specifically designed for this purpose <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led to companies developing custom hardware, known as [[the_ai_and_ai_chip_boom_landscape|AI accelerators]], specifically for [[the_ai_and_ai_chip_boom_landscape|AI algorithms]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Early Research and Development

In 2011, a paper presented at the CVPR conference by a New York University and Yale University team discussed a scalable hardware architecture for large and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The paper suggested that custom hardware could improve performance and power consumption by two orders of magnitude compared to GPUs, which had become the de facto standard for running and testing [[the_ai_and_ai_chip_boom_landscape|AI algorithms]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

An architecture that processed each step in parallel was proposed and implemented on a Z-Link's Vertex 6 [[industry_shifts_and_acquisitions_in_the_fpga_market|FPGA]], demonstrating substantial improvements <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Although [[industry_shifts_and_acquisitions_in_the_fpga_market|FPGAs]] are primarily for development and testing and tend to be slower, a hypothetical 45-nanometer chip design fabricated with an IBM process significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### How AI Accelerators Work

Neural networks are complex mathematical functions that model relationships between many inputs using simple processing elements <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They operate by processing input data through many layers, involving matrix multiplication and activation functions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

[[the_ai_and_ai_chip_boom_landscape|AI accelerators]] serve two main roles:
*   **Training Phase**: Using large datasets to determine weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Inference Stage**: Using the trained neural network to derive a result from input data <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

These accelerators are more efficient than general-purpose CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the workload <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Given that some neural networks can have up to 100 million weights, building specialized hardware is logical <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Early Notable Projects

A small community of [[the_ai_and_ai_chip_boom_landscape|AI hardware]] projects emerged, including:
*   **Shudianna (Chinese Academy of Sciences Institute of Computing Technology)**: A 2015 project tuned for computer vision neural networks. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded use <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **IRIS (MIT project with DARPA funding)**: A flexible accelerator for mobile devices running neural networks, focusing on inference with 10 times more energy efficiency than contemporary GPUs <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>, <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **TeraDeep**: A startup founded by members of the original CVPR 2011 team, whose NNX processor aimed to give deep learning capabilities to older webcams and hardware <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

These early projects primarily focused on inferring results from pre-trained models <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Market Classification: Edge vs. Server

The [[the_ai_and_ai_chip_boom_landscape|AI hardware]] industry classifies accelerators based on their operational environment <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:

*   **Edge AI Chips**: Integrated directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Server Chips**: Used in data centers, where the primary concern is the cost-performance ratio, with power being a significant portion of the total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. These are higher-end products that require substantial upfront investment for development <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

All [[the_ai_and_ai_chip_boom_landscape|AI accelerators]] are classified by these two axes: whether they perform training or inference, and whether they operate on the edge or in a server/data center <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Google's Entry and the Server AI ASIC Industry

While initially mostly research projects, the [[the_ai_and_ai_chip_boom_landscape|AI accelerator]] market gained prominence with Google's 2016 announcement <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Google began developing its own chips in 2013 due to the immense computational demands of training and deploying neural networks <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>, <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

They developed the Tensor Processing Unit (TPU), an Application Specific Integrated Circuit (ASIC) specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. The first TPUs, designed quickly and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>, <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

The TPU's core is a matrix multiply unit containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This design ensures constant use of the matrix multiply unit <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Compared to an 18-core Intel Haswell CPU or an [[Nvidia and competition in the AI chip market|Nvidia]] Kepler K80 GPU, the TPU has far more MAC units and on-chip memory for intermediate results <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>, <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

Google's first-generation TPU could run inference 50 to 30 times faster and with 30 to 80 times better energy efficiency than its contemporaries, saving the company millions of dollars in their data centers <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Google's control over its TensorFlow machine learning software framework allows for precise hardware customization <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This end-to-end system enables advanced capabilities like object searches on years of uploaded Google Photos <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

Google did not sell its TPUs directly, considering them a competitive advantage, but offered their computing power through Google Cloud services <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Google effectively established the server [[the_ai_and_ai_chip_boom_landscape|AI ASIC]] industry <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Competitive Landscape

### Server Market Competition

Following Google, other companies have entered the server [[the_ai_and_ai_chip_boom_landscape|AI accelerator]] market:
*   **Amazon**: As the largest cloud hyperscaler with AWS, Amazon announced its own Trainium devices, [[the_ai_and_ai_chip_boom_landscape|AI training]] accelerators, in December 2020 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>, <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Intel**: Acquired Habana, a company founded in 2016 for data center machine learning training products, for $2 billion in December 2019 <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **[[Nvidia and competition in the AI chip market|Nvidia]]**: Offers its own custom [[the_ai_and_ai_chip_boom_landscape|AI hardware]], the Tesla V100, an [[the_ai_and_ai_chip_boom_landscape|AI processor]] with over 20 billion transistors and 5,120 cores <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. [[Nvidia and competition in the AI chip market|Nvidia]] maintains a strong software competitive advantage <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

This intense competition from large tech giants makes it challenging for startups in the [[financial_sustainability_of_ai_investments|AI server market]] <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. When major buyers start developing their own [[the_ai_and_ai_chip_boom_landscape|AI chips]] and prioritizing their own instances, it raises concerns for external providers <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Edge Market Opportunities

Approximately half of the [[the_ai_and_ai_chip_boom_landscape|AI chip market]] is in specialized [[the_ai_and_ai_chip_boom_landscape|AI chips]] for mobile phones, which likely handle the increasing computational demands of image processing <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Mobile CPU processors are also incorporating on-board neural networking hardware to capture this market <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

*   **Apple**: Led the way in 2017 with the iPhone X A11 Bionic chip, which included a dedicated neural engine <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This first iteration had two cores and could perform 600 billion operations per second <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Apple's control over its software stack facilitates this integration <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **MediaTek**: This Taiwanese fabless chip maker is adding dedicated [[the_ai_and_ai_chip_boom_landscape|AI functionality]] to its chips, such as the Dimensity 5G mobile processors <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

While opportunities for inference on the edge remain in IoT devices and autonomous driving, mobile devices have distinct margin profiles <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Low power and low latency use cases present complex technical challenges <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.

## Future Directions for AI Accelerators

Despite specialized architectures, training a single machine learning model for production can still take hours or longer <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. One suggestion for future [[the_ai_and_ai_chip_boom_landscape|AI chips]] is the implementation of silicon photonics <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>.

Current server architectures, based on the von Neumann model, separate the processor and memory, creating bottlenecks <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>, <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>. Silicon photonics uses light instead of electricity to send signals, enabling faster data transmission through optical fiber without additional heating concerns <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

The [[the_ai_and_ai_chip_boom_landscape|AI accelerator]] hardware industry can be compared to the Bitcoin mining hardware industry, which also evolved from CPUs to GPUs and then to increasingly powerful ASICs <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. For Bitcoin miners, the next step has typically been to move to a more advanced node <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. However, it is uncertain if future [[the_ai_and_ai_chip_boom_landscape|AI accelerators]] must follow this path, as major chip companies like [[Nvidia and competition in the AI chip market|Nvidia]] would always have superior access to resources for advanced nodes <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

The most promising approach for [[the_ai_and_ai_chip_boom_landscape|AI accelerators]] may lie in finding new ways to achieve similar inference or training results without relying on advanced nodes, possibly through technologies like silicon photonics or advanced parallelism <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.