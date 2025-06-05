---
title: User authentication with decentralized apps
videoId: J5x3OMXjgMc
---

From: [[fireship]] <br/> 

This article describes how [[user_authentication_with_firebase | user authentication]] is implemented in a [[decentralized_chat_application | decentralized chat app]] built using Gun.js and Svelte. This approach moves away from traditional centralized control by big tech companies, distributing data and infrastructure across the user base <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Core Concepts of Gun.js for Authentication

Gun.js is a decentralized graph database that distributes data among users based on what they consume in the application <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Unlike a traditional database where data resides on a central server, Gun.js allows users to store a subset of data locally, syncing with other peers on the network using technologies like WebRTC <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This model is conceptually similar to a blockchain ledger, where no single entity controls the entire network, though Gun.js is not blockchain technology itself, as it's typically too slow for real-time applications like chat <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Cryptography and Key Pairs
[[implementing_cryptographic_concepts_in_blockchain_development | Cryptography]] plays a crucial role in Gun.js for [[user_authentication_and_profile_management_in_chat_apps | user authentication]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. When a new user account is created, a cryptographically secure key pair is generated <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>:
*   **Public Key**: The username is associated with a public key, allowing the system to locate past messages and data belonging to that user <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Proof-of-Work Seed**: The password acts as a proof-of-work seed, used to prove access and decrypt the account's private keys <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

This cryptographic foundation also enables the implementation of end-to-end encryption for messages <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Data Persistence
By default, Gun.js data is stored in the browser's local storage (limited to 5 MB) <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. For production-grade applications, it's recommended to deploy a relay server using a different storage mechanism, like Radix, which can store significantly more data on a server's disk <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This makes the network more robust by allowing queries to fall back to a relay if data isn't available from another peer <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Public Data Exposure
When a node is created in the Gun.js database, it becomes available to the entire decentralized network <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This means public data can be accessed by knowing the name of the node where it's stored <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. While encryption is possible, it requires a different mental model than traditional centralized databases <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

## [[implementing_angular_and_firestore_for_authorization | Implementing User Authentication]] with Svelte and Gun.js

The example decentralized chat application uses Svelte for the frontend UI and focuses on email/password [[user_authentication_and_profile_management_in_chat_apps | user authentication]] <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Dependencies
The primary dependency is `gun`, installed via npm <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Additionally, two supporting libraries are imported:
*   `c` (Security, Encryption, and Authorization): This module enables the core [[user_authentication_and_profile_management_in_chat_apps | user authentication]] functionalities <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   `ax` (Advanced Exchange Equation): An alternative for connecting peers, offering more performant connections for chat applications <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Initialization and User Management
1.  **Database Initialization**: A `db` variable initializes the Gun database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
2.  **User Reference**: A reference is made to the currently authenticated user <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The `recall` option chained to this reference ensures the user remains logged in across browser sessions by utilizing session storage <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
3.  **Username (Alias) Retrieval**: The username, referred to as an "alias," is retrieved by making a reference to the user and calling `get('alias')` <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
4.  **Reactive State with Svelte Stores**: To manage user state reactively in the Svelte UI, the `writable` store from `svelte/store` is used. This allows the UI to automatically re-render when the username or authentication state changes <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
5.  **Listening to Auth Events**: The application listens to the `auth` event on the database to detect sign-in and sign-out actions, updating the username store accordingly <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

### Sign-in and Sign-up Logic
*   **Sign In**: The `user.auth()` method is used, taking the username and password as arguments. A callback can be defined for handling success or errors <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Sign Up**: The `user.create()` method is used. If user creation is successful, the user is automatically logged in <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Sign Out**: The `user.leave()` method logs the user out, and the username store is cleared <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

### Considerations
One important consideration for this type of decentralized authentication is that the uniqueness of usernames is not enforced by default <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>. While possible to implement, it is beyond the scope of this basic example <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

### Example: Displaying User State in UI
Svelte's reactive capabilities simplify UI updates. For instance, an `if` statement with a dollar sign (`$`) prefix to a store name (`$username`) subscribes to the store, dynamically showing or hiding UI elements (like a sign-out button or avatar) based on whether the username exists <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
```html
{#if $username}
    <!-- Show username and avatar -->
    <img src="https://api.dicebear.com/7.x/initials/svg?seed={$username}" alt="User Avatar">
    <p>{$username}</p>
    <button on:click={signOut}>Sign Out</button>
{:else}
    <!-- Show login options -->
    <p>Please log in</p>
{/if}
```
User avatars can be generated dynamically using APIs like DiceBear, which creates a unique avatar based on the username as a random seed <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.