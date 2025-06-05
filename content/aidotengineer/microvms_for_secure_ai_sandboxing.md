---
title: MicroVMs for secure AI sandboxing
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

Arachis, an open-source code execution and computer use sandboxing service for [[personal_local_and_private_ai_agents | AI agents]], utilizes microVMs as its core technology to provide secure and customizable sandboxes for AI workloads <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach addresses the critical need for isolated environments when running untrusted or potentially malicious AI-generated code <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Why AI Sandboxes Are Essential
The latest AI models, such as GPT-3, increasingly leverage tool calling (e.g., search or code execution) during inference to provide more intelligent replies <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. These tool calls necessitate [[MicroVMs for secure AI sandboxing | AI sandboxes]] for their execution <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

Key use cases and benefits include:
*   **Reinforcement Learning (RL)**: Sandboxes are crucial during the training phase to run reward functions at scale <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Enhanced Agent Capabilities**: A full [[linux_virtualization_and_container_security | Linux sandbox]] empowers agents, allowing them to debug entire applications using [[linux_virtualization_and_container_security | Linux commands]] like `ps` or `lsof` during code generation <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This enables agents to backtrack, replan, and work towards goals effectively <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Security**: Running AI-generated code, which can be buggy or malicious, directly on a host or production server poses significant risks, including potential root access or data breaches <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Sandboxes provide the necessary isolation <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Examples like Manas AI demonstrate how a sandbox enables complex code generation tasks without extensive prompting or alignment frameworks, leveraging the AI's pre-training knowledge of [[linux_virtualization_and_container_security | Linux]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Introducing Arachis
Arachis offers a secure, fully customizable, and self-hosted solution for spawning and managing [[MicroVMs for secure AI sandboxing | AI sandboxes]] for code execution and computer use <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Key Features
*   **MicroVM-based Secure Code Execution**: Utilizes microVMs as a runtime to protect data and systems from potentially malicious or buggy AI-generated code <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Speed**: Arachis boots sandboxes in less than 7 seconds, significantly faster than traditional VMs, with ongoing efforts to reduce this to under a second <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. [[snapshotting_in_ai_sandboxes | Snapshots]] are also very fast, in single-digit seconds <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Port Forwarding**: Automatically handles port forwarding, allowing easy access to code execution environments or browser use via public URLs <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Easy Computer Use**: Chrome is pre-installed with a VNC server, enabling easy access to the browser GUI within the sandbox <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **[[snapshotting_in_ai_sandboxes | Backtracking]] (Snapshot and Restore)**: Agents can checkpoint their progress by [[snapshotting_in_ai_sandboxes | snapshotting]] the sandbox. If multi-step workflows fail, they can restore an older snapshot, leading to more reliable and complex task execution <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Ubiquitous API**: Provides Python and Golang clients, an MCP server, and an Open API compatible YAML file for generating clients in any language <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Configurable with Docker Tooling**: Users can customize binaries and packages installed in the sandbox using existing Docker commands and Dockerfiles <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### High-Level Architecture
Arachis features a REST server that spawns and manages microVM sandboxes <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Each sandbox runs a VNC server and a code server, exposed via port forwarding <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The system is tied to [[linux_virtualization_and_container_security | Linux]] due to its reliance on `/dev/kvm`, the [[linux_virtualization_and_container_security | Linux virtualization]] device <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

The API exposes resources for managing VMs (start, stop, delete), snapshots (snapshot, restore), command execution, file upload/download, and health checks <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Understanding Linux Sandboxing
To grasp why microVMs are chosen for [[MicroVMs for secure AI sandboxing | AI sandboxes]], it's helpful to understand different [[linux_virtualization_and_container_security | Linux sandboxing]] options.

### Linux Execution Model
On [[linux_virtualization_and_container_security | Linux]], a thread is the smallest unit of execution, represented by a `task_struct` in the kernel <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. A process is a logical construct of multiple threads that share page tables and other resources <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. The kernel provides privileged access to hardware, requiring system calls to switch to kernel or supervisor mode <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Containers
Containers solve the problem of packaging an application's dependencies with its core logic, enabling arbitrary user code to run on a machine <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. On [[linux_virtualization_and_container_security | Linux]], a container is a collection of [[linux_virtualization_and_container_security | namespaces]] (e.g., process, mount, network) that abstract resources, giving the container an isolated view of its environment <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Cgroups are used alongside [[linux_virtualization_and_container_security | namespaces]] to control resource access (CPU, memory) for a container <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

#### Security Story of Containers
Containers run as native processes directly on the host kernel <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This means a kernel vulnerability can be exploited by a malicious or buggy process within the container, allowing it to gain root access and compromise the host <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

#### Container Security Mitigation
To mitigate these risks, techniques like jailing containers by restricting [[linux_virtualization_and_container_security | Linux capabilities]] and system calls are used to reduce the attack surface <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>. `seccomp` filters can also block or filter arguments to system calls <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. However, even with these measures, sandboxing has limits and can sometimes be bypassed <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

## Transition to Virtualization
When stronger isolation is needed, virtualization provides a more robust primitive for running untrusted code <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Each Virtual Machine (VM) has its own guest user space and guest kernel, offering a smaller attack surface to the host kernel compared to containers <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

### Linux Virtualization Explained
In [[linux_virtualization_and_container_security | Linux virtualization]], a Virtual Machine Monitor (VMM), such as QEMU, CrossVM, or Firecracker, manages the VMs <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. The VMM interacts with `/dev/kvm`, a [[linux_virtualization_and_container_security | Linux]] kernel device that exposes the processor's virtualization stack, to start VMs and grant access to privileged resources <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

When a guest VM needs to access host resources (disk, network), it triggers a "VM exit" to the host. The VMM handles this exit, interacts with the host kernel for the resource, and then sends the response back to the guest with a "VM resume" <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. Minimizing VM exits and resumes is crucial for performance <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>. While VMs offer superior security, performance might be affected in I/O-heavy loads due to these exits, unlike native processes in containers <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.

## MicroVMs vs. Traditional VMs
MicroVMs represent a refined approach to virtualization, offering enhanced security and performance compared to traditional VMs like QEMU <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

### Key Differentiators:
*   **Rust-based Implementation**: Projects like CrossVM pioneered writing VMMs in Rust, which provides memory safety, mitigating vulnerabilities that could allow untrusted guest code to attack host devices written in less memory-safe languages like C <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
*   **Jailed Emulated Devices**: MicroVMs typically jail their emulated devices separately. For example, a block device is restricted to only block-related system calls, preventing a compromise in one device from affecting others <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **"Micro" Aspect (Speed and Memory)**: The "micro" in microVMs refers to the VMM process itself <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>. Unlike older VMMs that support numerous architectures and obscure devices, microVMs (e.g., Firecracker, Cloud Hypervisor) support a limited set (Intel, ARM) and only major devices <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. This reduced codebase leads to blazing fast boot times and lower memory consumption at runtime <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.

MicroVMs like Firecracker (underpinning AWS Lambda) and Cloud Hypervisor (a more general-purpose [[enterprise_ai_deployment_within_security_boundaries | enterprise VM]]) stemmed from the CrossVM revolution <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. Arachis selected Cloud Hypervisor for its hot-plugging device support, GPU support, existing [[snapshotting_in_ai_sandboxes | snapshot]] capabilities, and its community-driven project model <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. G Visor, another option, offers a middle ground between containers and microVMs in terms of performance and security, and provides easier GPU access <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

## Arachis's MicroVM-Powered Architecture
Arachis explicitly chooses a microVM runtime for its [[MicroVMs for secure AI sandboxing | AI sandboxes]] primarily due to security requirements for multi-tenant code execution, where untrusted AI-generated code might access different clients' data <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. The fast boot times and ease of [[snapshotting_in_ai_sandboxes | snapshotting]] by simply dumping guest memory are also critical factors <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>.

### File System Management
Arachis protects the sandbox's root file system by using an overlay FS <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.
*   A read-only base layer is shared among sandboxes <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
*   Each sandbox receives its own read-write layer where all new files are created <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>.
*   When [[snapshotting_in_ai_sandboxes | snapshotting]], only this read-write layer is persisted, optimizing storage and backup <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
This setup is handled during the sandbox's boot process, making it appear as a regular [[linux_virtualization_and_container_security | Linux]] file system to processes inside <a class="yt-timestamp" data-t="00:25:59">[00:25:59]</a>.

### Networking Setup
Each Arachis sandbox, running as a virtual machine, has its own isolated networking setup <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>.
*   A unique `tap` device (virtual networking interface) is created for each sandbox <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
*   All `tap` devices connect to a [[linux_virtualization_and_container_security | Linux bridge]] on the host server <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.
*   Arachis automatically handles port forwarding, utilizing [[linux_virtualization_and_container_security | Linux IP tables]] to direct traffic between the host and the sandbox's code server or VNC server <a class="yt-timestamp" data-t="00:27:44">[00:27:44]</a>.

### Customization and Built-in Tools
Arachis allows customization of binaries and packages within the sandbox via a Dockerfile <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>. The default setup includes Ubuntu 22.04, standard packages, Chrome (booted via systemd), NodeJS, npm, and Python, providing a rich environment for AI agents <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>.

### Code Execution and GUI Access
Arachis bundles a code execution server within the sandbox <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>. This server provides a `files` API for uploading/downloading files and a `command` API for executing commands and returning JSON output/errors <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>. Running this server inside a secure microVM means high confidence that code won't escape to the host OS <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>. Chrome is pre-installed, and port forwarding facilitates direct GUI access via a VNC server <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

### [[snapshotting_in_ai_sandboxes | Snapshotting]] in Arachis
[[snapshotting_in_ai_sandboxes | Snapshotting]] is a critical feature enabling agents to backtrack and replan during complex, multi-step tasks <a class="yt-timestamp" data-t="00:33:09">[00:33:09]</a>. If an agent fails deep into a workflow, it can restore to a last known good checkpoint instead of starting from scratch <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.

Arachis saves the entire running state of a sandbox, including guest memory and the read-write overlay FS layer <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This means all created files, spawned processes, and even open GUI windows are restored exactly as they were <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

The [[snapshotting_in_ai_sandboxes | snapshot]] process involves four steps:
1.  Pause the VM <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>.
2.  Call the snapshot API to dump guest memory <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
3.  Manually persist the read-write overlay FS layer <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>.
4.  Resume the VM <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.
Future work includes migrating to `btrfs` for native incremental snapshot awareness <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>.

## Using the Arachis API
Arachis offers a user-friendly API, including a Python SDK <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>. Users can self-host Arachis, start sandboxes, run commands, upload/download files, create [[snapshotting_in_ai_sandboxes | snapshots]] with a simple ID, and restore VMs from these checkpoints <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.

## Demo: Google Docs Clone with [[snapshotting_in_ai_sandboxes | Backtracking]]
A demonstration showcased Claude Desktop creating a collaborative Google Docs clone using Arachis's MCP server <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>. Without extensive prompting, Claude piped commands into the [[linux_virtualization_and_container_security | Linux sandbox]] to build the application <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. The demo highlighted:
*   Real-time collaboration enabled by Arachis's networking setup <a class="yt-timestamp" data-t="00:38:47">[00:38:47]</a>.
*   [[snapshotting_in_ai_sandboxes | Snapshotting]] the current state of the application <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
*   Adding a new feature (dark mode) and verifying its functionality <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.
*   Restoring to the previous snapshot, effectively undoing the dark mode addition, demonstrating the power of [[snapshotting_in_ai_sandboxes | backtracking]] <a class="yt-timestamp" data-t="00:38:20">[00:38:20]</a>.

## Ongoing Work
Current development efforts for Arachis focus on:
*   Achieving sub-1-second boot times <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.
*   Enhancing [[snapshotting_in_ai_sandboxes | snapshot]] and persistence support, including a move to `btrfs` for incremental snapshots <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.
*   Optimizing for bin-packing many sandboxes on a single server through dynamic memory and resource management (e.g., memory ballooning or hot-plugging) <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>.