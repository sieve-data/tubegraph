---
title: Role of software in ASML machine development
videoId: 1fOA85xtYxs
---

From: [[asianometry]] <br/> 

ASML's lithography machines, critical for semiconductor manufacturing, operate with extreme precision, positioning wafers to within a few nanometers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This incredible accuracy and the complex operations involved are heavily reliant on sophisticated software.

## Early Indications and Growth
From 1989 to 2000, the number of CPUs and sensors within ASML's tools saw a significant increase, growing six and eight times, respectively <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. This growth in hardware components directly correlates with the increasing reliance on complex software for their control and functionality.

The scale of this software development is evident in the size of their codebases:
*   The 1989 PAS5000 stepper contained 200 million lines of source code, including comments <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   By 2003, the [[ASML lithography machine operation and precision | TWINSCAN]] machine's codebase had expanded to 1.25 billion lines <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

While the complexity of software cannot be solely judged by lines of code, this dramatic increase highlights the massive investment and evolution in software development within ASML <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

## Software in Operation
Software plays a crucial role in managing the intricate movements and processes of an ASML machine. For instance, the wafer stage movements within the [[ASML lithography machine operation and precision | TWINSCAN]] are coordinated by the Control Architecture Reference Model motion control platform, or CARM, which is powered by FPGAs and process controllers <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

The measurement stage, which is crucial for achieving throughput benchmarks, involves complex scans to prepare and align the wafer in relation to the reticle, ensuring precise focus and accurate overlay <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a> <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This entire measurement process is heavily governed by software, which must figure out the correct sequence of actions to ensure a competitive machine <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

## Impact and Future
The aggressive leveraging of software has been identified as a key driver behind ASML's strong performance <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. The former CEO noted that the software development team doubled in size every four years <a class="yt-timestamp" data-t="00:15:59">[00:15:59]</a>. This continuous and significant investment underscores the fundamental role software plays in ASML's technological advancements and market position.