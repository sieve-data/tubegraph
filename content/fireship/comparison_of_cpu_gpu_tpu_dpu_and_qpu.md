---
title: Comparison of CPU GPU TPU DPU and QPU
videoId: r5NQecwZs1A
---

From: [[fireship]] <br/> 

A computer needs a processing unit (PU) to compute things at the hardware level, including [[how_a_cpu_works | CPUs]], GPUs, TPUs, and DPUs <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The last hundred years have seen significant advancements in these technologies <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## History and Evolution of Computer Processing Units

The first truly programmable computer was the Z1, created by Konrad Zuse in 1936 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. It was highly mechanical with over 20,000 parts <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a> and represented binary data with sliding metal sheets <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. The Z1 could perform Boolean algebra and floating-point numbers <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, operating at a clock rate of 1 Hertz, meaning it executed one instruction per second <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. In contrast, modern [[how_a_cpu_works | CPUs]] are measured in gigahertz, or billions of cycles per second <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

In 1945, the Von Neumann architecture was developed, which is still used in modern chips today <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This foundational design describes how data and instructions are stored in the same memory space and handled by a processing unit <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. A few years later, the invention of the [[transistors_and_logic_gates_in_a_cpu | transistor]] marked a huge breakthrough <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A [[transistors_and_logic_gates_in_a_cpu | transistor]] is a semiconductor that can amplify or switch electrical signals <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, representing a one if current passes through it or a zero if it doesn't <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The integrated circuit was developed in 1958, allowing multiple [[transistors_and_logic_gates_in_a_cpu | transistors]] to be placed on a single silicon chip <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Finally, in 1971, Intel released the first commercially available microprocessor, which had all the features of a modern [[how_a_cpu_works | CPU]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This was a 4-bit processor that could handle four bits of data at a time <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, with approximately 2,300 [[transistors_and_logic_gates_in_a_cpu | transistors]] and a clock speed of 740 kilohertz <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Central Processing Unit (CPU)

The Central Processing Unit (CPU) is often considered the brain of a computer <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Its primary functions include running the operating system, executing programs, and managing hardware <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. It accesses the system's RAM and includes a hierarchy of caches on the chip for faster data retrieval <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

[[how_a_cpu_works | CPUs]] are optimized for sequential computations that require extensive branching and logic <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. For example, navigation software computing the shortest route involves a lot of conditional logic that must be computed sequentially <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Modern [[how_a_cpu_works | CPUs]] also feature multiple cores, enabling them to perform work in parallel <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>, allowing users to run multiple applications simultaneously <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Programmers can write multi-threaded code to utilize these cores <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

However, simply adding more [[how_a_cpu_works | CPU]] cores has diminishing returns due to increased cost, power consumption, and heat dissipation requirements <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. As of this video, 24 cores are typically the upper limit for high-end consumer chips like Apple's M2 Ultra and Intel's i9, though specialized chips like the 128-core AMD Epyc exist for data centers <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### CPU Architectures
Two common [[history_and_evolution_of_computer_processing_units | CPU]] architectures are x86 and ARM <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **x86 (64-bit)**: Commonly found in most modern desktop computers <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **ARM**: Predominantly used in mobile devices due to its simplified instruction set and better power efficiency, leading to longer battery life <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. However, this distinction is blurring with Apple Silicon chips demonstrating ARM's capability for high-performance computing on laptops and desktops <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Microsoft is also investing in Windows on ARM, and ARM is gaining popularity in cloud providers like Amazon's Graviton 3 for increased computing power with less consumption <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

A [[how_a_cpu_works | CPU]] is described as a versatile "Toyota Camry," capable of many tasks but not specialized for specific, intense computations <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Graphics Processing Unit (GPU)

When a [[how_a_cpu_works | CPU]] reaches its limitations, such as when running graphically intensive applications, a Graphics Processing Unit (GPU) comes into play <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. A [[gpu_vs_cpu_in_parallel_computing | GPU]] is highly optimized for [[gpu_vs_cpu_in_parallel_computing | parallel computing]] <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Unlike a [[how_a_cpu_works | CPU]] with a typical maximum of 24 cores (or 128 for data centers), a [[gpu_vs_cpu_in_parallel_computing | GPU]] like NVIDIA's RTX 4080 can have nearly 10,000 cores <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. Each of these cores can handle a floating-point or integer computation per cycle <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, allowing games to perform massive amounts of linear algebra in parallel to render graphics instantly <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

[[role_of_gpus_and_tpus_in_deep_learning | GPUs]] are also essential for training [[role_of_gpus_and_tpus_in_deep_learning | deep learning]] models, which involve extensive matrix multiplication on large datasets <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This has led to massive demand in the [[role_of_gpus_and_tpus_in_deep_learning | GPU]] market <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### GPU vs. CPU Cores
While [[gpu_vs_cpu_in_parallel_computing | GPUs]] have significantly more cores than [[how_a_cpu_works | CPUs]], not all cores are created equal <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. A single [[how_a_cpu_works | CPU]] core is much faster and can handle complex logic and branching <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, whereas a [[gpu_vs_cpu_in_parallel_computing | GPU]] is designed for simple computations <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Most general code needs to run sequentially with a single thread <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. A [[gpu_vs_cpu_in_parallel_computing | GPU]] is compared to a "rocket ship" – fast for straight-line tasks but not ideal for varied, everyday computations <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

## Tensor Processing Unit (TPU)

While [[gpu_vs_cpu_in_parallel_computing | GPUs]] have become popular for AI, specific hardware exists for this use case called the Tensor Processing Unit (TPU) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. These chips are similar to [[gpu_vs_cpu_in_parallel_computing | GPUs]] but are designed specifically for tensor operations, particularly the matrix multiplication required for [[role_of_gpus_and_tpus_in_deep_learning | deep learning]] <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Google developed TPUs in 2016 to integrate directly with its TensorFlow software <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

A TPU contains thousands of "multiply accumulators," which allow the hardware to perform matrix multiplication without needing to access registers or shared memory like a [[gpu_vs_cpu_in_parallel_computing | GPU]] would <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. For neural networks that take weeks or months to train, a TPU can significantly reduce training time and cost <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

## Data Processing Unit (DPU)

The newest type of processing unit discussed is the Data Processing Unit (DPU) <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. NVIDIA's CEO has described it as the "third major pillar of computing" <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Users are unlikely to use a DPU in their personal computers as they are designed specifically for big data centers <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

DPUs are most like [[how_a_cpu_works | CPUs]] and are typically based on the ARM architecture <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. They are highly optimized for moving data around <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>, handling networking functions such as packet processing, routing, and security <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, as well as data storage tasks like compression and encryption <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The main goal of a DPU is to offload data processing jobs from the [[how_a_cpu_works | CPU]], allowing the [[how_a_cpu_works | CPU]] to focus on general-purpose computing <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Quantum Processing Unit (QPU)

A potential "wild card" that might be experienced in our lifetime is the Quantum Processing Unit (QPU) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. While all traditional chips deal with bits (ones and zeros), quantum computers deal in qubits, or Quantum bits <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Qubits can exist in a superposition of both states simultaneously <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>, and when measured, they collapse into one of the possible states based on probability <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

These qubits are also subject to quantum entanglement, meaning the state of one qubit is directly related to another, regardless of the distance between them <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. These properties are used to create Quantum Gates, which function differently from [[transistors_and_logic_gates_in_a_cpu | logic gates]] in regular computers <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Impact of Quantum Computing
If quantum computing technology significantly advances, it could revolutionize the world <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. Current cryptographic systems like RSA rely on the fact that classical algorithms for factorization would take billions of years to crack by brute force <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. However, quantum computers could run algorithms like Shor's algorithm, which are exponentially faster at factorization <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, posing a major threat to modern encryption and security <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Fortunately, no quantum computer today can run this algorithm, and such a development would likely be kept secret <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

```chart
type: doughnut
labels: [CPU, GPU, TPU, DPU, QPU]
series: [1, 1, 1, 1, 1]
```
> [!NOTE] This chart is symbolic and does not represent actual market share or usage, but rather the distinct categories of processing units discussed.

For a more in-depth look at how [[how_a_cpu_works | CPUs]] execute programs, consider exploring resources like cpu.land, a free resource written by high schoolers Lexi Matic and Hack Club <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.