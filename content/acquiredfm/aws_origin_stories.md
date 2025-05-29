---
title: AWS origin stories
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

There are multiple origin stories for [[amazon_web_services_aws_history_and_origin_stories | AWS]], each offering insight into [[amazons_early_history_and_founding | Amazon]] and its culture <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. One of the most commonly believed narratives, which is "obviously untrue," is the [[the_excess_capacity_myth_about_aws | excess capacity myth]] <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The "Excess Capacity" Myth

The popular story suggests that around 2001-2003, [[amazons_early_history_and_founding | Amazon]].com, like most retail businesses, experienced highly seasonal demand with huge spikes in traffic during Q4 for the holiday shopping season <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This period accounts for the largest share of quarterly revenue <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For the first five years of the business, a rule existed prohibiting new code commits to production in November and December to ensure stability, with all teams, including executives and engineers, working in warehouses during Q4 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

The urban legend posits that because [[amazons_early_history_and_founding | Amazon]] had to build out technical infrastructure for the peak Q4 demand, it had "excess capacity" in its IT operations during Q1 through Q3 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The company then supposedly had the "brilliant realization" to rent out this idle capacity to other developers, thereby turning a large expense into a revenue stream <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Debunking the Myth

This narrative falls apart for several reasons:

### Technical Impossibility in the Pre-Cloud Era
In a pre-cloud technology environment, systems were not designed to be easily rented out. Servers were highly customized and tightly coupled to specific applications <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. There was no built-in security or network hardware to serve multiple tenants <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. [[amazons_early_history_and_founding | Amazon]].com's codebase was installed on specific, owned servers, such as Digital Equipment Corporation (DEC) Alpha servers, which were part of highly bundled, monolithic hardware-software platforms <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

The eventual shift to [[the_role_of_linux_in_amazons_infrastructure_evolution | Linux]] allowed for the use of commodity hardware (like HP servers) and open-source operating systems, significantly reducing infrastructure costs and preventing [[amazons_early_history_and_founding | Amazon]] from potentially going out of business around 2000 due to cash constraints <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. However, this change to an open-source ecosystem and a rewrite of [[amazons_early_history_and_founding | Amazon]].com to run on [[the_role_of_linux_in_amazons_infrastructure_evolution | Linux]] and HP servers was a cost-saving measure, not a virtualization for cloud services <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Business Impossibility
If [[awss_approach_to_cloud_computing_and_technology_strategy | AWS]] operated on excess capacity, it would be unable to serve its customers during [[amazons_early_history_and_founding | Amazon]]'s peak Q4, which is an untenable proposition for critical services like Netflix streaming <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

### Official Refutation
The [[the_excess_capacity_myth_about_aws | excess capacity myth]] was definitively disproven by Werner Vogels, who was the CTO of [[awss_approach_to_cloud_computing_and_technology_strategy | AWS]] at the time and later became the CTO of all of [[amazons_early_history_and_founding | Amazon]] <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. In a 2011 Quora post, Vogels flatly stated, "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually within two months after launch [[amazon_web_services_aws_history_and_origin_stories | AWS]] would have already burned through the xs[[amazons_early_history_and_founding | Amazon]].com [capacity]" <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. He further clarified that [[amazon_web_services_aws_history_and_origin_stories | AWS]] was "always considered a business by itself with the expectation that it could even grow as big as the [[amazons_early_history_and_founding | Amazon]].com retail operation" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Amazon's Intentional Strategy

The [[the_excess_capacity_myth_about_aws | excess capacity myth]] "short sells" [[amazons_early_history_and_founding | Amazon]]'s true intentionality and strategy <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. For [[amazons_early_history_and_founding | Amazon]], technology was never viewed as a cost center, but always as an investment <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The creation of [[amazon_web_services_aws_history_and_origin_stories | AWS]] was an "incredibly intentional strategy" focused on creating and addressing an emerging market <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.