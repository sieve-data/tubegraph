---
title: Guards and Route Protection
videoId: Np3ULAMqwNo
---

From: [[fireship]] <br/> 
The Angular router is a powerful tool that offers more than just defining URL structures; it can also control performance with lazy loading and help write DRY (Don't Repeat Yourself) code using resolvers and [[router_guards_for_access_control | guards]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This article focuses on how [[router_guards_for_access_control | guards]] can be used to protect routes and preload data.

### What are Guards?
A [[router_guards_for_access_control | guard]] is an Angular service that implements specific interfaces to interact with the router <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. They are commonly used to protect routes from unauthorized users or to preload data into components <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### CanActivate Guard (Route Protection)
One of the most common uses for a [[router_guards_for_access_control | guard]] is to protect routes from unauthorized users <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

#### Generating a Guard
To create a guard, you can use the Angular CLI command `ng generate guard [guard-name]` <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. For example, `ng generate guard admin` would create a guard named 'admin' to protect routes from non-admin users <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

#### Implementing `CanActivate`
The `CanActivate` interface is used to determine if a route can be activated <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This route will only activate if the [[router_guards_for_access_control | guard]] returns `true` <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

To apply the `CanActivate` guard, add the `canActivate` property to the route definition in your router configuration, assigning it the guard <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

Inside the guard, it is decorated with `@Injectable` like any other Angular service <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. The `canActivate` method provided by the interface receives information about the route's state <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. For the guard to work, it must return a boolean, an observable, or a promise <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. If it returns an observable, it will automatically subscribe for you <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. For instance, returning `false` will block access to the route and can be accompanied by an alert message <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.

#### Asynchronous Authorization Checks
In real-world scenarios, authorization checks often need to be asynchronous, typically by checking with an API to verify user authorization <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. This can be simulated with a timer, mapping the emitted value to a boolean <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. The `tap` operator can be used to show an alert or redirect to a login page if authorization fails <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. When navigating to a page protected by an asynchronous `CanActivate` [[router_guards_for_access_control | guard]], there will be a delay until the observable resolves before the route is blocked or allowed <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. This is a key component of [[implementing_security_rules_and_user_authentication | implementing security rules and user authentication]] in the frontend.

### Resolve Guard (Preloading Data)
Beyond `CanActivate`, the `Resolve` interface allows for preloading data into a route before the component is rendered <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. This prevents duplicating data fetching logic across multiple components <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.

#### Generating and Implementing `Resolve`
Generate a new guard (e.g., `preload`) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Instead of `CanActivate`, implement the `Resolve` interface <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. The `resolve` method should return the actual data you want to be available when the route is navigated to, commonly as an observable from an external API or database like [[firestore_security_rules_setup_and_implementation | Firestore]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

The [[router_guards_for_access_control | guard]] can access URL parameters via `next.params` <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. When fetching data from a real-time stream like Firebase, it's crucial to pipe the `first` operator to ensure the observable completes for the [[router_guards_for_access_control | guard]] to work properly <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

#### Making Preloaded Data Available
Once the data is preloaded by the `Resolve` [[router_guards_for_access_control | guard]], it becomes available on the `route.data` property of the `ActivatedRoute` in the component <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. To apply the `Resolve` [[router_guards_for_access_control | guard]], add the `resolve` property to the route configuration <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This approach isolates the data-fetching code in a reusable way, which can be applied to multiple routes as needed <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

The Angular Router, as a [[framework_features_like_routing_and_database_integration | framework feature]], provides these powerful [[router_guards_for_access_control | guards]] to enhance application logic, security, and data handling <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.