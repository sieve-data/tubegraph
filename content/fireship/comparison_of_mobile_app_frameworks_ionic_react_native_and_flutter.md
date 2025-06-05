---
title: Comparison of mobile app frameworks Ionic React Native and Flutter
videoId: 34fDUKaJBtw
---

From: [[fireship]] <br/> 

The landscape of mobile app development in 2018 offers various strategies for building and delivering applications, each with distinct trade-offs that are crucial for making informed business decisions <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. When deciding whether to use [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] for a mobile app, it's essential to understand specific technical demands and weigh the pros and cons of different approaches <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Mobile App Development Approaches

There are three primary methods for building mobile apps today <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:

### 1. [[native_mobile_app_development_versus_hybrid_apps | Native Mobile App Development]] with SDKs
This approach involves writing a separate app for each platform using its native language <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Android**: Kotlin or Java <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **iOS**: Swift or Objective-C <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Web**: JavaScript <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

> [!P PROS]
> *   Generally results in the highest quality and best-performing apps <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

> [!C CONS]
> *   Higher cost due to more code to maintain <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
> *   Difficulty in hiring talent for specific iOS and Android codebases <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### 2. [[native_mobile_app_development_versus_hybrid_apps | Hybrid Mobile Apps]] with Web Technologies (e.g., Ionic 4)
This strategy, where [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] fits, aims to write code once and run it seamlessly on multiple platforms <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. A [[native_mobile_app_development_versus_hybrid_apps | hybrid app]] is essentially a web app embedded on a native device via a webview <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. It communicates with native device features indirectly using a bridge like Apache Cordova or Capacitor, which wraps native code in a JavaScript API <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

> [!P PROS]
> *   Leverages web developers to build [[crossplatform_app_development_with_flutter | cross-platform]] mobile apps at a lower cost <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
> *   If well-executed, can be indistinguishable from a truly [[native_mobile_app_development_versus_hybrid_apps | native app]] <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

> [!C CONS]
> *   Decoupling from native SDKs can make debugging and [[performance_and_developer_experience_in_react_native_and_flutter | performance optimization]] more difficult <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### 3. Frameworks like [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] or [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]]
These frameworks differ from [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] by not using a webview for the UI <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. They achieve [[crossplatform_app_development_with_flutter | cross-platform app development]] by rendering directly to native components or drawing their own UI, which can offer significant advantages <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Real-World Scenarios and Framework Suitability

When deciding if [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] is a good fit, the delivery method of the app to customers is key <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Scenario 1: Progressive Web App (PWA) Focus
If the focus is solely on Progressive Web Apps (PWAs), which are supported by all major browsers, [[differences_and_simila|Ionic]] is primarily useful as a component library <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. An [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] app, especially when combined with Angular, offers pre-built components and services for common UI use cases <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Scenario 2: PWA Primary, Mobile Apps Secondary
This is where [[native_mobile_app_development_versus_hybrid_apps | hybrid apps]] like those built with [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] shine brightest <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. If a PWA is the main product, [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] simplifies deploying the existing codebase to app stores for iOS and Android without tripling development costs <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Scenario 3: Mobile App Primary, PWA Secondary or Non-Existent
For products where the mobile app is primary, and a PWA is an afterthought or not needed, [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]], optimized for PWAs and web components, might not be the best fit <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. Non-webview frameworks like [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] or [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] offer advantages <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Advantages of Non-Webview Frameworks ([[react_native_vs_flutter_comparison | React Native vs Flutter comparison]])

Compared to [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]] (hybrid apps), frameworks like [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] and [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] offer specific benefits:

### 1. Pure Native Code Execution
*   [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] and [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] allow running purely native code <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   This can overcome performance issues because developers interact directly with [[native_mobile_app_development_versus_hybrid_apps | native SDK]] code, avoiding a bridge <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] notably does not use a bridge at all, often leading to better out-of-the-box [[performance_and_developer_experience_in_react_native_and_flutter | performance]] <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### 2. [[performance_and_developer_experience_in_react_native_and_flutter | Hot Reloading]]
*   Unlike [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]]'s live reloading, [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] and [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] feature [[performance_and_developer_experience_in_react_native_and_flutter | hot reloading]] <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   [[performance_and_developer_experience_in_react_native_and_flutter | Hot reloading]] maintains the app's state while updating code changes, significantly speeding up development, especially when working with native emulators <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

### 3. Testing Resources
*   While [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] offers testing guidance based on Angular CLI with Jasmine and Karma (great for web), [[performance_and_developer_experience_in_react_native_and_flutter | React Native]] and [[performance_and_developer_experience_in_react_native_and_flutter | Flutter]] have more resources dedicated to testing on real mobile devices <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Drawbacks of Non-Webview Frameworks ([[react_native_vs_flutter_comparison | React Native vs Flutter comparison]])

> [!C CONS]
> *   **[[performance_and_developer_experience_in_react_native_and_flutter | Flutter]]**: Requires learning Dart, a relatively obscure programming language <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
> *   **[[performance_and_developer_experience_in_react_native_and_flutter | React Native]]**: Can hit performance bottlenecks with its bridge, potentially leading to more native code being written than initially intended <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## [[building_mobile_app_components_with_flutter | Ionic 4]] Specifics

[[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] introduced significant changes:

*   **Framework Agnostic**: A major shift in [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] is the use of web components, enabled by Stencil <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This makes [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] framework agnostic, meaning it can be used with Vue.js, Angular, [[performance_and_developer_experience_in_react_native_and_flutter | React]], or plain JavaScript <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. First-class support for Angular remains <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Angular CLI Integration**: An [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] app closely resembles an Angular 6 CLI project, as it uses the Angular 6 CLI under the hood <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. It adds specific elements for [[native_mobile_app_development_versus_hybrid_apps | native mobile apps]], such as `config.xml` for Cordova and a `resources` file for native builds <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Routing with Angular Router**: A positive change in [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] is the adoption of the Angular router instead of [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic]]'s previous navigation system <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. This provides more powerful tools for managing router state and simplifies deep linking as paths become regular URLs <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. Generating a new page component automatically wires it up for lazy loading <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Component Changes**: [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] components, like the `ionic-button`, are now custom elements instead of directives, though they retain expected styling and control mechanisms <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Navigation between pages is streamlined using the `routerLink` directive <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Plugins**: Future versions will support Capacitor plugins in addition to Cordova plugins <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Services and Asynchronous APIs**: "Providers" are now aligned with Angular conventions and called "services" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Some synchronous APIs are now asynchronous, allowing for `async`/`await` syntax <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## Conclusion

The choice of framework among [[comparing_flutter_to_react_native_and_ionic | Ionic, React Native, and Flutter]] ultimately depends on specific project requirements and technical demands <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Ionic 4]] is a suitable choice, especially for a [[native_mobile_app_development_versus_hybrid_apps | hybrid app]] strategy, particularly when Progressive Web Apps are a primary product focus <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.