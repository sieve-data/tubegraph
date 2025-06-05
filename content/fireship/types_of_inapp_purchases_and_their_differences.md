---
title: Types of inapp purchases and their differences
videoId: NWbkKH-2xcQ
---

From: [[fireship]] <br/> 

In-app purchases (IAP) allow mobile applications to sell digital products to users directly within the app experience. For example, in 2018, the game Candy Crush generated an estimated four million dollars per day from in-app purchases and microtransactions, primarily by selling digital products to casual gamers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores the main types of in-app purchases and their key differences, focusing on implementation in Flutter across iOS and Android <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Main Types of In-App Purchases

There are three primary types of in-app purchases <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:

### Consumables
Consumables are products that are depleted upon use and can be purchased multiple times <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Examples include in-game coins or gems, which a user can buy, consume, and then buy again <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Non-Consumables
Non-consumables are items the user purchases once and should never need to purchase again <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. An upgrade within an app is a typical example <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.

### Subscriptions
Subscriptions grant the user access to a purchase for a limited duration <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Platform-Specific Differences and Considerations

While the core concepts of IAPs apply to both iOS and Android, there are important subtle differences in their implementation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

### Setup Requirements
*   **iOS**: Requires an Apple Developer account and an existing release of the app on App Store Connect (even if not publicly available) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Within App Store Connect, consumable products must be explicitly defined as such <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The "in-app purchases" capability must also be enabled in Xcode <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Android**: Requires a Google Play Developer account and a signed APK uploaded as at least an alpha release <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Unlike iOS, Google Play does not require a distinction between consumable and non-consumable types at the product setup level; this distinction is handled directly in the application's code <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The product must be set to "active" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Payment Restrictions
In-app purchases are almost always required for selling digital content <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. This means third-party [[using_apis_and_third_party_services | APIs]] like [[introduction_to_stripe_payments_and_3d_secure | Stripe]] and PayPal are typically not an option for digital goods <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Fortunately, Flutter provides an officially supported plugin for in-app purchases that offers a unified interface across both platforms <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Handling Consumables in Code
For Android, the distinction between consumable and non-consumable products is made when the purchase is initiated in the app's code, using `buyConsumable` or `buyNonConsumable` methods <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

By default, consumable purchases are marked as consumed automatically. This means the app's business logic is responsible for tracking and managing the state of that purchase <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Developers can also set `autoConsume` to `false` (Android only) to prevent re-purchase until the app explicitly marks the product as consumed <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### Retrieving Past Purchases
The `queryPastPurchases` method in the `in-app purchases` plugin does *not* return consumed products <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This means the state of consumed products must be saved in the developer's own database (e.g., using a service like Firebase Firestore) to ensure users can retrieve them after the app's widget has been destroyed <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Retrieving past purchases directly from the marketplace is primarily relevant for non-consumable products <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. On iOS, retrieved past purchases should also be marked as complete <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## App Design for Successful In-App Purchases

To maximize revenue from in-app purchases, apps often employ [[design_techniques_in_app_development | design techniques]] that make them highly addictive and appeal to a wide audience <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This includes designing interfaces around "dopamine hits" and "compulsion loops," where users are regularly rewarded but always kept pursuing more <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.