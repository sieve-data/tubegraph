---
title: Introduction to Flutter for JavaScript Developers
videoId: 7sJZi0grFR4
---

From: [[fireship]] <br/> 

[[crossplatform_app_development_with_flutter | Flutter]] has impressed [[dart_vs_javascript_programming_languages | JavaScript]] developers with its [[performance_and_developer_experience_in_react_native_and_flutter | developer experience]] and the quality of apps it produces, making it an attractive option for native mobile app development beyond existing [[dart_vs_javascript_programming_languages | JavaScript]] tools like [[comparing_flutter_to_react_native_and_ionic | Ionic]], Cordova, or [[react_native_vs_flutter_comparison | React Native]] <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

## Trade-offs and Benefits of [[crossplatform_app_development_with_flutter | Flutter]]

While [[crossplatform_app_development_with_flutter | Flutter]] offers compelling advantages, there are some initial considerations for [[dart_vs_javascript_programming_languages | JavaScript]] developers <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.

### Potential Drawbacks
*   **Learning Curve** There is a learning curve for [[crossplatform_app_development_with_flutter | Flutter]], unlike [[comparing_flutter_to_react_native_and_ionic | Ionic]] or [[react_native_vs_flutter_comparison | React Native]] where a web or [[dart_vs_javascript_programming_languages | JavaScript]] developer can often jump right in <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. However, this learning curve is considered "pretty gentle" <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   **Community Size** The [[crossplatform_app_development_with_flutter | Flutter]] community is smaller compared to the large and constantly growing pool of [[dart_vs_javascript_programming_languages | JavaScript]] developers <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. Sourcing talent for projects might be easier with [[dart_vs_javascript_programming_languages | JavaScript]]-based hybrid frameworks <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

### Advantages
*   **[[performance_and_developer_experience_in_react_native_and_flutter | Performance]]** [[dart_vs_javascript_programming_languages | Dart]], the language [[crossplatform_app_development_with_flutter | Flutter]] uses, is an ahead-of-time compiled language, which contributes to its [[performance_and_developer_experience_in_react_native_and_flutter | performance]] <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Its engine is written in C++ and can perform better than [[dart_vs_javascript_programming_languages | JavaScript]] bridges, especially when making frequent callbacks to the native system <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.
*   **Native Code Integration** [[crossplatform_app_development_with_flutter | Flutter]] can integrate existing native code <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.
*   **Hot Reloads** During development, [[crossplatform_app_development_with_flutter | Flutter]] supports hot reloads, which significantly boosts development productivity by saving the app's state while changes are applied <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. [[react_native_vs_flutter_comparison | React Native]] also offers this feature <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.
*   **Excellent Documentation** [[crossplatform_app_development_with_flutter | Flutter]] is noted for having some of the best documentation among frameworks <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.

## Project Structure: [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Flutter]] vs. [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]] and [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]]

To illustrate the differences, a baseline app with three tabs and three screens is used for comparison <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

### [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]] Project Structure
*   [[building_mobile_app_components_with_flutter | Components]] combine styles, templating, and [[dart_vs_javascript_programming_languages | JavaScript]] logic in a single file per component <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.
*   Dependencies are managed via NPM <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   A simple three-tab layout might require around ten different [[dart_vs_javascript_programming_languages | JavaScript]] files <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>.
*   The structure closely resembles a regular [[comparing_flutter_to_react_native_and_ionic | React]] app with specific components for native UI rendering and platform checks <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

### [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] (Angular) Project Structure
*   [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] projects tend to have more files because Angular separates templates and CSS into their own isolated files <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.
*   While separating concerns is good, it can be overwhelming for newcomers, especially those unfamiliar with Angular <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
*   [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] 4 uses web components, allowing it to be used with any framework <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

### [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Flutter]] Project Structure
*   [[crossplatform_app_development_with_flutter | Flutter]] projects are generally less complex than their [[dart_vs_javascript_programming_languages | JavaScript]] counterparts <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
*   A single `main.dart` file serves as the app's entry point <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   A three-tab layout can be achieved with as few as 45 lines of code, with no import/export or boilerplate issues <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
*   Apps can be run directly from the command line, without needing a special app from an app store or debugging in a browser <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   Changes can be hot reloaded by entering 'R' on the command line, preserving the app's state <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>.
*   Dependencies are managed in `pubspec.yaml`, which is similar to `package.json` <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. It starts with only the [[crossplatform_app_development_with_flutter | Flutter]] SDK as a dependency, and adding new ones automatically updates them on save <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

## [[dart_vs_javascript_programming_languages | Dart]] vs. [[dart_vs_javascript_programming_languages | JavaScript]] Programming Languages

Learning [[crossplatform_app_development_with_flutter | Flutter]] requires learning [[dart_vs_javascript_programming_languages | Dart]], but it shares many conventions with [[dart_vs_javascript_programming_languages | JavaScript]] <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.

### Entry Point
*   In [[dart_vs_javascript_programming_languages | Dart]], the `main` function is the app's entry point where execution begins <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
*   [[dart_vs_javascript_programming_languages | JavaScript]] doesn't have a direct equivalent; typically, a function is exported and called by a library consumer <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

### Variable Declaration
*   **Mutable Variables**: In [[dart_vs_javascript_programming_languages | Dart]], you start with a type annotation (e.g., `String`) to declare a reassignable variable <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. `print` is used for logging, similar to `console.log` in [[dart_vs_javascript_programming_languages | JavaScript]] <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>. In [[dart_vs_javascript_programming_languages | JavaScript]], `let` is used <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>.
*   **Single Assignment Variables**: [[dart_vs_javascript_programming_languages | JavaScript]] uses `const` <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. [[dart_vs_javascript_programming_languages | Dart]] uses `final` for single assignment, while its `const` keyword makes entire data structures immutable (like `Object.freeze` in [[dart_vs_javascript_programming_languages | JavaScript]]) <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
*   **Type Flexibility**: [[dart_vs_javascript_programming_languages | Dart]] has a sound type system but also flexibility. The `var` keyword allows [[dart_vs_javascript_programming_languages | Dart]] to implicitly infer the type <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
*   **Dynamic Type**: [[dart_vs_javascript_programming_languages | Dart]] has a `dynamic` type, akin to TypeScript's `any` type, useful for data from external sources with unknown shapes <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

### Imports and Exports
*   In [[dart_vs_javascript_programming_languages | JavaScript]], modules often use `export` to expose values and `import` to bring them in, which can lead to "boilerplate" management issues with many imports <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.
*   In [[dart_vs_javascript_programming_languages | Dart]], explicit `export` statements are often unnecessary; variables declared in a file are available by default upon `import` <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. Strong typing and tooling provide auto-completion <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.

### Functions
*   [[dart_vs_javascript_programming_languages | Dart]] functions are similar to [[dart_vs_javascript_programming_languages | JavaScript]] functions, but without the `function` keyword <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.
*   Type annotations come *before* the function name in [[dart_vs_javascript_programming_languages | Dart]], unlike TypeScript <a class="yt-timestamp" data-t="06:33:00">[06:33:00]</a>.
*   Both anonymous functions, arrow functions, and higher-order functions are supported with similar syntax <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.

### Object-Oriented Programming (OOP)
*   **Inheritance**: [[dart_vs_javascript_programming_languages | Dart]] supports mixin-based inheritance, meaning a class has one superclass but its body can be used in multiple classes for behavior-based composition <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. [[dart_vs_javascript_programming_languages | JavaScript]] classes are syntactic sugar over prototype inheritance <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>.
*   **Class Definition and Instantiation**: Syntax for defining classes with the `class` keyword is very similar <a class="yt-timestamp" data-t="07:26:00">[07:26:00]</a>. In [[dart_vs_javascript_programming_languages | Dart]], the `new` keyword is optional when instantiating a class, leading to cleaner code <a class="yt-timestamp" data-t="07:35:00">[07:35:00]</a>.
*   **Constructors**: In [[dart_vs_javascript_programming_languages | JavaScript]], arguments are passed to a `constructor` method and initialized to `this` context <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>. TypeScript offers a more concise way by annotating input variables as private or public <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. [[dart_vs_javascript_programming_languages | Dart]] provides an even cleaner way to construct an object by just calling the class as a function <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Public/Private Members**: By default, everything in [[dart_vs_javascript_programming_languages | Dart]] is public. To make something private to a library or class, an underscore is added to the beginning of its name <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>.
*   **Named Constructors**: [[dart_vs_javascript_programming_languages | Dart]] allows defining multiple constructors with different initialization logic by naming them after the class name <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>.

### Lists and Maps
*   **Lists**: [[dart_vs_javascript_programming_languages | Dart]]'s `List` is equivalent to a [[dart_vs_javascript_programming_languages | JavaScript]] array <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. It supports type annotations and has built-in methods like `forEach`, `map`, and `reduce`, along with useful properties like `last` <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.
*   **Maps**: [[dart_vs_javascript_programming_languages | Dart]]'s `Map` combines features of [[dart_vs_javascript_programming_languages | JavaScript]] objects and `Map` objects <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>. Keys in a [[dart_vs_javascript_programming_languages | Dart]] Map are strongly typed, allowing any type (e.g., classes or class instances) to be used as a key <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Asynchronous Programming
*   **Futures vs. Promises**: [[dart_vs_javascript_programming_languages | JavaScript]] uses Promises for asynchronous operations, while [[dart_vs_javascript_programming_languages | Dart]] uses Futures <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. Futures work "exactly like a promise," supporting `async`/`await` and `.then()` or `.catchError()` for handling resolved values or errors <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
*   **Streams**: [[dart_vs_javascript_programming_languages | Dart]] provides a `Stream` data structure for handling multiple asynchronous values over time, similar to observables in libraries like RxJS or MobX in [[dart_vs_javascript_programming_languages | JavaScript]] <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>. Streams can be iterated using an `await for` loop for more readable code, or subscribed to using the `.listen()` method <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

## [[building_user_interfaces_with_flutter_widgets | Building User Interfaces with Flutter Widgets]]

[[crossplatform_app_development_with_flutter | Flutter]]'s approach to UI development takes inspiration from [[comparing_flutter_to_react_native_and_ionic | React]] <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>.

### Styling Stateless Widgets
*   In [[react_native_vs_flutter_comparison | React Native]], a `render` function returns components resembling HTML <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>. Styles are applied via a `style` property, allowing multiple styles in an array to be merged from left to right <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.
*   In [[crossplatform_app_development_with_flutter | Flutter]], the structure is similar, but instead of HTML-like elements, you instantiate objects <a class="yt-timestamp" data-t="12:12:00">[12:12:00]</a>. Due to the optional `new` keyword, it looks like calling functions <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>. All UI rendering occurs within the `build` method, which is equivalent to [[comparing_flutter_to_react_native_and_ionic | React]]'s `render` <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>.

### State Management with [[building_user_interfaces_with_flutter_widgets | Stateful Widgets]]
*   [[react_native_vs_flutter_comparison | React Native]] [[building_user_interfaces_with_flutter_widgets | components]] have a `setState` method that re-renders them when called with state changes <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>.
*   [[crossplatform_app_development_with_flutter | Flutter]] has an exact equivalent in its [[building_user_interfaces_with_flutter_widgets | Stateful Widget]] <a class="yt-timestamp" data-t="12:46:00">[12:46:00]</a>.
*   While `setState` is viable, calling it frequently in both [[crossplatform_app_development_with_flutter | Flutter]] and [[comparing_flutter_to_react_native_and_ionic | React]] doesn't scale well, often leading to the implementation of state management solutions like Redux <a class="yt-timestamp" data-t="12:53:00">[12:53:00]</a>.
*   [[crossplatform_app_development_with_flutter | Flutter]] also introduces "builders" which allow working with asynchronous data sources (like Streams) and automatically rendering the UI <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. This concept is similar to Angular's async pipe, where the UI listens to a stream and re-renders based on its value <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>.