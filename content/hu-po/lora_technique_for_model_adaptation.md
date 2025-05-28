---
title: LoRA technique for model adaptation
videoId: vjEPXSCbmDE
---

From: [[hu-po]] <br/> 

The LoRA (Low-Rank Adaptation) technique has gained significant popularity as a method for fine-tuning existing models <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It involves training additional parameters rather than fully retraining the original model <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Developed by Microsoft Corporation, the paper on LoRA was published on October 16, 2021 <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a> <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Despite being "infinity ago" in machine learning years, its approach has stood the test of time and continues to be used widely in open-source fine-tuning repositories <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a> <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Core Concept and Mechanism

Traditionally, adapting [[large language models and their applications | large language models]] to specific tasks involves full fine-tuning, which retrains all model parameters <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This becomes prohibitively expensive for models like GPT-3, with 175 billion parameters, as it requires deploying independent instances of these large models <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a> <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

LoRA addresses this by freezing the pre-trained model weights and injecting trainable rank decomposition matrices into each layer of the [[Application of LoRA in Transformer architectures | Transformer architecture]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a> <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. This means gradients are not pushed into the original model <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Instead, new, smaller model weights, known as trainable rank decomposition matrices, are added and trained <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

*   **Low Rank:** A "rank decomposition matrix" is essentially a smaller weight matrix with a lower rank <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a> <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. The core hypothesis is that the change in weights during model adaptation also has a low intrinsic rank <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a> <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.
*   **Weight Update:** For a pre-trained weight matrix `W₀` (with dimensionality `D x K`), its update `ΔW` is represented as a low-rank decomposition `BA`, where `B` is `D x R` and `A` is `R x K` <a class="yt-timestamp" data-t="00:38:31">[00:38:31]</a> <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>. `R` (the rank) is chosen to be much smaller than `D` and `K` <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.
*   **Initialization:** Matrix `A` is initialized with a random Gaussian distribution, while matrix `B` is initialized to zeros <a class="yt-timestamp" data-t="00:41:33">[00:41:33]</a> <a class="yt-timestamp" data-t="00:41:48">[00:41:48]</a>. This ensures `ΔW = BA` is zero at the beginning of training <a class="yt-timestamp" data-t="00:41:52">[00:41:52]</a>.
*   **Scaling:** `ΔW` is scaled by `Alpha/R`, where `Alpha` is a constant <a class="yt-timestamp" data-t="00:41:57">[00:41:57]</a>. This scaling helps reduce the need to retune hyperparameters when `R` is varied <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>.

## Advantages of LoRA

LoRA offers several significant advantages:

*   **Parameter and Memory Efficiency**: Compared to GPT-3 fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by three times <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a> <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For GPT-3, trainable parameters can be as small as 0.01% of the original model <a class="yt-timestamp" data-t="00:26:10">[00:26:10]</a> <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
*   **No Additional Inference Latency**: When deployed, the trainable LoRA matrices (`BA`) can be explicitly computed and merged with the pre-trained weights (`W₀`) to form `W₀ + BA` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a> <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a> <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. This means there is no extra computational cost or latency during inference <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a> <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a>.
*   **Faster Training**: LoRA allows for a 25% speed-up during training compared to full fine-tuning because it doesn't need to calculate gradients or maintain optimizer states for most parameters <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a> <a class="yt-timestamp" data-t="00:52:07">[00:52:07]</a>.
*   **Efficient Task Switching**: A pre-trained model can be shared and used with many small LoRA modules for different tasks <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. To switch tasks, one can recover the original `W₀` by subtracting the old `BA` and then adding a new `BA` <a class="yt-timestamp" data-t="00:45:46">[00:45:46]</a> <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>. This significantly reduces storage and task-switching overhead <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a> <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>.

## [[Comparison between LoRA and traditional finetuning | Comparison with Other Adaptation Methods]]

LoRA stands apart from other parameter-efficient adaptation strategies like adding adapter layers or optimizing input layer activations (e.g., prefix tuning) <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a> <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>.

*   **Adapters:** Adapter layers, like those used in [[LLaMAAdapter and its role in adapting language models | LLaMAAdapter]], add new modules or layers to the network <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a> <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. While they reduce parameters, they introduce additional compute, leading to increased inference latency, especially in online inference settings with small batch sizes <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a> <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a> <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. LoRA, by merging weights, avoids this latency <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.
*   **Prefix Tuning:** Methods like prefix tuning modify input layer activations by prepending or appending special tokens to the prompt <a class="yt-timestamp" data-t="01:01:18">[01:01:18]</a> <a class="yt-timestamp" data-t="01:01:31">[01:01:31]</a>. However, this is often difficult to optimize, and reserving part of the sequence length for adaptation necessarily reduces the context available for the task <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a> <a class="yt-timestamp" data-t="00:31:45">[00:31:45]</a>.

## Application Areas

LoRA has been successfully applied beyond just [[Large Language Models and their applications | Large Language Models]]:

*   **Language Models**: It has been used for fine-tuning [[large language models and their applications | LLMs]] like Alpaca <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, Roberta, GPT-2, and GPT-3 <a class="yt-timestamp" data-t="00:55:22">[00:55:22]</a> <a class="yt-timestamp" data-t="00:55:26">[00:55:26]</a>.
*   **Image Generation Models**: It's also applicable to image generation models, such as the diffusion models used in Stable Diffusion <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a> <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> <a class="yt-timestamp" data-t="01:49:51">[01:49:51]</a>.

## Performance and Empirical Observations

LoRA performs on par with or even better than full fine-tuning in terms of model quality, despite training significantly fewer parameters <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:57:37">[00:57:37]</a>.

*   **Impact of Model Size**: LoRA's effectiveness appears to be related to model capacity <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>. [[large language models and their applications | Larger models]] like GPT-2 and GPT-3, with their greater number of weights and model capacity, tend to have more "low-rank" properties, making them well-suited for LoRA <a class="yt-timestamp" data-t="01:06:52">[01:06:52]</a> <a class="yt-timestamp" data-t="01:07:26">[01:07:26]</a>. Smaller models like Roberta may have more "squeezed" signals, making low-rank decomposition harder <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>.
*   **Optimal Rank (R)**: The choice of `R` (rank) is often tied to a desired parameter budget <a class="yt-timestamp" data-t="01:25:39">[01:25:39]</a> <a class="yt-timestamp" data-t="01:25:58">[01:25:58]</a>. Surprisingly, a very small rank, such as `R=1`, can suffice and perform competitively in certain tasks like WikiSQL and MultiNLI, suggesting that the intrinsic rank of the update matrix can be very low <a class="yt-timestamp" data-t="01:30:15">[01:30:15]</a> <a class="yt-timestamp" data-t="01:30:23">[01:30:23]</a> <a class="yt-timestamp" data-t="01:30:32">[01:30:32]</a>.
*   **Which Weights to Adapt**: The paper primarily focuses on adapting the query (`WQ`) and value (`WV`) projection matrices within the Transformer's self-attention module, freezing MLP modules <a class="yt-timestamp" data-t="00:46:53">[00:46:53]</a> <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a> <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>. Empirical studies suggest that adapting both `WQ` and `WV` yields the best results <a class="yt-timestamp" data-t="01:27:53">[01:27:53]</a> <a class="yt-timestamp" data-t="01:27:55">[01:27:55]</a>. It's often more beneficial to adapt more weight matrices with a smaller rank than a single type of weight with a larger rank <a class="yt-timestamp" data-t="01:28:02">[01:28:02]</a> <a class="yt-timestamp" data-t="01:28:04">[01:28:04]</a>.

## Limitations

One limitation of LoRA is that it is not straightforward to batch inputs from different tasks (which would use different A and B matrices) in a single forward pass <a class="yt-timestamp" data-t="01:14:24">[01:14:24]</a> <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.

## Future Directions

The paper suggests several avenues for future research:

*   **Combinations**: LoRA could be combined with other efficient adaptation methods for orthogonal improvements <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Mechanism Understanding**: Further research is needed to clarify the underlying mechanism of fine-tuning or LoRA, especially how features learned during pre-training are adapted <a class="yt-timestamp" data-t="01:50:06">[01:50:06]</a> <a class="yt-timestamp" data-t="01:50:13">[01:50:13]</a>.
*   **Optimal Weight Selection**: Currently, heuristics are largely used to select which weight matrices to apply LoRA to <a class="yt-timestamp" data-t="01:50:21">[01:50:21]</a>. More principled methods for this selection could be explored.
*   **Rank Deficiency of `W`**: The rank efficiency of `ΔW` also suggests that the original pre-trained weight matrix `W` itself could be rank-efficient, offering another source of inspiration for future work <a class="yt-timestamp" data-t="01:50:48">[01:50:48]</a> <a class="yt-timestamp" data-t="01:50:55">[01:50:55]</a>.

LoRA represents a significant step forward in [[challenges and benefits of parameterefficient model adaptation | parameter-efficient model adaptation]], offering a practical solution to [[challenges and approaches in adapting large language models for specific tasks | adapting large language models for specific tasks]] without the prohibitive costs of full fine-tuning <a class="yt-timestamp" data-t="01:49:04">[01:49:04]</a>.