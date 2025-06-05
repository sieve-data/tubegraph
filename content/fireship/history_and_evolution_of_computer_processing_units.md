---
title: History and evolution of computer processing units
videoId: r5NQecwZs1A
---

From: [[fireship]] <br/> 

The foundation of computer processing units (PUs) lies in silicon dioxide, refined into silicon substrate, which can act as both a conductor and insulator <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Electrical engineers inscribe billions of microscopic symbols on this material, allowing it to "speak" the binary language when electricity passes through it <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This enables the creation of powerful machines capable of computation <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Early Computing Milestones

The history of computing has seen rapid advancements over the last 100 years <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### The Z1 Computer
The Z1, created by Konrad Zuse in his mother's basement in 1936, was the first truly programmable computer <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
It featured:
*   A highly mechanical design with over twenty thousand parts <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   Representation of binary data using sliding metal sheets <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   Capabilities for Boolean algebra and floating-point numbers <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   A clock rate of 1 Hertz, executing one instruction per second <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
The Z1 was destroyed in 1943 during the bombardment of Berlin <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### The Von Neumann Architecture
In 1945, after a decade of intense thought on computer design, the Von Neumann architecture emerged <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. This foundational design, still used in modern chips today, describes how data and instructions are stored in the same memory space and handled by a [[how_a_cpu_works | processing unit]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Semiconductor Breakthroughs
A significant breakthrough occurred a couple of years later with the invention of the transistor <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A transistor is a semiconductor capable of amplifying or switching electrical signals, representing a one if current passes through it or a zero if it doesn't <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This invention marked a huge leap forward <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Following this, the integrated circuit was developed in 1958, enabling multiple transistors to be placed on a single silicon chip <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Rise of the Microprocessor

In 1971, Intel released the first commercially available microprocessor <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This 4-bit processor, which could handle four bits of data at a time, had approximately 2,300 transistors and a clock speed of 740 kilohertz, considered extremely fast for its era <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Modern Central Processing Units (CPUs)

The central processing unit (CPU) serves as the brain of a computer, running the operating system, executing programs, and managing hardware <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. It has access to system RAM and includes a hierarchy of on-chip caches for faster data retrieval <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Optimization and Parallelism
[[function_and_optimization_of_different_processing_units | CPUs]] are optimized for sequential computations requiring extensive branching and logic, such as navigation software algorithms that compute shortest routes with many `if/else` statements <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

Modern CPUs feature multiple cores, enabling them to perform work in parallel. This allows users to run multiple applications simultaneously and programmers to write multi-threaded code <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. While increasing CPU cores can enhance speed, it leads to diminishing returns due to increased power consumption, heat dissipation, and cost <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. As of the video's creation, 24 cores are typically the upper limit for high-end chips like Apple's M2 Ultra and Intel's i9, though massive 128-core AMD Epyc chips exist for data centers <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Modern CPUs are measured in gigahertz, representing billions of cycles per second, a significant advancement from the Z1's 1 Hertz <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### CPU Architectures: x86 and ARM
Two prominent CPU architectures are x86 64-bit and ARM <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **x86**: Most commonly found on modern desktop computers <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **ARM**: Predominant in mobile devices due to its simplified instruction set and superior power efficiency, leading to better battery life <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

This distinction is changing with Apple Silicon chips demonstrating ARM's capability for high-performance computing on laptops and desktops <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Microsoft is also investing in running Windows with ARM <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Furthermore, ARM is gaining popularity with cloud providers like Amazon's Graviton 3 and the Neoverse chip, enabling more efficient cloud computing with less power consumption <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Evolution of Specialized Processing Units

While the CPU remains central, other specialized processing units have evolved to handle specific computational tasks, often due to the limitations of a general-purpose CPU for certain workloads <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This represents a significant shift in [[computer_architecture_and_components | computer architecture and components]].

### [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | Graphics Processing Unit (GPU)]]
Originally designed for graphics, GPUs are highly optimized for parallel computing <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Unlike a CPU with a few dozen cores, a GPU like Nvidia's RTX 4080 can have nearly 10,000 cores, each performing floating-point or integer computations per cycle <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This enables rapid linear algebra operations for rendering graphics in games <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. GPUs are also essential for training deep learning models, which involve extensive matrix multiplication on large datasets, driving significant demand in the GPU market <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

While GPUs excel at parallel tasks, a single CPU core is generally faster and its architecture handles complex logic and branching better than a GPU, which is designed for simpler, highly parallel computations <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | Tensor Processing Unit (TPU)]]
Tensor Processing Units (TPUs) are chips developed by Google in 2016, specifically designed for tensor operations, like the matrix multiplication common in deep learning <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. A TPU contains thousands of "multiply accumulators," allowing it to perform matrix multiplication without needing to access registers or shared memory like a GPU <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. TPUs can significantly reduce the time and cost of training large neural networks <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. These units represent a significant advancement in [[ai_capabilities_in_modern_chips | AI capabilities in modern chips]].

### [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | Data Processing Unit (DPU)]]
The Data Processing Unit (DPU) is a newer type of PU, described by Nvidia's CEO as the "third major pillar of computing" <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. DPUs are primarily for large data centers, rather than personal computers <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. They are often CPU-like and based on the ARM architecture, but are highly optimized for moving data, handling networking functions (packet processing, routing, security), and data storage (compression, encryption) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. Their main goal is to offload data processing jobs from the main CPU, allowing it to focus on general-purpose computing <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### [[future_prospects_of_computing_technology | Quantum Processing Unit (QPU)]]
A potential future development is the Quantum Processing Unit (QPU) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Unlike current chips that use bits (ones and zeros), quantum computers deal in qubits (quantum bits) which can exist in a superposition of both states simultaneously <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Qubits can represent multiple possibilities at once, collapsing into one state when measured based on probability <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. They are also subject to quantum entanglement, where the state of one is related to another regardless of distance <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. These properties are used to create Quantum Gates, which operate differently from logic gates in classical computers <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. If this technology matures, it could profoundly change the world, potentially breaking current cryptographic systems like RSA by running exponentially faster algorithms like Shor's algorithm for factorization <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.