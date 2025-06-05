---
title: System on Chip SoC vs Traditional Architectures
videoId: vqs_0W-MSB0
---

From: [[fireship]] <br/> 

The Central Processing Unit (CPU) is often described as the "engine" or "brain" of a computer, functioning like a highly sophisticated calculator that runs applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Software written in languages like JavaScript or Python is translated into machine code executed by the CPU <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. A CPU is a meticulously crafted piece of metal and silicon, containing billions of tiny transistors—on/off switches representing ones and zeros <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. These transistors combine to form logic gates, which enable complex mathematical calculations and computational problems <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Modern chips contain billions of transistors that can switch on and off billions of times per second <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The CPU's state is synchronized by an oscillator called the clock generator, with higher clock speeds (measured in gigahertz) generally indicating faster computation <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Overclocking CPUs can boost performance but at the cost of higher temperatures and reduced life expectancy <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

To run applications, the CPU interacts with system memory (RAM) through a four-step machine or instruction cycle <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>:
1.  **Fetch Phase:** Instructions stored in RAM are copied from a memory address (held in registers) to the instruction register <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
2.  **Decode Phase:** The control unit parses the instruction's bits, identifying the "opcode" (e.g., add, subtract) and the "operand" (memory address for the operation) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Execute Stage:** The decoded information is converted into electrical signals and sent to relevant CPU parts, like the Arithmetic Logic Unit (ALU), which performs calculations and stores results in RAM <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
This cycle repeats billions of times per second, with modern chips utilizing multiple CPU cores for parallel computations <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

## Evolution with Apple Silicon

The introduction of Apple Silicon, specifically the M1 chip, has significantly impacted the [[computer_architecture_and_components | computer architecture and components]] industry, including software development <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. The M1 machines have generally outperformed Intel machines in various build tests <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### System on Chip (SoC) Explained

Apple Silicon is an example of a **System on Chip (SoC)** architecture <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. An SoC is a collection of many chips housed within a single silicon container, essentially an entire computer on one chip <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. In an SoC design, the main CPU, GPU, I/O controller, and [[ai_capabilities_in_modern_chips | ML engine]] are all co-located <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

This integrated design offers significant advantages in efficiency:
*   **Energy Usage:** SoCs use very little power <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Speed:** They are faster when tasks involve multiple components, as all "ingredients" are in one place, eliminating the need for data to travel across a motherboard <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This concept can be likened to having all sandwich ingredients in one refrigerator, saving time and energy <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.

### Traditional Architectures (Intel/AMD)

In contrast, traditional architectures (like Intel-based machines) have separate components <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The CPU is a single chip, and memory, I/O, and other components are located elsewhere on the motherboard <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. While individual components in traditional systems might be more powerful than those on current Apple Silicon machines, their separation comes at a cost <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. Data must "travel all over town" to access different components, which consumes more power and reduces efficiency <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Key Differences and Trade-offs

| Feature                  | System on Chip (SoC) - e.g., Apple Silicon M1                                                                                              | Traditional Architecture - e.g., Intel/AMD                                                                                                      |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Component Integration**  | Multiple components (CPU, GPU, I/O, ML engine) integrated into a single silicon container <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a> | Components are separate chips located at different places on the motherboard (CPU, RAM, I/O, etc.) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a> |
| **Efficiency**             | High energy efficiency, faster for multi-component tasks due to co-location <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>      | Less efficient due to data transfer between separate components, higher power consumption <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>  |
| **Upgradeability**         | Components are not typically upgradable or changeable; users "get what's on the menu" <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a> | Individual components can often be upgraded or replaced, offering more customization <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> |
| **Performance (M1 vs. Intel)** | Generally provides better overall performance, especially for tasks utilizing multiple integrated components <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a> | Individual components might be more powerful, but overall system performance can be bottlenecked by component separation <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a> |

While the lack of upgradeability in SoC designs like Apple's may be a drawback for some, the benefits of a more efficient design often outweigh these cons, providing better performance overall <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

## Impact on Development Workflows

The new [[differences_between_arm_and_x86_architectures | Apple Silicon]] design has shown significant promise for developer workflows <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### JavaScript Development
*   **Browser Benchmarks (Speedometer):** The M1 Safari demonstrated significantly more iterations, even "going off the scale," while Chrome also performed well <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Node.js Benchmarks (fancook redux):** An Intel Core i9 MacBook Pro slightly outperformed an M1 MacBook Air, but the M1 stayed cool, consumed less battery, and offered a better price-to-performance ratio <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **NativeScript Builds:** In a three-minute build test of a NativeScript plugins repository (using NX workspaces), the M1 MacBook Air beat the Intel MacBook Pro two out of three times, with only tens of seconds difference <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Tech Stacks with Major Gains
Developers building mobile apps for iOS or compiling C++ code see a 40% to 50% improvement in build times on Apple Silicon <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. Tests involving Xcode and Swift builds, C++ algorithms, OpenCV, and WebKit all showed the M1 coming out on top <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Software compiled natively for the [[differences_between_arm_and_x86_architectures | Apple Silicon architecture]] (ARM) generally provides superior speed and battery performance compared to Intel-based machines <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Even when running some software via Apple's Rosetta translation layer (which allows x86/x64 programs to run on ARM), performance can still be better than on Intel hardware <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Tech Stacks with Current Limitations
*   **Android Development:** Android Studio and official Android emulators work on Apple Silicon via Rosetta, but they are not yet performant enough for CPU-intensive Android workflows, leading to "not very usable" results <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **.NET Development:** .NET 5 is not fully supported on ARM. While simple console applications run, web workflows like ASP.NET Core do not work at all yet <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. Full ARM support is expected with .NET 6 by the end of the year <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Visual Studio 2019 is also not compatible with ARM <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Virtual Windows:** Parallels is the only vendor supporting M1 for virtual Windows environments, but the Windows guest operating system for ARM is still immature <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Unity (Game Development):** Unity works surprisingly well on Apple Silicon via Rosetta but is not as performant as running natively on x86 <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. A native M1-compatible version is expected soon <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Overall, Apple Silicon has significantly boosted many developer and professional workflows, and future generations of Apple Silicon machines are expected to be even more performant <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.