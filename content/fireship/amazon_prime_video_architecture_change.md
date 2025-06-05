---
title: Amazon Prime Video architecture change
videoId: qQk94CjRvIs
---

From: [[fireship]] <br/> 

Amazon Prime Video recently published an article detailing how they significantly reduced their [[aws_cloud_computing_solutions | Amazon Web Services]] (AWS) bill by re-architecting a component from a serverless microservices setup to a traditional monolith. This change resulted in a 90% cost saving for that particular service, amounting to millions of dollars for a product of Prime Video's scale <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.

## The Serverless Debate

The announcement sent "shockwaves" through the tech industry because a core promise of the serverless model is more efficient infrastructure scaling, which theoretically should lead to lower costs <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. Amazon itself was an early pioneer of serverless technology with its Lambda functions <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Today, many platforms like Vercel and Netlify offer serverless services, often by reselling [[overview_of_aws_services | AWS services]] <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. An entire industry of startups and open-source projects, such as the Serverless Framework and SST, have emerged to simplify the use of AWS <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>.

Despite its popularity, the "serverless" concept has been called the "biggest lie in the history of computers" because users are still relying on servers; they just don't own them <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Prominent figures like DHH, creator of Ruby on Rails and Basecamp, have long advocated for "majestic monoliths" <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. Basecamp famously moved off the cloud after spending over $3 million in one year, opting to run their own servers <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. Similarly, successful startups like Dropbox have left the cloud once they reached a certain size <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Prime Video's Serverless Microservices Architecture

Prime Video's case involved a tool designed to analyze audio content for issues like video freeze and corruption, contributing to the [[development_of_video_content_using_ai_technology | development of video content]] <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. Initially, this tool was built using a serverless microservices architecture, specifically multiple Step Functions (similar to Lambda functions) to handle different responsibilities <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

The process involved:
1.  An initial entry point <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
2.  A service for file conversion, transforming audio/video streams into frames <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
3.  Multiple detectors utilizing [[aws_machine_learning_tools | machine learning]] to analyze the video frames <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
4.  A final function to aggregate results and store them in an [[aws_storage_and_databases | S3 bucket]] <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

### Bottlenecks and Costs

The distributed nature of this architecture led to significant overhead. Every time data was passed between services, it required serialization and deserialization, as well as network communication <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. Since the service needed to run multiple times for every second of a video stream, these overheads quickly became a bottleneck, especially due to hitting account limits for orchestrating the service <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>. Additionally, temporarily uploading files to S3 for processing incurred substantial costs related to data access <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Prime Video concluded that the distributed architecture was the root cause of these issues <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

## Transition to a Monolith Architecture

Based on their findings, Prime Video made the "bold decision" to re-architect the component into a monolith <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Instead of decoupled, distributed services, all components were consolidated to run on a single container <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

Key characteristics of the new monolith:
*   All components remained the same, but now ran on a single server <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.
*   Scaling shifted from horizontal (adding more instances of individual services) to vertical (making the single server larger to handle more work) <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

This change, while seemingly a drawback in terms of scaling flexibility, eliminated all unnecessary communication and network usage between services <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. This optimization led directly to the 90% cost reduction for this specific service <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

## Broader Implications: Tradeoffs in Cloud Architecture

The Prime Video case highlights that there are no universal solutions in [[tradeoffs_in_cloud_architecture | cloud architecture]], only tradeoffs <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. While a monolith proved beneficial for Prime Video's specific use case, it's not always the answer. Famously, Netflix transitioned from a monolith to hundreds of microservices after a massive failure in 2008 <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. This allowed them to achieve independent scaling and fault tolerance, which is crucial for a service where downtime could cost millions in lost memberships <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

For smaller projects, [[serverless_architecture_critique | serverless architecture]] can still be a "game-changer" for rapid deployment without needing to manage infrastructure, often staying within free tiers <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. The peace of mind that comes with knowing a single bug won't bring down an entire operation can be well worth the cost <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.