---
title: AI accelerator hardware market and its growth
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

The [[ai_and_ai_chip_boom | neural network revolution]], initially driven by NVIDIA's GPU evolution, has led to a demand for specialized hardware. While GPUs perform well with neural network algorithms, they aren't specifically designed for them <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This need has spurred the development of [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerators]], which are hardware customized for running specific AI algorithms <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

Today, the [[ai_and_ai_chip_boom | AI accelerator hardware market]] is estimated to be worth over $35 billion <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Venture capitalists invested nearly $2 billion in AI chip startups in 2021 <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. TSMC views [[ai_and_ai_chip_boom | AI accelerator hardware]] as one of their top secular drivers for future revenue <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Evolution of AI Accelerators

In 2011, a paper presented at the CVPR conference by a team from New York University and Yale University discussed a scalable hardware architecture for big and deep neural networks <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Although GPUs were widely accepted as the de facto standard for running and testing AI algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, the paper highlighted that custom hardware could improve performance and power consumption by two orders of magnitude <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

The paper proposed an architecture that processed each individual step in parallel for computer vision algorithms <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Implementing this data grid architecture on a Xilinx Vertex 6 FPGA (a configurable chip) showed substantial improvements <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. The team also presented a hypothetical 45-nanometer chip design fabricated with an IBM process, which significantly outperformed competitors <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

## Neural Networks and Accelerator Roles

Neural networks are essentially massive mathematical functions that use simple processing elements to model complex relationships between many inputs <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. They are represented with matrices, where input data is multiplied with weight matrices, and then activation functions are applied <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

[[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerators]] play two primary roles:
1.  **Training Phase**: Large datasets are used to determine the weight values for the network's layers <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  **Inference Stage**: The trained neural network function is used to infer a result from input data, such as identifying a dog in a photo <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

Accelerators are more efficient than general-purpose CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the work in neural networks <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Google's 2016 survey found neural networks with up to 100 million weights, underscoring the need for specialized hardware <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Forerunners in AI Hardware

The concept of custom AI hardware caught on, leading to a community of projects:
*   **Dianna (Chinese Academy of Sciences Institute of Computing Technology)**: Launched in 2015, Dianna is tuned for computer vision neural networks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Its 65-nanometer accelerator consumed 400 times less energy than a GPU and was small enough for embedding with commercial image sensors <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. CAS later expanded this into four product lines <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Iris (MIT Project)**: A flexible accelerator for mobile devices running neural networks, with DARPA funding <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Iris's chip focused on inference with pre-trained models, achieving 10 times more energy efficiency than contemporary GPUs <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   **Teradeep**: A startup founded by members of the original 2011 CVPR team <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Their NNX processor aimed to empower old webcams and hardware with deep learning capabilities <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

These early projects primarily focused on inferring results from pre-trained models <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Classification of AI Hardware: Training vs. Inference, Edge vs. Server

The [[ai_and_ai_chip_boom | AI hardware industry]] classifies accelerators based on their function (training or inference) and their operating environment (edge or server) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

*   **Edge AI Chips**: These are placed directly into devices like smartphones, cars, IoT devices, or wearables <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Designers must consider power and size restrictions for this form factor <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Server Chips**: Used in data centers, these chips prioritize the cost-performance ratio, as power is a substantial portion of the chip's total cost of ownership <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. These are typically higher-end products near the leading edge, requiring significant upfront investment <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

## [[impact_of_ai_chip_innovations_by_companies_like_google_and_amazon | Impact of Big Tech Innovations]]

The [[ai_and_ai_chip_boom | AI accelerator market]] gained wide prominence after Google's significant announcement in 2016 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Google's Tensor Processing Unit (TPU)

Google started working on its Tensor Processing Unit (TPU) in 2013, recognizing the immense computational demand of training and deploying neural networks on their servers <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The first TPUs, designed quickly and fabricated with a 28-nanometer process, entered Google's data centers in 2015 and were publicly unveiled in May 2016 <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

TPUs are Application-Specific Integrated Circuits (ASICs) focused on matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. At their core is a matrix multiply unit containing 65,536 multiply-accumulator (MAC) circuits arranged in a 256x256 array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This unit efficiently multiplies two numbers and adds them to an accumulation sum <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

Compared to an 18-core Intel Haswell CPU or NVIDIA Kepler K80 GPU, the TPU has far more MAC units and more on-chip memory for intermediate results <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. While CPUs and GPUs handle generalized tasks, the TPU's specialization allows Google's first generation to run inference 50 to 30 times faster and with 30 to 80 times better energy efficiency than contemporaries <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This specialization saves Google millions of dollars by reducing the need for traditional CPUs and GPUs in their [[ai_boom_and_data_center_demands | data centers]] <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

Google's control over its machine learning software framework, TensorFlow, allows for precise customization of hardware to software <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This enabled Google to build an end-to-end machine learning system, capable of tasks like object searches on years of Google Photos <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Although Google didn't sell TPUs (considering them a competitive advantage), their computing power can be rented via Google Cloud service <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. Google essentially created the server AI ASIC industry <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Other Key Players in Server AI ASICs

Following Google's lead, other companies have developed their own server AI ASICs:
*   **Amazon**: As the largest cloud hyperscaler with AWS, Amazon already proved its chip design capabilities with its Graviton ARM-based CPUs <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. In December 2020, they announced Trainium devices, their own [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI training accelerators]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Intel**: Acquired Habana, a company founded in 2016 with a data center product for training machine learning models, for $2 billion in December 2019 <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **NVIDIA**: Possesses its own custom AI hardware, the Tesla V100, an AI processor with over 20 billion transistors and 5,120 cores <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. Their strong software competitive advantage makes them a formidable player <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

This intense competition between billion-dollar startups and multi-billion-dollar tech giants makes navigating the data center market challenging for new entrants <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

### Edge AI Chips and Mobile Integration

The [[ai_and_ai_chip_boom | AI chip market]] also sees about half its value in specialized AI chips for mobile phones <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>, primarily handling computation-heavy image processing <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Mobile CPU processors are also expanding their onboard neural networking hardware to capture this market <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

Apple led this integration in 2017 with the iPhone X A11 Bionic chip, which featured a dedicated "Neural Engine" <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. The first iteration had two cores and could perform 600 billion operations per second <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. Apple's control over its software stack, including the Core ML API, made this integration ideal <a class="yt-timestamp" data-t="00:12:46">[00:12:46]</a>. Other chip vendors, like Taiwanese fabless chip maker MediaTek with their Dimensity 5G mobile processors, are also adding dedicated AI functionality <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

Opportunities for inference on the edge remain in IoT devices, autonomous driving, and other low-power, low-latency use cases <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

## Future Outlook for AI Accelerators

Even with specialized architectures, current [[ai_and_ai_chip_boom | AI accelerators]] can take hours or longer to train a single machine learning model for production <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>. One suggestion for future development is to implement new [[ai_and_ai_chip_boom | AI chips]] using silicon photonics <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

Current data center servers operate on a von Neumann architecture, where the CPU processes information separately from the memory bank that stores data and instructions <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This separation, known as the "von Neumann bottleneck," slows things down <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. Silicon photonics, which uses light instead of electricity to send signals, can travel faster through optical fiber and without additional heating concerns <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

It is interesting to draw a [[comparison_of_ai_accelerator_industry_with_bitcoin_mining | comparison between the AI accelerator hardware industry and the Bitcoin mining hardware industry]] <a class="yt-timestamp" data-t="00:14:44">[00:14:44]</a>. Both have followed a similar path, starting with CPUs, then GPUs, and moving towards increasingly powerful ASICs <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. For Bitcoin miners, the next step has typically been to adopt a more advanced node <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. However, it's uncertain if future [[ai_and_ai_chip_boom | AI accelerators]] must follow the same path <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>. If they do, large chip companies like NVIDIA will maintain an advantage due to their access to advanced nodes and resources <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The more intriguing approaches for [[ai_and_ai_chip_boom | AI accelerators]] will be those that find new ways to achieve similar performance results for inference or training without relying solely on advanced nodes, possibly through innovations like silicon photonics or advanced parallelism <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.