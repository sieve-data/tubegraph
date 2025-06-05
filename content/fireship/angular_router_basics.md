---
title: Angular Router Basics
videoId: Np3ULAMqwNo
---

From: [[fireship]] <br/> 

The Angular router is a powerful tool for defining URL structures, controlling performance with lazy loading, and writing DRY (Don't Repeat Yourself) code using resolvers and guards <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It allows you to build sophisticated navigation within your application.

## Getting Started
To begin, you can generate a new Angular 6 application using the [[introduction_to_angular_commandline_interface_cli | Angular CLI]] with the `router` flag, which automatically provides a routing module <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Core Concepts

### Router Outlet
The `router-outlet` is a directive that tells Angular where to render a [[using_angular_components_and_component_architecture | component]] based on the URL the user navigates to <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. When a [[using_angular_components_and_component_architecture | component]] is routed, it becomes a child of another [[using_angular_components_and_component_architecture | component]], typically the root `app` [[using_angular_components_and_component_architecture | component]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Content outside the `router-outlet` (like a nav bar or footer) will persist across routed pages <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Defining Routes
Routes are defined in the `app-routing.module.ts` file as an array typed to the `Routes` interface <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Each route is an object with configuration parameters, most basically a `path` and a `component` to render <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   **Example Root Path:** To set up a home page at the root, give its path an empty string:
    ```typescript
    const routes: Routes = [
      { path: '', component: HomeComponent }
    ];
    ```
    This configuration will render `HomeComponent` at the position of the `router-outlet` when the user navigates to the root URL <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Navigation

### Router Link Directive
When creating hyperlinks in Angular, avoid using a standard `href` attribute, as it will cause the Angular app to completely reload <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. Instead, use the `routerLink` [[angular_directives_and_usage | directive]] <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

*   The `routerLink` [[angular_directives_and_usage | directive]] tells Angular to treat the link as an internal route, accepting the path you would normally route to <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   For [[Dynamic Routes and Child Routing | dynamic routing]], `routerLink` can take an expression (an array of URL segments) by wrapping it in brackets:
    ```html
    <a [routerLink]="['animals', animal.name]"> {{ animal.name }} </a>
    ```
    The array's items represent URL segments, allowing for dynamic construction of links <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Programmatic Navigation
You can also navigate directly from within a [[using_angular_components_and_component_architecture | component]]'s TypeScript code, useful for dynamic navigation that isn't tied to a link click <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

*   Import the `Router` service into your [[using_angular_components_and_component_architecture | component]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   Use `router.navigate()` with an array of URL segments to navigate to a specific path <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    ```typescript
    // Inside a component method
    if (confirm('Do you want to navigate?')) {
        this.router.navigate(['/animals', 'elephant']);
    }
    ```

## Advanced Routing

### [[Dynamic Routes and Child Routing | Dynamic URL Parameters and Child Routes]]
For applications pulling information from a database, such as displaying details for thousands of items, you cannot hardcode every route manually <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

*   **[[Dynamic Routes and Child Routing | Dynamic URL Parameters]]:** Define a dynamic URL parameter by placing a colon (`:`) in front of the parameter name (e.g., `:name`) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This allows routing to paths like `/animals/elephant` where "elephant" is the dynamic parameter <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Child Routes:** Create child routes that render inside their parent [[using_angular_components_and_component_architecture | component]] by adding a `children` property to the parent route configuration <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The `children` property takes an array of routes, forming a tree structure <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Data Retrieval with [[Dynamic Routes and Child Routing | Dynamic Routes]]
To retrieve data based on a dynamic URL parameter in a child [[using_angular_components_and_component_architecture | component]]:

*   Inject the `ActivatedRoute` service into the [[using_angular_components_and_component_architecture | component]] to listen to state changes in the router <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   The `params` observable from `ActivatedRoute` provides an observable of route parameters <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
*   Use the `switchMap` operator from RxJS to switch to an observable of the actual data, fetching it from a database like Firestore using the parameter's value (e.g., `params.get('name')`) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   The [[using_angular_components_and_component_architecture | component]] is initialized once, so subsequent navigations to child routes won't call `ngOnInit` again, necessitating parameter observation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

## Useful Router Features

### Wildcard Route (404 Page)
A wildcard route (`**`) can be used as a catch-all for paths that don't match any defined routes, serving as a 404 page <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This route should always be the very last route in your configuration <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

```typescript
const routes: Routes = [
  // ...other routes
  { path: '**', component: ErrorComponent } // Must be last
];
```

### Redirects
You can redirect from one route to another, useful for handling common misspellings or deprecated paths <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
A redirect route requires the `redirectTo` property and the `pathMatch` option (e.g., `'full'`) to avoid errors <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

```typescript
const routes: Routes = [
  { path: 'animalz', redirectTo: '/animals', pathMatch: 'full' },
  // ...other routes
];
```

### `routerLinkActive` [[angular_directives_and_usage | Directive]]
The `routerLinkActive` [[angular_directives_and_usage | directive]] applies a CSS class to an element when its associated route is active <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This simplifies building UI features that highlight the user's current link <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

```html
<a routerLink="/home" routerLinkActive="active">Home</a>
```

## Route Guards and Resolvers
Guards are Angular services that implement special interfaces to interact with the router, enabling route protection, reusable code, and data preloading <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### `CanActivate` Guard
The `CanActivate` interface is commonly used to protect routes from unauthorized users <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. It only activates a route if the guard's logic returns `true` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

*   **Implementation:** Generate a guard using `ng generate guard admin` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The guard must be `injectable` and implement `CanActivate` <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   **Return Value:** The `canActivate` method must return a boolean, an observable of a boolean, or a promise of a boolean <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. If an observable is returned, it automatically subscribes <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Asynchronous Checks:** For asynchronous authorization checks (e.g., against an API), you can simulate a delay with a timer and map the emitted value to a boolean <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The `tap` operator can be used to show alerts or redirect to a login page <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
*   **Usage:** Apply the guard to a route using the `canActivate` property in the route configuration <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### `Resolve` Guard
The `Resolve` interface allows you to preload data into your route before the [[using_angular_components_and_component_architecture | component]] is activated <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. This avoids repeating data-fetching logic in multiple [[using_angular_components_and_component_architecture | components]] <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

*   **Implementation:** Generate a guard and implement the `Resolve` interface, optionally strong-typing it <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Return Value:** The `resolve` method returns the actual data you want to be available when the route is navigated to, commonly an observable <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
*   **Data Access:** The guard receives the `next` parameter (snapshot of the activated route) to retrieve URL parameters <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Observable Completion:** When fetching data from a real-time stream like Firebase, use the `first` operator to ensure the observable completes, which is required for the resolver to work properly <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Accessing Resolved Data:** In the [[using_angular_components_and_component_architecture | component]], the preloaded data is available on the `ActivatedRoute`'s `data` property <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
*   **Usage:** Add the `resolve` property to your route configuration, mapping a key to your resolver <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

By mastering these fundamental and advanced features, the Angular router enables the creation of scalable and efficient single-page applications <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.