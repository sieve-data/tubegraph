---
title: Neural Information Processing Systems Conference
videoId: -jG7S5g071Q
---

From: [[hu-po]] <br/> 

The Neural Information Processing Systems Conference (NeurIPS) is considered one of the more prestigious [[Deep Learning and Neural Networks | machine learning]] conferences <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. It offers various accolades, including a [[Machine Learning Conference Awards | best paper award]] <a class="yt-timestamp" data-t="04:02:04">[04:02:04]</a>.

## History and Naming

The conference was previously known as NIPS <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. The name was changed to NeurIPS because "NIPS" is slang for nipples, which was deemed "too cringe" <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## Awards and Recognition

NeurIPS presents a [[Machine Learning Conference Awards | best paper award]] among other recognitions <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>. The paper "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction" won this award, indicating its supposed quality <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>.

### Visual Autoregressive Modeling (VARM) Paper Controversy

The first author of the award-winning paper, K. Tion, was a student from Peking University and had interned at ByteDance <a class="yt-timestamp" data-t="04:24:00">[04:24:00]</a>. Other co-authors on the paper had ByteDance emails <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

A controversy arose surrounding the paper, leading to a legal battle between ByteDance and Tion <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>. Allegations claimed Tion "maliciously disrupted or was poisoning internal model training" by altering code, resulting in significant resource wastage <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. This disruption might have been an accident, as interns often have SSH access to training machines to monitor and adjust processes <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. While such disruptions can waste time from the last checkpoint and engineering effort, the claim of "tens of millions of dollars" in damages remains a legal dispute <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.

Despite the controversy, the paper's idea and results are considered "very pleasing" <a class="yt-timestamp" data-t="23:59:00">[23:59:00]</a>. Key aspects contributing to its award include:
*   **Strong Results:** The paper achieved impressive FID (Fréchet Inception Distance) scores, improving from 18 to 1 on ImageNet 256x256, and Inception Score from 80 to 350 <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>. An FID score of 1.78 is considered a lower bound, making a score of 1 "insane" and "pretty impressive" <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.
*   **Clarity and Writing Quality:** The paper is well-written and explains concepts clearly, making it an effective educational piece <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.
*   **Simple yet Profound Idea:** The core idea of next-scale prediction is considered very simple but highly effective <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>. This simplicity, combined with strong performance, often leads to [[Machine Learning Conference Awards | best paper awards]] <a class="yt-timestamp" data-t="24:29:00">[24:29:00]</a>.
*   **Computational Efficiency:** VARM achieves a 20x faster inference speed compared to previous methods <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. This is due to its ability to generate all tokens within a given resolution map in parallel, reducing the time complexity to O(N^4) from O(N^6) in standard autoregressive models <a class="yt-timestamp" data-t="01:01:54">[01:01:54]</a>.
*   **Zero-Shot Generalization:** The model demonstrates zero-shot generalization abilities in downstream tasks like image inpainting, outpainting, and editing, without requiring fine-tuning <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.
*   **Foundation on Human Perception:** The paper's approach of hierarchical, multi-scale, course-to-fine prediction is inspired by how humans perceive and create images <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>, mirroring the structure of the human visual system that led to [[Convolutional Neural Networks and Visual Systems | convolutional neural networks]] <a class="yt-timestamp" data-t="20:54:00">[20:54:00]</a>.
*   **Use of Established Architectures:** The paper leverages the gpt2 Transformer architecture and a vanilla VQVAE tokenizer, indicating that its improvements stem from the fundamental inductive prior rather than complex new tricks <a class="yt-timestamp" data-t="26:18:00">[26:18:00]</a>. This makes the findings more robust <a class="yt-timestamp" data-t="55:50:00">[55:50:00]</a>.

The win was attributed to a combination of "luck" (picking the right idea that works well) and "skill" (well-written paper, good figures) <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.