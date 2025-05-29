---
title: Von Neumann architecture limitations
videoId: 5tmGKTNW8DQ
---

From: [[asianometry]] <br/> 

The Von Neumann architecture is a foundational design for virtually every modern computer, storing both instructions and data in the same memory bank <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. At its core are processing units like CPUs or GPUs, which access memory to execute instructions and process data <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. While this architecture has been highly successful, contributing to the power of modern software <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>, it faces significant challenges, particularly with the rapid growth of [[memory_wall_problem_in_ai_hardware | Deep learning]] models <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.

## The [[memory_wall_problem_in_ai_hardware | Memory Wall Problem]]

Since the [[memory_wall_problem_in_ai_hardware | Deep learning]] explosion began in 2012, the largest industry models have grown hundreds of thousands of times <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. For example:
*   OpenAI's DALL-E 2 has 3.5 billion parameters <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   Google's Imagen has 4.6 billion parameters <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   GPT-3 has 175 billion parameters <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.
*   Google recently pre-trained a model with 1 trillion parameters <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

These increasingly large models strain hardware, with many limitations tied to memory usage <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. The AI hardware industry is scaling up memory and processing unit performance as fast as possible <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. For instance, [[nvidias_innovation_with_general_processing_unit_concept | Nvidia's]] V100 GPU (2017) offered 32 gigabytes, while current top-tier [[nvidias_innovation_with_general_processing_unit_concept | Nvidia]] Data Center GPUs (A100 and H100) support 80 gigabytes <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.

Despite this, hardware performance, especially memory, struggles to keep pace with model growth <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>. Memory allocations for leading-edge models can exceed hundreds of gigabytes <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. A trillion-parameter model is estimated to require 320 [[nvidias_innovation_with_general_processing_unit_concept | A100 GPUs]], each with 80 gigabytes of memory <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

This disparity leads to a "[[memory_wall_problem_in_ai_hardware | memory wall]]" or "memory capacity bottleneck" <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>, where processing units waste multiple cycles waiting for data to travel to and from memory, and for memory operations <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

### Practical and Economic Constraints
Adding more memory to GPUs faces several limits:
*   **Technological Limits**: There are practical and technological limits to how much extra memory can be added <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.
*   **Interconnections**: Issues arise with connections and wiring, akin to widening a highway not always solving traffic <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.
*   **Energy Consumption**: Significant energy is consumed shuttling data between the chip and memory due to electrical connection losses <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.
    *   Accessing memory off-chip uses 200 times more energy than a floating-point operation <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
    *   80% of a Google TPU's energy usage comes from its electrical connections, not its logic computational units <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
    *   DRAM alone can account for 40% of total system power in some GPU and CPU systems <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
    *   Energy constitutes 40% of a data center's operating costs, making storage and memory significant factors in profitability <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.
*   **Capital Costs**: The upfront cost of AI hardware is substantial. A trillion-parameter model needing 320 [[nvidias_innovation_with_general_processing_unit_concept | A100 GPUs]] (at $32,000 each MSRP) would cost $10 million <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. A hundred-trillion parameter model might require over 6,000 such GPUs <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. This doesn't include energy costs for inference, which make up 90% of a model's total costs <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.
    *   These costs risk restricting advanced AI benefits to only the wealthiest tech giants or governments <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

## Historical and Technological Limits of DRAM

Much of the current shortcomings are tied to historical and technological limits. The industry adopted Dynamic Random Access Memory (DRAM) as the basis of computers in the 1960s and 70s due to its relatively low latency and cheap bulk manufacturing <a class="yt-timestamp" data-t="04:55:00">[04:55:00]</a>.

However, after 1980, compute scaling far outpaced memory scaling <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>. CPU/GPU industries primarily optimized for transistor density <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>, while the memory industry had to balance capacity, bandwidth, and latency simultaneously <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. As a result, latency has lagged significantly:
*   Over the past 20 years, memory capacity improved 128 times <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.
*   Bandwidth improved 20 times <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.
*   Latency improved by just 30 percent <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

Furthermore, shrinking DRAM cells beyond a certain size leads to worse performance, less reliability, less security, and energy inefficiency <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. A DRAM cell stores a bit of data as a charge in a capacitor, accessed by a transistor <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. As cells shrink to nanoscale, the capacitor and transistor become leakier and more vulnerable to electrical noise, also opening new security vulnerabilities <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. These fundamental technical limitations are extremely difficult to engineer around <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.

## Proposed Solutions: [[compute_in_memory_innovations | Compute-in-Memory]]

To overcome these challenges, researchers are exploring radical ideas, such as making memory perform computations itself <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. This concept, broadly termed [[compute_in_memory_innovations | compute-in-memory]], refers to random access memory with integrated processing elements, either very near each other or on the same die <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>. Other terms include "processing in memory," "computational RAM," "near data computing," "memory-centric computing," and "in-memory computation" <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.

[[compute_in_memory_innovations | Compute-in-memory]] is well-suited for [[memory_wall_problem_in_ai_hardware | Deep learning]] because neural network models involve massive matrix calculations, primarily multiply-accumulate (MAC) operations <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>. While the arithmetic is simple, the sheer volume makes it ideal for executing MAC operations directly within the memory chip <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>. This is especially beneficial for running inference on edge devices (outside data centers) where energy, size, or heat restrictions are critical; it can cut up to 80% of a neural network's energy usage <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

### Historical Attempts

The idea of [[compute_in_memory_innovations | compute-in-memory]] dates back decades:
*   **1960s**: Professor Harold Stone of Stanford University explored logic and memory integration <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>. He noted that processor communication with memory was limited by pin count, proposing moving computation into memory caches <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.
*   **1995**: Terraces produced what is considered the first processor-in-memory chip, a 4-bit memory with an integrated single-bit logical unit <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>.
*   **1997**: UC Berkeley professors, including Professor David Patterson (inventor of RISC), created the IRAM project to put a microprocessor and DRAM on the same chip <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.

None of these early proposals gained traction due to practical manufacturing challenges:
*   **Manufacturing Conflict**: Memory and logic are difficult to manufacture together as their fabrication processes have opposing goals <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. Logic transistors prioritize speed and performance, while memory transistors prioritize high density, low cost, and low leakage <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
*   **Metal Layers**: Logic designs are complex and use more metal layers (7-12+) for interconnections, while DRAM designs are very regular with fewer metal layers (3-4) <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.
    *   Making logic circuits with a DRAM process would result in 80% larger and 22% worse performing circuits <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
    *   Making DRAM cells with a logic process (embedded DRAM) would significantly increase power consumption, space (10x more), and reduce reliability <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

### Modern Workarounds and Approaches

The industry has developed workarounds for these manufacturing shortcomings, categorizing [[compute_in_memory_innovations | compute-in-memory]] proposals into three levels:

#### Device Level
This level focuses on new memory hardware types beyond conventional DRAM and SRAM <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>.
*   **Resistive Random Access Memory (RRAM)**: Stores information by changing the electrical resistance of a material <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>. This structure allows RRAM to compute logical functions directly within memory cells <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>. RRAM is promising due to its compatibility with silicon CMOS, but substantial hurdles remain before commercialization <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.
*   **Spin Transfer Torque Magnetoresistive Random Access Memory (STT-MRAM)** <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.

#### Circuit Level
This involves modifying peripheral circuits to perform calculations directly inside SRAM or DRAM memory arrays ("in-situ computing") <a class="yt-timestamp" data-t="12:57:00">[12:57:00]</a>.
*   **Ambit**: An in-memory accelerator proposed by researchers from Microsoft, [[nvidias_innovation_with_general_processing_unit_concept | Nvidia]], Intel, ETH Zurich, and Carnegie Mellon <a class="yt-timestamp" data-t="13:21:00">[13:21:00]</a>. Ambit activates three rows of DRAM cells (two inputs, one output) to implement AND/OR logic functions <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>. While utilizing memory's internal bandwidth is attractive, Ambit's logic operations take multiple cycles, and more complex logic remains challenging <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

A significant downside of device and circuit level approaches is that their performance still falls short of current Von Neumann [[nvidias_innovation_with_general_processing_unit_concept | GPU-ASIC-centric systems]] <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>, creating a "jack of all trades, master of none" situation <a class="yt-timestamp" data-t="14:33:00">[14:33:00]</a>.

#### System Level
This middle-ground approach integrates discrete processing units and memory at a very close level <a class="yt-timestamp" data-t="14:39:00">[14:39:00]</a>. This is enabled by new packaging technologies like 2.5D or 3D memory die stacking, where DRAM dies are stacked on top of a CPU die <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. Memories connect to the CPU via thousands of channels called through-silicon Vias (TSVs), providing immense internal bandwidth <a class="yt-timestamp" data-t="15:04:00">[15:04:00]</a>.
*   **AMD 3D V-Cache**: Based on TSMC's 3D stacking technology, this adds more memory cache to processor chips <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>.
This approach allows for integrating world-class memory and logic dies closer than ever without placing them on the same die <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>.

## Challenges and Future Outlook

While [[compute_in_memory_innovations | compute-in-memory]] ideas are promising, executing them to outperform existing market solutions, like current [[nvidias_innovation_with_general_processing_unit_concept | Nvidia A100]] and [[nvidias_innovation_with_general_processing_unit_concept | H100 AI GPUs]], is challenging <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>. However, with leading-edge semiconductor technology development slowing down <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>, new ways to develop more powerful and robust AI hardware are necessary <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.

Bigger models generally perform better, and current top-performing natural language processing and computer vision models may need to grow further to improve <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. Without new systems and hardware to overcome these fundamental Von Neumann limitations, [[memory_wall_problem_in_ai_hardware | Deep learning]] might fall short of its great expectations <a class="yt-timestamp" data-t="16:28:00">[16:28:00]</a>.