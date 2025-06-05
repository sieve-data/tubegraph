---
title: Hybrid app development with Ionic 4
videoId: 34fDUKaJBtw
---

From: [[fireship]] <br/> 

The beta release of Ionic 4 brought a new suite of features leveraging web technologies <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This version introduces important changes, especially for those [[migrating_from_ionic_3_to_ionic_4 | migrating from Ionic 3 to 4]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Deciding whether to use Ionic involves understanding various [[crossplatform_mobile_app_development | cross-platform app development]] strategies and their trade-offs <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Should You Use Ionic?

To determine if Ionic is suitable for a mobile app, it's crucial to assess technical demands and weigh the pros and cons of different [[native_mobile_app_development_versus_hybrid_apps | mobile app development approaches]] <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

### Mobile App Development Approaches

Three primary methods are used to build mobile apps today <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>:

1.  **Native SDKs Directly** <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
    *   Requires writing a separate app for each platform (e.g., Kotlin/Java for Android, Swift/Objective C for iOS, JavaScript for web) <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   **Pros:** Generally produces the highest quality and best-performing apps <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   **Cons:** Higher cost due to more code maintenance and the need to hire specialized talent for each platform <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

2.  **Hybrid Mobile Apps (Ionic 4's Category)** <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
    *   Aims to write code once and deploy it across multiple platforms <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
    *   A hybrid app is essentially a web app embedded on a native device via a webview <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Utilizes a bridge (like Apache Cordova or Capacitor) to wrap native code in a JavaScript API, enabling web app access to native device features <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   **Pros:** Leverages web developers for [[crossplatform_mobile_app_development | cross-platform mobile apps]] at a lower cost <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Can be indistinguishable from a truly native app if done well <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   **Cons:** Decoupling from native SDKs can make debugging and performance optimization more challenging <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. See [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | Capabilities and limitations of hybrid apps with Ionic and Cordova]].

3.  **Frameworks like React Native, Flutter, or NativeScript** <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>
    *   Unlike Ionic, these frameworks do not use a webview for the UI <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   **Advantages over Ionic:**
        *   Ability to run purely native code, overcoming performance issues by interacting directly with native SDKs without a bridge (especially true for Flutter) <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
        *   Hot reloading, which maintains app state while updating code changes, accelerating development with native emulators <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
        *   More dedicated resources for testing on real mobile devices <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. See [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Comparison of mobile app frameworks Ionic React Native and Flutter]].
    *   **Drawbacks:**
        *   [[crossplatform_app_development_with_flutter | Flutter]] has a learning curve for the Dart programming language <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
        *   React Native's bridge can lead to performance bottlenecks, potentially requiring more native code than intended <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Real-World Scenarios for Ionic 4

The decision to use Ionic 4 largely depends on the app delivery strategy <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

*   **Progressive Web App (PWA) Focus:** If the primary focus is on PWAs (supported by all major browsers), Ionic 4 is useful as a component library <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Ionic 4 apps resemble vanilla Angular 6 CLI apps, with Ionic's value-add being pre-built components and services for common UI use cases <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **PWA Primary, iOS/Android Secondary:** This is where [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | hybrid apps shine the brightest]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. If a PWA is the main product, Ionic 4 makes it relatively easy to deploy the existing codebase to app stores without tripling development costs <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Mobile App Primary, PWA Secondary/Non-Existent:** Ionic 4, with its reliance on web components, is optimized for products building PWAs <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. While it can be used for native mobile apps exclusively, non-webview frameworks like React Native or Flutter offer advantages, especially regarding performance and direct native code interaction <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Developer Experience with Ionic 4

To begin, Ionic needs to be installed globally via NPM, ensuring version 4.0 or greater <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Key Changes

*   **Web Components and Framework Agnostic:** A major shift in Ionic 4 is the use of web components instead of Angular components, enabled by the Stencil library <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This makes Ionic 4 framework-agnostic, allowing use with Vue.js, Angular, React, or plain JavaScript <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. First-class support for Angular remains <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   **Angular CLI Integration:** An Ionic 4 project closely resembles an Angular 6 CLI project, as it uses the Angular 6 CLI under the hood <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. It adds specific elements for native mobile apps, like `config.xml` for Cordova and a `resources` file for native builds <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **[[migrating_from_ionic_3_to_ionic_4 | Project Structure Changes (from Ionic 3)]]:**
    *   All app code is in the `app` directory, mirroring a typical Angular app <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   Code migration can involve copying into the `app` directory, with VS Code plugins helping rewrite paths <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Angular Router Integration:** Ionic 4 now uses the Angular router, replacing Ionic's push/pop navigation system <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. This is a positive change, offering powerful routing capabilities and improved deep linking via regular URLs instead of hash-based strategies <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   Generating a new page component automatically wires it up with the router for lazy loading <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
    *   Navigating between pages using `routerLink` directives from Angular includes smooth animations <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **Component Setup:** There are breaking changes in component setup, but they are minor, mostly involving naming conventions, making migration relatively easy <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. For instance, the Ionic button is now a custom element instead of a directive <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Detailed documentation on breaking changes is available on GitHub <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Capacitor Plugins:** Future support will include Capacitor plugins as an alternative to Cordova plugins <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Services (formerly Providers):** What were called "providers" in Ionic 3 are now consistently named "services" in Ionic 4, aligning with Angular conventions <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Functionality remains the same <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Asynchronous APIs:** Some synchronous APIs are now asynchronous. For example, rendering UI elements like alerts happens within the context of a promise, allowing the use of async/await syntax <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## Conclusion

Ionic 4 is a recommended choice for hybrid app development, provided the use case aligns with the [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | hybrid app strategy]] <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.