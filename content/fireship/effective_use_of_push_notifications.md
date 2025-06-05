---
title: Effective use of push notifications
videoId: 2TSm2YGBT1s
---

From: [[fireship]] <br/> 

Push notifications can significantly drive user engagement when used correctly, but improper use can lead users to uninstall an application <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[Firebase Cloud Messaging services | Firebase Cloud Messaging]] (FCM) is a service that enables smart and targeted notification broadcasts <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Ways to Send Push Notifications with FCM

There are three primary methods for [[sending_targeted_notifications | sending targeted notifications]] using [[Firebase Cloud Messaging services | Firebase Cloud Messaging]]:

### To a Segment of Users
This is the broadest approach, allowing notifications to be sent to a specific user segment <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>. This can range from all users of an Android app to a more specific audience, such as Korean Android users whose last app engagement was over ten days ago <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a>. FCM provides analytics on the number of users who will receive the notification and their relative size to the total user base <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>. [[Design techniques in app development | Firebase Predictions]] can also be used for dynamic user segmentation, enabling notifications based on desired engagement types <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.

### To a Topic
Users can be manually subscribed to a notification topic, or programmatically assigned to one in the background of the app <a class="yt-timestamp" data-t="01:39:27">[01:39:27]</a>. This is useful for opt-in scenarios, such as a user following a specific category like "puppies" and receiving notifications related to that topic <a class="yt-timestamp" data-t="01:50:57">[01:50:57]</a>. Notifications to topics can be sent via the Firebase console or a [[Optimizing chat app performance with cloud functions | Cloud Function]] <a class="yt-timestamp" data-t="06:14:26">[06:14:26]</a>.

### To a Single Device or User
This is the most personalized method <a class="yt-timestamp" data-t="01:57:51">[01:57:51]</a>. Each device with permission to receive notifications provides a unique token, which is a string identifying the device <a class="yt-timestamp" data-t="02:02:18">[02:02:18]</a>. These tokens can be saved to [[working_with_firebase_firestore_and_realtime_updates | Firestore]] and associated with a user, allowing notifications to be sent based on individual user activities <a class="yt-timestamp" data-t="02:11:47">[02:11:47]</a>.

## Sending Notifications: Firebase Console vs. Cloud Functions

Notifications can be sent from the Firebase console or programmatically using [[Optimizing chat app performance with cloud functions | Cloud Functions]] <a class="yt-timestamp" data-t="02:21:05">[02:21:05]</a>. For most real-world applications, especially when sending to individual device tokens, [[Optimizing chat app performance with cloud functions | Cloud Functions]] are predominantly used for notification sending <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>.

## Front-End Setup with Flutter

A Flutter application needs to be configured with Firebase for both iOS and Android <a class="yt-timestamp" data-t="02:38:25">[02:38:25]</a>.

### Platform-Specific Configurations
*   **Android:** Add an intent filter to the `Android manifest` file to set up push notifications <a class="yt-timestamp" data-t="02:43:08">[02:43:08]</a>.
*   **iOS:** Register a certificate with the Apple Push Notification Service. A detailed official guide is available for this <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### Dependencies
The `pubspec.yaml` file requires `firebase_core`, `auth`, `cloud_firestore`, and `messaging` <a class="yt-timestamp" data-t="03:05:07">[03:05:07]</a>.

### Message Handling Callbacks
In the `main.dart` file, a `MessageHandler` widget manages notification permissions, device token saving, and UI display <a class="yt-timestamp" data-t="03:29:26">[03:29:26]</a>. Three callbacks are crucial for handling incoming messages:
*   `onMessage`: Called when the app is running in the foreground <a class="yt-timestamp" data-t="03:44:03">[03:44:03]</a>.
*   `onResume`: Called when the app is in the background and the user clicks the notification <a class="yt-timestamp" data-t="03:52:43">[03:52:43]</a>.
*   `onLaunch`: Called if the app is terminated and the user clicks the notification, requiring a reboot <a class="yt-timestamp" data-t="04:00:27">[04:00:27]</a>.

For Android, set the `click_action` to `FLUTTER_NOTIFICATION_CLICK` to utilize background or terminated callbacks <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>.

### Displaying Notifications in UI
In-app notifications can be displayed using:
*   **Snack Bar:** A subtle bar at the bottom that dismisses automatically if not engaged with <a class="yt-timestamp" data-t="04:25:21">[04:25:21]</a>.
*   **Alert Dialog:** Interrupts the current experience for important messages, forcing manual dismissal <a class="yt-timestamp" data-t="04:31:07">[04:31:07]</a>.

### Requesting Permissions (iOS)
On iOS, explicit permission from the user is required by calling `FCM.requestNotificationPermission` <a class="yt-timestamp" data-t="05:41:40">[05:41:40]</a>.

### Subscribing to Topics
Users can be subscribed to or unsubscribed from a topic with a single line of code <a class="yt-timestamp" data-t="06:01:31">[06:01:31]</a>.

### Saving Device Tokens to Firestore
To send notifications to individual users, the FCM token from the device needs to be retrieved and saved in a backend database like [[working_with_firebase_firestore_and_realtime_updates | Firestore]] <a class="yt-timestamp" data-t="06:26:40">[06:26:40]</a>.

#### Database Model for Tokens
A `users` collection holds user profiles, with a `tokens` subcollection under each user document <a class="yt-timestamp" data-t="06:35:05">[06:35:05]</a>. Each document in the `tokens` subcollection represents a device token, using the token string itself as the document ID to ensure uniqueness <a class="yt-timestamp" data-t="06:42:07">[06:42:07]</a>. Optional information like `createdAt` timestamp or platform OS can also be saved <a class="yt-timestamp" data-t="07:23:09">[07:23:09]</a>.

#### Saving Token Code
The `saveDeviceToken` method retrieves the FCM token by calling `getToken` and then saves it to the appropriate token subcollection under the user's ID <a class="yt-timestamp" data-t="07:02:16">[07:02:16]</a>. For Android, this can run upon widget initialization, while iOS requires listening to a stream to ensure permission is granted before saving <a class="yt-timestamp" data-t="07:34:04">[07:34:04]</a>.

## Back-End Logic with Firebase Cloud Functions

[[Optimizing chat app performance with cloud functions | Firebase Cloud Functions]] are ideal for dynamically sending notifications based on user activity <a class="yt-timestamp" data-t="08:08:52">[08:08:52]</a>. Initialize Firebase admin SDK, and set up variables for [[working_with_firebase_firestore_and_realtime_updates | Firestore]] and FCM <a class="yt-timestamp" data-t="08:30:33">[08:30:33]</a>.

### Sending to a Topic (e.g., New Puppy Adoption)
A [[Optimizing chat app performance with cloud functions | Cloud Function]] can listen to a [[working_with_firebase_firestore_and_realtime_updates | Firestore]] `onCreate` event in a collection (e.g., `puppies`) <a class="yt-timestamp" data-t="08:50:56">[08:50:56]</a>. When a new document is created, the function can access the document's data to customize a notification payload, for example, "Puppy Name is ready for adoption" <a class="yt-timestamp" data-t="08:57:24">[08:57:24]</a>.

*   **Notification Payload:** Key properties include `title`, `body`, and `icon`, which determine the notification's appearance <a class="yt-timestamp" data-t="09:17:29">[09:17:29]</a>. The `click_action` should be set to `FLUTTER_NOTIFICATION_CLICK` to enable background callbacks <a class="yt-timestamp" data-t="09:24:26">[09:24:26]</a>.
*   **Sending:** Call `FCM.sendToTopic` with the topic name and notification payload <a class="yt-timestamp" data-t="09:33:04">[09:33:04]</a>.

### Sending to an Individual User (e.g., New Order)
Another [[Optimizing chat app performance with cloud functions | Cloud Function]] can listen to an `orders` collection for `onCreate` events <a class="yt-timestamp" data-t="09:47:48">[09:47:48]</a>.
*   **Token Retrieval:** The function queries the `tokens` subcollection under the relevant user ID in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] to get all device tokens for that user <a class="yt-timestamp" data-t="10:04:22">[10:04:22]</a>.
*   **Sending:** Format the message payload and use `FCM.sendToDevice` with the array of retrieved tokens to send a push notification to every device owned by that user <a class="yt-timestamp" data-t="10:28:03">[10:28:03]</a>.

Finally, deploy the [[Optimizing chat app performance with cloud functions | Cloud Functions]] <a class="yt-timestamp" data-t="10:37:11">[10:37:11]</a>.