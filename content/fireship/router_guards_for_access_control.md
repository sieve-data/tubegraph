---
title: Router Guards for Access Control
videoId: 1PEdd2rtG30
---

From: [[fireship]] <br/> 

[[Guards and Route Protection | Router Guards]] are a mechanism in Angular that helps prevent unauthorized access to specific routes or content within an application based on a user's role or abilities <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>. They enhance [[Security Measures in Frontend and Backend | front-end security]] and improve the user experience by conditionally displaying or hiding content <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

## Creating a Router Guard

To create a router guard, you can generate it using the Angular CLI, typically within a core module to isolate authentication and authorization logic <a class="yt-timestamp" data-t="00:52:00">[00:52:00]</a>, <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>:

1.  Generate a guard, e.g., `admin.guard.ts` <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
2.  Import the [[Implementing Angular and Firestore for Authorization | Auth Service]] and RxJS operators like `tap`, `map`, and `take` <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

## Implementing Logic in `canActivate`

The core logic for access control resides within the `canActivate` method of the guard <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. This method should return an observable that maps to a boolean value <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

*   **Pipe RxJS Operators**: Use the `pipe` method with operators like `take(1)` to prevent a running subscription <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   **Access User Data**: Within the `map` operator, check if the user object exists and inspect its roles property <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. For example, to restrict access to admin users, check `user.roles.admin` <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.
*   **Check Abilities**: Instead of checking specific roles, you can pass the user object to an `AuthService` method like `canRead` to authorize any roles associated with that specific ability <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>.
*   **Handle Unauthorized Access**: Use the `tap` operator to log an error to the console if the user is unauthorized <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>. Alternatively, you can use the [[Angular Router Basics | Angular Router]] to redirect the user to a different route <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.

### Example `canActivate` Logic:

```typescript
// Inside the guard
canActivate(
  next: ActivatedRouteSnapshot,
  state: RouterStateSnapshot): Observable<boolean> {

  return this.auth.user$.pipe(
    take(1),
    map(user => {
      // Check for a specific role
      const isAdmin = user && user.roles.admin;
      if (isAdmin) {
        return true;
      }

      // Or check for an ability using the auth service
      // const canRead = user && this.auth.canRead(user);
      // if (canRead) {
      //   return true;
      // }

      console.log('Access Denied!');
      return false;
    }),
    tap(canAccess => {
      if (!canAccess) {
        // Optionally redirect here
      }
    })
  );
}
```

## Applying Router Guards to Routes

Once created, guards are applied to route objects in the [[Angular Router Basics | Angular Router]] configuration using the `canActivate` array <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>:

```typescript
// Inside your routing module
import { AdminGuard } from './guards/admin.guard';
import { ReadGuard } from './guards/read.guard';

const routes: Routes = [
  { path: 'admin-page', component: AdminComponent, canActivate: [AdminGuard] },
  { path: 'content', component: ContentComponent, canActivate: [ReadGuard] },
  // ...other routes
];
```

## Benefits of Router Guards

*   **Code Simplification**: Locking down access at the [[Dynamic Routes and Child Routing | route level]] simplifies the overall codebase <a class="yt-timestamp" data-t="09:24:00">[09:24:00]</a>.
*   **Enhanced User Experience**: Prevents unauthorized users from even attempting to access restricted pages <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>. For example, an unauthenticated user will be denied access to protected pages directly by the guard <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>, and an editor role will be able to access main content but still be blocked from an admin page <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
*   **Front-end Security**: Provides a layer of protection that prevents users from navigating to unauthorized areas on the client-side <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>.

## Security Considerations

It's crucial to remember that anything implemented in Angular, including [[Guards and Route Protection | router guards]], only provides [[Security Measures in Frontend and Backend | front-end security]] <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>, <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. It would be trivial to reverse engineer and circumvent these rules on the client side <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. Therefore, [[firestore_security_rules_setup_and_implementation | back-end Firestore security rules]] are essential for guaranteeing data security and preventing unauthorized data reads or writes <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>, <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. The goal is to use router guards to enhance the user experience by preventing unauthorized actions from even reaching the backend rules <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>, <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.