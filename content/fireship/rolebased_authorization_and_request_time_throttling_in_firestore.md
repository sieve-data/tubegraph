---
title: Rolebased authorization and request time throttling in Firestore
videoId: b7PUm7LmAOw
---

From: [[fireship]] <br/> 

Deploying a Firebase application without proper backend security rules leaves it vulnerable to data theft and deletion within seconds <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This can be exploited by identifying the project ID via Chrome developer tools and executing a `curl delete` request to the Firebase REST API <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Implementing expressive and easy-to-understand backend security rules is crucial for keeping your Firestore database secure <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Firestore Security Rules Fundamentals

Firestore security rules are defined in their own special language, somewhat resembling JavaScript, within the rules tab of the Firestore database <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Rule Structure

*   **Root Block**: All rule logic is defined inside the root block <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   `match` Keyword: Used to point to specific paths in your database where rules should be applied <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   `**` (double star): Matches every single document and cascades down to all subcollections and nested paths, useful for broad rules like user authentication <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   Hardcoded ID: Points to a specific document by its ID <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   Wildcard ID `[{variable_name}]`: The most common matcher, allowing the document ID to be evaluated as a variable at runtime within the `allow` statement <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
*   `allow` Keyword: Followed by the operation(s) you want to permit <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. If left blank, it allows the operations. Otherwise, an expression returning `true` or `false` applies the rule logic <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Example: `allow read, write: if false;` completely locks down all documents from client-side access <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Secure by Default**: Unless an operation is explicitly allowed, Firestore will block it <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Request Operations

Rules can be scoped to specific operations:

*   **Read Rules**:
    *   `get`: Applies to reading a specific document <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
    *   `list`: Applies to a collection query <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   `read`: Combines `get` and `list` <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Write Rules**:
    *   `create`: Applies to creating new data <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   `update`: Applies to modifying existing data <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   `delete`: Applies to removing data <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
    *   `write`: Combines `create`, `update`, and `delete` <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Accessing Data within Rules

*   `request.auth`: Contains information about the current user, such as `request.auth.uid` to check if a user is logged in (`request.auth != null`) <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. It also contains `request.auth.token` with properties like `email_verified` <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   `resource.data`: Represents the existing data of a document before an operation. Useful for ensuring a document isn't modified after it's been "locked" <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   `request.resource.data`: Represents the incoming data that is being written to the database. Essential for [[handling_manytomany_relationships_in_firestore | validating incoming data structure]] and ensuring data integrity, such as checking if a price is greater than a minimum value <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Custom Functions for Reusability

Firestore rules allow you to write custom functions for dry (Don't Repeat Yourself) and readable code <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

```
function isSignedin() {
  return request.auth != null;
}

// Example usage:
allow delete: if isSignedin();
```
This makes rules read like plain English sentences <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

You can chain multiple conditions using `&&` (AND) or `||` (OR) statements <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Role-Based Authorization

[[RoleBased Authorization with Firestore]] involves storing user role information on their user document and reading that document when applying rules <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Reading User Documents for Roles

The `get()` keyword reads a document by pointing to its absolute path <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This is typically done within a function to manage verbosity.

```
function getUserRoles() {
  return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.roles;
}
```

This function retrieves the current user's document, interpolating `$(request.auth.uid)` into the path <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

### Authorizing by Role

Once the user's roles object is obtained, you can use `.keys()` to get all role names and `.hasAny()` or `.hasAll()` to check for specific roles <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

```
allow update: if isSignedin() && getUserRoles().keys().hasAny(['editor', 'admin']);
```

This provides a simple solution for [[rolebased_authorization_with_firestore | implementing role-based user authorization]] <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## Request Time Throttling

Time can be used to impact database security, for example, to throttle the amount of data a user can create within a specific duration <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

*   `request.time`: Provides the current timestamp of any request <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
*   `duration`: A helper function that allows adding a number of seconds, minutes, or hours to a Firestore timestamp <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

### Example: Limiting Writes to Once Every 60 Seconds

A rule can ensure that `request.time` comes after a document's `createdAt` timestamp plus a specified duration.

```
allow write: if request.time > resource.data.createdAt + duration.seconds(60);
```

This rule allows a user to write to a product document only once every 60 seconds <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.