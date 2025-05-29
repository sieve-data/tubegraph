---
title: Von Neumann architecture vs brain computing
videoId: 5tmGKTNW8DQ
---

From: [[asianometry]] <br/> 
The growth of deep learning models has put significant strain on current hardware, particularly in how memory is utilized <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This challenge is often referred to as the "memory wall" or "memory capacity bottleneck" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### The Von Neumann Architecture

Virtually all modern computers operate based on the Von Neumann architecture <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This means that both instructions and data are stored in the same memory bank <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Processing units, such as CPUs or GPUs, access this memory to execute instructions and process data <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. The Von Neumann architecture has been instrumental in making software as powerful as it is today <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Human Brain Computing

In contrast to the Von Neumann architecture, the human brain operates differently <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The brain's computational ability is relatively low precision <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. However, it tightly integrates computation with memory and input/output communication <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

### The Memory Wall Problem

Modern computers, adhering to the Von Neumann architecture, run on high-precision arithmetic (e.g., 32 or 64-bit floating point) <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, but they separate computation from memory and communication <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This separation has significant consequences, particularly for memory <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Since the deep learning explosion began in 2012, the largest models have grown hundreds of thousands of times <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. For example, OpenAI's DALL-E 2 has 3.5 billion parameters, Google's Imagen has 4.6 billion, and GPT-3 has 175 billion parameters <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Google recently pre-trained a model with 1 trillion parameters <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

While the [[the_ai_and_ai_chip_boom_landscape | AI hardware industry]] is scaling up memory and processing unit performance as fast as possible (e.g., Nvidia's A100 and H100 GPUs sport 80 gigabytes of memory compared to the 2017 V100's 32 gigabytes) <a class="yt-timestamp" data-t="00:01:55">[00:02:13]</a>, hardware performance, especially memory, is not keeping pace with the rapid growth of these models <a class="yt-timestamp" data-t="00:02:15">[00:02:21]</a>. Memory allocations for leading-edge models can easily exceed hundreds of gigabytes <a class="yt-timestamp" data-t="00:02:23">[00:02:28]</a>. A trillion-parameter model is estimated to require 320 Nvidia A100 GPUs, each with 80 gigabytes of memory <a class="yt-timestamp" data-t="00:02:30">[00:02:37]</a>.

These disparities mean that a processing unit wastes multiple cycles waiting for data to travel to and from memory, and for memory read/write operations <a class="yt-timestamp" data-t="00:02:39">[00:02:54]</a>.

### [[challenges_in_scaling_ai_hardware | Challenges in Scaling AI Hardware]]

There are practical and technological limits to simply adding more memory to GPUs <a class="yt-timestamp" data-t="00:03:07">[00:03:10]</a>:

*   **Energy Consumption**: Significant [[energy_efficiency_in_ai_hardware | energy limitations]] are associated with shuttling data between the chip and memory due to losses in electrical connections <a class="yt-timestamp" data-t="00:03:19">[00:03:28]</a>. Accessing off-chip memory uses 200 times more energy than a floating-point operation <a class="yt-timestamp" data-t="00:03:32">[00:03:39]</a>. Eighty percent of a Google TPU's energy usage comes from its electrical connections rather than its computational units <a class="yt-timestamp" data-t="00:03:40">[00:03:45]</a>. DRAM alone can account for 40% of a system's total power in some GPU and CPU systems <a class="yt-timestamp" data-t="00:03:47">[00:03:53]</a>. Given that energy accounts for 40% of a data center's operating costs, memory and storage are significant factors in profitability <a class="yt-timestamp" data-t="00:03:54">[00:04:05]</a>.
*   **Capital Costs**: The upfront cost of purchasing [[ai_inference_versus_training_hardware | AI hardware]] is substantial <a class="yt-timestamp" data-t="00:04:09">[00:04:14]</a>. A trillion-parameter model, needing 320 A100 GPUs (each costing $32,000 MSRP), would have an upfront hardware cost of $10 million <a class="yt-timestamp" data-t="00:04:16">[00:04:29]</a>. A hundred-trillion-parameter model might require over 6,000 such GPUs <a class="yt-timestamp" data-t="00:04:29">[00:04:34]</a>. This doesn't include the energy costs, which account for 90% of a model's total operational costs, risking advanced AI benefits being restricted to a few large entities <a class="yt-timestamp" data-t="00:04:36">[00:04:52]</a>.

### Historical Context of Memory Scaling

The shortcomings are rooted in historical and technological limits. The industry adopted Dynamic Random Access Memory (DRAM) in the 1960s and 70s due to its relatively low latency and cheap bulk manufacturing <a class="yt-timestamp" data-t="00:04:55">[00:05:14]</a>.

However, after 1980, compute scaling far outpaced memory scaling <a class="yt-timestamp" data-t="00:05:26">[00:05:29]</a>. The CPU/GPU industries primarily optimized for transistor density <a class="yt-timestamp" data-t="00:05:32">[00:05:36]</a>. The memory industry, conversely, had to scale DRAM capacity, bandwidth, *and* latency simultaneously <a class="yt-timestamp" data-t="00:05:40">[00:05:47]</a>. Over the past 20 years, memory capacity improved 128 times and bandwidth 20 times, but latency only improved by 30 percent <a class="yt-timestamp" data-t="00:05:51">[00:06:00]</a>.

Furthermore, shrinking DRAM cells beyond a certain size leads to worse performance, less reliability, less security, and energy inefficiency <a class="yt-timestamp" data-t="00:06:02">[00:06:16]</a>. This is because a DRAM cell stores data as a charge in a capacitor accessed by a transistor <a class="yt-timestamp" data-t="00:06:16">[00:06:29]</a>. At nanoscale sizes, the capacitor and transistor become leakier and more vulnerable to electrical noise and security vulnerabilities <a class="yt-timestamp" data-t="00:06:31">[00:06:45]</a>. These are fundamental hardware limitations, making them extremely difficult to engineer around <a class="yt-timestamp" data-t="00:06:47">[00:06:52]</a>.

### Towards New Paradigms: [[compute_in_memory_technology | Compute in Memory]]

The challenges open the door for radical new ideas, potentially offering a 10x improvement over current paradigms <a class="yt-timestamp" data-t="00:07:00">[00:07:08]</a>. One such idea is to alleviate or eliminate the Von Neumann bottleneck and memory wall problems by making memory perform computations itself <a class="yt-timestamp" data-t="00:07:21">[00:07:27]</a>.

[[compute_in_memory_technology | Compute in memory]] refers to Random Access Memory (RAM) with integrated processing elements, either very near each other or on the same die <a class="yt-timestamp" data-t="00:07:30">[00:07:39]</a>. It is also known by other terms like processing in memory, computational RAM, near-data computing, or memory-centric computing <a class="yt-timestamp" data-t="00:07:42">[00:07:51]</a>. While the concept can extend to SRAM (used for CPU memory caches), the primary focus is on bringing processing ability to the computer's main memory <a class="yt-timestamp" data-t="00:08:03">[00:08:17]</a>.

This idea is well-suited for deep learning, which involves calculating massive matrices <a class="yt-timestamp" data-t="00:08:20">[00:08:27]</a>. Neural networks often require many multiply-accumulate (MAC) operations <a class="yt-timestamp" data-t="00:08:27">[00:08:32]</a>. While the arithmetic is simple, the sheer volume of operations is the challenge <a class="yt-timestamp" data-t="00:08:35">[00:08:40]</a>. An ideal [[compute_in_memory_technology | compute in memory]] chip could execute MAC operations directly inside the memory chip <a class="yt-timestamp" data-t="00:08:41">[00:08:47]</a>. This is particularly beneficial for [[ai_inference_versus_training_hardware | running inference]] on edge devices outside data centers, where energy, size, or heat restrictions apply <a class="yt="yt-timestamp" data-t="00:08:48">[00:08:55]</a>, as it could cut up to 80 percent of a neural network's energy usage <a class="yt-timestamp" data-t="00:08:57">[00:09:00]</a>.

#### Historical Attempts

The concept of [[compute_in_memory_technology | compute in memory]] dates back to the 1960s <a class="yt-timestamp" data-t="00:09:03">[00:09:06]</a>.

*   **Harold Stone (1960s)**: Professor Harold Stone of Stanford University explored the idea of logic and memory integration, noting the growing number of transistors in microprocessors versus the limited communication ability with memory due to pin count <a class="yt-timestamp" data-t="00:09:06">[00:09:22]</a>. He proposed moving part of the computation into memory caches <a class="yt-timestamp" data-t="00:09:24">[00:09:27]</a>.
*   **Terraces (1995)**: Produced what was likely the first processor-in-memory chip, a standard 4-bit memory with an integrated single-bit logical unit capable of applying simple logic to data and writing it back to memory <a class="yt-timestamp" data-t="00:09:30">[00:09:52]</a>.
*   **Iram Project (1997)**: Professors at UC Berkeley, including [[seymour_cray_and_the_cray_supercomputer | David Patterson]], created the Iram project to put a microprocessor and DRAM on the same chip <a class="yt-timestamp" data-t="00:09:53">[00:10:06]</a>.

Despite these proposals in the 1990s, none gained widespread adoption due to practical reasons <a class="yt-timestamp" data-t="00:10:07">[00:10:14]</a>.

#### Manufacturing Challenges

A primary obstacle has been the difficulty of manufacturing memory and logic together, as their fabrication processes have opposing goals <a class="yt-timestamp" data-t="00:10:14">[00:10:19]</a>.

*   **Logic Transistors**: Optimized for speed and performance <a class="yt-timestamp" data-t="00:10:22">[00:10:25]</a>.
*   **Memory Transistors**: Designed for high density, low cost, and low leakage simultaneously <a class="yt-timestamp" data-t="00:10:25">[00:10:33]</a>.

It is challenging to build a logic process with a DRAM process, and vice versa <a class="yt-timestamp" data-t="00:10:33">[00:10:38]</a>. DRAM designs are highly regular with many parallel wires, while logic designs are much more complex <a class="yt-timestamp" data-t="00:10:38">[00:10:43]</a>. Logic processes use more metal layers (7 to 12+) for complexity, unlike DRAM processes (3 to 4 layers) <a class="yt-timestamp" data-t="00:10:46">[00:11:06]</a>. If logic circuits were made with a DRAM process, they would be 80 percent bigger and perform 22 percent worse <a class="yt-timestamp" data-t="00:11:07">[00:11:17]</a>. Conversely, making DRAM cells with a logic process (embedded DRAM) leads to significantly more power usage, up to 10 times more space, and lower reliability <a class="yt-timestamp" data-t="00:11:19">[00:11:32]</a>.

#### Modern Approaches to [[compute_in_memory_technology | Compute in Memory]]

The industry has devised workarounds for these manufacturing shortcomings, proposing [[compute_in_memory_technology | compute in memory]] solutions at three levels: device, circuit, and system <a class="yt-timestamp" data-t="00:11:34">[00:11:47]</a>.

1.  **Device Level**: Leans on new types of memory hardware beyond conventional DRAM and SRAM <a class="yt-timestamp" data-t="00:11:47">[00:11:53]</a>.
    *   **Resistive Random Access Memory (ReRAM or RRAM)**: Stores information by changing the electrical resistance of a material, allowing it to compute logical functions directly within memory cells <a class="yt-timestamp" data-t="00:12:08">[00:12:37]</a>. ReRAM is one of the more promising emerging memory technologies due to its compatibility with silicon CMOS, though substantial hurdles remain <a class="yt-timestamp" data-t="00:12:42">[00:12:55]</a>.
    *   **Spin-Transfer Torque Magnetoresistive Random Access Memory (STT-MRAM)** <a class="yt-timestamp" data-t="00:12:00">[00:12:08]</a>.

2.  **Circuit Level**: Modifies peripheral circuits to perform calculations directly inside SRAM or DRAM memory arrays ("in-situ computing") <a class="yt-timestamp" data-t="00:12:57">[00:13:12]</a>.
    *   **Ambit**: An in-memory accelerator proposed by researchers from Microsoft, Nvidia, Intel, ETH Zurich, and Carnegie Mellon <a class="yt-timestamp" data-t="00:13:21">[00:13:30]</a>. It leverages DRAM's sub-arrays by activating three rows simultaneously (two for inputs, one for output) to implement AND/OR logic functions <a class="yt-timestamp" data-t="00:13:33">[00:13:50]</a>. While it utilizes the memory's internal bandwidth, it performs basic logic functions over multiple cycles, and more complex logic like XNOR remains challenging <a class="yt-timestamp" data-t="00:13:53">[00:14:14]</a>.

These device and circuit level approaches currently fall short of the performance achieved by existing Von Neumann GPU ASIC-centric systems <a class="yt-timestamp" data-t="00:14:16">[00:14:29]</a>, reinforcing the "jack of all trades, master of none" issue <a class="yt-timestamp" data-t="00:14:31">[00:14:38]</a>.

3.  **System Level**: The industry is trending towards integrating discrete processing units and memory at a very close level <a class="yt-timestamp" data-t="00:14:39">[00:14:50]</a>. This is enabled by new packaging technologies like 2.5D or 3D memory die stacking, where DRAM memory dies are stacked on top of a CPU die <a class="yt-timestamp" data-t="00:14:53">[00:15:03]</a>. These memories connect to the CPU using thousands of channels called Through Silicon Vias (TSVs), providing immense internal bandwidth <a class="yt-timestamp" data-t="00:15:04">[00:15:15]</a>.
    *   **AMD's 3D V-cache**: Uses TSMC's 3D stacking technology to add more memory cache to its processor chips <a class="yt-timestamp" data-t="00:15:15">[00:15:28]</a>.
    *   Future possibilities include using similarly advanced packaging to add hundreds of gigabytes of memory to an [[custom_ai_hardware_design_for_neural_networks | AI ASIC]], integrating world-class memory and logic dies closer than ever without needing them on the same die <a class="yt-timestamp" data-t="00:15:28">[00:15:43]</a>.

### Conclusion

While radical ideas in the lab are abundant, the challenge lies in executing them to outperform existing market solutions like Nvidia's A100 and H100 AI GPUs, which are formidable competitors <a class="yt-timestamp" data-t="00:15:45">[00:16:02]</a>. However, as leading-edge semiconductor technology slows down, new methods are needed to leapfrog towards more powerful and robust hardware for AI <a class="yt-timestamp" data-t="00:16:04">[00:16:12]</a>.

Generally, bigger models perform better, and today's best natural language processing and computer vision models still need to grow to improve further <a class="yt-timestamp" data-t="00:16:14">[00:16:26]</a>. Unless new systems and hardware can overcome the limitations of the Von Neumann architecture, deep learning may not fulfill its great expectations <a class="yt-timestamp" data-t="00:16:28">[00:16:40]</a>.