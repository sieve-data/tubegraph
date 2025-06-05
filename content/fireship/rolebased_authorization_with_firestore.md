---
title: RoleBased Authorization with Firestore
videoId: 1PEdd2rtG30
---

From: [[fireship]] <br/> 

Role-based authorization is fundamental for any user-moderated website, similar to how Stack Overflow grants privileges based on user reputation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This system allows you to define roles that control a user's ability to interact with data and features, providing both front-end and back-end security <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Core Concepts

The system works by assigning a role to a user, which is then saved in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This role dictates permissible actions within an Angular application <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Defined Roles
Three primary roles are typically defined:
*   **Subscriber**: Can only read data <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **Editor**: Can read and update data <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Admin**: Can read, update, create, and delete data <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

Roles are saved as an object in [[working_with_firebase_firestore_and_realtime_updates | Firestore]], with each role assigned a boolean value, allowing for multiple roles to be assigned to a single user if desired <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A user object includes a user ID, email, and a `roles` property that references this roles object <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Setup and Implementation

### Angular Application Setup
Begin with a new Angular application with AngularFire2 installed <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A core module is generated to isolate authentication and authorization logic, within which an `AuthService` is created <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### User Authentication
The `AuthService` sets up an observable typed to the user interface <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. It listens to the AngularFire auth state and, if a user is defined, retrieves the corresponding user document from [[working_with_firebase_firestore_and_realtime_updates | Firestore]] <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. For authentication, Google OAuth is used <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

Upon successful authentication, the `updateUserData` method is called <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This method creates or updates the user document in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] by referencing the user's authentication ID and setting a default role of `subscriber` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The `merge: true` option is used to update the document non-destructively <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## Front-End Security (Angular)

While front-end security in Angular can be easily circumvented, it enhances the user experience by visually managing access <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Defining Abilities
A set of "abilities" is created, with different roles authorized to perform them <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. A helper method checks if a user has the appropriate role for a given ability <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Example abilities:
*   `canRead`: Allows admin, editor, and subscriber roles <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   `canEdit`: Allows admin and editor roles <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   `canDelete`: Only allows admin role <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Implementing Authorization in Components
The `AuthService` can be used to lock down specific methods or hide/show elements in the DOM:
*   **Method Locking**: Subscribe to the user observable and wrap sensitive code within `if` statements that check `canEdit` or similar abilities <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Template Logic**: Use `ng-if` directives in templates to hide or show buttons or other elements based on the user's abilities <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.

### Router Guards for Route-Level Access
Angular router guards provide a mechanism to prevent unauthorized access to entire routes:
1.  **Create a Guard**: Generate a guard (e.g., `AdminGuard`) and add it to the core module <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
2.  **Guard Logic**:
    *   Import the `AuthService` and RxJS operators (`tap`, `map`, `take`) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   In the `canActivate` method, return an observable mapped to a boolean <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   Use `take(1)` to prevent running subscriptions <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
    *   Inside `map`, check if the user object and their specific role (e.g., `user.roles.admin`) or an ability (e.g., `canRead(user)`) is true <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
    *   Use `tap` to log errors or redirect unauthorized users <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
3.  **Apply to Routes**: Import and add the guards to the `canActivate` array in the router's route objects <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

Using router guards simplifies the codebase and does not require a read in [[working_with_firebase_firestore_and_realtime_updates | Firestore]] to evaluate a rule <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

## Back-End Security (Firestore Security Rules)

Back-end [[firestore_security_rules_setup_and_implementation | Firestore security rules]] are essential for guaranteeing data security, as they produce errors if unauthorized data access or modification is attempted <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

### Implementing Role-Based Rules
1.  **Retrieve User Document**: Use the `get` method to retrieve the authenticated user's document from the [[working_with_firebase_firestore_and_realtime_updates | Firestore]] database based on `request.auth.uid` <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This document contains the `roles` object <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
2.  **Check Role Status**: Access the specific role (e.g., `subscriber`) within the retrieved roles object and ensure its value is `true` <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

```javascript
// Example: Rule for read access
allow read: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.roles.subscriber == true; <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
```

### Using Custom Functions in Security Rules
To improve readability and maintainability, [[creating_custom_functions_for_firestore_security_rules | custom functions]] can be written within [[firestore_security_rules_setup_and_implementation | Firestore rules]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

Example `getRole` function:
```javascript
function getRole(role) {
  return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.roles[role];
} <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>
```

Applying `getRole` to rules:
*   `allow read: if getRole('subscriber') == true;` <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>
*   `allow update: if getRole('editor') == true;` <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
*   `allow create, delete: if getRole('admin') == true;` <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

When an editor attempts to delete a page, a [[working_with_firebase_firestore_and_realtime_updates | Firestore]] error will occur because they lack admin privileges, while an update operation will succeed <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

## Conclusion

For robust authorization:
*   Use back-end [[firestore_security_rules_setup_and_implementation | Firestore security rules]] for actual data security <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   Use front-end Angular logic, such as router guards and component-level checks, to enhance the user experience <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.