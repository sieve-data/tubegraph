---
title: GPU vs CPU in Parallel Computing
videoId: pPStdjuYzSI
---

From: [[fireship]] <br/> 

[[Introduction to CUDA | CUDA]], or Compute Unified Device Architecture, is a parallel computing platform developed by [[Nvidia]] in 2007, based on the prior work of Ian Buck and John Nichols <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It allows users to leverage their Graphics Processing Unit (GPU) for tasks beyond just playing video games <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Since its inception, [[Introduction to CUDA | CUDA]] has revolutionized the world by enabling the parallel computation of large blocks of data, which has unlocked the true potential of deep neural networks behind artificial intelligence <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## GPU vs. CPU: Design and Function

Historically, the Graphics Processing Unit (GPU) was designed specifically for rendering graphics <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. When playing a game in 1080p at 60 frames per second, over two million pixels on the screen may need to be recalculated after every frame <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This intensive task requires hardware capable of performing extensive matrix multiplication and vector transformations in parallel <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Modern GPUs are measured in teraflops, indicating how many trillions of floating-point operations they can handle per second <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

In contrast, a Central Processing Unit (CPU) is designed to be versatile <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. While a modern CPU like the Intel i9 might have 24 cores, a modern GPU like the RTX 4090 boasts over 16,000 cores <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This fundamental difference in architecture means that while a CPU is built for general-purpose versatility, a GPU is optimized to perform tasks exceptionally fast in parallel <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This distinction is crucial for understanding the [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | function and optimization of different processing units]].

## Parallel Computing with CUDA

[[Introduction to CUDA | CUDA]] allows developers and data scientists to tap into the immense parallel processing power of the GPU <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Data scientists worldwide are currently using [[Introduction to CUDA | CUDA]] to train the most powerful machine learning models <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

The process of using [[Introduction to CUDA | CUDA]] involves:
1.  **Writing a [[CUDA Kernels and Functions | CUDA kernel]]**: A function designed to run on the GPU <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
2.  **Data Transfer**: Copying data from the main RAM (host memory) to the GPU's memory <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
3.  **Execution Command**: The CPU instructs the GPU to execute the [[CUDA Kernels and Functions | kernel function]] in parallel <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
4.  **Parallel Execution**: The code is executed in a block, which organizes threads into a multi-dimensional grid <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
5.  **Result Transfer**: The final result from the GPU is copied back to the main memory <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

[[Optimizing with CUDA for Deep Learning | CUDA]] applications are most often written in C++ <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. A `__global__` specifier defines a [[CUDA Kernels and Functions | CUDA kernel]] that runs on the GPU <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. For operations involving billions of parallel computations, it's necessary to calculate the global index of the thread within its block <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Using `managed` memory tells [[Introduction to CUDA | CUDA]] that data can be accessed by both the host CPU and the device GPU without manual copying <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

The triple brackets `<<<...>>>` are used to configure the [[CUDA Kernels and Functions | CUDA kernel]] launch, controlling the number of blocks and threads per block used for parallel execution <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This configuration is critical for [[Optimizing with CUDA for Deep Learning | optimizing]] multi-dimensional data structures like tensors, which are commonly used in [[role_of_gpus_and_tpus_in_deep_learning | deep learning]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. `cudaDeviceSynchronize` pauses the CPU's execution until the GPU has completed its task and copied data back to the host machine <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.