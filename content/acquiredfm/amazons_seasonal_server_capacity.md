---
title: Amazons seasonal server capacity
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

The "excess capacity narrative" is one of four distinct origin stories for [[Amazon Web Services AWS | AWS]], and it is ironically the most widely believed by the public, despite being untrue <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This story suggests that [[Amazons strategy in cloud storage and machine learning | Amazon]] leveraged its idle server capacity to create [[Amazon Web Services AWS | AWS]] <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## The Excess Capacity Narrative Explained

The myth posits that around 2001-2003, [[Amazons business strategy and competitive dynamics | Amazon.com's retail business]], like other retail operations, experienced significant seasonal spikes in traffic and demand during Q4 (the holiday shopping season) <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. For the first five years of the business, a rule existed prohibiting new code commits to production in November and December to maintain stability during this peak <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Additionally, the executive team and engineers would work in warehouses during Q4 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

The urban legend claims that because [[Amazons business strategy and competitive dynamics | Amazon]] had to build out its technical infrastructure for peak Q4 demand, it had excess capacity during Q1-Q3 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The "brilliant realization" was to rent out this unused capacity to other developers, thereby transforming a major expense into a revenue stream <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Why the Myth is Untrue

The excess capacity narrative falls apart for several reasons:

### Technical Impossibility in a Pre-Cloud Era
In the pre-cloud technology landscape, it was not feasible to simply rent out unused servers <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   Servers were highly customized and tightly coupled to specific applications <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Security measures for multi-tenancy did not exist, nor did network hardware understand how to serve multiple distinct tenants <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   [[Amazons business strategy and competitive dynamics | Amazon.com's]] codebase was literally installed on physical boxes they owned, making it impossible to simply "rent out capacity" <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   The servers were DEC Alpha servers, high-margin, monolithic platforms leased from manufacturers like Digital Equipment Corporation (DEC), following a business model similar to IBM or Oracle <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### The Impact of Linux and Open Source
The advent of Linux and open-source operating systems changed the infrastructure landscape by allowing companies to run applications on commodity hardware rather than expensive, bundled platforms <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This shift enabled [[Amazons transition to open source infrastructure | Amazon]] to undertake a massive rewrite of [[Amazons business strategy and competitive dynamics | Amazon.com]] to run on Linux and HP servers around 2000, which significantly reduced costs and saved the company from potential collapse during a period of financial strain <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. However, this move to open source was about cost savings, not about creating virtualized cloud servers for rent <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Business and Logistical Impossibility
If [[Amazon Web Services AWS | AWS]] were based on excess capacity, [[Amazons business strategy and competitive dynamics | Amazon]] would be unable to serve its [[Amazon Web Services AWS | AWS]] customers during their own Q4 peak <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. For example, a company like Netflix, dependent on [[Amazon Web Services AWS | AWS]] for streaming, could not be told they couldn't operate during Q4 because [[Amazons business strategy and competitive dynamics | Amazon]] needed the servers for its retail business <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Such a model would be inherently unreliable for any serious customer <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Official Dispelling of the Myth

Werner Vogels, who was the [[Amazon Web Services AWS | AWS]] CTO and is now the CTO of all of [[Amazons business strategy and competitive dynamics | Amazon]], explicitly debunked this myth in a Quora post in 2011:

> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually, within two months after launch, [[Amazon Web Services AWS | AWS]] would have already burned through the excess [[Amazons business strategy and competitive dynamics | Amazon.com]] capacity. [[Amazon Web Services AWS | Amazon Web Services]] was always considered a business by itself with the expectation that it could even grow as big as the [[Amazons business strategy and competitive dynamics | Amazon.com]] retail operation."

## Intentional Strategy, Not Accidental Discovery

The excess capacity myth undervalues [[Amazons strategy in cloud storage and machine learning | Amazon's]] deliberate strategy and intentionality <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. [[Amazons business strategy and competitive dynamics | Amazon]] never viewed technology as a mere cost center; rather, they considered themselves a technology company and saw technology as a continuous investment <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The creation of [[Amazon Web Services AWS | AWS]] was an "incredibly intentional strategy" focused on an emerging market that [[Amazons business strategy and competitive dynamics | Amazon]] believed it could create and dominate <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.