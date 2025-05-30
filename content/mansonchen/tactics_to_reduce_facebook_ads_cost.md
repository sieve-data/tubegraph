---
title: Tactics to reduce Facebook ads cost
videoId: jC8Ceb_NBQg
---

From: [[mansonchen]] <br/> 

This article outlines five tactics that can significantly reduce your Facebook ads Cost Per Acquisition (CAC) by 30% or more <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Poor unit economics is identified as the primary reason apps struggle to [[scaling_facebook_ads|scale with Facebook ads]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The strategies aim to address rising ad costs and improve return on investment <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## 1. Qualified Trial Event

The first tactic is to test a qualified trial event <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. This event typically occurs 24 to 48 hours after a trial start <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, indicating active app usage <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. It is highly correlated with the subscribe event, as users who reach this point are more likely to see value and pay for the app <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The goal is to test bringing the optimization event further down the funnel <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It's crucial to balance this with a high enough event volume; if there isn't sufficient volume for the qualified trial event, it's recommended to revert to optimizing for the trial start event and use other techniques <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

Examples of qualified trial events include:
*   Logging a workout <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>
*   Saving a search <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>
*   Requesting a brochure <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>

> [!PRO TIP]
> Exclude people who have canceled their free trial within the first 10 to 15 hours to avoid sending negative signals back to Facebook <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## 2. Testing Lookalike Audiences

While broad targeting is generally preferred for [[scaling_facebook_ads|scaling Facebook ad accounts]] <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, testing lookalike audiences can be beneficial when struggling with CAC <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

Consider testing different seed sets beyond just "all customers" <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, such as your highest LTV (Lifetime Value) users <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Focus on users who are most active within the last 30 or 90 days, as time recency has shown good results <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Aim for a list size of at least 10,000 users for upload to Facebook, though 5,000 may be acceptable <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. An expected match rate around 70% is common <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Although these lookalike audiences might result in a higher cost per trial <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, they are often offset by a higher trial-to-subscribe rate due to superior audience quality <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. These user lists can typically be pulled from analytics providers like Mode Analytics, Amplitude, or PostHog <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This strategy can be combined with broad targeting for significant CAC improvements <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## 3. [[creative_team_strategies_for_facebook_ads|Creative Testing]]

It is crucial to continually iterate on ads that are performing well and consistently test new concepts <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This prevents ad fatigue when winning ads lose effectiveness <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The goal is to establish a repeatable process that reliably produces "unicorn winning ads" every month <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

For more detailed information on making video ads that convert, refer to the related resource <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The tool Sovereign was developed to [[automating_facebook_video_ads|automate the grunt work of video editing and ad launching]] <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, aiming to save thousands of dollars monthly on headcount and hourly wages, allowing focus on higher-order problems <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## 4. Bid Caps and Cost Caps

Implementing bid caps and cost caps in evergreen broad targeting campaigns is recommended <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. The optimal value may not be found on the first attempt <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

*   **Cost Caps:** Start at approximately 130% of your target CAC goal <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. For example, if the goal is $100, set the cost cap at $130 <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Bid Caps:** Start even higher than the cost cap <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Starting higher helps ensure immediate data inflow and delivery <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

The risk on these ad sets is considered low because they are populated with creatives that have already met [[facebook_creative_testing_strategies|creative testing]] criteria <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This allows for an aggressive approach to spending with bid and cost caps <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## 5. Bin Multipliers (Special Resource)

> [!CAUTION]
> This special resource, known as bin multipliers, is typically unknown to most marketers <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. It is exclusively available through the API and requires whitelisting by a Facebook ad representative <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. A script for this was made available for free in 2023 <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Bin multipliers allow you to inform Facebook that you are willing to pay more for specific demographics or placements <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This is advantageous because it enables continued broad targeting <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>, which is generally preferred to avoid making the audience too small (e.g., excluding genders or specific age ranges), as this can significantly increase CPM <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

With bid multipliers, you can maintain broad targeting while bidding lower on less desirable demographics (e.g., 18-24 year olds) and higher on more valuable ones (e.g., 30+ year olds) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This is a highly recommended tactic to test if you have a Facebook representative <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

For more information on how to [[automating_facebook_video_ads|make video ads that actually convert]] in 2025, refer to the linked video <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.