---
title: Hyperparameters and hardware considerations in MoEs
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 
The development of Mixture of Experts (MoE) models represents a significant advancement in [[AI algorithms and computational constraints | AI algorithms]], allowing for the scaling of model capacity without proportionate increases in training or inference costs <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. While larger models generally require more computational resources for training and inference, leading to higher time and memory complexity <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>, MoEs offer a promising alternative by leveraging the sparsity inherent in many neural networks <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

Despite their benefits, traditional MoEs have faced issues such as training instability, token dropping, limitations in scaling the number of experts, and ineffective fine-tuning <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. The "SoftMoE" approach, a fully [[Differentiability in MoEs | differentiable]] sparse [[Transformer models and MoEs | Transformer]], aims to mitigate these challenges, enabling larger model capacity at a lower inference cost by processing only a subset of combined tokens <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.

## Hyperparameters in MoEs
Key hyperparameters in MoE architectures include the number of experts (`n`) and the number of slots (`p`) per expert <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. These choices are not arbitrary but are typically influenced by the available [[Hardware infrastructure and computational challenges | hardware infrastructure]] <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>.

The total number of slots is a critical hyperparameter that directly determines the computational cost of an MoE layer <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. For example, if the number of slots per expert (`p`) is chosen as `M/N` (where `M` is the number of tokens and `N` is the number of experts), the FLOPs (floating point operations per second) can be matched to that of an equivalently dense Transformer <a class="yt-timestamp" data-t="01:08:22">[01:08:22]</a>.

Experiments with SoftMoE have shown that one slot per expert tends to be the optimal configuration for performance <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>. This suggests that distributing capacity across more, smaller experts is more effective than fewer experts with multiple slots, which can lead to redundant information gains <a class="yt-timestamp" data-t="01:33:55">[01:33:55]</a>.

Furthermore, SoftMoE appears to mitigate performance degradation seen in other MoE algorithms when increasing the number of experts, allowing for continuous performance improvement with more experts without a significant increase in training time <a class="yt-timestamp" data-t="02:00:42">[02:00:42]</a>.

## Hardware Considerations
The selection of hyperparameters, particularly the number of experts and slots, is heavily dependent on the specific [[Hardware for AI training and deployment | hardware]] being used <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>. This includes considering factors like:
*   Whether the model runs on a server rack with HPUs (Hardware Processing Units), a single GPU, or a distributed system with varying memory capacities across different GPUs <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>.
*   The type of interconnects used between devices, as these can add overhead not captured by simple FLOPs measurements <a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>.

For large MoE models, which often exceed the memory capacity of a single device, distributed computing techniques like model parallelism are employed <a class="yt-timestamp" data-t="01:18:31">[01:18:31]</a>. While this adds overhead, it's a necessary compromise for scaling <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

SoftMoE has demonstrated significant advantages in terms of inference speed and computational cost <a class="yt-timestamp" data-t="01:52:31">[01:52:31]</a>. It can be trained for longer periods without overfitting, leading to higher quality models even with smaller backbones <a class="yt-timestamp" data-t="01:50:41">[01:50:41]</a>. This efficiency makes MoEs, particularly SoftMoE, highly relevant for industry needs requiring faster inference, such as in robotics for real-time control loops <a class="yt-timestamp" data-t="02:21:12">[02:21:12]</a>.

The interaction between different training parameters, such as the learning rate, learning rate schedule, and batch size, also adds to the complexity. Optimal configurations for these parameters in MoEs are still an active area of research <a class="yt-timestamp" data-t="01:51:11">[01:51:11]</a>.