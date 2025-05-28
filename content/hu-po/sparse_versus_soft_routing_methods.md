---
title: Sparse versus soft routing methods
videoId: _epq9VsViJc
---

From: [[hu-po]] <br/> 

Mixture of Experts (MoE) architectures are a promising alternative to traditional, dense Transformer models, enabling significant scaling of model capacity without a proportional increase in training or inference costs <a class="yt-timestamp" data-t="04:12:06">[04:12:06]</a>. This approach replaces dense feed-forward network (FFN) layers with multiple independent FFNs, known as "experts" <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. The core idea behind MoEs stems from the observation that much of the compute in large neural networks is wasted on calculations that ultimately have little impact on the final output, as many neurons have activations very close to zero <a class="yt-timestamp" data-t="11:43:00">[11:43:00]</a>. By selectively activating parts of the model for specific inputs, MoEs aim to achieve better answers at a lower computational cost <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.

## Sparse Mixture of Experts

Earlier work in MoEs, often referred to as "sparse MoEs," originated from Google DeepMind <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. These architectures utilize a "router" to assign input tokens (or patches in vision models) to specific experts <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. This routing mechanism typically involves a [[continuous_vs_discrete_optimization | discrete optimization problem]], deciding which expert modules should process each input token <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. Various [[comparison_of_different_routing_strategies | routing strategies]] have been devised, including:

*   **Token's Choice**: Each token selects the top-K experts with the highest routing score <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Expert's Choice**: Experts select the top-C tokens based on routing scores <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

However, sparse MoEs suffer from several issues:

*   **Training Instability**: The discrete nature of routing can lead to large fractions of input tokens simultaneously changing routes, causing training challenges <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.
*   **Token Dropping and Expert Imbalance**: Some tokens might not be assigned to any expert, or some experts might receive a disproportionately large number of tokens, negatively impacting performance <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.
*   **Non-Differentiability**: Most sparse MoE approaches rely on discrete assignments, making them non-[[differentiable_rendering_and_optimization | differentiable]] and requiring heuristic auxiliary losses for training <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   **Scaling Limitations**: Hard routing can be challenging with many experts, with most prior works training with only a few dozen <a class="yt-timestamp" data-t="02:47:00">[02:47:47]</a>.
*   **Batch Effects**: During inference, tokens from different inputs within a batch can compete for limited expert capacity, leading to non-deterministic outputs <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This non-determinism was observed in models like GPT-4 and GPT-3.5, suggesting their use of sparse MoEs <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

## Soft Mixture of Experts

A recent paper from Google DeepMind introduced [[soft_mixture_of_experts_architecture | Soft Mixture of Experts]] (Soft MoE) as an extension to sparse MoEs, aiming to overcome these challenges <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a> <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Soft MoE proposes a fully [[differentiable_rendering_and_optimization | differentiable]] sparse Transformer.

### Mechanism
Unlike sparse MoEs that use discrete routing, Soft MoE performs a "soft assignment" by passing different weighted combinations of *all* input tokens to each expert <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

The process involves:
1.  **Learning Per-Slot Parameters (Phi)**: Each expert slot has a set of learnable parameters (Phi) <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
2.  **Computing Dispatch Weights (D)**: The input tokens (X) are combined with the learned Phi parameters via an Einstein summation and then passed through a softmax function to produce "dispatch weights" (D) <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a> <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. These weights determine the weighted average of input tokens for each slot <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
3.  **Expert Processing**: The resulting weighted average tokens are fed into their respective experts (FFN layers) <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
4.  **Computing Combined Weights (C)**: The outputs from all experts are then combined using "combined weights" (C), calculated similarly to dispatch weights, to produce the final output tokens <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

This design ensures all operations within Soft MoE layers are continuous and fully [[differentiable_rendering_and_optimization | differentiable]] <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. The learned parameters (Phi) are designed to be general and transferable <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

### Advantages over Sparse MoEs
*   **Full Differentiability**: Unlike sparse MoEs, Soft MoEs allow gradients to be pushed through all operations, enabling more stable training and better learning of the routing parameters <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   **Immunity to Token Dropping and Expert Imbalance**: Since every slot receives a weighted average of *all* tokens (with strictly positive weights due to softmax), there is no token dropping or expert imbalance <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.
*   **Scalability**: Soft MoE scales to thousands of experts <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>, with the total number of slots determining the cost, rather than the number of experts <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
*   **No Batch Effects**: Soft MoE's per-example deterministic nature means an input's prediction is not affected by other inputs in the batch, solving a major issue of sparse MoEs <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a> <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

### Similarities to Attention Mechanisms
The process of creating weighted combinations of tokens and distributing them to experts in Soft MoE bears strong resemblance to the attention mechanism in Transformers. Both involve computing weights (or "attention scores") to combine different parts of the input <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>. Just as different attention heads learn to focus on different semantic concepts, different Soft MoE "slots" (and thus experts) learn to specialize in processing specific features, like parts of an image (e.g., a duck's bill or head) <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a> <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. This suggests a convergence towards attention-like mechanisms in efficient model design <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.

## Performance and Ablations

Soft MoE models have been extensively evaluated on image classification and image-language contrastive learning tasks, primarily using Vision Transformer (ViT) models on large internal Google datasets like JFT-4B <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a> <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

*   **Dominating Performance**: Soft MoE "dominates" (outperforms in every metric) <a class="yt-timestamp" data-t="01:38:23">[01:38:23]</a> dense ViT models and other sparse MoE variants (Token's Choice, Expert's Choice) across various metrics, including accuracy, precision, training flops, and wall-clock time <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   **Efficiency**: Soft MoE models are computationally cheaper during both training and inference. For instance, a Soft MoE model can match the quality of a much larger dense ViT while being significantly faster at inference <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a> <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Extended Training**: Soft MoE models benefit from longer training periods (beyond standard scaling laws) without overfitting, steadily improving performance where other models plateau <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>.
*   **Optimal Configuration**: Ablation studies suggest that using "one slot per expert" tends to be optimal for performance <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>. Interestingly, even basic [[dynamic_token_routing_in_transformers | routing strategies]] like identity or uniform mixing in a Soft MoE layer can outperform a dense Transformer, highlighting the inherent benefits of the mixture of experts approach <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

## Technical and Hardware Considerations

MoE layers are typically used to replace the feed-forward layers in Transformer encoder blocks <a class="yt-timestamp" data-t="01:13:07">[01:13:07]</a>. The choice of [[hyperparameters_and_hardware_considerations_in_moes | hyperparameters and hardware considerations]] (number of experts `N` and slots per expert `P`) is crucial and dependent on the available hardware (e.g., GPUs, TPUs) and their interconnects <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. While Soft MoE adds communication overhead due to model parallelism, large dense models also require distribution, lessening the gap <a class="yt-timestamp" data-t="02:20:38">[02:20:38]</a>. The paper highlights the importance of measuring both theoretical FLOPs and practical wall-clock time <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.

## Limitations and Future Work

A key limitation of Soft MoE is its difficulty in integration with auto-regressive decoders, common in language models <a class="yt-timestamp" data-t="02:27:53">[02:27:53]</a>. The soft assignment, which combines all tokens, conflicts with the causal masking required in decoders to prevent future tokens from influencing current predictions <a class="yt-timestamp" data-t="02:29:01">[02:29:01]</a>. This remains an exciting research avenue <a class="yt-timestamp" data-t="02:29:58">[02:29:58]</a>.

Integrating [[lora_finetuning_techniques | LoRA finetuning techniques]] with MoEs would likely require applying LoRA to each expert, adding complexity <a class="yt-timestamp" data-t="01:48:46">[01:48:46]</a>. Furthermore, finding optimal [[layerwise_scaling_and_architecture_tricks | architecture tricks]] and learning rate schedules for Soft MoE is another area for exploration <a class="yt-timestamp" data-t="01:51:11">[01:51:11]</a>.