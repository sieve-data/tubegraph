---
title: MicroVMs in AI sandboxes
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

MicroVMs are a core technology behind modern AI sandboxing solutions like Arachis, an open-source code execution and computer use sandboxing service for AI agents <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. They provide a secure, fast, and efficient environment for running untrusted AI-generated code <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Why AI Sandboxes Need MicroVMs

AI models, particularly those using tool calling for inference, require sandboxes for executing tools like search or code execution <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. For reinforcement learning, sandboxes are crucial during the training phase to run reward functions at scale <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

A key driver for using MicroVMs is security <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. AI-generated code, like any code from untrusted sources, could be buggy or malicious <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Without proper isolation, such code could gain root access, compromise data, or affect the host system <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. MicroVMs address this by providing a highly isolated execution environment <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Furthermore, MicroVMs offer:
*   **Speed** Fast boot times are paramount for AI sandboxes <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Arachis, leveraging MicroVMs, can boot in less than 7 seconds, with ongoing efforts to reduce this to under a second <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Backtracking and [[snapshotting_in_ai_sandboxes | Snapshotting]]** MicroVMs enable quick [[snapshotting_in_ai_sandboxes | snapshotting]] and restoration of the sandbox's state <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This allows AI agents to checkpoint progress, backtrack if multi-step workflows fail, replan, and continue without starting from scratch <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Full Linux Sandbox Capability** Agents benefit from a full Linux sandbox, allowing them to use commands like `ps` or `lsof` to debug applications during code generation, backtrack, and replan <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Understanding MicroVMs and Linux Sandboxing

To grasp MicroVMs, it's helpful to understand the evolution of Linux sandboxing:

### Linux Execution Model
A thread is the smallest unit of execution on Linux, represented by a `task_struct` in the kernel's scheduler run queue <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. A process is a logical construct of multiple threads, sharing resources like page tables <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. The kernel provides privileged access to hardware, requiring system calls to switch to kernel or supervisor mode for privileged operations <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Containers
From a programmer's perspective, containers package an application's dependencies with its core logic, allowing arbitrary user code to run <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. Technically, a container is a collection of namespaces (e.g., process, mount, network) <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. A container sees an abstracted view of its own resources, with the host able to see inside but the container unable to see its host's namespace <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Control groups (cgroups) are used with namespaces to manage resource allocation (e.g., CPU, memory) for containers <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

**Security Limitations of Containers:**
Containers run as native processes directly on top of the host kernel <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This means a kernel vulnerability can be exploited by a malicious or buggy process within a container to gain root access on the host, allowing data access or other malicious actions <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

### Virtualization
Virtualization offers a stronger primitive for running untrusted code <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Each Virtual Machine (VM) has its own guest user space and guest kernel, providing isolation unlike containers where processes run directly on the host kernel <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>. This significantly reduces the attack surface to the host kernel <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

On Linux, virtualization relies on `/dev/kvm`, a device in the Linux kernel that exposes the processor's virtualization stack <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. A Virtual Machine Monitor (VMM), such as QEMU, CrossVM, or Firecracker, sits on top of `/dev/kvm` to spawn and manage VMs <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. When a guest VM needs to access host resources (e.g., disk, network), it "exits" to the host, triggering a VM exit to the VMM process. The VMM then interacts with the host kernel and sends the response back to the guest with a VM resume <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. Minimizing these VM exits is crucial for performance <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.

### MicroVMs vs. Traditional VMs
MicroVMs differ from traditional VMs in several key ways:
*   **Security-First Design** MicroVMs, pioneered by projects like CrossVM (the first Rust-based VMM) <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>, are often written in memory-safe languages like Rust to prevent memory-related bugs that untrusted guest code could exploit to attack host devices <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. They also implement stricter jailing architectures, isolating emulated devices (like block and network) into separate processes or with limited capabilities to reduce cross-device attack surfaces <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **"Micro" for Speed and Memory** The "micro" in MicroVM refers to the VMM process itself <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. Unlike old VMMs that support many architectures and devices, MicroVMs (e.g., CrossVM, Firecracker, Cloud Hypervisor) support only one or two common architectures (Intel, ARM) and major devices <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This drastically reduces code paths at boot and runtime, leading to blazing-fast boot times and lower memory consumption <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

Arachis specifically uses Cloud Hypervisor as its MicroVM VMM <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Cloud Hypervisor was chosen for its hot-plugging support (adding/removing RAM at runtime), GPU support, [[snapshotting_in_ai_sandboxes | snapshot]] support, and its open-source, non-company-specific control <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>.

While G Visor is another option, offering better security than containers but less than MicroVMs, and easier GPU access, MicroVMs were chosen for Arachis due to their strong security guarantees, especially for multi-tenant untrusted code execution <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Architecture of MicroVM-based Sandboxes

In Arachis, a REST server manages the MicroVM-based sandboxes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Each sandbox runs a VNC server for GUI access and a code server for execution <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### File System
Sandboxes employ an overlay file system setup <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. A shared, read-only base layer (root FS) is protected and shared among sandboxes <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. On top of this, each sandbox gets its own read-write layer where new files are created <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>. When a sandbox is [[snapshotting_in_ai_sandboxes | snapshotting]], only this read-write layer needs to be persisted <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

### Networking
Each sandbox has isolated networking through a unique virtual networking interface called a tap device <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>. These tap devices connect to a Linux bridge on the host server <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>. Arachis handles port forwarding from the host to the sandbox's code server or VNC server, simplifying external access <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### [[snapshotting_in_ai_sandboxes | Snapshotting]] Process
Arachis's [[snapshotting_in_ai_sandboxes | snapshotting]] allows agents to save the entire running state of a sandbox, including guest memory and the read-write file system layer <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This ensures that any processes, open windows, or files created are restored exactly as they were <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>. The process involves:
1.  Pausing the VM <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>.
2.  Dumping the guest memory using the VMM's snapshot API <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
3.  Manually persisting the read-write overlay FS layer <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>.
4.  Resuming the VM <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.

Future work on [[snapshotting_in_ai_sandboxes | snapshotting]] includes moving to Btrfs for optimized incremental snapshots <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.

## Conclusion
MicroVMs provide a robust foundation for [[building_ai_sandboxes | building AI sandboxes]] due to their strong security guarantees, fast boot times, and efficient [[snapshotting_in_ai_sandboxes | snapshotting]] capabilities. This allows AI agents to perform complex, multi-step workflows with reliable backtracking and recovery <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Ongoing work in Arachis aims to achieve sub-second boot times and advanced [[memory_management_in_ai | memory management]] for greater efficiency <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.