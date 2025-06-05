---
title: Building AI sandboxes from scratch
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

AI sandboxes are crucial for safely executing AI agents, enabling complex tasks, and ensuring security [00:00:09](<a class="yt-timestamp" data-t="00:00:09">00:00:09</a>). This article explores the architecture and components involved in [[building_effective_ai_agents | building effective AI agents]] within a sandbox environment, drawing insights from Arachis, an open-source code execution and computer use sandboxing service [00:00:04](<a class="yt-timestamp" data-t="00:00:04">00:00:04</a>).

## Why AI Sandboxes are Essential

Several factors drive the need for robust AI sandboxes:

*   **Tool Calling and Inference** Modern AI models, such as GPT-3, extensively use tool calling for search or code execution during inference to provide smarter replies to user queries, which necessitates sandboxes for secure execution [00:00:57](<a class="yt-timestamp" data-t="00:00:57">00:00:57</a>).
*   **Reinforcement Learning** During the training phase of reinforcement learning, sandboxes are required to run reward functions at scale [00:01:12](<a class="yt-timestamp" data-t="00:01:12">00:01:12</a>).
*   **Enhanced Agent Capabilities** A full Linux sandbox empowers agents significantly. For instance, during code generation, agents can debug entire applications using Linux commands (e.g., `ps`, `lsof`) to monitor and debug code execution. This allows them to backtrack, replan, and work towards goals effectively [00:01:21](<a class="yt-timestamp" data-t="00:01:21">00:01:21</a>).
*   **Security** Agent-generated code, similar to code from GitHub or Stack Overflow, can be buggy or malicious. Running such code directly on a host or production server risks unauthorized root access, leading to data breaches. Therefore, sandboxing is critical for locking down the execution environment [00:01:37](<a class="yt-timestamp" data-t="00:01:37">00:01:37</a>).

Examples of AI services leveraging sandboxes include OpenAI Canvas, Claude Artifacts, and Manas AI, which extensively uses a sandbox for tasks like creating a ChatGPT clone and fixing issues within the Linux environment [00:02:00](<a class="yt-timestamp" data-t="00:02:00">00:02:00</a>).

## Introducing Arachis

Arachis is an open-source solution designed to spawn and manage AI sandboxes for code execution and computer use [00:02:42](<a class="yt-timestamp" data-t="00:02:42">00:02:42</a>). Its key features include:

*   **Secure and Customizable** Provides a self-hosted solution that offers complete control over the sandbox environment [00:02:45](<a class="yt-timestamp" data-t="00:02:45">00:02:45</a>), [00:03:33](<a class="yt-timestamp" data-t="00:03:33">00:03:33</a>).
*   **[[snapshotting_in_ai_sandboxes | Snapshot and Restore]]** Supports backtracking via snapshotting, allowing agents to checkpoint progress and restore to a previous state if multi-step workflows fail. This prevents agents from starting from scratch and improves reliability for complex tasks [00:02:53](<a class="yt-timestamp" data-t="00:02:53">00:02:53</a>), [00:04:48](<a class="yt-timestamp" data-t="00:04:48">00:04:48</a>).
*   **MicroVM-based Execution** Utilizes microVMs as its runtime, prioritizing security against potentially malicious or buggy code [00:03:22](<a class="yt-timestamp" data-t="00:03:22">00:03:22</a>).
*   **Speed** Boots in less than 7 seconds, with ongoing efforts to reduce this to under 1 second. Snapshots are also very fast, completing in single-digit seconds [00:03:48](<a class="yt-timestamp" data-t="00:03:48">00:03:48</a>).
*   **Port Forwarding** Handles port forwarding automatically, exposing sandbox services like VNC or code execution via a public URL, eliminating the need for manual IP tables or firewall configurations [00:04:15](<a class="yt-timestamp" data-t="00:04:15">00:04:15</a>).
*   **Easy Computer Use** Pre-installs Chrome and a VNC server, facilitating GUI access for computer use workflows [00:04:28](<a class="yt-timestamp" data-t="00:04:28">00:04:28</a>).
*   **Ubiquitous API** Offers Python and Golang clients, an MCP server, and an OpenAPI-compatible YAML file for generating clients in any language [00:05:07](<a class="yt-timestamp" data-t="00:05:07">00:05:07</a>).
*   **Docker Tooling Integration** Allows customization of installed binaries and packages within the sandbox via a Dockerfile [00:05:23](<a class="yt-timestamp" data-t="00:05:23">00:05:23</a>).

## Architecture of an AI Sandbox

### High-Level Components

The core architecture of Arachis involves a REST server that spawns and manages microVM sandboxes [00:05:40](<a class="yt-timestamp" data-t="00:05:40">00:05:40</a>). Each sandbox runs a VNC server and a code server, with port forwarding exposing them for easy access [00:05:47](<a class="yt-timestamp" data-t="00:05:47">00:05:47</a>). The system is tied to Linux due to its reliance on `/dev/kvm`, the Linux virtualization device [00:06:17](<a class="yt-timestamp" data-t="00:06:17">00:06:17</a>).

The API of Arachis is REST-based, offering resources to start, stop, and delete VMs, manage [[snapshotting_in_ai_sandboxes | snapshots]], execute commands, and upload/download files [00:06:36](<a class="yt-timestamp" data-t="00:06:36">00:06:36</a>).

### Linux Sandboxing Models

Understanding Linux sandboxing is crucial for [[building_effective_ai_agents | building effective AI agents]] that are secure.

#### Linux Execution Model

*   **Threads and Processes** A thread is the smallest unit of execution, managed by a `task_struct` in the kernel's scheduler run queue. A process is a logical construct of multiple threads, sharing resources like page tables [00:08:21](<a class="yt-timestamp" data-t="00:08:21">00:08:21</a>).
*   **Kernel and Privileged Access** The kernel provides privileged access to hardware. Special instructions or system calls are needed to switch to kernel mode for privileged operations [00:08:56](<a class="yt-timestamp" data-t="00:08:56">00:08:56</a>).

#### Containers

Containers address the problem of packaging application dependencies by abstracting resources using namespaces (e.g., process, mount, net) and controlling resource access with cgroups [00:09:41](<a class="yt-timestamp" data-t="00:09:41">00:09:41</a>), [00:11:00](<a class="yt-timestamp" data-t="00:11:00">00:11:00</a>).

However, containers run as native processes on top of the host kernel [00:12:20](<a class="yt-timestamp" data-t="00:12:20">00:12:20</a>). This poses a security risk: a kernel vulnerability allows a malicious process to gain root access and compromise the entire system [00:12:30](<a class="yt-timestamp" data-t="00:12:30">00:12:30</a>). Mitigations include jailing containers by restricting Linux capabilities (governing syscalls) and using seccomp to filter or block syscalls [00:13:19](<a class="yt-timestamp" data-t="00:13:19">00:13:19</a>). Libraries like minijail can assist in this process [00:14:19](<a class="yt-timestamp" data-t="00:14:19">00:14:19</a>).

#### Virtualization

Virtualization offers a stronger isolation primitive. Each VM has its own guest user space and guest kernel, providing a smaller attack surface to the host kernel compared to containers [00:14:49](<a class="yt-timestamp" data-t="00:14:49">00:14:49</a>).

*   **VMM (Virtual Machine Monitor)** A VMM process (e.g., QEMU, CrossVM, Firecracker) talks to the `/dev/kvm` device in the Linux kernel to spawn VMs and manage emulated devices (e.g., block, network) [00:15:48](<a class="yt-timestamp" data-t="00:15:48">00:15:48</a>).
*   **VM Exits and Resumes** When a VM needs to access host resources (disk, network), it "exits" to the VMM process. The VMM then interacts with the host kernel and sends the response back to the guest with a "VM resume" [00:17:00](<a class="yt-timestamp" data-t="00:17:00">00:17:00</a>). Minimizing VM exits is crucial for performance [00:17:28](<a class="yt-timestamp" data-t="00:17:28">00:17:28</a>).

#### MicroVMs

MicroVMs differ from traditional VMs by being optimized for security and speed:

*   **Rust-based VMMs** Projects like CrossVM (the first Rust-based VMM), Firecracker, and Cloud Hypervisor offer memory-safe implementations of virtualization, reducing vulnerabilities that can arise from memory safety bugs in C-written devices [00:18:38](<a class="yt-timestamp" data-t="00:18:38">00:18:38</a>).
*   **Device Jailing** They jail emulated devices separately, restricting compromised devices (e.g., block) from accessing unrelated resources (e.g., network) [00:19:14](<a class="yt-timestamp" data-t="00:19:14">00:19:14</a>).
*   **"Micro" Efficiency** By supporting only a limited number of architectures (Intel, ARM) and major devices, MicroVMs have less code, resulting in faster boot times and lower memory consumption [00:19:54](<a class="yt-timestamp" data-t="00:19:54">00:19:54</a>).

Arachis selected **Cloud Hypervisor** as its VMM due to its features like hot plugging of devices, GPU support, snapshot capabilities, and its open-source project governance not being controlled by a single company [00:22:42](<a class="yt-timestamp" data-t="00:22:42">00:22:42</a>). G Visor is another alternative that offers a balance between container performance and improved security, with easier GPU access [00:23:09](<a class="yt-timestamp" data-t="00:23:09">00:23:09</a>).

### Storage and File System

To protect the sandbox's root file system (root FS) from malicious or buggy code that could delete critical files, AI sandboxes utilize an **overlay filesystem** [00:24:40](<a class="yt-timestamp" data-t="00:24:40">00:24:40</a>).

*   **Shared Base Layer** A read-only base layer of the root FS is shared among all sandboxes [00:25:03](<a class="yt-timestamp" data-t="00:25:03">00:25:03</a>).
*   **Read-Write Layer** Each sandbox receives its own unique read-write layer where all new files and modifications are stored [00:25:11](<a class="yt-timestamp" data-t="00:25:11">00:25:11</a>).
*   **Snapshotting Optimization** When a sandbox is [[snapshotting_in_ai_sandboxes | snapshotted]], only this read-write layer is persisted, ensuring efficient storage and sharing of the base image [00:25:31](<a class="yt-timestamp" data-t="00:25:31">00:25:31</a>).

This setup is configured before the sandbox fully boots, presenting a regular Linux file system to the processes running inside [00:25:59](<a class="yt-timestamp" data-t="00:25:59">00:25:59</a>).

### Networking

Every sandbox requires networking to perform actions and call external APIs [00:27:01](<a class="yt-timestamp" data-t="00:27:01">00:27:01</a>).

*   **Isolated Networking** Each sandbox runs in a VM with its own isolated network [00:27:12](<a class="yt-timestamp" data-t="00:27:12">00:27:12</a>).
*   **Tap Device** A unique tap network device (virtual networking interface) is created for each sandbox [00:27:19](<a class="yt-timestamp" data-t="00:27:19">00:27:19</a>).
*   **Linux Bridge** All tap devices connect to a Linux bridge on the host server [00:27:34](<a class="yt-timestamp" data-t="00:27:34">00:27:34</a>).
*   **Port Forwarding** Arachis handles port forwarding using Linux IP tables to facilitate data flow between the host and sandbox, allowing access to services like the code server or VNC server [00:27:44](<a class="yt-timestamp" data-t="00:27:44">00:27:44</a>).

### Code Execution and GUI

Arachis bundles a code execution server, providing APIs for:

*   **File Operations** Uploading and downloading files [00:31:27](<a class="yt-timestamp" data-t="00:31:27">00:31:27</a>).
*   **Command Execution** Executing commands and returning structured output (JSON) [00:31:39](<a class="yt-timestamp" data-t="00:31:39">00:31:39</a>).
    Running this server within a secure guest VM increases confidence in exposing such functionality, unlike running it directly on the host OS [00:31:52](<a class="yt-timestamp" data-t="00:31:52">00:31:52</a>).

Chrome is pre-installed in the sandbox, with port forwarding enabling direct GUI access via the VNC server [00:32:06](<a class="yt-timestamp" data-t="00:32:06">00:32:06</a>).

### Snapshotting in AI Sandboxes

[[snapshotting_in_ai_sandboxes | Snapshotting]] is a critical feature, especially for complex, multi-step tasks where agents often fail towards the end [00:32:30](<a class="yt-timestamp" data-t="00:32:30">00:32:30</a>). Instead of restarting, agents can backtrack to a "last good checkpoint," replan, and retry [00:33:08](<a class="yt-timestamp" data-t="00:33:08">00:33:08</a>).

Arachis allows agents to save the entire running state of a sandbox, including guest memory and the read-write layer of the file system [00:33:30](<a class="yt-timestamp" data-t="00:33:30">00:33:30</a>). This ensures that any processes spawned or windows opened within the GUI are restored exactly as they were [00:33:51](<a class="yt-timestamp" data-t="00:33:51">00:33:51</a>).

The snapshot process involves four steps [00:34:39](<a class="yt-timestamp" data-t="00:34:39">00:34:39</a>):
1.  **Pause the VM** by calling the pause API on the VMM [00:34:44](<a class="yt-timestamp" data-t="00:34:44">00:34:44</a>).
2.  **Call the snapshot API** to dump the guest memory [00:34:50](<a class="yt-timestamp" data-t="00:34:50">00:34:50</a>).
3.  **Persist the read-write overlay FS** to save all files created by the agent [00:34:57](<a class="yt-timestamp" data-t="00:34:57">00:34:57</a>).
4.  **Resume the VMM** to allow the sandbox to continue its operations [00:35:08](<a class="yt-timestamp" data-t="00:35:08">00:35:08</a>).

## Usage and Future Work

[[building_ai_agents_using_primitives | Building AI agents using primitives]] like Arachis is straightforward via its Python SDK [00:35:54](<a class="yt-timestamp" data-t="00:35:54">00:35:54</a>). Users can self-host Arachis, start sandboxes, run commands, manage [[snapshotting_in_ai_sandboxes | snapshots]], and restore checkpoints with simple API calls [00:36:01](<a class="yt-timestamp" data-t="00:36:01">00:36:01</a>).

Ongoing work in Arachis focuses on achieving sub-1-second boot times, enhancing snapshot and persistence support (e.g., by moving to Btrfs for incremental snapshots), and optimizing dynamic memory and resource management (e.g., ballooning, hot-plugging RAM) to bin-pack more sandboxes on a single server [00:39:11](<a class="yt-timestamp" data-t="00:39:11">00:39:11</a>).