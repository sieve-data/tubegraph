---
title: Linux kernel and its role
videoId: LKCVKw9CzFo
---

From: [[fireship]] <br/> 

While statistically 96% of human viewers are not using [[introduction_to_linux | Linux]], it is a superior, free, and open-source operating system with about a 4% share of the PC market <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Conversely, [[introduction_to_linux | Linux]] is the dominant operating system on servers, with 96% of non-human bots utilizing it <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. For programmers or developers, understanding [[introduction_to_linux | Linux]] is essential, as code eventually runs and may fail on it, requiring the ability to SSH into a [[basic_linux_commands_and_operations | Linux]] terminal for fixes <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Historical Context

Before understanding [[introduction_to_linux | Linux]], it is important to recognize its predecessor, Unix, an operating system developed at AT&T Bell Labs in the 1970s <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Unix's development led to POSIX (Portable Operating System Interface) standardization, ensuring compatibility between different systems <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Its influence is still strong, with macOS, Android, FreeBSD, and most [[Linux Distributions and their Origins | Linux distributions]] being POSIX compliant <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

In 1987, Minix, an OS for academic use, was developed, but its code redistribution was restricted <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This restriction inspired Finnish computer science student Linus Torvalds to develop [[history_and_creation_of_linux | Linux]] in 1991 <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. [[history_and_creation_of_linux | Linux]] is free and open-source software, licensed under GPL 2.0, meaning it is free to distribute, modify, and profit from <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## What is the Linux Kernel?

What is commonly referred to as [[introduction_to_linux | Linux]] is, in fact, not an operating system itself, but rather an operating system kernel <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. It is written in the C programming language and acts as the interface between software applications and the hardware <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Kernel Boot Process

When a computer is powered on, the boot loader (commonly GRUB) loads the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] into Random Access Memory (RAM) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. From there, the kernel detects hardware and starts the init system, typically System D <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Once initialized, the kernel launches applications in user space, leading to a login screen for the user <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Responsibilities of the Linux Kernel

The kernel has significant responsibilities as the user interacts with the system:
*   **Memory Management** It allocates and deallocates memory for processes <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. It can also create virtual memory by utilizing the hard drive, allowing the system to use more memory than physically available <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **[[Linux file system hierarchy | File System Interaction]]** The kernel provides a virtual [[Linux file system hierarchy | file system]] to interact with files across different systems <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The fourth extended [[Linux file system hierarchy | file system]] (ext4) is the most common default on [[introduction_to_linux | Linux]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Device Management** It interacts with peripheral devices via drivers <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Process Management** Any command or program execution creates a process on the CPU, which is managed by the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The kernel assigns a unique Process ID (PID) to each process <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. It can send signals to processes, such as `Sigterm` for graceful termination or `Sigkill` for forceful termination using the `kill` command <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

## Kernel Protection and User Interaction

The kernel is protected by the CPU's protection ring at ring zero, giving it the highest level of privilege <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Most users operate in user space at ring three, with the lowest level of privilege <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

To perform operations requiring kernel access, such as writing to the [[Linux file system hierarchy | file system]], **system calls** are used <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. A system call transitions from ring three to ring zero <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Functions like `write` are wrappers provided by Glibc (the GNU standard library for C), which offers various wrappers for making system calls <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## The GNU Project and Core Utilities

The GNU project, pronounced "gnu", predates the [[role_of_linux_kernel_in_operating_systems | Linux kernel]] and was started in 1983 by Richard Stallman <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It provides all the core utilities for [[introduction_to_linux | Linux]], which are essential software utilities that make the kernel useful to humans <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. When a command like `echo` is run in the terminal, it triggers a system call to the kernel, which then manages drivers and permissions to display output on the screen <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.