---
title: Telemetry and monitoring in AI data centers
videoId: 3j1dHivahFQ
---

From: [[aidotengineer]] <br/> 

[[ai_data_center_design_and_challenges | AI data centers]] require advanced telemetry and monitoring to ensure optimal performance and minimize downtime, especially given the high cost and criticality of the hardware involved <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. The objective is to proactively identify network issues before they impact [[cost_and_efficiency_in_deploying_ai_systems | AI model]] training or inference <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

## Importance of Visibility and Telemetry

Visibility and telemetry are crucial in [[ai_data_center_design_and_challenges | AI data centers]] for several reasons:
*   **Proactive Problem Solving** Network operations centers (NOCs) and operations centers aim to be aware of problems before developers call about [[importance_of_evaluation_and_metrics_in_ai_systems | model]] failures <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>, <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>.
*   **High Costs and Criticality** GPUs are extremely expensive, consume significant power, and are hard to obtain <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Ensuring they run 24/7 is paramount to maximize return on investment <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

## Key Monitoring Techniques

### RDMA Error Codes and Packet Dropping Analysis
[[importance_of_infrastructure_design_for_ai_applications | AI networks]] often use RDMA (Remote Direct Memory Access) for memory-to-memory writes, bypassing the CPU <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>, <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. RDMA is a complex protocol with numerous error codes <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

For monitoring, when the network encounters congestion and starts dropping packets, it can:
*   Copy the dropped packet to a buffer <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   Send only the headers <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>.
*   Provide the reason for the packet drop, including any RDMA information <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>, <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.
This detailed analysis helps pinpoint network issues <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### [[ai_in_it_infrastructure_management | AI Agent]] for GPU-Network Correlation
A specialized [[ai_in_it_infrastructure_management | AI agent]] provides crucial visibility into GPU performance and its interaction with the network <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. From a networking perspective, it's challenging to gain insights directly into the [[gpu_and_server_configurations_for_ai | GPUs]] <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

This agent, an API with code loaded onto the [[gpu_and_server_configurations_for_ai | GPUs]], communicates directly with the network switches <a class="yt-timestamp" data-t="00:17:45">[00:17:45]</a>, <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. Its functions include:
1.  **Configuration Verification** The agent verifies that flow control mechanisms (like PFC and ECN) are correctly configured between the [[gpu_and_server_configurations_for_ai | GPU]] and the switch. Incorrect configuration can lead to network disaster <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
2.  **Statistical Reporting** It provides statistics on packets received, packets sent, RDMA errors, and other RDMA issues <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.
This allows for correlation between [[gpu_and_server_configurations_for_ai | GPU]] and network problems, significantly improving troubleshooting <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

## Network Design Considerations for Monitoring

### Lossless Ethernet and Flow Control
For [[scaling_ai_solutions_in_production | AI networks]], lossless Ethernet is key, as dropping too many packets can be detrimental to [[importance_of_evaluation_and_metrics_in_ai_systems | model training]] <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. Constant latency is also important <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. Flow control mechanisms are vital to maintain network health:
*   **ECN (Explicit Congestion Notification)** Provides end-to-end flow control. When network congestion occurs, packets are marked, signaling the receiver to notify the sender to slow down. The sender then pauses and gradually speeds up if no more ECN packets are received <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.
*   **PFC (Priority Flow Control)** Acts as an emergency stop. If switch buffers are full, PFC signals the sender to halt traffic completely <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
Because [[gpu_and_server_configurations_for_ai | GPUs]] synchronize, a slowdown on one [[gpu_and_server_configurations_for_ai | GPU]] can impact the entire collective, highlighting the need for effective flow control and managing oversubscription <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>.

### Buffer Management
Network switches need to manage buffers effectively <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Buffering is costly, but tuning buffers to accept specific packet sizes, which are often consistent in [[ai_in_it_infrastructure_management | AI model]] training, can optimize resource allocation <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

### Network Isolation and Simplicity
[[enterprise_ai_within_security_boundaries | AI networks]], particularly the backend networks connecting [[gpu_and_server_configurations_for_ai | GPUs]], are typically kept completely isolated. This is due to the high cost of [[gpu_and_server_configurations_for_ai | GPUs]] and the need to prevent interference <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>, <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. Simple network protocols like IBGP or EBGP are preferred for their efficiency and speed <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Unlike traditional data centers with firewalls and load balancers, [[ai_data_center_design_and_challenges | AI networks]] are usually direct and purpose-built <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

## Future Developments

Network speeds are rapidly increasing, with 800 gigabits per second (Gbps) currently supported and 1.6 terabits per second (Tbps) expected by late 2024 or early 2027 <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>, <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>. The Ultra Ethernet Consortium is working on refining Ethernet for [[ai_data_center_design_and_challenges | AI workloads]], focusing on improved congestion control and efficient packet handling <a class="yt-timestamp" data-t="00:21:23">[00:21:23]</a>.