---
title: Incentives for electric vehicle adoption
videoId: sljBU_HFnFs
---

From: [[causalpython]] <br/> 

Incentivizing the purchase of electric vehicles (EVs) by governments and policymakers is a strategy aimed at reducing greenhouse gas emissions and promoting environmental sustainability <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. However, the effectiveness of these incentives is not straightforward and presents complex challenges <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

## The Problem with EV Incentives

While EVs are generally better for the environment than internal combustion engine (ICE) vehicles, their manufacturing process incurs significantly higher greenhouse gas emission costs <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. A critical issue arises if an incentivized EV is not driven frequently, especially if it's purchased as a complementary vehicle and most driving miles are still accumulated on an ICE vehicle <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. In such cases, the EV could actually have a negative environmental impact compared to if it had never been purchased <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Therefore, it is crucial for governments to incentivize the *right* people <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Counterfactual Nature and Response Types

This challenge is considered a [[causality_and_ai_challenges_and_opportunities | problem of counterfactual nature]], involving unit selection and the probabilities of necessity and sufficiency <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. Policy makers must identify groups of people who will respond to incentives in a way that truly benefits the environment <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

Different household responses to incentives can occur:
*   **Negative Response** Some households might react negatively to an incentive, perhaps because it originates from a government associated with an opposing political party <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. This could lead them to *never* buy an EV, which would be a detrimental outcome for long-term greenhouse gas emission reduction <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. This "harmful consequence" is something policymakers aim to avoid <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   **Positive Response** The ideal scenario is when an individual receives an incentive, purchases an EV, and drives it extensively <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. This also implies that without the incentive, they would either not have purchased the vehicle or would have purchased it but not driven it much <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. This concept is referred to as the "probability of benefit" or "probability of necessity and sufficiency" <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.

## Weighting Response Types

To optimize incentive programs, different response types can be assigned varying weights <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. For example:
*   A "harmful consequence" where an incentive causes someone *not* to buy an EV (when they otherwise would have) might be assigned a strong negative weight, such as -10 <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
*   A "beneficial outcome" where an incentive leads to an EV purchase and high usage might receive a positive weight, such as 2 <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

These weighted response types are incorporated into a formula to guide policy decisions <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## Key Insights and Impact

The primary insight from this work is that policy decisions regarding which groups to incentivize and what types of incentives to offer can vary significantly based on the preferences for these weights <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The research helps to understand the complexities of the EV and ICE vehicle industries, as well as the decision-making processes of governments <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The hope is that this work will enable governments and policymakers to make more informed decisions, incentivizing the right people in a way that genuinely benefits the environment <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.