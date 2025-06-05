---
title: Disruptive trends in the JavaScript ecosystem
videoId: f0DrPLKf6Ro
---

From: [[fireship]] <br/> 

Predicting the future, especially that of JavaScript, is challenging, yet crucial for developers who will spend their careers within its evolving landscape <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores new language features, the state of front-end frameworks, and disruptive trends that are reshaping the JavaScript ecosystem in 2020 and beyond <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## [[New JavaScript features in 2020 | New JavaScript Features in 2020]]

New features are introduced to JavaScript through the Technical Committee 39 (TC39) process, with proposals making their way into the language <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. In 2020, eight finished proposals were slated for publication, many already shipped to browsers, Node.js, and TypeScript <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

Key additions include:

*   **Dynamic Imports**
    *   Allows lazy import of modules at runtime, meaning imports don't have to be static at the top of a file <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Modules can be loaded asynchronously, delaying non-essential dependencies to improve performance <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Optional Chaining (`?.`)**
    *   Referred to as the "Elvis operator," this feature enables accessing deeply nested object properties without throwing an error if an intermediate parent property is undefined <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   It's useful when working with APIs or databases returning deeply nested objects, preventing runtime errors <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Nullish Coalescing Operator (`??`)**
    *   Provides a way to set a default value for a property specifically when it is `null` or `undefined` <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
    *   Unlike the logical OR (`||`) operator, which can be problematic with `0` or empty strings (as they are coerced to `false`), `??` only treats `null` and `undefined` as "falsy," leading to more predictable code <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **BigInt**
    *   A new primitive data type capable of representing numbers beyond JavaScript's `MAX_SAFE_INTEGER` (limited to 64 bits) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
    *   While not needed by most developers, it's crucial for extremely precise timestamps or geometric calculations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Disruptive Technologies and Trends

### TypeScript

TypeScript has seen remarkable growth, evolving from less than 0.5% developer usage in 2016 to over 20% in 2019, making it a top ten language <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. It is widely adopted and well-regarded by both front-end and back-end developers across various frameworks <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Web Components

While predicted to have a significant year in 2019, [[web_components | Web Components]] saw limited adoption and faced criticism <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. However, tools like Stencil and Lit Element (a Google-sponsored project) are dedicated to building them and have been gaining traction <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Front-End Frameworks

[[JavaScript frameworks and their updates | JavaScript frameworks]] continue to evolve, with key updates and trends:

*   **Svelte**
    *   An "underdog" of 2019, Svelte 3 was released in April 2019, generating excitement for its elegant, easy-to-learn package and high performance with no runtime dependencies <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
    *   Its npm downloads tripled over the last year <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **React**
    *   Remains the dominant force in terms of adoption, with more than twice the npm downloads of Angular and Vue combined <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   A significant experimental feature is **Concurrent Mode**, allowing the framework to handle multiple state updates simultaneously <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   This opens the door for **Suspense**, a built-in React component that waits for asynchronous activity (like API calls or lazy loading components via Dynamic Imports) to finish, enabling declarative loading states <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   **Angular**
    *   The major update is **Ivy**, an entirely new compiler enabled by default in Angular 9 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
    *   A static site generator for Angular is also under development, expected to be released in alpha soon <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
*   **Vue**
    *   A key new feature is the **Composition API**, a set of tools designed to improve code reusability in complex Vue applications <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
    *   It exposes core Vue capabilities like reactive state as functions, allowing for more complex components and better strong typing with TypeScript <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### Web Platform Features

The web platform itself is gaining new features that fundamentally extend the types of applications possible:

*   **Web Authentication API (WebAuthn)**: Enables web applications to use hardware-based authenticators, including biometric authentication <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Native File System API**: Gives web applications access to a user's local files, a long-desired feature for web developers <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. It's available in Chrome with a flag <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **`loading` attribute for images and iframes**: Provides native browser-level lazy loading for these elements with a simple HTML attribute, reducing reliance on JavaScript libraries <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Brave Browser

Brave is a disruptive new browser that blocks ads and trackers by default, making it faster <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Its CEO is Brendan Eich, the creator of JavaScript <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. It offers a Chrome-like experience and supports Chrome extensions <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Node.js and Backend Trends

Node.js, as a server-side JavaScript runtime, has also seen significant developments:

*   **Worker Threads**: A module that overcomes the single-threaded limitation of JavaScript, allowing for parallel execution of JavaScript code using threads <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **ES Modules Support**: Node 13 supports `import` and `export` statements, aligning with modern JavaScript module syntax <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **NestJS**: A fast-growing backend tool for Node.js that leverages TypeScript to build scalable and developer-friendly server-side applications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **GraphQL**: This trend continues to grow, offering an efficient and powerful way to query APIs <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Backend as a Service (BaaS)**: Tools like AWS Amplify and Firebase continue to grow, providing comprehensive backend services that allow development teams to focus primarily on the front-end user experience <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Mobile Development (JavaScript-based)

*   **React Native**, Ionic, and NativeScript remain the primary options for mobile development using JavaScript <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   React Native has added improvements like fast refresh, and Ionic now supports React in addition to Angular <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. However, overall growth in this sector has been relatively flat <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

## JavaScript Anti-Heroes: Emerging Alternatives

Several technologies are emerging as alternatives or complements to JavaScript, allowing developers to "place their bets" elsewhere:

*   **SwiftUI**: Released by Apple in June 2019, SwiftUI offers a declarative UI approach similar to React, but using the Swift programming language for iOS development, promising an improved developer experience for Apple platforms <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Flutter**: A significant disruptive force for cross-platform app development (iOS and Android) <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. It uses the Dart programming language, which is syntactically similar to JavaScript <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Dart was the fastest-growing programming language in 2019, and Flutter is a hot open-source project, now supporting the web as a beta target <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **WebAssembly (Wasm)**: Became an official fourth language on the web (alongside JavaScript, HTML, and CSS) <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. WebAssembly is a complement to JavaScript, enabling the creation of higher-quality applications that can rival desktop apps <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
    *   **Case Study: Figma**: Figma utilizes a React shell with its high-performance design tool powered by WebAssembly <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   **Language Support**: Languages like C, C++, and Rust can compile to Wasm, and more are emerging, such as C# <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   **Blazor**: Microsoft's new framework, partly via WebAssembly, allows building web applications using C#, HTML, and CSS <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

## Other Notable Tools

The JavaScript world is vast and includes tools that are changing specific aspects of development:

*   **Cypress**: For testing applications <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Gatsby**: For building [[javascript_trends_and_frameworks | JavaScript]] applications, particularly static sites <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
*   **XState**: For state management, offering new ways to conceptualize application states <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.

Despite the rapid evolution and [[emergence_of_frameworks_and_tools_in_modern_javascript | disruptive trends]], the core message for developers remains: "always bet on JavaScript" <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.