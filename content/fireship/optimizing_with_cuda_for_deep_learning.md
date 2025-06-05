---
title: Optimizing with CUDA for Deep Learning
videoId: pPStdjuYzSI
---

From: [[fireship]] <br/> 

CUDA (Compute Unified Device Architecture) is a parallel computing platform developed by Nvidia in 2007, based on the prior work of Ian Buck and John Nichols <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It allows users to leverage the power of their Graphics Processing Unit (GPU) for tasks beyond just gaming <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Since its inception, [[Introduction to CUDA|CUDA]] has enabled the parallel computation of large data blocks, which has been crucial in unlocking the full potential of [[role_of_gpus_and_tpus_in_deep_learning|deep neural networks]] behind [[training and finetuning AI models|artificial intelligence]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## GPU vs. CPU in Parallel Computing

Historically, the GPU was used for computing graphics <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. When playing a game at 1080p and 60 FPS, over two million pixels on the screen may need recalculation after every frame, requiring hardware capable of extensive matrix multiplication and vector transformations in parallel <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Modern GPUs are measured in teraflops, indicating how many trillions of floating-point operations they can handle per second <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

In contrast to a modern CPU like the Intel i9, which has 24 cores, a modern GPU such as the RTX 4090 boasts over 16,000 cores <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   **CPU:** Designed for versatility <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **GPU:** Designed for extremely fast parallel processing <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

[[Introduction to CUDA|CUDA]] allows developers to tap into this parallel processing power of the GPU, which data scientists worldwide are currently using to [[training and finetuning AI models|train powerful machine learning models]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How CUDA Works

The process of using [[Introduction to CUDA|CUDA]] involves several steps:
1.  **Kernel Definition:** A function, known as a [[cuda_kernels_and_functions|CUDA kernel]], is written to run on the GPU <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
2.  **Data Transfer:** Data is copied from the main RAM of the host CPU to the GPU's memory <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
3.  **Execution Command:** The CPU instructs the GPU to execute the [[cuda_kernels_and_functions|kernel]] in parallel <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
4.  **Parallel Execution:** The code executes in a block, which organizes threads into a multi-dimensional grid <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
5.  **Result Transfer:** The final result from the GPU is copied back to the main memory <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Building a CUDA Application

To [[Building a CUDA Application|build a CUDA application]], you need an Nvidia GPU and the [[Building a CUDA Application|CUDA toolkit]], which includes device drivers, a runtime, compilers, and development tools <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The actual code is typically written in C++ <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Defining a CUDA Kernel
A [[cuda_kernels_and_functions|CUDA kernel]] is defined using the `__global__` specifier, indicating it runs on the GPU <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. For operations like vector addition, which can involve billions of parallel operations, it's necessary to calculate the global index of the thread within its block <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Managed Memory
The `managed` keyword in [[Introduction to CUDA|CUDA]] allows data to be accessed from both the host CPU and the device GPU without requiring manual data copying between them <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Launching the Kernel
The main function, running on the CPU, launches the [[cuda_kernels_and_functions|CUDA kernel]] <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. Arrays are initialized with data using a for loop <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The `<<<...>>>` triple brackets are used to configure the [[cuda_kernels_and_functions|CUDA kernel]] launch, controlling the number of blocks and threads per block <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This configuration is vital for optimizing multi-dimensional data structures like tensors used in [[role_of_gpus_and_tpus_in_deep_learning|deep learning]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Synchronization and Results
`cudaDeviceSynchronize` will pause the execution of the CPU code and wait for the GPU to complete its operations <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Once the GPU finishes and copies the data back to the host machine, the result can be used and printed <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Compiling and running this code allows for parallel execution of threads on the GPU <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.