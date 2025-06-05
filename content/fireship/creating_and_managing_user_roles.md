---
title: Creating and Managing User Roles
videoId: 1PEdd2rtG30
---

From: [[fireship]] <br/> 

[[rolebased_authorization_with_firestore | Rule-based authorization]] is a fundamental aspect of any user-moderated website, similar to how Stack Overflow grants privileges based on user reputation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article demonstrates how to implement a flexible and secure role-based authorization feature using Angular 5 and Firestore, focusing on both front-end and back-end security <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Core Concept: Assigning Roles
The system works by assigning a role to a user, which is then saved in Firestore <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This assigned role dictates what actions a user can perform within the Angular application <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Defined Roles
Three primary roles are defined, each with distinct permissions:
*   **Subscriber**: Can only read data <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This is the default role <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Editor**: Can read and update data <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   **Admin**: Possesses full control, able to read, update, create, and delete data <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

These roles are stored as an object in Firestore, where each possible role is set to a boolean value, allowing for multiple roles to be assigned to a single user if desired <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. A user's profile includes a user ID, email, and the roles object <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Setup and Authentication
A new Angular app with AngularFire2 installed serves as the starting point <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A `core` module is generated to centralize authentication and authorization logic, within which an `AuthService` is created <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

The authentication process involves:
1.  Importing AngularFire libraries <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
2.  Defining a custom user interface that includes the roles object <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
3.  Setting up an observable for the user interface <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
4.  Listening to the AngularFire authentication state to retrieve the user document from Firestore <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
5.  Using Google OAuth for user authentication <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
6.  Upon successful authentication, the `updateUserData` method creates or updates the user document in Firestore with a default role of "subscriber" using the `merge: true` option to prevent data loss <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Implementing Role-Based Rules

### Front-End: Defining Abilities
[[website_access_and_user_interactions | Rule-based authorization]] on the front-end involves creating "abilities" and assigning roles authorized to perform them <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. A helper method checks if a user has the appropriate role for a given ability <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

Examples of abilities:
*   **`canRead`**: Determines if a user can read a document. Admin, Editor, and Subscriber roles all have read access <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   **`canEdit`**: Allows specific roles (e.g., Admin, Editor) to modify data <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **`canDelete`**: Restricted to Admin users only <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

These abilities can be used to hide or block content in components or within router guards to control access throughout the application <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Front-End: Component-Level Logic
To [[implementing_security_rules_and_user_authentication | lock down specific methods]] or elements in a component:
*   Subscribe to the user observable during `ngOnInit` and use the user's roles to conditionally execute code <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   Use `ngIf` directives in the template to hide buttons or other interactive elements based on user abilities, which is generally a more maintainable approach <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Back-End: Firestore Security Rules
Front-end security is easily circumvented, so **back-end Firestore rules are essential for guaranteeing data security** <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. These rules ensure that any attempt to read or write unauthorized data results in a Firestore error <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

Firestore rules use the `get` method to retrieve the authenticated user's document and check their roles object <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. For example, a rule might deny read access if the user doesn't have the "subscriber" role <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

To improve readability and maintainability, custom functions can be written within Firestore rules <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. A `getRole` function can take a role name as a string argument and check if the authenticated user has that role <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Example rule structure:
```firestore
allow read: if getRole('subscriber') == true;
allow update: if getRole('editor') == true;
allow create, delete: if getRole('admin') == true;
```
This ensures that data is 100% secure, preventing unauthorized operations even if front-end checks are bypassed <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### Front-End: Router Guards
Angular's router guards provide an even better mechanism to prevent unauthorized access by [[dynamic_routes_and_child_routing | locking down routes]] based on a user's role or ability <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

To create a guard (e.g., `AdminGuard`):
1.  Generate a guard and add it to the core module <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
2.  Import the `AuthService` and RxJS operators (`tap`, `map`, `take`) <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
3.  The `canActivate` method of the guard returns an observable mapped to a boolean value <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
4.  Inside the `map` operator, check if the user object exists and if their roles object contains the required role (e.g., `user.roles.admin`) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
5.  Use the `tap` operator to log errors or redirect the user to a different route if access is denied <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

Router guards can also check for specific abilities (e.g., `canRead` method from the `AuthService`) instead of direct roles, allowing multiple roles to grant access to the same ability-restricted route <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. These guards are then applied to route objects in the Angular router using the `canActivate` array <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Conclusion
For robust security, always prioritize **back-end Firestore security rules** for actual data protection <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. Front-end measures like router guards and conditional logic within components serve to enhance the user experience and simplify the codebase by preventing users from attempting unauthorized actions in the first place <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.