---
title: Firebase Cloud Messaging services
videoId: 2TSm2YGBT1s
---

From: [[fireship]] <br/> 

Firebase Cloud Messaging (FCM) is a service that enables developers to intelligently broadcast push notifications to users, enhancing user engagement and preventing app uninstalls when used correctly <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows for smart broadcasting of notifications <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

FCM allows messages to be received from a front-end Flutter app and broadcast from a back-end [[cloud_functions_and_integration_with_firebase | cloud function]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Notifications can be broadcast to a single device or user, to a topic, or to a segment of a user base using collected analytics data <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Combining these techniques allows for a sophisticated pipeline for app notifications <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Ways to Send Push Notifications with FCM

There are three primary methods for sending push notifications using Firebase Cloud Messaging:

1.  **To a Segment of Users**
    This is the broadest approach, allowing notifications to be sent to a specific segment of your user base <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Examples include all Android app users, or a more drilled-down audience like "Korean Android users whose last app engagement was more than ten days ago" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. FCM provides exact user counts and relative size to the total user base for these segments <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Firebase Predictions can also be used to dynamically segment users and send notifications based on desired engagement types <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

2.  **To a Topic**
    Users can be manually subscribed to a notification topic <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This is useful for user opt-in scenarios or programmatic assignment to topics in the app's background <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. For instance, a user following a "puppies" category could be subscribed to "puppy notifications" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Notifications to topics can be sent via the Firebase console or with a [[cloud_functions_and_integration_with_firebase | cloud function]] <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

3.  **To a Single Device or User**
    This is the most personalized method <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Every device with notification permission provides a unique token (a string identifier) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. These tokens can be saved to [[firestore_features_and_methods_for_handling_chat_data | Firestore]] and associated with a user, enabling notifications based on individual user activities <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Sending to individual device tokens is typically done programmatically with a [[cloud_functions_and_integration_with_firebase | cloud function]] <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Frontend Implementation with Flutter

A Flutter app needs to be configured with Firebase for both iOS and Android to use FCM <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Setup and Dependencies

*   **Android:** Add an intent filter to the Android manifest file for push notifications <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **iOS:** Register a certificate with the Apple Push Notification Service. A detailed official guide is available for this <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **`pubspec.yaml`:** Include `firebase_core`, `auth`, `cloud_firestore`, and `messaging` packages <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Imports:** Import `dart:io` for platform checking and Firebase services in the `main.dart` file <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Message Handling and UI

A `MessageHandler` stateful widget can manage user permissions, saving device tokens to the database, and displaying UI elements upon notification receipt <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

Three callbacks handle incoming messages:
*   `onMessage`: Called when the app is running in the foreground <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   `onResume`: Called when the app is in the background and the user clicks the notification <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   `onLaunch`: Runs if the app is terminated and the user clicks the notification, requiring a reboot <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

For Android, setting the `click_action` to `flutter_notification_click` is necessary to use background or terminated callbacks <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

*   **Displaying Notifications:**
    *   **Snack bar:** A subtle bar at the bottom, automatically dismissed if not engaged <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   **Alert dialog:** Interrupts the current experience, forcing manual dismissal for important messages <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **FCM Configuration:** `FCM.configure` sets up callbacks to handle message data payloads <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Permissions and Token Management

*   **iOS Permissions:** Explicit permission must be requested from the user by calling `FCM.requestNotificationPermission` with iOS notification settings <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Subscribing/Unsubscribing from Topics:** A single line of code handles subscription or unsubscription from a topic <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   **Saving Device Tokens to [[firestore_features_and_methods_for_handling_chat_data | Firestore]]:**
    *   Each device with permission provides an FCM token (a unique string) <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   These tokens are saved to a `tokens` sub-collection under a user's document in [[firestore_features_and_methods_for_handling_chat_data | Firestore]] <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   The device token itself is used as the document ID in the sub-collection to ensure uniqueness <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
    *   The `saveDeviceToken` method retrieves the FCM token using `get token` and then sets it in the [[firestore_features_and_methods_for_handling_chat_data | Firestore]] sub-collection, optionally including `createdAt` timestamps or platform OS <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   On Android, this code can run when the widget is initialized; on iOS, it runs after user permission is granted <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Backend Implementation with [[cloud_functions_and_integration_with_firebase | Cloud Functions]]

[[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]] are the ideal solution for dynamically sending notifications based on user activity <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### [[setting_up_firebase_cloud_functions | Setting up Firebase Cloud Functions]]

*   Run `firebase init functions` from the project root <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   Typescript is highly recommended <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   In `index.ts`, import and initialize `firebase-admin`, then set up variables for [[firestore_features_and_methods_for_handling_chat_data | Firestore]] and FCM <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Sending to Topics from [[firestore_features_and_methods_for_handling_chat_data | Firestore]] Changes

*   Notifications to topics are often triggered by database changes <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   Example: A [[data_modeling_in_firestore_chat_applications | Cloud Function]] can listen to the `onCreate` event in a `puppies` collection <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   When a new document is created, the function accesses the new data to create a notification payload <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   Notification customization: Use data from the [[firestore_features_and_methods_for_handling_chat_data | Firestore]] document to tailor the notification (e.g., "Puppy Name is ready for adoption") <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   Key properties: `title`, `body`, and `icon` dictate the appearance on the device's notification tray <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   Set `click_action` to `flutter_notification_click` for background callbacks <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   Send the notification by calling `FCM.sendToTopic` with the topic name and payload <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Sending to Individual Users from [[firestore_features_and_methods_for_handling_chat_data | Firestore]] Changes

*   A [[cloud_functions_and_integration_with_firebase | Cloud Function]] can listen to an `orders` collection to send a notification to an individual user upon a new order <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   When an order document is created (assuming it contains `price`, `product`, and `userID`), the function queries the `tokens` sub-collection under that `userID` to retrieve all device tokens for that specific user <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   Device tokens are mapped from snapshots to an array of document IDs <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   The message payload is formatted <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   `FCM.sendToDevice` is called with the array of tokens to send the push notification to every device owned by the user <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Deployment

The final step is to deploy the [[cloud_functions_and_integration_with_firebase | Cloud Functions]] <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Creating a document in [[firestore_features_and_methods_for_handling_chat_data | Firestore]] will then broadcast the notification <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. This establishes a full-stack solution for cloud messaging, capable of handling multiple app notification paradigms <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.