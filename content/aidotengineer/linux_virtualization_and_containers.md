---
title: Linux virtualization and containers
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

This article explores the fundamental concepts of Linux execution, containers, and virtualization, focusing on how they provide sandboxing environments, particularly for [[AI agents]].

## Linux Execution Model

On Linux, the smallest unit of execution is a thread, each represented by a `task_struct` in the kernel's scheduler run queue [00:08:21]. A process is a logical construct composed of multiple threads that share page tables and other resources [00:08:42]. The kernel grants privileged access to hardware, requiring special instructions or system calls to switch to kernel or supervisor mode for privileged operations [00:08:56]. This mechanism prevents buggy or malicious code from crashing devices or performing harmful actions [00:09:01].

## Containers

[[Docker for AI Workshops | Containers]] are a solution for packaging an application's dependencies along with its core logic, allowing it to run on various servers without needing specific software versions or libraries on the host [00:10:13]. From a programmer's perspective, they enable the execution of arbitrary user code on a machine, which is a core requirement for an [[AI sandbox]] [00:10:24].

### Technical Definition
Technically, a container on Linux is a collection of namespaces that abstract different resources, such as process IDs, mount points, and network configurations [00:10:32]. For example, within a container's process namespace, it might see processes as PID 1, 2, and 3, while outside in the root namespace, these are arbitrary processes [00:10:47]. A container has an abstracted or bound view of its own resources [00:11:02]. While the host can inspect a child container's namespace, the container cannot look up into its host namespace [00:11:08]. [[Docker for AI Workshops | Cgroups]] are used in tandem with namespaces to control resource allocation, such as CPU and memory percentages, for a specific container [00:11:41].

### Security Story of Containers
Containers run as native processes directly on top of the host kernel [00:12:20]. This means that if a kernel vulnerability exists, a malicious or buggy process within a container can attack the kernel, gain root access, and compromise the entire system, potentially accessing sensitive data [00:12:33].

### Jailing Containers
To reduce the attack surface and mitigate risks, containers can be "jailed" by restricting Linux capabilities and system calls [00:13:19].
*   **Capabilities (Caps)**: Linux capabilities govern which privileged operations a process can perform [00:13:40]. By only granting the necessary capabilities for a container to function, the attack surface is reduced [00:13:48].
*   **Seccomp**: Seccomp (secure computing mode) filters the arguments passed to system calls or can block system calls entirely [00:14:04].
*   **Mini Jail**: These APIs can be complex and hard to use due to granular error checking [00:14:14]. Libraries like Mini Jail, used in Chrome OS, assist in jailing and sandboxing containers and processes [00:14:19].

Despite these measures, sandboxing and jails have limits and can still be bypassed [00:14:31].

## Virtualization on Linux

Virtualization offers a stronger primitive for running untrusted or arbitrary code [00:14:47]. Unlike containers, where processes run directly on the host kernel, each Virtual Machine (VM) has its own isolated guest user space and guest kernel [00:14:55]. This isolation significantly reduces the attack surface to the host kernel [00:15:10].

### How VMs Access Host Resources
The process responsible for managing VMs is called the Virtual Machine Monitor (VMM), examples include QEMU, CrossVM, and Firecracker [00:15:47]. The VMM interacts with `/dev/kvm`, a device in the Linux kernel that exposes the processor's virtualization stack [00:16:01].
*   **VMM Functions**: The VMM spawns VMs and manages emulated devices like block and network devices [00:16:23].
*   **Guest Code Execution**: Guest code runs in a separate virtualization context on the processor [00:16:49].
*   **VM Exits and Resumes**: When the VM needs to access host resources (e.g., disk, network), it triggers a "VM exit" back to the host [00:16:56]. The VMM then handles the request with the host kernel and sends the response back to the guest with a "VM resume" [00:17:13].
*   **Performance Trade-offs**: Frequent VM exits and resumes can impact performance [00:17:25]. CPU-bound tasks within the guest incur minimal penalty as they run directly on the processor, but I/O-bound tasks may experience overhead due to frequent exits [00:17:37]. This contrasts with containers, which run as native processes and generally have better performance but offer less security [00:18:02].

## MicroVMs

[[MicroVMs in AI sandboxes | MicroVMs]] are a distinct evolution in virtualization, differing from traditional VMs in several key aspects [00:18:32].

### Key Characteristics
*   **Rust-based VMMs**: The concept originated with the CrossVM project at Chrome OS, which was the first Rust-based VMM [00:18:38]. Writing VMMs in Rust provides memory safety, addressing potential memory-related bugs in C-written devices that untrusted guest code could exploit to attack the host [00:18:52].
*   **Jailed Emulated Devices**: [[MicroVMs in AI sandboxes | MicroVMs]] often jail their emulated devices separately. For instance, a block device would only have access to block-related system calls, preventing compromise from extending to network resources, and vice-versa [00:19:14].
*   **"Micro" Reflection**: The "micro" in [[MicroVMs in AI sandboxes | MicroVMs]] refers to the VMM process itself (e.g., CrossVM, Firecracker, Cloud Hypervisor), not what runs inside the guest [00:20:26].
*   **Faster Boot Times and Less Memory**: Traditional VMMs like QEMU support many architectures and emulated devices, leading to larger codebases [00:19:54]. [[MicroVMs in AI sandboxes | MicroVMs]] typically support only one or two major architectures (Intel, ARM) and essential devices [00:20:07]. This streamlined approach means less code and fewer code paths at boot, resulting in blazing fast boot times and reduced runtime memory consumption [00:20:17].

### Examples of MicroVMs
*   **CrossVM**: Initiated the [[MicroVMs in AI sandboxes | MicroVM]] revolution [00:22:11].
*   **Firecracker**: A [[MicroVMs in AI sandboxes | MicroVM]] forked from CrossVM, it underpins AWS Lambda for [[luminal_cloud_and_serverless_inference | serverless loads]] [00:22:26]. It features a fleshed-out REST API and a better jailing architecture [00:22:35].
*   **Cloud Hypervisor**: Another [[MicroVMs in AI sandboxes | MicroVM]] forked from CrossVM, it's a more general-purpose enterprise VMM [00:22:40]. It offers hot-plugging of devices (adding/removing RAM at runtime), [[gpu_and_server_configurations_for_ai | GPU support]], and snapshot support [00:22:44]. Its independent control, not tied to a single company, makes it a sensible choice [00:22:59].

### Comparison with GVisor
GVisor is another sandboxing option [00:23:12]. It performs closer to a container in terms of performance but offers slightly better security [00:23:16]. However, untrusted code can still attack the host kernel when running in GVisor [00:23:22]. GVisor and containers generally provide easier [[gpu_and_server_configurations_for_ai | GPU access]] compared to [[MicroVMs in AI sandboxes | MicroVMs]] [00:23:31].

## Arachis: An AI Sandbox using MicroVMs

Arachis, an open-source code execution and computer use sandboxing service for [[AI agents]], leverages a [[MicroVMs in AI sandboxes | MicroVM]] runtime as its execution environment [00:00:04, 00:20:54].

### Why Arachis Chose MicroVMs
*   **Security**: A key design choice due to [[AI agents]] generating code in multi-tenant environments where untrusted code could access client data [00:21:02]. [[MicroVMs in AI sandboxes | MicroVMs]] prevent untrusted code from gaining root access to the server [00:21:23].
*   **Fast Boot Times**: As discussed, [[MicroVMs in AI sandboxes | MicroVMs]] boot significantly faster than traditional VMs [00:21:40]. Arachis currently boots in under 7 seconds, with a goal to achieve less than 1 second [00:03:55, 00:04:02].
*   **Snapshotting and Persistence**: [[MicroVMs in AI sandboxes | MicroVMs]] facilitate fast snapshotting by dumping the entire guest memory [00:21:43]. This allows [[AI agents]] to checkpoint progress and restore old snapshots if multi-step workflows fail, enabling backtracking and more reliable, complex task execution [00:02:53, 00:04:48, 00:33:01]. Snapshotting takes single-digit seconds [00:04:08]. Arachis plans to move to Btrfs for incremental snapshots [00:39:27].

### Arachis Architecture and Features
*   **REST Server**: Manages and spawns [[MicroVMs in AI sandboxes | MicroVM]] sandboxes [00:05:42].
*   **Components per Sandbox**: Each sandbox runs a VNC server and a code server [00:05:47].
*   **Port Forwarding**: Arachis handles port forwarding, allowing easy access to code execution or browser use via a public URL [00:04:14].
*   **Computer Use Workflows**: Chrome and a VNC server are pre-installed, enabling easy GUI access for browser-based tasks [00:04:31].
*   **API**: Arachis provides a simple, ubiquitous API with Python and Golang clients, and an OpenAPI compatible YAML file for client generation in any language [00:05:10, 00:05:16]. It includes resources for managing VMs (start, stop, delete), snapshots, command execution, and file transfer [00:06:46].
*   **Configurability**: Sandboxes can be customized using [[Docker for AI Workshops | Docker]] tooling and Dockerfiles to install specific binaries and packages [00:05:24, 00:29:29].
*   **Linux Dependence**: Arachis is tied to Linux because the underlying [[MicroVMs in AI sandboxes | MicroVM]] technology relies on `/dev/kvm`, the Linux virtualization device [00:06:19].

### Storage and File System
To protect the root file system (rootfs) from malicious or buggy code, Arachis implements an overlay file system [00:24:58].
*   **Shared Read-Only Layer**: A shared base layer of the rootfs is read-only and shared across sandboxes [00:25:03].
*   **Per-Sandbox Read-Write Layer**: Each sandbox receives its own read-write layer where new files are created [00:25:14].
*   **Snapshotting**: When a sandbox is snapshotted, only the read-write layer is persisted, providing efficient storage and restoration [00:25:31]. The setup occurs via an `init.script` inside the guest, mounting the overlay FS before PID 1 boots [00:26:12].

### Networking
Every sandbox requires networking for external communication and tool calls [00:27:00].
*   **Isolated Networking**: Each sandbox runs with its own isolated virtual networking [00:27:15].
*   **Tap Device**: Each sandbox gets a unique virtual network interface called a tap device [00:27:19].
*   **Linux Bridge**: All tap devices connect to a Linux bridge on the host server [00:27:33].
*   **Automatic Port Forwarding**: Arachis automatically forwards ports from the host to the VNC or code servers inside the sandbox, using Linux `iptables` commands [00:27:44, 00:28:46].

### Code Execution and GUI Access
Arachis bundles a code execution server, exposing APIs for uploading/downloading files and executing commands within the sandbox [00:31:19]. This allows [[AI agents]] to run commands and debug applications using standard Linux commands (e.g., `ps`, `lsof`) [00:01:28]. Running this server within a secure guest VM increases confidence in its safety compared to running directly on the host OS [00:31:51]. With Chrome pre-installed and VNC server forwarding, users can directly access the browser GUI inside the sandbox [00:32:06].

### Snapshotting for Agent Reliability
Snapshotting is crucial for [[AI agents]] to improve reliability in multi-step workflows [00:33:01].
*   **Motivation**: [[AI agents]] often fail during complex tasks [00:32:39]. Snapshotting allows them to save their state, backtrack to a last good checkpoint, replan, and retry without starting from scratch [00:33:08]. This enables exploration of multiple paths in parallel for more reliable, higher-order task execution [00:33:24].
*   **Saved State**: Arachis saves the entire running state of a sandbox, including guest memory and the read-write part of the overlay filesystem. This means processes, files, and even GUI windows are restored as they were [00:33:30].
*   **Process**: Snapshotting involves pausing the VM, calling the VMM's snapshot API to dump guest memory, manually persisting the read-write overlay FS, and then resuming the VMM [00:34:44].

### Ongoing Work
Future development for Arachis includes:
*   Achieving sub-1-second boot times [00:39:14].
*   Implementing first-class support for snapshots and persistence, potentially by moving to Btrfs for incremental snapshots [00:39:24].
*   Enabling dynamic memory and resource management (e.g., ballooning, hot-plugging/removal of memory) to pack more sandboxes onto a single server [00:39:35].