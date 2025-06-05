---
title: Decentralized chat application
videoId: J5x3OMXjgMc
---

From: [[fireship]] <br/> 

A decentralized chat application (DApp) is a type of chat application where the data and infrastructure are not controlled by a single central entity, such as a big tech company <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Instead, the data is distributed and managed across the entire user base using [[web3_and_decentralized_internet | web technologies]] <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. An example is a Super Chat-like application built using Gun.js <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.

A live demo of such an application is available at `gunchatdap.web.app` <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Core Technologies

### Gun.js

Gun.js is a decentralized graph database <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. Unlike traditional databases that store all data on a central server, Gun.js stores a subset of data on each user's device based on the data they consume within the application <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. When a user requests data, the system searches across the network for other users who possess that data and synchronizes it using technologies like WebRTC <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. The entire database is conceptualized as the union of all peers on the network <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

While similar in concept to a blockchain ledger where no single entity controls the network, Gun.js is not blockchain technology, as blockchain can be too slow and unnecessary for applications like a Super Chat <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>. However, it heavily relies on cryptography <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

Key modules used with Gun.js include:
*   **SEA (Security, Encryption, Authorization)**: Enables [[user_authentication_with_decentralized_apps | user authentication]] and encryption <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **AX (Advanced Exchange Equation)**: An alternative peer connection method often more performant for chat applications <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

### Data Persistence

By default, Gun.js stores data in the browser's local storage, which has a 5MB limit <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. Data in local storage can be lost if a user clears their browser cache and the data isn't replicated elsewhere on the network <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. For production-grade applications, a relay server can be deployed <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. These servers use a different storage mechanism called Radix, which can store much more data on a server's disk, making the network more robust by allowing queries to fall back to a relay if data is not available from another peer <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Frontend UI

Svelte, a JavaScript library, is used for the frontend UI <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Svelte's `writable` stores provide reactive values that re-render the UI when changed and can be shared across multiple components <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.

## Features

### [[user_authentication_and_profile_management_in_chat_apps | User Authentication]]

When a new user account is created in a decentralized chat app using Gun.js, a cryptographically secure key pair is generated <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. The username is linked to a public key, which helps locate past messages <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. The password acts as a proof-of-work seed to prove and decrypt access to the account's private keys <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>. End-to-end encryption can also be implemented <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

Implementation details:
*   The `user` object in Gun.js is used for authentication <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   The `recall` option can be chained to session storage to keep the user logged in between browser sessions <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
*   The `user.get('alias')` method fetches the username <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   The `user.auth()` method logs a user in <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>.
*   The `user.create()` method signs up a new user <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
*   Signing out is done by calling `user.leave()` <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.
*   A caveat is that username uniqueness is not enforced by default, though it is possible to implement <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>.
*   Avatars can be generated dynamically based on the username using an API like DiceBear <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

### Chat Functionality

[[data_modeling_in_firestore_chat_applications | Chat messages]] are typically stored in a dedicated node in the Gun.js database <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. For a single large chat, a node named `chat` can be used, but for multiple chat rooms, each would have a unique name <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

[[firestore_features_and_methods_for_handling_chat_data | Messages are retrieved]] and displayed using:
*   `db.get('chat').map()`: Loops over every message in the chat <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
*   `.once()`: Reads each message only once, suitable for immutable messages <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. The `.on()` method could be used for real-time updates <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
*   Messages include properties for `who` (sender's alias), `what` (message text), and `when` (timestamp) <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.

#### [[secure_and_efficient_data_modeling_for_chat_applications | End-to-End Encryption]]

Messages can be stored with [[secure_and_efficient_data_modeling_for_chat_applications | end-to-end encryption]], meaning the data in the database is encrypted and requires a corresponding key to decrypt <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. While the demonstration uses a hard-coded key, in a secure implementation, the key would be a secret shared between users <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

#### Sending Messages

Sending a message involves:
1.  Encrypting the message text using the SEA module and the encryption key <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
2.  Associating the encrypted message with the current user <a class="yt-timestamp" data-t="10:17:00">[10:17:00]</a>.
3.  Creating a date timestamp to serve as an index for proper sorting <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.
4.  Referencing the chat collection, creating a new node based on the timestamp index, and storing the encrypted message value <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.