---
title: Quantization for large language models
videoId: 6wEVz0wkhCM
---

From: [[hu-po]] <br/> 

## What is Quantization?
[[quantization_in_large_language_models | Quantization]] is the process of reducing the amount of information used to represent data, similar to how an image can be reduced from 24 bits per pixel to 8 or even 1 bit per pixel, making it grainier but still recognizable <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Applied to neural networks, it means reducing the precision of the numerical values (weights) that constitute the model <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

## Why Quantize Machine Learning Models?
There are four primary reasons to quantize neural networks and [[large_language_models_and_their_applications | Large Language Models]] <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>:

*   **Memory Usage**: Lower data type precision drastically reduces the memory footprint. This allows larger models, like CodeLlama-34B, to fit on consumer GPUs <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Power Consumption**: Smaller neural networks consume less power for inference, which could become significant with widespread AI companion usage <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Latency**: Reduced size leads to faster computation and fetching, making nearly all computer operations quicker <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Silicon Area**: Requires less physical space for computation <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

These benefits make [[quantization_and_optimization_in_machine_learning | quantization and optimization in machine learning]] a critical area of research <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## The QuIP Paper: 2-bit Quantization with Guarantees
The paper "QuIP: 2-Bit Quantization of Large Language Models with Guarantees" proposes a novel [[2bit_quantization_for_machine_learning_models | 2-bit quantization]] technique for LLMs <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a> <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Published as a preprint on July 25, 2023, it builds upon previous [[quantization_in_large_language_models | quantization in large language models]] research, including QLoRA <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

QuIP focuses on *post-training parameter quantization*, meaning it quantizes an already trained model for faster and cheaper inference, unlike quantization-aware training <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. The paper uniquely offers theoretical guarantees that their [[quantization_and_optimization_in_machine_learning | quantization technique]] is optimal within a general class of rounding methods <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a> <a class="yt-timestamp" data-t="01:21:09">[01:21:09]</a>.

### Key Concepts in QuIP

#### Incoherence
The core insight of QuIP is that [[quantization in large language models | quantization]] is most effective when weight and proxy Hessian matrices are "incoherent" <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. Incoherence in this context means that the matrices are basically separate and non-correlated <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. The goal is to ensure that the weights (values of neurons) and the directions important for rounding accuracy (represented by the Hessian matrix, which indicates the curvature of the loss landscape) are not too large in any one coordinate and are unrelated to each other <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a> <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

To achieve this, QuIP employs a "scrambling" process where the weight matrix and the Hessian matrix are multiplied by random orthogonal matrices <a class="yt-timestamp" data-t="01:49:45">[01:49:45]</a> <a class="yt-timestamp" data-t="01:50:24">[01:50:24]</a>. Orthogonal matrices preserve distance and angles, essentially rotating and possibly reflecting the data in space <a class="yt-timestamp" data-t="01:47:06">[01:47:06]</a>. The Kronecker product is used as a trick to efficiently create large random orthogonal matrices from smaller ones <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a>.

#### Adaptive Rounding
The first step of QuIP is an adaptive rounding procedure <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>. This procedure, based on the AdaRound paper, determines whether to round a weight up or down intelligently, rather than simply to the nearest value <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. It approximates the task loss of the neural network using a Taylor series expansion, specifically a quadratic proxy objective, which is good for local approximation around the current weights <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a> <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>. This rounding task is framed as a quadratic unconstrained binary optimization problem and simplified to a layer-wise local loss, optimized with a soft relaxation <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a> <a class="yt-timestamp" data-t="00:32:27">[00:32:27]</a>. This involves using continuous variables (e.g., probability of rounding up) that can be adjusted via gradient-based methods using a small amount of unlabeled calibration data, allowing for intelligent rounding <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

### QuIP's Two Steps
QuIP combines two main steps <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>:
1.  **Optimal Adaptive Rounding Procedure**: Minimizing a quadratic proxy objective using an estimate of the Hessian <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>.
2.  **Efficient Pre- and Post-processing**: Ensuring the incoherence of weight and Hessian matrices through multiplication by random orthogonal matrices <a class="yt-timestamp" data-t="01:51:52">[01:51:52]</a>. This "scrambling" disrupts any existing patterns between the matrices <a class="yt-timestamp" data-t="01:49:45">[01:49:45]</a>.

The [[quantization_techniques_for_transformers | quantization process]] is performed one Transformer block at a time <a class="yt-timestamp" data-t="00:55:41">[00:55:41]</a>.

## Experimental Findings
The QuIP researchers evaluated their method on the OPT family of [[large_language_models_and_their_applications | Large Language Models]], ranging up to 30 billion parameters <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. The calibration data set used was 128 random 2048-token segments from the generic C4 data set, ensuring no task-specific data was viewed during quantization <a class="yt-timestamp" data-t="00:54:23">[00:54:23]</a>. All models were quantized on a single GPU with up to 48 GB of memory <a class="yt-timestamp" data-t="00:53:50">[00:53:50]</a>.

### Comparison to OptQ
QuIP consistently outperformed OptQ and other baselines across all model sizes and evaluation tasks <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>.

For OptQ, reducing precision from 3-bit to 2-bit drastically increased perplexity (worse performance) for the OPT models <a class="yt-timestamp" data-t="01:04:07">[01:04:07]</a> <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>. However, QuIP achieved "viable" [[2bit_quantization_for_machine_learning_models | 2-bit quantization]] results <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>.

### Performance and Model Size
A remarkable finding was that the performance gap between [[2bit_quantization_for_machine_learning_models | 2-bit]] QuIP and full 16-bit precision *decreases* as model size increases <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a> <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. This suggests that larger models are more resistant to [[quantization in large language models | quantization]] <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a>.

### Ablation Studies
Ablation studies showed that all sub-steps within QuIP's incoherence processing and adaptive rounding contribute to the overall performance, indicating a "magical combination" rather than a single dominant factor <a class="yt-timestamp" data-t="01:08:57">[01:08:57]</a>.

## Implications and Future Outlook
The ability to perform [[2bit_quantization_for_machine_learning_models | 2-bit quantization]] for [[large_language_models_and_their_applications | Large Language Models]] with minimal accuracy loss has significant implications:

*   **Cost Reduction**: Inference budgets for services like ChatGPT could be halved, leading to substantial savings <a class="yt-timestamp" data-t="01:06:58">[01:06:58]</a>.
*   **Feasibility of Extreme Quantization**: The trend of larger models being more amenable to [[quantization_in_large_language_models | quantization]] hints at the possibility of 1-bit quantization for future, even larger, models (e.g., trillion-parameter models) <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a> <a class="yt-timestamp" data-t="01:56:32">[01:56:32]</a>.
*   **Intelligence in Connectivity**: This robustness to quantization may suggest that the "intelligence" in very large models primarily resides in their connectivity patterns rather than the precise numerical values of their weights <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>. This aligns with concepts like the Lottery Ticket Hypothesis, where neural networks can be drastically pruned (reducing connections) while maintaining performance <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>.

## Limitations
Despite its theoretical guarantees and promising results, QuIP's current formulation has limitations <a class="yt-timestamp" data-t="01:23:20">[01:23:20]</a>:
*   The proxy objective (Taylor series approximation) does not account for interactions between different blocks of a Transformer, or even layers within a block <a class="yt-timestamp" data-t="01:23:20">[01:23:20]</a>. The computational cost of including such interactions is also unclear <a class="yt-timestamp" data-t="01:23:56">[01:23:56]</a>.
*   The experimental evidence is limited to the OPT family of models <a class="yt-timestamp" data-t="01:14:09">[01:14:09]</a>. While the theoretical guarantees are broad, further empirical validation on other [[large_language_models_and_their_applications | Large Language Models]] (e.g., Llama) would strengthen the conclusions <a class="yt-timestamp" data-t="01:14:36">[01:14:36]</a>.