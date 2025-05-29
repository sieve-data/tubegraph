---
title: Neural network revolution and role of GPUs
videoId: L0948yq2Hqk
---

From: [[asianometry]] <br/> 

The evolution of [[Nvidias innovation with general processing unit concept | Nvidia's]] Graphics Processing Units (GPUs) initiated the [[AI and AI chip boom | neural network revolution]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. While GPUs were effective at running neural network algorithms, they were not specifically designed for this purpose <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This led to the development of specialized hardware, dubbed [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerators]], which are customized for running specific AI algorithms <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## GPUs as the De Facto Standard
By 2011, the AI research community had widely accepted GPUs as the de facto standard hardware for running and testing their algorithms <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Limitations and the Rise of Specialized Hardware
Despite their initial impact, GPUs, along with Central Processing Units (CPUs), are designed for more generalized tasks <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. In contrast, custom hardware can significantly improve performance and power consumption for neural networks <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Neural Network Operations
A neural network functions as a massive mathematical operation, using simple processing elements to model complex relationships between many inputs <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Data is represented as matrices, which are then processed through the network's layers by multiplying input matrices with weight matrices and applying activation functions <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

Neural network accelerators outperform generalized hardware like CPUs and GPUs because they are specifically tuned to handle matrix multiplication and convolution operations, which constitute about 90% of the computational work <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. For example, Google's Tensor Processing Unit (TPU), an [[role_of_ai_accelerators_in_neural_network_training_and_inference | ASIC]] (Application Specific Integrated Circuit), focuses primarily on matrix multiplication <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Comparison to Custom Hardware
A 2011 paper presented at CVPR by a team from New York and Yale universities highlighted that custom hardware could achieve two orders of magnitude improvement in performance and power consumption over GPUs <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. For example, the Dianna chip from the Chinese Academy of Sciences Institute of Computing Technology, developed in 2015, consumed 400 times less energy than a GPU for computer vision tasks <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## [[Nvidia and AI chip competition | Nvidia's]] Role and Competition
[[Nvidias rise in the graphics card industry | Nvidia]] remains a formidable player in the AI chip market <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

### [[Nvidia and AI chip competition | Nvidia's]] Custom AI Hardware
[[Nvidia and AI chip competition | Nvidia]] has developed its own custom AI hardware, such as the Tesla V100. This is described not necessarily as a GPU, but as an [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI processor]] featuring over 20 billion transistors and 5,120 cores <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

### Market Dynamics
The emergence of custom [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerator]] hardware has created intense competition. Major cloud hyperscalers like Google and Amazon have started designing their own [[impact_of_ai_chip_innovations_by_companies_like_google_and_amazon | AI chips]], challenging traditional GPU providers <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This means the largest buyers are now manufacturing their own chips, making the data center market increasingly competitive for outside vendors <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

Additionally, the mobile phone market, which accounts for half of the specialized AI chip market, is seeing mobile CPU processors integrate their own on-board neural networking hardware <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. For instance, Apple's iPhone X A11 Bionic chip, released in 2017, included a dedicated "Neural Engine" <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

## Future Outlook
The path for future [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerators]] is still evolving. While some suggest moving to more advanced manufacturing nodes, similar to the progression seen in Bitcoin mining hardware from CPUs to GPUs to ASICs <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>, this approach might give larger chip companies like [[Nvidia and AI chip competition | Nvidia]] a persistent advantage due to their resources <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.

A more intriguing direction for [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI accelerators]] could involve finding novel ways to achieve desired results for inference or training without relying solely on advanced nodes <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This could include technologies like silicon photonics or advanced parallelism <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.