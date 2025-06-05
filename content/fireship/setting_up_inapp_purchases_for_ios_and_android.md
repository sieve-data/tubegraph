---
title: Setting up inapp purchases for iOS and Android
videoId: NWbkKH-2xcQ
---

From: [[fireship]] <br/> 

In-app purchases and microtransactions are a significant source of revenue for mobile applications, with games like Candy Crush generating an estimated four million dollars per day in 2018 from these features <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article focuses on the initial setup required to implement in-app purchases for both iOS and Android platforms, primarily for consumable digital products using the official Flutter plugin <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## [[types_of_in_app_purchases_and_their_differences | Types of In-App Purchases]]

There are three main types of in-app purchases <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>:

*   **Consumables**: Products that are depleted and can be purchased multiple times, such as coins in a game <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This guide will focus on setting these up <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Non-Consumables**: Items purchased once, like an upgrade, which the user should not have to buy again <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Subscriptions**: Provide access to content for a limited duration <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

These concepts apply to both iOS and Android, though subtle differences exist in their implementation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. When selling digital content, platform-specific in-app purchase APIs are almost always required, precluding the use of third-party APIs like Stripe or PayPal for this purpose <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### [[technical_details_of_the_flutter_inapp_purchase_plugin | Flutter In-App Purchase Plugin]]

Flutter recently released an officially supported plugin for in-app purchases, offering a unified interface across iOS and Android <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This plugin, although currently in beta, is used for implementation <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### [[design_techniques_in_app_development | Design Considerations]]

To maximize revenue from in-app purchases, apps often need to be highly addictive and target a wide audience <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. [[design_techniques_in_app_development | Designing]] the interface around "dopamine hits" and "compulsion loops" by regularly rewarding the user while keeping them engaged is a common strategy <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Initial Setup for iOS

To set up in-app purchases for iOS, you'll need an Apple Developer account <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

1.  **App Store Connect Release**: Your iOS app needs to have a release on App Store Connect, even if it's not publicly available (e.g., for TestFlight) <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Detailed guides for preparing an iOS release are available in Flutter documentation and various courses <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
2.  **Add In-App Purchase in App Store Connect**:
    *   Navigate to the **Features** tab <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Add a new in-app purchase <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   Ensure it's a **Consumable** type <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   Assign it a name and a **Product ID** <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. It's advisable to use the same Product ID on the Google Play Store <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
    *   Configure pricing and display details <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
3.  **Enable Capability in Xcode**:
    *   Open your project in Xcode <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Select the build target <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Go to the **Capabilities** tab <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   Flip the **In-App Purchase** switch to "on" <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## Initial Setup for Android

For Android, a Google Play Developer account is necessary <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

1.  **Google Play Release**:
    *   You need to create a signed release APK that can be uploaded to Google Play <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Refer to Flutter documentation for detailed steps <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
    *   Create at least an **alpha release** for your app in Google Play Console <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This is crucial for testing the Google Play billing API locally <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Add your email address as a tester on that release track <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
2.  **Add In-App Product in Google Play Console**:
    *   Go to the **Store presence** tab <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, then **In-app products**, and finally **Manage products** <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
    *   On Google Play, there's no direct distinction between consumable and non-consumable types during setup; this is handled within the app's code <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Create a new product using the same **Product ID** as used for iOS <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   Ensure your product is set to **Active** <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## In-App Purchase Management

Once the setup is complete, the application needs to interact with the billing APIs. This involves querying for available products and a user's past purchases <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. For consumable products, it's critical to save their state in your own database (e.g., [[setting_up_and_managing_firebase_projects | Firebase Firestore]]) because the marketplace APIs do not return consumed products <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. This ensures the user can retrieve their consumed product state even if the app widget is destroyed <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

When purchasing a consumable product on Android, you explicitly designate it as `buyConsumable` (as opposed to `buyNonConsumable` for one-time purchases) <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. By default, it's automatically marked as consumed, meaning your business logic manages its state <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. However, `autoConsume` can be set to `false` on Android, which prevents re-purchase until you explicitly mark it as consumed after the user depletes it <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. On iOS, you'll need to mark past purchases as complete <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.