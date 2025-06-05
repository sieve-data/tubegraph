---
title: How a CPU Works
videoId: vqs_0W-MSB0
---

From: [[fireship]] <br/> 

The Central Processing Unit (CPU) functions as the "engine" of a car or the "brain" in a skull for a computer <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It is essentially a sophisticated calculator designed to execute applications <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. When software is written in languages like JavaScript or Python, it generates a set of instructions that the [[compilation_and_execution_process_in_assembly_language | CPU]] executes as machine code <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Core Components and Operation

A [[computer_architecture_and_components | CPU]] is a precisely engineered component made of metal and silicon, containing billions of tiny [[transistors_and_logic_gates_in_a_cpu | transistors]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These [[transistors_and_logic_gates_in_a_cpu | transistors]] act as on/off switches, representing ones and zeros <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

To perform mathematical calculations, a [[computer_architecture_and_components | CPU]] combines multiple [[transistors_and_logic_gates_in_a_cpu | transistors]] to form [[transistors_and_logic_gates_in_a_cpu | logic gates]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For example, an "and" [[transistors_and_logic_gates_in_a_cpu | logic gate]] requires two binary inputs to be true to produce a true output <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Even a few basic [[transistors_and_logic_gates_in_a_cpu | logic gates]] can solve highly complex computational problems <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Modern chips contain billions of [[transistors_and_logic_gates_in_a_cpu | transistors]] that can switch on and off billions of times per second <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The [[computer_architecture_and_components | CPU]]'s state is synchronized by an oscillator called the clock generator <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Generally, a higher pulse rate per second from the clock generator results in a faster [[computer_architecture_and_components | CPU]], with speeds typically measured in gigahertz <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Gamers sometimes [[cpu_overclocking_and_performance | overclock their CPUs]] for more performance, though this leads to higher temperatures and reduced lifespan <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### The Machine/Instruction Cycle

To run applications, the [[computer_architecture_and_components | CPU]] interacts with the system memory (RAM) through a four-step process known as the machine or instruction cycle <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

1.  **Fetch Phase**: A software program is a set of instructions stored in RAM <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The [[computer_architecture_and_components | CPU]] uses registers to temporarily store the address and memory it needs to interact with <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The program counter starts at zero, copying an address to the memory address register <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The control unit then signals to copy the data from that address to the instruction register <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
2.  **Decode Phase**: The control unit analyzes the bits within the instruction <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. The "opcode" specifies the instruction (e.g., add or subtract), while the "operand" indicates the memory address on which to perform the operation <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
3.  **Execute Phase**: The decoded information is converted into electrical signals and sent to the relevant parts of the [[computer_architecture_and_components | CPU]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The arithmetic logic unit (ALU) performs mathematical operations on the data and stores the results in RAM, thereby changing the program's state <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

This cycle repeats billions of times per second <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Modern chips often have multiple [[computer_architecture_and_components | CPU]] cores to run several computations in [[gpu_vs_cpu_in_parallel_computing | parallel]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Modern Processor Architectures: Apple Silicon (M1 Chip)

The introduction of Apple Silicon, particularly the M1 chip, has significantly impacted the industry, including software development <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The M1 machines have generally outperformed Intel machines in most build tests <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### System on Chip (SoC) Design

Apple Silicon chips utilize a "System on Chip" (SoC) design <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This means that many chips, including the main [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | CPU]], [[comparison_of_cpu_gpu_tpu_dpu_and_qpu | GPU]], I/O controller, and ML engine, are housed together in a single silicon container <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This co-location improves efficiency and speed, particularly for tasks involving multiple components, while using less power <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

In contrast, traditional Intel-based machines have a single [[computer_architecture_and_components | CPU]] chip, with memory and I/O controllers located separately on the motherboard <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. While individual components in Intel systems might be powerful, the separation leads to increased energy usage and time taken for components to communicate, reducing overall efficiency <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

A drawback of the SoC design, at least with current Apple Macs, is the inability to upgrade or change individual components after purchase <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. However, the benefits of a more efficient design often outweigh this limitation, providing better performance <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Impact on Developer Workflows

Developer-focused tests on Apple Silicon machines reveal significant promise for various workflows <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

#### JavaScript and Node.js

*   **Browser Benchmarks (Speedometer)**: The Speedometer benchmark, which measures web application responsiveness, showed significantly more iterations on the M1 chip <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Safari on M1 had the best results, with Chrome also performing well <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Node.js Benchmarks**: A [[computer_architecture_and_components | CPU]]-intensive JavaScript algorithm called Fannkuch Redux, used for benchmarks game, showed the Intel Core i9 MacBook Pro slightly outperform the M1 MacBook Air <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. However, considering the price difference, the M1's ability to stay cool and maintain battery life made it a compelling choice <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Real-World Builds**: A NativeScript plugins repository build, based on Nx workspaces, showed the M1 MacBook Air beating the Intel MacBook Pro in build times two out of three times, differing by only tens of seconds <a class="yt-timestamp" data-t="00:08:42">[00:09:01]</a>.

#### Tech Stacks with Major Gains

*   **iOS Development (Xcode/Swift)**: [[function_and_optimization_of_different_processing_units | Developers]] building mobile apps for iOS and compiling C++ code see a 40% to 50% improvement in build times on Apple Silicon <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Xcode, Swift, C++ algorithms, OpenCV, and WebKit builds all showed the M1 coming out on top <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Native Software**: Builds using natively compiled software for the Apple Silicon architecture exhibit superior speed and battery performance compared to Intel <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Even some Intel/AMD x64/x86 programs running via Apple's Rosetta 2 translation layer performed better than on Intel hardware <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

#### Tech Stacks with Current Limitations

*   **Android Development**: While Android Studio and official Android emulators work on Apple Silicon, they currently use Rosetta for translations <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. This translation is not sufficient for [[computer_architecture_and_components | CPU]]-intensive Android workflows, making the results not very usable at present <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **.NET Development**: .NET version 5 is not fully supported on ARM <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Simple console applications run fine, but web workflows like ASP.NET Core do not work at all <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Full ARM support is expected with .NET 6 by the end of 2021 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   **Virtual Windows Machines**: Parallels is the only vendor supporting M1 for virtual Windows environments, but the Windows guest operating system for ARM is still immature <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. Visual Studio 2019 is incompatible with ARM, and even Windows' built-in x64 to ARM translation is not stable enough for it <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Unity (Game Development)**: Unity works surprisingly well on Apple Silicon via Rosetta <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. However, it is not as performant as running natively on x86, though a native M1-compatible version is in development <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

## Conclusion

Overall, Apple Silicon has provided a significant boost to many workflows for [[function_and_optimization_of_different_processing_units | developers]] and other professions, with future improvements expected to impact gaming as well <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. The initial M1 tests show improvements even with entry-level machines, suggesting that future generations of Apple Silicon will be even more performant and potentially elevate the entire industry <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.