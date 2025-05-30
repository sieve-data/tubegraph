---
title: Qualified trial events for app optimization
videoId: jC8Ceb_NBQg
---

From: [[mansonchen]] <br/> 

A "qualified trial event" is a key metric used in app optimization, particularly for Facebook ads, to identify users who are highly engaged and likely to convert into paying subscribers [00:00:41]. This strategy aims to improve unit economics for apps struggling to scale with Facebook ads due to poor performance [00:00:14].

## Definition and Purpose

A qualified trial event is an action a user takes *after* initiating a free trial, typically within 24 to 48 hours, that indicates active engagement with the app [00:00:41]. This event is highly correlated with the eventual subscribe event, as it demonstrates that the user is seeing value in the app and is therefore more likely to pay after the free trial period [00:00:57].

The core idea behind [[optimizing_for_purchases_and_trial_starts | testing]] this event is to bring the optimization event further down the funnel, past just the trial start, to capture higher-quality leads [00:01:07].

## Implementation Considerations

When implementing qualified trial events for [[optimizing_meta_ads_for_subscription_apps | optimizing Meta ads for subscription apps]], it's crucial to balance the desired event with sufficient event volume [00:01:11]. If there isn't enough volume for the qualified trial event, it's advisable to revert to the trial start event and [[testing_strategies_for_successful_ads | test]] other techniques [00:01:14].

### Examples of Qualified Trial Events

Examples of actions that can serve as qualified trial events include:
*   Logging a workout [00:01:29]
*   Saving a search [00:01:32]
*   Requesting a brochure [00:01:32]

### Pro Tip for Data Quality

<div class="admonition tip">
<p class="admonition-title">Pro Tip from Silvin from Growth Gems</p>
To maintain the quality of the signal sent back to Facebook, exclude users who cancel their free trial within the first 10 to 15 hours from your qualified trial event data [00:01:35]. This prevents negative signals from skewing your optimization efforts [00:01:42].
</div>