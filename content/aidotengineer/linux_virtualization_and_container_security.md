---
title: Linux virtualization and container security
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

Linux sandboxing is crucial for modern applications, particularly those involving [[ai_agents_in_devops | AI agents]] and untrusted code execution <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article explores the evolution of Linux sandboxing techniques, from basic execution models to advanced virtualization methods like [[microvms_for_secure_ai_sandboxing | MicroVMs]], emphasizing their role in ensuring [[ai_security_and_observability | security]] and stability.

## Linux Execution Model
The fundamental unit of execution on Linux is a thread <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Each thread has a `task_struct` in the kernel's scheduler run queue, which represents the unit of execution <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. A process is a logical construct comprising multiple threads that share page tables and other resources <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The kernel provides privileged access to hardware <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. To prevent buggy or malicious code from crashing a device or performing harmful actions, special instructions (like `int 0x80` for system calls) are required to switch to kernel or supervisor mode for privileged operations <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

## Containers
Containers offer a solution for packaging an application's dependencies along with its core logic, enabling arbitrary user code to run on a machine <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This is a core feature needed for an [[ai_security_and_observability | AI sandbox]] <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

Technically, a container on Linux is a collection of namespaces that abstract different resources, such as process, mount, and network <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. For example, a container's process namespace sees its own processes as `pid 1, pid 2`, etc., while these are arbitrary processes in the root namespace outside the container <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. The host can inspect a child container's namespace, but a container cannot look upwards into its host namespace <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Cgroups are used in conjunction with namespaces to control resource access, such as CPU and memory percentages, allocated to a specific container <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

### Container Security
Containers run as native processes directly on top of the host kernel <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This means that a kernel vulnerability can be exploited by any malicious or buggy process within a container to gain root access on the host, leading to data exfiltration, system compromise, and other attack vectors <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.

To mitigate these risks, techniques are used to jail containers by restricting Linux capabilities (`caps`) and system calls <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.
*   **Capabilities:** Linux capabilities govern which privileged operations a process can perform, allowing only necessary capabilities to be granted <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **Seccomp (Secure Computing Mode):** Filters arguments to system calls or blocks them entirely, further reducing the attack surface <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

Despite these measures, sandboxing and jailing still have limits, and containers can potentially bypass them <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

## Virtualization on Linux
Virtualization offers a stronger primitive for running untrusted or arbitrary code <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Unlike containers, each Virtual Machine (VM) has its own guest user space and guest kernel, providing isolated environments <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>. This model presents a significantly smaller attack surface to the host kernel <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.

VMs access host resources via a Virtual Machine Monitor (VMM), such as QEMU, CrossVM, or Firecracker <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. The VMM communicates with `/dev/kvm`, a Linux kernel device that exposes the processor's virtualization stack and provides an API for spawning VMs and granting privileged resource access <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. When a VM needs to access host resources like disk or network, it triggers a "VM exit" back to the host <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. The VMM handles the request with the host kernel and sends the response back to the guest with a "VM resume" <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. Minimizing VM exits and resumes is crucial for performance <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. While CPU-bound operations within a guest incur no penalty due to direct processor execution, I/O-bound loads can lead to performance trade-offs due to frequent exits <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## MicroVMs for Secure AI Sandboxing
[[microvms_for_secure_ai_sandboxing | MicroVMs]] are a distinct evolution of virtualization that prioritize [[ai_security_and_observability | security]] and speed <a class="yt-timestamp" data-t="00:19:39">[00:19:39]</a>. The concept originated from the CrossVM project at Chrome OS <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

Key differences from traditional VMs include:
*   **Rust-based VMMs:** VMMs like CrossVM, Firecracker, and Cloud Hypervisor are written in Rust, providing memory-safe implementations that mitigate memory safety-related bugs often found in C-written devices <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>. This reduces the attack surface from untrusted guest code to the host <a class="yt-timestamp" data-t="00:18:57">[00:18:57]</a>.
*   **Jailed Emulated Devices:** [[microvms_for_secure_ai_sandboxing | MicroVMs]] jail their emulated devices separately. For instance, a block device is restricted to only block-related system calls, preventing network access if compromised, and vice versa <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
*   **Performance Optimization ("Micro"):** [[microvms_for_secure_ai_sandboxing | MicroVMs]] are designed to boot rapidly and consume less memory <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. Unlike old VMMs like QEMU that support many architectures and emulated devices, [[microvms_for_secure_ai_sandboxing | MicroVMs]] typically support only one or two architectures (Intel, ARM) and major devices, resulting in less code and fewer code paths at boot <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. The "micro" refers to the lightweight nature of the VMM process itself, not necessarily the guest <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.

### Arachis's Choice of MicroVMs
Arachis, an open-source code execution and computer use sandboxing service for [[ai_agents_in_devops | AI agents]], utilizes a [[microvms_for_secure_ai_sandboxing | MicroVM]] runtime as its final execution environment <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The choice of [[microvms_for_secure_ai_sandboxing | MicroVMs]] is driven by several design factors:
*   **[[ai_security_and_observability | Security]]:** Paramount for [[ai_agents_in_devops | AI sandboxes]], especially for multi-tenant code execution where LLM-generated code might access different clients' data <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. Preventing untrusted code from gaining root access is critical <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.
*   **Fast Boot Times:** Arachis currently boots in less than 7 seconds, with ongoing efforts to reduce it to under a second <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Snapshotting:** [[microvms_for_secure_ai_sandboxing | MicroVMs]] enable fast snapshots by dumping the entire guest memory, allowing [[ai_agents_in_devops | agents]] to backtrack to a good checkpoint if multi-step workflows fail <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. This provides more reliable, higher-order complex task execution for [[ai_agents_in_devops | agents]] <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Arachis considered various VMMs:
*   **CrossVM:** Initiated the [[microvms_for_secure_ai_sandboxing | MicroVM]] revolution <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Firecracker:** Underpins AWS Lambda for serverless loads, featuring a fleshed-out REST API and better jailing [[ai_application_frameworks_and_architecture | architecture]] <a class="yt-timestamp" data-t="00:22:27">[00:22:27]</a>.
*   **Cloud Hypervisor:** A more general-purpose [[enterprise_ai_deployment_within_security_boundaries | enterprise VMM]] <a class="yt-timestamp" data-t="00:22:40">[00:22:40]</a>. It offered hot plugging of devices, GPU support, and snapshot support at the time of choice <a class="yt-timestamp" data-t="00:22:44">[00:22:44]</a>. Its open-source project structure, not controlled by a single company, also made it a sensible choice for Arachis <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>.

Another option for sandboxing is **GVisor**, which is closer to a container in performance but offers slightly better [[ai_security_and_observability | security]] <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>. While untrusted code can still attack the host kernel in GVisor, it can be a good intermediate option, especially for scenarios requiring easier GPU access compared to [[microvms_for_secure_ai_sandboxing | MicroVMs]] <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. Ultimately, the choice depends on specific needs and [[ai_security_and_observability | security]] guarantees <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. Arachis opted for Cloud Hypervisor as its underlying [[microvms_for_secure_ai_sandboxing | MicroVM]] VMM <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>.