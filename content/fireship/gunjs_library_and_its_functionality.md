---
title: Gunjs library and its functionality
videoId: J5x3OMXjgMc
---

From: [[fireship]] <br/> 

Gun.js is a decentralized graph database that allows applications to handle thousands of messages per second and scale globally without relying on centralized big tech company infrastructure <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It enables the data and infrastructure to be decentralized across the entire user base using web technologies <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Core Concepts

### Decentralized Data Storage
Unlike traditional databases that store all data on a hard disk in the cloud, Gun.js stores a small subset of data on each user's device based on the actual data they consume in the application <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. When a user queries for data, Gun.js searches across the network for other users who have that data and syncs it up using technologies like WebRTC <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The entire database can be thought of as the union of all peers on the network <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Comparison to Blockchain
The concept of decentralization in Gun.js is similar to a blockchain ledger, where no single individual controls the entire network <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. However, Gun.js is not blockchain technology itself, as blockchain tends to be too slow and unnecessary for applications like a chat app <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Cryptography and Security
Gun.js heavily relies on cryptography to implement features like user authentication <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. When a new user account is created, a cryptographically secure key pair is generated <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The username is associated with a public key to find past messages, and the password acts as a proof-of-work seed to prove and decrypt access to the account's private keys <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. End-to-end encryption is also possible <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

### Data Persistence
By default, Gun.js stores data in the browser's local storage, which has a 5MB limit <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. If a user clears their browser cache, data could be lost unless it's stored elsewhere on the network <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For production-grade applications, a relay server can be deployed <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. These servers use a different storage mechanism called Radix, which can store significantly more data on a server's disk, making the network more robust by allowing queries to fall back to a relay if data isn't available from another peer <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

### Public Data Model
When a node is created in the Gun.js database, it becomes available to the entire decentralized network <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Other developers can easily access public data by knowing the name of the node where it's stored <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While data encryption is possible, it requires a different mental model than traditional centralized databases <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Key Modules and Concepts

### SEA (Security, Encryption, Authorization)
The SEA module is crucial for enabling user authentication within Gun.js <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. It handles the cryptographic operations required for secure user accounts.

### AX (Advanced Exchange Equation)
AX is an alternative method for connecting peers together in the Gun.js network <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. It generally provides better performance for applications like chat apps <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Building a Decentralized Chat App with Gun.js

A decentralized chat application can be built using Gun.js for backend functionality and a [[javascript_trends_and_frameworks | JavaScript]] library like Svelte for the frontend UI <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### User Authentication
1.  **Initialization**: Initialize the Gun database and reference the current authenticated user <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. The `recall` option can be chained to session storage to keep the user logged in between browser sessions <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
2.  **User State Management**: The `user.get('alias')` method retrieves the chosen username <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. In Svelte, a writable store can make this value reactive, updating the UI whenever the alias changes <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
3.  **Authentication Events**: Listen to the `auth` event on the database to handle changes in the user's login state (sign-in or sign-out) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
4.  **Sign Out**: The `user.leave()` method signs out the user, and the username store can be cleared <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
5.  **Login/Sign Up**:
    *   **Login**: Use the `user.auth()` method with username and password as arguments. A callback can be defined for error handling or other actions <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   **Sign Up**: Use the `user.create()` method. If successful, the user can be automatically logged in <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   *Note*: By default, username uniqueness is not enforced, but it is possible to implement <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Chat Functionality
1.  **Querying Messages**:
    *   On component initialization, reference a specific node (e.g., `'chat'`) in the database <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. For a single chat room, a simple name like 'chat' suffices; for multiple rooms, unique names are needed <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   Use `map()` to loop over messages and `once()` to read each message only once, as chat messages are typically immutable <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Alternatively, `on()` can be used to listen for real-time changes <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   The callback provides access to the message data and its node ID <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   Message formatting: Messages can be formatted with properties like `who` (sender alias via `data.get('alias')`), `what` (message text), and `when` (timestamp from `Gun.state(rawData)` for accurate time across users) <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a> <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
    *   **End-to-End Encryption**: Message content (`what`) can be encrypted using the SEA module. The key used for encryption must match the key used for decryption <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
2.  **Sending Messages**:
    *   **Encryption**: Use `SEA.encrypt()` to encrypt the message text with the chosen key <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   **Association**: Associate the encrypted message with the current user <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
    *   **Indexing**: Create a new `Date` object to serve as an index for the message, allowing proper sorting <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
    *   **Storage**: Reference the chat collection, create a new node based on the timestamp index, and store the encrypted message value <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### External APIs
When displaying user avatars, an API like Dicebear can be used to generate unique avatars based on the username as a random seed <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This demonstrates the [[research_and_use_of_apis_in_programming | research and use of APIs in programming]] in conjunction with Gun.js.