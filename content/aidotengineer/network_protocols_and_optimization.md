---
title: Network Protocols and Optimization
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a tech lead for Arista Networks, focuses on the "plumbing" of AI, specifically how models are trained and inferenced on infrastructure <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. His work involves designing and building enterprise networks that support these demanding AI workloads <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Understanding AI Workloads: Training vs. Inference

The concepts of job completion time and barriers are crucial in network design for AI <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. While building networks for model training is understood, inference has significantly evolved due to Chain of Thought and reasoning models <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Dr. Wed Sosa's slide illustrates the scale difference between training and inference: training can involve 248 [[gpu_infrastructure_and_performance | GPUs]] for one to two months, while inference after finetuning and alignment might only require four H100 [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Next-generation models mean inference now consumes significant resources, unlike earlier large language models (LLMs) that required very little <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## AI Network Architecture

AI networks are fundamentally different from traditional data center networks <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. They are designed as two distinct, isolated networks:

*   **Backend Network** This network connects [[gpu_infrastructure_and_performance | GPUs]] directly to each other <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. It is completely isolated due to the high cost, power consumption, and scarcity of [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Typically, servers contain eight [[gpu_infrastructure_and_performance | GPUs]] per pool, connected to high-speed leaf and spine switches <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. [[gpu_infrastructure_and_performance | GPUs]] can operate at 400 GB/s on this network, with future support for 800 GB/s with new [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The backend network is always designed to be wire rate, meaning no oversubscription <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Frontend Network** This network provides storage for the training model, allowing [[gpu_infrastructure_and_performance | GPUs]] to request more data as needed <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It is not as intense as the backend network <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

An H100 server, a popular AI server, features eight 400 gig GPU ports and additional Ethernet ports <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. These servers can generate significant traffic, with an H100 potentially putting 4.8 terabytes onto the network <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Future 800 gig [[gpu_infrastructure_and_performance | GPUs]] could generate 9.6 terabytes per server <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## Networking Challenges in AI Infrastructure

AI networks present unique challenges:

*   **Hardware and Software Differences**
    *   **[[gpu_infrastructure_and_performance | GPU]] Hardware**: New to networking professionals, [[gpu_infrastructure_and_performance | GPUs]] have specific port configurations (e.g., eight 400 gig ports on the backend, four 400 gig ports on the frontend) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Protocols**: Cuda and Nickel are key protocols, with Nickel's "collective" behavior significantly influencing network traffic <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Application Traffic Patterns**
    *   **Synchronized Burstiness**: All [[gpu_infrastructure_and_performance | GPUs]] in an AI network will burst traffic at the same time, potentially reaching their maximum speed (e.g., 400 gig) simultaneously <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This contrasts with typical data center applications that are easier to balance <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
    *   **Failure Impact**: If one [[gpu_infrastructure_and_performance | GPU]] or component fails, the entire training job might fail, unlike traditional applications with built-in failover <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Power Consumption**: AI racks require significantly more power than traditional data center racks. An average rack is 7-15 KW, but a single AI server with eight [[gpu_infrastructure_and_performance | GPUs]] can draw 10.2 KW <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. This necessitates new infrastructure with 100-200 KW racks, often requiring water cooling instead of air cooling <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
*   **Traffic Direction**: AI networks have both East-West (GPU-to-GPU within the backend network) and North-South (GPU-to-storage on the frontend network) traffic patterns <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. East-West traffic is particularly intense, running at wire rate <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Buffering and Congestion Control**: Network switches need robust buffering and congestion control mechanisms to handle the high-speed, bursty traffic <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Single Point of Failure**: A single [[gpu_infrastructure_and_performance | GPU]] failure can stop a model training job <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Cable problems and transceiver issues are also prevalent in large-scale [[gpu_infrastructure_and_performance | GPU]] networks <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Network Complexity**: AI networks are kept simple and isolated, often without firewalls, load balancers, or direct internet connections, to avoid performance bottlenecks <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Key Network Protocols and Technologies for AI

*   **Routing Protocols**: Simple protocols like IBGP or EBGP are used <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. BGP is recommended for its simplicity and speed <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Congestion Control (Rocky V2)**: Essential for AI networks, Rocky V2 has two main components <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>:
    *   **Explicit Congestion Notification (ECN)**: An end-to-end flow control where marked packets inform the receiver of congestion, prompting the sender to slow down <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
    *   **Priority Flow Control (PFC)**: A "stop" mechanism that halts traffic when buffers are full, preventing packet drops <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. PFC and ECN must be correctly configured to avoid network disaster <a class="yt-timestamp" data-t="00:17:58">[00:17:58]</a>.
*   **Remote Direct Memory Access (RDMA)**: Used for memory-to-memory writes, bypassing the CPU for faster data transfer <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. RDMA is a complex protocol with numerous error codes, which can indicate network problems <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **GPU Communication Protocols**: Cuda and Nickel are critical for [[gpu_infrastructure_and_performance | GPU]] communication, especially Nickel's "collective" operations that influence network traffic patterns <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **Ultra Ethernet Consortium (UEC)**: This consortium is working on evolving Ethernet to better handle AI traffic patterns, focusing on improved congestion control, packet spraying, and direct communication between Network Interface Cards (NICs) <a class="yt-timestamp" data-t="00:21:24">[00:21:24]</a>. Version 1.0 is expected to be ratified in Q1 2025 <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

## Network Optimization and Management

*   **No Oversubscription**: Networks are built as "one-to-one" rather than "one-to-ten" or "one-to-three" as in traditional data centers, ensuring maximum bandwidth for [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Advanced Load Balancing**: Standard load balancing (entropy based on 5-tuple IP/port/MAC) is insufficient because [[gpu_infrastructure_and_performance | GPUs]] might use a single IP address, potentially oversubscribing a single uplink <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. New methods load balance based on the percentage of bandwidth used on uplinks, achieving up to 93% utilization <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. "Cluster load balancing" specifically looks at the Nickel collective running on the [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
*   **Buffer Management**: Network switch buffers are tuned to the specific packet sizes sent and received by models, optimizing the use of this expensive commodity <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Visibility and Telemetry**: Enhanced monitoring is crucial to proactively identify network issues before they impact AI jobs <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. This includes tracking RDMA error codes and understanding why packets are dropped <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
*   **AI Agent for [[gpu_infrastructure_and_performance | GPU]]-Network Correlation**: Arista has developed an AI agent (API and code) that runs on Nvidia [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>. This agent communicates with the network switch to verify flow control configurations (PFC and ECN) and provides statistics on packets, RDMA errors, allowing correlation of problems between [[gpu_infrastructure_and_performance | GPU]] and network <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.
*   **Smart System Upgrade**: Allows for upgrading switch software without taking the switch offline, ensuring continuous operation of [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

## Network Scalability Examples

*   A 1,400 gig cluster would use a spine-and-leaf architecture with no oversubscription, featuring 800 gig links between leaf and spine switches and 400 gig links down to the [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   For clusters with thousands of [[gpu_infrastructure_and_performance | GPUs]], larger switches (e.g., Arista's 7800 series 16-slot boxes) are used, which can accommodate 576 x 800 gig [[gpu_infrastructure_and_performance | GPUs]] or 1150 x 400 gig [[gpu_infrastructure_and_performance | GPUs]] <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.

## Summary

AI networks require a specialized approach:
*   The backend network, connecting [[gpu_infrastructure_and_performance | GPUs]], is the most critical and bursty part <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>.
*   [[gpu_infrastructure_and_performance | GPUs]] are synchronized, meaning a slow [[gpu_infrastructure_and_performance | GPU]] creates a "barrier" that slows down all others <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   Job completion time is the key metric <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.
*   Essential network features include no oversubscription, advanced load balancing (especially "cluster load balancing"), Rocky (PFC/ECN) for congestion control, and robust visibility/telemetry <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
*   Network speeds are rapidly increasing, with 800 gig currently available and 1.6 terabytes expected by the end of 2024 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.