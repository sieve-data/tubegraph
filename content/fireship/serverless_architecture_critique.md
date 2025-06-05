---
title: Serverless architecture critique
videoId: qQk94CjRvIs
---

From: [[fireship]] <br/> 

"Serverless" is considered by some to be a misnomer, as it still utilizes servers; they are simply not managed by the user directly <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. The core premise of the serverless vision is the promise of more efficient infrastructure scaling, theoretically leading to lower costs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Amazon Prime Video's Experience

Amazon Prime Video published an article detailing how they achieved a 90% reduction in their Amazon Web Services (AWS) bill by transitioning from [[microservices_vs_monoliths | serverless microservices]] to an "Old-Fashioned" [[microservices_vs_monoliths | monolith architecture]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This revelation caused significant discussion in the tech community, especially since Amazon was an early pioneer of serverless technology with Lambda functions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### The Initial Serverless Implementation

To analyze audio content for issues like video freeze and corruption, Prime Video initially developed a tool using multiple serverless functions, specifically AWS Step functions and Lambda functions <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This [[microservices_vs_monoliths | microservices]] approach involved several steps:
*   An entry point initiating a file conversion service <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   Conversion of audio/video streams into frames for detector use <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Multiple machine learning detectors analyzing the video <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
*   A final function to aggregate results and store them in an S3 bucket <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Bottlenecks and Costs

The distributed [[microservices_vs_monoliths | architecture]] led to several problems:
*   **Communication Overhead** Passing data between services required serialization and deserialization, along with network communication, creating overhead <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Account Limits** The service needed to run multiple times for every second of a video stream, quickly hitting account limits related to service orchestration <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   **Storage Costs** Temporarily uploading files to S3 incurred significant costs due to file access in the buckets <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

The distributed architecture was identified as the root cause of these bottlenecks <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### The Monolith Solution

Prime Video made the "bold decision" to re-architect to a [[microservices_vs_monoliths | monolith]] <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Instead of decoupled, distributed services, all components were consolidated to run on a single container <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. While the components remained the same, running on a single server meant they could only scale vertically (requiring bigger servers for more work), unlike the horizontal scaling of [[microservices_vs_monoliths | microservices]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This change eliminated unnecessary communication and network usage, resulting in a 90% [[cost_savings_with_monolith_architecture | cost reduction]] <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, saving millions of dollars <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Broader Critiques and Alternatives

Not everyone is fully convinced by the serverless model.
*   **DHH's "Majestic Monoliths"** David Heinemeier Hansson (DHH), creator of Ruby on Rails and Basecamp, has advocated for "Majestic Monoliths" for over a decade <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. His company, Basecamp, moved entirely off the cloud after spending over three million dollars in one year, opting to run their own servers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Companies Leaving the Cloud** Successful startups like Dropbox have also moved away from cloud services once they reached a sufficient size <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## The Case for Serverless (Despite Drawbacks)

Despite the critiques, serverless architecture remains popular and beneficial for many use cases:
*   **Ease of Use for Small Projects** For individual projects, serverless can be an "absolute game changer" for getting things done quickly <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It allows developers to deploy code without needing to consider infrastructure <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Cost-Effectiveness for Low Usage** Many users can operate within free tiers, making it a cost-effective option <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Risk Mitigation** For small businesses, serverless provides peace of mind, as a deployment of bad code is less likely to take down an "entire operation" compared to a monolith <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Ecosystem Support** An entire industry of startups and open-source projects (like the Serverless framework and SST) exists to simplify the use of AWS services <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Additionally, platforms like Vercel and Netlify offer serverless services by reselling AWS services <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Conclusion: No Solutions, Only Trade-offs

The decision between [[microservices_vs_monoliths | microservices]] (often associated with serverless) and [[microservices_vs_monoliths | monoliths]] depends heavily on the specific context and needs.
*   **Netflix's experience** In 2008, Netflix experienced a "massive failure" with its monolith [[microservices_vs_monoliths | architecture]], which led them to restructure into hundreds of [[microservices_vs_monoliths | microservices]] that could scale independently and offer fault tolerance <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. While more complex and potentially expensive, a few hours of downtime for Netflix would cost significantly more in lost memberships <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

> [!INFO] Key Takeaway
> "When it comes to [[tradeoffs_in_cloud_architecture | Cloud architecture]] there are no solutions, only [[tradeoffs_in_cloud_architecture | trade-offs]]" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.