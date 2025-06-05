---
title: Developer experience and tooling in React Native and Flutter
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

When building cross-platform mobile applications, [[developer_productivity_tools | tooling]] and the overall developer experience are crucial factors. Both [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | React Native]] and Flutter offer distinct approaches in these areas <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Initial Setup and Project Structure

### React Native
To get started with [[applications_of_react_including_react_native | React Native]], you can generate a new app using `npx react-native init` from the command line <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. An optional template, like `native-base`, can be passed for a pre-configured UI <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. Alternatively, Expo can be used instead of the default [[applications_of_react_including_react_native | React Native]] CLI for a more complete starting point <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

The root directory of a [[applications_of_react_including_react_native | React Native]] project contains several configuration files, including `metro` and `watchman` for hot reloading, `buck` as a build tool, and `babel` for JavaScript transpilation <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Flow is also shipped by default <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. The core application source code is typically found in `App.js` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This file contains [[applications_of_react_including_react_native | React]] code familiar to web developers, with special components imported from [[applications_of_react_including_react_native | React Native]] used in JSX instead of standard HTML elements <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

### Flutter
For Flutter, after installing the SDK, `flutter create` can be run from the command line <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. This process is notably faster as it doesn't require downloading numerous packages via npm <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

When opening a Flutter project in VS Code, it's recommended to have the Flutter extension installed, which manages additional packages automatically <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The project structure is more simplified, with `pubspec.yaml` serving as the main configuration file, similar to `package.json` in [[applications_of_react_including_react_native | React Native]], where third-party packages are registered and installed <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The application's source code is located in `main.dart` <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Developers with backgrounds in TypeScript, Java, or C# will likely find Dart's syntax (with keywords like `extends`, `super`, and `override`) familiar <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

## Development Workflow and [[developer_productivity_tools | Tooling]]

### React Native
To serve a [[applications_of_react_including_react_native | React Native]] app locally on an Android emulator, an `adb` command is needed to connect to it <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Then, `npm start` runs Metro to monitor code changes, and `npm run android` in a separate terminal builds and installs the app on the emulator <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. [[developer_productivity_tools | React Native]] supports hot reloading by typing 'r' into the Watchman terminal, which preserves application state while reflecting code changes <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

[[developer_productivity_tools | Tooling]] with [[applications_of_react_including_react_native | React Native]] is described as a "create your own adventure story" <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Being a JavaScript project, it allows for flexibility with options like adding TypeScript, using the Ignite CLI for boilerplate generation, or Expo for quick deployment to a device <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. While offering many options, this can also lead to decision fatigue and a reliance on third-party solutions <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Flutter
Flutter provides a button in VS Code to select a configured emulator <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Running `flutter run` in the terminal starts the application <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Flutter also supports hot reloading by typing 'r' due to Dart's just-in-time compilation <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

Dart's sound type system enables robust [[developer_productivity_tools | tooling]], providing full documentation on hover for classes and immediate feedback on incorrect data types, preventing runtime errors <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This is particularly important for mobile apps where app store reviews depend on stability <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. While TypeScript can be added to [[applications_of_react_including_react_native | React Native]] for similar benefits, Dart's null safety further enhances code reliability <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## UI Component Development and Refactoring

Both frameworks utilize a tree of components (or widgets) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   In [[applications_of_react_including_react_native | React Native]], this resembles HTML or JSX, where components like `View` are nested <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. [[applications_of_react_including_react_native | React Native]] automatically re-renders the UI when a component's state changes <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Flutter operates similarly, inspired by [[applications_of_react_including_react_native | React]], but uses classes with a `build` method that returns a tree of widgets <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Widgets are class instances with properties that can accept other widgets as arguments <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

While Flutter's approach leads to deeply nested widget trees that can be challenging to follow, its robust [[developer_productivity_tools | tooling]] in VS Code allows for easy wrapping and repositioning of widgets with a click <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This mitigates the manual refactoring difficulties when coding by hand <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. In contrast, [[applications_of_react_including_react_native | React]] allows for simpler component extraction by creating new functions for UI components <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

One challenge with [[applications_of_react_including_react_native | React Native]] is the frequent absence of a pre-built component for a specific need, often requiring developers to start with a base component and customize it or install a third-party package <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Additionally, many [[react_ecosystem_and_libraries | React libraries]] are not compatible with [[applications_of_react_including_react_native | React Native]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.