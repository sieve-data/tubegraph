---
title: CPU Overclocking and Performance
videoId: vqs_0W-MSB0
---

From: [[fireship]] <br/> 
The Central Processing Unit (CPU) is often described as the "engine" of a computer or the "brain" in a skull, functioning as a sophisticated calculator that runs applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. When software is written in languages like JavaScript or Python, it creates a set of instructions that the CPU executes as machine code <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### How a CPU Works

A [[How a CPU Works | CPU]] is a precisely engineered piece of metal and silicon, containing billions of tiny transistors <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These transistors act as on/off switches, representing ones and zeros <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. To perform mathematical calculations, multiple transistors are combined to form logic gates <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. For instance, an AND gate takes two binary inputs and validates that both are true to produce a true output <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Only a few basic logic gates are needed to solve highly complex computational problems <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Modern chips contain billions of transistors that can be flipped on and off billions of times per second <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

The state of the [[How a CPU Works | CPU]] is synchronized by an oscillator called the clock generator <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Generally, the more times the clock can pulse per second, the faster the [[How a CPU Works | CPU]] can compute <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This speed is typically measured in gigahertz <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The [[How a CPU Works | CPU]] operates by interacting with system memory (RAM) through a four-step process known as the machine or instruction cycle <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>:
1.  **Fetch Phase**: The [[How a CPU Works | CPU]] uses registers to temporarily store the address of instructions from RAM. The program counter copies the address to the memory address register, and the control unit signals to copy data from that address to the instruction register <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
2.  **Decode Phase**: The control unit parses the bits in the instruction, primarily focusing on the "opcode" (the instruction itself, e.g., add, subtract) and the "operand" (the memory address to perform the operation on) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Execute Stage**: The decoded information is passed as electrical signals to the relevant parts of the [[How a CPU Works | CPU]] <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The [[Computer Architecture and Components | Arithmetic Logic Unit (ALU)]] performs mathematical operations on the data and stores results in RAM, changing the program's state <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

This cycle repeats billions of times per second <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Modern chips often utilize multiple [[How a CPU Works | CPU]] cores to run computations in parallel <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### CPU Overclocking and Performance

"Overclocking" is a practice where gamers sometimes increase their [[How a CPU Works | CPU]]'s clock speed beyond its factory settings to gain more performance <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. While this can provide a boost, it comes at the cost of higher operating temperatures and a lower life expectancy for the CPU <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Modern Processor Architectures and Performance

The design of processor architectures significantly impacts overall performance. A notable shift in the industry has been seen with Apple Silicon chips, which demonstrate significant performance gains over older Intel-based machines <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

#### System on Chip (SoC) vs. Separate Components

The key difference lies in the physicality of the design <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>:
*   **Apple Silicon (System on Chip - SoC)**: Apple Silicon is a collection of many chips housed within one silicon container <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. It's essentially an entire computer on a single chip, with the main [[How a CPU Works | CPU]], [[GPU vs CPU in Parallel Computing | GPU]], I/O controller, and ML engine all co-located <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This integrated design leads to greater efficiency in energy usage and faster task execution, especially for operations involving multiple components <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Intel-based Machines**: Typically have a [[How a CPU Works | CPU]] as a single chip, with memory, I/O, and other components located separately on the motherboard <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. While individual components might be more powerful, the separation creates inefficiencies due to the time and power required to transfer data between these distinct units <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

One drawback of the SoC design, at least currently with Apple Macs, is that components cannot be upgraded or changed <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. However, for many, the benefits of efficiency and performance outweigh this limitation <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Real-World Developer Performance Benchmarks

Developer-focused tests on Apple Silicon machines (like the M1 chip) have shown significant promise for various workflows <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

#### JavaScript Tests
*   **Speedometer (Browser Benchmark)**: This benchmark measures web application responsiveness by simulating actions in demo web apps built with popular UI frameworks (Angular, React, Ember, jQuery, etc.) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. The M1 significantly out-performed, with Safari on M1 showing the best results <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Fannkuch Redux (Node Environment)**: A CPU-intensive algorithm implemented in JavaScript for benchmarksgame.com <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. An Intel Core i9 MacBook Pro slightly beat the M1 MacBook Air in this test, but the M1 remained cool and had minimal battery drain, making the small time difference less impactful considering the price <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Nativescript Plugins Repository (NX Workspaces)**: A build of this project, based on NX Workspaces, showed the M1 MacBook Air beating the Intel MacBook Pro in build time two out of three times, with differences in tens of seconds for a three-minute build <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

#### Development Stacks with Biggest Gains
*   **iOS Development and C++ Compiling**: Building mobile apps for iOS or compiling C++ code shows a significant 40% to 50% improvement in build times <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Xcode builds, Swift builds, C++ algorithms, OpenCV, and WebKit all performed better on the M1 <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Native Software Builds**: Any builds involving natively compiled software using native tooling (compiled for Apple Silicon architecture) have shown superior speed and battery performance compared to Intel <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Even some software running via Apple's Rosetta (a translation layer for Intel x86/x64 programs on ARM chips) performed better than on native Intel hardware <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

#### Development Stacks with Limitations
*   **Android Development**: Android Studio and official Android emulators work on Apple Silicon, but they rely on Rosetta for translation <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. While Rosetta is generally good, it's insufficient for CPU-hungry Android workflows, leading to unusable results <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **.NET Development**: .NET 5 is not fully supported on ARM <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Simple console applications run, but web workflows like ASP.NET Core do not <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Full ARM support is expected with .NET 6 <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.
*   **Virtual Windows Machines**: Parallels is the only vendor currently supporting Windows virtual environments on M1 <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. However, the Windows guest operating system for ARM is still immature, and Visual Studio 2019 is not compatible with ARM <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Unity (Game Development)**: Unity works surprisingly well on Apple Silicon via Rosetta, but it's not as performant as running natively on x86 <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. A natively compatible version for M1 is expected to improve performance <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

Overall, Apple Silicon has significantly boosted many developer workflows, and further improvements are expected with future generations of the chips <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.