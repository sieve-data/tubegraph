---
title: AI data center design and challenges
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a Tech Lead for Arista Networks based in New York City, specializes in designing and building enterprise networks, particularly the "plumbing" for [[ai_network_infrastructure | AI networks]] where models are trained and inference is performed [00:00:16]. The [[ai_network_infrastructure | AI network infrastructure]] presents unique [[challenges_in_aidriven_architecture_design | challenges]] that differentiate it from traditional data center designs [00:05:43].

## Training vs. Inference Infrastructure
The infrastructure requirements for training and inference in AI are distinct:
*   **Training** involves significant computational resources [00:01:04]. For example, a model might be trained on 248 [[gpu_and_server_configurations_for_ai | GPUs]] for one to two months [00:02:03].
*   **Inference** has evolved, especially with Chain-of-Thought and reasoning models [00:01:13]. After fine-tuning and alignment, the same model might only require four H100 [[gpu_and_server_configurations_for_ai | GPUs]] for inference [00:02:10]. While Large Language Models (LLMs) used to need minimal inference capabilities, next-generation models demand significantly more [00:02:25]. This often necessitates building different types of networks for each process [00:01:16].

## AI Network Architecture
[[ai_network_infrastructure | AI networks]] typically consist of two main parts:
*   **Backend Network** <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:
    *   This network connects the [[gpu_and_server_configurations_for_ai | GPUs]] [00:02:40].
    *   It is completely isolated from other networks because [[gpu_and_server_configurations_for_ai | GPUs]] are expensive, power-intensive, and hard to acquire [00:02:45].
    *   Servers typically contain eight [[gpu_and_server_configurations_for_ai | GPUs]] (e.g., Nvidia, Supermicro), which connect to high-speed leaf and spine switches [00:03:03].
    *   No other devices are attached to this network [00:03:16].
    *   [[gpu_and_server_configurations_for_ai | GPUs]] can operate at 400 GB, generating unprecedented traffic volumes for enterprise networks [00:03:39].
    *   Networks are kept as simple as possible, often using IBGP or EBGP protocols, to ensure 24/7 operation and maximize return on investment [00:03:58].
    *   The backend network operates at "wire rate," meaning it needs to deliver the maximum possible speed [00:07:58].
    *   Crucially, these networks are built with **no oversubscription** (1:1 ratio), a significant departure from traditional data centers that might use 1:10 or 1:3 ratios due to the cost of bandwidth [00:07:19].
*   **Frontend Network** <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>:
    *   This network handles storage access for training data [00:03:21].
    *   It is generally less intense than the backend network, with storage vendors typically supporting 100-200 gigabits per second currently [00:11:34].

## Hardware and Traffic Characteristics
*   **[[gpu_and_server_configurations_for_ai | GPU and Server Configurations]]**: An H100 server, a popular [[gpu_and_server_configurations_for_ai | AI server]], has four ports that break out into eight [[gpu_and_server_configurations_for_ai | GPU]] ports and additional Ethernet ports for connectivity [00:04:23]. One H100 server with 8x400 gig [[gpu_and_server_configurations_for_ai | GPUs]] and 4x400 gig connections can generate 4.8 terabytes of traffic [00:07:44]. Newer B200 [[gpu_and_server_configurations_for_ai | GPUs]] will operate at 800 gigabits, potentially generating 9.6 terabytes per server [00:08:00].
*   **Network Scalability**: While "scale up" (adding more [[gpu_and_server_configurations_for_ai | GPUs]] to a single server) isn't common with fixed configurations like Nvidia's DGX/HGX, "scale out" (adding more [[gpu_and_server_configurations_for_ai | GPU]] servers to the network) is supported, enabling clusters from small to hundreds of thousands of [[gpu_and_server_configurations_for_ai | GPUs]] in cloud environments [00:05:07].
*   **Traffic Patterns**:
    *   [[ai_network_infrastructure | AI networks]] experience "bursty" traffic where thousands of [[gpu_and_server_configurations_for_ai | GPUs]] can simultaneously burst at their full capacity (e.g., 400 gigabits) [00:07:03].
    *   Traffic is bi-directional (both East-West and North-South) [00:11:03]. East-West traffic (between [[gpu_and_server_configurations_for_ai | GPUs]]) is often at wire rate, while North-South traffic (to storage) is generally calmer [00:11:16].
*   **Protocols**:
    *   NVIDIA Collective Communications Library (NCCL) is crucial for understanding how traffic is placed on the network, especially for collective operations [00:06:05].
    *   RDMA (Remote Direct Memory Access) over Converged Ethernet (RoCE) v2 is used for memory-to-memory writes, bypassing the CPU [00:16:44]. It has complex error codes [00:16:59].
    *   Congestion control mechanisms are vital due to bursty traffic and the synchronized nature of [[gpu_and_server_configurations_for_ai | GPUs]]:
        *   **ECN (Explicit Congestion Notification)**: An end-to-end flow control mechanism where packets are marked during congestion, signaling the receiver to inform the sender to slow down [00:12:16].
        *   **PFC (Priority Flow Control)**: A "dead stop" mechanism that halts traffic flow when buffers are full [00:12:41].
    *   These protocols ensure "lossless Ethernet," meaning packets are not dropped, as dropping too many packets can halt the AI model's job [00:15:27]. If one [[gpu_and_server_configurations_for_ai | GPU]] slows down, the entire synchronized cluster slows down [00:15:53].

## Operational Challenges and Solutions
*   **Power Requirements**: AI racks demand significantly more power. Traditional data center racks consume 7-15 KW, fitting multiple 1U servers [00:10:19]. An [[gpu_and_server_configurations_for_ai | AI server]] with eight [[gpu_and_server_configurations_for_ai | GPUs]] can draw 10.2 KW, meaning only one server fits in a standard rack [00:10:41]. This necessitates new racks (100-200 KW) and **water cooling**, as air cooling is insufficient [00:10:48].
*   **Load Balancing**: Traditional load balancing using 5-tuple entropy (IP, port, MAC) can be problematic because [[gpu_and_server_configurations_for_ai | GPUs]] often use a single IP address, potentially oversubscribing a single uplink [00:08:49]. Newer methods balance based on the percentage of bandwidth used on uplinks, achieving up to 93% utilization [00:09:10]. [[ai_in_it_infrastructure_management | Advanced load balancing]] can also consider the collective being run [00:19:43].
*   **Fault Tolerance**: Unlike traditional data center applications that can fail over, a single [[gpu_and_server_configurations_for_ai | GPU]] failure in an [[ai_network_infrastructure | AI network]] can halt the entire model training job [00:06:48]. Physical issues like optics, transceivers, and cable problems are more prevalent with thousands of [[gpu_and_server_configurations_for_ai | GPUs]] [00:09:44].
*   **Network Isolation**: Due to the high cost and criticality, [[ai_network_infrastructure | AI networks]] are totally isolated, without connections to the internet, DMZs, firewalls, or load balancers typical of regular data centers [00:13:00].
*   **Buffering**: Network switches need to optimize buffering to accommodate the specific packet sizes sent and received by AI models [00:16:11].
*   **[[telemetry_and_monitoring_in_ai_data_centers | Monitoring and Visibility]]**: [[telemetry_and_monitoring_in_ai_data_centers | Visibility and telemetry]] are crucial for proactive problem detection before model failures occur [00:14:46].
    *   Networks can take snapshots of dropped packets (headers, RDMA info) to explain why they were dropped [00:17:06].
    *   An [[ai_in_it_infrastructure_management | AI agent]] running on [[gpu_and_server_configurations_for_ai | GPUs]] can communicate with switches via API to verify configuration (e.g., PFC/ECN) and provide [[gpu_and_server_configurations_for_ai | GPU]] statistics (packets sent/received, RDMA errors), helping correlate problems to either the [[gpu_and_server_configurations_for_ai | GPU]] or the network [00:17:36].
*   **Upgrades**: Smart system upgrade capabilities allow network switches to be upgraded without taking them offline, enabling [[gpu_and_server_configurations_for_ai | GPUs]] to continue working even during software updates [00:18:32].

## Future Trends
*   **Network Speeds**: The industry is rapidly moving from 800 gigabits today to 1.6 terabits per second by late 2024 or early 2027, driven by ever-larger models [00:14:25].
*   **Ultra Ethernet Consortium (UEC)**: This consortium is working to evolve Ethernet for AI workloads, focusing on improving congestion control, packet spraying, and NIC-to-NIC communication. Version 1.0 is expected to be ratified in Q1 2025, potentially shifting more functionality to Network Interface Cards (NICs) [00:21:23].

## Key Takeaways
*   **No Oversubscription**: The backend [[ai_network_infrastructure | AI network]] must have a 1:1 ratio because [[gpu_and_server_configurations_for_ai | GPUs]] utilize all available bandwidth [00:19:10].
*   **Simple Protocols**: BGP is a preferred, simple, and quick protocol for AI networks [00:19:29].
*   **Lossless Ethernet**: Essential for model training; RoCE (RoCEv2, ECN, PFC) implementations are crucial to prevent network melt-downs and provide early warnings [00:19:56].
*   **[[telemetry_and_monitoring_in_ai_data_centers | Visibility and Telemetry]]**: Constant [[telemetry_and_monitoring_in_ai_data_centers | monitoring]] is vital to identify and address network issues before they impact model completion times [00:20:09].
*   **Job Completion Time**: This is the primary metric for [[importance_of_infrastructure_design_for_ai_applications | AI network performance]]; significant increases in job completion time likely indicate a network problem [00:22:23].
*   **Synchronized GPUs**: All [[gpu_and_server_configurations_for_ai | GPUs]] operate in sync, sending and receiving data simultaneously. A slow [[gpu_and_server_configurations_for_ai | GPU]] creates a barrier that stops the entire process [00:22:15].