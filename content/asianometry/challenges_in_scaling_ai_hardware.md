---
title: Challenges in scaling AI hardware
videoId: 5tmGKTNW8DQ
---

From: [[asianometry]] <br/> 

The growth of deep learning models since 2012 has been exponential, with the industry's largest models increasing in size by hundreds of thousands of times <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. For instance, OpenAI's DALL-E 2 has 3.5 billion parameters, Google's Imagen has 4.6 billion, and GPT-3 has 175 billion <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Google has even pre-trained a model with 1 trillion parameters <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These increasingly large models strain the capabilities of current hardware, with many limitations tied to memory usage <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## The Von Neumann Bottleneck and Memory Wall

Virtually all modern computers operate on a Von Neumann architecture, which stores both instructions and data in the same memory bank <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Processing units like CPUs or GPUs must access this memory to execute instructions and process data <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. While this architecture has enabled powerful software, it fundamentally differs from a human brain, which tightly integrates compute with memory and I/O <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Computers separate compute from memory and communication, leading to significant consequences, particularly for memory <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

This separation creates a "memory wall" or "memory capacity bottleneck," where a processing unit wastes multiple cycles waiting for data to travel to and from memory, as well as for memory read/write operations <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Consequences of the Memory Wall

The [[the_ai_and_ai_chip_boom_landscape | AI hardware]] industry is rapidly scaling up memory and processing unit performance <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. For example, [[Nvidia and competition in the AI chip market | Nvidia's]] V100 GPU had a 32 GB offering in 2017, and their top-tier A100 and H100 data center GPUs now sport 80 GB <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. However, hardware performance is not keeping pace with the rapid growth of AI models, especially regarding memory <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Memory allocations for leading-edge models can easily exceed hundreds of gigabytes <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. A trillion-parameter model is estimated to require 320 A100 GPUs, each with 80 GB of memory <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### [[Energy efficiency in AI hardware | Energy Limitations]]

A significant challenge in adding more memory is the substantial [[energy_efficiency_in_ai_hardware | energy limitations]] associated with shuttling data between the chip and memory <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. These electrical connections incur losses that cost energy <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Accessing memory off-chip uses 200 times more energy than a floating-point operation <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. For example, 80% of Google's TPU energy usage comes from its electrical connections rather than its computational units <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. DRAM alone can account for 40% of the total system power in some GPU and CPU systems <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### [[Financial sustainability of AI investments | Financial Costs]]

Energy constitutes 40% of a data center's operating costs, making storage and memory a significant factor in profitability <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Beyond operating costs, the upfront [[financial_sustainability_of_ai_investments | capital costs]] of purchasing AI hardware are substantial <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. A trillion-parameter model requiring 320 A100 GPUs (each costing $32,000 MSRP) would cost a clean $10 million for hardware alone <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. A 100 trillion-parameter model could demand over 6,000 such GPUs <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. These figures do not include the energy costs for running inference, which account for 90% of a model's total costs <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This risks restricting advanced AI benefits to only the wealthiest tech giants or governments <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Historical Context and Manufacturing Challenges

Many of these shortcomings are tied to historical and technological limits <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. In the 1960s and 70s, Dynamic Random Access Memory (DRAM) was adopted as the basis of computers due to its relatively low latency and cheap bulk manufacturing <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

After 1980, compute scaling (primarily focused on transistor density) far outpaced memory scaling <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. The memory industry, unlike CPUs/GPUs, had to optimize for DRAM capacity, bandwidth, and latency simultaneously <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Over the past two decades, memory capacity improved 128 times and bandwidth 20 times, but latency improved by just 30% <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

A second issue is that shrinking DRAM cells beyond a certain size leads to worse performance, reliability, security, latency, and [[energy_efficiency_in_ai_hardware | energy inefficiency]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. A DRAM cell stores one bit of data as a charge in a capacitor, accessed by a transistor <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. As the cell scales down to nanoscale, the capacitor and transistor become leakier and more vulnerable to electrical noise and security vulnerabilities <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. These fundamental technical limitations are extremely difficult to engineer around <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### Manufacturing Incompatibility

One major practical reason compute-in-memory ideas didn't catch on in the past is the difficulty of manufacturing memory and logic together <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Their fabrication processes have opposing goals <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>:
*   Logic transistors prioritize speed and performance.
*   Memory transistors prioritize high density, low cost, and low leakage.

DRAM designs are highly regular with many parallel wires, while logic designs are much more complex <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Circuit elements in a chip are connected via metal layers; more layers allow more complexity but increase current leakage and reduce reliability <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Contemporary DRAM processes use 3-4 metal layers, whereas logic processes use 7-12 or more <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

Estimates suggest that if logic circuits were made with a DRAM process, they would be 80% bigger and perform 22% worse <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Conversely, making DRAM cells with a logic process (embedded DRAM) results in cells that use significantly more power, take up to 10 times more space, and are less reliable <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Proposed Solutions: [[Custom AI hardware design for neural networks | Compute-in-Memory]] (CIM)

The memory wall problem opens the door to radical new ideas for a potential 10x improvement over current paradigms <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Beyond [[silicon_photonics_in_ai_chip_development | silicon photonics]] for energy-efficient data transfer <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>, a key approach is to alleviate or eliminate the Von Neumann bottleneck by making the memory perform computations itself <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

[[Custom AI hardware design for neural networks | Compute-in-memory]] (CIM), also known by terms like processing-in-memory, computational RAM, or memory-centric computing, refers to integrating processing elements with random access memory <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. These elements can be very near each other or integrated onto the same die <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. The idea is well-suited for deep learning, which heavily relies on calculating massive matrices and multiply-accumulate (MAC) operations <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. An ideal CIM chip could execute MAC operations directly inside the memory chip <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>, particularly beneficial for [[ai_inference_versus_training_hardware | AI inference]] on the edge, where energy, size, or heat restrictions apply <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, potentially cutting up to 80% of a neural network's energy usage <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

### Historical Attempts

The idea of integrating logic and memory dates back to the 1960s with Professor Harold Stone of Stanford University <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. He noted the growing number of transistors in microprocessors but limited communication with memory due to pin count, proposing moving computation into memory caches <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

The 1990s saw further explorations:
*   In 1995, Terraces produced what was arguably the first processor-in-memory chip, a 4-bit memory with an integrated single-bit logical unit <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   In 1997, UC Berkeley professors, including David Patterson (inventor of RISC), created the IRAM project with the goal of putting a microprocessor and DRAM on the same chip <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

None of these early proposals gained widespread adoption due to practical manufacturing reasons <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>, as detailed in the "Manufacturing Incompatibility" section above.

### Modern Approaches

The industry has since developed workarounds for manufacturing shortcomings, with many CIM proposals categorized at three levels: device, circuit, and system <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

1.  **Device Level:** This approach leans on new types of memory hardware beyond conventional DRAM and SRAM <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
    *   **Resistive Random Access Memory (ReRAM or RRAM):** One of the more promising emerging memory technologies <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Unlike conventional RAM that stores information via charge in a capacitor, ReRAM stores data by changing the electrical resistance of a material <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. This structure allows ReRAM to compute logical functions directly within memory cells <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. ReRAM is close to commercialization due to its compatibility with silicon CMOS, but substantial hurdles remain <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    *   **Spin Transfer Torque Magnetoresistive Random Access Memory (STT-MRAM):** Another example of an emerging memory technology <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

2.  **Circuit Level:** This involves modifying peripheral circuits to perform calculations directly inside SRAM or DRAM memory arrays (often called "in-situ computing") <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. These are clever but require deep knowledge of memory function and can be complex to understand <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.
    *   **Ambit:** An in-memory accelerator proposed by researchers from Microsoft, [[Nvidia and competition in the AI chip market | Nvidia]], Intel, ETH Zurich, and Carnegie Mellon <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. In a DRAM memory, which contains sub-arrays with many rows of DRAM cells, Ambit activates three rows simultaneously (two for inputs, one for output) to implement AND/OR logic functions, leveraging the memory's internal bandwidth <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. However, Ambit's logic operations take multiple cycles, and more complex logic (like XNOR) remains challenging <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

3.  **System Level:** The middle ground the industry is moving towards involves integrating discrete processing units and memory at a very close level <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. This is enabled by new packaging technologies like 2.5D or 3D memory die stacking <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>, where DRAM memory dies are stacked on top of a CPU die <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Connections are made using thousands of channels called Through-Silicon Vias (TSVs), providing immense internal bandwidth <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
    *   AMD is working on similar technology with their 3D V-Cache, based on TSMC's 3D stacking packaging technology, used to add more memory cache to processors <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. This approach allows for integrating world-class memory and logic dies closer than ever before without needing to place them on the same die <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

## Current State and Outlook

While the concept of CIM is promising, current device and circuit-level approaches still fall short of the performance achievable with existing Von Neumann GPU ASIC-centric systems <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This echoes the "jack of all trades, master of none" situation seen in the 1990s <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

However, with leading-edge semiconductor technology slowing down, new methods are needed to leapfrog towards more powerful and robust hardware for running AI <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. Generally, bigger models perform better, and today's best-performing natural language processing and computer vision models still have room for improvement, which implies they might need to get even larger <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. Unless new systems and hardware can overcome these memory and scaling limits, deep learning may not fulfill its full potential <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.