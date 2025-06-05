---
title: Luminal Cloud and Serverless Implementation
videoId: 0uj9lMI-sIo
---

From: [[aidotengineer]] <br/> 

Luminal Cloud is an offering designed to provide a straightforward and highly optimized cloud experience for Machine Learning (ML) inference workloads <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>. It aims to be the "simplest, fastest ML cloud in the world" <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

## How Luminal Cloud Works

The foundation of Luminal Cloud relies on Luminal's ability to represent ML models as graphs <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a> <a class="yt-timestamp" data-t="00:23:11">[00:23:11]</a>. Users can:
1.  Work on a model within the Luminal framework <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.
2.  Export the model graph using `graph.export` to obtain a file <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>.
3.  Upload that file to Luminal Cloud <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
4.  Receive a [[role_of_serverless_platforms_in_ai | serverless]] inference endpoint <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.

Luminal Cloud handles all subsequent processes automatically <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.

> [!INFO] Simplification through Graphs
> The ability to represent ML models as directed acyclic graphs of operations is a core aspect of Luminal's design, enabling extreme simplicity in the library itself (under 5,000 lines of code) <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a> <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. This simplification is also leveraged for cloud deployment.

## Serverless Implementation

Luminal Cloud is built with a [[role_of_serverless_platforms_in_ai | serverless]] architecture <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>. This means users only pay for the time their graph is actively executing <a class="yt-timestamp" data-t="00:23:32">[00:23:32]</a>.

> [!QUOTE] "It's totally serverless. You only pay for when your graph is actually executing." <a class="yt-timestamp" data-t="00:23:30">[00:23:30]</a>

### Automated Management
Luminal Cloud automates several critical aspects of ML deployment:
*   **Optimization:** The platform handles [[cost_and_latency_optimization_in_ai_deployments | optimization]] of the deployed models <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.
*   **Batching and Queuing:** It manages batching and queuing of inference requests <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
*   **Machine Provisioning:** The provisioning of machines for inference is fully automated <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.

This automated approach aims to deliver the "simplest, fastest, most straightforward cloud experience out there" <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.