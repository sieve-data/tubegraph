---
title: Capabilities and limitations of hybrid apps with Ionic and Cordova
videoId: 34fDUKaJBtw
---

From: [[fireship]] <br/> 

The beta release of Ionic 4, announced recently, introduces a suite of new features leveraging web technologies <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This version presents significant changes, especially for those [[migrating_from_ionic_3_to_ionic_4 | migrating from Ionic 3 to 4]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. When considering if Ionic is the right choice, it's crucial to understand the trade-offs of various mobile app development strategies <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Mobile App Development Approaches

There are three primary ways to build mobile apps today <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>:

### 1. Native SDKs Directly
This approach involves writing a separate application for each target platform using its native language <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Android**: Kotlin or Java <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>
*   **iOS**: Swift or Objective-C <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   **Web**: JavaScript <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

**Pros:**
*   Generally yields the highest quality and best-performing apps <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

**Cons:**
*   Higher cost due to more code maintenance <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   Requires hiring specific talent for each platform, which can be challenging, especially for iOS and Android <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### 2. [[hybrid_app_development_with_ionic_4 | Hybrid Mobile App Development]]
Ionic 4 falls into this category, utilizing web technologies to build apps <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The core idea is to write code once and run it seamlessly on multiple platforms <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

*   **Definition**: A hybrid app is essentially a web app embedded on the native device through a webview <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Native Device Interaction**: Hybrid apps cannot directly communicate with many native device features <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. They use a bridge, such as [[integration_of_media_in_mobile_applications | Apache Cordova]] or Capacitor, which wraps native code in a JavaScript API accessible by the web app <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

**Pros:**
*   Allows leveraging web developers to build [[crossplatform_mobile_app_development | cross-platform]] mobile apps for a lower cost <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   If executed well, it can be indistinguishable from a truly native app <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

**Cons:**
*   Decoupling from native SDKs can make debugging and performance optimization more difficult <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### 3. Cross-Platform Frameworks (e.g., React Native, Flutter, NativeScript)
These frameworks differ from Ionic because they do not use a webview for the UI <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

**Advantages over Ionic:**
*   **Native Code Execution**: Can run purely native code, allowing developers to overcome certain performance issues as they interact directly with native SDK code, without a bridge <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. [[flutter_app_integration_with_firebase | Flutter]], for example, does not use a bridge at all, leading to better out-of-the-box performance <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Hot Reloading**: Unlike Ionic's live reloading, hot reloading maintains the app's state while updating code changes, significantly speeding up the development process, especially with native emulators <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Testing Resources**: More resources are dedicated to testing on real mobile devices <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Ionic 4 does offer testing guidance based on Angular CLI's Jasmin and Karma, which is good for the web <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

**Drawbacks of these frameworks:**
*   **Learning Curve**: [[flutter_app_integration_with_firebase | Flutter]] requires learning the Dart programming language, which is relatively obscure <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Performance Bottlenecks**: React Native's bridge can hit performance bottlenecks, potentially requiring more native code than initially intended <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## When to Use Ionic 4: Real-World Scenarios

The decision to use Ionic 4 largely depends on how the app will be delivered to customers <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Scenario 1: Focus on Progressive Web Apps (PWA) Only
*   If the primary focus is on PWAs (supported by all major browsers), Ionic 4 is useful as a component library <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   An Ionic 4 app resembles a vanilla Angular 6 CLI app <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Its main value-add over plain Angular is access to pre-built components and services for common UI use cases <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Scenario 2: PWA as Primary Product with iOS/Android Support Desired
*   This is the niche where [[hybrid_app_development_with_ionic_4 | hybrid apps]] excel <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   If a PWA is the main product, Ionic 4 makes it relatively easy to take the existing codebase and deploy it to the App Store without significantly increasing development costs <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Scenario 3: Mobile App as Primary Product (PWA as Afterthought or Non-existent)
*   Ionic 4, which leverages web technologies like web components, feels optimized for products building PWAs <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   While Ionic 4 can be used exclusively for building native mobile apps, non-webview frameworks (like React Native or Flutter) offer advantages in terms of pure native code execution, hot reloading, and testing resources, which might be more beneficial for mobile-first products <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Ionic 4 Developer Experience and Key Changes

To work with Ionic 4, `ionic` needs to be installed globally with NPM (version 4.0 or greater) <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.

### Core Architecture Shift
*   Ionic 4 now uses web components (made possible by the Stencil library) instead of Angular components <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   This change makes Ionic 4 framework-agnostic, allowing use with Vue.js, Angular, React, or plain JavaScript <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   First-class support for Angular remains, and an Ionic 4 app with Angular looks very similar to an Angular 6 CLI project, using Angular 6 CLI under the hood <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
*   It adds specific elements for native mobile apps, such as `config.xml` for [[integration_of_media_in_mobile_applications | Cordova]] and a resources file for native builds <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

### Project Structure and Migration
*   For those [[migrating_from_ionic_3_to_ionic_4 | migrating from Ionic 3]], the project directory structure has changed <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. All app code is contained within the `app` directory, following a typical Angular app pattern <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   Migration can involve copying and pasting code into the `app` directory, with VS Code plugins available to help rewrite paths <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Routing
*   A significant change in Ionic 4 is the adoption of the Angular router, replacing Ionic's zone push/pop navigation system <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   This is a positive change, as the Angular router is powerful <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   It provides better tools for managing router state <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Generating a new page component automatically wires it up with the router for lazy loading <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   Paths are now easier for deep linking as they are regular URLs, not using the hash location strategy seen in Ionic 3 <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Component and API Changes
*   There are breaking changes in how components are set up, but they are minor <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   The Ionic button is now a custom element instead of a directive, retaining built-in mechanisms for shape, color, and style <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   Navigating between pages with a button is simplified by using Angular's `routerLink` directive <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   A detailed GitHub documentation outlines all breaking changes, which are mainly naming conventions, making the overall feel similar to Ionic 3 <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   It will be possible to use Capacitor plugins instead of [[integration_of_media_in_mobile_applications | Cordova]] plugins in the future <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   "Providers" are now called "services," aligning with Angular conventions, and they function identically <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   Some synchronous APIs are now asynchronous, requiring the use of `async`/`await` syntax (e.g., with the alert controller) <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## Conclusion

Ionic 4 is a viable choice for mobile app development, provided the use case aligns with a [[hybrid_app_development_with_ionic_4 | hybrid app]] strategy <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. The decision ultimately depends on an evaluation of one's specific situation and weighing the pros and cons of the available options <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.