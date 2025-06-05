---
title: Designing AI Networks and Data Centers
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

Paul Gil, a tech lead for Arista Networks based in New York City, designs and helps build Enterprise networks, focusing on the underlying "plumbing" for AI infrastructure rather than agents. His work involves understanding how models are trained, what the infrastructure looks like, and how inferencing is performed <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Training vs. Inference
Historically, when building computer networks, terms like "job completion time" and "barrier" were common <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The distinction between training and inference has evolved significantly with Chain of Thought and reasoning models <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Dr. Wes Sousa developed a concept illustrating the difference in GPU size requirements: training might require 18 times the resources, while inference might require 2 times, though this is changing with Chain of Thought and reasoning <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. For example, a model trained with 248 GPUs for one to two months might only need four H100s for inference after fine-tuning and alignment <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. While LLMs used to be small for inference, next-generation models require a lot more resources <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## AI Network Architecture
AI networks are built with new terminology for networking professionals <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. They typically consist of two main parts:

### Backend Network
This network connects GPUs <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Due to the high cost, power consumption, and scarcity of GPUs, these networks are completely isolated from other systems <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
- Servers typically have eight GPUs (e.g., Nvidia, Supermicro) per pool <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
- GPUs connect to a high-speed leaf switch, which then connects to a spine switch, forming a dedicated network with nothing else attached <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
- The backend network is highly intense; GPUs can work at 400 GB/s depending on the model being trained <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
- Networking for AI is simplified, using basic protocols like IB BGP or EBGP to ensure maximum uptime <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Frontend Network
This network handles storage access for the model <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. GPUs synchronize, calculate, produce an algorithm, and then request more data, forming a continuous cycle <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The frontend network is less intense than the backend <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## [[challenges_in_building_ai_applications | Challenges in Building AI Applications]] and Networks
Designing AI networks presents unique [[challenges_in_building_ai_applications | challenges]] compared to traditional data center networks <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Hardware Differences
- GPUs are unfamiliar hardware for many networking professionals; configuring them can take hours <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
- An H100 server, a popular AI server, has eight 400 gig GPU ports and four 400 gig Ethernet ports <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Such servers can generate unprecedented traffic loads, e.g., 4.8 terabytes from a single H100 <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
- Nvidia servers (like the DGX or HGX) come with a fixed number of GPUs (typically eight) and cannot be "scaled up" by adding more, though networks can be "scaled out" to add more GPUs over time <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Software and Protocols
- Cuda and Nickel are key protocols <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Networking teams need to understand Nickel's "collective" operations as they impact network traffic patterns <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

### Traffic Patterns
- Unlike typical data center applications (web/database) where traffic goes between different parts and can fail over, AI networks involve GPUs communicating directly <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. If one GPU fails, the entire job might fail <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
- AI network traffic is extremely bursty <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Thousands of GPUs can burst simultaneously at 400 gig, creating massive network load <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
- Traditional load balancing using entropy (five-tuple: IP address, port, MAC address) is insufficient for GPU traffic as it often uses a single IP address, potentially oversubscribing a single uplink <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

### Power and Cooling
- AI racks require significantly more power than traditional data center racks <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. An average rack is 7-15 KW, but a single AI server with 8 GPUs draws 10.2 KW <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
- New data centers are being built with racks supporting 100-200 KW, often requiring water cooling instead of air cooling <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### Traffic Direction
- Traditional data centers primarily have "north-south" traffic (user to database/web) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
- AI networks exhibit both "east-west" traffic (GPUs speaking to each other at wire rate) and "north-south" traffic (requesting data from storage) <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. East-west traffic is particularly intense <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

### Network Resiliency and Failures
- A single GPU failure can stop the model, unlike typical applications where components can fail over <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
- Problems with optics, transceivers, DOMs (rates, loss), and cables are common in networks with thousands of GPUs <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

## Solutions and Best Practices
To address these [[challenges_and_strategies_in_ai_production | challenges and strategies in AI production]], specific design principles and technologies are employed.

### Network Design Principles
- **Isolation:** AI networks are designed to be completely isolated from other parts of the enterprise network to protect expensive GPU resources <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
- **No Over-Subscription:** Networks are built "one to one" rather than oversubscribed (e.g., 1 to 10 or 1 to 3), ensuring maximum bandwidth for bursty GPU traffic <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
- **Simple Protocols:** Using simple routing protocols like BGP is recommended for efficiency and speed <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
- **Advanced Load Balancing:** To handle GPU traffic from a single IP, advanced load balancing techniques are used that monitor bandwidth utilization on uplinks <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. This can achieve up to 93% utilization across uplinks <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
- **Tuned Buffering:** Switches are configured with buffers specifically tuned to the packet sizes sent and received by models, optimizing expensive buffering resources <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

### Congestion Control
- **Rocky V2 (RDMA over Converged Ethernet v2):** This protocol is essential for AI networks to prevent meltdowns <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
    - **Explicit Congestion Notification (ECN):** An end-to-end flow control mechanism where congested network paths mark packets, signaling the receiver to tell the sender to slow down <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
    - **Priority Flow Control (PFC):** A "stop" mechanism used when buffers are full, preventing further packet transmission <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
- **Lossless Ethernet:** While some packet drops might be acceptable, maintaining flow control and lossless Ethernet with ECN and PFC is crucial to avoid significant issues that can slow down synchronized GPUs <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Monitoring and Visibility
- **RDMA Monitoring:** Networks should monitor RDMA (Remote Direct Memory Access) errors, which is a complex protocol with many error codes <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>. This allows for identifying network problems like packet drops by capturing packet headers and RDMA information <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
- **AI Agent:** An AI agent (API and code) can be loaded onto GPUs to communicate with switches, verifying correct flow control configuration (PFC, ECN) and providing statistics on packets sent/received and RDMA errors. This helps correlate issues to either the GPU or the network <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
- **Proactive Awareness:** Telemetry and visibility are crucial for the Network Operations Center to be aware of potential problems before receiving calls about failed models <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

### Smart System Upgrades
- Network device software can be upgraded without taking switches offline, even in large clusters with thousands of GPUs and dozens of switches. This ensures continuous GPU operation <a class="yt-timestamp" data-t="00:18:32">[00:18:32]</a>.

## Future Outlook
- Network speeds are rapidly advancing: currently at 800 gig, with 1.6 terabytes expected by the end of 2024 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. Models will continue to grow and consume more bandwidth <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
- **Ultra Ethernet Consortium:** A new initiative aiming to redefine Ethernet for better congestion control, packet spraying, and direct NIC-to-NIC communication. Version 1.0 is expected to be ratified in Q1 2025, with deployments in Q3/Q4 2025 <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>. This will shift more functionality to NICs, allowing the network to focus on forwarding packets <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

## Summary
AI networks are distinct from traditional data center networks, requiring specialized design due to their unique characteristics <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>. The backend network is critical and highly bursty, with synchronized GPUs sending and receiving at the same time <a class="yt-timestamp" data-t="00:22:09">[00:22:09]</a>. A slow GPU can act as a barrier, impacting overall job completion time <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. While models can checkpoint, this is an expensive process <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. Implementing Rocky (ECN/PFC) and ensuring comprehensive visibility and telemetry are crucial for maintaining network health and proactive problem resolution <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.