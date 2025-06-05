---
title: Introduction to CUDA
videoId: pPStdjuYzSI
---

From: [[fireship]] <br/> 

[[CUDA]] is a parallel computing platform developed by Nvidia, first released in 2007, based on the earlier work of Ian Buck and John Nichols <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It stands for Compute Unified Device Architecture <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. CUDA allows users to leverage their Graphics Processing Units (GPUs) for general-purpose computing beyond just displaying video games <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

Since its inception, CUDA has significantly advanced the field of computing by enabling the parallel processing of large datasets <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This capability has been instrumental in unlocking the full potential of [[role_of_gpus_and_tpus_in_deep_learning | deep neural networks]] within artificial intelligence <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## GPU vs. CPU in Parallel Computing

Historically, GPUs were designed specifically for rendering graphics <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. When playing a game in 1080p at 60 frames per second, over two million pixels may need recalculation for each frame, demanding hardware capable of extensive parallel matrix multiplication and vector transformations <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. Modern GPUs are measured in teraflops, indicating how many trillions of floating-point operations they can handle per second <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

A key distinction between GPUs and CPUs lies in their core count and design philosophy <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>:
*   A modern CPU, like the Intel I9, typically has around 24 cores <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. CPUs are designed for versatility <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   A modern GPU, such as the RTX 4090, can have over 16,000 cores <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. GPUs are engineered for extremely fast parallel processing <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

[[gpu_vs_cpu_in_parallel_computing | CUDA]] enables developers and data scientists to tap into this immense parallel processing power of GPUs, which is actively used for training powerful machine learning models <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## How CUDA Works

The general workflow for a CUDA application involves several steps <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>:
1.  **Kernel Definition**: A function, known as a [[cuda_kernels_and_functions | CUDA kernel]], is written to execute on the GPU <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
2.  **Data Transfer**: Data is copied from the main system RAM to the GPU's dedicated memory <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
3.  **Execution Launch**: The CPU instructs the GPU to execute the kernel in parallel <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The code is organized into blocks, which in turn arrange threads into a multi-dimensional grid <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
4.  **Result Transfer**: Once the GPU completes the computation, the final result is copied back to the main system memory <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Building a CUDA Application

To [[building_a_cuda_application | build a CUDA application]], an Nvidia GPU and the CUDA Toolkit are required <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The toolkit includes device drivers, a runtime environment, compilers, and development tools <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. CUDA code is most commonly written in C++ <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Example: Vector Addition

Consider a simple example of adding two vectors (arrays) in parallel:

1.  **Define the CUDA Kernel**: The `__global__` specifier is used to define a function, or CUDA kernel, that will run on the GPU <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This function takes pointer arguments for the two input vectors (A and B) and a pointer for the result vector (C) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    ```cpp
    // Example Kernel structure
    __global__ void addVectors(int* A, int* B, int* C, int size) {
        // Calculate the global index of the current thread
        int idx = blockIdx.x * blockDim.x + threadIdx.x;
        if (idx < size) {
            C[idx] = A[idx] + B[idx];
        }
    }
    ```
    For parallel operations, the global index of the thread within its block must be calculated <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

2.  **Memory Management**: The `__managed__` keyword can be used to tell CUDA that data can be accessed from both the host CPU and the device GPU without needing manual data copying between them <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

3.  **Main Function (CPU)**: A `main` function for the CPU is written to orchestrate the CUDA kernel execution <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This includes initializing arrays with data <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a> and then calling the kernel <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

4.  **Kernel Launch Configuration**: The `<<<...>>>` (triple brackets) syntax is used to configure the CUDA kernel launch, specifying the number of blocks and threads per block to be used for parallel execution <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This configuration is critical for [[optimizing_with_cuda_for_deep_learning | optimizing]] computations involving multi-dimensional data structures like tensors used in deep learning <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

5.  **Synchronization**: `cudaDeviceSynchronize()` pauses the CPU's execution, waiting for the GPU to complete its computations and copy the results back to the host machine <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

6.  **Result Handling**: After synchronization, the results can be utilized, for example, by printing them to the standard output <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Executing this code with a CUDA compiler allows for parallel thread execution on the GPU, such as 256 threads running simultaneously <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

Nvidia's GTC conference offers further insights into building large-scale parallel systems with CUDA <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.