---
title: Combining multiple vision encoders for improved performance
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

Vision Language Models (VLMs), also known as multimodal large language models (MLMs), large multimodal models (LMMs), or large-scale Vision Language Models (LVLMs), integrate a visual model with a large language model to process and understand both image and text inputs <a class="yt-timestamp" data-t="00:04:22">00:04:22</a>, <a class="yt-timestamp" data-t="01:55:07">01:55:07</a>. Recent research explores various strategies to optimize these models, including the strategic [[Use of multiple visual encoders | use of multiple visual encoders]] to enhance performance.

## Why Combine Vision Encoders?

The core idea behind combining multiple vision encoders is to leverage their complementary strengths <a class="yt-timestamp" data-t="00:31:08">00:31:08</a>. Different vision encoders are pre-trained on varying datasets with different objectives and losses, leading them to develop distinct biases and excel at different types of visual information <a class="yt-timestamp" data-t="00:30:47">00:30:47</a>, <a class="yt-timestamp" data-t="00:39:46">00:39:46">00:39:51</a>. By combining them, the VLM can benefit from a richer, more comprehensive understanding of the visual input.

This approach is analogous to an ensemble of models, where aggregating outputs from multiple models often yields better results than any single model alone <a class="yt-timestamp" data-t="00:31:08">00:31:08</a>.

## Key Examples and Findings

### Comm Paper (Huawei)

The "From Clip to Dino Visual Encoders Shout in Multimodal Large Language Models" (Comm) paper, though later retracted, extensively investigated the effectiveness of different visual encoders in MLMs <a class="yt-timestamp" data-t="00:05:01">00:05:01</a>, <a class="yt-timestamp" data-t="01:42:51">01:42:51</a>.

Key findings and approaches in the Comm paper included:
*   **Dual Vision Encoders** The paper explicitly explored combining two different types of [[role_of_vision_transformers_in_dinov2 | Vision Transformers]]:
    *   **CLIP (Contrastive Language-Image Pre-training):** Developed by OpenAI, it is known for its ability to capture global semantic information <a class="yt-timestamp" data-t="00:30:28">00:30:28</a>, <a class="yt-timestamp" data-t="00:39:46">00:39:46">00:39:49</a>.
    *   **DINOv2:** Developed by Meta, it excels at learning fine-grained pixel-level information through a self-supervised objective <a class="yt-timestamp" data-t="00:30:34">00:30:34</a>, <a class="yt-timestamp" data-t="00:39:51">00:39:51">00:39:54</a>, <a class="yt-timestamp" data-t="01:43:17">01:43:17">01:43:22</a>.
*   **Multi-Level Feature Fusion:** Instead of just using the final representations from each vision encoder, the Comm paper proposed extracting and concatenating intermediate features from various layers of both Clip and DINOv2 <a class="yt-timestamp" data-t="00:32:01">00:32:01</a>, <a class="yt-timestamp" data-t="00:38:41">00:38:41">00:38:51</a>. This allows the VLM to access both low-level detailed information (from shallower layers) and high-level semantic information (from deeper layers) <a class="yt-timestamp" data-t="00:38:30">00:38:30</a>, <a class="yt-timestamp" data-t="01:12:52">01:12:52">01:13:01</a>.
*   **Connection Mechanism:** The outputs from these combined, multi-level features are typically fed into a small Multi-Layer Perceptron (MLP) that acts as a "glue" or "connector" to integrate them before feeding into the language model <a class="yt-timestamp" data-t="00:32:31">00:32:31</a>, <a class="yt-timestamp" data-t="00:33:12">00:33:12">00:33:16</a>.
*   **Performance:** While combining Clip and DINOv2 with multi-level features showed an improvement in Visual Question Answering (VQA) accuracy (e.g., from 68.8 with Clip alone to 70.0 with the combination), the increase was considered "underwhelming" given the added complexity and computational cost <a class="yt-timestamp" data-t="01:25:50">01:25:50</a>, <a class="yt-timestamp" data-t="01:51:37">01:51:37">01:52:11</a>. This suggests that the cost-benefit ratio for such complex fusion might not always justify the marginal gains.

### DeepSpeed Visual Chat (Microsoft)

This paper focused on the overall framework for multi-round, multi-image dialogues <a class="yt-timestamp" data-t="00:35:04">00:35:04</a>, <a class="yt-timestamp" data-t="01:45:21">01:45:21</a>. Although not primarily about combining vision encoders directly in its core contribution, it revealed practical observations about using pre-trained vision encoders. The authors noted that a "better visual encoder commonly the clip visual encoder is used in large Vision language models" <a class="yt-timestamp" data-t="01:00:10">01:00:10</a>. They also observed that using the [[pretrained_vision_transformers_and_koco | QuenVL]] visual encoder (which is based on OpenCLIP, a fine-tuned version of Clip) significantly improved the model quality due to its higher output resolution compared to the standard 224x224 resolution of Clip <a class="yt-timestamp" data-t="00:59:04">00:59:04</a>, <a class="yt-timestamp" data-t="00:59:55">00:59:55">01:00:01</a>.

## Architectural Implications

When designing VLMs, researchers often freeze the weights of the pre-trained vision encoders, meaning no gradients are pushed into them during VLM training <a class="yt-timestamp" data-t="00:28:07">00:28:07</a>, <a class="yt-timestamp" data-t="00:32:41">00:32:41">00:32:47</a>, <a class="yt-timestamp" data-t="01:53:16">01:53:16">01:53:20</a>. This significantly reduces computational costs and accelerates training <a class="yt-timestamp" data-t="00:28:16">00:28:16">00:28:20</a>. The focus then shifts to how to best connect the frozen vision encoder outputs to the large language model. While simple MLPs are commonly used as connectors <a class="yt-timestamp" data-t="01:54:01">01:54:01">01:54:05</a>, some approaches like QuenVL use a cross-attention module, a mini-[[comparison_of_vision_architectures | Vision Transformer]], as the adapter <a class="yt-timestamp" data-t="00:50:06">00:50:06</a>, <a class="yt-timestamp" data-t="01:53:59">01:53:59">01:54:14</a>. However, experiments have shown that using a more complex Transformer approach for this connection might not yield significant benefits over simpler linear layers or MLPs <a class="yt-timestamp" data-t="01:31:54">01:31:54">01:32:03</a>.

Another consideration is the relative size of the vision encoder and the language model. A large language model (e.g., 70 billion parameters) paired with a comparatively small vision encoder (e.g., 2 billion parameters) might lead to suboptimal results, suggesting that a balanced scaling of both components could be beneficial <a class="yt-timestamp" data-t="00:46:42">00:46:42">00:46:52</a>, <a class="yt-timestamp" data-t="01:18:14">01:18:14">01:18:15</a>. This aligns with findings in image generation models where larger text encoders significantly improve image quality <a class="yt-timestamp" data-t="00:45:47">00:45:47">00:45:50</a>.

## Future Directions

The field of VLMs is rapidly evolving, with ongoing research into optimizing training recipes, exploring various connector architectures, and developing new data augmentation strategies for multimodal datasets <a class="yt-timestamp" data-t="01:32:52">01:32:52</a>. The consensus points towards using contrastively pre-trained vision encoders (like Clip or SigLIP) over classification-based ones for VQA tasks, even if they underperform on standard image classification benchmarks <a class="yt-timestamp" data-t="01:39:00">01:39:00">01:39:06</a>, <a class="yt-timestamp" data-t="01:42:33">01:42:33">01:42:40</a>. The increasing scale of models and data continues to be a driving force behind improved performance, with the potential for emergent behaviors as models grow larger <a class="yt-timestamp" data-t="01:30:50">01:30:50">01:31:05</a>.