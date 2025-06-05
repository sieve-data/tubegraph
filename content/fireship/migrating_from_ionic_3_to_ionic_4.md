---
title: Migrating from Ionic 3 to Ionic 4
videoId: 34fDUKaJBtw
---

From: [[fireship]] <br/> 

The beta release of [[Hybrid app development with Ionic 4 | Ionic 4]] brought a suite of new features leveraging web technologies. This update includes significant changes, particularly for those [[Hybrid app development with Ionic 4 | migrating from Ionic 3 to Ionic 4]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Changes in Ionic 4

### Framework Agnostic with Web Components
A major difference in [[Hybrid app development with Ionic 4 | Ionic 4]] is its shift from using [[Using Angular components and component architecture | Angular components]] to using Web Components <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This is made possible by the Stencil library <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
This transition makes [[Hybrid app development with Ionic 4 | Ionic 4]] framework agnostic, allowing developers to use Vue.js, Angular, React, or even plain JavaScript to build their apps <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. However, [[Hybrid app development with Ionic 4 | Ionic 4]] still maintains first-class support for Angular <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Angular 6 CLI Integration
An [[Hybrid app development with Ionic 4 | Ionic 4]] application closely resembles a vanilla Angular 6 CLI application because it utilizes the Angular 6 CLI under the hood <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a> <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. The primary added value of [[Hybrid app development with Ionic 4 | Ionic]] over plain Angular is access to pre-built components and services for common UI use cases <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
It also includes extra elements for native mobile apps, such as a `config.xml` file for Cordova and a `resources` file for native builds <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. The CLI provides additional commands for building apps on native platforms, while largely functioning like the standard Angular CLI <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

### Project Structure
For users [[Hybrid app development with Ionic 4 | migrating from Ionic 3]], there are noticeable changes to the project directory structure <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. All application code is now contained within the `app` directory, following the typical Angular application pattern <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

### Angular Router for Navigation
Perhaps the most significant change in [[Hybrid app development with Ionic 4 | Ionic 4]] is the adoption of the [[Router animations in Angular | Angular router]] instead of [[Hybrid app development with Ionic 4 | Ionic's]] previous push/pop navigation system <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. This is considered a positive change due to the power of the [[Router animations in Angular | Angular router]], offering better tools for managing router state <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
Generating a new "page" component in [[Hybrid app development with Ionic 4 | Ionic]] automatically wires it up with the router for lazy loading <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Another benefit is that paths are now regular URLs, making deep linking much easier, unlike the hash location strategy used in [[Hybrid app development with Ionic 4 | Ionic 3]] <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Component Setup
While there's a list of breaking changes in component setup, most are minor and related to naming conventions, making migration relatively straightforward <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. For example, the [[Hybrid app development with Ionic 4 | Ionic]] button is now a custom element instead of a directive, retaining its built-in styling mechanisms <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
Navigating between pages using a button is simplified by using the `routerLink` directive from Angular <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. [[Hybrid app development with Ionic 4 | Ionic]] also automatically adds smooth animations between view transitions <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Plugin Changes
In the future, it will be possible to use Capacitor plugins instead of Cordova plugins <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Services (formerly Providers)
[[Hybrid app development with Ionic 4 | Ionic 4]] aligns with Angular conventions by renaming "providers" to "services" <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Aside from the naming change, they function identically to how they did previously <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.

### Asynchronous APIs
Some synchronous APIs in [[Hybrid app development with Ionic 3]] are now asynchronous in [[Hybrid app development with Ionic 4 | Ionic 4]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. For instance, rendering UI elements like an alert controller now occurs in the context of a promise, allowing for the use of `async`/`await` syntax <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a> <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

## Migration Process Tips
To migrate existing code from [[Hybrid app development with Ionic 3]], you can copy and paste it into the new `app` directory <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. VS Code plugins are available to assist with rewriting file paths in the application <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. A detailed documentation of all breaking changes is available on GitHub <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

## Why Choose Ionic 4?
[[Hybrid app development with Ionic 4 | Ionic 4]] is particularly well-suited for products building Progressive Web Apps (PWAs) <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. It makes it relatively easy to take an existing PWA codebase and deploy it to app stores without significantly increasing development costs <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
While [[Hybrid app development with Ionic 4 | Ionic 4]] can be used exclusively for building native mobile apps, non-webview frameworks like [[Comparing Flutter to React Native and Ionic | React Native]] or [[Comparing Flutter to React Native and Ionic | Flutter]] offer advantages such as the ability to run pure native code, potentially overcoming performance issues by directly interacting with native SDK code without a bridge <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a> <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. [[Comparing Flutter to React Native and Ionic | Flutter]], in particular, doesn't use a bridge at all, which can lead to better out-of-the-box performance <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

Other advantages of non-webview frameworks include:
*   **Hot Reloading**: Maintains the app's state while simultaneously updating code changes, which can accelerate the development process, especially with native emulators <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. [[Hybrid app development with Ionic 4 | Ionic]] uses live reloading, which is different <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Testing Resources**: While [[Hybrid app development with Ionic 4 | Ionic 4]] provides testing guidance based on the Angular CLI's Jasmin and Karma implementation (great for the web), frameworks like [[Comparing Flutter to React Native and Ionic | React Native]] and [[Comparing Flutter to React Native and Ionic | Flutter]] offer more resources dedicated to testing on real mobile devices <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

Drawbacks of other frameworks:
*   [[Comparing Flutter to React Native and Ionic | Flutter]] requires learning the Dart programming language, which is relatively obscure <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   [[Comparing Flutter to React Native and Ionic | React Native]] can encounter performance bottlenecks with its bridge, potentially requiring more native code than initially intended <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Ultimately, the decision to use [[Hybrid app development with Ionic 4 | Ionic 4]] depends on the specific use case and weighing the pros and cons of different mobile app development strategies <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a> <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. However, for suitable hybrid app strategies, [[Hybrid app development with Ionic 4 | Ionic 4]] is generally recommended <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.