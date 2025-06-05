---
title: Compiling and Executing C Sharp Code
videoId: ravLFzIguCM
---

From: [[fireship]] <br/> 

[[overview_of_c_sharp_language | C#]] code undergoes a specific process to be compiled and executed.

## Compilation Process

[[overview_of_c_sharp_language | C#]] code is compiled into an intermediate language (IL) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This intermediate language is then interpreted by the Common Language Runtime (CLR) <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Execution

The Common Language Runtime executes the intermediate language as native machine code <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. A key benefit of this process is that the code can be executed on any operating system without requiring recompilation <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Getting Started and Running Code

To begin working with [[overview_of_c_sharp_language | C#]], users should install the [[c_sharp_and_net_framework | .NET Core SDK]] <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. After installation, open the terminal in an empty directory and use the `dotnet new` command to create a new application <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

To compile and execute the code, the `dotnet run` command is used <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.