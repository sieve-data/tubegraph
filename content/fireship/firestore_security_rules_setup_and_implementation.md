---
title: Firestore security rules setup and implementation
videoId: b7PUm7LmAOw
---

From: [[fireship]] <br/> 

Firestore security rules are essential for protecting your database from unauthorized access and manipulation <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Without proper backend security rules, anyone can steal or delete your data by sending delete requests to the Firebase REST API using your project ID <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This article outlines how to set up and implement robust security rules to keep your [[firestore_data_modeling_techniques | Firestore database]] secure <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## Initial Setup and Basic Structure

To begin, navigate to the Firestore database section in your Firebase console and open the `rules` tab <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Firestore rules are defined in a special language that resembles JavaScript <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. All rule logic is defined within a main block, starting at the root of your database <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

```
service cloud.firestore {
  match /databases/{database}/documents {
    // Rules logic here
  }
}
```

### Defining Paths and Operations

The `match` keyword is used to specify the paths in your database where you want to apply rules <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   `match /{document=**}`: This special syntax matches every single document in the database, including all sub-collections and anything nested under that path <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This is useful for rules applied broadly, such as verifying a user is [[user_authentication_with_firebase | authenticated]] <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Specific Document IDs**: You can hardcode a specific document ID directly into the path for very specific rules <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Wildcard IDs (`{documentId}`)**: The most common and useful matcher allows you to use a variable name in brackets (e.g., `{productId}`) that can be evaluated as the document ID at runtime <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. This variable can then be used in `allow` statements <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

The `allow` keyword is followed by the operation(s) you want to set a rule for <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. If left blank, it allows the operations <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. You can also write an expression that returns `true` or `false` to apply specific logic <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Types of Request Operations

Rules can lock down various types of requests <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>:

*   **Read Rules**:
    *   `get`: Applies to reading a specific document <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   `list`: Applies to collection queries <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   `read`: Combines `get` and `list` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Write Rules**:
    *   `create`: Applies to creating new data <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   `update`: Applies to modifying existing data <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   `delete`: Applies to removing data <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   `write`: Combines `create`, `update`, and `delete` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Secure by Default

> [!NOTE]
> Your Firestore rules are "secure by default" <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Unless you explicitly allow an operation, it will be blocked by Firestore <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

For example, to completely lock down all documents from client-side read or write operations:

```
match /{document=**} {
  allow read, write: if false;
}
```

## Advanced Rule Logic

Rules can perform logic based on [[user_authentication_with_firebase | user authentication]], underlying data, or the incoming request time <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### The `request` Object

The `request` object is built into the rules environment and provides important information about the current user and incoming request <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

*   **Checking Authentication**: To determine if a user is logged in, you can check `request.auth != null` <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### [[creating_custom_functions_for_firestore_security_rules | Custom Functions]]

[[creating_custom_functions_for_firestore_security_rules | Custom functions]] improve readability and promote DRY (Don't Repeat Yourself) principles <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

**Example: `isSignedIn` Function**
Instead of repeatedly writing `request.auth != null`, you can create a function:

```
function isSignedIn() {
  return request.auth != null;
}

// Usage in rules
match /someCollection/{documentId} {
  allow delete: if isSignedIn(); // Reads like plain English
}
```

### Document Ownership Logic

To determine if a user is the owner of a document, you can compare the authenticated user's ID with the document's ID <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This is common for user profiles where only the owner can write to their profile <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. It's crucial that the document ID matches the user's ID for this to work <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

**Example: `isOwner` Function**

```
function isOwner(userId) {
  return request.auth.uid == userId;
}

// Usage in rules for a user profile document
match /users/{userId} {
  allow read: if isSignedIn();
  allow write: if isOwner(userId);
}
```

### Chaining Conditions (AND/OR)

You can chain multiple conditions using `&&` (AND) or `||` (OR) statements <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

*   `&&` (AND): Both functions/conditions must return `true` for the rule to pass <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   `||` (OR): Only one of the functions/conditions needs to return `true` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

**Example: Verified Email Check**

```
function hasVerifiedEmail() {
  return request.auth.token.email_verified == true;
}

// Allow write if owner AND email is verified
match /users/{userId} {
  allow write: if isOwner(userId) && hasVerifiedEmail();
}
```

The `request.auth.token` object contains various useful properties like `email_verified`, `signed_up` time, `anonymous` status, and `phone_number` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Inspecting Data: `resource` vs. `request.resource`

When writing rules, you often need to compare existing data with incoming data to maintain database integrity <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

*   `resource.data`: Refers to the existing data of the document <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
*   `request.resource.data`: Refers to the incoming data of the document in the current request <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

It's recommended to wrap these in helper functions (e.g., `existingData()`, `incomingData()`) for clarity due to their similar names <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Common Use Cases for Data Inspection

*   **Locking Documents**: Prevent updates to a document once it reaches a certain state (e.g., a "published" document becoming "locked") <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

    ```
    match /products/{productId} {
      allow update: if resource.data.locked == false; // Allow update only if not locked
    }
    ```

*   **Data Validation**: Validate the structure and values of incoming data <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

    ```
    match /products/{productId} {
      allow create, update: if request.resource.data.price > 10; // Ensure price is above $10
    }
    ```

## [[RoleBased Authorization with Firestore | Role-Based Authorization]]

[[RoleBased Authorization with Firestore | Role-based user authorization]] allows you to grant permissions based on a user's assigned roles <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This often involves storing user role information on their user document <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

Since the user's role document isn't directly available on the `request.auth` object, you need to explicitly read it using the `get()` keyword <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

*   **`get()` Keyword**: Reads a document by pointing to its absolute path <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Interpolation**: Use `${request.auth.uid}` within the path to get the current user's document <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

**Example: `getRoles()` Function and Usage**

```
function getRoles() {
  return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.roles;
}

// Authorize update if user has 'editor' or 'admin' roles
match /products/{productId} {
  allow update: if getRoles().keys().hasAny(['editor', 'admin']);
}
```

*   `keys()`: Returns all keys from the roles object <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   `hasAny()`: Checks if the user has any of the specified roles <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   `hasAll()`: Checks if the user has all of the specified roles <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Time-Based Security

Time can be used to implement security rules, such as throttling the amount of data a user can create within a specific duration <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

*   `request.time`: Gets the current time of the request <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   `duration()`: A helper function to operate on timestamps (e.g., adding seconds, minutes, or hours) <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

**Example: Throttling Writes**

```
match /products/{productId} {
  allow write: if request.time > resource.data.createdAt + duration.seconds(60);
  // User can only write to a product document every 60 seconds
}
```