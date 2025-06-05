---
title: JavaScript frameworks and their updates
videoId: f0DrPLKf6Ro
---

From: [[fireship]] <br/> 

Making predictions about the future of [[JavaScript and Frontend Development | JavaScript]] is challenging, especially for developers who spend their careers in this evolving field <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The landscape of [[JavaScript trends and frameworks | JavaScript frameworks]] and tools is constantly shifting, with new features and disruptive trends emerging regularly <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## New JavaScript Language Features

Several new features are being introduced to the JavaScript language, many of which were slated for publication in 2020 but are already available in browsers, Node.js, and TypeScript <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. These features enhance performance, code robustness, and developer experience:

*   **Dynamic Imports**: This function allows modules to be imported lazily at runtime, meaning imports no longer need to be static at the top of a file <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This feature enables asynchronous loading of modules, which can improve application performance by delaying non-essential dependencies <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Optional Chaining**: Also known as the Elvis operator, this feature allows calling a deeply nested object property without throwing an error if its parent property is undefined <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. It serves as a useful replacement for functions like Lodash's `get` when working with deeply nested objects from APIs or databases <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Nullish Coalescing Operator (`??`)**: Similar to optional chaining, this operator provides a more predictable way to set default values for properties <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Unlike the logical OR (`||`) operator, `??` treats only `null` or `undefined` as "falsy" values, preventing issues with `0` or empty strings being coerced to `false` <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   **BigInt**: JavaScript is gaining a new primitive data type, `BigInt`, which can represent numbers beyond JavaScript's maximum safe integer value (limited to 64 bits) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. While not needed by most developers, it's useful for extremely precise timestamps or geometric calculations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Key Trends and Disruptions

### TypeScript
[[Comparison of popular JavaScript frameworks in 2021 | TypeScript]] has emerged as a major disruptive force in the [[JavaScript trends and frameworks | JavaScript]] world since its appearance on the 2016 Stack Overflow survey <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. By 2019, it became a top ten language, used by over 20% of developers <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. It is widely embraced by both front-end and back-end developers across various frameworks <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Web Components
Although a previous prediction for widespread adoption in 2019 did not fully materialize, web components have seen increased adoption and continue to be supported by dedicated tools like Stencil and Lit Element (a Google-sponsored project) <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Frontend Framework Landscape

The [[comparison_of_popular_javascript_frameworks_in_2021 | landscape of frontend frameworks]] continues to evolve with significant updates to major players and the rise of new contenders.

### Svelte
Svelte was a notable "underdog" in 2019, especially with the release of Svelte 3 in April 2019 <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. It gained excitement for its elegant and easy-to-learn package, high performance, and lack of runtime dependencies <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. Svelte's npm downloads roughly tripled in the year leading up to 2020 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Comparison of Popular Frameworks: React, Angular, and Vue
In terms of adoption, React remains the dominant force, boasting more than twice the npm downloads compared to Angular and Vue combined <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. Job market data from Stack Overflow also reflects React's lead, with significantly more openings than Angular and Vue <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

#### React Updates
Following the introduction of Hooks, React introduced another significant experimental feature: Concurrent Mode <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This mode allows the framework to handle multiple state updates simultaneously and paves the way for a new built-in component called Suspense <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Suspense will wait for asynchronous activities, such as API calls or lazy loading of React components using [[dynamic_imports | dynamic imports]], allowing for declarative handling of loading states without manual boolean toggles <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

#### Angular Updates
The major update in the Angular ecosystem is Ivy, an entirely new compiler enabled by default in Angular 9 <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Additionally, a static site generator for Angular was released in alpha, allowing for [[comparison_with_other_javascript_frameworks | comparison]] with existing tools like Gatsby and VuePress <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

#### Vue Updates
Vue introduced the Composition API, a set of tools designed to improve code reusability in complex Vue applications <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This API exposes Vue's core capabilities, such as reactive state, as functions, enabling the composition of more complex components that are also easier to strongly type with TypeScript <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

## Broader Web Development Trends

### Web Platform Features
Beyond frameworks, the web platform itself has gained new features that extend the types of applications that can be built:

*   **Web Authentication API (WebAuthn)**: Enables web applications to utilize hardware-based authenticators for features like biometric authentication <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   **Native File System API**: Can grant web applications access to a user's local files, a long-desired capability for web developers <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. This is currently available in Chrome with a flag <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **`loading` attribute for images and iframes**: Provides native browser support for lazy loading, simplifying a common performance optimization previously handled by JavaScript libraries <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Node.js and Backend Development
Node.js has also seen significant advancements:

*   **Worker Threads**: Addresses the single-threaded limitation of JavaScript by allowing parallel execution of JavaScript code in Node.js <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **ES Modules Support**: Node.js 13 introduced support for `import` and `export` statements, aligning with modern JavaScript module syntax <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

On the backend, NestJS is a fast-growing tool that leverages TypeScript to build scalable and developer-friendly server-side applications <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. GraphQL continues its growth trend as a query language for APIs <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Many modern web applications also opt for backend-as-a-service solutions like AWS Amplify and Firebase, which provide comprehensive tools for scaling mobile applications, allowing teams to focus on frontend user experience <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Mobile Application Development
In mobile app development, React Native, Ionic, and NativeScript remain prominent <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. While npm downloads for these have remained relatively flat, React Native has improved with features like fast refresh, and Ionic now supports React in addition to Angular <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## JavaScript Anti-Heroes: Alternatives and Complements

Emerging technologies offer alternatives to JavaScript for specific use cases:

*   **SwiftUI**: Released by Apple in June 2019, SwiftUI enables declarative UI building for iOS using the Swift programming language, aiming to improve the iOS developer experience <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Flutter**: A disruptive force for building cross-platform iOS and Android apps using the Dart programming language <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Dart was the fastest-growing programming language in 2019, and Flutter is a highly popular open-source project that now supports the web as a target in beta <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.
*   **WebAssembly**: Officially recognized as a fourth language on the web alongside JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. WebAssembly is a complement to JavaScript, enabling the creation of high-quality, high-performance web applications that rival desktop apps <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. Languages like C, C++, and Rust can compile to WebAssembly, and support is emerging for more languages, such as C# with Microsoft's Blazor framework <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, which allows building web applications using C#, HTML, and CSS through WebAssembly <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.

The [[emergence_of_frameworks_and_tools_in_modern_javascript | JavaScript ecosystem]] is dynamic, with tools like Cypress for testing, Gatsby for [[building_a_todo_app_with_different_javascript_frameworks | building web apps]], and XState for state management continually changing how applications are developed <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.