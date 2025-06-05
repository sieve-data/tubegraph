---
title: Setting up Firebase Cloud Functions
videoId: 2TSm2YGBT1s
---

From: [[fireship]] <br/> 

[[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]] are an effective way to dynamically send push notifications based on user activity or database changes within your application <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. While [[introduction_to_firebase_and_benefits | Firebase]] provides other SDKs to send messages, most real-world applications handle notification sending via [[cloud_functions_and_integration_with_firebase | Cloud Functions]], especially for individual device tokens <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Initializing Firebase Cloud Functions

To begin using [[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]] in your project, navigate to the root of your project directory and run `firebase init functions` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. It is highly recommended to use TypeScript as the language for your functions <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

Once initialized, open the `index.ts` file. You will need to import and initialize `firebase-admin`, then set up variables for `firestore` and `FCM` (Firebase Cloud Messaging) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

```typescript
import * as admin from 'firebase-admin';
admin.initializeApp();
const firestore = admin.firestore();
const fcm = admin.messaging();
```

## Sending Notifications with Cloud Functions

[[cloud_functions_and_integration_with_firebase | Cloud Functions]] allow you to programmatically broadcast notifications based on various triggers, such as changes in your [[setting_up_and_managing_firebase_projects | Firebase]] database.

### Sending to a Topic

You can send notifications to a specific topic, typically when something changes in the database that is relevant to that topic <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. For example, if you have a "puppies" collection and want to notify users subscribed to the "puppies" topic when a new document is added <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

To achieve this, you can set up a [[cloud_functions_and_integration_with_firebase | Cloud Function]] that listens to the `firestore.onCreate` event in the target collection <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

```typescript
// Example: Notifying about new puppies
export const newPuppyNotification = functions.firestore
    .document('puppies/{puppyId}')
    .onCreate(async (snapshot, context) => {
        const puppyData = snapshot.data();
        const notificationPayload = {
            notification: {
                title: 'New Puppy Alert!',
                body: `${puppyData.name} is ready for adoption!`,
                icon: 'your_icon_url', // Optional
                click_action: 'FLUTTER_NOTIFICATION_CLICK' // Required for background/terminated app callbacks on Android
            }
        };

        // Send to a specific topic
        await fcm.sendToTopic('puppies', notificationPayload);
    });
```

The notification payload can be customized using data from the `firestore` document itself <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Key properties include `title`, `body`, and `icon`, which dictate how the notification appears <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. For Android, setting `click_action` to `FLUTTER_NOTIFICATION_CLICK` is crucial for enabling background or terminated app callbacks <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. The final step is to call `fcm.sendToTopic` with the topic name and payload <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### Sending to an Individual User/Device

To send notifications to an individual user or device, you'll need to retrieve the FCM token from the device and save it in a back-end database like Firestore <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

#### Database Model for Device Tokens

A common approach is to have a `users` collection, with a `tokens` sub-collection under each user document. Each document in this sub-collection represents a device token for which the user has granted notification permission <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The unique device token string itself can serve as the document ID in the sub-collection to ensure uniqueness <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

```
/users/{userId}
    /tokens/{deviceTokenId}
        {
            createdAt: timestamp,
            platform: "android" | "ios"
        }
```

#### Cloud Function for Individual Notifications

You can create a [[cloud_functions_and_integration_with_firebase | Cloud Function]] that listens to a collection like `orders` to send a notification to an individual user when they receive a new order <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

```typescript
// Example: Notifying about new orders to individual users
export const newOrderNotification = functions.firestore
    .document('orders/{orderId}')
    .onCreate(async (snapshot, context) => {
        const orderData = snapshot.data();
        const userId = orderData.userId; // Assume order document has a userId

        // Query the tokens sub-collection for the specific user
        const tokensSnapshot = await firestore
            .collection('users')
            .doc(userId)
            .collection('tokens')
            .get();

        // Map snapshots to an array of device tokens
        const tokens = tokensSnapshot.docs.map(doc => doc.id);

        if (tokens.length === 0) {
            console.log('No device tokens found for user:', userId);
            return null;
        }

        const notificationPayload = {
            notification: {
                title: 'New Order Received!',
                body: `You have a new order for ${orderData.product} at $${orderData.price}.`,
                click_action: 'FLUTTER_NOTIFICATION_CLICK'
            }
        };

        // Send to an array of device tokens
        await fcm.sendToDevice(tokens, notificationPayload);
    });
```

This function takes the `userId` from the new order document and queries the `tokens` sub-collection for that user to retrieve all their device tokens <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. It then formats a message payload and uses `fcm.sendToDevice` with the array of tokens to send the push notification to every device owned by that user <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

## Deploying Cloud Functions

After writing your [[cloud_functions_and_integration_with_firebase | Cloud Functions]], the final step is to deploy them <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. Once deployed, creating a document in the relevant `firestore` collection (e.g., `puppies` or `orders`) should trigger the [[cloud_functions_and_integration_with_firebase | Cloud Function]] and broadcast the notification to your emulator or local device <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.