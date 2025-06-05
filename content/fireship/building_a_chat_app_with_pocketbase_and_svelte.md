---
title: Building a chat app with Pocketbase and Svelte
videoId: gUYBFDPZ5qk
---

From: [[fireship]] <br/> 

This article describes how to build a full-stack chat application using Pocketbase for the backend and Svelte for the frontend, then deploy it to a Linux server on Linode. This combination is referred to as the "Spock stack" due to its efficiency in development <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. A notable feature of this demo application is its community moderation system, where messages receiving five negative reactions disappear from the UI <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Backend: Pocketbase

Pocketbase is an open-source alternative to [[Building a realtime chat app with Firebase | Firebase]], written in Go <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. It provides user authentication and a real-time database powered by SQLite <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A key differentiator is its ability to compile into a single executable file, meaning it only requires one small server to self-host <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This simplicity makes it a strong contender for scalable applications <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Deployment to Linode

The first step in building the application is to deploy the Pocketbase backend to a cloud server <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Linode, a cloud provider established in 2003, is recommended for its simplicity and predictable pricing <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Step 1: Create a Linode Server

To get a Linux server running in the cloud <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:
1.  Register and go to the dashboard <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
2.  Click to create a new Linode <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
3.  Choose a preferred Linux distribution, such as Debian <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
4.  Select a region and the size of the machine <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
5.  Set a root password and click create <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
6.  Note the server's IP address for access <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Step 2: Deploy Pocketbase to Linode

1.  Download the Pocketbase executable (Linux version) from its website <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
2.  Unzip the file to get the single executable <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
3.  Open a terminal and use `ssh` to access the Linode server as the root user, entering the created password <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
4.  Create a directory (e.g., `PB`) on the server <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
5.  Use `scp` from a separate local terminal to copy the Pocketbase executable to the new directory on the remote server <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
6.  On the Linode terminal, navigate to the `PB` directory and run `pocketbase serve` with the `--http` flag, specifying the server's IP address and port 80 <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This makes the backend accessible over HTTP, serving a REST API and an admin dashboard <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

#### Production Readiness Enhancements:

*   **Domain and HTTPS:** Bring a domain to Linode's DNS manager. Pocketbase uses Let's Encrypt to automatically generate an SSL certificate, allowing the backend to be served over HTTPS by adding an extra flag to the serve command <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Data Persistence:** Mount a volume to the `pb_data` directory where Pocketbase stores all data. This ensures data persistence and portability across servers <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Automatic Restart:** Set up a systemd service to automatically restart Pocketbase whenever the server reboots <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Data Modeling with Pocketbase

### Step 3: Configure Collections and API Rules

1.  Navigate to the Pocketbase dashboard and create an admin user <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
2.  In the database section, the default `users` collection manages application users with fields like username, email, and password <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  **Create a `messages` collection:**
    *   Add a `text` field for the message content, with optional server-side validations like min/max length <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Add a `user` field to create a one-to-many relationship, indicating a message belongs to a user. Pocketbase automatically creates a foreign key for the user ID in the messages table <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
4.  **Set API rules for security:**
    *   **`messages` collection:** Allow anybody to view (list and view) messages. Allow authenticated users to create messages, but enforce that the message is associated with their own user ID (`user = @request.auth.id`) <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   **`users` collection:** Allow users to view each other's profiles by removing the default view and list rules <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Frontend: Svelte

Svelte is chosen for the frontend due to its effectiveness in building real-time UIs, leveraging its built-in reactive stores <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Initial Setup
1.  Generate a new Svelte project using Vite, selecting the TypeScript option <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
2.  Install npm dependencies (`npm install`) and serve locally (`npm run dev`) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
3.  Delete boilerplate code and create a `pocketbase.ts` file in the `lib` directory <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### User Authentication in Svelte
1.  **`pocketbase.ts`:**
    *   Install the Pocketbase JavaScript SDK (`npm install pocketbase`) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Import `pocketbase` and `writable` from `svelte/store` <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   Initialize Pocketbase with the Linode IP address (backend URL) <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
    *   Create a `writable` store named `currentUser`, initialized with `pb.authStore.model` (null if not logged in, or the user's database record if logged in) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
    *   Register a callback for `pb.authStore.onChange` to update the Svelte store when the user signs in or out <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
2.  **`Login.svelte` component:**
    *   Import `pb` and `currentUser` from `pocketbase.ts` <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   Use Svelte's reactive syntax (`$currentUser`) to display user information if logged in <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   Define `username` and `password` variables <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Create an HTML form with inputs, using `bind:value` to link them to the variables <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   `login` function: Authenticates a user by calling `pb.collection('users').authWithPassword(username, password)` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   `signup` function: Creates a new user record with `pb.collection('users').create()` and then logs them in <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   Include `try-catch` blocks for error handling <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   `signout` function: Clears the authentication store with `pb.authStore.clear()` <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   Bind these functions to buttons using `on:click` and use `on:submit|preventDefault` on the form to prevent page refresh <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
3.  **`App.svelte`:** Declare the `Login` component to render it <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Real-time Chat Messages

Create a new component called `Messages.svelte` to implement the chat functionality <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

1.  Import `onMount`, `onDestroy` lifecycle hooks and `pb` (Pocketbase instance) <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
2.  Initialize a `messages` array as an empty array <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
3.  **Fetching Messages (`onMount`):**
    *   Use `onMount` to fetch messages when the component is initialized <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
    *   Query the `messages` collection using `pb.collection('messages').getList(1, 50)` (page 1, 50 messages per page) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   Sort the results by the `created` field <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   Use `expand: 'user'` to include related user data with each message, avoiding complex SQL joins <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   Set the `messages` array to `result.items` <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
4.  **Displaying Messages:**
    *   Loop over the `messages` array in HTML using Svelte's `{#each messages as message (message.id)}` block, which creates a keyed loop for efficient rendering <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   Render the `message.text`, `message.expand.user.username`, and generate a unique avatar for each user using a service like Dicebear <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>.
5.  **Sending Messages:**
    *   Create a `newMessage` variable <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   Define a `sendMessage` function that takes the `newMessage` text and the current user's ID (`$currentUser.id`) <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
    *   Call `pb.collection('messages').create({ text: newMessage, user: $currentUser.id })` to create a new message <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   Bind this function to a form's `on:submit|preventDefault` event and link the input to `newMessage` <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
6.  **Real-time Updates:**
    *   Inside the `onMount` callback, subscribe to real-time updates for the `messages` collection using `pb.collection('messages').subscribe('*', (e) => {...})` <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. The wildcard `*` symbol listens for creations, updates, or deletions <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
    *   In the callback, update the `messages` array based on the event `action`:
        *   If `created`, add the new record to the array. Note that real-time events may not include expanded user data, requiring an additional `getOne` query if needed <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
        *   If `deleted`, filter out the removed message by ID <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.
    *   **Unsubscribing:** It's crucial to unsubscribe from real-time listeners to prevent memory leaks and unnecessary database reads <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. The `subscribe` call returns an `unsubscribe` function <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>. Call this `unsubscribe` function in the `onDestroy` lifecycle hook <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.

## Production and Scaling

Once the Svelte frontend is complete, build it for production using `npm build` <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. Since it's a single-page application, the generated files can be uploaded to a storage bucket on Linode and configured as a static website host <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

As the website grows and traffic increases, Pocketbase can scale vertically by resizing the Linode server to provide more CPU and RAM <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. A larger server can handle tens of thousands of concurrent users, sufficient for most projects <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.