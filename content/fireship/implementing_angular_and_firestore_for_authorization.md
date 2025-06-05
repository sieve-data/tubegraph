---
title: Implementing Angular and Firestore for Authorization
videoId: 1PEdd2rtG30
---

From: [[fireship]] <br/> 

[[RoleBased Authorization with Firestore | Rule-based authorization]] is a fundamental component for any user-moderated website, akin to Stack Overflow's system where user privileges are granted based on reputation [00:00:00]. This guide demonstrates how to build a [[RoleBased Authorization with Firestore | role-based authorization]] feature using Angular 5 and [[Firestore security rules setup and implementation | Firestore]], focusing on both front-end and back-end security [00:00:11]. The approach involves assigning roles to users in [[Firestore security rules setup and implementation | Firestore]] and then using these roles to control actions in Angular [00:00:21].

## Defining User Roles and Privileges

Three primary roles are established:
*   **Subscriber**: Can only read data [00:00:29].
*   **Editor**: Can read and update data [00:00:32].
*   **Admin**: Possesses full control, able to read, update, create, and delete data [00:00:35].

These roles are stored as an object in [[Firestore security rules setup and implementation | Firestore]], where each role is assigned a boolean value, allowing for multiple roles to be assigned to a single user [00:01:32]. A user's profile includes their ID, email, and a `roles` property that references this roles object interface [00:01:42].

## Front-End Implementation with Angular

The development begins with a new Angular application with AngularFire2 installed [00:00:44].

### Core Module and Authentication Service
A core module is generated to encapsulate all authentication and authorization logic [00:00:52]. Within this module, an `AuthService` is created [00:00:58].

The [[User authentication with Firebase | authentication process]] involves:
1.  Importing AngularFire libraries [00:01:15].
2.  Defining a custom user interface [00:01:19].
3.  Setting up an observable for the user interface type [00:01:51].
4.  Listening to the AngularFire authentication state to retrieve the user document from [[Firestore security rules setup and implementation | Firestore]] [00:01:57].
5.  Using Google OAuth for [[User authentication with Firebase | user authentication]] [00:02:20].
6.  Upon successful [[User authentication with Firebase | authentication]], an `updateUserData` method is executed to create or update the user document in [[Firestore security rules setup and implementation | Firestore]] [00:02:24]. This method uses `set` with the `merge: true` option to non-destructively update the document, assigning a default role of "subscriber" to new users [00:02:47].

### Implementing Role-Based Abilities
[[RoleBased Authorization with Firestore | Role-based authorization]] is implemented by creating a set of abilities, which are then assigned to authorized roles [00:03:25]. A helper method checks if a user has the appropriate role to perform an ability [00:03:34].

Examples of abilities include:
*   `canRead`: Allows admin, editor, and subscriber roles to read a document [00:04:01].
*   `canEdit`: Allows admin and editor roles to edit [00:04:25].
*   `canDelete`: Only allows the admin role to delete [00:04:30].

These methods can be used to hide or block content in components or in [[Router guards for authorization | router guards]] to control application access [00:04:13].

### Front-End Security Caveat
> [!WARNING] Front-end security provided by Angular is easily circumvented. It is crucial to implement robust back-end [[Firestore security rules setup and implementation | Firestore security rules]] to guarantee data security [00:04:35].

## Back-End Implementation with Firestore Security Rules

To ensure data security, back-end [[Firestore security rules setup and implementation | Firestore security rules]] are essential. These rules determine what actions are permitted based on a user's role.

### Retrieving User Roles in Rules
The `get` method is used within [[Firestore security rules setup and implementation | Firestore rules]] to retrieve a user's document from the database using their `request.auth.uid` [00:04:58]. This allows the rules to inspect the user's `roles` object and enforce access based on the boolean values [00:05:07]. For instance, a subscriber role must be `true` for read access [00:05:12].

### [[Creating custom functions for Firestore security rules | Custom Functions for Firestore Security Rules]]
To make [[Firestore security rules setup and implementation | Firestore rules]] more readable and maintainable, [[Creating custom functions for Firestore security rules | custom functions]] can be defined [00:05:30]. A `getRole` function takes a role name as a string argument and returns whether the authenticated user has that role [00:05:37].

Example of [[Understanding and using Firestore match and allow statements | match and allow statements]] with custom functions:
*   `allow read`: If `getRole('subscriber')` is true [00:05:51].
*   `allow update`: If `getRole('editor')` is true [00:06:05].
*   `allow create, delete`: If `getRole('admin')` is true [00:06:10].

This ensures that even if front-end checks are bypassed, [[Firestore security rules setup and implementation | Firestore]] will deny unauthorized operations, resulting in a [[Firestore security rules setup and implementation | Firestore]] error [00:06:21].

## Integrating Front-End and Back-End Security

While [[Firestore security rules setup and implementation | Firestore rules]] handle data security, front-end logic enhances the user experience by preventing users from attempting unauthorized actions.

### Component-Level Logic
Within components, you can subscribe to the user's observable and use the `AuthService`'s ability methods to lock down specific methods [00:06:53]. For example, `if (authService.canEdit(user))` can wrap code that performs an edit operation [00:07:10].

### Template-Level Logic
For better maintainability, elements that trigger actions (e.g., buttons) can be hidden from the DOM using `ng-if` in the template, leveraging the `AuthService`'s abilities [00:07:23].

### [[Router guards for authorization | Router Guards]] for Route Protection
Angular's [[Router guards for authorization | router guards]] provide a powerful mechanism to prevent unauthorized access to entire routes [00:07:42].
1.  **Create a Guard**: For example, an `AdminGuard` is created and added to the core module [00:07:51].
2.  **Guard Logic**:
    *   Inject the `AuthService` [00:08:04].
    *   Return an observable from `canActivate` that maps to a boolean [00:08:08].
    *   Use `pipe` with `take(1)` to prevent running subscriptions [00:08:15].
    *   Inside `map`, check if the user object exists and if the user has the required role (e.g., `user.roles.admin`) [00:08:21].
    *   Use the `tap` operator (formerly `do`) to log errors or redirect unauthorized users [00:08:37].
3.  **Apply to Routes**: Import and add the guards to the `canActivate` array within the route objects in the router configuration [00:09:14].

This method simplifies the codebase by centralizing access control at the route level and avoids unnecessary [[Firestore security rules setup and implementation | Firestore]] reads to evaluate rules [00:09:24]. Unauthenticated users are denied access, and users with specific roles (e.g., editor) can access authorized pages while restricted from others (e.g., admin pages) [00:09:36].

## Conclusion
The best approach for authorization involves using back-end [[Firestore security rules setup and implementation | Firestore security rules]] for actual data security, complemented by front-end Angular logic (like [[Router guards for authorization | router guards]] and conditional UI rendering) to enhance the user experience [00:09:51].