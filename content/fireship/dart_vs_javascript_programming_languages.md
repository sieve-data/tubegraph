---
title: Dart vs JavaScript Programming Languages
videoId: 7sJZi0grFR4
---

From: [[fireship]] <br/> 

This article compares Dart and JavaScript, two programming languages used for building applications, with a focus on their differences and similarities from the perspective of a JavaScript developer. The comparison highlights various language features, project structures, and development experiences.

## Overview and Trade-offs

For developers passionate about building for the web, JavaScript has historically been the preferred tool for native mobile apps via frameworks like Ionic, Cordova, or React Native <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. However, Dart, especially with Flutter, has shown impressive developer experience and app quality <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

When considering Dart versus JavaScript frameworks for mobile development, there are several [[Tradeoffs of JavaScript frameworks | trade-offs]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>:

*   **Learning Curve**: A JavaScript developer can typically jump into an Ionic or React Native project without a significant learning curve <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Learning Dart, however, introduces a new programming language, though it is described as "pretty gentle" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Community Size**: The JavaScript community is significantly larger, with many new developers entering the field regularly, making it easier to find talent for projects <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Performance**: Dart is an ahead-of-time (AOT) compiled language with its engine written in C++ <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This allows it to perform better than a JavaScript bridge, especially when making numerous callbacks to the native system <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Dart can also integrate existing native code <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Developer Experience**: Dart supports hot reloads during development, similar to React Native, which significantly impacts productivity <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Dart also boasts extensive documentation <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Project Structure Comparison

Comparing a basic three-tab layout application:

*   **React Native**: Components combine styles, templating, and JavaScript logic in a single file <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Dependencies are managed with NPM, and a typical three-tab layout might involve about ten different JavaScript files <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Ionic (Angular)**: Often involves more files due to Angular separating templates and CSS into isolated files, which helps [[tradeoffs_of_javascript_frameworks | separate concerns]] but can be overwhelming for newcomers <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. Ionic 4 uses web components, allowing use with any framework <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Flutter (Dart)**: Features a simpler structure, often with a single `main.dart` file as the entry point <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. A three-tab layout can be built with minimal lines of code (e.g., 45 lines) with no import/export headaches or boilerplate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Dependencies are managed via `pubspec.yaml`, similar to `package.json` <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

## Language Syntax Comparison

Dart shares many conventions with JavaScript, making the transition relatively smooth for JavaScript developers <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. The following compares Dart syntax side-by-side with TypeScript (which is mostly vanilla JavaScript).

### Entry Point
*   **Dart**: The application starts executing at the `main` function <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **JavaScript**: Doesn't have a direct equivalent concept; typically, a function is exported and called by a library consumer <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Variables and Types
*   **Reassignable Variables**:
    *   **Dart**: Declared with a type annotation (e.g., `String myVar = "hello";`) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. Can be logged using `print()` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
    *   **JavaScript**: Uses `let` (e.g., `let myVar = "hello";`) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Types can be appended in TypeScript <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Logging uses `console.log()` <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Single-Assignment (Immutable) Variables**:
    *   **Dart**: Uses the `final` keyword (e.g., `final String myVar = "value";`) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The `const` keyword in Dart makes an entire data structure (like an array or map) completely immutable, similar to `Object.freeze` in JavaScript <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
    *   **JavaScript**: Uses `const` (e.g., `const myVar = "value";`) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Type System Flexibility**:
    *   **Dart**: Has a sound type system but is flexible. The `var` keyword allows Dart to implicitly infer the type <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The `dynamic` type is similar to TypeScript's `any` type, useful for external data with unknown shapes <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Imports and Exports
*   **Dart**: Doesn't require explicit `export` statements. If a variable is declared in a file, it's available for import in other files by default <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Strong typing and tooling enable auto-completion <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **JavaScript**: Relies on `import` and `export` statements (e.g., ES6 modules), which can lead to "boilerplate" and mental overhead when managing many dependencies <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Functions
*   **Dart**: Functions feel similar to JavaScript, but without the `function` keyword <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Type annotations for return types come before the function name <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. Supports anonymous arrow functions and higher-order functions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.
*   **JavaScript**: Uses the `function` keyword, and type annotations in TypeScript come after the name <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Supports arrow functions and higher-order functions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

### Object-Oriented Programming (OOP)
*   **Dart**: Supports mixin-based inheritance, allowing a class to have one superclass but use the body of multiple classes for behavior-based composition <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **JavaScript**: Classes are syntactic sugar for prototype inheritance <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Class Instantiation**:
    *   **Dart**: Instantiated by calling the class with parentheses (e.g., `MyClass()`); the `new` keyword is optional, leading to cleaner code <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   **JavaScript**: Instantiated using the `new` keyword (e.g., `new MyClass()`) <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Constructors**:
    *   **Dart**: Offers a clean way to construct objects by calling the class as a function <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Also has "named constructors" to provide different initialization logic <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
    *   **JavaScript**: Constructors initialize properties on the `this` context <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. TypeScript offers a "sugary" way to annotate input variables as private/public for automatic assignment <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Access Modifiers**:
    *   **Dart**: Members are public by default. Adding an underscore (`_`) to the beginning of a member's name makes it private to the library or class <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   **JavaScript**: No built-in public/private keywords in vanilla JS.

### Data Structures

#### Lists (Arrays)
*   **Dart**: `List` is the equivalent of a JavaScript array <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. Lists have built-in methods like `forEach`, `map`, and `reduce` <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. A notable convenience is the `last` property to get the final element <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **JavaScript**: `Array` has similar built-in methods <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Getting the last element often requires `arr[arr.length - 1]` or methods like `pop()` <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

#### Maps (Objects)
*   **Dart**: `Map` combines features of JavaScript objects and maps <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. Keys in a Dart map are strongly typed, allowing for any type (e.g., class instances) as a key <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **JavaScript**: Plain objects use brace notation for key-value pairs <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. JavaScript Maps also allow any type as a key but have different syntax <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

### [[Asynchronous programming in JavaScript | Asynchronous Programming]]

Asynchronous programming is crucial in both languages <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

*   **Promises vs. Futures**:
    *   **Dart**: Uses `Future` objects, which work exactly like JavaScript promises <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Asynchronous functions return a `Future` by default, and `await` pauses execution until the `Future` resolves <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. `then` and `catchError` methods are available <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   **JavaScript**: Uses `Promise` objects. `async` functions automatically return a promise, and `await` pauses execution <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. `then` and `catch` methods handle resolved values and errors <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
*   **Streams vs. Observables**:
    *   **Dart**: Has a `Stream` data structure for handling multiple asynchronous values <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. Streams can be iterated with an `await for` loop for more readable code than chaining callbacks <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Similar to observables, you can `listen` to a stream for new values <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
    *   **JavaScript**: Vanilla JavaScript lacks a direct equivalent, but libraries like RxJS and MobX provide `Observables` for handling multiple asynchronous values <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. Observables are typically consumed by calling `subscribe` <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

## Conclusion

Dart is very similar to JavaScript in many ways, but with "smoother edges" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, particularly in its streamlined approach to object instantiation, explicit typing, and simplified module system. For JavaScript developers, learning Dart can be a pleasant and refreshing experience <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.