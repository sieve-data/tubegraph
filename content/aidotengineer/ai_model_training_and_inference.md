---
title: AI Model Training and Inference
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

## Overview
[[ai_models_and_training_methods | AI model training]] and [[inference_and_training_processes_in_luminal | inference]] are critical processes in the lifecycle of artificial intelligence models. Training involves feeding large datasets to a model to enable it to learn patterns and make decisions, while inference is the application of a trained model to new data to make predictions or generate outputs. Paul Gil, a tech lead for Arista Networks, explains the underlying infrastructure and networking considerations for these processes, highlighting the distinct demands of each [00:00:34].

## Training vs. Inference
The infrastructure requirements for training and inference differ significantly [00:01:36]. Historically, inference consumed a minimal amount of resources compared to training, but this has changed considerably with the advent of Chain of Thought and reasoning models [00:01:13]. Next-generation models, particularly large language models (LLMs), now demand substantial resources for inference [00:02:27].

For example, a model might require 248 GPUs for one to two months of training, but then only four H100 GPUs for inference after fine-tuning and alignment [00:02:05].

## AI Network Architecture
AI networks are purpose-built and typically completely isolated due to the high cost and power consumption of GPUs [00:02:45]. These networks are divided into two main components:

### Backend Network (Training)
This is where GPUs are interconnected. It's designed for high-speed, direct communication between GPUs, which are incredibly expensive and hard to acquire [00:02:48].
*   **GPU Configuration**: Typically, eight GPUs are grouped per server, which can be from vendors like Nvidia or Supermicro [00:03:03].
*   **Connectivity**: These servers connect to high-speed leaf and spine switches [00:03:10].
*   **Isolation**: No other network traffic is connected to this backend [00:03:16].
*   **Bandwidth**: GPUs operate at speeds up to 400 Gbps [00:03:39], a level of traffic density unprecedented in traditional enterprise data centers [00:03:46]. This requires a 1:1 network design with no oversubscription to ensure peak performance [00:07:21]. Upcoming B-series GPUs are expected to support 800 Gbps, with servers potentially generating 9.6 terabytes of traffic per server [00:08:03].
*   **Traffic Pattern**: Traffic within the backend network is predominantly "east-west" (GPU-to-GPU), as GPUs communicate with each other [00:11:18]. This traffic often runs at wire rate [00:11:31].
*   **Hardware**: An NVIDIA H100 server, for instance, has eight 400 Gbps GPU ports and four 400 Gbps Ethernet ports [00:04:30].

### Frontend Network (Storage and Data Ingestion)
This network handles data ingress for training models and connects to storage [00:03:20].
*   **Function**: GPUs synchronize, perform calculations, and then request more data, initiating a continuous cycle [00:03:26].
*   **Demands**: This network is less intense than the backend [00:03:34].
*   **Traffic Pattern**: Traffic is "north-south" (GPU-to-storage), which is calmer as storage vendors typically operate at 100-200 Gbps [00:11:22].

## Networking Challenges for AI
Building [[ai_implementation_and_best_practices | AI networks]] presents unique challenges:

*   **Hardware Differences**: GPUs are complex to configure compared to traditional servers [00:05:50].
*   **Software Protocols**: Networking teams must understand protocols like NVIDIA Collective Communications Library (NCCL) and CUDA, particularly how collectives operate to manage network traffic patterns [00:06:03].
*   **Application Behavior**: Unlike traditional data center applications that are resilient to single-point failures, if one GPU fails in an AI network, the entire training job might fail or require a restart, which is a different operational concept [00:06:44].
*   **Bursty Traffic**: Thousands of GPUs can burst traffic simultaneously at 400 Gbps, leading to massive network loads [00:07:03].
*   **Packet Loss**: Packet drops are generally acceptable up to a point, but excessive loss is detrimental [00:15:29]. Consistent latency is also crucial [00:15:34].
*   **Load Balancing**: Traditional load balancing methods using five-tuple entropy (IP, port, MAC address) can fail when GPUs use a single IP address, potentially oversubscribing a single uplink [00:08:37]. New methods are needed to balance based on bandwidth utilization [00:09:11].
*   **Reliability**: A single GPU failure can halt a model's progress [00:09:31]. Optics, transceivers, and cabling issues become significant with thousands of GPUs [00:09:45].
*   **Power and Cooling**:
    *   Standard data center racks (7-15 KW) cannot accommodate AI servers [00:10:21].
    *   An 8-GPU server can draw 10.2 KW, meaning only one such server can fit in a traditional rack [00:10:41].
    *   New racks must support 100-200 KW and require water cooling instead of air cooling [00:10:51].

## Solutions and Features
Advanced networking solutions are vital for robust [[ai_model_considerations | AI model considerations]] and performance:

*   **Congestion Control**: Networks need sophisticated congestion control mechanisms to prevent buffering and ensure efficient data flow [00:11:50].
    *   **RoCE v2 (RDMA over Converged Ethernet)**: Utilizes two primary components:
        *   **Explicit Congestion Notification (ECN)**: An end-to-end flow control where marked packets indicate congestion, prompting the receiver to tell the sender to slow down [00:12:16].
        *   **Priority Flow Control (PFC)**: A "stop" signal used when buffers are full, acting as an emergency brake [00:12:41].
    *   **Buffer Tuning**: Switches can adjust their buffers to specific packet sizes, which are consistent in AI models, optimizing expensive buffer commodities [00:16:15].
*   **Network Isolation**: AI networks are kept completely isolated from other enterprise networks (e.g., DMZ, firewalls, load balancers, internet connections) to maintain performance and security [00:13:12].
*   **Predictive Monitoring & Telemetry**:
    *   **RDMA Monitoring**: RDMA (Remote Direct Memory Access) is used for memory-to-memory writes [00:16:47]. Networks can capture snapshots of dropped packets, including headers and RDMA error codes, to diagnose issues [00:17:08].
    *   **AI Agent**: An agent on the GPU (via API and code) communicates with the network switch to verify configuration (e.g., PFC/ECN) and provide statistics on packets received/sent and RDMA errors, allowing correlation between GPU and network issues [00:17:36].
*   **Simple Protocols**: Using simple, fast protocols like BGP is recommended for AI networks [00:19:29].
*   **Advanced Load Balancing**: Newer techniques can balance loads based on the specific collective running on the GPUs, known as "cluster load balancing" [00:19:47].
*   **Smart System Upgrade**: Allows for upgrading switch software without taking the network offline, ensuring continuous operation for thousands of GPUs [00:18:47].
*   **Scalability**: Networks can scale from small setups to hundreds of thousands of GPUs, especially in cloud environments [00:05:32].

## Future Outlook
Networking technology for AI is evolving rapidly:
*   **Speed Increases**: Networks are currently at 800 Gbps, with 1.6 Tbps expected by late 2024 or early 2025 [00:19:40]. These speeds are crucial as [[evolution_of_ai_models_and_their_application | AI models]] continue to grow in size and complexity [00:19:40].
*   **Ultra Ethernet Consortium (UEC)**: This consortium aims to improve Ethernet for AI workloads by enhancing congestion control, packet spraying, and direct NIC-to-NIC communication [00:21:24]. Version 1.0 is expected to be ratified in Q1 2025 [00:21:41]. UEC pushes more intelligence into the NICs, allowing the network to focus on forwarding packets [00:21:56].

## Key Network Considerations for AI
*   **No Oversubscription**: The backend network must be 1:1, as GPUs utilize all available bandwidth [00:19:10].
*   **Efficient Addressing**: Point-to-point connections (e.g., /30 or /31 subnets) are crucial, with IPv6 as an option for addressing challenges [00:19:17].
*   **Robust Protocols**: BGP is preferred for its simplicity and speed [00:19:29].
*   **Multi-Tenancy (if applicable)**: EVPN-VXLAN can support multiple business units [00:19:36].
*   **RDMA/RoCE**: Essential for preventing network meltdown and providing early warning systems for congestion [00:19:56].
*   **Comprehensive Visibility and Telemetry**: Crucial for network operations centers to identify and resolve issues before they impact model training or inference [00:20:09].
*   **Job Completion Time**: The ultimate metric for AI networks, as network performance directly impacts how quickly AI tasks are finished [00:22:23].
*   **Model Checkpointing**: While models can checkpoint progress, this process is expensive [00:22:34].