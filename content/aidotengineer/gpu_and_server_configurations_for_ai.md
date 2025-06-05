---
title: GPU and server configurations for AI
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a Tech Lead for Arista Networks, specializes in building and designing enterprise networks, particularly the underlying infrastructure for [[building_scalable_ai_systems | training AI models]] and performing inferencing <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a> <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. His work focuses on the "plumbing" of AI systems, detailing what the infrastructure looks like for these demanding workloads <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Training vs. Inference Workloads

The infrastructure requirements differ significantly between model training and inferencing <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Training**: Historically, training might require 18 times the resources compared to inference <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. A typical example involves training a model using 248 GPUs for one to two months <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   **Inference**: After fine-tuning and alignment, the same model might only require four H100 GPUs for inference <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. However, with the advent of Chain of Thought and reasoning models, the nature and scale of inference are evolving, becoming more intensive than previously seen with traditional Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## AI Network Architecture

AI infrastructure typically comprises two distinct network types:

### Backend Network
This network connects GPUs directly and is designed to be completely isolated due to the high cost and scarcity of GPUs <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a> <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **GPU Servers**: Servers typically contain eight GPUs (e.g., Nvidia, Super Micro), which connect to high-speed leaf and spine switches <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a> <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Traffic Intensity**: GPUs in the backend network operate at extremely high speeds, with current models working at 400 Gigabit per second (Gbps) <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. These speeds are unprecedented in typical enterprise data centers <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Isolation**: No other devices are connected to this network to prevent interference and ensure maximum uptime for expensive GPU resources <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Protocols**: Simple routing protocols like IBGP or EBGP are used to keep the network as efficient as possible <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Frontend Network
This network provides storage access to the GPUs for training data <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Traffic Profile**: It is less intense than the backend network because current storage vendors cannot match the speeds required by the GPUs <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a> <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Storage traffic typically runs at 100-200 Gbps <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.

## GPU and Server Specifications

The NVIDIA H100 is noted as the most popular AI server currently available <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a> <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Connectivity**: An H100 server features eight 400 Gbps GPU ports (broken out from four physical ports) and additional Ethernet ports <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a> <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Traffic Capacity**: A single H100 server with eight 400 Gbps GPUs and four 400 Gbps front-end ports can generate 4.8 terabytes per second (TBps) of traffic <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Future Speeds**: 800 Gbps GPUs (B-series) are expected soon, potentially increasing server traffic to 9.6 TBps <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Scalability**: AI networks are designed for scale-out, allowing the addition of more GPUs, starting small and potentially expanding to hundreds of thousands of GPUs in cloud environments <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. Scale-up (adding to existing servers) is not typical for Nvidia servers like the DGX or HGX <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

## Unique Challenges and Solutions in AI Networking

### Network Design
*   **No Oversubscription**: AI networks, particularly the backend, are built with a one-to-one subscription ratio, meaning bandwidth is fully provisioned without oversubscription. This contrasts with traditional data centers that might use ratios of 1:10 or 1:3 due to [[cost_and_efficiency_in_deploying_ai_systems | cost considerations]] <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a> <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Traffic Patterns**:
    *   **East-West Traffic**: GPUs communicate directly with each other (east-west traffic), which is highly bursty, with all GPUs potentially bursting at 400 Gbps simultaneously <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a> <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This is the wire-rate traffic.
    *   **North-South Traffic**: When GPUs request more data from storage, it's north-south traffic <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   **Load Balancing**: Traditional load balancing (e.g., using five-tuple entropy) is inefficient as GPU traffic often uses a single IP address, potentially oversubscribing a single uplink <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Advanced tools now load balance based on the percentage of bandwidth utilized on uplinks, achieving up to 93% utilization <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a> <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. Cluster load balancing looks at the collective operation being run <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>.
*   **Addressing**: Point-to-point connections (e.g., /30, /31) are preferred, with IPv6 as an option for address space issues <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>. BGP is recommended as the routing protocol <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. EVPN VXLAN can be used for multi-tenancy <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

### Power and Cooling
*   **High Power Draw**: A single AI server with eight GPUs can draw 10.2 kilowatts (KW), compared to 7-15 KW for an entire traditional data center rack <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a> <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Advanced Racks**: Enterprises are now building racks capable of handling 100-200 KW, necessitating water cooling instead of traditional air cooling <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a> <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

### Fault Tolerance and Monitoring
*   **GPU Dependencies**: Unlike traditional data center applications where failures might cause minor skips, a single GPU failure in an AI network can halt the entire job, making reliability paramount <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. Job completion time is the critical metric <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.
*   **Lossless Ethernet and Congestion Control**: To prevent packet drops, which are detrimental to synchronized GPUs, AI networks implement lossless Ethernet using Remote Direct Memory Access (RDMA) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a> <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>. Key mechanisms include:
    *   **Explicit Congestion Notification (ECN)**: An end-to-end flow control that marks packets during congestion, prompting the sender to slow down <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
    *   **Priority Flow Control (PFC)**: A "stop" mechanism that halts traffic when buffers are full, acting as an emergency brake <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   [[telemetry_and_monitoring_in_ai_data_centers | Telemetry and Monitoring]]: Crucial for proactive problem identification. Switches can provide detailed insights into packet drops, including why they occurred and any associated RDMA error codes <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a> <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>.
*   **AI Agent for GPU-Network Correlation**: A network-side [[scaling_ai_agents_in_production | AI agent]] (API and code) can be loaded onto GPUs to communicate with network switches <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. This agent verifies network configuration (e.g., PFC/ECN settings) and provides statistics on packets sent/received and RDMA errors, allowing correlation between GPU and network problems <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Smart System Upgrade**: Networks can be upgraded without taking switches offline, enabling continuous operation of GPUs during maintenance <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

## Future Developments

*   **Ultra Ethernet Consortium (UEC)**: This consortium aims to evolve Ethernet to better handle AI traffic patterns, specifically improving congestion control and packet spraying, and optimizing communication between Network Interface Cards (NICs) <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. Version 1.0 is expected to be ratified in Q1 2025 <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

AI networks are rapidly evolving, with speeds increasing to 800 Gbps and future projections of 1.6 TBps by the end of 2026 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a> <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a> <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>. This continuous growth in model size and data consumption necessitates specialized and robust network infrastructure <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.