---
title: The excess capacity myth in AWS origin story
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

The origin of Amazon Web Services (AWS) is often attributed to four distinct narratives, one of the most widespread but untrue being the "excess capacity narrative" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This story suggests that AWS emerged from Amazon's need to monetize its idle computing infrastructure during off-peak seasons <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## The Myth Explained

Around 2001-2003, Amazon.com's retail business was highly seasonal, experiencing immense spikes in traffic and demand during Q4 (the holiday shopping season) <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. To handle this peak, Amazon had to build out significant technical infrastructure <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. The myth posits that for the rest of the year, this capacity sat unused, leading Amazon to a "brilliant realization" to rent it out to other developers, transforming a cost into a revenue stream <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. During these peak periods, Amazon's culture reflected this intensity, with rules prohibiting new code commits in November and December <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a> and even executive teams working in warehouses <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Debunking the Myth

The "excess capacity myth" falls apart for two primary reasons: technical feasibility in a pre-cloud era and fundamental business logic <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Technical Implausibility

In the early 2000s, technology companies operated very differently than in the modern cloud era.
*   **Monolithic Systems**: Pre-cloud infrastructure was highly customized and tightly coupled to specific applications <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Amazon.com's codebase was directly installed on proprietary servers, such as high-margin DEC Alpha servers <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Lack of Virtualization**: It was not possible to simply "rent out" unused capacity because systems weren't designed for multi-tenancy, security isolation, or easy application deployment by external users <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Shift to Open Source**: The move to Linux and open source was a critical development, allowing companies to build infrastructure on commodity hardware instead of expensive, bundled hardware-software platforms <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This shift helped [[importance_of_linux_and_open_source_for_aws_development | save Amazon]] financially during a cash-tight period around 2000 <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, as they rewrote Amazon.com to run on Linux and HP servers <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. However, this was about cost efficiency, not creating virtualized cloud servers for rent <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Business and Strategic Inconsistencies

*   **Service Reliability**: If AWS were built on excess capacity, Amazon would have to deny service to its customers (e.g., Netflix) during its own Q4 peak, which is an untenable business model for a critical infrastructure provider <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Amazon's View of Technology**: Amazon never viewed technology as a mere "cost center" or an IT department <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. They always considered themselves a technology company, viewing technological advancements as investments and opportunities for new ventures <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Intentional Strategy**: The myth "short sells Amazon" <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a> by implying AWS was an accidental byproduct. In reality, [[amazon_and_aws_business_strategy_intentions | AWS was an incredibly intentional strategy]], a "brand new business school case study type laser focus on an emerging market" <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

## Official Refutation

The most definitive debunking of the myth comes from Werner Vogels, the CTO of Amazon, who stated in a 2011 Quora post:
> "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually, within two months after launch, AWS would have already burned through the excess Amazon.com capacity... Amazon Web Services was always considered a business by itself with the expectation that it could even grow as big as the amazon.com retail operation." <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>

The [[the_evolution_of_amazon_web_services_from_amazoncom | evolution of Amazon Web Services]] was a deliberate strategic move, not an opportunistic disposal of idle hardware.