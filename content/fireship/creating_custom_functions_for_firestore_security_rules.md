---
title: Creating custom functions for Firestore security rules
videoId: b7PUm7LmAOw
---

From: [[fireship]] <br/> 

Custom functions in [[Firestore security rules setup and implementation | Firestore security rules]] allow for DRY (Don't Repeat Yourself) and readable rule logic, making it easier to manage complex authorization requirements <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. They help make rules read like plain English sentences <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Defining a Basic Function

Functions are defined within the rules environment. A common use case is to check if a user is signed in. Instead of repeatedly writing `request.auth != null`, a function can encapsulate this logic:

```
function isSignedIn() {
  return request.auth != null;
}

// Example usage:
allow delete: if isSignedIn();
```
This makes the rule `allow delete: if signed in` <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## Passing Arguments to Functions

Functions can accept arguments, often used with wildcard variables from the `match` path. For example, to determine if a user is the owner of a document, where the document ID matches the user's ID:

```
match /users/{userID} {
  allow read: if isSignedIn();
  allow write: if isOwner(userID);
}

function isOwner(userID) {
  return request.auth.uid == userID;
}
```
This requires the document ID to match the user ID <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>, <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

## Chaining Functions with Logical Operators

Multiple conditions can be combined using `and` and `or` statements to create more sophisticated rules <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

*   **`and` statement**: Both functions must return `true` for the rule to pass <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   **`or` statement**: Only one of the conditions needs to be `true` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

Example for checking owner *and* verified email:
```
match /users/{userID} {
  allow write: if isOwner(userID) && hasVerifiedEmail();
}

function hasVerifiedEmail() {
  return request.auth.token.email_verified == true;
}
```
The `request.auth.token` object contains properties like `email_verified`, `sign_in_provider`, `anonymous`, or `phone_number` that can be evaluated <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## Accessing Document Data

Functions can also access the existing or incoming data of a document. It's recommended to create helper functions for clarity to avoid confusing `resource.data` (existing data) with `request.resource.data` (incoming data) <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>, <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>, <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Existing Data
Use `resource.data` to access the document's data as it currently exists in Firestore <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This is useful for preventing changes to locked documents or checking previous states <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

Example:
```
function existingData() {
  return resource.data;
}

match /products/{productID} {
  allow update: if !existingData().locked; // Only allow update if not locked
}
```

### Incoming Data
Use `request.resource.data` to access the data that is being written to Firestore <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. This is crucial for [[implementing_security_rules_and_user_authentication | validation rules]] on the data structure <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

Example:
```
function incomingData() {
  return request.resource.data;
}

match /products/{productID} {
  allow create, update: if incomingData().price > 10; // Price must be greater than $10
}
```

## Reading Other Documents

For more complex authorization, such as [[RoleBased Authorization with Firestore | role-based authorization]], functions can use the `get` keyword to read other documents within the rules environment <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This is necessary because user roles are typically stored in a separate document, not directly on the `request.auth` object <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.

The `get` keyword requires an absolute path to the document <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.
```
function getUserRole(userID) {
  return get(/databases/(default)/documents/users/$(userID)).data;
}

function hasAnyRole(roles) {
  // Assuming roles is an array like ['editor', 'admin']
  let userRoles = getUserRole(request.auth.uid).roles;
  return userRoles.keys().hasAny(roles);
}

// Example usage:
match /products/{productID} {
  allow update: if hasAnyRole(['editor', 'admin']);
}
```
This pattern allows checking if a user has "any" of the specified roles using `hasAny` or "all" of them using `hasAll` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Time-based Rules (Throttling)

Functions can leverage `request.time` and the `duration` helper to implement [[Rolebased authorization and request time throttling in Firestore | request time throttling]] or other time-based security measures <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

Example: Preventing a user from writing to a document more frequently than every 60 seconds:
```
function isThrottled(createdAt) {
  return request.time < createdAt + duration.seconds(60);
}

match /products/{productID} {
  allow create, update: if !isThrottled(resource.data.createdAt);
}
```
The `duration` helper allows adding seconds, minutes, or hours to a timestamp <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.