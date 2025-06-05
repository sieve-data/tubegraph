---
title: Flutter app integration with Firebase
videoId: 2TSm2YGBT1s
---

From: [[fireship]] <br/> 

Push notifications can significantly drive user engagement when used correctly, but improper use can lead to app uninstallation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[Cloud functions and integration with Firebase | Firebase Cloud Messaging]] (FCM) provides a service for intelligent notification broadcasting <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This integration allows Flutter applications to receive messages from the front-end and broadcast them from a backend [[Setting up Firebase Cloud Functions | cloud function]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Ways to Send Push Notifications with Firebase Cloud Messaging

There are three primary methods for sending push notifications using FCM <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:

1.  **To a Segment of Users**
    This is the broadest approach, allowing targeting of specific user groups <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. For example, notifications can be sent to "all Android app users" or more specifically to "Korean Android users whose last app engagement was more than ten days ago" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. [[Enhancing applications with Firebase extensions and integrations | Firebase predictions]] can dynamically segment users based on desired engagement types <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
2.  **To a Notification Topic**
    Users can be manually subscribed to specific topics, or topics can be assigned programmatically in the app's background <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This is useful for opt-in scenarios, such as a user following a "puppies" category and receiving related notifications <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Notifications can be sent to all devices subscribed to a topic via the Firebase console or a [[Setting up Firebase Cloud Functions | Cloud Function]] <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
3.  **To a Single Device or User**
    This is the most personalized method <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Each device that grants permission for notifications provides a unique token, which is a string identifying the device <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. These tokens can be saved in a database like Firestore and associated with a user, enabling notifications based on individual user activities <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

Notification sending can be performed from the Firebase console or programmatically using a [[Setting up Firebase Cloud Functions | Cloud Function]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. For most real-world applications, especially when sending to individual device tokens, [[Setting up Firebase Cloud Functions | Cloud Functions]] are predominantly used <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Setting up FCM in a Flutter App

A Flutter app must be configured with Firebase for both iOS and Android to integrate FCM <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Platform-Specific Setup

*   **Android**: An optional step is to add an intent filter to the `Android manifest` file to set up push notifications <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **iOS**: More steps are required, involving registering a certificate with the Apple Push Notification Service <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. An official guide is available for this process <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Dependencies

The `pubspec.yaml` file should include the following Firebase dependencies <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>:
*   `firebase_core`
*   `firebase_auth`
*   `cloud_firestore`
*   `firebase_messaging`

### Handling Messages in Flutter

The business logic for handling messages is typically managed within a stateful widget, such as a `MessageHandler` widget <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This widget handles user permission, saving device tokens, and displaying UI elements upon notification receipt <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

FCM provides three callbacks to manage message reception based on app state <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>:

*   **`onMessage`**: Called when the app is running in the foreground <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **`onResume`**: Called when the app is in the background and the user clicks on the notification <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **`onLaunch`**: Called if the app is terminated and needs to reboot when the user clicks on the notification <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

For Android, setting the `click_action` to `FLUTTER_NOTIFICATION_CLICK` is necessary to use background or terminated callbacks <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Inside the `initState` of the widget, `FCM.configure()` is called to set up these callbacks <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Each callback provides access to the notification data payload <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Displaying Notifications in the UI

*   **Snack Bar**: A subtle bar displayed at the bottom of the screen, automatically dismissed if not engaged with <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. It can display the notification title and optionally include an action to navigate to a different screen <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Alert Dialog**: Used for important messages that should interrupt the user's current experience, forcing manual dismissal <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. It can display the title and body of the notification <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

### Requesting Permissions

On iOS, explicit user permission is required to receive notifications <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. This is done by calling `FCM.requestNotificationPermissions()` and passing in `iOSNotificationSettings` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

### Subscribing to Topics

Users can subscribe or unsubscribe from a topic with a single line of code <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. This can be done in the background or triggered by a UI element <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## Saving Device Tokens to Firestore

To send notifications to individual users or devices, the FCM token from the device must be retrieved and saved in a backend database like Firestore <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Database Model

A `users` collection contains user profiles <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Under each user, a sub-collection named `tokens` stores device tokens <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. Each document in this `tokens` collection represents a device token, and the unique device token string itself serves as the document ID to enforce uniqueness <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Flutter Code to Save Tokens

A `saveDeviceToken` method is implemented to retrieve the FCM token using `getToken()` <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This token is then used as the document ID in the `tokens` sub-collection under the current user's ID <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. Optional information like `createdAt` timestamp or `platform` operating system can also be saved <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

The `saveDeviceToken` method is called in the `initState` of the widget <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. On Android, it can run directly as the token is usually available <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. On iOS, it should wait for user permission by listening to a stream and then saving the token once data is available <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

## Dynamically Sending Notifications with Firebase Cloud Functions

[[Setting up Firebase Cloud Functions | Firebase Cloud Functions]] are the recommended way to dynamically send notifications based on user activity <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Initializing functions involves running `firebase init functions` and using TypeScript <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

### Setting up Firebase Admin

In the `index.ts` file, `firebase-admin` is imported and initialized, and variables for Firestore and FCM are set up <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

### Sending to a Topic (e.g., New Document in Collection)

A [[Setting up Firebase Cloud Functions | cloud function]] can listen to `onCreate` events in a Firestore collection (e.g., `puppies`) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. When a new document is created, the function accesses the document data to customize a notification payload <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

Important notification properties include:
*   `title`
*   `body`
*   `icon`
*   `click_action` (set to `FLUTTER_NOTIFICATION_CLICK` for background callbacks) <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>

The notification is sent by calling `fcm.sendToTopic()` with the topic name and payload <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### Sending to an Individual User (e.g., New Order)

Another [[Setting up Firebase Cloud Functions | cloud function]] can listen to an `orders` collection <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. When an order document is created, it assumes `price`, `product`, and `userId` fields <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

The function uses the `userId` to query the `tokens` sub-collection to retrieve all device tokens for that specific user <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. The snapshot results are mapped to an array of document IDs (which are the FCM tokens) <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. A message payload is formatted, and `fcm.sendToDevice()` is called with the array of tokens to send a push notification to every device owned by that user <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

After deploying the functions, creating a document in Firestore should trigger the notification broadcast to the emulator or local device <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. This establishes a full-stack solution for cloud messaging, capable of handling various app notification paradigms <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.