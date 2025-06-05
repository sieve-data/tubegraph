---
title: Programming languages and syntax used in React Native and Flutter
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

When building [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | cross-platform mobile apps]] today, developers choose between React Native and Flutter, both of which allow building applications for multiple platforms like iOS, Android, and the web from a single codebase <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. A key distinction between these frameworks lies in their chosen programming languages and the resulting syntax.

## React Native

React Native utilizes [[popular_programming_languages_for_web_development | JavaScript]] as its primary programming language <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. [[applications_of_react_including_react_native | React]], a required UI library, effectively extends the [[popular_programming_languages_for_web_development | JavaScript]] language within the framework <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Developers also have the option to use TypeScript to add a type system on top of [[popular_programming_languages_for_web_development | JavaScript]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

While [[popular_programming_languages_for_web_development | JavaScript]] was not originally designed for mobile app development <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, React Native's syntax is often familiar to web developers <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The code consists of [[building_components_with_react | React]] code, importing special components from React Native for use in JSX (a syntax extension for [[popular_programming_languages_for_web_development | JavaScript]]), replacing typical HTML elements <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

React Native constructs a tree of components, resembling HTML or JSX, where tags like `View` can contain other components, which in turn might contain more components <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. These components can possess state that changes throughout the app's lifecycle, and React Native automatically re-renders the UI when the state is updated <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

From a development perspective, refactoring is often considered easier in React Native, as developers can simply copy and paste components or create new functions for UI components <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. However, a potential drawback is that there may not always be a component that perfectly matches a desired functionality, requiring developers to either customize a base component or install a third-party package <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. Additionally, many [[react_ecosystem_and_libraries | React libraries]] designed for the web are not compatible with React Native <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Flutter

Flutter employs Dart, a language optimized for compiling to multiple platforms with both ahead-of-time (AOT) and just-in-time (JIT) compilation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. While Dart is less known outside of the Flutter ecosystem <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, its syntax resembles TypeScript, making it easier for developers familiar with curly-brace languages like TypeScript, Java, or C# to get started <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

The app's source code is typically found in the `main.dart` file <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. If a web developer has never used TypeScript, the code might initially appear complex with keywords such as `extends`, `super`, and `override` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Like React Native, Flutter also creates a tree of widgets <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>. It operates similarly to React, using classes with a `build` method that returns a tree of widgets <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Each widget is an instance of a class and can have properties that take other widgets as arguments <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. This represents a different approach to building declarative UIs <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

One observed drawback of Flutter is the potential for deeply nested widget trees, which can be challenging to follow. While logic can be extracted into custom widgets, the process might not feel as intuitive as in React <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. However, Flutter's [[developer_experience_and_tooling_in_react_native_and_flutter | tooling]] helps mitigate this, allowing developers to wrap and reposition widgets by simply clicking a button in VS Code <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Dart's sound type system also provides robust [[developer_experience_and_tooling_in_react_native_and_flutter | tooling]], catching potential runtime errors during code writing, which is crucial for mobile apps <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Dart also includes features like null safety to enhance code reliability <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.