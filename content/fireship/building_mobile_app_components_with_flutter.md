---
title: Building Mobile App Components with Flutter
videoId: 7sJZi0grFR4
---

From: [[fireship]] <br/> 

Flutter has significantly impressed JavaScript developers with its developer experience and the quality of mobile applications it can produce <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This framework offers a compelling alternative for those looking to build native mobile apps, especially when compared to options like [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] or [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Project Structure and Workflow

A Flutter project is notably less complex than its JavaScript counterparts <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. The application's entry point is typically a single file called `main.dart` <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. For instance, a three-tab layout can be achieved with only 45 lines of code, free from import/export headaches or boilerplate <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

During development, Flutter supports hot reloads; entering 'R' on the command line will hot reload the code while preserving the app's state, significantly boosting development productivity <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Dependencies are managed via `pubspec.yaml`, which functions similarly to a `package.json` file <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Dart Programming Language for Components

To learn Flutter, developers must learn Dart, its programming language <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Luckily, Dart shares many conventions with JavaScript <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Key Dart Concepts Relevant to Components:

*   **Entry Point:** The main entry point for a Dart app is the `main` function <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Variable Declaration:**
    *   Reassignable variables use type annotations (e.g., `String myVar`) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   Single-assignment variables (constants) use the `final` keyword, similar to JavaScript's `const` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
    *   The `const` keyword in Dart makes entire data structures immutable, similar to `Object.freeze` in JavaScript <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
    *   The `var` keyword allows Dart to implicitly infer the type <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   The `dynamic` type is similar to TypeScript's `any` type, useful for external data sources with unknown shapes <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Importing:** Dart doesn't require explicit exports; variables declared in one file are available for import in another <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Functions:** Functions in Dart are similar to JavaScript, supporting type annotations before the name, anonymous functions, and higher-order functions <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Object-Oriented Programming:**
    *   Dart supports mixin-based inheritance <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
    *   Classes are defined using the `class` keyword <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   Class instantiation doesn't require the `new` keyword, leading to cleaner code when creating many objects (common in Flutter) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   Constructors initialize objects <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Dart allows for a cleaner way to construct objects by just calling the class as a function <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
    *   Dart supports named constructors for different initialization logic <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Asynchronous Programming:** Dart uses "futures" instead of promises, which work similarly, supporting `async`/`await`, `.then()`, and `.catchError()` <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Streams:** Dart has a `Stream` data structure for handling multiple asynchronous values, similar to RxJS observables <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Streams can be iterated with an `await for` loop for more readable code <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a> or subscribed to using `.listen()` <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

## [[building_user_interfaces_with_flutter_widgets | Building User Interfaces with Flutter Widgets]]

Flutter takes significant inspiration from React for UI development <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Stateless Widgets

When [[building_user_interfaces_with_flutter_widgets | building components]] in Flutter, the structure is very similar to React Native. Instead of a `render` function, Flutter uses a `build` method. Inside this method, UI elements are created by instantiating objects, which look like function calls due to the omitted `new` keyword <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>. Styling in Flutter involves passing style properties directly to these widget objects <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

### Stateful Widgets and State Management

The core value of frameworks like Flutter lies in their ability to react to data changes <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

*   **`setState`:** Similar to React Native's `setState` method, Flutter's stateful widgets also have a `setState` method that triggers a re-render when called with state changes <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Builders:** For more complex [[managing_state_in_flutter_applications | state management]] and working with asynchronous data sources, Flutter offers "builders" <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. These allow the UI to listen to a stream and automatically re-render different templates or widgets based on the stream's value <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This concept is similar to Angular's async pipe <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.