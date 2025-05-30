---
title: Broad targeting with Meta ads
videoId: sFcHfdB9dDo
---

From: [[mansonchen]] <br/> 

Broad targeting with Meta ads can lead to challenges if not managed carefully, potentially resulting in negative LTV:CAC (Lifetime Value to Customer Acquisition Cost) and extended payback periods <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Meta media buying is increasingly becoming a "blackbox," with broad targeting now the recommended audience setting for scaling <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## What Broad Targeting Entails

For scaling, broad targeting typically involves:
*   Country-level targeting <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>
*   Exclusion of past purchasers <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   Absence of interest targeting or lookalikes <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>

To optimize, it's crucial to provide Meta with the best possible signal, using purchase optimization and Conversion API feeds <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Advertisers are encouraged to supply a large volume of diverse [[creative_strategy_and_testing_for_meta_ads | creatives]] and let Meta identify the right audience based on these creatives <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

Meta is actively pushing users towards Advantage Shopping Plus campaigns, which are designed to be more streamlined <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These campaigns often hide various settings:
*   Campaign Budget Optimization (CBO) decides budget allocation <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Advantage Plus audience settings hide audience targeting <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>
*   Advantage Plus placements hide placement targeting <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   Highest volume bidding hides bid caps <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>

## Drawbacks: The "Broad Targeting Trap"

A common pitfall with broad targeting is [[optimizing_meta_ads_for_subscription_apps | optimizing for the wrong event]], particularly for apps <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Many optimize for trials, installs, or registrations, which can be challenging to execute correctly <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. While this can reach incremental audiences if current purchase-optimized setups face diminishing returns, it requires a robust data science team and expertise <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

When optimizing for a trial event, Meta focuses on the lowest cost per trial or purchase, but it does not account for audience quality or LTV <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This can lead to:
*   Declining trial-to-subscribe rates <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>
*   Refunds <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
*   Lack of activation <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>
*   Increased customer support tickets <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>

If your optimization signal isn't highly correlated to your business objective, you are effectively telling Meta to find the wrong people <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. For example, focusing on free trials might attract users with fake or prepaid credit cards, leading to failed charges and no activation upon trial expiration <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

## Taking Back Control of the Meta Algorithm

To regain control and ensure Meta targets your ideal customer profile (ICP), consider these tactics:

### 1. Creative Strategy Aligned with ICP
*   Tailor [[creative_strategy_and_testing_for_meta_ads | creatives]] to your ICP <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   Older demographics tend to use Facebook Feed, while younger audiences are more on Instagram Reels <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

### 2. Optimize for Qualified Trial Events
*   Send a "qualified trial event" to Meta and optimize for that event within the platform <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   This could be an activation metric that occurs within 24-48 hours after sign-up, such as an asset uploaded, a project created, or an asset generated <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Determine what actions are highly correlated to your subscribe event, potentially using regression analysis <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### 3. Bid Multipliers
*   This feature is typically available through a Facebook representative via whitelisting <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   Bid multipliers helped increase trial-to-subscribe rates by 20-30% on Android campaigns for Calm <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. A free Python script might be available for those whitelisted <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### 4. Add Friction to the Signup Flow
*   Introduce friction or disqualification steps in your signup process <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   Examples include reducing free trial durations (e.g., from 14 to 7 days) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>, requiring business email confirmation <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, or adding a minimum spend threshold in scheduling invites <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### 5. Consider Removing the Free Trial
*   Eliminating the free trial can align the Meta algorithm more closely with your core business objective <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   To reduce risk for prospects, offer a money-back guarantee instead <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   This could involve switching to a demo-based onboarding process or implementing a hard paywall where users must pay to use the app <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   The Opal app, for instance, initially added an early paywall for an expensive subscription, which they used as a "discovery engine" and "product market fit engine," focusing on Day 8 return on ad event <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.