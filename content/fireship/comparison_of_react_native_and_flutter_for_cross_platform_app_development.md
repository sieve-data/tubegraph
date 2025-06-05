---
title: Comparison of React Native and Flutter for cross platform app development
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

For developers building cross-platform mobile applications today, [[applications_of_react_including_react_native | React Native]] (from Facebook) and Flutter (from Google) are two leading options <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Both aim to build applications for multiple platforms like iOS, Android, and the web from a single codebase <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. While they achieve the same fundamental goal, there are significant differences in their internal workings and [[developer_experience_and_tooling_in_react_native_and_flutter | developer experience]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

The following comparison dives into their features, tooling, [[developer_experience_and_tooling_in_react_native_and_flutter | developer experience]], [[performance_differences_between_react_native_and_flutter | performance]], and code <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Programming Languages

A key difference lies in the [[programming_languages_and_syntax_used_in_react_native_and_flutter | programming languages]] used:

*   **[[applications_of_react_including_react_native | React Native]]**: Apps are coded in JavaScript, with React being a required UI library <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. It also supports TypeScript for adding a type system <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Flutter**: Uses Dart, a language optimized for compiling to multiple platforms with ahead-of-time and just-in-time compilation <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. While Dart offers [[performance_differences_between_react_native_and_flutter | performance advantages]], it's not widely known outside of Flutter <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. Its syntax resembles TypeScript, making it easier for "curly brace developers" to pick up <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

The choice of language presents a fundamental question: learn a new language (Dart) or stick with familiar JavaScript <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

## Ecosystem and Development Philosophy

Both frameworks are among the most actively developed GitHub repositories <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **[[applications_of_react_including_react_native | React Native]]**:
    *   **Sponsor**: Facebook <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
    *   **Philosophy**: Minimalist design, similar to [[features_and_trade_offs_of_react_angular_and_vue | React for the web]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. It provides base components but relies heavily on the open-source community for everything else, often requiring many third-party dependencies for a complete project <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Flutter**:
    *   **Sponsor**: Google <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
    *   **Philosophy**: Comes with a large widget library out-of-the-box <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The Flutter team maintains many common plugins, such as those for accessing a device's native camera <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Dart also has its own package manager, `pub`, with a large ecosystem of open-source packages <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Both [[ecosystem_and_development_philosophy_of_react_native_and_flutter | ecosystems]] boast large communities capable of achieving virtually any development need <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

## Underlying Architectures

The architectures of React Native and Flutter differ significantly in how they render UI components:

*   **[[applications_of_react_including_react_native | React Native]]**:
    *   Runs on two separate JavaScript threads: one for the native platform and one for application business logic <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   These threads communicate via a "bridge" that passes serialized messages <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
    *   When React Native renders a component, it's a truly *native* component on the corresponding platform, not just a bundled React website <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This ensures the UI looks exactly like native components <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
*   **Flutter**:
    *   Uses its own high-performance rendering engine built with C++ and Skia <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
    *   It renders its own custom pixels to the screen using compiled native code <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
    *   This allows it to create pixel-perfect versions of iOS and Android widgets, and also paint custom pixels, similar to a gaming engine <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
    *   It renders smoothly without the need for a "bridge" for UI <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
    *   It uses "platform channels" to communicate with the native system for features or integrating native code <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

Ultimately, the architecture matters less than creating a good user experience and enjoying the development process <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Developer Experience and Tooling

### Initial Setup

*   **[[applications_of_react_including_react_native | React Native]]**:
    *   Generate a new app with `npx react-native init` (optionally with templates like NativeBase for UI) <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
    *   [[developer_experience_and_tooling_in_react_native_and_flutter | Expo CLI]] can provide a more complete starting point <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   Projects often have many config files (Metro, Watchman for hot reloading, Buck for building, Babel for transpiling JavaScript, Flow for type checking) <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.
    *   Source code is typically in `App.js`, looking like [[features_and_trade_offs_of_react_angular_and_vue | React]] code with special components imported from React Native <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Flutter**:
    *   After installing the SDK, run `flutter create` <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This is considerably faster as it doesn't rely on `npm` <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
    *   Requires the Flutter extension in VS Code, which manages packages automatically <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
    *   Simplified project structure; `pubspec.yaml` is the main config file (similar to `package.json`) <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   Source code is in `main.dart` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. The code, with keywords like `extends`, `super`, and `override`, is familiar to developers with a background in TypeScript, Java, or C# <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

### Development Loop and Tooling

*   **[[applications_of_react_including_react_native | React Native]]**:
    *   Requires running an Android emulator and connecting via `adb` <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
    *   `npm start` runs Metro to watch for code changes, and `npm run android` builds the app <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
    *   Supports hot reloading by typing 'r' in the Watchman terminal, preserving application state while updating code <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
    *   Tooling is more "create your own adventure," allowing developers to integrate TypeScript, Ignite CLI for boilerplate, or Expo for quick device testing <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. This flexibility can lead to decision fatigue and reliance on third parties <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Flutter**:
    *   Offers a VS Code button to select and launch an emulator <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
    *   `flutter run` in the terminal starts the app, and hot reloading is supported by typing 'r' <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Dart's sound type system provides excellent tooling, showing full documentation on hover and catching type errors immediately during development, rather than at runtime <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This is crucial for mobile apps where app store reviews depend on stability <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. Dart also includes features like null safety for more reliable code <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### UI Composition

Both frameworks build a tree of components or widgets:

*   **[[applications_of_react_including_react_native | React Native]]**:
    *   Uses JSX (like HTML) where components like `View` are nested <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   Components have state, and React Native automatically re-renders the UI when state changes <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   Building declarative UIs with function-based components feels intuitive, making refactoring easier (e.g., copying and pasting components) <a class="yt-timestamp" data-t="08:08:21">[08:08:21]</a>.
    *   A drawback is the frequent lack of a specific component, often requiring developers to build from a base component or install third-party packages <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>. Many [[popularity_and_impact_of_reactjs_in_web_development | React]] web libraries are not compatible with [[applications_of_react_including_react_native | React Native]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Flutter**:
    *   Inspired by [[features_and_trade_offs_of_react_angular_and_vue | React]], it works similarly <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Instead of functions, it uses classes with a `build` method that returns a tree of widgets <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. Each widget is a class instance with properties that can take other widgets as arguments <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
    *   While doing the same basic job as [[features_and_trade_offs_of_react_angular_and_vue | React]], it can make manual refactoring more difficult <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   Flutter's tooling provides features to wrap and reposition widgets by clicking a button in VS Code, mitigating some refactoring challenges <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   A common drawback is deeply nested widget trees that can be hard to follow, although logic can be extracted into custom widgets <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Performance

The question of [[performance_differences_between_react_native_and_flutter | performance]] is often raised: is Flutter faster than [[applications_of_react_including_react_native | React Native]]?

*   **General Assessment**: Most benchmarks suggest Flutter is likely faster <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Target**: The goal for mobile app performance is generally 60 frames per second (FPS) <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Reasons for Flutter's Advantage**: Flutter apps are compiled directly to machine code and do not require a JavaScript bridge, leading to better [[performance_differences_between_react_native_and_flutter | performance]] <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Benchmarks indicate Flutter achieves performance much closer to native applications <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   **Practical Relevance**: For the majority of apps, [[performance_differences_between_react_native_and_flutter | performance differences]] will be indistinguishable to the end-user <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. However, [[applications_of_react_including_react_native | React Native]] might encounter [[performance_differences_between_react_native_and_flutter | performance bottlenecks]] sooner <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. If performance is paramount, building a true native app remains the best option <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

Ultimately, the choice between [[applications_of_react_including_react_native | React Native]] and Flutter often comes down to the developer's existing skill set, project requirements, and philosophical preference for either a more minimalist, community-driven approach (React Native) or a more batteries-included, opinionated framework (Flutter).