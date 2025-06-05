---
title: Understanding and using Firestore match and allow statements
videoId: b7PUm7LmAOw
---

From: [[fireship]] <br/> 

Firebase Firestore security rules are essential for protecting your application's data. Without properly configured backend rules, your database can be hacked, and all data can be stolen or deleted within seconds via the Firebase REST API [00:00:00]<a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article focuses on how to secure your Firestore database by writing expressive and easy-to-understand backend security rules using `match` and `allow` statements.

## Setting Up Firestore Security Rules

To get started, navigate to your Firestore database and open the "rules" tab [00:00:47]<a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Rules are defined in a special language that somewhat resembles JavaScript [00:00:51]<a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. All rules logic is defined inside a block that points to the root of your database [00:00:57]<a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## The `match` Keyword

The `match` keyword is used to specify paths in your database where you want to apply rules [00:01:01]<a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Matching All Documents
You can use `**` (double star) to match every single document in the database [00:01:08]<a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This special syntax cascades rules down to all sub-collections and anything nested under that path, which is useful for rules applied to many collections, like verifying user authentication [00:02:36]<a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Matching Specific Paths
Rules can be made very specific. You can point to a specific document by hardcoding its ID directly into the path [00:02:51]<a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Wildcard IDs
The most common and useful matcher is the wildcard ID [00:03:03]<a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Instead of hardcoding an ID, you add brackets with a variable name, e.g., `{productID}` [00:03:07]<a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This variable represents the document ID at runtime and can be evaluated within the `allow` statement [00:03:11]<a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

## The `allow` Keyword

The `allow` keyword is followed by the operation you want to set a rule for [00:01:12]<a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. By default, Firestore rules are secure, meaning unless an operation is explicitly allowed, it will be blocked [00:03:31]<a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Defining Operations
Operations can be allowed by leaving the `allow` expression blank or by writing an expression that returns `true` or `false` to apply specific logic [00:01:18]<a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. For example, `allow read, write: if false;` would completely lock down all documents [00:01:29]<a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

The various types of requests that can be locked down include:
*   **Read Rules**:
    *   `get`: Applies to reading a specific document [00:01:57]<a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   `list`: Applies to a collection query [00:02:00]<a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   `read`: Combines `get` and `list` [00:02:15]<a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Write Rules**:
    *   `create`: Applies to creating new data [00:02:07]<a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   `update`: Applies to modifying existing data [00:02:09]<a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   `delete`: Applies to removing data [00:02:12]<a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   `write`: Combines `create`, `update`, and `delete` into a single rule [00:02:19]<a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Rule Logic and Context

Firestore rules can perform logic based on user authentication, underlying data, and incoming request time [00:01:47]<a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The `request` Object
The `request` object provides information about the current user and the incoming request [00:03:50]<a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Authentication**: To check if a user is logged in, you can verify if `request.auth` does not equal `null` [00:03:56]<a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. The `request.auth.token` object contains additional user details like `email_verified`, `anonymous`, `phone_number`, and `sign_up_time` [00:06:06]<a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Request Time**: `request.time` provides the current time of any request, which can be used with the `duration` helper for throttling or time-based rules [00:09:05]<a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

### The `resource` Object
The `resource` object provides information about the data involved in the operation.
*   `resource.data`: Refers to the existing data in the database before an update or delete [00:06:27]<a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This is useful for preventing modifications to locked documents, for instance [00:06:51]<a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   `request.resource.data`: Refers to the incoming data in a `create` or `update` request [00:06:32]<a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This is critical for [[Data modeling in Firestore chat applications | data validation]], ensuring the integrity of your database, such as requiring a price to be greater than $10 [00:07:10]<a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

### Reading Other Documents with `get`
When information is not available directly on the `user` object (e.g., user roles for [[RoleBased Authorization with Firestore | role-based authorization]]), you can use the `get` keyword to read other documents by pointing to their absolute path [00:07:51]<a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. The `get` function allows you to interpolate the `request.auth.uid` to retrieve the current user's document [00:08:13]<a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Once retrieved, you can use methods like `.keys()` and `.hasAny()` or `.hasAll()` to check for authorized roles [00:08:32]<a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Custom Functions
[[Creating custom functions for Firestore security rules | Custom functions]] are a powerful feature that allow you to write DRY (Don't Repeat Yourself) and readable rules [00:04:09]<a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Examples of Custom Functions
*   **`isLoggedIn()`**: Returns `request.auth != null` [00:04:21]<a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    ```firestore
    function isSignedIn() {
      return request.auth != null;
    }
    // Usage: allow delete: if isSignedIn();
    ```
*   **`isOwner(userId)`**: Compares `request.auth.uid` to a document's `userId` field to determine if the current user is the owner [00:05:20]<a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. This is useful for user profiles where only the owner can write to their data [00:04:51]<a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **`hasVerifiedEmail()`**: Checks `request.auth.token.email_verified` [00:06:06]<a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Chaining Functions
You can chain functions and conditions using `&&` (AND) or `||` (OR) statements. For example, `allow write: if isOwner(userId) && hasVerifiedEmail();` would require both conditions to be true [00:05:46]<a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

By understanding and properly implementing `match` and `allow` statements, along with the `request` and `resource` objects and custom functions, you can effectively secure your Firestore database.