---
title: Technical details of the Flutter inapp purchase plugin
videoId: NWbkKH-2xcQ
---

From: [[fireship]] <br/> 

The official Flutter in-app purchases plugin provides a unified interface for selling digital products across iOS and Android platforms <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Types of In-App Purchases

There are three main [[types_of_inapp_purchases_and_their_differences | types of in-app purchases]]:
*   **Consumables** Products that are depleted and can be purchased multiple times, like coins or gems in a game <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This article focuses on implementing consumable purchases <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Non-consumables** Items purchased once, such as an upgrade, and should never need to be purchased again <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Subscriptions** Provide access to a purchase for a limited duration <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

These concepts generally apply to both iOS and Android, though there are subtle differences in their implementation <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Initial Setup for In-App Purchases

[[setting_up_inapp_purchases_for_ios_and_android | Setting up in-app purchases for iOS and Android]] involves platform-specific configurations before implementing them in Flutter <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.

### iOS Setup

For iOS, you need an Apple Developer account and a release of your app on App Store Connect (it doesn't have to be public) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
1.  **App Store Connect**:
    *   Navigate to the "Features" tab.
    *   Add a new in-app purchase and select "consumable" type <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
    *   Assign a name and a Product ID. This Product ID should ideally be the same on the Google Play Store <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  **Xcode**:
    *   Go to Xcode, select the build target, and open the "Capabilities" tab <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Enable the "In-App Purchases" capability <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Android Setup

For Android, you need a Google Play Developer account and a signed release uploaded to Google Play <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
1.  **Google Play Console**:
    *   Create at least an alpha release for your app; the Google Play billing API won't work locally without one <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
    *   Add your email address as a tester on that release track <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
    *   Go to the "Store Presence" tab, then "In-app products," and "Manage products" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   On Google Play, there's no distinction between consumable and non-consumable products in the console; this is handled in the app logic <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   Create a new product using the same Product ID as iOS <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
    *   Ensure the product is set to "active" <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## [[implementing_in_app_purchases_in_flutter | Implementing in-App Purchases in Flutter]]

The following steps detail the technical implementation using the official Flutter in-app purchase plugin. This example uses a `StatefulWidget` for simplicity, but [[managing_state_in_flutter_applications | state management]] tools like Provider, BLoC, or [[state_management_with_flutter_and_firebase | Firebase]] could be used for more complex scenarios <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### 1. Add Plugin and Imports

Add the `in_app_purchase` plugin to your `pubspec.yaml` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
Import `in_app_purchase.dart` and `dart:io` for platform checking <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### 2. State Management and Properties

In a `StatefulWidget`, define the following properties:
*   `InAppPurchaseConnection _iapConnection`: A reference to the plugin's API instance <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   `bool _isAvailable`: To check if the in-app purchase API is available on the device <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   `List<ProductDetails> _products`: A list to store product details queried from the marketplace <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   `Set<PurchaseDetails> _purchases`: A set to store the user's past purchases <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   `StreamSubscription<List<PurchaseDetails>> _purchaseUpdatedSubscription`: A subscription to listen for updates to purchase details (new purchases, or purchases made from other clients) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   `int _credits`: A placeholder for a consumable product, like gems <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### 3. Lifecycle Hooks

*   `initState()`: Call an `_initialize` async method to fetch products and past purchases from the marketplace <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   `dispose()`: Cancel the `_purchaseUpdatedSubscription` to prevent memory leaks <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### 4. Initialization Logic (`_initialize` method)

This method handles asynchronous data loading:
1.  **Check API Availability**: Verify `_iapConnection.isAvailable()` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
2.  **Retrieve Products**: Call `_getProducts()` to query product details <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
3.  **Retrieve Past Purchases**: Call `_getPastPurchases()` to get the user's purchase history <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   **Concurrency**: Use `Future.wait([_getProducts(), _getPastPurchases()])` to run these concurrently for better performance <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
4.  **Listen to Purchase Updates**: Set up the `_purchaseUpdatedSubscription` to `_iapConnection.purchaseUpdatedStream` <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   When the stream emits new `PurchaseDetails`, append them to the existing `_purchases` list (do not override) <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
    *   For each new purchase, verify it and then deliver the product <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

### 5. Data Retrieval Methods

*   **`_getProducts()`**:
    *   Create a `Set<String>` of product IDs you want to retrieve <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   Call `_iapConnection.queryProductDetails(productIDs)` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Update the `_products` list in `setState()` with `response.productDetails` <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **`_getPastPurchases()`**:
    *   Call `_iapConnection.queryPastPurchases()` <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   **Caveat**: This method *does not* return consumed products <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. For consumables, you must save their state in your own database (e.g., [[state_management_with_flutter_and_firebase | Firebase Firestore]]) <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
    *   This method is primarily relevant for non-consumable products <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
    *   On iOS, you also need to mark retrieved past purchases as complete <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   Update the `_purchases` list in `setState()` <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### 6. Helper Methods

*   **`_hasPurchase(String productID)`**:
    *   Loops through the `_purchases` list to find a matching `PurchaseDetails` for a given `productID` <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   Returns the `PurchaseDetails` if found, otherwise `null` <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **`_deliverProduct(PurchaseDetails purchase)`**:
    *   Contains your app's business logic to deliver the purchased content (e.g., add credits) <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
    *   **Verification**: Crucially, check `purchase.status` to ensure it's `PurchaseStatus.purchased` (not `error` or `pending`) before delivering <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. This verification should happen upon app initialization and whenever a new purchase is emitted <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. Server-side verification is also an option <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### 7. Making a Purchase (`_buyProduct` method)

*   This method takes a `ProductDetails` object <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   Create a `PurchaseParam` with the necessary data for the marketplace <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Android Consumable Distinction**:
    *   For one-time purchases (non-consumables), use `_iapConnection.buyNonConsumable(purchaseParam)` <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.
    *   For consumables (to be purchased multiple times), use `_iapConnection.buyConsumable(purchaseParam)` <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   By default, Android consumables are *marked as consumed automatically* after purchase <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This means your app's business logic controls its state.
    *   Alternatively, you can set `autoConsume: false` (Android only) to prevent re-purchasing until you manually mark it as consumed <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

### 8. Consuming a Product (`_spendCredits` method)

*   This method takes `PurchaseDetails` as an argument.
*   Decrement the `_credits` in your app's state <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   When the consumable is fully used (e.g., `_credits` reaches zero), call `_iapConnection.consumePurchase(purchaseDetails)` (specifically for Google Play Store) <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. This allows the user to purchase another instance of that product <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.