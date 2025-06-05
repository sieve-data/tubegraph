---
title: Building AI sandboxes
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

[[Building AI sandboxes | AI sandboxes]] are emerging as a critical component for the advancement of AI agents, providing a secure and capable environment for code execution and computer use <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Abhishek, the solo founder and developer of Arachis, an open-source code execution and computer use sandboxing service for AI agents, highlights their necessity and construction <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Why AI Sandboxes Are Needed

AI models, such as GPT-4, leverage tool calling (like search or code execution) during inference to generate smarter replies <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. These tool calls necessitate [[AI sandbox security | secure]] execution environments <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Beyond inference, [[building_and_improving_ai_agents | AI sandboxes]] are essential for:
*   **Reinforcement Learning (RL)**: Running reward functions at scale during the training phase <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Enhanced Agent Capabilities**: A full Linux sandbox allows agents to perform advanced tasks. For instance, during code generation, agents can debug entire applications using Linux commands like `ps` or `lsof` to monitor execution and fix issues <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This enables agents to backtrack, replan, and work towards a goal effectively <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **[[AI sandbox security | Security]]**: Agent-generated code is akin to running untrusted code from sources like GitHub or Stack Overflow <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Such code can be buggy or malicious, potentially gaining root access and compromising user or client data <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. Sandboxes provide the necessary isolation and lockdown <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Examples like Manas AI demonstrate how a sandbox enables complex tasks without extensive prompting or frameworks, leveraging the agent's pre-training Linux knowledge <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a> <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Introducing Arachis

Arachis is an open-source solution designed to spawn and manage [[AI sandboxes | AI sandboxes]] for code execution and computer use <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. It offers:
*   **Security**: Built with [[microvms_in_ai_sandboxes | MicroVMs]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Customization**: Fully customizable <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Self-hosting**: Can be self-hosted <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **Backtracking**: Supports [[snapshotting_in_ai_sandboxes | snapshot]] and restore for agents to backtrack <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Speed**: Boots in less than 7 seconds, with ongoing efforts to reduce this to under 1 second <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a> <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Port Forwarding**: Handles port forwarding for easy access to code execution or browser use via public URLs <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
*   **Computer Use**: Pre-installed Chrome and VNC server for GUI access <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **API**: A dead simple, ubiquitous API with Python, Golang clients, and OpenAPI compatibility <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Configurability**: Leverages Docker tooling for customizing binaries and packages within the sandbox <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

## Core Components of an AI Sandbox (as exemplified by Arachis)

### 1. [[microvms_in_ai_sandboxes | MicroVM-Based Secure Code Execution]]

[[AI sandbox security | Security]] is paramount for [[AI sandboxes | AI sandboxes]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Arachis uses [[microvms_in_ai_sandboxes | MicroVMs]] as its runtime environment <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

#### Understanding Linux Sandboxing Options:
*   **Linux Execution Model**: Threads are the smallest unit of execution, processes are logical constructs of multiple threads sharing resources. The kernel provides privileged access to hardware via system calls <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   **Containers**: Package an app's dependencies with its logic, enabling arbitrary user code execution <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. On Linux, containers are collections of namespaces (e.g., process, mount, net) that abstract resources, giving a bound view to the container <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Cgroups control resource access (CPU, memory) <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   **Container Security Flaw**: Containers run as native processes on the kernel <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. A kernel vulnerability can allow malicious processes to gain root access, compromising the host <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
    *   **Mitigation (Jailing)**: Reducing the attack surface by restricting Linux capabilities (caps) and system calls using techniques like `seccomp` filters. Libraries like `minijail` assist in this <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. However, jailing has limits and can still be bypassed <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Virtualization (VMs)**: Provide stronger isolation by running a guest user space and guest kernel separate from the host kernel <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. This significantly reduces the attack surface compared to containers <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
    *   **Linux Virtualization**: A Virtual Machine Monitor (VMM) process (e.g., QEMU, CrossVM, Firecracker) interacts with `dev/kvm`, a Linux kernel device exposing the processor's virtualization stack <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. When a VM needs host resources (disk, net), it "VM exits" to the VMM, which then communicates with the host kernel and returns the response with a "VM resume" <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. Frequent VM exits can impact performance <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.
*   **[[microvms_in_ai_sandboxes | MicroVMs]]**: A lighter-weight, security-first approach to VMs <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
    *   **Security**: Often written in memory-safe languages like Rust (e.g., CrossVM) to prevent memory-related bugs in emulated devices <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. They also jail emulated devices separately, limiting the scope of compromise <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   **"Micro"**: Refers to the smaller VMM process <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. They support fewer architectures and only major emulated devices, leading to less code, faster boot times, and lower memory consumption <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.
    *   **Arachis's Choice**: Arachis opts for [[microvms_in_ai_sandboxes | MicroVMs]] (specifically Cloud Hypervisor) due to their enhanced security, fast boot times, and support for features like [[snapshotting_in_ai_sandboxes | snapshotting]], hot-plugging devices, and GPU support <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a> <a class="yt-timestamp" data-t="00:22:42">[00:22:42]</a>. This choice addresses the need for multi-tenant untrusted code execution without compromising data <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

### 2. Storage and File System

Sandboxes need to create, read, and write files, but the root file system (root FS) must be protected from deletion or corruption by buggy or malicious code <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.
*   **OverlayFS**: Arachis uses a shared, read-only base layer (root FS) across sandboxes <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. On top of this, each sandbox gets its own read-write layer where new files are created <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
*   **Snapshotting**: When a sandbox is [[snapshotting_in_ai_sandboxes | snapshotted]], only the read-write layer is persisted, optimizing storage and sharing <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>. The sandbox itself sees a regular Linux file system, with the OverlayFS magic handled underneath <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.

### 3. Networking

Each sandbox requires networking for external actions or tool calls <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **Isolated Networking**: Every Arachis sandbox runs in a [[microvms_in_ai_sandboxes | virtual machine]] with its own isolated networking setup <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>.
*   **Tap Device**: Each sandbox receives a unique virtual networking interface called a "tap device" <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Linux Bridge**: All tap devices connect to a Linux bridge on the host server <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
*   **Port Forwarding**: Arachis handles port forwarding from the host to the sandbox's code server or VNC server, eliminating the need for manual IP tables or firewall configurations <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### 4. Customization with Docker Tooling

Arachis allows full control over the sandbox environment.
*   **Docker Files**: Users can use their existing Docker commands and modify a Dockerfile to customize which binaries and packages are installed in the sandbox <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.
*   **Pre-installed Tools**: Default sandboxes include standard packages, Chrome (booted via systemd), NodeJS, npm, and Python to make agents productive out-of-the-box <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>.

### 5. Code Execution Server

[[Building AI sandboxes | AI sandboxes]] bundle a code execution server <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.
*   **Files API**: Allows uploading and downloading files to and from the sandbox <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>.
*   **Command API**: Executes commands within the sandbox and returns output or errors in JSON format <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.
*   **Security**: Running this server within a [[microvms_in_ai_sandboxes | guest VM]] provides confidence against escapes, unlike running it directly on the host <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.
*   **Browser Access**: Chrome is pre-installed, and port forwarding to the VNC server allows direct GUI access <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

### 6. [[snapshotting_in_ai_sandboxes | Snapshotting]] and Restore

[[snapshotting_in_ai_sandboxes | Snapshotting]] is a crucial feature for agent reliability, especially for multi-step workflows <a class="yt-timestamp" data-t="00:32:26">[00:32:26]</a>.
*   **Motivation**: Agents often fail during complex, multi-stage tasks <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>. [[snapshotting_in_ai_sandboxes | Snapshotting]] allows agents to backtrack to a last good checkpoint, replan, and retry without starting from scratch <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>. This enables more reliable execution of higher-order complex tasks and parallel exploration of paths <a class="yt-timestamp" data-t="00:33:23">[00:33:23]</a>.
*   **Functionality**: Arachis saves the entire running state of a sandbox, including guest memory and the read-write part of the OverlayFS (created files, spawned processes, open windows) <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
*   **Process**: [[snapshotting_in_ai_sandboxes | Snapshotting]] involves four steps <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>:
    1.  Pause the VM via the VMM's pause API <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>.
    2.  Call the snapshot API to dump guest memory <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
    3.  Manually persist the read-write OverlayFS layer (thin disk) <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>.
    4.  Resume the VMM to continue execution <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.
*   **Future Work**: Plans to move to `btrfs` for native support of incremental snapshots <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

## High-Level Architecture of Arachis

The Arachis architecture features a REST server that spawns and manages [[microvms_in_ai_sandboxes | MicroVM]] sandboxes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Each sandbox runs a VNC server and a code server, with port forwarding handled to expose these services <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Clients interact via a Golang CLI (Arachis CLI), a Python SDK, or an MCP server, using an OpenAPI compatible YAML file for client generation in any language <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a> <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. The system is tied to Linux due to its reliance on `dev/kvm`, the Linux virtualization device <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Using the Arachis API

Arachis provides a simple API <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>:
*   **VM Management**: A `/vms` resource to start, stop, or delete VMs <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **[[snapshotting_in_ai_sandboxes | Snapshots]]**: A `/snapshots` resource within a VM to snapshot <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Command Execution**: A `/command` resource for executing commands <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **File Management**: A `/files` API to upload and download files <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Health Check**: A `/health` endpoint for monitoring the REST server <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

The Python SDK simplifies usage, allowing users to start sandboxes, run commands, create [[snapshotting_in_ai_sandboxes | snapshots]], and restore checkpoints with straightforward API calls <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.

## Demo: Google Docs Clone

A demonstration showcased Claude Desktop creating a Google Docs clone using Arachis via its MCP server <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>.
*   Claude piped commands into the Linux sandbox to build the collaborative app <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>.
*   [[snapshotting_in_ai_sandboxes | A snapshot]] of the initial version was taken <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   A dark mode feature was added, demonstrating the agent's ability to modify the application <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.
*   The sandbox was then restored to the previous [[snapshotting_in_ai_sandboxes | snapshot]] without the dark mode, illustrating the backtracking capability <a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>.
This demo highlighted the ability to build end-to-end applications and achieve truly collaborative experiences, unlike client-side code generation tools <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>.

## Ongoing Work

Arachis development focuses on:
*   **Boot Time Reduction**: Aiming for boot times under 1 second <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.
*   **Improved Snapshotting**: Moving to `btrfs` for better support for incremental snapshots and persistence <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.
*   **Dynamic Resource Management**: Implementing dynamic memory management, ballooning, or hot-plugging/removal of memory at runtime to pack more sandboxes onto a single server <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>.