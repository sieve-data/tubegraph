---
title: Understanding Facebooks winner take all algorithm
videoId: jnKf0m9s99E
---

From: [[mansonchen]] <br/> 

The Facebook algorithm operates on a "winner-take-all" principle <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This means that typically, within an ad set, one or two ads will receive the majority of the ad spend <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

## Implications for Creative Testing

This characteristic of the algorithm has significant implications for how advertisers should approach creative testing. Newer advertisers often waste money testing Facebook ads because they don't know how to set up their creative testing campaigns effectively <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>.

### The Problem with Advantage Shopping Plus (ASC) Campaigns for Testing
The **Advantage Shopping Plus (ASC) campaign** type should be avoided for creative testing <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

*   **Uneven Spend Distribution**: If you upload 50 ads into an ASC campaign's ad set, only one out of the 50 ads will typically get most of the spend <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This provides a very low chance (e.g., 2% with 50 ads) that Facebook will pick the "right" winning ad immediately <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   **Probabilistic Errors**: While Facebook promises to find the winning ad for you, the algorithm is probabilistic and can make mistakes <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. When you have many ads in one ad set, the likelihood of it picking the wrong one increases <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Misleading Early Metrics**: Early funnel metrics, such as click-through rate (CTR) and view duration, heavily influence delivery early on <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. However, these metrics don't always translate to conversions. For example, a clickbaity ad might get high early engagement but fail to convert <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.
*   **Real-world Example**: One adtech app founder using an ASC campaign for creative testing found his first three ads generated a cost per trial of $40-$50. Only after pausing these, the fourth ad, which finally received spend, achieved a cost per trial of $8 – five to six times better <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### Recommended Approach for Creative Testing: Ad Set Budget Optimization (ABO)
For effective creative testing, it is highly recommended to use **Ad Set Budget Optimization (ABO) campaigns** <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.

*   **Controlled Budget Allocation**: ABO campaigns allow you to manually set the daily budget for each ad set within the campaign <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Increased Chance of Finding Winners**: With four ad variants in an ad set test, you have a 25% chance of Facebook picking the right one from the start <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. This method, while potentially leading to more upfront spend, offers more opportunities to find the best ad <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Objective Pausing**: You can quickly and objectively pause underperforming ads using triggers <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.
*   **Setup Recommendations**:
    *   Test one country and one language (e.g., US in English) <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.
    *   Start a creative testing ad set with a daily budget of $100 <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
    *   Use auto bidding, without entering a value for cost per result goal or bid cap <a class="yt-timestamp" data-t="04:57:00">[04:57:00]</a>.
*   **Localization**: Once a winning ad is found, if your app is localized, you can localize the winning ads and move them into [[optimizing_and_scaling_facebook_ad_campaigns | evergreen campaigns]] for their respective countries or country groupings <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.

### Scaling Campaigns
For [[scaling_facebook_ads | scaling]] campaigns, using an [[optimizing_and_scaling_facebook_ad_campaigns | Advantage Shopping campaign]] is ideal <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>, <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>. In this scenario, every ad within the ad set has already proven itself in the creative testing campaign <a class="yt-timestamp" data-t="05:13:00">[05:13:00]</a>. Therefore, it matters less which ad Facebook picks, as you are confident it will lead to a low Cost Per Acquisition (CPA) <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. If a winning ad experiences fatigue, it can be paused, allowing another proven ad to take its place and continue spending <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.