---
title: Performance and developer experience in React Native and Flutter
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

When building a [[crossplatform_app_development_with_flutter | cross-platform mobile app]] today, [[React Native vs Flutter comparison | Flutter]] (from Google) and [[React Native vs Flutter comparison | React Native]] (from Facebook) are two leading frameworks that can achieve the fundamental goal of building apps for multiple platforms like iOS, Android, and the web from a single codebase <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article provides a [[React Native vs Flutter comparison | detailed side-by-side comparison]] of their features, tooling, developer experience, and performance <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Developer Experience

### Programming Languages

*   **[[React Native programming languages and ecosystem | React Native]]**: Apps are coded in JavaScript, with React serving as a required UI library <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It also supports TypeScript for adding a type system <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: Implemented with [[introduction_to_flutter_for_javascript_developers | Dart]], a language optimized for compiling to multiple platforms with ahead-of-time (AOT) and just-in-time (JIT) compilation <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. [[introduction_to_flutter_for_javascript_developers | Dart]]'s syntax somewhat resembles TypeScript <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The choice between learning a new language ([[introduction_to_flutter_for_javascript_developers | Dart]]) or sticking with JavaScript/TypeScript is a major consideration <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Ecosystem and Philosophy

Both frameworks have highly active GitHub repositories and are backed by major tech corporations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **[[React Native programming languages and ecosystem | React Native]]**: Designed to be minimal, providing base components but relying heavily on the open-source community for everything else <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This often means a project requires many third-party dependencies <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **[[building_mobile_app_components_with_flutter | Flutter]]**: Comes with a large widget library out-of-the-box, and the [[building_mobile_app_components_with_flutter | Flutter]] team maintains many common plugins, such as those for camera access <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. [[introduction_to_flutter_for_javascript_developers | Dart]] also has its own package manager, Pub, with a large open-source ecosystem <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Both have large communities supporting them <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Initial Setup

*   **[[React Native programming languages and ecosystem | React Native]]**:
    *   Start by running `npx react-native init` from the command line, optionally passing a template like `nativebase` <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   Expo can be used instead of the default CLI for a more complete starting point <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   Projects include various config files (Metro, Watchman, Buck, Babel) and ship with Flow by default <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   The app source code is typically in `App.js`, using React components and special components imported from [[React Native programming languages and ecosystem | React Native]] <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

*   **[[building_mobile_app_components_with_flutter | Flutter]]**:
    *   After installing the [[building_mobile_app_components_with_flutter | Flutter]] SDK, run `flutter create` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This process is faster due to less reliance on external package downloads <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   The `pubspec.yaml` file acts as the main config, similar to `package.json` <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
    *   The app source code is in `main.dart` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The code, with keywords like `extends`, `super`, and `override`, feels familiar to developers with a background in TypeScript, Java, or C# <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Tooling and Development Workflow

Good tooling is crucial for [[crossplatform_app_development_with_flutter | cross-platform mobile app development]] <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

*   **[[React Native programming languages and ecosystem | React Native]]**:
    *   To serve locally, an Android emulator is started, then `adb` connects to it <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   `npm start` runs Metro to watch for code changes, and `npm run android` builds and installs the app <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   Hot reloading is available by typing 'r' into the Watchman terminal, preserving application state while reflecting code changes <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   Tooling is more "create your own adventure," with options like TypeScript, Ignite CLI for boilerplate, or Expo for quick device launching <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This flexibility can lead to decision fatigue and reliance on third parties <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

*   **[[building_mobile_app_components_with_flutter | Flutter]]**:
    *   VS Code offers a button to select a configured emulator <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
    *   `flutter run` starts the app, and hot reloading is supported because [[introduction_to_flutter_for_javascript_developers | Dart]] includes JIT compilation <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
    *   [[introduction_to_flutter_for_javascript_developers | Dart]]'s sound type system provides excellent tooling, offering full documentation on hover and catching type errors early at compile-time instead of runtime <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This is critical for mobile apps where runtime errors impact app store reviews <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. [[introduction_to_flutter_for_javascript_developers | Dart]] also features null safety for more reliable code <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### UI Declarative Approach

Both frameworks build a tree of components or widgets and automatically re-render the UI when state changes <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>.

*   **[[React Native programming languages and ecosystem | React Native]]**: Uses HTML-like JSX where components are nested tags (e.g., `<View>`), with functions managing component state <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Refactoring is often easier, as you can simply create new functions for UI components <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. However, many React libraries are not compatible with [[React Native programming languages and ecosystem | React Native]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, and often a base component needs to be extended or a third-party package installed <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **[[building_mobile_app_components_with_flutter | Flutter]]**: Inspired by React, it uses classes with a `build` method that returns a tree of widgets <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Each widget is a class instance with properties that can take other widgets as arguments <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. While this is a different approach to declarative UIs <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>, refactoring can be more difficult by hand <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. However, [[building_mobile_app_components_with_flutter | Flutter]]'s tooling allows wrapping and repositioning widgets with a single click in VS Code <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. A potential drawback is the tendency to create deeply nested widget trees that are hard to follow <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## Performance

### Underlying Architectures

*   **[[React Native programming languages and ecosystem | React Native]]**: Runs two separate JavaScript threads: one for the app on the native platform and another for business logic <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. These threads communicate via a "bridge" by passing serialized messages <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. When [[React Native programming languages and ecosystem | React Native]] renders a component, it's a truly native component on the corresponding platform, ensuring the UI looks exactly as intended <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

*   **[[building_mobile_app_components_with_flutter | Flutter]]**: Instead of native UI components, [[building_mobile_app_components_with_flutter | Flutter]] uses its own high-performance rendering engine built with C++ and Skia <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This engine renders custom pixels to the screen with compiled native code, allowing for pixel-perfect iOS and Android widgets and custom pixel painting, similar to a gaming engine like Unity <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This approach enables smooth graphics without needing a bridge, though it does have "platform channels" for native system communication <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

### Benchmarks and Speed

*   **[[building_mobile_app_components_with_flutter | Flutter]]** is generally faster than [[React Native programming languages and ecosystem | React Native]] <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The goal is to render at 60 frames per second <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   Because [[building_mobile_app_components_with_flutter | Flutter]] apps compile directly to machine code and don't require a JavaScript bridge, they tend to perform better based on most benchmarks, getting much closer to native performance <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   However, for the majority of apps, performance differences may be indistinguishable to the end-user <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. While [[React Native programming languages and ecosystem | React Native]] might encounter performance bottlenecks sooner <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, for critical performance, true native development remains the best option <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.