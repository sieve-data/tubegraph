---
title: Understanding Hessian matrices and incoherence in neural networks
videoId: 6wEVz0wkhCM
---

From: [[hu-po]] <br/> 

This article explores the concepts of Hessian matrices and incoherence, particularly their application in the context of neural network [[memory_optimization_in_neural_networks | quantization]]. These ideas are central to the Quip paper, which proposes a 2-bit [[memory_optimization_in_neural_networks | quantization]] method for large language models with theoretical guarantees <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

## Quantization Basics
[[memory_optimization_in_neural_networks | Quantization]] is the process of reducing the amount of information used to represent data, similar to how an image can be progressively compressed from 24 bits per pixel down to 1 bit per pixel <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>, <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

The main reasons to quantize machine learning models include:
*   **Memory Usage:** Lower data type precision reduces memory requirements, making it possible to load large models like Code Llama 34B onto consumer GPUs <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Power Consumption:** Smaller neural networks use less power for inference, which could be significant when AI companions are in widespread use <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Latency:** Smaller models lead to faster computation and inference times <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

Current research has made significant strides, with 4-bit [[memory_optimization_in_neural_networks | quantization]] being a frontier before the Quip paper, which achieves effective 2-bit [[memory_optimization_in_neural_networks | quantization]] <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

## Hessian Matrices

In the context of neural networks, the Hessian matrix refers to the second-order derivative of the loss function with respect to the model's weights <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>, <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

*   **Curvature of the Loss Landscape:** The Hessian provides information about the curvature of the loss landscape <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. This can be understood through an analogy: if the first derivative (gradient) indicates velocity or slope, the second derivative (Hessian) indicates acceleration or curvature <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>, <a class="yt-timestamp" data-t="03:11:13">[03:11:13]</a>.
*   **Local Convexity:** If the Hessian is symmetric positive definite (SPD), it implies that the function is locally convex, meaning the graph is bowl-shaped at least locally <a class="yt-timestamp" data-t="01:32:38">[01:32:38]</a>, <a class="yt-timestamp" data-t="01:33:31">[01:33:31]</a>. This property tells you about the nature of critical points where the gradient is zero (local minima or maxima) <a class="yt-timestamp" data-t="01:34:56">[01:34:56]</a>.
*   **Role in Quantization:** In [[memory_optimization_in_neural_networks | quantization]] methods like Adaptive Rounding, the Hessian is used as a "proxy Hessian" to approximate the task loss using a Taylor series expansion <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>, <a class="yt-timestamp" data-t="01:29:22">[01:29:22]</a>. This approximation helps decide how to round weights to maintain accuracy <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

## Incoherence in Neural Networks

In the context of matrices, incoherence implies that two matrices are not correlated, meaning they are independent of each other <a class="yt-timestamp" data-t="01:19:20">[01:19:20]</a>. Specifically, it suggests that patterns in one matrix (e.g., weights) do not mimic or align with patterns in another (e.g., the Hessian matrix) <a class="yt-timestamp" data-t="01:21:24">[01:21:24]</a>.

### Incoherence Processing in Quip

The Quip paper introduces "incoherence processing" (IP) as a crucial second step in its [[memory_optimization_in_neural_networks | quantization]] algorithm <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

*   **Goal:** The primary goal of incoherence processing is to ensure that the weight matrices and the Hessian matrices are incoherent <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>, <a class="yt-timestamp" data-t="01:20:43">[01:20:43]</a>.
*   **Method:** This is achieved by multiplying the weight and Hessian matrices by random orthogonal matrices <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
    *   **Orthogonal Matrices:** An orthogonal matrix is a square matrix whose inverse is equal to its transpose <a class="yt-timestamp" data-t="00:37:29">[00:37:29]</a>. Multiplying by an orthogonal matrix effectively rotates and possibly reflects the data in space, preserving distances and angles <a class="yt-timestamp" data-t="01:47:06">[01:47:06]</a>.
    *   **Kronecker Product:** Since finding large random orthogonal matrices can be challenging, the Kronecker product is used as a trick to create large orthogonal matrices from smaller ones <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>, <a class="yt-timestamp" data-t="00:40:44">[00:40:44]</a>.
*   **Intuition:** The process "scrambles" the weight and Hessian matrices. By applying random orthogonal transformations to both, the structure or patterns that might otherwise be coherent get disrupted <a class="yt-timestamp" data-t="01:49:55">[01:49:55]</a>, <a class="yt-timestamp" data-t="01:50:52">[01:50:52]</a>. This makes it harder for algorithms to exploit any specific structure in the original matrices, ensuring results are not tied to specific structures and are more generalizable <a class="yt-timestamp" data-t="01:51:02">[01:51:02]</a>.

The Quip paper empirically found that incoherence processing significantly improves [[memory_optimization_in_neural_networks | quantization]] performance for large models, especially at higher compression rates <a class="yt-timestamp" data-t="00:44:01">[00:44:01]</a>. In fact, it's identified as the most important part of the entire [[memory_optimization_in_neural_networks | quantization]] algorithm <a class="yt-timestamp" data-t="01:45:45">[01:45:45]</a>.

## Relationship between Model Size and Quantization

The Quip paper observed a fascinating relationship: as the model size increases, the difference in performance between 2-bit and 16-bit [[memory_optimization_in_neural_networks | quantization]] becomes smaller <a class="yt-timestamp" data-t="00:51:38">[00:51:38]</a>. This hints at the feasibility of accurate 2-bit inference in larger language models <a class="yt-timestamp" data-t="00:51:56">[00:51:56]</a>.

[!NOTE] This observation contrasts with previous findings, such as those from the [[memory_optimization_in_neural_networks | QLoRA]] paper by Tim Detmers, which noted more outliers in larger models, potentially making [[memory_optimization_in_neural_networks | quantization]] more challenging <a class="yt-timestamp" data-t="00:52:44">[00:52:44]</a>, <a class="yt-timestamp" data-t="00:53:06">[00:53:06]</a>. This discrepancy suggests a deeper, not fully understood underlying truth about how models store and process information <a class="yt-timestamp" data-t="00:59:57">[00:59:57]</a>.

This phenomenon leads to speculation that in very large models, the "intelligence" might reside more in the *connectivity* patterns of the neural network rather than the precise numerical values of individual weights <a class="yt-timestamp" data-t="01:09:41">[01:09:41]</a>, <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>. If true, this could imply that larger models are inherently more robust to aggressive [[memory_optimization_in_neural_networks | quantization]], potentially opening the door for 1-bit [[memory_optimization_in_neural_networks | quantization]] of future trillion-parameter models to fit on consumer hardware <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.