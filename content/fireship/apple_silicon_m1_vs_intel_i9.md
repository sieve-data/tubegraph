---
title: Apple Silicon M1 vs Intel i9
videoId: vqs_0W-MSB0
---

From: [[fireship]] <br/> 

The Central Processing Unit (CPU) functions as the "brain" or "engine" of a computer, running applications by executing instructions as machine code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Modern chips, including both [[apples_m4_chip_unveiling | Apple Silicon]] and Intel, contain billions of tiny transistors—on/off switches representing ones and zeros—that perform mathematical calculations by forming logic gates <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. These transistors can flip billions of times per second, synchronized by a clock generator <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. A higher clock speed, measured in gigahertz, generally indicates a faster CPU <a class="yt-timestamp" data-t="00:54:54">[00:54:54]</a>. CPUs interact with system memory (RAM) through a four-step machine cycle: fetch, decode, execute, and store <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. Modern chips also utilize multiple CPU cores to run computations in parallel <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.

## Architectural Differences

The primary distinction between [[apples_m4_chip_unveiling | Apple Silicon]] (such as the M1 chip) and Intel-based architectures lies in their physical design:

*   **[[apples_m4_chip_unveiling | Apple Silicon]] (System on Chip - SoC)**: [[apples_m4_chip_unveiling | Apple Silicon]] is not just a processor but a collection of many chips housed within one silicon container, known as a System on Chip (SoC) <a class="yt-timestamp" data-t="04:11:11">[04:11:11]</a>. This means the CPU, GPU, I/O controller, and [[ai_capabilities_in_modern_chips | ML engine]] are all co-located <a class="yt-timestamp" data-t="04:23:23">[04:23:23]</a>. This integrated design leads to greater efficiency in energy usage and faster performance because components do not need to retrieve data from separate locations <a class="yt-timestamp" data-t="04:41:41">[04:41:41]</a>. This can be likened to having all ingredients for a sandwich (turkey, cheese, mayonnaise) in one refrigerator <a class="yt-timestamp" data-t="03:47:47">[03:47:47]</a>. A drawback for some users is that components on [[apples_m4_chip_unveiling | Apple Silicon]] Macs are generally not upgradeable or changeable after purchase <a class="yt-timestamp" data-t="05:45:45">[05:45:45]</a>.
*   **Intel-based Machines**: Traditional Intel-based machines typically have a CPU as a single chip, with memory, I/O, and other components located separately on the motherboard <a class="yt-timestamp" data-t="04:50:50">[04:50:50]</a>. While individual components might be more powerful, the need to access them from different locations can lead to less overall efficiency and higher power consumption. This is comparable to driving to separate supermarkets to gather different sandwich ingredients <a class="yt-timestamp" data-t="05:10:10">[05:10:10]</a>.

## Developer Workflow Comparisons

The shift to [[apples_m4_chip_unveiling | Apple Silicon]] has significantly impacted developer workflows, with the M1 machines generally outperforming Intel models in most build tests <a class="yt-timestamp" data-t="03:17:17">[03:17:17]</a>.

### JavaScript and Node.js

*   **Browser Benchmarks (Speedometer)**: In browser tests, the M1 chip showed significantly more iterations. Safari on M1 had the best results, with Chrome also performing well <a class="yt-timestamp" data-t="07:37:37">[07:37:37]</a>.
*   **CPU-Intensive Node.js Algorithm (Fancook Redux)**: An Intel Core i9 processor in a 16-inch MacBook Pro slightly outperformed a MacBook Air with the M1 chip in this test. However, the M1 remained cool throughout the test, and its battery was minimally impacted, making its performance impressive given the price difference <a class="yt-timestamp" data-t="08:02:02">[08:02:02]</a>.
*   **NX Workspaces Build (Nativescript plugins repository)**: The M1 MacBook Air generally beat the Intel MacBook Pro in build times, with differences in the tens of seconds <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Biggest Performance Gains on [[apples_m4_chip_unveiling | Apple Silicon]]

The most significant improvements on [[apples_m4_chip_unveiling | Apple Silicon]] are seen in specific development stacks:

*   **iOS Mobile App Development**: For building mobile apps for iOS, and compiling C++ code, developers can expect a 40-50% improvement in build times <a class="yt-timestamp" data-t="09:18:18">[09:18:18]</a>.
*   **Xcode and Swift Builds**: Tests involving Xcode and Swift builds, C++ algorithms, OpenCV, and WebKit all demonstrated the M1 chip coming out on top <a class="yt-timestamp" data-t="09:29:29">[09:29:29]</a>.
*   **Native Software Execution**: Running software natively built for the [[apples_m4_chip_unveiling | Apple Silicon]] architecture "absolutely destroyed Intel" in terms of speed and battery performance <a class="yt-timestamp" data-t="09:44:44">[09:44:44]</a>. Even software run through Apple's Rosetta 2 translation layer (which allows running x86/x64 programs on [[differences_between_arm_and_x86_architectures | ARM]] hardware) sometimes performed better than on Intel machines <a class="yt-timestamp" data-t="09:58:58">[09:58:58]</a>.

### Development Stacks with Least Benefit (or Issues)

While [[apples_m4_chip_unveiling | Apple Silicon]] shows strong promise, some workflows are not yet fully optimized:

*   **Android Development**: [[pros_and_cons_of_using_mac_os_for_development | Android Studio]] and official Android emulators work on [[apples_m4_chip_unveiling | Apple Silicon]] via Rosetta, but this translation is not sufficient for CPU-hungry Android workflows, leading to "not very usable" results currently <a class="yt-timestamp" data-t="10:16:16">[10:16:16]</a>.
*   **.NET Development**: .NET 5 is not fully supported on [[differences_between_arm_and_x86_architectures | ARM]]. While simple console applications might run, web workflows like ASP.NET Core do not work at all <a class="yt-timestamp" data-t="10:38:38">[10:38:38]</a>. Full [[differences_between_arm_and_x86_architectures | ARM]] support is expected with .NET 6 later in the year <a class="yt-timestamp" data-t="10:52:52">[10:52:52]</a>.
*   **Virtual Windows Machines**: Currently, Parallels is the only vendor supporting virtual Windows environments on M1 <a class="yt-timestamp" data-t="11:07:07">[11:07:07]</a>. However, the Windows guest operating system for [[differences_between_arm_and_x86_architectures | ARM]] is still immature, and Visual Studio 2019 is not compatible with [[differences_between_arm_and_x86_architectures | ARM]] at all <a class="yt-timestamp" data-t="11:15:15">[11:15:15]</a>.
*   **Unity (Game Development)**: Unity works surprisingly well on [[apples_m4_chip_unveiling | Apple Silicon]] via Rosetta but is less performant than running natively on x86 <a class="yt-timestamp" data-t="11:39:39">[11:39:39]</a>. A native M1-compatible version is anticipated <a class="yt-timestamp" data-t="11:49:49">[11:49:49]</a>.

Overall, [[apples_m4_chip_unveiling | Apple Silicon]] has boosted many development and professional workflows, even with its entry-level machines. Future generations of [[apples_m4_chip_unveiling | Apple Silicon]] are expected to bring even greater performance <a class="yt-timestamp" data-t="12:02:02">[12:02:02]</a>.