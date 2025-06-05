---
title: Secure and efficient data modeling for chat applications
videoId: gUYBFDPZ5qk
---

From: [[fireship]] <br/> 

Building a full-stack chat application requires careful consideration of data modeling for both efficiency and security <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. This article explores an approach using PocketBase as the backend, combined with Svelte for the frontend, deployed on a Linux server <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.

## PocketBase as a Backend Solution

PocketBase is a free and open-source alternative to Firebase, written in Go, offering [[user_authentication_and_profile_management_in_chat_apps | user authentication]] and a real-time database powered by SQLite <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. A key advantage of PocketBase is its compilation into a single executable, simplifying self-hosting requirements to just one server <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## Data Modeling with PocketBase

[[Using Firebase databases and data modeling techniques | Data modeling]] in PocketBase begins by accessing its admin dashboard <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.

### Core Collections

1.  **Users Collection**: By default, PocketBase includes a `users` collection containing fields such as username, email, and password, managing application users <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
2.  **Messages Collection**: To manage chat messages, a `messages` collection is created with two primary fields <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>:
    *   `text`: Stores the content of the message <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>. Server-side validations like minimum and maximum length can be applied here <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.
    *   `user`: Establishes a one-to-many relationship, indicating that a message belongs to a specific user <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. Under the hood, PocketBase creates a foreign key for the user ID on the messages table in the SQLite database <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

### Retrieving Relational Data

PocketBase simplifies the retrieval of relational data. When fetching messages, the `expand` option can be used to automatically include the associated user data (e.g., username) without complex SQL joins <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This allows displaying message text alongside the sender's username and avatar <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.

## Securing Data with API Rules

PocketBase allows defining API rules for each collection, determining who can access data from a frontend application <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>.

### Messages Collection Rules

*   **View/List**: To allow anyone to view messages, the API rule for list and view actions should be unlocked <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>.
*   **Create**: Users must only be able to create messages associated with their own user ID. This is enforced by ensuring the `user` property of the message is equal to the `request.auth.id` <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This eliminates significant backend code complexity <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>.

### Users Collection Rules

*   **View/List**: To allow users to view each other's profiles, the rules for view and list actions on the `users` collection should be removed, making this data public <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

### Production Readiness

For production, it's recommended to:
*   Bring a custom domain over to the hosting provider <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.
*   Utilize Let's Encrypt through PocketBase to automatically generate an SSL certificate for HTTPS <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>.
*   Mount a separate volume for the `pb_data` directory, where PocketBase stores all data, allowing it to be moved between servers <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
*   Set up a systemd service to automatically restart PocketBase whenever the server reboots <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

## Efficient Real-time Updates and Scaling

Svelte's built-in reactive stores are highly effective for [[building_a_realtime_chat_app_with_firebase | real-time UIs]] <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.

### Real-time Chat Messages

To achieve real-time message updates:
*   Subscribe to the `messages` collection using `pb.collection('messages').subscribe('*')` <a class="yt-timestamp" data-t="11:40:00">[11:40:00]</a>. This callback fires whenever a message is created, updated, or deleted <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
*   Update the frontend's messages array when new messages are created or deleted <a class="yt-timestamp" data-t="11:57:00">[11:57:00]</a>.
*   Crucially, unsubscribe from the real-time listener using the `on_destroy` lifecycle hook in Svelte to prevent memory leaks and unnecessary database reads <a class="yt-timestamp" data-t="12:19:00">[12:19:00]</a>.

### Scaling PocketBase

PocketBase typically scales vertically, meaning that as website traffic grows, the server requires more CPU and RAM <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>. This can be easily accomplished by resizing the server, for instance, on platforms like Linode <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. A larger server can handle tens of thousands of concurrent users, making it adequate for the vast majority of projects <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.