---
title: Cost savings with monolith architecture
videoId: qQk94CjRvIs
---

From: [[fireship]] <br/> 

The notion that [[serverless_architecture_critique | serverless]] architectures inherently lead to cost efficiency has been challenged by real-world experiences. A notable example is Amazon Prime Video, which reported significant savings by transitioning from a [[microservices_vs_monoliths | microservices]] approach back to a [[microservices_vs_monoliths | monolith]] architecture <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Amazon Prime Video's Experience

In May 2023, Amazon Prime Video published an article detailing how they saved 90% on their Amazon Web Services (AWS) bill <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This massive reduction was achieved by migrating an audio-video monitoring service from a [[serverless_architecture_critique | serverless]] [[microservices_vs_monoliths | microservices]] setup to an "Old-Fashioned" [[microservices_vs_monoliths | monolith]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This revelation sent "shockwaves" through the tech industry, as a core promise of the [[serverless_architecture_critique | serverless]] vision is efficient scaling and lower costs <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### The Problem with Distributed Architectures

The service in question was designed to analyze audio content for issues like video freeze and corruption <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Its initial implementation utilized multiple [[serverless_architecture_critique | serverless]] functions, specifically AWS Step Functions (similar to Lambda), each handling different responsibilities <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This process involved:
*   An initial entry point triggering a file conversion service to turn audio/video streams into frames <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   Multiple machine learning detectors analyzing the video <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   A final function to aggregate results and store them <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

The overhead of passing data between these [[microservices_vs_monoliths | microservices]] became a significant issue <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Each data transfer required serialization and deserialization, and communication over a network <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Since this service needed to run multiple times per second of video, it quickly encountered bottlenecks due to account limits for orchestrating services <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Additionally, temporarily uploading files to S3 buckets for inter-service communication led to high costs for file access <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

The distributed nature of the architecture was identified as the root cause of these bottlenecks and excessive costs <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### The Monolith Solution

Amazon Prime Video made the "bold decision" to re-architect their service into a [[microservices_vs_monoliths | monolith]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Instead of decoupled, distributed services, all components were consolidated to run on a single container <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. While the core components remained the same, running them on a single server meant scaling could only occur vertically (making each server bigger) rather than horizontally (creating more services for individual components) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

This shift, despite seemingly limiting scaling options, eliminated "unnecessary communication and network usage" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. This simplification directly led to the 90% cost reduction, saving millions of dollars for a product of Prime Video's scale <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Other Examples and Considerations

This trend is not isolated. DHH, the creator of Ruby on Rails and Basecamp, has been a long-time advocate for "Majestic [[microservices_vs_monoliths | monoliths]]" <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. His company moved entirely off the cloud after spending over three million dollars in one year, opting to run their own servers instead <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Similarly, successful startups like Dropbox have chosen to leave the cloud once they reach a certain scale <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

However, the choice between [[microservices_vs_monoliths | microservices]] and [[microservices_vs_monoliths | monoliths]] involves significant [[tradeoffs_in_cloud_architecture | tradeoffs]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. For example, Netflix famously transitioned from a [[microservices_vs_monoliths | monolith]] to hundreds of [[microservices_vs_monoliths | microservices]] after a massive failure in 2008 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This shift allowed them independent scaling with fault tolerance, which, despite being potentially more complex and expensive, prevents even greater losses from downtime <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

For smaller projects or businesses, [[serverless_architecture_critique | serverless]] can still be a valuable tool, offering quick deployment without needing to manage infrastructure and often staying within free tiers <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The peace of mind from not having a bad code deployment take down an entire operation can outweigh the costs <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Ultimately, there are "no solutions, only [[tradeoffs_in_cloud_architecture | trade-offs]]" in cloud architecture <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.