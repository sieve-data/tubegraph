---
title: GPU Infrastructure and Performance
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a tech lead for Arista Networks based in New York City, designs and helps build enterprise networks <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. His focus is on the underlying "plumbing" of the network infrastructure required for training and inferencing AI models <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## AI Network Fundamentals

Traditional computer networks prioritize "job completion time" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. For AI, understanding the distinction between model training and inference is crucial for [[designing_ai_networks_and_data_centers | network design]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### Training vs. Inference
Training typically involves a large number of GPUs (e.g., 248 GPUs for one to two months) <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, while inference, especially after fine-tuning and alignment, might use significantly fewer (e.g., four H100s) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The complexity of inference has increased with models like Chain of Thought and reasoning <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Next-generation LLMs now require substantial inference capabilities <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Network Segregation
AI networks are typically segmented into two main parts <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>:
1.  **Backend Network**: Connects GPUs to each other <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This network is completely isolated due to the expense and power requirements of GPUs <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Frontend Network**: Used for storage, allowing GPUs to call for more data after calculations <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Backend Network: The Core of GPU Communication

The backend network is where GPUs (like Nvidia or Supermicro) in servers, typically eight GPUs per server, connect to high-speed leaf and spine switches <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Nothing else attaches to this network <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### High-Speed Requirements
*   GPUs can operate at 400 GB/s on the backend network, a speed rarely seen in typical enterprise data centers <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   An Nvidia H100 server can put 4.8 terabytes per second (TB/s) of traffic onto the network from its eight 400 gig GPU ports and four 400 gig frontend ports <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   Upcoming 800 gig "B" series GPUs are expected to generate 9.6 TB/s per server <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   Network speeds are rapidly increasing, with 1.6 terabytes per second expected by late 2026 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

### Network Design for Performance
*   **Simplicity**: Networks are built as simply as possible to ensure 24/7 operation of expensive GPUs <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Simple protocols like IBGP or EBGP are used <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **No Over-subscription**: AI networks are built with a one-to-one subscription ratio, unlike traditional data centers that might use 1:10 or 1:3 <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This is critical because GPUs will burst at their full 400 gig capacity simultaneously <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Traffic Patterns**:
    *   **East-West Traffic**: Predominates on the backend network as GPUs communicate directly with each other at wire rate <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
    *   **North-South Traffic**: Occurs when GPUs request data from the storage network <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Load Balancing**: Traditional load balancing (e.g., 5-tuple IP address, port, MAC address) can lead to oversubscription on single uplinks in AI networks <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Advanced methods are needed, such as balancing based on the percentage of bandwidth used on an uplink, achieving up to 93% utilization <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Specific collective load balancing is also possible for [[ai_application_frameworks_and_architecture | AI application frameworks]] <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.

### Power and Cooling
AI racks require significantly more power. A typical data center rack uses 7KW to 15KW, accommodating multiple servers <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>. An AI server with eight GPUs, however, can draw 10.2 KW, meaning only one such server fits in a traditional rack <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>. New racks for AI are being built to support 100-200 KW and require water cooling, as air cooling is insufficient <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

## Frontend Network: Data Ingestion

The frontend network is responsible for providing storage to train the model <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It is less intense than the backend, with most storage vendors currently putting around 100-200 gigabits per second (GB/s) of traffic on the network <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

## Unique Challenges and Solutions in AI Networking

Building [[designing_ai_networks_and_data_centers | AI networks]] presents distinct challenges compared to traditional data centers <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>:

*   **Hardware and Software**: The reliance on GPUs and specific software protocols like CUDA and NCCL (Nickel) is new <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. NCCL, with its collective operations, dictates how traffic is placed on the network <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Application Behavior**: Unlike web applications or databases with clear client-server patterns, all GPUs in an AI network communicate actively with each other <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. If one GPU fails, the entire training job might fail <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Error Management**: A single GPU failure can halt a model <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. With thousands of GPUs, cable, optics, and transceiver issues become prevalent <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Congestion Control**:
    *   **Buffering**: Switches require robust buffering, which is an expensive commodity <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Buffers can be adjusted to efficiently accept the specific packet sizes common in AI models <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
    *   **[[cost_and_latency_optimization_in_ai_deployments | Congestion Control]] and Feedback**: Rocky V2 (RDMA over Converged Ethernet) is essential <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. It has two main components:
        *   **ECN (Explicit Congestion Notification)**: An end-to-end flow control where marked packets inform receivers to tell senders to slow down <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
        *   **PFC (Priority Flow Control)**: A "stop" signal used when buffers are full, acting as an emergency brake <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
    *   Lossless Ethernet is key <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
*   **Network Isolation**: AI networks are kept totally isolated from other networks, including the internet, to prevent risks to expensive hardware <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
*   **On-Demand Applications**: Unlike traditional applications that might recover seamlessly from failures, an AI model failure can be a critical event <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
*   **RDMA Monitoring**: RDMA (Remote Direct Memory Access) is a complex protocol crucial for [[gpu_kernel_optimization | GPU kernel optimization]] and requires monitoring for error codes and dropped packets <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>. Network devices can capture packet headers and RDMA information to diagnose reasons for packet drops <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
*   **AI Agent**: An AI agent, loaded on Nvidia GPUs via an API, allows the GPU to communicate with the network switch. It verifies correct flow control configuration (PFC, ECN) and provides statistics on packets sent/received and RDMA errors, helping to correlate problems to either the GPU or the network <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This enhances [[visibility_and_telemetry_in_ai_networks | visibility and telemetry]] <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **Smart System Upgrade**: Allows upgrading switch software without taking the switch offline, critical for maintaining 24/7 operation of large GPU clusters <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

## Network Design Recommendations for AI

Key considerations for [[designing_ai_networks_and_data_centers | AI network design]] include:
*   No oversubscription on the backend <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
*   Point-to-point connections with specific IP addressing (e.g., /30, /31) or IPv6 <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   Using BGP as the routing protocol due to its simplicity and speed <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   EVPN VXLAN for multi-tenancy <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
*   Mandatory deployment of Rocky (PFC and ECN) to prevent network meltdown and provide early warnings <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   Continuous [[visibility_and_telemetry_in_ai_networks | visibility and telemetry]] to proactively identify issues <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>.

## Future Developments

The Ultra Ethernet Consortium (UEC) is working on evolving Ethernet to better handle AI workloads, focusing on congestion control, packet spraying, and NIC-to-NIC communication <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Version 1.0 is expected to be ratified in Q1 2025 <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>. This initiative aims to shift more intelligence into the NICs, simplifying the network's role to just forwarding packets <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>.

## Summary

The backend network for GPUs is the most critical and bursty component of [[scaling_generative_ai_workloads | AI infrastructure]] <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. Since GPUs operate in synchronization, a slow GPU can become a barrier for the entire system <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. "Job completion time" is the primary metric, and network issues can drastically increase it <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>. Although models can use checkpoints, these are expensive <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>.