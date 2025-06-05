---
title: Implementing in app purchases in Flutter
videoId: NWbkKH-2xcQ
---

From: [[fireship]] <br/> 

In-app purchases and microtransactions can generate significant revenue for mobile applications; for example, Candy Crush made an estimated four million dollars per day from them in 2018 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explains how to implement consumable in-app purchases in [[crossplatform_app_development_with_flutter | Flutter]] for selling digital products on iOS or Android <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Types of In-App Purchases
There are three main [[types_of_inapp_purchases_and_their_differences | types of in-app purchases]]:
*   **Consumables:** Products that are depleted and can be purchased multiple times, like in-game coins or gems <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This article focuses on implementing these <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Non-Consumables:** Items purchased once that the user should not have to buy again, such as an upgrade <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Subscriptions:** Provide access to a purchase for a limited time <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

While these concepts apply to both iOS and Android, there are important differences in their implementation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. In-app purchases are almost always required for selling digital content, meaning APIs like Stripe and PayPal are generally not an option <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Flutter In-App Purchase Plugin
Flutter offers an officially supported [[technical_details_of_the_flutter_inapp_purchase_plugin | plugin for in-app purchases]] that provides a unified interface across iOS and Android <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This plugin is currently in beta, so details may change <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

> [!tip] App Design for Monetization
> To maximize revenue, design your app to be highly addictive and target a wide audience <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Focus on creating an interface that provides dopamine hits and compulsion loops by regularly rewarding the user while keeping them engaged in chasing future rewards <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## [[setting_up_inapp_purchases_for_ios_and_android | Setting Up In-App Purchases for iOS and Android]]

### iOS Setup
1.  **Apple Developer Account:** You need an Apple Developer account <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
2.  **App Store Connect:** An iOS app release needs to be on App Store Connect (not necessarily public App Store) for testing with TestFlight <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Refer to Flutter documentation for preparing an iOS release <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
3.  **Add In-App Purchase:** In App Store Connect, go to the "Features" tab, add a new in-app purchase, select "Consumable" type, and provide a name and Product ID <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Note this Product ID as it should be the same on Google Play Store <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. Configure pricing and display details <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
4.  **Xcode Capability:** In Xcode, select the build target, go to the "Capabilities" tab, and enable the "In-App Purchases" switch <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Android Setup
1.  **Google Play Developer Account:** You need a Google Play Developer account <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Signed Release:** Create a signed APK release to upload to Google Play <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. Refer to Flutter documentation for detailed steps <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
3.  **Alpha Release:** Create at least an alpha release for your app on Google Play to test the Google Play billing API locally <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. The billing API won't work without a release <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Add your email address as a tester on that track <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
4.  **Manage Products:** Go to "Store Presence" > "In-app products" > "Manage products" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
5.  **Create Product:** On Google Play, you handle the distinction between consumable and non-consumable directly in the app code <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Create a new product with the same Product ID used on iOS <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Ensure the product is set to "Active" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Technical Implementation in Flutter

This section focuses on the API of the in-app purchases plugin using only built-in [[building_mobile_app_components_with_flutter | Flutter]] tools (e.g., `StatefulWidget`) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. For production apps, consider using state management solutions like Provider, BLoC, or [[state_management_with_flutter_and_firebase | Firebase]] to manage the state of purchases across devices and screens <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Project Setup
1.  Add the `in_app_purchase` plugin to your `pubspec.yaml` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
2.  Import the plugin and `dart:io` for platform checking in your Dart file <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Widget Properties (State)
In a `StatefulWidget` (e.g., a "MarketScreen"), you'll manage the following properties:
*   `InAppPurchaseConnection`: A reference to the plugin's API instance <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   `_isAvailable`: Boolean indicating if the in-app purchase API is available on the device <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   `_products`: A list to store product details queried from the marketplace <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   `_purchases`: A set of `PurchaseDetails` representing the user's past purchases <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   `_purchaseUpdateSubscription`: A subscription to a stream of purchase detail updates, which emits new values when a user buys a product or if they buy it from a different client <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   `_credits`: A placeholder representing the consumable product (e.g., in-game currency) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### Lifecycle Hooks
*   **`initState`**: Call an asynchronous `_initialize` method to fetch products and past purchases from the marketplace <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **`dispose`**: Cancel the `_purchaseUpdateSubscription` to prevent memory leaks <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### UI Structure
A basic UI might include:
*   A `Scaffold` with an `AppBar` displaying "Open for Business" or "Not Available" based on API availability <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.
*   A loop over `_products` to display each product.
*   For each product, determine if the user has a past purchase.
    *   If purchased, display custom logic to allow consumption.
    *   Otherwise, display a button to make a new purchase <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Initialization (`_initialize` method)
The `_initialize` method, called in `initState`, performs the following steps:
1.  Check if the in-app purchase API is available <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  Retrieve products and user's past purchases concurrently using `Future.wait` for better performance <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
3.  Implement business logic to verify a purchase <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
4.  Set up a subscription to the `purchaseUpdatedStream` <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. When new `PurchaseDetails` are emitted, append them to the existing `_purchases` list without overriding it <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Retrieving Products (`_getProducts` method)
This method involves:
1.  Creating a `Set` of product IDs you want to retrieve from the App Store or Google Play Store <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
2.  Calling `inAppPurchase.queryProductDetails(productIDs)` <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
3.  Checking the response for errors or missing product IDs.
4.  Calling `setState` to update the `_products` list with the `response.productDetails` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### Retrieving Past Purchases (`_getPastPurchases` method)
1.  Call `inAppPurchase.queryPastPurchases()` <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
2.  **Important Caveat:** This method *does not* return consumed products <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. For consumable products, you *must* save their state in your own database (e.g., Firestore with [[advanced_data_management_techniques_in_flutter_apps | Firebase]]) to retrieve them after the widget is destroyed <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This method is primarily relevant for non-consumable products <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
3.  On iOS, you'll also want to mark past purchases as complete <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
4.  Call `setState` to update the `_purchases` list <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### Verifying Purchases (`_hasPurchased` helper method)
Create a helper method that takes a `Product ID` and checks the `_purchases` list for a matching ID, returning the `PurchaseDetails` if found, or `null` otherwise <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Delivering Products (`_deliverProduct` method)
This method contains your app's business logic for delivering a purchased product:
1.  Check if the user has purchased the specific product <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
2.  Verify that the purchase status is valid (not error or pending) before delivering credits or gems <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
3.  Purchases should be verified both at app initialization and when a new purchase is emitted by the `purchaseUpdatedStream` <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Server-side verification is also an option <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### Purchasing a Product (`_buyProduct` method)
This method is called when the user initiates a purchase:
1.  Pass the `ProductDetails` to create a `PurchaseParam` <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
2.  Call `inAppPurchase.buyConsumable()` for consumable products (or `buyNonConsumable()` for one-time purchases) <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
3.  By default, `autoConsume` is `true` for Android, meaning your app controls the purchase state <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
4.  Setting `autoConsume` to `false` (Android only) prevents the user from purchasing the product again until you manually mark it as consumed <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Consuming a Product (`_spendCredits` method)
This method demonstrates how to manage consumption, especially for Android with `autoConsume` set to `false`:
1.  Takes `PurchaseDetails` as an argument <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
2.  Decrements the `_credits` on the widget as the user "spends" them <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
3.  When `_credits` reach zero, inform the Google Play Store that the purchase has been consumed (`inAppPurchase.completePurchase(purchaseDetails)`) <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. This allows the user to purchase another instance of the product; otherwise, they would receive an error stating they already own it <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.