---
title: Role of GPUs and TPUs in deep learning
videoId: r5NQecwZs1A
---

From: [[fireship]] <br/> 

Graphics Processing Units (GPUs) and Tensor Processing Units (TPUs) play crucial roles in modern computing, especially in the field of deep learning. While CPUs are optimized for sequential computations, GPUs and TPUs are designed to handle massive parallel workloads, making them indispensable for tasks like rendering graphics and [[training_and_finetuning_AI_models | training AI models]] <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

## Graphics Processing Units (GPUs)

A Graphics Processing Unit, or graphics card, is highly optimized for [[gpu_vs_cpu_in_parallel_computing | parallel computing]] <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. Unlike a Central Processing Unit (CPU) that might have around 24 cores in high-end chips like Apple's M2 Ultra or Intel's I9, an Nvidia RTX 4080 GPU possesses nearly 10,000 cores <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. Each of these cores can handle a floating-point or integer computation per cycle <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

Initially designed for rendering graphics in games, allowing for the instant calculation of lights and shadows, GPUs perform tons of linear algebra in parallel <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a><a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>. This capability makes them essential for [[training_and_finetuning_AI_models | training deep learning models]], as these models rely on performing numerous matrix multiplications on large datasets <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. The massive demand for GPUs in this area has significantly impacted the market <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

While a single CPU core is significantly faster and more capable of handling complex logic and branching than a single GPU core, GPUs excel at simple, repetitive computations that can be parallelized <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. Most code, however, cannot take advantage of parallel computing and needs to run sequentially with a single thread <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

> A CPU is described as being like a Toyota Camry: "extremely versatile but can't take you to the Moon" <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>.
> A GPU is "more like a rocket ship: it's really fast when you want to go in a straight line but not really ideal if we're going to pick up your groceries" <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

## Tensor Processing Units (TPUs)

For specific deep learning use cases, specialized hardware called Tensor Processing Units (TPUs) exists <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. These chips are similar to GPUs but are specifically designed for tensor operations, which include the matrix multiplication central to deep learning <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.

Google developed TPUs in 2016 to integrate directly with its [[training_and_finetuning_AI_models | TensorFlow]] software framework <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. A TPU contains thousands of "multiply accumulators" <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>. This architecture allows the hardware to perform matrix multiplication without needing to access registers or shared memory, a process a GPU would typically require <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>. For neural networks that might take weeks or months to train, using a TPU could result in savings of millions of dollars <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>.