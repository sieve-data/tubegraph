---
title: Function and optimization of different processing units
videoId: r5NQecwZs1A
---

From: [[fireship]] <br/> 

Modern computers utilize various processing units (PUs) at the hardware level to perform computations. These include the Central Processing Unit (CPU), Graphics Processing Unit (GPU), Tensor Processing Unit (TPU), and Data Processing Unit (DPU) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## A Brief [[history_and_evolution_of_computer_processing_units | History of Computing]]

The first truly programmable computer was the Z1, created by Konrad Zuse in 1936 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This highly mechanical machine, with over 20,000 parts, represented binary data using sliding metal sheets <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It could perform Boolean algebra and floating-point numbers and operated at a clock rate of 1 Hertz, executing one instruction per second <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. The Z1 was destroyed in 1943 during the bombardment of Berlin <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

In 1945, the Von Neumann architecture was introduced, a foundational design that describes how data and instructions are stored in the same memory space and handled by a processing unit; this architecture is still used in modern chips today <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. A significant breakthrough occurred a few years later with the invention of the transistor, a semiconductor capable of amplifying or switching electrical signals, representing binary ones or zeros based on current flow <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. By 1958, the integrated circuit was developed, allowing multiple transistors to be placed on a single silicon chip <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Finally, in 1971, Intel released the first commercially available microprocessor, a 4-bit processor with approximately 2300 transistors and a clock speed of 740 kilohertz <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Central Processing Unit (CPU)

The CPU, or [[how_a_cpu_works | central processing unit]], functions as the "brain" of a computer <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Its primary roles include running the operating system, executing programs, and managing hardware <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. CPUs access the system's RAM and incorporate a hierarchy of on-chip caches for faster data retrieval <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Optimization and Function
CPUs are optimized for sequential computations that demand extensive branching and logic <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. An example is navigation software computing the shortest route, which involves numerous conditional `if-else` statements that must be processed one by one <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

Modern CPUs feature multiple cores, enabling them to perform work in parallel. This allows users to run multiple applications simultaneously and programmers to write multi-threaded code <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. However, increasing CPU cores leads to diminishing returns due to rising costs, power consumption, and heat dissipation requirements <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. High-end chips typically feature up to 24 cores (e.g., Apple's M2 Ultra, Intel's i9), while specialized data center chips like the AMD EPYC can have 128 cores <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Architectures
Two dominant CPU architectures are ARM and x86 64-bit <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **x86 64-bit** is common in most modern desktop computers <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **ARM** is found in mobile devices due to its simplified instruction set and superior power efficiency, which translates to better battery life <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. The distinction is blurring with Apple Silicon chips demonstrating ARM's capability for high-performance computing in laptops and desktops <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. ARM is also gaining popularity with cloud providers like Amazon's Graviton 3, as it enables more computation with less power consumption, a significant expense in data centers <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Graphics Processing Unit (GPU)

A GPU, or Graphics Processing Unit, is highly optimized for [[gpu_vs_cpu_in_parallel_computing | parallel computing]] <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While a CPU might have around 16 cores, a GPU like NVIDIA's RTX 4080 boasts nearly 10,000 cores <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Each GPU core can handle a floating-point or integer computation per cycle, allowing for rapid linear algebra operations to render graphics instantly in games <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Optimization and Function
GPUs are also crucial for [[optimizing_with_cuda_for_deep_learning | training deep learning models]] that involve numerous matrix multiplications on large datasets <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

Despite having many more cores, a single CPU core is significantly faster and its architecture can handle complex logic and branching better than a single GPU core <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. GPUs are designed for simple, parallel computations, whereas much of the world's code requires sequential execution with a single thread <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. A CPU is like a versatile car, while a GPU is akin to a rocket ship—fast for straightforward parallel tasks but not ideal for general-purpose use <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

## Tensor Processing Unit (TPU)

TPUs, or Tensor Processing Units, are chips developed by Google in 2016 specifically for [[ai_capabilities_in_modern_chips | tensor operations]] like the matrix multiplication common in deep learning <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. They integrate directly with Google's TensorFlow software <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

### Optimization and Function
A TPU contains thousands of "multiply accumulators," enabling hardware to perform matrix multiplication without needing to access registers or shared memory like a GPU <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. TPUs can save millions of dollars for neural networks that would otherwise take weeks or months to train <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Data Processing Unit (DPU)

The DPU, or Data Processing Unit, is described by NVIDIA's CEO as a "third major pillar of computing" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. DPUs are primarily designed for large data centers rather than personal computers <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Optimization and Function
DPUs are most similar to CPUs, often based on the ARM architecture, but are highly optimized for moving data <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. They manage networking functions such as packet processing, routing, and security, and handle data storage operations like compression and encryption <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. The main purpose of a DPU is to offload data processing tasks from the CPU, allowing the CPU to focus on general-purpose computing <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Quantum Processing Unit (QPU)

A potential future "wild card" in computing is the QPU, or Quantum Processing Unit <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. While traditional chips deal in binary bits (ones and zeros), quantum computers utilize qubits, or quantum bits, which can exist in a superposition of both states simultaneously <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

### Theoretical Function
A qubit can represent multiple possibilities at once but collapses into one state based on probability when measured <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. Qubits are also subject to quantum entanglement, where the state of one is directly related to another regardless of distance <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. These properties are used to create Quantum Gates, which operate differently from logic gates in classical computers <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

If this technology advances, it could profoundly change the world, particularly impacting current cryptographic systems like RSA. Classical algorithms used for factorization would take billions of years to crack by brute force on today's best computers, but quantum computers could run exponentially faster algorithms, such as Shor's algorithm, posing a major threat to modern encryption and security <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. Currently, no quantum computer exists that can run Shor's algorithm effectively <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.