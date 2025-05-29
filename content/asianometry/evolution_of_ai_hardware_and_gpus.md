---
title: Evolution of AI hardware and GPUs
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.# Evolution of AI Hardware and GPUs

Nvidia's GPU evolution initiated the neural network revolution <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs run neural network algorithms well, they were not specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led companies to develop hardware customized for running specific AI algorithms, known as AI accelerators <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

The [[the_ai_and_ai_chip_boom_landscape | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, with venture capitalists pouring nearly $2 billion into AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC considers AI accelerator hardware one of their top secular revenue drivers for the near future <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## GPUs and the Emergence of Custom Hardware

By 2011, the AI research community largely accepted GPUs as the de facto standard hardware for running and testing algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. However, a paper presented at the 2011 CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This paper suggested that [[custom_ai_hardware_design_for_neural_networks | custom hardware]] could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step of a neural network in parallel, applying it to a computer vision algorithm <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. They implemented this "data grid architecture" on a Xilinx Vertex 6 FPGA (a type of chip allowing for custom configurations) and observed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design that, when fabricated with an IBM process, significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Understanding Neural Networks and AI Accelerators

At its core, a neural network is a complex mathematical function that uses simple processing elements to model intricate relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data (e.g., an image turned into a matrix) is sent through layers by multiplying input matrices with weight matrices, and then applying activation functions to the resulting values <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

AI accelerators play two primary roles:
1.  **Training Phase**: Using large datasets to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: When the trained neural network function is used to infer a result from input data (e.g., identifying a dog in a photo) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Given that some neural networks had up to 100 million weights as surveyed by Google in 2016 <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, building custom hardware for these calculations makes sense <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Early AI Hardware Projects

The concept of custom AI hardware gained traction, leading to the development of several projects:

*   **Dianna (2015)**: A project by the Chinese Academy of Sciences Institute of Computing Technology, Dianna was a piece of hardware tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedded applications <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The Chinese Academy of Sciences (CAS) later expanded their hardware into four lines for basic, multi-configuration, training/learning, and computer vision purposes <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris Flexible Accelerator**: An MIT project funded by DARPA, Iris's chip focused on running inferences on images using a pre-trained model <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. It achieved 10 times greater [[energy_efficiency_in_ai_hardware | energy efficiency]] than contemporary GPUs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
*   **Teradeep (NNX)**: Founded by members of the original CVPR 2011 team, Teradeep's NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

A common theme among these early projects was their focus on [[ai_inference_versus_training_hardware | inferring results from pre-trained models]] <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

## Classification of AI Hardware

The AI hardware industry classifies chips based on two axes:
1.  **Training vs. Inference**: As discussed above <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  **Environment of Operation (Edge or Server)**:
    *   **Edge AI Chips**: Placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   **Server Chips**: Companies prioritize the cost-performance ratio, with power being a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are higher-end products, often near the leading edge of technology, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## Google's Entry: The Tensor Processing Unit (TPU)

AI accelerators remained mostly research projects until Google made a significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Google began considering building its own chips in 2006, but the effort gained momentum in 2013 due to the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This led to the development of the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

The first TPUs, quickly designed and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. TPUs are Application-Specific Integrated Circuits (ASICs), specifically designed for matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their heart is a Matrix Multiply Unit (MMU) containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. A MAC circuit performs one task: multiplying two numbers and adding the result to an accumulation sum <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

The TPU's design ensures the MMU is in constant use <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.