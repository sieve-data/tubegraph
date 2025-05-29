---
title: Amazons seasonal traffic and IT capacity
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

Amazon's retail business experiences significant seasonality, with huge spikes in traffic and demand during the fourth quarter (Q4) for the holiday shopping season <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. The largest share of Amazon's quarterly revenue historically occurs in Q4 <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This seasonal peak led to strict operational rules within the company:
*   For at least the first five years, a rule was enforced in November and December that no new code could be committed to production unless it was a critical bug fix <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
*   For many years, the executive team, business side, and engineers would all work in the warehouses during Q4 to handle demand <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## The Excess Capacity Narrative

The most widely believed, yet untrue, origin story for AWS is the [[the_excess_capacity_myth_about_aws | excess capacity narrative]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This urban legend suggests that around 2001-2003, as [[amazons_transition_from_growth_to_profitability | Amazon sought profitability]], it realized it had significant excess technical infrastructure capacity during quarters one through three <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Because Amazon had to build out its IT infrastructure to handle the peak demand of Q4, the story claims that this capacity sat idle for the rest of the year <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. The company supposedly decided to rent out this "sitting" capacity to other developers, turning a large expense into a revenue stream <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

## Debunking the Myth

This narrative falls apart for several reasons:

### Technical Impossibility
In a pre-cloud technology company, IT infrastructure was not easily shareable <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Servers were highly customized and tightly coupled to specific applications <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. It was not possible to simply rent out unused servers for others to run their applications without extensive re-configuration and security measures <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Amazon's code base was literally installed on its owned hardware, making it impossible to "rent out" that capacity directly <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

The company's early servers were DEC Alpha servers, high-margin, monolithic hardware-software platforms <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The fundamental shift that laid the groundwork for flexible infrastructure was the emergence of [[the_role_of_linux_in_amazons_infrastructure_evolution | Linux]], which allowed companies to use off-the-shelf hardware and run open-source operating systems <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This shift, which saved Amazon from a cost perspective around 2000 by moving its website to Linux on HP servers, was about cost reduction, not virtualized cloud services <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Logical Inconsistency
If AWS were based on excess capacity, Amazon would not be able to guarantee service to its AWS customers during its own Q4 peak <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It's illogical to assume AWS customers, like Netflix, would accept having their services interrupted during Amazon's busiest retail period <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

### Official Refutation
Werner Vogels, who was AWS CTO and is now CTO of all of Amazon, explicitly stated in a 2011 Quora post:
> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually, within two months after launch AWS would have already burned through the excess amazon.com capacity."
> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a> "Amazon Web Services was always considered a business by itself with the expectation that it could even grow as big as the amazon.com retail operation."

### Undermining Amazon's Strategy
The [[the_excess_capacity_myth_about_aws | excess capacity myth]] undervalues Amazon's intentionality and strategic foresight <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. [[amazons_transition_to_a_technology_company | Technology was never viewed as a cost center for Amazon]]; rather, it was seen as an investment <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The creation of AWS was an incredibly intentional strategy focused on an emerging market Amazon believed it could create <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.