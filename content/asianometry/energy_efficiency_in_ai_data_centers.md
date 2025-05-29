---
title: Energy efficiency in AI data centers
videoId: 5tmGKTNW8DQ
---

From: [[asianometry]] <br/> 

The rapid growth of Deep Learning models since 2012 has led to a significant increase in model size, straining existing hardware capabilities and creating a "memory wall" problem <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This challenge has major implications for [[impact_of_data_centers_on_energy_consumption | energy consumption]] and operational costs in [[ai_boom_and_data_center_demands | AI data centers]] <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## The Memory Wall Problem

Modern computers primarily use a Von Neumann architecture, storing both instructions and data in the same memory bank <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. While this architecture has been foundational for software, it creates a separation between processing units (CPUs or GPUs) and memory <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This separation leads to consequences, particularly for memory access <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Despite efforts by the [[ai_and_ai_chip_boom | AI hardware]] industry to scale memory and processing unit performance, hardware improvements are not keeping pace with the rapid growth of AI models <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   For instance, [[nvidia_and_ai_chip_competition | Nvidia's]] V100 GPU in 2017 offered 32 gigabytes of memory, while today's top-tier [[nvidia_and_ai_chip_competition | Nvidia]] Data Center GPUs (A100 and H100) support 80 gigabytes <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   However, leading-edge models can easily require hundreds of gigabytes of memory <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. A trillion-parameter model is estimated to need 320 A100 GPUs, each with 80 gigabytes <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

This disparity causes processing units to waste multiple cycles waiting for data to travel to and from memory and for memory operations to complete <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This limitation is widely known as the "memory wall" or "memory capacity bottleneck" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Energy and Cost Implications

Adding more memory to GPUs is not a simple solution due to practical, technological, and energetic limitations <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. A significant concern is the energy cost associated with shuttling data between the chip and memory <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>:
*   Accessing off-chip memory consumes 200 times more energy than a floating-point operation <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   80% of a [[impact_of_ai_chip_innovations_by_companies_like_google_and_amazon | Google TPU's]] energy usage comes from its electrical connections, not its computational logic units <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   DRAM (Dynamic Random Access Memory) alone can account for 40% of the total system power in some GPU and CPU systems <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Energy costs make up 40% of a data center's operating expenses, making memory and storage significant factors in their profitability <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Beyond operating costs, the upfront capital expenditure for AI hardware is substantial. A hypothetical trillion-parameter model requiring 320 A100 GPUs (each costing $32,000 MSRP) would incur an initial hardware cost of $10 million <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This does not even account for the energy costs of running inference, which constitutes 90% of a model's total lifetime costs <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Historical and Technological Limits

The current challenges are rooted in historical and technological limitations related to DRAM adoption in the 1960s and 70s, which was chosen for its low latency and cheap bulk manufacturing <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   Since 1980, compute scaling has far outpaced memory scaling <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. While CPU/GPU industries primarily optimize for transistor density <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, the memory industry must optimize for capacity, bandwidth, and latency simultaneously <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. This has led to latency improvements of only 30% over the past 20 years, compared to 128 times for capacity and 20 times for bandwidth <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   Shrinking DRAM cells beyond a certain point results in worse performance, less reliability, reduced security, poorer latency, and energy inefficiency <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. DRAM cells store data as a charge in a capacitor, accessed by a transistor <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. At nanoscale sizes, these components become leakier and more vulnerable to electrical noise and security vulnerabilities <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

These fundamental technical limitations are extremely difficult to engineer around, suggesting that small solutions will offer only incremental improvements <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Proposed Solutions: Compute in Memory (CIM)

To address the memory wall and improve [[impact_of_data_centers_on_energy_consumption | energy efficiency]], new, radical ideas are being explored, aiming for a 10x improvement over current paradigms <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. One such idea is to alleviate or eliminate the Von Neumann bottleneck by enabling memory to perform computations itself <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

Compute in Memory (CIM) refers to Random Access Memory with integrated processing elements, either very near or on the same die <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Other terms for this concept include processing-in-memory (PIM), computational RAM, near-data computing, memory-centric computing, and in-memory computation <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. CIM is particularly well-suited for deep learning, as neural network models involve massive matrix calculations, which are arithmetically simple but extremely numerous <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. An ideal CIM chip could execute multiply-accumulate (MAC) operations directly inside the memory chip <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. This approach is especially beneficial for running [[role_of_ai_accelerators_in_neural_network_training_and_inference | inference]] on edge devices, where energy, size, or heat restrictions are significant, potentially cutting up to 80% of a neural network's energy usage <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

### Historical Attempts and Manufacturing Challenges
The concept of integrating logic and memory dates back to the 1960s with Professor Harold Stone of Stanford <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. The 1990s saw further explorations, including Terraces' 1995 processor-in-memory chip and UC Berkeley's 1997 Iram project, which aimed to put a microprocessor and DRAM on the same chip <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. However, none of these early proposals gained traction due to practical reasons, primarily manufacturing difficulties <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>:
*   **Opposing Manufacturing Goals**: Logic transistors prioritize speed and performance, while memory transistors (DRAM) aim for high density, low cost, and low leakage <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Design Complexity**: DRAM designs are very regular with parallel wires, whereas logic designs are more complex <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Metal Layers**: Contemporary DRAM processes use 3-4 metal layers, while logic processes use 7-12 or more <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. Trying to integrate them often leads to compromises:
    *   Logic circuits made with a DRAM process would be 80% larger and perform 22% worse <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    *   DRAM cells made with a logic process (embedded DRAM) would consume significantly more power, take up to 10 times more space, and be less reliable <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Modern Approaches to Compute in Memory
The industry has developed workarounds for these manufacturing shortcomings, approaching CIM at three levels: device, circuit, and system <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

#### Device Level
This level focuses on new types of memory hardware beyond conventional DRAM and SRAM <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Resistive Random Access Memory (ReRAM)**: ReRAM stores information by changing a material's electrical resistance <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. This structure allows ReRAM to compute logical functions directly within memory cells <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. It is considered one of the most promising emerging memory technologies due to its compatibility with silicon CMOS, though substantial hurdles remain for commercialization <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   Spin Transfer Torque Magnetoresistive Random Access Memory (STT-MRAM) is another example <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

#### Circuit Level
This involves modifying peripheral circuits to perform calculations directly inside SRAM or DRAM memory arrays, often called "in-situ computing" <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
*   **Ambit**: Proposed by researchers from Microsoft, [[nvidia_and_ai_chip_competition | Nvidia]], Intel, ETH Zurich, and Carnegie Mellon, Ambit is an in-memory accelerator <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. It works by activating three rows of DRAM cells simultaneously (two for inputs, one for output) to implement AND/OR logic functions <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. While logically attractive for utilizing memory's internal bandwidth, Ambit takes multiple cycles for basic operations and struggles with more complex logic like XNOR <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

A major downside for both device and circuit-level CIM approaches is that their performance still falls short of current Von Neumann GPU ASIC-centric systems, inheriting the "jack of all trades, master of none" drawback from the 1990s <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

#### System Level
The industry is moving towards integrating compute in memory at a system level, bringing discrete processing units and memory closer together <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   **Advanced Packaging Technologies**: Innovations like 2.5D or 3D memory die stacking allow multiple DRAM memory dies to be stacked on top of a CPU die <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. These memories connect to the CPU via thousands of channels called Through Silicon Vias (TSVs), providing immense internal bandwidth <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **AMD's 3D V-Cache**: AMD is implementing a similar approach using TSMC's 3D stacking technology to add more memory cache to their processor chips <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. This technology could enable hundreds of gigabytes of memory to be added to an [[role_of_ai_accelerators_in_neural_network_training_and_inference | AI ASIC]], allowing the integration of world-class memory and logic dies closer than ever before without being on the same die <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

## Conclusion

While current [[nvidia_and_ai_chip_competition | Nvidia]] A100 and H100 AI GPUs are formidable competitors, the slowing pace of leading-edge semiconductor technology necessitates new methods to develop more powerful and robust hardware for AI <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. Larger models generally perform better, and today's best AI models will likely need to grow even bigger to improve <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. Without new systems and hardware that can overcome the memory wall and its associated energy limitations, deep learning may not fulfill its full potential <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.