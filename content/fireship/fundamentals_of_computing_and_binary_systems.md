---
title: Fundamentals of computing and binary systems
videoId: -uleG_Vecis
---

From: [[fireship]] <br/> 

Software engineering allows individuals to learn to code and secure high-paying jobs, even without a deep understanding of how underlying systems function, often making it feel like "magic" <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. [[introduction_to_computer_science_concepts | Computer science]] provides the foundational knowledge to understand the mechanisms behind software <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## The Computer and Its Core Components

At its essence, a computer can be conceptualized as a Turing machine: a piece of tape holding ones and zeros, coupled with a device that can read and write to it <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. In theory, such a machine can compute anything <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Central Processing Unit (CPU)
The core of modern computers is the Central Processing Unit (CPU) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. A CPU contains billions of tiny transistors, which act like microscopic on/off switches <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

### Random Access Memory (RAM)
Unlike the CPU, which executes code, Random Access Memory (RAM) is used to store data for applications <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. RAM is a volatile storage area where each location has a memory address that the CPU can read from and write to <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The CPU and RAM together can be considered the "brain" of the computer <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### Input and Output Devices
For a computer to be useful, it must handle input and output <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Examples include keyboards and mice as input devices, and monitors as output devices <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Operating Systems (OS)
Most developers do not directly interact with the complex hardware components because operating system kernels, such as [[linux_kernel_and_system_architecture | Linux]], Mac, and Windows, manage all hardware resources through device drivers <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Shell and Command Line Interface
The primary entry point for interacting with an operating system is often the shell <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. A shell is a program that exposes the operating system to the user <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. It wraps the kernel, taking text input and producing output, forming what is known as a Command Line Interface (CLI) <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. CLIs can connect to local or remote computers using protocols like Secure Shell (SSH) <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Data Representation: Binary Systems

### Bits and Bytes
The smallest piece of information a computer can use is a **bit**, which represents the value at one of the on/off switches (transistors) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Bits are typically grouped into packages of eight, called a **byte** <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. One byte can represent 256 different values <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Binary and Hexadecimal
Binary is a counting system that uses only two characters: one and zero <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Since humans find binary difficult to read, it is often represented in hexadecimal (base-16) format <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Hexadecimal uses ten numbers and six letters to represent a four-bit group called a **nibble** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

### Character Encoding
When characters are typed on a keyboard, they are mapped to a binary value using a character encoding standard like ASCII or UTF-8 <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Machine Code
Code written in a [[programming_languages_and_their_execution_models | programming language]] is eventually converted into **machine code**, which is a binary format that the CPU can decode and execute <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Memory Management

### Pointers
A **pointer** is a variable whose value is the memory address of another variable, enabling low-level memory control <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Garbage Collection
Many [[programming_languages_and_their_execution_models | languages]] implement a **garbage collector** to handle memory management automatically <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. This system automatically allocates and de-allocates memory when an object is no longer referenced in the program <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Endianness
When characters or data are stored in memory, their order matters <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Big Endian**: The most significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   **Little Endian**: The least significant byte is stored at the smallest memory address <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

## Programming Paradigms and Memory Allocation

### Call Stack and Heap
When a function is called, the [[programming_languages_and_their_execution_models | programming language]] places it into memory on the **call stack**, a short-term chunk of memory for executing code <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. If a function recursively calls itself indefinitely, it can lead to a **stack overflow error** as the call stack keeps growing <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

For long-lived data that cannot reside on the call stack, most languages use a separate memory area called the **heap** <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Unlike the call stack, the heap can grow and shrink dynamically based on application usage <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. The heap also allows for passing objects by reference, enabling multiple variables to point to the same object without increasing memory footprint <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### Threads and Concurrency
Modern CPUs often contain multiple **threads**, which virtually divide the physical CPU core to allow simultaneous code execution <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Parallelism**: Some [[programming_languages_and_their_execution_models | languages]] support parallelism, allowing code to literally execute on different threads at the same time <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Concurrency**: Many languages are single-threaded but achieve concurrency through models like an event loop or co-routines <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. These models can pause or delay normal code execution to handle multiple jobs on a single thread simultaneously <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

## Virtualization and Networking Basics

### Virtual Machines
In modern computing, work is often done in the cloud using a **virtual machine (VM)** <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. A VM is software that simulates hardware, allowing large physical computers to be split into many smaller virtual ones <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### The Internet and Networking Protocols
Virtual machines form the backbone of the [[understanding_the_internet_and_the_world_wide_web | Internet]], connected via the Internet Protocol (IP) <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Each machine has a unique **IP address** for identification on the network <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. IP addresses are often aliased to a Uniform Resource Locator (URL) registered in a global database called the Domain Name Service (DNS) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

To establish a connection, two computers perform a TCP handshake, enabling them to exchange messages known as packets <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. A security layer like SSL (Secure Sockets Layer) is commonly used on top of this to encrypt and decrypt messages over the network <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>. Once connected, data can be securely shared using the Hypertext Transfer Protocol (HTTP) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.

Modern servers provide a standardized way for clients to request data through an **Application Programming Interface (API)** <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. A common API architecture is REST, where URLs are mapped to different data entities available on the server <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.