---
title: Comparing Flutter to React Native and Ionic
videoId: 7sJZi0grFR4
---

From: [[fireship]] <br/> 

For [[react_native_programming_languages_and_ecosystem | JavaScript]] developers building native mobile apps, [[react_native_programming_languages_and_ecosystem | JavaScript]] has historically been a popular choice via frameworks like [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]], Cordova, or [[react_native_vs_flutter_comparison | React Native]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, [[introduction_to_flutter_for_javascript_developers | Flutter]] has emerged as a strong contender due to its developer experience and app quality <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This article aims to compare [[introduction_to_flutter_for_javascript_developers | Flutter]] with [[react_native_vs_flutter_comparison | React Native]] and [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]], particularly from a [[react_native_programming_languages_and_ecosystem | JavaScript]] developer's perspective <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Key Considerations and Trade-offs

Choosing a framework always involves trade-offs <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Learning Curve
*   **[[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] / [[react_native_vs_flutter_comparison | React Native]]**: As a web or [[react_native_programming_languages_and_ecosystem | JavaScript]] developer, you can jump into these projects with virtually no learning curve <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: There is a learning curve, but it is considered "pretty gentle" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Learning [[introduction_to_flutter_for_javascript_developers | Flutter]] means learning [[introduction_to_flutter_for_javascript_developers | Dart]], its programming language <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Community Size & Talent Acquisition
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]] frameworks**: The [[react_native_programming_languages_and_ecosystem | JavaScript]] community is vast, with many new developers entering the field daily, making it easier to find talent <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Companies often use hybrid frameworks to save time and money <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Performance
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: [[introduction_to_flutter_for_javascript_developers | Dart]] is an ahead-of-time compiled language <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Its engine is written in C++ <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, allowing it to perform better than a [[react_native_programming_languages_and_ecosystem | JavaScript]] bridge when making numerous callbacks to the native system <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Development Experience
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: Offers hot reloads during development <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> and some of the best documentation for any framework <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. It can also integrate existing native code <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **[[react_native_vs_flutter_comparison | React Native]]**: Also supports hot reloading, which significantly impacts development productivity <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Project Structure Comparison

This comparison uses a baseline app with three bottom tabs switching between screens <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### [[react_native_vs_flutter_comparison | React Native]] Project Structure
*   Components combine styles, templating, and [[react_native_programming_languages_and_ecosystem | JavaScript]] logic in a single file <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Dependencies are managed with [[react_native_programming_languages_and_ecosystem | NPM]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   The three-tab layout example required about ten different [[react_native_programming_languages_and_ecosystem | JavaScript]] files <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. It largely resembles a regular [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]] app with special components for native UI rendering <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] Project Structure
*   Typically has more files, primarily because [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Angular]] separates templates and CSS into isolated files <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   While separating concerns, this can be overwhelming for new users, especially without [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Angular]] knowledge <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] 4 uses web components, allowing it to be used with any framework <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### [[introduction_to_flutter_for_javascript_developers | Flutter]] Project Structure
*   Less complex than [[react_native_programming_languages_and_ecosystem | JavaScript]] counterparts <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   Often a single `main.dart` file serves as the entry point <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   The three-tab layout example was built with only 45 lines of code, with no `import`/`export` headaches or boilerplate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Apps can be run directly from the command line, without needing special app store downloads or browser debugging <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Changes can be hot-reloaded by typing `R` on the command line, preserving the app's state <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   Dependencies are managed in `pubspec.yaml`, similar to `package.json` <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The [[introduction_to_flutter_for_javascript_developers | Flutter]] SDK is the initial dependency, and additions automatically update on save <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## [[introduction_to_flutter_for_javascript_developers | Dart]] Programming Language vs. [[react_native_programming_languages_and_ecosystem | JavaScript]] / [[react_native_programming_languages_and_ecosystem | TypeScript]]

[[introduction_to_flutter_for_javascript_developers | Dart]] shares many conventions with [[react_native_programming_languages_and_ecosystem | JavaScript]], making it relatively easy for [[react_native_programming_languages_and_ecosystem | JavaScript]] developers to become productive <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Entry Point
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: The main entry point is the `main` function, where the app begins execution <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Lacks a direct equivalent; typically exports a function called by a library consumer <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Variable Declaration
*   **Mutable Variables**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Declare with a type annotation (e.g., `String myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Use `print()` to log values <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Use `let` (e.g., `let myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Type annotations can be appended in [[react_native_programming_languages_and_ecosystem | TypeScript]] <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Single Assignment / Immutable Variables**:
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Use `const` (e.g., `const myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Use `final` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The `const` keyword in [[introduction_to_flutter_for_javascript_developers | Dart]] makes an entire data structure (like an array or map) completely immutable, similar to `Object.freeze` in [[react_native_programming_languages_and_ecosystem | JavaScript]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Type Flexibility**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Has a sound type system but is flexible. `var` implicitly infers the type <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The `dynamic` type is similar to [[react_native_programming_languages_and_ecosystem | TypeScript]]'s `any` type, useful for external data with unknown shapes <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Importing & Exporting
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Uses `export default` for single values or braced exports for multiple <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Imports are explicit, which can lead to boilerplate and mental overhead <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: No explicit `export` is needed.# Comparing [[crossplatform_app_development_with_flutter | Flutter]] to [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | React Native]] and [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]]

For [[react_native_programming_languages_and_ecosystem | JavaScript]] developers building native mobile apps, [[react_native_programming_languages_and_ecosystem | JavaScript]] has historically been a popular choice via frameworks like [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]], Cordova, or [[react_native_vs_flutter_comparison | React Native]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, [[introduction_to_flutter_for_javascript_developers | Flutter]] has emerged as a strong contender due to its developer experience and app quality <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This article aims to compare [[introduction_to_flutter_for_javascript_developers | Flutter]] with [[react_native_vs_flutter_comparison | React Native]] and [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]], particularly from a [[react_native_programming_languages_and_ecosystem | JavaScript]] developer's perspective <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Key Considerations and Trade-offs

Choosing a framework always involves trade-offs <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Learning Curve
*   **[[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] / [[react_native_vs_flutter_comparison | React Native]]**: As a web or [[react_native_programming_languages_and_ecosystem | JavaScript]] developer, you can jump into these projects with virtually no learning curve <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: There is a learning curve, but it is considered "pretty gentle" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Learning [[introduction_to_flutter_for_javascript_developers | Flutter]] means learning [[introduction_to_flutter_for_javascript_developers | Dart]], its programming language <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Community Size & Talent Acquisition
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]] frameworks**: The [[react_native_programming_languages_and_ecosystem | JavaScript]] community is vast, with many new developers entering the field daily, making it easier to find talent <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Companies often use hybrid frameworks to save time and money <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Performance
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: [[introduction_to_flutter_for_javascript_developers | Dart]] is an ahead-of-time compiled language <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. Its engine is written in C++ <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, allowing it to perform better than a [[react_native_programming_languages_and_ecosystem | JavaScript]] bridge when making numerous callbacks to the native system <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Development Experience
*   **[[introduction_to_flutter_for_javascript_developers | Flutter]]**: Offers hot reloads during development <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> and some of the best documentation for any framework <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. It can also integrate existing native code <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **[[react_native_vs_flutter_comparison | React Native]]**: Also supports hot reloading, which significantly impacts development productivity <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Project Structure Comparison

This comparison uses a baseline app with three bottom tabs switching between screens <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### [[react_native_vs_flutter_comparison | React Native]] Project Structure
*   Components combine styles, templating, and [[react_native_programming_languages_and_ecosystem | JavaScript]] logic in a single file <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Dependencies are managed with [[react_native_programming_languages_and_ecosystem | NPM]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   The three-tab layout example required about ten different [[react_native_programming_languages_and_ecosystem | JavaScript]] files <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>. It largely resembles a regular [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]] app with special components for native UI rendering <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] Project Structure
*   Typically has more files, primarily because [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Angular]] separates templates and CSS into isolated files <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   While separating concerns, this can be overwhelming for new users, especially without [[differences_and_simila|Angular]] knowledge <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   [[comparison_of_mobile_app_frameworks_ionic_react_native_and_flutter | Ionic]] 4 uses web components, allowing it to be used with any framework <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### [[introduction_to_flutter_for_javascript_developers | Flutter]] Project Structure
*   Less complex than [[react_native_programming_languages_and_ecosystem | JavaScript]] counterparts <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   Often a single `main.dart` file serves as the entry point <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   The three-tab layout example was built with only 45 lines of code, with no `import`/`export` headaches or boilerplate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   Apps can be run directly from the command line, without needing special app store downloads or browser debugging <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   Changes can be hot-reloaded by typing `R` on the command line, preserving the app's state <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
*   Dependencies are managed in `pubspec.yaml`, similar to `package.json` <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. The [[introduction_to_flutter_for_javascript_developers | Flutter]] SDK is the initial dependency, and additions automatically update on save <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## [[introduction_to_flutter_for_javascript_developers | Dart]] Programming Language vs. [[react_native_programming_languages_and_ecosystem | JavaScript]] / [[react_native_programming_languages_and_ecosystem | TypeScript]]

[[introduction_to_flutter_for_javascript_developers | Dart]] shares many conventions with [[react_native_programming_languages_and_ecosystem | JavaScript]], making it relatively easy for [[react_native_programming_languages_and_ecosystem | JavaScript]] developers to become productive <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Entry Point
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: The main entry point is the `main` function, where the app begins execution <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Lacks a direct equivalent; typically exports a function called by a library consumer <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Variable Declaration
*   **Mutable Variables**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Declare with a type annotation (e.g., `String myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Use `print()` to log values <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Use `let` (e.g., `let myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. Type annotations can be appended in [[react_native_programming_languages_and_ecosystem | TypeScript]] <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Single Assignment / Immutable Variables**:
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Use `const` (e.g., `const myVar = 'value'`) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Use `final` <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The `const` keyword in [[introduction_to_flutter_for_javascript_developers | Dart]] makes an entire data structure (like an array or map) completely immutable, similar to `Object.freeze` in [[react_native_programming_languages_and_ecosystem | JavaScript]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Type Flexibility**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Has a sound type system but is flexible. `var` implicitly infers the type <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The `dynamic` type is similar to [[react_native_programming_languages_and_ecosystem | TypeScript]]'s `any` type, useful for external data with unknown shapes <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Importing & Exporting
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Uses `export default` for single values or braced exports for multiple <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. Imports are explicit, which can lead to boilerplate and mental overhead <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: No explicit `export` is needed. If a variable is declared in a `.dart` file and imported elsewhere, it's available by default <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Strong typing and good tooling enable IntelliSense auto-completion <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Functions
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Functions feel similar to [[react_native_programming_languages_and_ecosystem | JavaScript]], but without the `function` keyword <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Type annotations come *before* the function name (unlike [[react_native_programming_languages_and_ecosystem | TypeScript]]) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Supports anonymous functions, arrow functions, and higher-order functions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Object-Oriented Programming (OOP)
*   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Supports mixin-based inheritance, meaning a class has one superclass but its body can be used in multiple classes, enabling behavior-based composition <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Classes are largely syntactic sugar for prototype inheritance <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Syntax**: Both use the `class` keyword <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Instantiation**:
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Uses the `new` keyword (e.g., `new MyClass()`) <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: The `new` keyword is optional, leading to cleaner code when instantiating many objects <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Constructors**:
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Arguments are passed and initialized on `this` context <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. [[react_native_programming_languages_and_ecosystem | TypeScript]] offers a more concise way by annotating input variables as private/public <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Provides a cleaner way by just calling the class as a function <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Public/Private Members**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Members are public by default. Adding an underscore (`_`) to the beginning of a name makes it private to the library or class <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Named Constructors**: [[introduction_to_flutter_for_javascript_developers | Dart]] supports named constructors to provide different initialization logic as needed, implemented as a method name on the class name itself <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Data Structures
*   **Lists ([[react_native_programming_languages_and_ecosystem | JavaScript]] Arrays)**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Create with type annotation (e.g., `List<int> numbers = [...]`) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Lists have built-in methods like `forEach`, `map`, `reduce`, and a `last` property to get the last element <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Maps ([[react_native_programming_languages_and_ecosystem | JavaScript]] Objects/Maps)**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: The `Map` type combines features of [[react_native_programming_languages_and_ecosystem | JavaScript]] objects and maps <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Keys can be strongly typed and can be anything (e.g., a class or instance) <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Asynchronous Programming
*   **Promises (in [[react_native_programming_languages_and_ecosystem | JavaScript]]) vs. Futures (in [[introduction_to_flutter_for_javascript_developers | Dart]])**:
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: `async` functions return Promises <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. `await` pauses execution until the Promise resolves <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. `.then()` and `.catch()` handle resolved values or errors <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Uses `Future` objects, which work exactly like Promises <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. `async` functions return Futures, and `await` is used similarly <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. `.then()` and `.catchError()` are equivalent <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Streams (in [[introduction_to_flutter_for_javascript_developers | Dart]]) vs. [[react_native_programming_languages_and_ecosystem | Observables]] (in [[react_native_programming_languages_and_ecosystem | JavaScript]] libraries like [[react_native_programming_languages_and_ecosystem | RxJS]])**:
    *   **[[introduction_to_flutter_for_javascript_developers | Dart]]**: Has a `Stream` data structure for handling multiple asynchronous values <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Supports `await for` loops for iterating over changing objects, leading to more readable code <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Also allows `listen` (similar to `subscribe`) to a stream <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   **[[react_native_programming_languages_and_ecosystem | JavaScript]]**: Vanilla [[react_native_programming_languages_and_ecosystem | JavaScript]] lacks a direct equivalent, but libraries like [[react_native_programming_languages_and_ecosystem | RxJS]] and MobX provide [[react_native_programming_languages_and_ecosystem | Observables]] <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. `subscribe()` is used to listen to values <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

In many ways, [[introduction_to_flutter_for_javascript_developers | Dart]] is very similar to [[react_native_programming_languages_and_ecosystem | JavaScript]], perhaps a little smoother around the edges <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

## Building Components / Widgets

### Styling and Merging Styles
*   **[[react_native_vs_flutter_comparison | React Native]]**: Implements a `render` function that returns components resembling HTML <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. Styles are applied via a `style` property, with styles in an array applied from left to right, allowing merging <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **[[building_mobile_app_components_with_flutter | Flutter]]**: Overall structure is similar, but it involves instantiating objects (widgets) <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The absence of the `new` keyword makes it look like function calls <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. All rendering occurs within the `build` method, equivalent to [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]]'s `render` <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. [[building_mobile_app_components_with_flutter | Flutter]] drew significant inspiration from [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]] <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### State Management
*   **[[react_native_vs_flutter_comparison | React Native]]**: Components feature a `setState` method to re-render when state changes <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **[[building_mobile_app_components_with_flutter | Flutter]]**: Has the exact same `setState` mechanism on what is called a "stateful widget" <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Scaling State**: In both [[introduction_to_flutter_for_javascript_developers | Flutter]] and [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | React]], frequent `setState` calls do not scale well, often necessitating state management solutions like [[performance_and_developer_experience_in_react_native_and_flutter | Redux]] <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   **Builders in [[introduction_to_flutter_for_javascript_developers | Flutter]]**: [[introduction_to_flutter_for_javascript_developers | Flutter]] also offers "builders," which allow working with asynchronous data sources and automatically rendering the UI <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. These are conceptually similar to [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | Angular]]'s async pipe; you tell the UI to listen to a stream and re-render different widgets based on its value <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>.

Overall, [[introduction_to_flutter_for_javascript_developers | Flutter]] presents a compelling alternative, especially for [[react_native_programming_languages_and_ecosystem | JavaScript]] developers seeking a refreshed development experience <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.