---
title: Implementing security rules and user authentication
videoId: iWEgpdVSZyg
---

From: [[fireship]] <br/> 

When building applications with Firebase, two critical aspects are ensuring data security and managing user access. Firebase provides robust features for both through [[Firestore security rules setup and implementation | Firestore Security Rules]] and [[User authentication with Firebase | user authentication]].

## Setting Up Your Firebase Project for Security

For any serious application, it's recommended to create two separate Firebase projects: one for development and one for production <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This setup provides a safe sandbox for testing and experimentation, keeping your sensitive customer data pristine in the production environment <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

When working with a team, navigate to the "Settings" tab, then "Users and Permissions," and assign roles based on the principle of least privilege. This ensures that team members only have access to the resources they truly need <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

Firebase application credentials generated for your frontend code are safe as long as you properly set up security rules <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## User Authentication

[[User authentication and profile management in chat apps | User authentication]] is a fundamental service to integrate into any Firebase project <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Determining User Login Status

There are two primary methods to check if a user is logged in:
*   **Pulling the current user:** Call `auth.currentUser` to retrieve the current user's record. This is suitable for handling events, such as when a user clicks a button <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This approach benefits from understanding asynchronous JavaScript, specifically `async/await` <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Listening to the auth state:** Use `onAuthStateChanged` to continuously listen for changes to the authentication state, such as when a user signs in or out. You provide a callback function that runs whenever the state changes <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This method is enhanced by understanding callbacks and functional programming <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

### Error Handling

When a user attempts to log in, errors may occur. It's crucial to catch these errors and implement a default handler that routes the user to a visual UI element, such as a dialog, to inform them of the issue <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

### Lazy User Registration

Firebase Auth allows for lazy user registration. You can initially sign a user in anonymously, which provides a user ID that can be tied to database data. Later in the onboarding process, you can collect their email or link social accounts like Twitter, Facebook, or Google to their anonymous account <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Custom Email Action Handlers

For authentication methods like email/password, Firebase may need to send emails for verification or password resets. You can control this process by using custom email action handlers <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. You even have the option to integrate your own custom SMTP email server <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Firestore Security Rules

[[Firestore security rules setup and implementation | Firestore security rules]] are paramount. Deploying an application to production without robust security rules can lead to compromised customer data and destructive writes to your database <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

### Initial Database State

When creating your Firestore database for the first time, it's safer to set it in "locked mode" initially. From this secure starting point, you can incrementally allow operations as they become necessary for your application's functionality <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

### Testing Security Rules

*   **Simulator:** Use the built-in simulator in the Firebase console to pass mock requests to your database and see how your rules will be evaluated <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.
*   **Firestore Emulator:** For serious production applications, use the Firestore emulator. This allows you to simulate the Firestore database in your local development environment, enabling you to throw many test cases at your rules to ensure their robustness <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>.

### Rule Operations

There are five main types of operations a user can perform on a document in Firestore, for which you can define fine-grained rules <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>:
*   `get`: Retrieve a single document <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.
*   `list`: Query a list of documents <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>.
*   `create`: Create new documents <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   `update`: Modify existing documents <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.
*   `delete`: Remove documents <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>.

If operations share the same logic, you can combine them using the `read` or `write` keywords, separated by a comma <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

### Rule Evaluation Context

When a security rule is evaluated, it considers two main elements <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>:
*   **Request:** Contains the user's authentication state (e.g., `request.auth.uid`) and the incoming data they are attempting to write (`request.resource.data`) <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Resource:** Represents the data that already exists at the specified path in the database (`resource.data`) <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

### Looking Up Data in Rules

In some cases, you may need to look at data elsewhere in the database to determine if a rule should be allowed. Use the `get` keyword and point to a specific path in the database. You can use dollar-sign parentheses (`$()`) to interpolate values, such as the `request.auth.uid`, into the path <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Be aware that each time this rule is evaluated, a read operation is charged for the data accessed via `get` <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

### [[Creating custom functions for Firestore security rules | Custom Functions for Security Rules]]

For complex or frequently used logic, you can extract it into its own function within your security rules. This makes your rules cleaner and more maintainable <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. For example, an `isAdmin` function can simplify checks for administrative users <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## Backend Security (Admin SDK and REST APIs)

For backend operations and sensitive tasks, Firebase provides the Admin SDK and REST APIs.

### Command Line Utilities with Admin SDK

You can create your own command-line utilities using the Firebase Admin SDK <a class="yt-timestamp" data-t="00:17:23">[00:17:23]</a>.
1.  Download the service account key for your project from project settings <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
2.  Install `firebase-admin` as a development dependency in your Node.js project <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
3.  Create a JavaScript file that imports `firebase-admin` and calls `initializeApp` <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

**Security Measure:** The service account key contains sensitive information. The safest way to use it locally is to store it privately on your system and reference it via an environment variable called `GOOGLE_APPLICATION_CREDENTIALS` <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. If you include the service account directly in your source code, ensure it's added to your `.gitignore` file to prevent it from ending up in a public repository <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

### Callable Functions

For endpoints that should only be accessed by authenticated users, `callable functions` are a secure and simplified alternative to regular HTTP functions. Callable functions automatically include the authentication context for the user, eliminating the need for you to implement your own middleware to authenticate functions <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

A great use case for a callable function is deleting an entire Firestore collection, which should always be handled on the backend due to the potential for a large number of documents <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. This function can authorize the operation based on the user ID, then use a recursive batch delete function to retrieve and delete documents in batches (e.g., 100 at a time) to avoid memory issues with millions of documents <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.