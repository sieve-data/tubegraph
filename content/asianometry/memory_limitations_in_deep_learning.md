---
title: Memory limitations in deep learning
videoId: 5tmGKTNW8DQ
---

From: [[asianometry]] <br/> 

Since the deep learning explosion began in 2012, the largest models in the industry have expanded by hundreds of thousands of times <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Current models like OpenAI's DALL-E 2 have 3.5 billion parameters, Google's Imagen has 4.6 billion, and GPT-3 has 175 billion <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Google recently pre-trained a model with 1 trillion parameters <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. These increasingly large models significantly strain the capacity of existing [[custom_ai_hardware_design_for_neural_networks | hardware]] to accommodate them, with many limitations tied to memory usage <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## The Memory Wall Problem

Virtually all modern computers operate on a [[von_neumann_architecture_vs_brain_computing | Von Neumann architecture]], which stores both instructions and data in the same memory bank <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Processing units like CPUs or GPUs access this memory to execute instructions and process data <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. While the [[von_neumann_architecture_vs_brain_computing | Von Neumann architecture]] has been instrumental in making software powerful, it differs significantly from a human brain's processing, which tightly integrates compute with memory and I/O <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Computers, however, separate compute from memory and communication, leading to consequences, especially for memory <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

The [[custom_ai_hardware_design_for_neural_networks | AI hardware]] industry is working to scale up memory and processing unit performance as quickly as possible <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. For example, [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]]'s V100 GPU (2017) offered 32 GB of memory, while today's top-tier [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]] data center GPUs, A100 and H100, boast 80 GB <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Despite this, hardware performance, particularly memory, struggles to keep pace with the rapid growth of these models <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

Memory allocations for leading-edge models can easily exceed hundreds of gigabytes <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. A trillion-parameter model is estimated to require 320 A100 GPUs, each with 80 GB of memory, even with the latest parallelization techniques <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. These disparities between processing and capacity result in processing units wasting multiple cycles waiting for data to move in and out of memory, as well as for read/write operations <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This bottleneck is known as the "memory wall" or "memory capacity bottleneck" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Practical and Technological Limits to Memory Expansion

Adding more memory to GPUs faces practical and technological limits, including issues with connections and wiring <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

Furthermore, there are significant [[energy_efficiency_in_ai_hardware | energy limitations]] associated with shuttling data between the chip and memory, as electrical connections incur losses <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. Accessing off-chip memory uses 200 times more energy than a floating-point operation <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Eighty percent of Google's TPU energy usage stems from electrical connections, not computational units <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. In some GPU and CPU systems, DRAM alone accounts for 40% of total system power <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

### Economic Implications

[[energy_efficiency_in_ai_hardware | Energy]] makes up 40% of a data center's operating costs, making storage and memory a significant factor in profitability <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Beyond operating costs, the upfront capital cost of purchasing [[custom_ai_hardware_design_for_neural_networks | AI hardware]] is substantial <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. A trillion-parameter model needing 320 A100 GPUs (at $32,000 each) would cost $10 million for hardware alone <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. A hundred-trillion-parameter model could require over 6,000 such GPUs <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. These costs do not include the [[energy_efficiency_in_ai_hardware | energy costs]] for [[ai_inference_versus_training_hardware | running inference]], which accounts for 90% of a model's total cost <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This financial barrier risks restricting the benefits of advanced AI to only the wealthiest tech giants or governments <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

## Historical and Technological Limits of DRAM

Many shortcomings are linked to historical and technological limits. The industry adopted Dynamic Random Access Memory (DRAM) as the basis of computers in the 1960s and 70s due to its relatively low latency and cheap bulk manufacturing <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

However, after 1980, compute [[scaling_laws_and_neural_language_models | scaling]] far outpaced memory [[scaling_laws_and_neural_language_models | scaling]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. CPU and GPU industries primarily optimized for transistor density, while the memory industry had to simultaneously scale DRAM capacity, bandwidth, and latency <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Over the past 20 years, memory capacity has improved 128 times, and bandwidth 20 times, but latency has only improved by 30% <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

Additionally, the memory industry discovered that shrinking DRAM cells beyond a certain size led to worse performance, less reliability, reduced security, and [[energy_efficiency_in_ai_hardware | energy inefficiency]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. A DRAM cell stores data as a charge in a capacitor accessed by a transistor <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. As cells shrink to nanoscale sizes, the capacitor and transistor become leakier and more vulnerable to electrical noise, also opening up new security vulnerabilities <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. These fundamental limitations are extremely difficult to engineer around <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

## Solutions: Compute in Memory (CIM)

To overcome the [[challenges_in_scaling_ai_hardware | hardware challenges]] and the memory wall, researchers are exploring radical ideas like making memory perform computations itself <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

[[compute_in_memory_technology | Compute in memory]] refers to a random access memory integrated with processing elements, either very near each other or on the same die <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. It's also known by terms like processing in memory, computational RAM, near-data computing, memory-centric computing, or in-memory computation <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. While the term can refer to concepts expanding on SRAM (memory cache on chip with CPU), the primary focus here is bringing processing ability to the computer's main memory <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.

This idea is well-suited for deep learning, where running a neural network model involves calculating massive matrices <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Since the arithmetic (e.g., multiply and accumulate operations) is relatively simple but abundant, an ideal [[compute_in_memory_technology | compute in memory]] chip can execute these operations right inside the memory chip <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This is particularly beneficial for [[ai_inference_versus_training_hardware | running inference]] on the edge (outside the data center) where [[energy_efficiency_in_ai_hardware | energy]], size, or heat restrictions apply <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Cutting up to 80% of a neural network's [[energy_efficiency_in_ai_hardware | energy usage]] would be a significant advantage <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Historical Context

The concept of [[compute_in_memory_technology | compute in memory]] dates back to the 1960s <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Professor Harold Stone of Stanford University first explored logic and memory integration, noting that microprocessor transistor growth outpaced communication ability with memory due to limited pins <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. He proposed moving computation into memory caches <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

The 1990s saw further developments:
*   **1995:** Terraces produced an early "processor in memory" chip, a 4-bit memory with an integrated single-bit logical unit that could apply simple logic and write data back to memory <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **1997:** UC Berkeley professors, including David Patterson, created the IRAM project to put a microprocessor and DRAM on the same chip <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

However, these early proposals didn't catch on for practical reasons <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Manufacturing Challenges

Manufacturing memory and logic together is difficult because their fabrication processes have opposing goals <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Logic transistors prioritize speed and performance, while memory transistors aim for high density, low cost, and low leakage <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

*   **Process incompatibility:** It's challenging to build a logic process with a DRAM process and vice versa <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. DRAM designs are regular with many parallel wires, whereas logic designs are more complex <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   **Metal layers:** More metal layers allow for greater complexity but increase current leakage and reduce reliability <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Contemporary DRAM processes use 3-4 metal layers, while logic processes use 7-12 or more <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Logic circuits made with a DRAM process would be 80% larger and perform 22% worse <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    *   DRAM cells made with a logic process (embedded DRAM or eDRAM) use significantly more power, take up to 10 times more space, and are less reliable <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

### Modern Workarounds and Approaches

The industry has developed workarounds for these manufacturing shortcomings, proposing [[compute_in_memory_technology | compute in memory]] solutions on three levels: device, circuit, and system <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

#### Device Level
This level focuses on new types of memory hardware beyond conventional DRAM and SRAM, such as Resistive Random Access Memory (RRAM or ReRAM) and Spin-Transfer Torque Magnetoresistive Random Access Memory (STT-MRAM) <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

ReRAM, one of the more promising emerging memory technologies, stores information by changing a material's electrical resistance <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. This structure allows ReRAM to compute logical functions directly within its memory cells <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. ReRAM is close to commercialization due to its compatibility with silicon CMOS, but substantial hurdles remain <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

#### Circuit Level
At this level, peripheral circuits are modified to perform calculations directly within SRAM or DRAM memory arrays (in-situ computing) <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. These approaches are clever but require deep knowledge of memory function and can be complex <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

One example is Ambit, an in-memory accelerator proposed by researchers from Microsoft, [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]], Intel, ETH Zurich, and Carnegie Mellon <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. In a DRAM memory, which contains sub-arrays with many rows, Ambit activates three rows simultaneously (two for inputs, one for output) to implement AND/OR logic functions <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. This utilizes the memory's internal bandwidth for calculations <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. However, Ambit's logic operations take multiple cycles, and more complex logic (like XNOR) remains challenging to implement <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.

A major downside for both device and circuit level [[compute_in_memory_technology | compute in memory]] approaches is that their performance still falls short of what current [[von_neumann_architecture_vs_brain_computing | Von Neumann]] GPU ASIC-centric systems can achieve <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>, leading to a "jack of all trades, master of none" situation <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

#### System Level
The industry appears to be moving towards implementing [[compute_in_memory_technology | compute in memory]] at a system level, integrating discrete processing units and memory very closely <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. This is enabled by new packaging technologies like 2.5D or 3D memory die stacking, where multiple DRAM memory dies are stacked atop a CPU die <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. These memories connect to the CPU via thousands of channels called Through Silicon Vias (TSVs), providing immense internal bandwidth <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

AMD is exploring this with its 3D V-Cache, based on TSMC's 3D stacking technology, to add more memory cache to processors <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. Future applications could use similar advanced packaging to add hundreds of gigabytes of memory to an AI ASIC, integrating world-class memory and logic dies more closely than ever without needing them on the same die <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

## Outlook

While ideas are abundant, the challenge lies in executing them effectively enough to displace established market leaders <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. The current [[nvidia_and_competition_in_the_ai_chip_market | Nvidia]] A100 and H100 AI GPUs present formidable competition <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. However, with leading-edge semiconductor technology [[challenges_in_scaling_ai_hardware | slowing down]], new methods are necessary to advance towards more powerful and robust [[custom_ai_hardware_design_for_neural_networks | hardware]] for AI <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

Generally, bigger models perform better <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. Today's top natural language processing and computer vision models still have room for improvement, suggesting they may need to grow larger <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>. Unless new systems and [[custom_ai_hardware_design_for_neural_networks | hardware]] can overcome the aforementioned memory limitations, deep learning risks falling short of its full potential <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>.