---
title: Realtime database and user authentication with Pocketbase
videoId: gUYBFDPZ5qk
---

From: [[fireship]] <br/> 

Pocketbase is a relatively new, free, and open-source backend tool written in Go [00:00:53]. It functions similarly to Firebase but offers user authentication and a [[RealTime Database Implementation | real-time database]] powered by SQLite [00:00:58]. A key differentiator of Pocketbase is its ability to compile everything into a single executable, allowing for self-hosting on a single, low-cost server [00:01:05]. This simplicity makes it efficient for development [00:01:17]. Pocketbase provides both a REST API and an admin dashboard [00:03:23].

## Deploying Pocketbase

To get started, Pocketbase can be [[deploying_pocketbase_to_a_linux_server | deployed to a Linux server in the cloud]] [00:01:20]. The process involves:
*   Spinning up a Linux server, for example, using Linode [00:01:46].
*   Downloading and unzipping the Pocketbase executable for Linux [00:02:17].
*   Using secure shell (SSH) to access the server and secure copy (SCP) to upload the executable to a chosen directory [00:02:37].
*   Running the `pocketbase serve` command on the server, specifying the HTTP flag with the server's IP address and Port 80 to make it accessible over the internet [00:03:10].
*   For a production setup, it's recommended to bring a domain over to the server, as Pocketbase uses Let's Encrypt to automatically generate an SSL certificate for HTTPS [00:03:35].
*   Mounting a volume to the `PB_data` directory is also advised, as this is where Pocketbase stores all data, providing a portable file system [00:03:50].
*   Finally, setting up a systemd service ensures Pocketbase automatically restarts if the server reboots [00:04:04].

## Data Modeling for a Chat Application

For a chat application, the database schema needs two collections:
*   **Users**: By default, Pocketbase includes a `users` collection with fields like username and email [00:04:17].
*   **Messages**: A new collection named `messages` is created with two fields:
    *   `text`: For the message content, with optional server-side validations like min/max length [00:04:34].
    *   `user`: This field creates a one-to-many relationship, indicating that a message belongs to a user [00:04:42]. Pocketbase automatically creates a foreign key for the user ID on the messages table in the SQLite database [00:04:47].

## Implementing Security Rules and User Authentication

[[implementing_security_rules_and_user_authentication | Security rules]] in Pocketbase determine who can access data from a front-end application [00:05:02].
*   **Messages Collection**:
    *   Initially, only admin users can access messages [00:05:10]. To allow anyone to view messages, the "list" and "view" rules are unlocked [00:05:16].
    *   Users need to be able to create new messages. The rule for creating messages should enforce that the `user` property of the message is equal to the `request.auth.userId`, ensuring users only create messages associated with their own ID [00:05:20].
*   **Users Collection**:
    *   Default rules are built-in, but to allow users to view each other's profiles, the "view" and "list" rules are removed [00:05:38].

[[User authentication with Firebase | User authentication]] and profile management in chat apps with Pocketbase can be managed by providing a way to listen to the current user in real time from anywhere in the application [00:06:24].
*   The Pocketbase JavaScript SDK is installed [00:06:33].
*   Pocketbase is initialized with its hosted URL (e.g., the Linode IP address) [00:06:42].
*   A `writable` store is created for the `currentUser`, defaulting to the Pocketbase `authStore.model`, which is `null` if no user is logged in or contains the user's database record (ID, username, etc.) [00:06:49].
*   The `onAuthChange` event is subscribed to, updating the Svelte store with the current user model when a user signs in or out [00:07:07].
*   To sign in a user, the `pb.collection('users').authWithPassword(username, password)` method is called [00:08:02].
*   To sign up a new user, initial data (username, password, custom fields) is prepared, then `pb.collection('users').create(data)` is used, followed by `authWithPassword` to log them in [00:08:17].
*   A `signOut` function is implemented by calling `pb.authStore.clear()` [00:08:44].

## Building a Chat Application with Svelte and Real-time Updates

A full stack [[building_a_chat_app_with_pocketbase_and_svelte | chat app]] can be built using Svelte for the frontend [00:05:25]. Svelte is well-suited for building [[realtime_database_implementation | real-time UIs]] due to its reactive stores [00:06:01].

For [[working_with_firebase_firestore_and_realtime_updates | real-time updates]] of chat messages:
*   Initial messages are fetched using `pb.collection('messages').getList(1, 50, { sort: 'created', expand: 'user' })` on component mount [00:09:36]. The `expand` option is crucial for including relational user data directly with each message without complex SQL joins [00:10:01].
*   Messages are rendered in a Svelte `each` block, displaying message text, username, and a unique avatar [00:10:24].
*   To send a message, a function `sendMessage` uses `pb.collection('messages').create({ text: newMessageText, user: $currentUser.id })` [00:11:01].
*   To achieve real-time updates without page refreshes, `pb.collection('messages').subscribe('*', (e) => { ... })` is used within the `onMount` callback [00:11:40]. This subscribes to the entire messages collection and runs a callback whenever a message is created, updated, or deleted [00:11:48].
    *   When a new message is created, the local messages array is updated with the new record [00:12:01]. Note that real-time updates do not include expanded user records by default, but they can be fetched with a `getOne` query if needed [00:12:07].
    *   For delete actions, the message ID is filtered out from the local array [00:12:13].
*   It's crucial to unsubscribe from real-time listeners when the component is destroyed (e.g., when the user logs out or navigates away) to prevent memory leaks and unnecessary database reads [00:12:19]. The `subscribe` method returns an `unsubscribe` function that can be called in Svelte's `onDestroy` lifecycle hook [00:12:28].

## Scaling Pocketbase

As a website grows, Pocketbase will need to [[scaling_pocketbase_applications_on_the_cloud | scale vertically]] with more CPU and RAM to handle increased traffic [00:13:05]. This is easily accomplished by resizing the server [00:13:13]. A larger server can handle tens of thousands of concurrent users, which should be adequate for most projects [00:13:16].