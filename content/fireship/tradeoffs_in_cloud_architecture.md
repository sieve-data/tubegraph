---
title: Tradeoffs in cloud architecture
videoId: qQk94CjRvIs
---

From: [[fireship]] <br/> 
This article is based on the Code Report from May 6, 2023 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Tradeoffs in Cloud Architecture

Cloud architecture involves significant [[Understanding and choosing a tech stack | tradeoffs]], with no single solution fitting all needs <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. Recent discussions highlight the complexities of choosing between microservices and monolith architectures, particularly regarding cost and scalability.

### The "Serverless Lie" and Cost Implications

The concept of [[Serverless architecture critique | serverless]] computing is contentious, with some critics labeling it "the biggest lie in the history of computers" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. While seemingly "serverless," it simply means you're using someone else's server, not your own <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The core claim of the [[Serverless architecture critique | serverless]] vision is efficient infrastructure scaling, which theoretically should reduce costs <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

Many platforms, like Vercel and Netlify, offer [[Serverless architecture critique | serverless]] services, often reselling [[AWS cloud computing solutions | AWS services]] behind the scenes <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. An entire industry of startups and open-source projects (e.g., the Serverless framework, SST) aims to make [[AWS cloud computing solutions | AWS]] easier to use <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### Amazon Prime Video's Monolith Re-Architecture

Amazon Prime Video published an article detailing how they achieved significant [[Cost savings with monolith architecture | cost savings]] by shifting from [[Serverless architecture critique | serverless]] microservices to a traditional monolith architecture <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This move saved them 90% on their [[AWS cloud computing solutions | Amazon Web Services]] bill <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This transparency is notable, as Amazon is a pioneer in [[Serverless architecture critique | serverless]] with [[Overview of AWS services | Lambda functions]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

Prime Video needed a tool to analyze audio content for issues like video freeze and corruption <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Initially, they used multiple [[Serverless architecture critique | serverless]] functions, specifically [[Overview of AWS services | Step functions]] (similar to [[Overview of AWS services | Lambda]]), to handle different responsibilities:
*   An entry point <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
*   File conversion from audio/video streams into frames <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
*   Multiple machine learning detectors to analyze video <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
*   A function to aggregate results and store them in an [[AWS storage and databases | S3]] bucket <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>

However, this distributed architecture incurred significant overhead <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Data transfer between services required serialization and deserialization and communication over a network <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The service needed to run multiple times per second of video, quickly hitting [[Managing cloud billing alerts and expenses | account limits]] for orchestration <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Additionally, temporary file uploads to [[AWS storage and databases | S3]] led to high costs from accessing files in buckets <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Recognizing the distributed architecture as the root cause of these bottlenecks, they re-architected to a monolith <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. All components were consolidated to run on a single container <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. While this limited scaling to vertical (making individual servers bigger) rather than horizontal (scaling individual components), it eliminated unnecessary communication and network usage <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This optimization led to a 90% [[Cost savings with monolith architecture | cost reduction]], saving millions of dollars for a product of Prime Video's scale <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Contrasting Perspectives

Not everyone embraces the cloud or [[Serverless architecture critique | serverless]]. David Heinemeier Hansson (DHH), creator of Ruby on Rails and Basecamp, has advocated for "majestic monoliths" for a decade <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Basecamp moved their entire operation off the cloud after spending over three million dollars in one year, now running their own servers <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Similarly, successful startups like Dropbox eventually leave the cloud once they reach a certain size <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

However, [[Serverless architecture critique | serverless]] can be a "game changer" for personal projects, enabling quick development without infrastructure concerns <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. The presenter noted rarely exceeding the free tier, finding it a worthwhile investment for peace of mind, despite the risk of accidentally creating infinitely scaling loops that could [[Managing cloud billing alerts and expenses | cost an infinite amount of money]] <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

Conversely, Netflix famously switched from a monolith to hundreds of microservices after a massive failure in 2008 <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This allowed them to scale independently with fault tolerance <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While more complex and expensive, a few hours of downtime for Netflix would result in greater losses from lost memberships than the additional infrastructure cost <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.