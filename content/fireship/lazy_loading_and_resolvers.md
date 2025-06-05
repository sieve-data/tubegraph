---
title: Lazy Loading and Resolvers
videoId: Np3ULAMqwNo
---

From: [[fireship]] <br/> 

The Angular Router is a powerful tool for controlling an application's URL structure, performance, and code reusability <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It supports features like [[preloading_data_with_resolve | lazy loading]] for performance and resolvers and guards for writing DRY (Don't Repeat Yourself) code <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Router Outlet and Basic Routing
When a component is routed to, it needs to be a child of another component, typically the `app` component at the root <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The `router-outlet` tells Angular where to render a component based on the navigated URL <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Routes are defined as an array of objects within the `app-routing.module` that conforms to the `Routes` interface <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Each route object includes a `path` and a `component` property <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. For example, the root path (`''`) can be mapped to a `HomeComponent` <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

## Navigation
Angular uses the `routerLink` directive for internal hyperlinks, rather than standard `href` attributes, to prevent full app reloads <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
Programmatic navigation is also possible directly from a component's TypeScript code using the `Router` service's `navigate` method <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This is useful for dynamic navigation, such as after user confirmation <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## Dynamic Routing
To handle dynamic content, such as thousands of database items, [[dynamic_routes_and_child_routing | dynamic routes]] are used <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Child Routes**: Routes can have a `children` property, which takes an array of sub-routes, forming a tree structure <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Child routes are rendered within the parent's `router-outlet` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **URL Parameters**: A dynamic URL parameter is defined by prefixing it with a colon (e.g., `:name`) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This allows navigation to paths like `animal/elephant` <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Accessing Parameters**: The `ActivatedRoute` service provides an observable of route parameters (`paramMap`), allowing components to react to URL changes and fetch corresponding data (e.g., using the `switchMap` operator from RxJS) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Advanced Router Features
*   **Catch-all Route**: A `path '**'` acts as a wildcard, serving as a 404 page for non-existent routes. It must be the very last route in the configuration <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Redirects**: Routes can redirect to different paths using `redirectTo` and `pathMatch` options <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Active Link Styling**: The `routerLinkActive` directive applies CSS classes to an element when its corresponding route is active, making it easy to highlight current navigation links <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## Guards
Guards are Angular services that implement special interfaces to control router behavior <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **`CanActivate`**: This interface determines if a route can be activated <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. It returns a boolean, observable, or promise, which must resolve to `true` for activation <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This is commonly used for authorization checks, potentially with asynchronous API calls <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

## Resolvers
Resolvers are a type of guard that [[preloading_data_with_resolve | preload data]] before a route is activated <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Purpose**: Resolvers prevent components from being rendered before necessary data is available, avoiding situations where the component attempts to display undefined data. They also promote DRY code by centralizing data-fetching logic that might be needed by multiple components <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Implementation**:
    1.  Generate a guard (e.g., `ng generate guard preload`) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    2.  Implement the `Resolve` interface within the guard service <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    3.  The `resolve` method returns the actual data to be made available, often an observable from an external API (like Angular Firestore) <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    4.  If the data source is a real-time stream (e.g., Firebase), the observable *must* be completed (e.g., using the `first` operator) for the resolver to work properly <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Accessing Resolved Data**: Once the route is navigated to, the preloaded data is available on the `route.data` property within the component, eliminating the need for the component to handle the data fetching logic directly <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. The resolver is then applied to the route configuration via the `resolve` property <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.