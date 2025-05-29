---
title: The excess capacity myth about AWS
videoId: E1cxZuHrwZc
---

From: [[acquiredfm]] <br/> 

The "excess capacity" narrative is one of four [[aws_origin_stories | separate origin stories]] identified for Amazon Web Services (AWS) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. While tempting and widely believed by the layperson, this story is largely untrue <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## The Myth Explained

The widely circulated urban legend suggests that around 2001-2003, Amazon.com, like other retail businesses, experienced highly seasonal traffic, with massive spikes in demand and revenue during Q4 for the holiday shopping season <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. To handle this peak demand, Amazon had to build out significant technical infrastructure <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The myth posits that for the rest of the year (Q1-Q3), this capacity sat idle, leading Amazon to a "brilliant realization": they could rent out this unused technical infrastructure to other developers, turning a large expense into a revenue stream <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This narrative is often linked to [[amazons_transition_from_growth_to_profitability | Amazon's transition from growth to profitability]] during that period <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Debunking the Myth

This "excess capacity" story falls apart for several reasons, both technical and business-related.

### Technical Implausibility

In the era before cloud computing, technology companies did not operate in a way that would allow for easily renting out excess capacity <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>:
*   **Customized and Coupled Infrastructure**: Servers were highly customized and tightly coupled to specific applications. It was not simple to allow external parties to run their applications on Amazon's existing infrastructure <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Security and Networking Challenges**: There were no inherent security setups for multi-tenancy, nor was the network hardware designed to serve other tenants simultaneously <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   **Proprietary Hardware**: Amazon.com's codebase was installed on owned servers, specifically DEC Alpha servers, which were high-margin, monolithic, and often leased proprietary hardware/software platforms <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Role of Linux**: While [[the_role_of_linux_in_amazons_infrastructure_evolution | Linux]] and open-source operating systems did change the landscape by allowing companies to build applications on more affordable, off-the-shelf hardware (like HP servers for Amazon), this enabled cost savings and internal rewrites, not external virtualization or multi-tenancy <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Amazon's move to Linux and HP servers significantly saved the company from a cost perspective during a tight cash period around 2000 <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. However, this was not the same as virtualized cloud servers <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Business and Strategic Inconsistencies

*   **Service Reliability**: If AWS were built on excess capacity, Amazon would not be able to guarantee service to its AWS customers during Q4 when its retail business needed the servers most <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. This is illustrated by the impracticality of telling a major customer like Netflix that they couldn't stream during the holidays <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Intentionality**: The myth "short sells Amazon" by implying AWS was an accidental byproduct rather than an intentional strategy <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Amazon never viewed technology as a mere cost center; they always considered themselves a technology company and an [[awss_approach_to_cloud_computing_and_technology_strategy | investment in future capabilities]] <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. AWS was an "incredibly intentional strategy" focused on creating a brand new business in an emerging market <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### Official Debunking

The most definitive refutation comes from Werner Vogels, who was AWS CTO at the time and is now CTO of all of Amazon <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. In a Quora post from 2011, Vogels stated:

> <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a> "The excess capacity story is a myth. It was never a matter of selling excess capacity. Actually, within two months after launch, AWS would have already burned through the excess amazon.com capacity. Amazon Web Services was always considered a business by itself with the expectation that it could even grow as big as the amazon.com retail operation." <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>

This statement reinforces that [[awss_business_model_and_financial_impact | AWS was conceived as a standalone business]] from the outset, not a way to monetize idle servers.