---
title: Security Measures in Frontend and Backend
videoId: 1PEdd2rtG30
---

From: [[fireship]] <br/> 

Rule-based authorization is a fundamental security measure for any user-moderated website, similar to how Stack Overflow grants users privileges based on reputation [00:00:00]. Implementing this requires a robust solution that secures both the [[front_end_and_back_end_development | front end and the back end]] [00:00:17].

## Core Concepts of Role-Based Authorization

The system works by assigning specific roles to users, which are then saved in Firestore [00:00:21]. These roles dictate the actions a user can perform within the application [00:00:25].

### Defined Roles
*   **Subscriber:** Has the ability to read data only [00:00:29].
*   **Editor:** Can read and update data [00:00:32].
*   **Admin:** Can read, update, create, and delete data [00:00:35].

### Role Storage
Roles are stored as an object in Firestore, with each possible role set to a boolean value [00:01:32]. This flexible structure allows for the assignment of multiple roles to a single user if desired [00:01:38]. Each user document includes a `userId`, `email`, and a `roles` property referencing this roles object [00:01:42].

## Implementation Overview

This security architecture is built using Angular 5 and Firestore, with an `Auth Service` responsible for authentication and authorization logic [00:00:11].

### User Authentication
The authentication process typically involves:
1.  **Observing Auth State:** Listening to the AngularFire authentication state to determine if a user is authenticated [00:02:00].
2.  **Retrieving User Document:** If a user is defined, their corresponding user document is pulled from Firestore [00:02:07].
3.  **Authentication Method:** For example, Google OAuth can be used for user sign-in [00:02:20].
4.  **`updateUserData` Method:** Upon successful authentication, this method creates or updates the user document in Firestore [00:02:29]. It sets a default role of 'subscriber' and uses the `merge: true` option to non-destructively update the document [00:02:43].

## Frontend Security Measures (Angular)

While [[javascript_and_frontend_development | front-end security]] measures enhance user experience, it's crucial to remember that they are not foolproof; client-side rules can be circumvented [00:04:35]. Therefore, they should always be complemented by robust [[implementing_backend_logic_with_webhooks | back-end logic]] [00:09:51].

### Defining User Abilities
A common approach is to define a set of 'abilities' and then assign various roles authorized to perform them [00:03:26].

A helper method checks if a user has the appropriate role for a specific ability [00:03:34]:
```typescript
// Helper method to check if a user has any of the allowed roles
hasRole(user: User, allowedRoles: string[]): boolean {
  if (!user) return false;
  for (const role of allowedRoles) {
    if (user.roles[role]) { // Check if user's roles object has the specific role set to true
      return true;
    }
  }
  return false;
}
```
Examples of abilities:
*   `canRead`: Allows admin, editor, and subscriber roles to read documents [00:04:03].
*   `canEdit`: Allows admin and editor roles to edit [00:04:27].
*   `canDelete`: Only allows the admin role to delete [00:04:30].

### Implementing Frontend Access Control

Frontend access control can be implemented at different levels:

#### Component-Level Logic
You can subscribe to the user's observable within a component's `ngOnInit` to lock down specific methods based on user abilities [00:06:54]. For example, `if (canEdit(user))` can wrap the code responsible for editing a post [00:07:10].

#### Template Logic (ngIf)
For a more maintainable approach, interactive elements like buttons can be hidden from the DOM using Angular's `ngIf` directive based on the `Auth Service`'s ability checks [00:07:31]. This prevents unauthorized users from even seeing options they cannot use [00:07:36].

#### [[router_guards_for_access_control | Router Guards]]
[[router_guards_for_access_control | Router guards]] are a powerful mechanism in Angular to prevent unauthorized access to entire routes based on a user's role or ability [00:07:46].

*   **Admin Guard Example:**
    *   An `AdminGuard` can be created that imports the `Auth Service` [00:07:51].
    *   Within its `canActivate` method, it returns an observable that maps the user's state to a boolean [00:08:09].
    *   It checks if the user object exists and specifically if the `admin` property in the `user.roles` object is true [00:08:23].
    *   The `tap` operator can be used to log an error or redirect the user if they try to access an unauthorized area [00:08:37].

*   **Ability-Based Guard Example:**
    *   A similar guard can be created that checks for a specific ability, like `canRead`, by passing the user object to the `canRead` method from the `Auth Service` [00:09:02]. This authorizes any roles that have the read ability [00:09:10].

These guards are then added to the `canActivate` array within the route objects in the Angular router [00:09:15]. Locking things down at the route level simplifies the codebase and provides an immediate access denial without necessarily requiring a Firestore read [00:09:25].

## Backend Security Measures (Firestore Rules)

[[implementing_security_rules_and_user_authentication | Backend rules]], specifically Firestore security rules, are critical for guaranteeing data security [00:04:42]. They prevent unauthorized data reads or writes directly at the database level [00:04:48].

### Implementing Firestore Rules
1.  **Accessing User Information:** Firestore rules can use `request.auth.uid` to retrieve the authenticated user's document, which contains their `roles` object [00:05:02].
2.  **Initial Rule Example:** A basic rule might state `allow read` if `resource.data.roles.subscriber == true` [00:05:12]. This ensures that if the current user tries to read a document without the `subscriber` role, access is blocked [00:05:16].

### Using Functions in Firestore Rules
To make rules more readable and expressive, especially with multiple roles, Firestore allows defining functions [00:05:30].

*   **`getRole` Function:** A function like `getRole(role: string)` can be created to encapsulate the logic for checking a user's role [00:05:37].
    ```firestore
    // Example Firestore rule function
    function getRole(role) {
      return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.roles[role] == true;
    }
    ```
*   **Applying Functions to Operations:** This function can then be used to define granular permissions for different operations:
    *   `allow read: if getRole('subscriber');` [00:05:51]
    *   `allow update: if getRole('editor');` [00:06:06]
    *   `allow create, delete: if getRole('admin');` [00:06:11]

These rules ensure that even if [[common_web_application_security_risks | frontend security]] is bypassed, the database itself remains secure, preventing unauthorized data manipulation [00:06:21].

## Conclusion

The bottom line for security in web applications is to use [[implementing_security_rules_and_user_authentication | backend Firestore rules]] for actual data security, and then use [[router_guards_for_access_control | router guards]] and additional logic on the [[javascript_and_frontend_development | frontend]] to enhance the user experience [00:09:51]. This multi-layered approach ensures both robust data protection and a smooth user interaction.