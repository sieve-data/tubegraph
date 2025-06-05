---
title: Dynamic Routes and Child Routing
videoId: Np3ULAMqwNo
---

From: [[fireship]] <br/> 

The Angular Router is a powerful tool for defining the URL structure of your application, controlling performance with lazy loading, and writing modular code using resolvers and guards <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article will cover the basics of defining dynamic and child routes, along with techniques for fetching data and controlling navigation.

## Router Outlet

The `router-outlet` is a directive that tells Angular where to render a component based on the current URL <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. When a component is routed to, it becomes the child of another component, typically the root `app` component by default <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Defining Routes

Routes are defined in the application's routing module (e.g., `app-routing.module.ts`) as an array of objects that conform to the `Routes` interface <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Each route object typically contains a `path` and a `component` to render <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The root path of the application is represented by an empty string (`''`) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Navigating Between Components

For navigation within an Angular application, the `routerLink` directive is used instead of a standard `href` attribute <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Using `href` would cause the entire Angular application to reload <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. The `routerLink` directive takes the path to which to navigate <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

## Dynamic URL Parameters

In real-world applications, you often need to route to specific items (e.g., an animal by its ID or name) from a large database without hardcoding every possible route <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This is achieved using dynamic URL parameters.

### Defining Dynamic Parameters

A dynamic URL parameter is defined in the route configuration by placing a colon (`:`) in front of the parameter name (e.g., `:name`) <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This allows paths like `animal/elephant` or `animal/aardvark` to route to the same component while passing different data <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

### Building Dynamic `routerLink`s

To generate links dynamically (e.g., from a list of items pulled from a database), `routerLink` can accept an array expression enclosed in brackets `[]` <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Each item in this array represents a URL segment <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. For example, `['animals', animal.name]` would create a link like `/animals/elephant` <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Child Routes

Child routes are routes that are rendered *inside* of their parent component <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Configuration

Child routes are defined by adding a `children` property to the parent route object in the routing configuration <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The `children` property takes an array of routes, forming a tree structure <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Rendering Child Components

Just like the main application component needs a `router-outlet` at the root, a parent component that hosts child routes must also include a `router-outlet` within its template to tell the router where to render the child components <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Retrieving Dynamic Data in Child Components

Fetching data based on dynamic URL parameters requires specific handling, especially since the component might not be re-initialized (i.e., `ngOnInit` might not be called again) when only a child route parameter changes <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### ActivatedRoute Service

The Angular Router provides the `ActivatedRoute` service, which allows components to listen to state changes in the router <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### Listening to Parameter Changes

To react to changes in URL parameters, you can subscribe to `ActivatedRoute.paramMap`, which returns an observable of the route parameters <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. When a change occurs, the `switchMap` RxJS operator can be used to switch to a new observable that fetches the actual data based on the updated parameter <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. The parameter value can be retrieved using `params.get('parameterName')` (e.g., `params.get('name')`) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

## Programmatic Navigation

While `routerLink` is useful for direct link clicks, you can also navigate programmatically from within a component's TypeScript code <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This is useful for dynamic scenarios, such as after a user confirms an action <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

To do this, inject the `Router` service into your component. You can then use `router.navigate()` and pass it an array of URL segments, similar to how `routerLink` accepts an array <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Advanced Router Techniques

### Wildcard (404) Routes

A "catch-all" route can be created to serve as a 404 page for non-existent URLs <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This is defined with a path of `**` (e.g., `path: '**', component: ErrorComponent`) and should always be the *last* route in your configuration to ensure all other routes are checked first <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Redirects

You can redirect one route to another. For example, to redirect `animals-typo` to `animals`, you would define a route with `path: 'animals-typo'`, `redirectTo: 'animals'`, and crucially, `pathMatch: 'full'` <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. The `pathMatch` option is required for redirect routes <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Router Link Active

The `routerLinkActive` directive allows you to apply CSS classes to an HTML element when the associated [[Angular Router Basics | route]] is active <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. This is useful for UI features like highlighting the current page in a navigation bar <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. It expects a list of CSS classes on the right-hand side <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

## Guards: Preloading Data with `Resolve`

[[Guards and Route Protection | Guards]] are Angular services that implement special interfaces to control router behavior <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. One such interface, `Resolve<T>`, is particularly useful for preloading data into a route before the component is activated <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.

Instead of fetching data inside the component (e.g., using `paramMap` and `switchMap`), a `Resolve` guard can handle the data fetching, making the code more reusable <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

### Implementing a `Resolve` Guard

1.  **Generate a Guard:** Use `ng generate guard preload` <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
2.  **Implement `Resolve`:** The guard service implements the `Resolve` interface and typically returns an observable of the data to be preloaded <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
3.  **Fetch Data:** Inside the `resolve()` method, you can access the route parameters via `route.paramMap.get('parameterName')` and fetch the data (e.g., from an API or database) <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. If fetching from a real-time stream (like Firebase), you might need to pipe the `first()` operator to ensure the observable completes <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
4.  **Add to Route Config:** In your `app-routing.module.ts`, add the `resolve` property to the route definition, mapping a key (e.g., `'animal'`) to your `PreloadGuard` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### Accessing Preloaded Data in the Component

Once configured, the preloaded data becomes available on the `ActivatedRoute.data` property within the component <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. For example, `this.route.data.pipe(map(data => data.animal))` would give you access to the preloaded `animal` data <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. This effectively isolates the data fetching logic from the component, making it more modular and reusable <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.