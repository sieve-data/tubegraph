---
title: React Native vs Flutter comparison
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

When building a [[Crossplatform app development with Flutter | cross-platform mobile app]] today, two major frameworks compete for developer attention: [[Introduction to Flutter for JavaScript Developers | Flutter]] by Google and [[React Native programming languages and ecosystem | React Native]] by Facebook <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Both aim to build applications for multiple platforms, including iOS, Android, and the web, from a single codebase <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This article provides a [[Comparison of mobile app frameworks Ionic React Native and Flutter | detailed side-by-side comparison]] of their features, tooling, [[Performance and developer experience in React Native and Flutter | developer experience]], performance, and code, based on building the same chat app with both frameworks using Firebase as the backend <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Programming Languages

*   **React Native**: Apps are coded in JavaScript, with React serving as a required UI library <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It also supports TypeScript for adding a type system <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Flutter**: Uses Dart, a language optimized for compiling to multiple platforms with ahead-of-time (AOT) and just-in-time (JIT) compilation, leading to performance advantages <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Dart's syntax resembles TypeScript, making it easier for "curly brace developers" to learn <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

> [!NOTE] Language choice often comes down to whether a developer prefers to learn a new language (Dart) or stick with what they already know (JavaScript/TypeScript) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Ecosystem and Philosophy

Both [[comparing_flutter_to_react_native_and_ionic | frameworks]] are among the most actively developed GitHub repositories globally <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **React Native**:
    *   Originates from Facebook <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   Designed to be minimal, providing base components but relying heavily on the open-source community for everything else <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This often results in projects requiring many third-party dependencies <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Many React web libraries are not compatible with React Native <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Flutter**:
    *   Originates from Google <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   Comes with a vast widget library out-of-the-box, and the Flutter team maintains many common plugins (e.g., for camera access) <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
    *   Dart has its own package manager called Pub, with a large ecosystem of open-source packages <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Architecture

*   **React Native**:
    *   Operates with two separate JavaScript threads: one for the native platform app and another for business logic <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   These threads communicate via a "bridge" to pass serialized messages <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   When React Native renders a component, it's a truly native component on the corresponding platform, ensuring the UI looks exactly as intended by native components <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Flutter**:
    *   Uses its own high-performance rendering engine built with C++ and Skia <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
    *   This engine renders its own custom pixels to the screen using compiled native code <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   It can render pixel-perfect versions of iOS and Android widgets and allows for custom pixel drawing, similar to a gaming engine <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   This approach eliminates the need for a bridge, though it has "platform channels" for communication with the native system when native features or code integration are needed <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

## Developer Experience

### Initial Setup

*   **React Native**:
    *   A new app can be generated using `npx react-native init` <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
    *   Templates like `native-base` can provide a pre-styled UI <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
    *   Alternatively, Expo CLI can be used for a more complete starting point <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   Projects often have many config files (Metro, Watchman, Buck, Babel) and include Flow by default <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   App source code is typically in `App.js`, using React code with special components imported from React Native <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Flutter**:
    *   After installing the SDK, `flutter create` generates a new project significantly faster as it doesn't rely on npm <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.
    *   The project structure is simpler, with `pubspec.yaml` serving as the main config file (similar to `package.json`) for managing third-party packages <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   The app source code is in `main.dart` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
    *   Code might seem complex to web developers unfamiliar with `extends`, `super`, or `override`, but feels familiar to those with TypeScript, Java, or C# backgrounds <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Tooling

*   **React Native**:
    *   Requires running `npm start` (Metro) for watching code changes and `npm run android` (or `ios`) in a separate terminal to build and install the app on an emulator <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   Supports hot reloading by typing `r` in the Watchman terminal, preserving app state while reflecting code changes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   Tooling is a "create your own adventure" with options like TypeScript, Ignite CLI for boilerplate, or Expo for quick device launches <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This flexibility can lead to decision fatigue and reliance on third parties <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Flutter**:
    *   Provides integrated tooling within VS Code, allowing direct selection of an emulator <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
    *   `flutter run` starts the app, and hot reloading is supported by typing `r` due to Dart's JIT compilation <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Dart's sound type system provides excellent tooling, like full documentation on hover and immediate error detection for wrong data types, preventing runtime errors <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   Dart also includes features like null safety for more reliable code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### UI Development

*   Both frameworks create a tree of components or widgets <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **React Native**:
    *   UI resembles HTML or JSX, where components are nested within tags (e.g., `<View>`) <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   React Native automatically re-renders the UI when a component's state changes <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
    *   The challenge can be the lack of a specific component for every desired feature, often requiring starting with a base component and modifying it, or installing third-party packages <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Flutter**:
    *   Inspired by React, it uses classes with a `build` method that returns a tree of widgets <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Each widget is a class instance with properties that can take other widgets as arguments <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   Refactoring by hand can be more difficult due to deep nesting <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
    *   However, Flutter's tooling is excellent for wrapping and repositioning widgets with simple button clicks in VS Code <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

## Performance

For most benchmarks, Flutter is generally faster than React Native <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

*   **Flutter**:
    *   Aims for 60 frames per second (FPS) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
    *   Apps are compiled directly to machine code and do not require a JavaScript bridge, leading to better performance <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    *   Gets much closer to native performance <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **React Native**:
    *   Might encounter performance bottlenecks sooner due to the JavaScript bridge <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

> [!CAUTION] For the majority of apps, performance differences between the two frameworks will be indistinguishable to the end-user <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. If performance is a critical concern, true native development remains the best option <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.