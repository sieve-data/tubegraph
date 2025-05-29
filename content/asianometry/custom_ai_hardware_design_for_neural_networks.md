---
title: Custom AI hardware design for neural networks
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

While [[evolution_of_ai_hardware_and_gpus | Nvidia]]'s GPUs catalyzed the neural network revolution, they were not specifically designed for neural network algorithms <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led to the development of specialized hardware, known as AI accelerators, customized for running specific AI algorithms <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion today <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Emergence of Custom Hardware

In 2011, a team from New York University and Yale University presented a paper at the CVPR conference, proposing a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. At this time, GPUs were the de facto standard for running and testing AI algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, the paper suggested that custom hardware could significantly improve performance and [[energy_efficiency_in_ai_hardware | power consumption]] by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

Traditionally, deep learning models process images through a sequential pipeline within a neural network <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The 2011 paper introduced an architecture that processed each individual step in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (Field-Programmable Gate Array), a chip type allowing for custom configurations, and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Although FPGAs are slower development devices, the team also presented a hypothetical 45-nanometer chip design that significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

### Understanding Neural Networks and their Hardware Needs

A neural network is fundamentally a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Neural networks are represented by matrices <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. Input data (e.g., an image turned into a matrix) is sent through the network's layers by multiplying input matrices with weight matrices and then applying an "activation function" <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

AI accelerators are more effective than general-purpose CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, which constitute approximately 90% of the computational work <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. In 2016, Google noted that some neural networks had up to 100 million weights, underscoring the need for specialized hardware <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### [[ai_inference_versus_training_hardware | Training vs. Inference]]

AI accelerators serve two primary roles <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>:
1.  **Training Phase:** Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage:** When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Edge vs. Server Environments

The [[ai_inference_versus_training_hardware | AI hardware industry]] also classifies chips based on their operating environment <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>:
*   **Edge AI Chips:** Integrated directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size constraints for these <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Server Chips:** Primarily concerned with cost-performance ratio for data centers <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Power consumption is a significant part of the total cost of ownership <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. These are typically higher-end products that require substantial investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

All AI accelerators are classified along these two axes: training or inference, and edge or server <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Early Forerunners in AI Hardware

Before Google's major announcement, AI accelerators were largely research projects <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>:
*   **Dianna (2015):** A project from the Chinese Academy of Sciences Institute of Computing Technology, tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough to be embedded with commercial image sensors <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Iris:** An MIT project (with DARPA funding) for running inferences on images using pre-trained models on mobile devices <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It offered 10 times more [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **TeraDeep:** A startup founded by members of the original 2011 CVPR team <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Their NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

These early projects primarily focused on inferring results from pre-trained models <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

## The Google TPU and the ASIC Era

The AI accelerator market gained wide prominence after Google's significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Google began working on the Tensor Processing Unit (TPU) in 2013, recognizing the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

TPUs are a type of ASIC (Application-Specific Integrated Circuit) <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>, specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. At its core, the TPU has a matrix multiply unit containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. MAC units are designed to perform a single operation: multiply two numbers and add the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU processes input image data and the neural network's weights, loaded from attached DDR3 DRAM memory, through its matrix multiply unit <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. Compared to an 18-core Intel Haswell CPU or [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]] Kepler K80 GPU of the time, the TPU had significantly more MAC units and on-chip memory for intermediate results <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. While CPUs and GPUs handle more generalized tasks, the TPU's specialized design ensures its matrix multiply unit is in constant use <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Recent TPU iterations can perform trillions of floating-point operations per second <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Google's first-generation TPU could run [[ai_inference_versus_training_hardware | inference]] 50 to 30 times faster and achieve 30 to 80 times better [[energy_efficiency_in_ai_hardware | energy efficiency]] than its contemporaries <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. By filling their data centers with TPUs, Google saved millions by reducing their reliance on CPUs and GPUs <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. Google's control over its machine learning software framework, TensorFlow, allows for precise hardware-software customization <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This end-to-end system enables advanced capabilities like object searches in Google Photos <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Google did not sell its TPUs directly, viewing them as a competitive advantage, but offered their computing power through Google Cloud <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.

## [[the_ai_and_ai_chip_boom_landscape | Competition and Market Dynamics]]

Google essentially pioneered the server AI ASIC industry <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Other companies swiftly followed suit:
*   **Amazon:** The largest cloud hyperscaler (AWS) developed its own Trainium devices, which are [[ai_inference_versus_training_hardware | AI training]] accelerators, announced in December 2020 <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. They also have Graviton chips, ARM-based CPUs offering an alternative to Intel server CPUs <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Habana:** Founded in 2016 with a data center product for training machine learning models, acquired by Intel in December 2019 for $2 billion <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]]: Possesses its own custom AI hardware, such as the Tesla V100, which is an AI processor with over 20 billion transistors and 5,120 cores <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. Their strong software competitive advantage makes them a formidable player <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

The intense competition among billion-dollar startups and multi-billion dollar tech giants makes navigating the server AI market challenging for outsiders, especially as major buyers develop their own AI chips <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

On the "edge" side, half of the AI chip market resides in specialized AI chips for mobile phones <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. Mobile CPU processors are also incorporating and expanding their on-board neural networking hardware to capitalize on this opportunity <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
*   **Apple:** Led the way in 2017 with the iPhone X A11 Bionic chip, which included a dedicated "Neural Engine" <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The first iteration had two cores and could perform 600 billion operations per second <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Apple's control over its software stack facilitates this ideal integration <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>.
*   **Other Chip Vendors:** Companies like MediaTek are also adding dedicated AI functionality to their chips, such as their Dimensity 5G mobile processors <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

Significant opportunities remain for [[ai_inference_versus_training_hardware | inference]] on the edge, including IoT devices and autonomous driving <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. However, few mobile devices offer the margin of phones, and developing for low-power, low-latency use cases can be technically trickier <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

## Future Directions and [[challenges_in_scaling_ai_hardware | Challenges in Scaling AI Hardware]]

Even with specialized architectures, training a single machine learning model for production can take hours or longer <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. One suggestion for future AI chips is to implement [[silicon_photonics_in_ai_chip_development | silicon photonics]] <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

Current data center servers largely operate on the [[von_neumann_architecture_vs_brain_computing | Von Neumann architecture]] (CPU processing information separate from memory) <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. Neural networks, being highly parallel, challenge this architecture because the separation between processor and memory slows things down significantly <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.

[[silicon_photonics_in_ai_chip_development | Silicon photonics]] products use light instead of electricity to send signals, allowing for faster travel through optical fiber and without additional heating concerns <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware industry]] can be compared to the Bitcoin mining hardware industry, which also transitioned from CPUs to GPUs and then to increasingly powerful ASICs <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. For Bitcoin miners, the next step was often moving to more advanced manufacturing nodes <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. However, it's uncertain if future AI accelerators must follow the same path <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. If so, large chip companies like [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]] would retain greater access and resources <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The more interesting approach for AI accelerators may involve companies finding new ways to achieve similar [[ai_inference_versus_training_hardware | inference]] or [[ai_inference_versus_training_hardware | training]] results without relying on advanced nodes, possibly through [[silicon_photonics_in_ai_chip_development | silicon photonics]] or advanced parallelism <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.