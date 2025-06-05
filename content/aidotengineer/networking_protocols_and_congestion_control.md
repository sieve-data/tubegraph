---
title: Networking protocols and congestion control
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Building networks for AI workloads presents unique challenges compared to traditional enterprise networks, primarily due to the intense demands of GPUs and the specific nature of AI traffic patterns <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Paul Gil, a tech lead for Arista Networks, explains the infrastructure and protocols required for efficient [[ai_network_infrastructure | AI network infrastructure]].

## AI Network Architecture
Networks designed for AI workloads are typically isolated and highly specialized. There are two main components:
*   **Backend Network** This network connects GPUs, often with eight GPUs per server (e.g., Nvidia, Super Micro), which then connect to high-speed leaf and spine switches <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. These networks are entirely isolated due to the high cost, power consumption, and scarcity of GPUs <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Nothing else is connected to this network <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Frontend Network** This network provides storage for training models and handles data synchronization for GPUs <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It is less intense than the backend network <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Unique Demands of AI Networks
Traditional data center applications are relatively easy to manage, with traffic flowing one way and failover mechanisms in place <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. AI networks, however, operate differently:
*   **GPU Communication** GPUs communicate with each other, sending and receiving data simultaneously <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. If one GPU fails, the entire job might fail or require a lengthy recovery <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Bursty Traffic** Traffic is highly bursty, with thousands of GPUs capable of bursting at 400 GB/s simultaneously <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. An H100 server alone can put 4.8 terabytes of data onto the network <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Upcoming GPUs (e.g., B-series) could push this to 9.6 terabytes per server <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **No Oversubscription** To handle this bursty traffic, AI networks are built with a one-to-one subscription ratio, meaning no oversubscription <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>. This is significantly different from traditional data centers, which might use 1:10 or 1:3 ratios <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.
*   **Traffic Patterns** AI networks experience both east-west traffic (GPU-to-GPU communication) and north-south traffic (GPU to storage network for data requests) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. East-west traffic typically runs at wire rate <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

## Networking Protocols and Congestion Control
Managing congestion is critical in AI networks to prevent packet loss and ensure job completion time <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Protocols**
    *   **BGP (Border Gateway Protocol)** is recommended as the best, simplest, and quickest protocol for these networks <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
    *   **Cuda and Nickel (NVIDIA Collective Communications Library)** are key software protocols. Nickel, with its collective operations, specifically dictates how traffic is put onto the network <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
    *   **RDMA (Remote Direct Memory Access)** is used for memory-to-memory writes, bypassing the CPU <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. It's a complex protocol with numerous error codes, which need to be monitored to diagnose network problems <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.
*   **Congestion Control Mechanisms**
    *   **Lossless Ethernet** is essential because while some packet drops might be acceptable, too many will cause problems <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
    *   **Rocky V2 (RDMA over Converged Ethernet)** is crucial for congestion control, utilizing two main mechanisms <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>:
        *   **ECN (Explicit Congestion Notification)** is an end-to-end flow control mechanism. When congestion occurs, packets are marked, and the receiver notifies the sender to slow down. The sender then pauses its transmission before gradually speeding up again <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
        *   **PFC (Priority Flow Control)** is a "stop" signal used when network buffers are full, halting traffic entirely <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
    *   **Advanced Load Balancing** Traditional load balancing uses entropy based on five-tuple information (IP address, port, MAC address) <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. However, with GPUs, traffic often comes from a single IP address, leading to oversubscription of uplinks <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. New methods involve load balancing based on the percentage of bandwidth used on uplinks, achieving up to 93% utilization <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. There is also "cluster load balancing" that works with the specific collective operations being run <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>.
    *   **Buffer Management** Network switches have limited buffering <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. By adjusting buffer sizes to match the specific packet sizes sent and received by models, network efficiency can be significantly improved <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

## Visibility and Monitoring
Proactive monitoring is crucial to prevent model failures and minimize downtime <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>.
*   **Telemetry** Different telemetry and visibility tools are deployed to detect network issues before they impact operations <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>.
*   **Packet Analysis** Instead of simply dropping packets during congestion, advanced systems can capture snapshots of packets and their headers (including RDMA information) to provide detailed reasons for the drop <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
*   **AI Agent** An [[MultiAgent Communication Systems | AI agent]] running on GPUs, with an API and code, can communicate with switches to verify correct configuration of flow control mechanisms (PFC and ECN) <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. It also provides statistics on packets received/sent and RDMA errors, helping to correlate problems to either the GPU or the network <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

## Future Developments
*   **Ultra Ethernet Consortium** This initiative aims to improve Ethernet for AI workloads by addressing congestion control and packet spraying, and by offloading more functions to Network Interface Cards (NICs), allowing the network to focus on forwarding packets <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Version 1.0 is expected to be ratified in Q1 2025 <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Increased Bandwidth** Network speeds are rapidly increasing, with 800 GB/s already supported and 1.6 TB/s expected by the end of 2024 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. Models will continue to grow larger and consume more network resources <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.