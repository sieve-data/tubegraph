---
title: User authentication and profile management in chat apps
videoId: LKAXg2drQJQ
---

From: [[fireship]] <br/> 

Building a [[building_a_realtime_chat_app_with_firebase | real-time chat app]] can be made almost trivial with Firebase, as its SDK handles state management and data syncing between the client and server <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This allows for rapid development, with an entire [[building_a_realtime_chat_app_with_firebase | chat app]] having been built in 24 hours using AngularFire and Firestore <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Core Requirements for Chat Applications
Every chat application requires a robust [[user_authentication_with_firebase | user authentication system]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This system is essential for managing user data and ensuring secure interactions. Along with authentication, public user profile information should be saved in a "users" collection in Firestore <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Implementing the Authentication Service
The authentication service is responsible for logging users in and saving their information to Firestore <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Key Aspects of the Authentication Service:
*   **Listening to Auth State**: The service listens to the AngularFire authentication state, which represents the currently authenticated user <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Fetching User Profiles**: It then queries Firestore to retrieve a related user document containing their profile information <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **Authentication Methods**: The service includes methods for signing users in (e.g., with Google) and signing out <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **`getUser` Method**: A specific `getUser` method converts the user observable into a promise, simplifying its use with `async/await` for writing data to Firestore <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Integrating User Data with Chat
When a user creates a new chat, a document is generated with their user ID as the `owner ID` <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This provides a unique URL that can be shared, allowing other [[user_authentication_with_firebase | authenticated users]] to participate <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. While the presented example features public chats, more advanced [[implementing_security_rules_and_user_authentication | user authorization]] in Firestore can be explored for private chat features <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Displaying User Profiles in Messages
To ensure chat messages always display the most recent user profile image and username, an advanced RxJS technique is employed to join user profiles to individual chat messages <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Process for Joining User Profiles:
1.  **Identify Unique User IDs**: The original chat document is processed to find all unique user IDs within its messages array <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
2.  **Concurrent Profile Reading**: All identified user profiles are read concurrently using the `combinedLatest` method <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
3.  **Recompose Messages**: The original messages object is recomposed so that each message includes a `user` property containing the user's profile data <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

This results in a single object containing all chat messages and their associated user profiles, all synced in real-time <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.