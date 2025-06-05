---
title: CUDA Kernels and Functions
videoId: pPStdjuYzSI
---

From: [[fireship]] <br/> 

[[Introduction to CUDA | CUDA]], or Compute Unified Device Architecture, is a [[introduction_to_cuda | parallel computing platform]] developed by Nvidia in 2007, building upon the work of Ian Buck and John Nichols <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It enables users to leverage their [[GPU vs CPU in Parallel Computing | GPU]] for tasks beyond just gaming <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This technology has transformed the field of computing by facilitating the parallel processing of large data blocks <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, which has been crucial in unleashing the potential of [[role_of_gpus_and_tpus_in_deep_learning | deep neural networks]] used in artificial intelligence <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## GPU vs. CPU in Parallel Computing
Historically, the [[GPU vs CPU in Parallel Computing | Graphics Processing Unit (GPU)]] was designed for graphics computation, such as recalculating millions of pixels on a screen at high frame rates <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This requires hardware capable of extensive parallel matrix multiplication and vector transformations <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Modern [[GPU vs CPU in Parallel Computing | GPUs]] are measured in teraflops, indicating how many trillions of floating-point operations they can handle per second <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. For instance, an RTX 4090 [[GPU vs CPU in Parallel Computing | GPU]] boasts over 16,000 cores, in contrast to a modern [[GPU vs CPU in Parallel Computing | CPU]] like the Intel i9, which has 24 cores <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While [[GPU vs CPU in Parallel Computing | CPUs]] are designed for versatility, [[GPU vs CPU in Parallel Computing | GPUs]] are built for rapid parallel processing <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

[[Optimizing with CUDA for Deep Learning | CUDA]] enables developers to harness this [[GPU vs CPU in Parallel Computing | GPU]] power, with data scientists worldwide utilizing it to train powerful machine learning models <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## How CUDA Kernels Work
The process of executing a [[optimizing_with_cuda_for_deep_learning | CUDA kernel]] involves several steps:
1.  **Kernel Definition**: A function, known as a [[optimizing_with_cuda_for_deep_learning | CUDA kernel]], is written to run specifically on the [[GPU vs CPU in Parallel Computing | GPU]] <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
2.  **Data Transfer**: Data is copied from the main system RAM to the [[GPU vs CPU in Parallel Computing | GPU]]'s memory <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
3.  **Execution Launch**: The [[GPU vs CPU in Parallel Computing | CPU]] instructs the [[GPU vs CPU in Parallel Computing | GPU]] to execute the [[optimizing_with_cuda_for_deep_learning | kernel]] in parallel <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
4.  **Parallel Execution**: The code executes within a block, which organizes threads into a multi-dimensional grid <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
5.  **Result Transfer**: The final result from the [[GPU vs CPU in Parallel Computing | GPU]] is copied back to the main system memory <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

## Building a CUDA Application
To create a [[building_a_cuda_application | CUDA application]], you need an Nvidia [[GPU vs CPU in Parallel Computing | GPU]] and the [[building_a_cuda_application | CUDA Toolkit]] installed <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. The toolkit includes device drivers, a runtime, compilers, and development tools <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. [[applications_and_usage_of_c | CUDA code]] is typically written in [[applications_and_usage_of_c | C++]] <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Defining a CUDA Kernel
A [[optimizing_with_cuda_for_deep_learning | CUDA kernel]] is defined using the `__global__` specifier, indicating it runs on the [[GPU vs CPU in Parallel Computing | GPU]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. For example, a kernel might add two vectors together:

```cpp
__global__ void addVectors(int* A, int* B, int* C) {
    int index = blockIdx.x * blockDim.x + threadIdx.x; // Calculate global index
    C[index] = A[index] + B[index];
}
```
This function takes pointer arguments for input vectors `A` and `B`, and `C` for the result <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. To perform billions of operations in parallel, it's necessary to calculate the global index of each thread within its block <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Memory Management
[[optimizing_with_cuda_for_deep_learning | CUDA]] offers "managed" memory, which allows data to be accessed by both the host [[GPU vs CPU in Parallel Computing | CPU]] and the device [[GPU vs CPU in Parallel Computing | GPU]] without manual copying <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### Launching the Kernel
The main function, running on the [[GPU vs CPU in Parallel Computing | CPU]], initializes arrays with data and then passes this data to the [[optimizing_with_cuda_for_deep_learning | kernel]] for [[building_a_cuda_application | GPU]] execution <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The `<<<gridDim, blockDim>>>` triple brackets are used to configure the [[optimizing_with_cuda_for_deep_learning | CUDA kernel]] launch, controlling the number of blocks and threads per block <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This configuration is vital for [[optimizing_with_cuda_for_deep_learning | optimizing]] computations on multi-dimensional data structures like tensors, common in [[role_of_gpus_and_tpus_in_deep_learning | deep learning]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

```cpp
// Example of launching the kernel
int main() {
    // ... data initialization ...
    addVectors<<<numBlocks, threadsPerBlock>>>(d_A, d_B, d_C);
    // ...
}
```

### Synchronization and Result Retrieval
After launching the [[optimizing_with_cuda_for_deep_learning | kernel]], `cudaDeviceSynchronize()` is used to pause the [[GPU vs CPU in Parallel Computing | CPU]]'s execution until the [[GPU vs CPU in Parallel Computing | GPU]] has completed its tasks and copied the results back to the host machine <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. The results can then be used and printed <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Compiling and executing this code, for example, running 256 threads in parallel on a [[GPU vs CPU in Parallel Computing | GPU]], demonstrates the power of [[optimizing_with_cuda_for_deep_learning | CUDA]] for parallel computation <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.