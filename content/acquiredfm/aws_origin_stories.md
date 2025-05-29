---
title: AWS origin stories
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

There are four distinct origin stories identified for [[amazon_web_services_aws | AWS]], each offering important insights into what [[amazon_web_services_aws | AWS]] is, as well as [[Amazons founding and early years | Amazon]] and its culture <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The "Excess Capacity" Narrative (A Myth)

The first and most commonly believed origin story, particularly among laypersons, is the "excess capacity narrative" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This story suggests that around 2001-2003, Amazon.com, being a highly seasonal retail business with huge spikes in traffic and demand during Q4 (the holiday shopping season), had a brilliant realization <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

The narrative claims that Amazon built its technical infrastructure to handle the peak demand of Q4, but for the rest of the year (Q1-Q3), this capacity sat idle <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. To achieve profitability, Amazon supposedly decided to rent out this excess capacity to other developers, turning a large expense into a revenue stream <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

This story is prevalent because it offers a convenient explanation for how an internet retailer could transform into a "real technology company" <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Why the "Excess Capacity" Narrative is False

This narrative falls apart for two main reasons:

1.  **Technical Impossibility in the Pre-Cloud Era**: Before cloud computing, technology companies did not operate in a way that allowed for easy sharing of server capacity <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Servers were highly customized and tightly coupled to specific applications <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   It was not possible to simply rent out idle servers; there was no inherent security or network hardware setup to serve multiple tenants <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
    *   In a pre-cloud infrastructure world, software was installed directly on owned servers <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The Amazon.com codebase was installed on specific machines, like DEC Alpha servers, which were part of a highly bundled hardware-software platform often leased from manufacturers <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
    *   The significant shift came with Linux and open-source operating systems, which allowed companies to buy various hardware, install Linux, and write their own applications, laying the groundwork for more affordable infrastructure <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This shift, along with a massive rewrite of Amazon.com to run on Linux and HP servers, did save Amazon from a cost perspective during a financially tight period around 2000, but this was not virtualized cloud servers <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
2.  **Business Model Illogicality**: If [[amazon_web_services_aws | AWS]] customers were relying on excess capacity, Amazon would have to tell them they couldn't use the services during Q4 when the retail business needed the servers <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This would be unsustainable for major customers like Netflix, whose streaming services depend on constant availability <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Official Debunking

Werner Vogels, who was the [[amazon_web_services_aws | AWS]] CTO and is now the CTO of all of [[Amazons founding and early years | Amazon]], explicitly stated in a 2011 Quora post:
> "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually within two months after launch [[amazon_web_services_aws | AWS]] would have already burned through the excess [[Amazons founding and early years | Amazon]].com" <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

Vogels further clarified that [[amazon_web_services_aws | Amazon Web Services]] was "always considered a business by itself with the expectation that it could even grow as big as the Amazon.com retail operation" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Intentionality vs. Accident

The excess capacity myth also "short sells" Amazon's [[intentionality_and_strategy_behind_aws | intentionality and strategy]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **Technology as Investment**: For Amazon, technology was never viewed as a mere "cost center" or an "IT department." They always saw themselves as a technology company, constantly considering future technological advancements like Moore's Law and how to leverage them <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Strategic Market Creation**: The development of [[amazon_web_services_aws | AWS]] was an "incredibly [[intentionality_and_strategy_behind_aws | intentional strategy]]" with a "laser focus on an emerging market that they had reason to believe that they could create" <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.