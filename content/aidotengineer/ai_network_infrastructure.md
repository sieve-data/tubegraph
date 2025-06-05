---
title: AI network infrastructure
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a tech lead for Arista Networks based in New York City, designs and helps build enterprise networks, focusing on the underlying "plumbing" for AI workloads. His work involves understanding the infrastructure required for training models and performing inferencing [00:00:23].

## Training vs. Inference Infrastructure

Traditional networking terms like "job completion time" and "barrier" are evolving for AI workloads [00:00:54]. The nature of inference, especially with advancements like Chain of Thought and reasoning models, has significantly changed [00:01:13].

For example, a model might require 248 GPUs for one to two months for training, but only four H100s for inference after fine-tuning and alignment [00:02:05]. This divergence necessitates different network designs for each phase [00:01:16]. While Large Language Models (LLMs) historically required a small amount of inference, next-generation models demand much more [00:02:27].

## Core Components of AI Networks

[[ai_data_center_design_and_challenges | AI data center design]] presents unique challenges compared to traditional data centers [00:06:31].

### Backend Network (GPU Connections)
This network connects GPUs and is designed to be completely isolated due to the high cost, power consumption, and scarcity of GPUs [00:02:42].
*   **Structure**: Typically, servers house eight GPUs per pool (e.g., Nvidia, Supermicro) [00:03:03]. These connect to high-speed leaf switches, which then connect to spine switches, forming an isolated network [00:03:10].
*   **Speed**: GPUs on the backend network can operate at 400 gigabits per second (Gbps) depending on the model being trained, a speed rarely seen in typical enterprise data centers [00:03:39]. Future B-series GPUs are expected to reach 800 Gbps [00:08:00].
*   **Simplicity**: These networks are built to be as simple as possible, often using basic protocols like IBGP or EBGP, to ensure 24/7 operation and maximize return on investment for expensive hardware [00:03:58].

### Frontend Network (Storage Connections)
This network provides storage access for training models and requesting more data [00:03:20].
*   **Intensity**: The frontend network is less intense than the backend, as storage vendors generally cannot sustain the same traffic levels as GPUs, typically operating around 100-200 Gbps [00:03:34].

### GPU Specifics (e.g., H100)
The H100 is a popular AI server [00:04:23]. Its back features eight GPU ports (four physical ports broken out into two each) for high-speed GPU-to-GPU communication, in addition to standard Ethernet ports for frontend connections [00:04:30]. Servers can put significant traffic onto the network, with an H100 alone potentially generating 4.8 terabits per second (Tbps) of traffic from its eight 400 Gbps GPU ports [00:07:44]. Future 800 Gbps GPUs could push this to 9.6 Tbps per server [00:08:10].

## Key Characteristics and Challenges of AI Networks

### Isolation and Security
AI networks, especially the backend, are kept completely isolated from other enterprise traffic to protect expensive GPU resources [00:02:45]. This helps ensure [[enterprise_ai_within_security_boundaries | security for enterprise AI]] deployments [00:13:12].

### High Bandwidth Requirements
Unlike traditional data centers, which might have 1:10 or 1:3 oversubscription ratios, AI networks require a 1:1 (no oversubscription) design to handle the massive, simultaneous data bursts from GPUs [00:07:19]. This makes them very expensive to build due to the required bandwidth [00:07:31]. Current networks operate at 400 Gbps and 800 Gbps, with 1.6 terabits expected by the end of 2024 or early 2027 [00:14:25].

### Traffic Patterns
*   **Bursty**: All GPUs in an AI network, even thousands of them, can burst at their maximum rate (e.g., 400 Gbps) simultaneously, creating enormous traffic spikes [00:07:03].
*   **East-West vs. North-South**: GPU-to-GPU communication is primarily east-west traffic, often running at wire rate. Requests for data from storage networks are north-south traffic, which tends to be calmer [00:11:16].

### Power and Cooling
AI racks demand significantly more power than typical data center racks. An average data center rack might draw 7-15 KW, accommodating multiple servers. An AI server with eight GPUs alone can draw 10.2 KW, meaning only one such server can fit into a standard rack [00:10:10]. Newer AI racks are being built to handle 100-200 KW and require water cooling, as air cooling is insufficient [00:10:48]. This is a major [[ai_data_center_design_and_challenges | challenge in AI data center design]] [00:10:55].

### GPU Synchronization and Job Completion Time
In an AI network, GPUs communicate extensively and collectively. If one GPU fails or slows down, the entire job might fail or be significantly delayed, affecting job completion time [00:06:48]. Checkpointing models can mitigate this but is expensive [00:22:34].

### Error Handling
Optics, transceivers, and cabling issues are common problems in large-scale networks. When building AI networks with thousands of GPUs, cable and GPU problems are inevitable, making troubleshooting complex for network engineers unfamiliar with this new environment [00:09:44].

## Networking Protocols and Mechanisms for AI

[[importance_of_infrastructure_design_for_ai_applications | Infrastructure design for AI applications]] must account for specific networking requirements.

### Congestion Control (RDMA over Converged Ethernet - RoCE V2)
To handle the bursty, high-volume traffic and prevent packet loss, AI networks rely on RoCE V2, which incorporates two key mechanisms [00:12:04]:
*   **Explicit Congestion Notification (ECN)**: An end-to-end flow control where congested network packets are marked. The receiver notifies the sender to slow down until congestion clears [00:12:17].
*   **Priority Flow Control (PFC)**: A "stop" mechanism that halts traffic when buffers are full, preventing packet drops at the switch level [00:12:41].
These are critical because packet loss can lead to model failures or significantly increased job completion times [00:15:28].

### Load Balancing
Traditional load balancing using entropy (five-tuple: IP address, port, MAC address) can be ineffective with GPUs, which often share a single IP address, potentially oversaturating an uplink [00:08:37]. Advanced load balancing in AI networks looks at the percentage of bandwidth utilized on uplinks to achieve up to 93% utilization across all links [00:09:14]. Some systems can even load balance based on the specific collective operations being run by GPUs [00:19:47].

### Buffer Management
Network switches need efficient buffering. Since AI models often send and receive specific packet sizes, buffers can be precisely tuned to these sizes, optimizing resource allocation and saving costs [00:16:05].

## Visibility and Monitoring

[[telemetry_and_monitoring_in_ai_data_centers | Telemetry and monitoring]] are crucial in AI data centers to proactively identify issues.

*   **RDMA Error Monitoring**: RDMA is a complex protocol with many error codes. AI network monitoring systems can capture snapshots of dropped packets, including headers and RDMA information, to identify the cause of packet loss [00:16:47].
*   **[[integration_of_ai_agents_into_existing_infrastructure | AI Agents]] for GPU-Network Correlation**: An [[ai_in_it_infrastructure_management | AI agent]] can be loaded onto GPUs (e.g., Nvidia) to communicate with network switches via API. This agent verifies correct configuration of flow control mechanisms (PFC, ECN) and provides statistics on packets sent/received and RDMA errors. This allows correlation between GPU performance and network health, determining if a problem originates from the GPU or the network [00:17:36].
*   **Smart System Upgrade**: Allows for upgrading switch software without taking the network offline, which is critical for maintaining continuous GPU operation in large clusters [00:18:32].

## Future Trends

*   **Ultra Ethernet Consortium (UEC)**: This consortium aims to evolve Ethernet to better suit AI workloads by improving congestion control, packet spraying, and direct communication between Network Interface Cards (NICs). Version 1.0 is expected to be ratified by Q1 2025, with deployments potentially seen by Q3/Q4 [00:21:23]. UEC intends to offload more functionality to NICs, allowing the network to focus on simple forwarding [00:21:56].
*   **Increased Bandwidth**: Network speeds are continuously increasing, with 800 Gbps becoming common and 1.6 Tbps expected soon [00:14:25].

## Key Takeaways

*   **No oversubscription** on the backend network [00:19:10].
*   **Simple, quick protocols** like BGP are preferred [00:19:30].
*   **RDMA (RoCE V2, ECN, PFC)** is essential for managing bursty traffic and preventing network meltdowns [00:19:54].
*   **Advanced load balancing** (e.g., cluster load balancing based on collective operations) is necessary [00:19:43].
*   **Visibility and telemetry** are critical for proactive problem detection before job completion time is impacted [00:20:06].
*   **GPU synchronization** means a slow or failed GPU can halt the entire job [00:22:19].
*   AI network infrastructure requires entirely new design considerations, different from traditional enterprise data centers [00:03:50].