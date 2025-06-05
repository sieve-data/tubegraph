---
title: Microservices vs monoliths
videoId: qQk94CjRvIs
---

From: [[fireship]] <br/> 

The choice between microservice and monolith architectures is a significant decision in software development, with each approach presenting distinct advantages and disadvantages, particularly concerning [[Cost savings with monolith architecture | cost]] and scalability <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Serverless Microservices Explained

"Serverless" is a term used to describe an architecture where developers do not directly manage servers; instead, they utilize services where the server infrastructure is handled by a third party <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While it's called "serverless," servers are still in use, just not directly owned or managed by the user <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

Key characteristics and industry context:
*   **Pioneering:** Amazon Web Services (AWS) was an early pioneer of serverless with Lambda functions <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Industry Adoption:** Many platforms, like Vercel and Netlify, offer serverless services, often by reselling AWS services <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Support Ecosystem:** An entire industry of startups and open-source projects (e.g., Serverless Framework, SST) exists to simplify AWS usage <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Scaling Theory:** A main claim of the serverless vision is that it allows for more efficient infrastructure scaling, theoretically leading to lower costs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Personal Use Cases:** For individual developers or small projects, serverless can be a "game-changer" for rapid development without needing to manage infrastructure <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. It can often stay within free tiers, providing peace of mind against deploying bad code that could take down an entire operation <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. However, there's a risk of accidentally creating infinitely scaling infinite loops that could incur significant costs <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

## Amazon Prime Video's Experience

Amazon Prime Video shared an article detailing their significant [[Cost savings with monolith architecture | cost savings]] by re-architecting their video monitoring service <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

### Initial Microservice Architecture
Prime Video developed a tool to analyze audio content for issues like video freeze and corruption <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. This tool was initially built using multiple serverless functions, specifically AWS Step Functions and Lambda <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

The process involved:
1.  An initial entry point <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
2.  A service to convert audio/video streams into frames <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.
3.  Multiple machine learning detectors to analyze the video frames <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
4.  A final function to aggregate results and store them in an S3 bucket <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

### Challenges with Microservices
The distributed architecture led to several issues for Prime Video:
*   **Overhead:** Every time data was passed between services, it required serialization and deserialization, and communication over a network <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>.
*   **Bottlenecks:** The service needed to run multiple times per second of video stream, quickly hitting account limits for orchestrating the services <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   **Cost:** Temporarily uploading files to S3 incurred significant costs just from accessing these files <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.

The distributed architecture was identified as the root cause of these bottlenecks <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>.

### Transition to Monolith Architecture
Prime Video made the decision to re-architect their system to a monolith <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Instead of decoupled, distributed services, all components were made to run on a single container <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

*   **Scaling:** In a monolith, scaling is primarily vertical, meaning individual servers need to be made larger to handle more work <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This contrasts with microservices, which can scale horizontally by creating more instances of individual components based on their specific needs <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   **Benefits:** This change eliminated unnecessary communication and network usage <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **Results:** The re-architecture resulted in a 90% reduction in costs, saving millions of dollars for a product of Prime Video's magnitude <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Broader Perspectives and [[Tradeoffs in cloud architecture | Tradeoffs]]

While Prime Video's success story with a monolith is notable, it doesn't mean microservices are inherently bad <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. There are different perspectives and scenarios where each architecture excels.

*   **"Majestic Monoliths":** David Heinemeier Hansson (DHH), creator of Ruby on Rails and Basecamp, has advocated for "Majestic Monoliths" for a decade <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. Basecamp moved its entire company off the cloud after spending over $3 million in one year, now running their own servers <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.
*   **Leaving the Cloud:** Other successful startups, like Dropbox, have also opted to leave cloud providers once they reach a certain size <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Netflix's Journey:** Famously, in 2008, Netflix experienced a massive failure while based on a monolith architecture <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>. This incident motivated them to break their architecture into hundreds of microservices, allowing for independent scaling and fault tolerance <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. While potentially more complex and expensive, downtime for Netflix would cost significantly more in lost memberships <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

Ultimately, when it comes to cloud architecture, there are no universal solutions, only [[Tradeoffs in cloud architecture | tradeoffs]] <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. The optimal choice depends on the specific needs, scale, and priorities of the project or organization.