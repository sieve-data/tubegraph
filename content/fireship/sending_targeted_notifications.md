---
title: Sending targeted notifications
videoId: 2TSm2YGBT1s
---

From: [[fireship]] <br/> 

When utilized effectively, [[effective_use_of_push_notifications | push notifications]] can significantly enhance user engagement <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Conversely, improper use can lead users to uninstall an application <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Fortunately, [[firebase_cloud_messaging_services | Firebase Cloud Messaging]] (FCM) provides a robust service for intelligent notification broadcasting <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

This guide will cover how to receive messages on a Flutter front-end and broadcast them from a backend [[optimizing_chat_app_performance_with_cloud_functions | Cloud Function]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It will explore sending notifications to a single device or user, to a specific topic, or to a segment of your user base based on analytics data <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Ways to Send Push Notifications with FCM

[[firebase_cloud_messaging_services | Firebase Cloud Messaging]] offers three primary methods for sending [[effective_use_of_push_notifications | push notifications]]:

### 1. Sending to a Segment of Users

This is the broadest approach, allowing notifications to be sent to a specific user segment <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. While it can target all users for an app (e.g., all Android users), it's typically used to target a smaller, more refined audience <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. For example, you can target Korean Android users whose last app engagement was over ten days ago <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. [[firebase_cloud_messaging_services | Firebase Predictions]] can also be used to dynamically segment users and send notifications based on desired engagement types <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### 2. Sending to a Notification Topic

Users can be manually subscribed to a notification topic <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This is useful for user opt-in scenarios or for programmatically assigning them to a topic in the app's background <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. For instance, if a user follows a category like "puppies," they can be subscribed to "puppy notifications" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Notifications to a topic can be sent via the Firebase Console or a [[optimizing_chat_app_performance_with_cloud_functions | Cloud Function]] <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### 3. Sending to a Single Device or User

This is the most personalized way to send notifications <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Every device with permission to receive notifications provides a unique token, which is a string identifying the device <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. These tokens can be saved to [[working_with_firebase_firestore_and_realtime_updates | Firestore]] and associated with a user, enabling notifications based on individual user activities <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. In real-world applications, most individual device token notifications are sent programmatically using [[optimizing_chat_app_performance_with_cloud_functions | Cloud Functions]] <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Front-End Implementation (Flutter)

A Flutter app needs to be configured with Firebase for both iOS and Android <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Platform-Specific Setup

*   **Android:** Add an intent filter to the Android manifest file for push notifications <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **iOS:** More steps are involved, requiring registration of a certificate with the Apple push notification service <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. An official detailed guide is available for this <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Dependencies

Ensure the `pubspec.yaml` file includes `firebase_core`, `firebase_auth`, `cloud_firestore`, and `firebase_messaging` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Handling Notification Callbacks

A `MessageHandler` stateful widget can manage user permissions, device token saving, and UI display upon notification receipt <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. There are three key callbacks for handling notification UI:

1.  **`onMessage`:** Called when the app is in the foreground (user actively using the app) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
2.  **`onResume`:** Called when the app is in the background, and the user clicks on the notification from the device <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
3.  **`onLaunch`:** Called if the user clicks on the notification when the app is completely terminated and needs to reboot <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

For Android, set the `click_action` to `FLUTTER_NOTIFICATION_CLICK` to use background or terminated callbacks <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Displaying Notifications

When an `onMessage` callback is triggered (app in foreground), notifications can be displayed using:

*   **SnackBar:** A subtle bar at the bottom that dismisses automatically <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **AlertDialog:** Interrupts the current experience, requiring manual dismissal from the user <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

The `FCM.configure` method sets up these callbacks, providing access to the notification data payload <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Requesting iOS Permission

On iOS, explicit user permission is required <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This is done by calling `FCM.requestNotificationPermission` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Subscribing/Unsubscribing to Topics

Users can be subscribed or unsubscribed from a topic with a single line of code <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This can happen in the background or via a user interface element <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

### Saving Device Tokens to Firestore

To send notifications to individual users, the FCM token from the device needs to be retrieved and saved to a backend database like [[working_with_firebase_firestore_and_realtime_updates | Firestore]] <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

#### Database Model
A `users` collection contains user profiles, with a subcollection called `tokens` <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Each document in the `tokens` subcollection represents a device token, using the unique device token string as its document ID for uniqueness <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

#### Implementation
1.  Implement a `saveDeviceToken` method <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
2.  Retrieve the FCM token using `get token` <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
3.  Create a reference to the token subcollection under the user, using the FCM token as the document ID <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
4.  Save the token along with optional information like creation timestamp or platform OS <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
5.  In the widget's `initState`, call `saveDeviceToken` <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. For Android, this can run on initialization, but for iOS, it should wait for user permission to be granted by listening to the stream <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Back-End Implementation (Firebase Cloud Functions)

For dynamically sending notifications based on user activity, [[optimizing_chat_app_performance_with_cloud_functions | Firebase Cloud Functions]] are the recommended solution <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Setup

Initialize [[optimizing_chat_app_performance_with_cloud_functions | Firebase Cloud Functions]] from your project root using `firebase init functions` and select TypeScript as the language <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

In the `index.ts` file:
1.  Import and initialize `firebase-admin` <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
2.  Set up variables for [[working_with_firebase_firestore_and_realtime_updates | Firestore]] and FCM <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

### Sending to a Specific Topic

To send notifications to a specific topic when database changes occur (e.g., a new document is added to a "puppies" collection), set up a [[optimizing_chat_app_performance_with_cloud_functions | Cloud Function]] that listens to the [[working_with_firebase_firestore_and_realtime_updates | Firestore]] `onCreate` event for that collection <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

1.  The `onCreate` event provides access to the new document's data <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
2.  Create a notification payload, customizing it with data from the [[working_with_firebase_firestore_and_realtime_updates | Firestore]] document (e.g., "Puppy name is ready for adoption") <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
3.  Important properties for the notification are `title`, `body`, and `icon` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
4.  Set `click_action` to `FLUTTER_NOTIFICATION_CLICK` to enable background callbacks <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
5.  Send the notification using `FCM.sendToTopic` with the topic name and payload <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Sending to an Individual User

To send notifications to an individual user, for example, when they receive a new order:

1.  Write a [[optimizing_chat_app_performance_with_cloud_functions | Cloud Function]] that listens to the `orders` collection's `onCreate` event <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
2.  Assuming the order document contains a `userId`, use this ID to query the `tokens` subcollection under that `userId` in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
3.  Map the query snapshots to an array of document IDs, which are the FCM tokens <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
4.  Format the message payload similar to previous examples <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
5.  Send the notification using `FCM.sendToDevice` with the array of tokens <a class="yt-timestamp" data-t="00:10:28">[0:10:28]</a>. This sends a [[effective_use_of_push_notifications | push notification]] to every device owned by that user <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

### Deployment

The final step is to deploy the [[optimizing_chat_app_performance_with_cloud_functions | Cloud Functions]] <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. After deployment, creating a document in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] (e.g., in the `orders` or `puppies` collection) should trigger the function and broadcast the notification to the target device or emulator <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.