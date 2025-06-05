---
title: Optimizing chat app performance with cloud functions
videoId: LKAXg2drQJQ
---

From: [[fireship]] <br/> 

[[building_a_realtime_chat_app_with_firebase | Building a real-time chat app]] can be made almost trivial with Firebase, as its SDK manages state and data syncing between the client and server <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. A functional chat app can be built in as little as 24 hours using Angular, AngularFire, and [[firestore_features_and_methods_for_handling_chat_data | Firestore]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Data Modeling for Performance

One crucial aspect of [[data_modeling_in_firestore_chat_applications | data modeling]] for chat applications is managing the size of chat documents, especially when embedding messages directly within the chat document <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This approach, while fast and simple for initial loads, has limitations <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. Documents in [[firestore_features_and_methods_for_handling_chat_data | Firestore]] are limited to one megabyte of data, which translates to conservatively between 250 and 1,000 messages per document <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

To circumvent this size limitation and ensure optimal performance, especially for initial loads, a [[using_cloud_functions_for_backend_chatbot_integration | cloud function]] can be implemented <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Automating Message Management with Cloud Functions

A simple [[using_cloud_functions_for_backend_chatbot_integration | cloud function]] can automatically manage older messages by archiving or deleting them <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This strategy helps keep the document size small, ensuring that the initial load of a chat is always performant <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Cloud Function Implementation

The [[using_cloud_functions_for_backend_chatbot_integration | cloud function]] will:
*   Listen for updates to chat documents <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   Monitor the size of the `messages` array within each chat document <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   Trigger an action (archive or delete) if the array exceeds a predefined limit (e.g., more than 50 messages) <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.
*   Alternatively, check if the total character length of messages exceeds a threshold (e.g., 10,000 characters) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

```typescript
// Example cloud function structure (conceptual)
import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';

admin.initializeApp();
const firestore = admin.firestore();

export const archiveChat = functions.firestore
  .document('chats/{chatId}')
  .onUpdate(async (change, context) => {
    const chatData = change.after.data();
    if (!chatData || !chatData.messages) {
      return null;
    }

    const messages = chatData.messages;
    const documentRef = change.after.ref;

    // Check array size
    if (messages.length > 50) { <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>
      // Remove oldest messages
      const newMessages = messages.slice(messages.length - 50); // Keep last 50
      
      const batch = firestore.batch();
      batch.update(documentRef, { messages: newMessages });
      
      // Optional: Add deleted messages to another location (not shown here) <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>
      // This should be an atomic batch operation <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>
      
      await batch.commit();
      console.log('Messages archived/deleted due to length.');
      return;
    }

    // Check document size (conceptual, using stringify to estimate) <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>
    const totalMessageChars = JSON.stringify(messages).length;
    if (totalMessageChars > 10000) { <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>
      // Implement more complex logic to reduce size, e.g.,
      // by deleting older messages until size is below threshold.
      console.log('Messages archived/deleted due to character limit.');
      return;
    }

    return null; // No update if conditions not met <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>
  });
```

### Performance Benefits

The `cloud function` operates in the background, listening to incoming messages <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. When limits are reached, it archives or deletes the oldest messages <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>. This process exhibits very low latency, with round-trip times finishing in just a few hundred milliseconds <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. This ensures that the chat experience remains smooth and responsive, even as the number of messages grows.