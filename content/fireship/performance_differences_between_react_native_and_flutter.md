---
title: Performance differences between React Native and Flutter
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

When building cross-platform mobile applications, [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] and [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | React Native]] are two prominent frameworks, with performance being a key area of [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | comparison]] <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. The general goal for mobile app performance is to render at 60 frames per second (FPS) <a class="yt-timestamp" data-t="09:21:00">[09:21:00]</a>.

## How Performance Differs

### React Native Architecture and Performance
[[applications_of_react_including_react_native | React Native]] operates by running two separate JavaScript threads: one for the main application on the native platform and another for the business logic <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. These threads are isolated but communicate via a "bridge" that passes serialized messages back and forth <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. When [[applications_of_react_including_react_native | React Native]] renders a component, it is a truly native component on the corresponding platform <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

Despite rendering native components, this architecture, especially the JavaScript bridge, can sometimes lead to performance bottlenecks <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.

### Flutter Architecture and Performance
In contrast, [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] does not use native UI components directly. Instead, it features its own high-performance rendering engine, built with C++ and Skia, which renders custom pixels directly to the screen using compiled native code <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. This approach allows [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] to render pixel-perfect versions of iOS and Android widgets, or custom pixels, without the need for a bridge <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>.

The [[programming_languages_and_syntax_used_in_react_native_and_flutter | Dart language]], which [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] uses, is optimized for compiling to multiple platforms with ahead-of-time (AOT) and just-in-time (JIT) compilation, leading to various performance advantages <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Comparative Outcomes
Based on most benchmarks available, [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] is generally considered faster than [[applications_of_react_including_react_native | React Native]] <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>. Because [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] applications compile directly to machine code and eliminate the JavaScript bridge, they tend to perform better and achieve a performance level closer to that of true native applications <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

## Practical Considerations
While [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] typically offers better performance, it's important to consider whether this difference is critical for a given application <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>. For the majority of applications, the performance differences between [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | Flutter]] and [[applications_of_react_including_react_native | React Native]] will be indistinguishable to the end user <a class="yt-timestamp" data-t="09:46:00">[09:46:00]</a>. If peak performance is an absolute necessity, the best option remains building a true native application <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.