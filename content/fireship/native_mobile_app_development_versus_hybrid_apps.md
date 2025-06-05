---
title: Native mobile app development versus hybrid apps
videoId: 34fDUKaJBtw
---

From: [[fireship]] <br/> 
This article discusses different approaches to mobile application development, focusing on the trade-offs between native SDK development and [[hybrid_app_development_with_ionic_4 | hybrid apps]].

### Choosing a Mobile App Development Approach <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>

When deciding on a strategy for building a mobile application, it's crucial to understand your technical demands and weigh the pros and cons of various approaches <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. In 2018, there are three primary methods for building mobile apps <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

#### 1. Native SDK Development <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>

This approach involves writing a separate application for each platform you intend to target, using its native language <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. For Android, this means Kotlin or Java, for iOS, Swift or Objective C, and for the web, JavaScript <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

**Advantages:**
*   **Performance and Quality:** Generally speaking, apps built with native SDKs offer the highest quality and best performance <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

**Disadvantages:**
*   **Cost:** A significant drawback is the cost <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. More code to maintain directly translates to higher operating costs <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Talent Acquisition:** It can be challenging to hire the right talent to maintain these distinct codebases, particularly for iOS and Android <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

#### 2. [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | Hybrid Mobile App Development]] <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>

This strategy, exemplified by Ionic 4, involves building a mobile app using web technologies <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The core idea is to write code once and run it seamlessly across multiple platforms <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. A [[hybrid_app_development_with_ionic_4 | hybrid app]] is essentially a web app embedded onto the native device via a webview <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. To interact with native device features, [[hybrid_app_development_with_ionic_4 | hybrid apps]] use a bridge, such as Apache Cordova or Capacitor, which wraps native code in a JavaScript API <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

**Advantages:**
*   **Cost-Effectiveness:** Enables the use of web developers to build [[crossplatform_mobile_app_development | cross-platform]] mobile apps at a reduced cost <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **User Experience:** If executed well, a [[hybrid_app_development_with_ionic_4 | hybrid app]] can be indistinguishable from a truly native app <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **PWA Synergy:** [[hybrid_app_development_with_ionic_4 | Hybrid apps]] excel when a Progressive Web App (PWA) is the primary product, as Ionic makes it relatively easy to deploy the existing codebase to app stores without tripling development costs <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Ionic 4 is optimized for products building Progressive Web Apps <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

**Disadvantages:**
*   **Debugging and Performance:** Decoupling from native SDKs can make debugging and performance optimization more challenging <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   **Native Feature Access:** [[hybrid_app_development_with_ionic_4 | Hybrid apps]] cannot communicate with many native device features directly, requiring a bridge <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

#### 3. Frameworks like [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]] and [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Flutter]] <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>

This category includes frameworks such as [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]], [[crossplatform_app_development_with_flutter | Flutter]], or NativeScript <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The key distinction from Ionic is that these frameworks do not use a webview for the user interface <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

**Advantages over [[capabilities_and_limitations_of_hybrid_apps_with_ionic_and_cordova | Hybrid Apps]] (Non-Webview Frameworks):**
*   **Native Code Execution:** These frameworks allow running purely native code, which can overcome certain performance issues by interacting directly with native SDK code, rather than relying on a bridge <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. [[crossplatform_app_development_with_flutter | Flutter]], for instance, does not use a bridge at all, leading to better out-of-the-box performance <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
*   **Hot Reloading:** Unlike Ionic's live reloading, frameworks like [[comparing_flutter_to_react_native_and_ionic | React Native]] and [[crossplatform_app_development_with_flutter | Flutter]] offer hot reloading <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This feature maintains the app's state while simultaneously updating code changes, significantly accelerating the development process, especially when working with native emulators <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Testing Resources:** There are more resources dedicated to testing on real mobile devices with [[comparing_flutter_to_react_native_and_ionic | React Native]] and [[crossplatform_app_development_with_flutter | Flutter]] compared to Ionic <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Ionic 4 does have testing guidance based on Angular CLI's implementation with Jasmine and Karma, which is suitable for the web <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

**Disadvantages:**
*   **Learning Curve:** [[crossplatform_app_development_with_flutter | Flutter]] requires learning the Dart programming language, which is relatively obscure <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Performance Bottlenecks:** [[react_native_vs_flutter_comparison | React Native]] can still encounter performance bottlenecks with its bridge, potentially leading to the need for more native code than initially intended <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Conclusion <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>

The decision of whether to use a particular framework or development strategy, such as Ionic 4, ultimately depends on your specific use case and business needs <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. You must assess your situation and weigh the pros and cons of the various options available <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. If a [[hybrid_app_development_with_ionic_4 | hybrid app]] strategy aligns with your use case, then Ionic 4 is a recommended choice <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.